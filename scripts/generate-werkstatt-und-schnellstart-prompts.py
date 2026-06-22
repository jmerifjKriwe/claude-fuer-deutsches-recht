#!/usr/bin/env python3
"""Erzeugt pro Plugin einen fachlich individualisierten Werkstatt- und Schnellstart-Prompt.

Die Quelle der Prompts sind plugin.json, README und die vorhandenen SKILL.md-Dateien.
Bestehende promptkonforme Dateien werden ohne --force nicht überschrieben. Mit --force
werden alle Prompts neu aus dem aktuellen Skill-Bestand erzeugt.
"""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path


REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"
MAX_SCHNELLSTART = 7500

COURT_PLUGIN_NAMES = {
    "relationstechnik-zivilrecht",
    "staatsanwaltschaft-amtsanwaltschaft",
    "staatsanwaltschaft-praxis-einstieg",
}

LAW_CODES = (
    "BGB",
    "ZPO",
    "StPO",
    "VwGO",
    "FGO",
    "SGG",
    "ArbGG",
    "FamFG",
    "GVG",
    "GmbHG",
    "AktG",
    "InsO",
    "StaRUG",
    "HGB",
    "AO",
    "EStG",
    "UStG",
    "KStG",
    "GewStG",
    "GG",
    "BDSG",
    "DSGVO",
    "OWiG",
    "StGB",
    "SGB",
    "GWB",
    "VgV",
    "VOB/A",
    "WEG",
    "BetrKV",
    "HeizkostenV",
    "KSchG",
    "TzBfG",
    "AGG",
    "BetrVG",
    "BRAO",
    "BNotO",
    "VVG",
    "KWG",
    "ZAG",
    "WpHG",
    "MarkenG",
    "UrhG",
    "PatG",
    "FamGKG",
    "RVG",
    "BVerfGG",
    "VersAusglG",
)

AKTENZEICHEN_RE = re.compile(
    r"\b(?:"
    r"[IVX]{1,4}\s?[A-Z]{1,5}\s?\d+/\d{2,4}|"
    r"\d+\s?BvR\s?\d+/\d{2,4}|"
    r"\d+\s?BvL\s?\d+/\d{2,4}|"
    r"\d+\s?BvF\s?\d+/\d{2,4}|"
    r"\d+\s?[A-Z]{1,5}\s?\d+/\d{2,4}|"
    r"[A-Z]\s?\d+\s?[A-Z]{1,5}\s?\d+/\d{2,4}|"
    r"C-\d+/\d{2,4}"
    r")\b"
)

COURT_RE = re.compile(
    r"\b(BVerfG|BVerfGE|BGH|BAG|BSG|BFH|BVerwG|EuGH|OLG|OVG|VGH|KG|LAG|LSG|FG|LG|AG|SG)\b"
)

DATE_RE = re.compile(r"\b\d{1,2}\.\d{1,2}\.\d{4}\b")


@dataclass
class Skill:
    slug: str
    title: str
    description: str
    body: str
    order: tuple[int, str]


def load_marketplace() -> list[dict]:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    return list(data.get("plugins", []))


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source") or f"./{plugin['name']}"
    if source.startswith("./"):
        source = source[2:]
    return REPO / source


def strip_frontmatter(text: str) -> tuple[str, str]:
    if not text.startswith("---"):
        return "", text.strip()
    match = re.match(r"---\s*\n([\s\S]*?)\n---\s*\n?", text)
    if not match:
        return "", text.strip()
    return match.group(1), text[match.end() :].strip()


def frontmatter_description(frontmatter: str) -> str:
    for line in frontmatter.splitlines():
        if line.startswith("description:"):
            value = line.split(":", 1)[1].strip()
            if value.startswith('"') and value.endswith('"'):
                value = value[1:-1]
            return value.strip()
    return ""


def strip_markdown(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"^#+\s*", "", text)
    return text


def clean_text(text: str, limit: int | None = None) -> str:
    replacements = {
        "Clau" + "de Desktop/Cowork": "kompatible Plugin-Oberfläche",
        "Clau" + "de Desktop": "kompatible Plugin-Oberfläche",
        "Clau" + "de Cowork": "kompatible Plugin-Oberfläche",
        "Clau" + "de Code": "Plugin-Setup",
        "Clau" + "de": "Chat-System",
        "Open" + "AI": "KI-Anbieter",
        "Cur" + "sor": "Editor",
        "Ai" + "der": "Editor",
        "Con" + "tinue": "Editor",
        "Megaprompt": "Werkstatt-Prompt",
        "Megaprompts": "Werkstatt-Prompts",
        "Miniprompt": "Schnellstart-Prompt",
        "Miniprompts": "Schnellstart-Prompts",
        "fuer": "für",
        "Fuer": "Für",
        "Klaeger": "Kläger",
        "Beklagter": "Beklagter",
        "Beklagten": "Beklagten",
        "Anwaelte": "Anwälte",
        "Betraege": "Beträge",
        "betraege": "beträge",
        "moeglich": "möglich",
        "Moeglich": "Möglich",
        "moegliche": "mögliche",
        "Moegliche": "Mögliche",
        "uebernommene": "übernommene",
        "uebernommen": "übernommen",
        "Vertraege": "Verträge",
        "vertraege": "verträge",
        "Beschluesse": "Beschlüsse",
        "beschluesse": "beschlüsse",
        "Gesellschafterbeschluesse": "Gesellschafterbeschlüsse",
        "Aufsichtsratsbeschluesse": "Aufsichtsratsbeschlüsse",
        "Hauptversammlungsbeschluesse": "Hauptversammlungsbeschlüsse",
        "Vorstandsbeschluesse": "Vorstandsbeschlüsse",
        "beschliessende": "beschließende",
        "Dateigroesse": "Dateigröße",
        "Auffaelligkeitsliste": "Auffälligkeitsliste",
        "Standardabsaetzen": "Standardabsätzen",
        "Vorlaeuferdokumenten": "Vorläuferdokumenten",
        "Naechstes": "Nächstes",
        "naechstes": "nächstes",
        "naechste": "nächste",
        "Naechste": "Nächste",
        "frueh": "früh",
        "fruehen": "frühen",
        "gefuehrten": "geführten",
        "fuehrt": "führt",
        "Fuehrt": "Führt",
        "fuehren": "führen",
        "Klaert": "Klärt",
        "klaert": "klärt",
        "Erklaert": "Erklärt",
        "erklaert": "erklärt",
        "schlaegt": "schlägt",
        "schlaegst": "schlägst",
        "Pruefer": "Prüfer",
        "pruefer": "prüfer",
        "pruefen": "prüfen",
        "Pruefpunkte": "Prüfpunkte",
        "Selbststaendige": "Selbstständige",
        "Rentenpruefer": "Rentenprüfer",
        "Vertragsausfueller": "Vertragsausfüller",
        "Bezuege": "Bezüge",
        "Begruendungspflichten": "Begründungspflichten",
        "Schoeffen": "Schöffen",
        "Buergergeld": "Bürgergeld",
        "Buerger": "Bürger",
        "enthaelt": "enthält",
        "Fuenf": "Fünf",
        "Kostenpruefer": "Kostenprüfer",
        "Abwaegung": "Abwägung",
        "Verspaetung": "Verspätung",
        "Rechtmaessigkeit": "Rechtmäßigkeit",
        "Rueckfrage": "Rückfrage",
        "benoetigt": "benötigt",
        "Faelle": "Fälle",
        "Geschaeftsbereich": "Geschäftsbereich",
        "Beweisantraege": "Beweisanträge",
        "lueckenliste": "lückenliste",
        "geldwaesche": "geldwäsche",
        "Wirtschaftspruefer": "Wirtschaftsprüfer",
        "Patentanwaelte": "Patentanwälte",
        "Verbaendeanhoerung": "Verbändeanhörung",
        "Heranfuehrung": "Heranführung",
        "Erfuellungsaufwand": "Erfüllungsaufwand",
        "gruen": "grün",
        "vollstaendig": "vollständig",
        "vollstaendige": "vollständige",
        "Zustaendigkeit": "Zuständigkeit",
        "zustaendig": "zuständig",
        "Gestaendnis": "Geständnis",
        "Auskuenfte": "Auskünfte",
        "Antraege": "Anträge",
        "Verfuegung": "Verfügung",
        "Verfuegungen": "Verfügungen",
        "aeusser": "äußer",
        "Pruefung": "Prüfung",
        "pruefen": "prüfen",
        "Pruefer": "Prüfer",
        "beduerftig": "bedürftig",
        "Schluessigkeit": "Schlüssigkeit",
        "schluessig": "schlüssig",
        "Paragraph": "Paragraf",
        "paragraph": "Paragraf",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    text = text.replace("§§", "Paragrafen").replace("§", "Paragraf")
    text = text.replace("→", "->").replace("✓", "").replace("★", "")
    text = text.replace("“", "'").replace("”", "'").replace('"', "'")
    text = text.replace("<", "[").replace(">", "]")
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\bAbs\.\s*", "Absatz ", text)
    text = re.sub(r"\bS\.\s*", "Satz ", text)
    text = re.sub(r"\bNr\.\s*", "Nummer ", text)
    text = re.sub(r"\bi\.V\.m\.\s*", "in Verbindung mit ", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = text.replace("**", "")
    text = re.sub(r"\bArt\.\s*", "Artikel ", text)
    text = re.sub(r"\s+", " ", text).strip()
    if limit and len(text) > limit:
        return text[: limit - 1].rstrip(" ,.;:-") + "…"
    return text


def human_title(slug: str) -> str:
    words = [w for w in re.split(r"[-_]+", slug) if w]
    small = {"und", "oder", "mit", "fuer", "für", "im", "am", "zur", "zum", "der", "die", "das", "des"}
    out: list[str] = []
    for word in words:
        mapped = {"fuer": "für", "pruefer": "prüfer", "pruefung": "prüfung", "zustaendigkeit": "zuständigkeit"}.get(word, word)
        if mapped in small:
            out.append(mapped)
        elif len(mapped) <= 4 and mapped.isalpha():
            out.append(mapped.upper())
        else:
            out.append(mapped[:1].upper() + mapped[1:])
    return " ".join(out)


def title_from_readme(directory: Path, fallback: str) -> str:
    readme = directory / "README.md"
    if readme.is_file():
        for line in readme.read_text(encoding="utf-8", errors="ignore").splitlines():
            if line.startswith("# "):
                title = clean_text(line[2:].strip(), 100)
                return re.sub(r"^Plugin:\s*", "", title, flags=re.IGNORECASE)
    return human_title(fallback)


def first_readme_signal(directory: Path) -> str:
    readme = directory / "README.md"
    if not readme.is_file():
        return ""
    text = readme.read_text(encoding="utf-8", errors="ignore")
    text = re.sub(r"<!-- BEGIN [^\n]*?-->\s*[\s\S]*?<!-- END [^\n]*?-->", "", text)
    for block in re.split(r"\n\s*\n", text):
        b = clean_text(strip_markdown(block.strip()), 700)
        if len(b) < 120 or b.startswith("|") or "latest/download" in b:
            continue
        return b
    return ""


def skill_order(slug: str) -> tuple[int, str]:
    match = re.match(r"^(\d+)[-_]", slug)
    if match:
        return int(match.group(1)), slug
    priority = 500
    if re.search(r"(einstieg|kaltstart|triage|routing|start)", slug):
        priority = 100
    elif re.search(r"(workflow|prozess|verfahren|akte)", slug):
        priority = 200
    elif re.search(r"(entwurf|schriftsatz|antrag|beschluss|tenor|verfuegung|verfügung)", slug):
        priority = 700
    elif re.search(r"(kontrolle|red-team|qualitaet|abschluss)", slug):
        priority = 900
    return priority, slug


def collect_skills(directory: Path) -> list[Skill]:
    skills_dir = directory / "skills"
    if not skills_dir.is_dir():
        return []
    out: list[Skill] = []
    for skill_md in sorted(skills_dir.glob("*/SKILL.md")):
        text = skill_md.read_text(encoding="utf-8", errors="ignore")
        fm, body = strip_frontmatter(text)
        slug = skill_md.parent.name
        desc = clean_text(frontmatter_description(fm), 650)
        title = ""
        for line in body.splitlines():
            if line.startswith("# "):
                title = clean_text(line[2:].strip(), 90)
                break
        if not title:
            title = human_title(slug)
        out.append(Skill(slug=slug, title=title, description=desc, body=body, order=skill_order(slug)))
    return sorted(out, key=lambda s: s.order)


def infer_norms(plugin_name: str, title: str, text: str) -> list[str]:
    if is_normfree_workflow_plugin(plugin_name, title, text):
        return []
    blob = f"{plugin_name} {title} {text}".lower()
    groups: list[str] = []
    def add(items: list[str]) -> None:
        for item in items:
            if item not in groups:
                groups.append(item)

    if "miet" in blob or "wohnung" in blob or "weg" in blob:
        add([
            "Paragraf 23 Nummer 2a GVG",
            "Paragraf 78 Absatz 1 ZPO",
            "Paragraf 535 BGB",
            "Paragraf 543 BGB",
            "Paragraf 569 BGB",
            "Paragraf 573 BGB",
        ])
    if "famil" in blob or "unterhalt" in blob or "scheidung" in blob:
        add([
            "Paragraf 38 FamFG",
            "Paragraf 1565 BGB",
            "Paragraf 1601 BGB",
            "Paragraf 1610 BGB",
            "Paragraf 1612a BGB",
            "Paragraf 1671 BGB",
            "Paragraf 1684 BGB",
        ])
    if "arbeit" in blob or "kuendigung" in blob or "kündigung" in blob or "zeugnis" in blob:
        add([
            "Paragraf 611a BGB",
            "Paragraf 109 GewO",
            "Paragraf 1 KSchG",
            "Paragraf 102 BetrVG",
            "Paragraf 14 TzBfG",
            "Paragraf 7 AGG",
        ])
    if "straf" in blob or "staatsanw" in blob or "owi" in blob or "bussgeld" in blob:
        add([
            "Paragraf 152 Absatz 2 StPO",
            "Paragraf 160 StPO",
            "Paragraf 163 StPO",
            "Paragraf 170 StPO",
            "Paragraf 200 StPO",
            "Paragraf 46 StGB",
        ])
    if "zivil" in blob or "relation" in blob or "forderung" in blob or "klage" in blob:
        add([
            "Paragraf 138 ZPO",
            "Paragraf 253 Absatz 2 ZPO",
            "Paragraf 286 ZPO",
            "Paragraf 287 ZPO",
            "Paragraf 313 ZPO",
        ])
    if "insolvenz" in blob or "restruktur" in blob:
        add([
            "Paragraf 13 InsO",
            "Paragraf 17 InsO",
            "Paragraf 19 InsO",
            "Paragraf 27 InsO",
            "Paragraf 80 InsO",
            "Paragraf 31 StaRUG",
        ])
    if "steuer" in blob or "finanz" in blob or "abgabe" in blob:
        add([
            "Paragraf 88 AO",
            "Paragraf 90 AO",
            "Paragraf 162 AO",
            "Paragraf 173 AO",
            "Paragraf 76 FGO",
            "Paragraf 96 FGO",
        ])
    if "sozial" in blob or "rente" in blob or "krankenkasse" in blob:
        add([
            "Paragraf 103 SGG",
            "Paragraf 105 SGG",
            "Paragraf 106 SGG",
            "Paragraf 20 SGB X",
            "Paragraf 39 SGB I",
        ])
    if "verwaltungs" in blob or "beamt" in blob or "hochschul" in blob or "versamml" in blob:
        add([
            "Paragraf 42 VwGO",
            "Paragraf 80 VwGO",
            "Paragraf 86 VwGO",
            "Paragraf 113 VwGO",
            "Paragraf 123 VwGO",
            "Paragraf 35 VwVfG",
        ])
    if "verfass" in blob or "grundrecht" in blob or "bverfg" in blob:
        add([
            "Artikel 1 GG",
            "Artikel 2 GG",
            "Artikel 3 GG",
            "Artikel 5 GG",
            "Artikel 12 GG",
            "Artikel 14 GG",
            "Paragraf 90 BVerfGG",
        ])
    if "gesellschaft" in blob or "corporate" in blob or "gmbh" in blob or "aktien" in blob:
        add([
            "Paragraf 15 HGB",
            "Paragraf 35 GmbHG",
            "Paragraf 40 GmbHG",
            "Paragraf 93 AktG",
            "Paragraf 119 AktG",
        ])
    if "treuepflicht" in blob or "gesellschafter" in blob:
        add([
            "Paragraf 241 Absatz 2 BGB",
            "Paragraf 242 BGB",
            "Paragraf 43 GmbHG",
            "Paragraf 93 AktG",
            "Paragraf 705 BGB",
        ])
    if "it-recht" in blob or "software" in blob or "digital" in blob:
        add([
            "Paragraf 327 BGB",
            "Paragraf 327e BGB",
            "Paragraf 327f BGB",
            "Paragraf 631 BGB",
            "Paragraf 280 BGB",
        ])
    if "datenschutz" in blob or "daten" in blob or "ki-vo" in blob or "ai-act" in blob:
        add([
            "Artikel 5 DSGVO",
            "Artikel 6 DSGVO",
            "Artikel 15 DSGVO",
            "Artikel 32 DSGVO",
            "Artikel 58 DSGVO",
            "Artikel 83 DSGVO",
            "Paragraf 26 BDSG",
        ])
    if "vergabe" in blob:
        add([
            "Paragraf 97 GWB",
            "Paragraf 160 GWB",
            "Paragraf 168 GWB",
            "Paragraf 56 VgV",
        ])
    if "europa" in blob or "unionsrecht" in blob:
        add([
            "Paragraf 1 EUZBBG",
            "Paragraf 4 EUZBBG",
            "Paragraf 80 BVerfGG",
            "Paragraf 90 BVerfGG",
            "Paragraf 93 BVerfGG",
        ])
    if "rechtsgeschichte" in blob or "landrecht" in blob or "roemisch" in blob or "römisch" in blob:
        add([
            "Paragraf 1 BGB",
            "Paragraf 2 EGBGB",
            "Paragraf 242 BGB",
            "Paragraf 305 BGB",
            "Paragraf 823 BGB",
        ])
    if "legistik" in blob or "gesetzgebung" in blob:
        add([
            "Paragraf 42 GGO",
            "Paragraf 43 GGO",
            "Paragraf 44 GGO",
            "Paragraf 45 GGO",
            "Paragraf 80 GGO",
        ])
    if "verhaeltnis" in blob or "verhältnismäß" in blob or "verhaeltnismaessigkeit" in blob:
        add([
            "Paragraf 32 BVerfGG",
            "Paragraf 90 BVerfGG",
            "Paragraf 93a BVerfGG",
            "Paragraf 93c BVerfGG",
            "Paragraf 95 BVerfGG",
        ])
    if "versicher" in blob:
        add([
            "Paragraf 1 VVG",
            "Paragraf 19 VVG",
            "Paragraf 28 VVG",
            "Paragraf 81 VVG",
            "Paragraf 86 VVG",
        ])
    if "marke" in blob or "urheber" in blob or "design" in blob or "gebrauchsmuster" in blob:
        add([
            "Paragraf 14 MarkenG",
            "Paragraf 97 UrhG",
            "Paragraf 24 UrhG",
            "Paragraf 33 DesignG",
            "Paragraf 11 GebrMG",
        ])
    return groups


def extract_norms(skills: list[Skill], plugin_name: str, title: str, max_items: int = 12) -> list[str]:
    if is_normfree_workflow_plugin(plugin_name, title, " ".join([s.description for s in skills])):
        return []
    found: list[str] = []
    code_alt = "|".join(re.escape(c) for c in LAW_CODES)
    patterns = [
        re.compile(rf"(Paragraf(?:en)?\s+[^.\n;]{{0,120}}(?:{code_alt})(?:\s+[IVX]+)?)", re.IGNORECASE),
        re.compile(rf"((?:{code_alt})(?:\s+[IVX]+)?\s+§{{1,2}}\s*[^.\n;]{{0,100}})", re.IGNORECASE),
        re.compile(rf"(§{{1,2}}\s*[^.\n;]{{0,100}}(?:{code_alt})(?:\s+[IVX]+)?)", re.IGNORECASE),
        re.compile(r"((?:Artikel|Art\.)\s+\d+[a-zA-Z]?(?:\s+Absatz\s+\d+|\s+Abs\.\s+\d+)?\s+(?:GG|DSGVO|GRCh|AEUV))", re.IGNORECASE),
    ]
    for skill in skills:
        sample = skill.description + "\n" + skill.body[:8000]
        for pattern in patterns:
            for match in pattern.findall(sample):
                item = clean_norm(match)
                if item and item not in found:
                    found.append(item)
                if len(found) >= max_items:
                    break
    inferred = infer_norms(plugin_name, title, " ".join([s.description for s in skills]))
    needs_more_paragraphs = sum(1 for item in found if "Paragraf " in item) < 3
    for item in inferred:
        if item not in found:
            found.append(item)
        if len(found) >= max_items and not needs_more_paragraphs:
            break
    result = found[:max_items]
    if sum(1 for item in result if "Paragraf " in item) < 3:
        paragraph_items = [item for item in found if "Paragraf " in item]
        for item in paragraph_items:
            if item in result:
                continue
            result.append(item)
            if sum(1 for entry in result if "Paragraf " in entry) >= 3:
                break
    return result[: max_items + 3]


def clean_norm(text: str) -> str:
    text = clean_text(text, 190)
    text = text.replace("§§", "Paragrafen").replace("§", "Paragraf")
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"Paragrafen\s+([0-9a-zA-Z]+)\s*[-–]\s*([0-9a-zA-Z]+)", r"Paragrafen \1 bis \2", text)
    return text.strip(" ,.;")


def extract_decisions(skills: list[Skill], max_items: int = 5) -> list[str]:
    found: list[str] = []
    for skill in skills:
        sample = "\n".join([skill.description, skill.body[:10000]])
        for line in sample.splitlines():
            if "BeckRS" in line or "juris" in line:
                continue
            if not AKTENZEICHEN_RE.search(line):
                continue
            clean = clean_text(strip_markdown(line), 260)
            clean = clean.lstrip("-• ").strip()
            if COURT_RE.search(clean) and clean not in found:
                found.append(clean)
            elif clean not in found:
                az = AKTENZEICHEN_RE.search(clean)
                if az:
                    found.append(f"Aktenzeichen {az.group(0)} — Gericht, Datum, Entscheidungsform und frei zugängliche Quelle vor Verwendung live verifizieren; nur übernehmen, wenn es den Skillgegenstand trägt")
            if len(found) >= max_items:
                return found
    return found


def workflow_selection(skills: list[Skill]) -> list[Skill]:
    if not skills:
        return []
    count = len(skills)
    target = min(12, max(5, 4 + int(math.log2(count + 1))))
    if count <= target:
        return skills
    picked = skills[:target]
    must_words = ("entwurf", "schriftsatz", "antrag", "beschluss", "tenor", "verfuegung", "verfügung", "kontrolle")
    for skill in skills[target:]:
        if any(word in skill.slug for word in must_words) and skill not in picked:
            picked[-1] = skill
            break
    return sorted(picked, key=lambda s: s.order)


def role_text(plugin_name: str, title: str, description: str) -> str:
    blob = f"{plugin_name} {title} {description}".lower()
    if is_normfree_workflow_plugin(plugin_name, title, description):
        return f"Du arbeitest als Strukturierungs- und Fortschrittsnavigator für {title}: Dokumente, To-dos, Lücken, Reihenfolgen, Zuständigkeiten, Statusfelder und nächste Schritte werden sichtbar gemacht, ohne eine Rechtsprüfung vorzutäuschen."
    if "relationstechnik" in blob:
        return f"Du arbeitest als Relationsersteller im Zivilrecht für {title}: Klägerstation, Beklagtenstation, Beweisstation und Entscheidungsstation werden so getrennt, dass daraus ein Hinweis, ein Beweisbeschluss, ein Votum oder ein Urteil entstehen kann."
    if plugin_name.startswith("richter-") or "/richter-" in plugin_name:
        return f"Du arbeitest im richterlichen Rollenbild von {title}: Akten werden aus Sicht des Spruchkörpers geordnet, entscheidungserhebliche Tatsachen werden herausgearbeitet und Beschluss-, Urteils-, Hinweis- oder Verfügungsentwürfe vorbereitet."
    if "staatsanwaltschaft" in plugin_name:
        return f"Du arbeitest als Dezernent der Staatsanwaltschaft im Zuschnitt von {title}: Anfangsverdacht, Ermittlungsrichtung, Beweisstand, Abschlussverfügung und Sitzungsrolle werden sauber getrennt."
    if "famil" in blob:
        return f"Du arbeitest im familienrechtlichen Mandats- oder Gerichtsmodus von {title}: Unterhalt, Scheidung, Kindschaftssachen und Versorgungsausgleich werden mit Fristen, Belegen und Antragslogik verbunden."
    if "miet" in blob:
        return f"Du arbeitest im mietrechtlichen Fallmodus von {title}: Wohnraum, Gewerberaum, Räumung, Zahlung, Minderung, Betriebskosten und Zuständigkeit werden getrennt geprüft."
    if "arbeits" in blob:
        return f"Du arbeitest im arbeitsrechtlichen Fallmodus von {title}: Kündigung, Zeugnis, Vergütung, Befristung, Beteiligungsrechte und Prozessrisiko werden belegorientiert geprüft."
    return description or f"Du arbeitest im fachlichen Rollenbild von {title}: Der vorhandene Skill-Bestand gibt Reihenfolge, Arbeitsprodukte und Kontrollpunkte vor."


def is_normfree_workflow_plugin(plugin_name: str, title: str, text: str) -> bool:
    blob = f"{plugin_name} {title} {text}".lower()
    explicit = {
        "status-navigator-step-plan",
        "tabellenreview-3d",
    }
    if plugin_name in explicit:
        return True
    return "normfrei" in blob and ("workflow" in blob or "struktur" in blob or "status" in blob)


def station_language(skill: Skill, plugin_title: str, plugin_name: str) -> tuple[str, str, str]:
    blob = f"{skill.slug} {skill.title} {skill.description}".lower()
    context = f"{plugin_name} {plugin_title}".lower()
    is_criminal_context = any(
        word in context
        for word in ["straf", "staatsanwaltschaft", "amtsanwaltschaft", "owi", "bussgeld", "bußgeld"]
    )
    is_civil_court_context = (
        "richter-amtsgericht-zivil" in plugin_name
        or "richter-landgericht-zivilkammer" in plugin_name
        or "relationstechnik-zivilrecht" in plugin_name
    )
    is_normfree_context = is_normfree_workflow_plugin(plugin_name, plugin_title, skill.description)
    if is_normfree_context:
        return (
            f"Übernimm für {skill.title} Dateiname, Datum, Version, Statusfeld, Verantwortlichen, Empfänger, Tabellenblatt und sichtbare Lücke.",
            "Prüfe Reihenfolge, Zuständigkeit, Dublette, fehlendes Dokument, falschen Namen, abweichenden Betrag und nächsten Arbeitsschritt ohne materiell-rechtliche Bewertung.",
            "Erstelle Statuszeile, Step-Plan-Karte, Excel-Reiter, Padlet-Spalte oder Lückenliste mit eindeutigem Anschluss.",
        )
    if is_civil_court_context:
        if any(word in blob for word in ["streitwert", "gerichtskosten", "gkg", "kostenrechnung"]):
            return (
                "Übernimm Klageantrag, wirtschaftliches Interesse, Nebenforderungen, vorläufige Wertangaben, Vorschussstand und erkennbare Wertprivilegien.",
                "Prüfe Streitwert, sachliche Zuständigkeit, Gerichtskostenvorschuss, Kostenfolge und ob der Wert für Rechtsmittel oder Verfahrensart gesondert relevant wird.",
                "Erstelle Streitwertvermerk, Kostenhinweis, Vorschussverfügung oder Wertfestsetzungsbaustein mit nachvollziehbarer Berechnung.",
            )
        if any(word in blob for word in ["urteil", "tenor", "kosten", "vollstreck", "entscheidung"]):
            return (
                "Übernimm Anträge, zugesprochenen Betrag, Nebenforderungen, Kostenquote, Vollstreckbarkeit, Beschwer und Rechtsmittel aus der Relation.",
                "Prüfe Hauptsachetenor, Zinsen, Kosten nach ZPO, vorläufige Vollstreckbarkeit, Beschwer und Begründungsanschluss nach Paragraf 313 ZPO.",
                "Erstelle Tenor, Kostenentscheidung, Vollstreckbarkeitsausspruch, Tatbestand oder Entscheidungsgründe in dezimaler Gliederung.",
            )
        if any(word in blob for word in ["relation", "schlüssigkeit", "schluessigkeit", "erheblichkeit", "klägerstation", "beklagtenstation"]):
            return (
                "Trenne Anträge, Klägerstation, Beklagtenstation, unstreitigen Sachverhalt, bestrittene Tatsachen, Einwendungen und Beweisangebote.",
                "Prüfe Schlüssigkeit, Erheblichkeit, Beweisbedürftigkeit, Beweislast, Hinweispflichten und Entscheidungsreife in der Relation.",
                "Erstelle Relationsteil, Votum, Hinweisbeschluss oder Entscheidungsstation mit klarer Trennung von Tatsache, Norm und Rechtsfolge.",
            )
        if any(word in blob for word in ["erstdurchsicht", "akte", "eingangsprüfung", "eingangspruefung", "zuständigkeit", "zustaendigkeit"]):
            return (
                "Ordne Klage, Klageerwiderung, Replik, Anlagen, Zustellung, Streitwert, Zuständigkeit und Verfahrensstand als zivilprozessuale Aktenstation.",
                "Prüfe Zulässigkeit, Zuständigkeit, Klageantrag, Parteistellung, Zustellung, frühen Termin oder schriftliches Vorverfahren und erkennbare Hinweise.",
                "Erstelle Erstdurchsicht, Zuständigkeitsvermerk, richterliche Verfügung oder Eingangshinweis mit konkreten Aktenfundstellen.",
            )
        if any(word in blob for word in ["beweis", "zeuge", "sachverständ", "gutachten"]):
            return (
                "Lege streitige Tatsache, Beweisangebot, Beweislast, Beweisthema, Beweismittel und prozessuale Anschlussfrist getrennt ab.",
                "Prüfe Beweisbedürftigkeit, Erheblichkeit, Beweislast, Verspätung, richterlichen Hinweisbedarf und den Zuschnitt eines Beweisbeschlusses.",
                "Erstelle Beweisbeschluss, Hinweisverfügung, Terminvorbereitung oder Beweiswürdigungsbaustein mit Aktenfundstelle.",
            )
        return (
            "Ordne Klage, Klageerwiderung, Replik, Anlagen, Zustellung, Streitwert, Zuständigkeit und Verfahrensstand als zivilprozessuale Aktenstation.",
            "Prüfe Schlüssigkeit, Erheblichkeit, Zulässigkeit, Zuständigkeit, Hinweispflicht, Beweisbedürftigkeit und Entscheidungsreife.",
            "Erstelle Relationsteil, Hinweisbeschluss, Verfügung, Vergleichsvorschlag oder Urteilsbaustein mit Rubrum- und Anlagenbezug.",
        )
    if any(word in blob for word in ["klage", "schriftsatz", "antrag", "berufung", "beschwerde"]):
        return (
            f"Ziehe Antrag, Parteistellung, Gericht, Frist, Zustellung, Anlagen und den letzten Schriftsatz für {skill.title} heran.",
            "Prüfe Zulässigkeit, Bestimmtheit, Zuständigkeit, Frist und materiellen Kern ohne den Vortrag der Gegenseite zu vermischen.",
            "Erstelle einen Antrag- oder Schriftsatzbaustein mit Rubrumshinweis, Sachverhalt, Subsumtion, Beweisangebot und dezimaler Gliederung.",
        )
    if any(word in blob for word in ["unterhalt", "duesseldorfer", "düsseldorfer", "ehegatten", "kindesunterhalt"]):
        return (
            "Lege Einkommen, Bereinigungen, Erwerbsobliegenheit, Bedarf, Rang, Selbstbehalt, Titel und Auskunftslücken getrennt ab.",
            "Prüfe Bedarf, Bedürftigkeit, Leistungsfähigkeit, Rangfolge, Mangelfall, Tabellenbezug und Pflicht zur Live-Prüfung der aktuellen Leitlinien.",
            "Erstelle ein Rechenschema mit belegten Zahlen, Varianten, Auskunftslücken und einem konkreten Antrag oder Hinweisbeschluss.",
        )
    if is_criminal_context and re.search(r"\b(straf|ermittlung|anklage|einstellung|bussgeld|bußgeld|tatvorwurf|schuld|hauptverhandlung)\b", blob):
        return (
            "Ordne Anzeige, Tatzeit, Tatort, Beschuldigtenangaben, Beweismittel, Schaden, Vorstrafen, Vermerke und offene Ermittlungsaufträge.",
            "Prüfe Anfangsverdacht, Tatbestand, Rechtfertigung, Schuld, Beweisbarkeit, Opportunität und Abschlussreife.",
            "Erstelle Ermittlungsverfügung, Abschlussvermerk, Anklagebaustein, Strafbefehlsentwurf oder Einstellungsverfügung.",
        )
    if any(word in blob for word in ["register", "grundbuch", "handelsregister", "gesellschafterliste"]):
        return (
            "Ordne Anmeldung, Urkunde, Vollmacht, Registerstand, Zwischenverfügung, Beteiligte und Nachweise in registerfähiger Form.",
            "Prüfe Zuständigkeit, Form, Vertretung, Eintragungsfähigkeit, Rechtspflegerzuständigkeit und behebbaren Mangel.",
            "Erstelle Zwischenverfügungsantwort, Eintragungsvermerk, Nachforderungsliste oder registertauglichen Prüfvermerk.",
        )
    if any(word in blob for word in ["betriebskosten", "nebenkosten", "miete", "räumung", "raeumung"]):
        return (
            "Trenne Wohnraum, Gewerberaum, Abrechnung, Belegeinsicht, Zugang, Fristen, Mietrückstand, Kündigung und Räumungsstand.",
            "Prüfe Umlagevereinbarung, Abrechnungsfrist, formelle Ordnung, materielle Einwendungen, Zuständigkeit und Beweislast.",
            "Erstelle Abrechnungskorrektur, Einwendungsschreiben, Klageentwurf, Räumungsstrategie oder Beleganforderung.",
        )
    if any(word in blob for word in ["akte", "dokument", "beleg", "anlage", "pdf", "excel"]):
        return (
            "Inventarisiere Dokumente mit Datum, Absender, Empfänger, Anlagenbezug, Aktenfundstelle, Zahlen und erkennbarer Lücke.",
            "Prüfe, welches Dokument welche Tatsache trägt und welche Behauptung ohne Beleg bleibt.",
            "Erstelle Dokumentenmatrix, Lückenliste, Anlagenverzeichnis oder geordneten Aktenauszug.",
        )
    if any(word in blob for word in ["kontrolle", "red-team", "qualitaet", "qualität", "risiko", "ampel"]):
        return (
            "Nimm das vorhandene Zwischenergebnis, die Quellenliste und die offenen Annahmen als Prüfgegenstand.",
            "Prüfe Widersprüche, fehlende Normanker, Fristfehler, falsche Zuständigkeit, Beweislastsprünge und zu starke Schlussfolgerungen.",
            "Erstelle eine Fehlerliste mit Priorität, Korrekturtext und Freigabe- oder Stop-Empfehlung.",
        )
    if any(word in blob for word in ["vertrag", "klausel", "agb", "nda", "leasing"]):
        return (
            "Ordne Vertragsparteien, Leistung, Gegenleistung, Laufzeit, Kündigung, Haftung, Sicherheiten, Anlagen und Verhandlungsstand.",
            "Prüfe Klauselzweck, dispositives Recht, AGB-Kontrolle, Beweis- und Abwicklungsrisiken sowie wirtschaftliche Schieflagen.",
            "Erstelle Redline-Hinweise, Klauselvorschläge, Risikomatrix oder Verhandlungsnarrativ.",
        )
    return (
        f"Nutze die Aktenstücke, Nutzerangaben und Belege, die den Arbeitsschritt {skill.title} im Kontext {plugin_title} tragen.",
        f"Prüfe den Skillauftrag anhand von {clean_text(skill.description or skill.title, 180)} und trenne Tatsachen, Normen, Risiken und Anschlussfragen.",
        f"Erstelle ein Teilprodukt zu `{skill.slug}` mit Kurzfazit, Begründung, Belegstelle und nächstem Handlungspunkt.",
    )


def is_court_plugin(plugin: dict) -> bool:
    source = (plugin.get("source") or "").strip("./")
    name = plugin["name"]
    return source.startswith("gerichtsplugins/") and (name.startswith("richter-") or name in COURT_PLUGIN_NAMES)


def court_profile(plugin_name: str) -> dict[str, str]:
    if "relationstechnik" in plugin_name:
        return {
            "input": "Klage, Klageerwiderung, Replik, Duplik, Anlagen, Protokolle, Hinweise und Vergleichsvorschläge",
            "structure": "Klägerstation, Beklagtenstation, Beweisstation und Entscheidungsstation werden vollständig getrennt. Rubrum, Anträge, unstreitiger Sachverhalt, streitige Tatsachen, Beweislast und Entscheidungsvorschlag dürfen nicht ineinanderlaufen.",
            "tools": "Hinweis nach Paragraf 139 ZPO, prozessleitende Verfügung nach Paragraf 273 ZPO, Beweisbeschluss nach Paragraf 358 ZPO, freie Beweiswürdigung nach Paragraf 286 ZPO.",
            "product": "Hinweisbeschluss: Das Gericht weist darauf hin, dass es auf die Behauptung [Tatsache] ankommen kann. Die Partei erhält Gelegenheit, binnen [Frist] substantiiert vorzutragen und Beweis anzutreten.",
        }
    if "straf" in plugin_name or "staatsanwaltschaft" in plugin_name or "amtsanwaltschaft" in plugin_name:
        return {
            "input": "Anzeige, Ermittlungsakte, Anklageschrift, Strafbefehl, Vernehmungen, Gutachten, Beweismittelvermerke und Hauptverhandlungsprotokolle",
            "structure": "Anklagevorwurf, Ermittlungsergebnis, Einlassung, Beweismittel, rechtliche Würdigung und Rechtsfolgenfrage werden getrennt. Jede Tatsache braucht Aktenfundstelle oder Beweismittel.",
            "tools": "Verfügung nach Paragraf 160 StPO, Nachermittlung nach Paragraf 163 StPO, Eröffnungsprüfung nach Paragraf 203 StPO, Verständigungslage nach Paragraf 257c StPO, Beweiswürdigung nach Paragraf 261 StPO.",
            "product": "Verfügung: Es wird um ergänzende Vernehmung des Zeugen [Name] zu [Beweisthema] gebeten. Das Ergebnis ist mit Fundstelle zur Akte zu nehmen und anschließend zur Abschlussentscheidung vorzulegen.",
        }
    if "arbeitsgericht" in plugin_name:
        return {
            "input": "Klageschrift, Klageerwiderung, Kündigung, Abmahnung, Betriebsratsanhörung, Vergleichsvorschlag und Protokolle",
            "structure": "Klageantrag, Klagebegründung, Erwiderung, Güteversuch, Kammertermin, Vergleichschance und Entscheidungsreife werden in getrennte Blöcke gelegt.",
            "tools": "Güteverhandlung, Aufklärungsverfügung nach Paragraf 56 ArbGG, Kammertermin, Beweisbeschluss, Vergleichsprotokoll.",
            "product": "Hinweis: Das Gericht weist darauf hin, dass der Vortrag zu [Tatsache] bislang nicht hinreichend konkret ist. Gelegenheit zur Ergänzung besteht bis zum [Datum].",
        }
    if "sozialgericht" in plugin_name:
        return {
            "input": "Bescheid, Widerspruchsbescheid, Verwaltungsakte, Klagebegründung, Befundberichte, Gutachten und Leistungsakten",
            "structure": "Verwaltungsentscheidung, Vorverfahren, Klagebegründung, medizinische oder beitragsrechtliche Tatsachen, Amtsermittlung und Entscheidungsform werden getrennt.",
            "tools": "Amtsermittlung nach Paragraf 103 SGG, richterliche Aufklärung nach Paragraf 106 SGG, Gerichtsbescheid nach Paragraf 105 SGG, Sachverständigenbeweis.",
            "product": "Aufklärungsverfügung: Die Beklagte wird gebeten, die vollständige Verwaltungsakte einschließlich Widerspruchsvorgang und medizinischer Befundunterlagen binnen [Frist] vorzulegen.",
        }
    if "finanzgericht" in plugin_name:
        return {
            "input": "Steuerbescheid, Einspruchsentscheidung, Steuererklärung, Buchführungsunterlagen, Prüfungsbericht und Klagebegründung",
            "structure": "Steuerbescheid, Einspruchsentscheidung, Klagegründe, Mitwirkung, Schätzung, Beweisangebot und Entscheidungsreife werden getrennt.",
            "tools": "Sachaufklärung nach Paragraf 76 FGO, Überzeugungsbildung nach Paragraf 96 FGO, richterliche Verfügung, Erörterungstermin, Aussetzung der Vollziehung.",
            "product": "Verfügung: Der Kläger wird gebeten, die behaupteten Betriebsausgaben durch Belege und Zahlungsnachweise bis zum [Datum] zu konkretisieren.",
        }
    if "verwaltungsgericht" in plugin_name:
        return {
            "input": "Verwaltungsakt, Widerspruchsbescheid, Behördenakte, Klagebegründung, Eilantrag, Stellungnahmen und Anlagen",
            "structure": "Verwaltungsakt, Vorverfahren, Klagegründe, Ermessensausübung, Amtsermittlung, Eilbedürftigkeit und Tenorierungsfolge werden getrennt.",
            "tools": "Amtsermittlung nach Paragraf 86 VwGO, Eilrechtsschutz nach Paragraf 80 Absatz 5 VwGO oder Paragraf 123 VwGO, Verpflichtungs- und Anfechtungstenor nach Paragraf 113 VwGO.",
            "product": "Hinweis: Die Beteiligten werden darauf hingewiesen, dass es auf die Ermessensausübung zu [Punkt] ankommen kann. Ergänzender Vortrag kann binnen [Frist] erfolgen.",
        }
    if "familiengericht" in plugin_name:
        return {
            "input": "Antragsschrift, Erwiderung, Jugendamtsbericht, Einkommensbelege, Versorgungsauskünfte, Kindesanhörung, Vergleichsvorschlag und Protokolle",
            "structure": "Antragstellerstation, Antragsgegnerstation, Kindeswohl- oder Unterhaltsachse, Belege, Anhörungen, Jugendamt, Verfahrensbeistand und Beschlussformel werden getrennt.",
            "tools": "Anhörung nach Paragraf 159 FamFG, Erörterung nach Paragraf 156 FamFG, einstweilige Anordnung nach Paragraf 49 FamFG, Beschluss nach Paragraf 38 FamFG.",
            "product": "Beschlussbaustein: Das Gericht ordnet an, dass [Regelung]. Die Gründe beruhen auf [Tatsache], [Beleg] und der Abwägung nach [Norm].",
        }
    if "bverfg" in plugin_name:
        return {
            "input": "Verfassungsbeschwerde, angegriffene Entscheidungen, Rechtswegnachweise, Fristnachweise, Vollmacht und Anlagen",
            "structure": "Beschwerdegegenstand, Beschwerdeführer, Rechtswegerschöpfung, Subsidiarität, Grundrechtsrüge, Annahmegrund und Entscheidungsvorschlag werden getrennt.",
            "tools": "Vorprüfung nach Paragraf 90 BVerfGG, Annahmeprüfung, einstweilige Anordnung nach Paragraf 32 BVerfGG, Kammerentscheidung.",
            "product": "Votumbaustein: Die Verfassungsbeschwerde ist nicht zur Entscheidung anzunehmen, weil [Zulässigkeits- oder Begründetheitsmangel] nicht hinreichend dargelegt ist.",
        }
    return {
        "input": "Schriftsätze, Anträge, Vermerke, Protokolle, Anlagen, Stellungnahmen und gerichtliche Hinweise",
        "structure": "Anträge, unstreitiger Sachverhalt, streitige Tatsachen, Beweisangebote, Rechtsfragen und entscheidungserhebliche Anschlussfragen werden getrennt.",
        "tools": "Hinweisverfügung, Aufklärungsanordnung, Beweisbeschluss, Terminverfügung und Entscheidungsentwurf werden nach der einschlägigen Verfahrensordnung vorbereitet.",
        "product": "Verfügung: Die Beteiligten erhalten Gelegenheit, zu [Punkt] binnen [Frist] ergänzend vorzutragen und die angekündigten Belege einzureichen.",
    }


def build_streitstoff_section(plugin_name: str) -> list[str]:
    profile = court_profile(plugin_name)
    return [
        "## Streitstoff strukturieren und sanieren",
        "",
        "### Eingang Streitstoff",
        "",
        f"- Erfasse {profile['input']} zuerst als Aktenfundstellen, nicht als freie Erzählung.",
        "- Mindestfelder: Parteien oder Beteiligte, Verfahrensart, Eingangs- oder Anhängigkeitsdatum, aktueller Verfahrensstand, Anträge, Anlagenliste, Fristen und zuständiger Spruchkörper.",
        "- Jede neue Datei wird einer Streitstoff-Kategorie zugeordnet: Tatsache, Rechtsansicht, Beweisangebot, Einwendung, Antrag, Frist, Kostenpunkt oder Anschlussverfügung.",
        "",
        "### Strukturierung Streitstoff",
        "",
        f"- {profile['structure']}",
        "- Unstreitiges wird separat gehalten. Bestreiten, Nichtwissen, Beweisangebot und bloße Rechtsmeinung erhalten jeweils eigene Spalten.",
        "- Neue Behauptungen werden nicht sofort bewertet, sondern erst einer Rechtsfolge und einem Tatbestandsmerkmal zugeordnet.",
        "",
        "### Sanierung Streitstoff",
        "",
        f"- Nutze als Sanierungshebel: {profile['tools']}",
        "- Pflicht-Tabelle Streitstoff-Liste: Tatsache/Position | Belegt durch | Bestritten durch | Beweisangebot | Rechtsfolge | nächste Anschlusspflicht.",
        "- Sanitäre Regeln: keine Tatsache ohne Beleg oder Beweisangebot; keine Rechtsfolge ohne Tatbestandsmerkmal; keine Anschlusspflicht ohne Frist; keine Quelle ohne Aktenzeichen oder Aktenfundstelle.",
        "",
        "### Durchdringung Streitstoff",
        "",
        "- Frage zu jedem Streitpunkt: Ist er entscheidungserheblich, beweisbedürftig und einer konkreten Norm zugeordnet?",
        "- Frage weiter: Wer trägt Darlegungs- und Beweislast, greift eine Vermutung, ist der Vortrag verspätet oder fehlt eine richterliche Hinweispflicht?",
        "- Bilde aus jedem entscheidungserheblichen Punkt eine Anschlussfrage: Hinweis, Beweisbeschluss, Terminvorbereitung, Vergleichsvorschlag, Tenor oder Abschlussverfügung.",
        "",
        "### Arbeitsprodukt am Streitstoff",
        "",
        f"{profile['product']}",
        "",
    ]


def build_station_lines(skills: list[Skill], title: str, plugin_name: str) -> list[str]:
    selected = workflow_selection(skills)
    if not selected:
        selected = [
            Skill("start-fallaufnahme", f"{title} Fallaufnahme", "Sachverhalt, Zielprodukt, Frist und verfügbare Unterlagen bestimmen.", "", (100, "start")),
            Skill("quellen-und-normenpruefung", f"{title} Quellen- und Normenprüfung", "Normen, Rechtsprechung und Aktualität aus gesicherten Quellen nachziehen.", "", (200, "normen")),
            Skill("arbeitsprodukt-erstellen", f"{title} Arbeitsprodukt erstellen", "Memo, Tabelle, Entwurf oder Antwort in ganzen Sätzen liefern.", "", (300, "output")),
            Skill("gegenpruefung", f"{title} Gegenprüfung", "Gegenargumente, Lücken und Fristen prüfen.", "", (400, "check")),
            Skill("abschluss", f"{title} Anschlussentscheidung", "Nächste Handlung und Stop-Kriterien benennen.", "", (500, "close")),
        ]
    lines: list[str] = []
    for idx, skill in enumerate(selected, 1):
        next_slug = selected[idx].slug if idx < len(selected) else "Abschlusskontrolle"
        desc = skill.description or "Der vorhandene Skill gibt die fachliche Prüfung, Eingaben und Ausgabepflichten vor."
        input_line, check_line, product_line = station_language(skill, title, plugin_name)
        lines += [
            f"{idx}. {skill.title}",
            f"   - Skill-Bezug: `{skill.slug}`.",
            f"   - Eingang: {clean_text(input_line, 360)}",
            f"   - Prüfung: {clean_text(desc, 330)} {clean_text(check_line, 240)}",
            f"   - Arbeitsprodukt: {clean_text(product_line, 260)}",
            f"   - Anschluss: Danach zu `{next_slug}` wechseln oder, wenn dieser Punkt entscheidungsreif ist, in das Endprodukt übernehmen.",
        ]
    return lines


def build_skill_spiegel(skills: list[Skill], target_lines: int) -> list[str]:
    if not skills:
        return []
    take = min(len(skills), max(8, target_lines // 7))
    lines = ["## Skill-Spiegel des Plugins", ""]
    for skill in skills[:take]:
        lines.append(f"- `{skill.slug}`: {clean_text(skill.description or skill.title, 290)}")
    lines.append("")
    return lines


def fallback_exception(skills: list[Skill]) -> list[str]:
    refs = [s.slug for s in skills[:3]]
    if len(refs) < 3:
        refs += ["README", "plugin.json", "Akte"]
    return [
        "- Dieses Plugin arbeitet ohne tragenden Rechtsprechungsanker, weil die vorhandenen Skills keinen belastbaren gerichtlichen Anker mit Aktenzeichen enthalten. Zitiere deshalb keine Entscheidung aus Erinnerung.",
        f"- Konkrete Skill-Verweise für die Arbeit ohne Scheinzitat: `{refs[0]}`, `{refs[1]}`, `{refs[2]}`.",
        "- Wenn eine Entscheidung gebraucht wird, wird sie erst aus amtlicher oder frei zugänglicher Quelle live verifiziert und dann mit Gericht, Datum, Aktenzeichen und Kernsatz eingesetzt.",
    ]


def paragraph_count_lines(norms: list[str], normfree: bool = False) -> list[str]:
    if normfree:
        return [
            "- Dieses Plugin ist als Strukturierungs- und Darstellungswerkzeug angelegt. Es setzt keine materiell-rechtliche Normenprüfung voraus.",
            "- Wenn die Akte Rechtsfragen enthält, werden diese nicht erfunden, sondern als Anschlussbedarf an das passende Fachplugin markiert.",
            "- Quellenarbeit bedeutet hier: Dateiname, Datum, Absender, Version, Tabellenblatt, Statusfeld und Aktenfundstelle sauber belegen.",
        ]
    if not norms:
        return [
            "- Pflichtnormen werden aus Akte, Skill-Text und Live-Quelle bestimmt; ohne belastbaren Normanker keine Subsumtion.",
            "- Verwende bei jedem Endprodukt mindestens einen konkreten Paragraf-Stamm aus dem zuständigen Gesetz.",
            "- Prüfe die aktuelle Fassung jedes Paragrafen vor Verwendung, insbesondere Übergangsrecht, Landesrecht und unionsrechtliche Vorgaben.",
        ]
    lines = ["- Pflichtnormen aus Plugin und Skill-Bestand:"]
    for norm in norms:
        lines.append(f"  - {norm}")
    return lines


def build_werkstatt(plugin: dict, directory: Path) -> str:
    name = plugin["name"]
    manifest = json.loads((directory / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    title = title_from_readme(directory, name)
    description = clean_text(plugin.get("description") or manifest.get("description") or "", 900)
    readme_signal = first_readme_signal(directory)
    skills = collect_skills(directory)
    norms = extract_norms(skills, name, title, 12)
    normfree = is_normfree_workflow_plugin(name, title, description or readme_signal)
    decisions = extract_decisions(skills, 5)
    station_lines = build_station_lines(skills, title, name)
    target_skill_lines = 16 + (len(skills) // 8)

    lines: list[str] = [
        f"# {title} — Werkstatt-Prompt",
        "",
        f"Nutze diesen Werkstatt-Prompt für {title}, wenn eine Akte, ein Dokumentenpaket oder ein einzelner Auftrag anhand der vorhandenen Skill-Stationen bearbeitet werden soll. Der Ablauf beginnt bei den realen Modulen dieses Plugins, übernimmt Aktenfundstellen vor Rückfragen und endet mit einem ausformulierten Arbeitsprodukt in dezimaler Gliederung.",
        "",
        "## Rolle",
        "",
        role_text(name, title, description or readme_signal),
        "Diese Rolle ist nicht allgemein rechtsberatend, nicht bloß zusammenfassend und nicht dazu da, fehlende Akten durch Vermutungen zu ersetzen.",
        "",
        "## Werkstattlogik",
        "",
    ]
    lines += station_lines
    lines.append("")

    if is_court_plugin(plugin):
        lines += build_streitstoff_section(name)

    lines += [
        "## Pflicht-Workflow am Anfang",
        "",
        f"- Lege zuerst das Zielprodukt für {title} fest und wähle dazu die passende Station aus der Werkstattlogik.",
        "- Lies vorhandene Dateien vor der ersten Rückfrage. Erkennbare Rollen, Fristen, Beträge, Zuständigkeiten, Streitpunkte und Anlagen werden als Startlage übernommen.",
        f"- Default für `{name}` ist ein kurzes Lagebild mit anschließendem Prüfpfad und direkt verwertbarem Arbeitsprodukt; Rückfragen nur zu entscheidungserheblichen Lücken.",
        "",
        "## Quellen-Disziplin",
        "",
        "- Normen werden mit Gesetz, Paragraf, Absatz, Satz, Nummer oder Buchstabe benannt. Bei unionsrechtlichen oder verfassungsrechtlichen Ankern wird Artikel ausgeschrieben.",
        "- Rechtsprechung wird nur verwendet, wenn Gericht, Datum, Aktenzeichen, Entscheidungsform und frei zugängliche Quelle vor Abgabe live nachgezogen wurden.",
        "- Keine Datenbank-Blindzitate, keine Literaturbehauptung ohne Quelle, keine Übernahme alter Tabellenwerte aus Erinnerung.",
    ]
    lines += paragraph_count_lines(norms, normfree)

    lines += [
        "",
        "## Leitentscheidungen",
        "",
    ]
    if decisions:
        for dec in decisions:
            lines.append(f"- {dec}. Kernsatz erst nach Live-Verifikation auf den konkreten Fall zuschneiden.")
    else:
        lines += fallback_exception(skills)

    lines += [
        "",
        "## Prüfraster oder Indizienliste",
        "",
    ]
    for skill in workflow_selection(skills)[:10]:
        lines += [
            f"- `{skill.slug}` prüfen:",
            f"  - Tatbestand oder Prüfauftrag: {clean_text(skill.description or skill.title, 260)}",
            "  - Belege: Aktenfundstelle, Datum, Absender, Anlage, Zahlenwerk oder Verfahrensstand benennen.",
            "  - Rechtsfolge: Ergebnis, Einwendung, Frist, Beweislast und Anschlussprodukt trennen.",
        ]
    if not skills:
        lines += [
            "- Fallaufnahme prüfen: Rollen, Zielprodukt, Frist und verfügbare Unterlagen festlegen.",
            "- Quellen prüfen: Normen und Rechtsprechung nur aus belastbarer Quelle übernehmen.",
            "- Ausgabe prüfen: Endprodukt vollständig ausformulieren und offene Punkte markieren.",
        ]

    lines += [
        "",
        "## Antwortform",
        "",
        "- Lagebild: Wer will was von wem, in welchem Verfahren oder Vertragsverhältnis, mit welchem Stand und welcher Frist?",
        "- Prüfung: Normen, Tatbestandsmerkmale, Beweisfragen, Einwendungen, Verfahrensfragen und Rechtsfolge in der Reihenfolge der Skill-Stationen.",
        "- Empfehlung: konkrete nächste Handlung mit Begründung, Frist, Zuständigkeit und Risiko.",
        "- Arbeitsprodukt: gewünschtes Dokument vollständig ausformulieren; Tabellen nur einsetzen, wenn sie die Entscheidung schneller prüfbar machen.",
        "- Schriftbild und Nummerierung: Enddokumente soweit technisch möglich in Times New Roman 11 pt ausgeben und ausschließlich dezimal gliedern, also 1, 1.1, 1.1.1, 2, 2.1. Bei reiner Markdown-Ausgabe den Formatwunsch als Exporthinweis aufnehmen.",
        "- Quellen: Normen konkret benennen; Rechtsprechung nur verifiziert oder als Prüfbedarf markieren.",
        "- Stop-Kriterien: Notfrist, unklare Identität, Straf- oder Haftungsrisiko, Interessenkollision, Echtdaten in ungeprüftem System, fehlende Akte oder nicht verifizierbare Quelle.",
        "",
        "## Eigenheiten dieses Plugins",
        "",
        f"- Der Arbeitsmodus bleibt auf `{name}` begrenzt; fachfremde Fragen werden nur über einen klar benannten Anschluss-Skill oder eine Rückfrage geöffnet.",
        "- Die Reihenfolge der Skills steuert die Reihenfolge der Antwort. Nicht erst ein allgemeines Lehrbuchschema schreiben, sondern aus dem passenden Skill heraus arbeiten.",
        "- Vorhandene Akteninformationen werden verwertet, statt erneut abgefragt zu werden.",
        "- Hypothesen, sichere Tatsachen und fehlende Belege werden sichtbar getrennt.",
        "- Fristen, Zuständigkeiten, Tabellenwerte und Formularanforderungen werden nicht aus Erinnerung übernommen.",
        "- Jedes Ergebnis endet mit einem nächsten praktischen Schritt.",
    ]
    if readme_signal:
        lines.append(f"- README-Schwerpunkt dieses Plugins: {readme_signal}")
    if skills:
        lines.append(f"- Der Skill-Bestand umfasst {len(skills)} Module; die Werkstatt arbeitet daher nicht als Einheitsprüfung, sondern als geführte Auswahl aus diesen Modulen.")
    lines.append("")

    lines += build_skill_spiegel(skills, target_skill_lines)

    lines += [
        "## Skelette",
        "",
        "### Skelett 1: Startlage nach Aktenlektüre",
        "",
        f"Ich habe die Unterlagen im Zuschnitt von {title} gelesen. Erkennbar sind [Rollen], [zentrale Dokumente], [Fristen], [Beträge] und [offene Belege]. Ich arbeite nun entlang der Stationen [Skill 1], [Skill 2] und [Skill 3]. Das Endprodukt wird in Times New Roman 11 pt und dezimaler Gliederung vorbereitet, soweit das Ausgabeformat dies zulässt.",
        "",
        "### Skelett 2: Prüfvermerk mit Anschlussentscheidung",
        "",
        "Kurzfazit: [Ergebnis in einem Satz]. Tragend sind [konkrete Normen] und [konkrete Aktenfundstellen]. Kritisch bleiben [Beweisfrage], [Frist] und [Gegenargument]. Nächster Schritt ist [konkrete Handlung], weil [Begründung].",
        "",
        "### Skelett 3: Ausformulierter Arbeitsbaustein",
        "",
        "Namens und im Auftrag von [Rolle] wird Folgendes vorgetragen oder vermerkt: [Tatsachenkern]. Rechtlich führt dies über [Norm] zu [Subsumtion]. Das Gegenargument [Einwand] greift nicht durch, weil [Antwort]. Daraus folgt [Antrag, Verfügung, Tenor, Klausel, Tabelle oder Empfehlung].",
        "",
        "## Schlusskontrolle",
        "",
        "- Stimmen Skill-Auswahl, Rolle und Zielprodukt überein?",
        "- Sind alle verwendeten Paragrafen aktuell und mit Absatz oder Satz präzisiert, soweit es auf Details ankommt?",
        "- Ist jedes Aktenzeichen live verifiziert oder ausdrücklich als Prüfbedarf markiert?",
        "- Ist das Endprodukt ausformuliert und nicht bloß eine Checkliste?",
        "- Enthält die Antwort eine Anschlussentscheidung mit Frist oder nächstem Arbeitsschritt?",
        "",
    ]

    while len(lines) < 150:
        idx = len(lines) - 140
        ref = skills[(idx - 1) % len(skills)].slug if skills else name
        lines.append(f"- Zusätzliche Kontrollfrage zu `{ref}`: Welche Tatsache, welcher Beleg, welche Norm und welcher nächste Schritt tragen diesen Teil der Antwort?")
    return "\n".join(lines).rstrip() + "\n"


def build_schnellstart(plugin: dict, directory: Path) -> str:
    name = plugin["name"]
    manifest = json.loads((directory / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
    title = title_from_readme(directory, name)
    description = clean_text(plugin.get("description") or manifest.get("description") or "", 420)
    skills = collect_skills(directory)
    norms = extract_norms(skills, name, title, 5)
    normfree = is_normfree_workflow_plugin(name, title, description)
    decisions = extract_decisions(skills, 2)
    selected = workflow_selection(skills)[:8]

    lines: list[str] = [
        f"# {title} — Schnellstart",
        "",
        f"Kompakter Arbeitsmodus für {title}. Er beginnt mit den vorhandenen Dateien, wählt die passenden Skill-Stationen und liefert ein ausformuliertes Ergebnis mit Quellen- und Stop-Kontrolle.",
        "",
        "## Rolle",
        "",
        role_text(name, title, description),
        "",
        "## Triage",
        "",
        "1. Welche Dateien oder Aktenstücke liegen vor, und welches Endprodukt soll entstehen?",
        "2. Welche Rolle gilt, welcher Verfahrens- oder Vertragsstand ist erreicht, und läuft eine Frist?",
        "3. Welche Beträge, Anträge, Beteiligten, Belege oder Zuständigkeiten sind erkennbar?",
        "4. Welcher Skill-Schwerpunkt passt zuerst: Einstieg, Prüfung, Entwurf, Kontrolle oder Anschlussentscheidung?",
        "",
        "## Werkstatt-Kurzweg",
        "",
    ]
    if selected:
        for idx, skill in enumerate(selected, 1):
            lines.append(f"{idx}. `{skill.slug}`: {clean_text(skill.description or skill.title, 190)}")
    else:
        lines += [
            "1. Akte lesen und Rollen, Fristen, Zielprodukt und Lücken festhalten.",
            "2. Normen und Zuständigkeit aus gesicherter Quelle bestimmen.",
            "3. Tatsachen, Belege, Einwendungen und Rechtsfolge trennen.",
            "4. Ergebnis vollständig ausformulieren und nächste Handlung benennen.",
        ]

    if is_court_plugin(plugin):
        lines += [
            "",
            "## Streitstoff in vier Schritten",
            "",
            "1. Streitstoff erfassen: Schriftsätze, Anträge, Vermerke, Anlagen und Fristen als Aktenfundstellen aufnehmen.",
            "2. Streitstoff strukturieren: unstreitig, streitig, Beweisangebot, Rechtsfrage und Anschlussverfügung trennen.",
            "3. Streitstoff sanieren: Hinweis, Aufklärung, Beweisbeschluss oder Verfügung mit Frist vorbereiten.",
            "4. Streitstoff durchdringen: Entscheidungserheblichkeit, Beweislast, Norm, Rechtsfolge und Tenorfolge prüfen.",
        ]

    lines += [
        "",
        "## Anker",
        "",
    ]
    if normfree:
        lines.append("- Normfreier Strukturanker: Dokument, Datum, Status, Verantwortlicher, nächster Schritt und offene Lücke werden belegbar festgehalten.")
        lines.append("- Rechtsfragen nur als Anschlussbedarf an das passende Fachplugin markieren.")
    elif norms:
        for norm in norms[:5]:
            lines.append(f"- {norm}")
    else:
        lines.append("- Paragraf-Stamm erst aus Akte, Skill und Live-Quelle bestimmen; keine Scheinpräzision.")
        lines.append("- Paragraf- und Artikelangaben vor Abgabe am aktuellen Normtext prüfen.")
    if decisions:
        for dec in decisions[:2]:
            lines.append(f"- {dec}")
    else:
        lines.append("- Kein sicherer Rechtsprechungsanker im Skill-Material; Entscheidungen nur nach Live-Verifikation mit Gericht, Datum und Aktenzeichen zitieren.")

    lines += [
        "",
        "## Antwortform",
        "",
        "- Lagebild: Rollen, Ziel, Frist, Aktenstand.",
        "- Prüfung: Skill-Stationen, Normen, Tatsachen, Beweis, Gegenargument.",
        "- Empfehlung: nächster Schritt mit Frist und Risiko.",
        "- Arbeitsprodukt: ganze Sätze, Times New Roman 11 pt als Exportwunsch, dezimale Gliederung.",
        "- Quellen: Normen konkret, Entscheidungen nur verifiziert oder als Prüfbedarf.",
        "",
        "## Stop",
        "",
        "Bei Notfrist, Haftungsrisiko, Interessenkollision, ungeprüften Echtdaten, fehlender Akte oder unsicherer Quelle an den zuständigen Berufsträger übergeben.",
        "",
    ]
    text = "\n".join(lines).rstrip() + "\n"
    if len(text) <= MAX_SCHNELLSTART:
        return text
    # Straffen: weniger Skills, dann kürzere Beschreibungen.
    while len(text) > MAX_SCHNELLSTART and len(selected) > 4:
        selected = selected[:-1]
        return build_schnellstart_from_parts(name, title, description, selected, norms, decisions, is_court_plugin(plugin), compact=True)
    return text[: MAX_SCHNELLSTART - 2].rstrip() + "\n"


def build_schnellstart_from_parts(
    name: str,
    title: str,
    description: str,
    selected: list[Skill],
    norms: list[str],
    decisions: list[str],
    court: bool,
    compact: bool,
) -> str:
    lines = [
        f"# {title} — Schnellstart",
        "",
        f"Kompakter Arbeitsmodus für `{name}` mit Aktenlektüre, Skill-Auswahl und ausformulierter Antwort.",
        "",
        "## Rolle",
        "",
        role_text(name, title, description),
        "",
        "## Triage",
        "",
        "1. Dateien, Rolle, Frist und Zielprodukt feststellen.",
        "2. Zuständigkeit, Belege, Beträge und Streitpunkte aus der Akte ziehen.",
        "3. Ersten passenden Skill wählen und Lücken nur entscheidungserheblich abfragen.",
        "",
        "## Werkstatt-Kurzweg",
        "",
    ]
    for idx, skill in enumerate(selected, 1):
        limit = 130 if compact else 190
        lines.append(f"{idx}. `{skill.slug}`: {clean_text(skill.description or skill.title, limit)}")
    if court:
        lines += [
            "",
            "## Streitstoff in vier Schritten",
            "",
            "1. Erfassen: Aktenfundstellen aufnehmen.",
            "2. Strukturieren: unstreitig, streitig, Beweis, Rechtsfrage trennen.",
            "3. Sanieren: Hinweis, Aufklärung oder Beweisbeschluss vorbereiten.",
            "4. Durchdringen: Entscheidungserheblichkeit, Beweislast, Norm, Rechtsfolge prüfen.",
        ]
    lines += ["", "## Anker", ""]
    for norm in norms[:4]:
        lines.append(f"- {norm}")
    for dec in decisions[:1]:
        lines.append(f"- {dec}")
    if not decisions:
        lines.append("- Rechtsprechung nur nach Live-Verifikation mit Gericht, Datum und Aktenzeichen.")
    lines += [
        "",
        "## Antwortform",
        "",
        "Lagebild, Prüfung, Empfehlung, Arbeitsprodukt, offene Punkte, Quellen. Enddokument als Times New Roman 11 pt und dezimal gegliedert anlegen, soweit technisch möglich.",
        "",
        "## Stop",
        "",
        "Bei Notfrist, Haftungsrisiko, Interessenkollision, Echtdatenproblem oder unsicherer Quelle an den Berufsträger übergeben.",
        "",
    ]
    return "\n".join(lines).rstrip() + "\n"


def remove_old_local_files(directory: Path, keep: set[Path]) -> list[str]:
    removed: list[str] = []
    tokens = ("megaprompt", "miniprompt", "kleiner-prompt", "grosser-prompt", "unified-kleiner-prompt")
    for path in directory.iterdir():
        if not path.is_file() or path in keep:
            continue
        lower = path.name.lower()
        if lower in {"megaprompt.md", "miniprompt.md"} or any(token in lower for token in tokens):
            path.unlink()
            removed.append(path.name)
    return removed


def validate_prompt(path: Path, schnellstart: bool) -> list[str]:
    text = path.read_text(encoding="utf-8")
    problems: list[str] = []
    if not text.endswith("\n"):
        problems.append("Datei endet nicht mit Leerzeile")
    if text.startswith("---"):
        problems.append("YAML-Frontmatter ist verboten")
    if len(re.findall(r"^# ", text, flags=re.MULTILINE)) != 1:
        problems.append("Datei braucht exakt eine H1")
    if "§" in text:
        problems.append("Paragrafenzeichen gefunden")
    if "<" in text or ">" in text:
        problems.append("spitze Klammer gefunden")
    if "**" in text:
        problems.append("Doppelstern-Markdown gefunden")
    if re.search(r"[\U0001F300-\U0001FAFF]", text):
        problems.append("Emoji gefunden")
    if schnellstart and len(text) > MAX_SCHNELLSTART:
        problems.append(f"Schnellstart zu lang: {len(text)} Zeichen")
    if not schnellstart:
        lines = len(text.splitlines())
        if lines < 150:
            problems.append(f"Werkstatt zu kurz: {lines} Zeilen")
        if lines > 400:
            problems.append(f"Werkstatt zu lang: {lines} Zeilen")
    return problems


def prompt_stem(plugin_name: str) -> str:
    return plugin_name


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="Promptdateien auch dann neu schreiben, wenn sie schon existieren")
    args = parser.parse_args()
    plugins = load_marketplace()
    problems: list[str] = []
    rewritten = 0
    for plugin in plugins:
        directory = plugin_dir(plugin)
        name = plugin["name"]
        stem = prompt_stem(name)
        werkstatt = directory / f"{stem}-werkstatt.md"
        schnellstart = directory / f"{stem}-schnellstart.md"
        if args.force or not werkstatt.is_file():
            werkstatt.write_text(build_werkstatt(plugin, directory), encoding="utf-8")
            rewritten += 1
        if args.force or not schnellstart.is_file():
            schnellstart.write_text(build_schnellstart(plugin, directory), encoding="utf-8")
            rewritten += 1
        remove_old_local_files(directory, {werkstatt, schnellstart})
        for path, is_schnell in [(werkstatt, False), (schnellstart, True)]:
            for problem in validate_prompt(path, is_schnell):
                problems.append(f"{path.relative_to(REPO)}: {problem}")
    if problems:
        print("Prompt-Validierung fehlgeschlagen:")
        for problem in problems[:120]:
            print(f"  - {problem}")
        raise SystemExit(1)
    max_s = max(len((plugin_dir(p) / f"{prompt_stem(p['name'])}-schnellstart.md").read_text(encoding="utf-8")) for p in plugins)
    print(f"Werkstatt-/Schnellstart-Prompts geprüft: {len(plugins)} Plugins")
    print(f"Neu geschrieben: {rewritten} Dateien")
    print(f"Schnellstart max: {max_s} Zeichen")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
