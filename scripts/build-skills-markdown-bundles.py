#!/usr/bin/env python3
"""
Baut pro Plugin ein ZIP-Bundle mit allen Skill-Markdown-Dateien (SKILL.md) und
Megaprompts. Diese ZIPs werden als Release-Assets unter
releases/latest/download/<plugin>-skills-markdown.zip veroeffentlicht, damit
echte Datei-Downloads moeglich sind (statt browser-rendered Markdown auf
GitHub).

Aufruf:
    python3 scripts/build-skills-markdown-bundles.py <output-dir>

Erzeugt:
    <output-dir>/<plugin>-skills-markdown.zip   (213 Stueck)
    <output-dir>/alle-skills-markdown.zip       (eines mit allen Plugins)
"""
import json
import sys
import zipfile
from pathlib import Path


def list_plugins(repo_root: Path) -> list[str]:
    """Lese die Plugin-Liste aus marketplace.json."""
    manifest = json.loads((repo_root / ".claude-plugin" / "marketplace.json").read_text())
    return sorted(p["name"] for p in manifest.get("plugins", []))


def collect_skill_files(plugin_dir: Path) -> list[Path]:
    """Alle SKILL.md unter <plugin>/skills/ einsammeln."""
    skills_dir = plugin_dir / "skills"
    if not skills_dir.is_dir():
        return []
    return sorted(skills_dir.glob("*/SKILL.md"))


def collect_megaprompt_files(plugin_dir: Path) -> list[Path]:
    """Megaprompts liegen in testakten/megaprompts/<plugin>/ — falls vorhanden."""
    repo_root = plugin_dir.parent
    mp_dir = repo_root / "testakten" / "megaprompts" / plugin_dir.name
    if not mp_dir.is_dir():
        return []
    return sorted(mp_dir.glob("*.md"))


def build_plugin_bundle(plugin: str, repo_root: Path, out_dir: Path) -> tuple[Path, int]:
    plugin_dir = repo_root / plugin
    skills = collect_skill_files(plugin_dir)
    megaprompts = collect_megaprompt_files(plugin_dir)

    # Plugin-README als Index mitnehmen
    plugin_readme = plugin_dir / "README.md"

    bundle_path = out_dir / f"{plugin}-skills-markdown.zip"
    n_files = 0
    with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as zf:
        if plugin_readme.is_file():
            zf.write(plugin_readme, arcname=f"{plugin}/README.md")
            n_files += 1
        for skill_md in skills:
            # arcname: <plugin>/skills/<skill-slug>/SKILL.md
            rel = skill_md.relative_to(repo_root)
            zf.write(skill_md, arcname=str(rel))
            n_files += 1
        for mp_md in megaprompts:
            # arcname: <plugin>/megaprompts/<filename>
            zf.write(mp_md, arcname=f"{plugin}/megaprompts/{mp_md.name}")
            n_files += 1
    return bundle_path, n_files


def build_combined_bundle(individual_bundles: list[Path], out_dir: Path) -> Path:
    combined = out_dir / "alle-skills-markdown.zip"
    with zipfile.ZipFile(combined, "w", zipfile.ZIP_DEFLATED) as zf:
        for b in individual_bundles:
            zf.write(b, arcname=b.name)
    return combined


def main():
    if len(sys.argv) != 2:
        print("Usage: build-skills-markdown-bundles.py <output-dir>", file=sys.stderr)
        sys.exit(2)
    out_dir = Path(sys.argv[1]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Repo-Root: Script liegt unter scripts/
    repo_root = Path(__file__).resolve().parent.parent

    plugins = list_plugins(repo_root)
    print(f"Plugins gefunden: {len(plugins)}")

    individual = []
    total_files = 0
    empty = []
    for plugin in plugins:
        bundle_path, n_files = build_plugin_bundle(plugin, repo_root, out_dir)
        if n_files == 0:
            empty.append(plugin)
            bundle_path.unlink()
            continue
        individual.append(bundle_path)
        total_files += n_files

    print(f"Individual bundles erzeugt: {len(individual)}")
    print(f"Skill/Megaprompt-Dateien gesamt: {total_files}")
    if empty:
        print(f"Plugins ohne Skills/Megaprompts (kein ZIP): {len(empty)}")
        for p in empty:
            print(f"  - {p}")

    combined = build_combined_bundle(individual, out_dir)
    size_mb = combined.stat().st_size / 1024 / 1024
    print(f"Combined bundle: {combined.name} ({size_mb:.1f} MB)")


if __name__ == "__main__":
    main()
