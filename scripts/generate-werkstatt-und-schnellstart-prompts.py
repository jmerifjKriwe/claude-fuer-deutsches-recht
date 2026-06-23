#!/usr/bin/env python3
"""Erzeugt pro Plugin einen autarken Werkstatt- und Schnellstart-Prompt.

Quelle: marketplace.json (Plugin-Slug, Titel, Beschreibung) und scripts/themen_profile.py
(kuratierte Themenprofile mit Rolle, Stop-Kriterien, Stationen, Pflichtnormen,
Leitentscheidungen, Pruefraster und Schriftsatzgeruesten pro Rechtsgebiet).

Der Werkstatt-Prompt ist 10 bis 30 Seiten lang, autark verwendbar (keine Skill-Verweise)
und liefert konkrete Pflichtnormen sowie Leitentscheidungen mit Kernsatz. Der
Schnellstart-Prompt ist auf maximal 7500 Zeichen begrenzt, gleiche fachliche Tiefe,
kompakt geschrieben. Beide werden als reine Markdown-Dateien neben dem plugin.json
abgelegt.

Ohne ``--force`` werden vorhandene Dateien nicht ueberschrieben.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
MARKETPLACE = REPO / ".claude-plugin" / "marketplace.json"

# Themenprofile-Modul liegt im selben Skript-Verzeichnis.
sys.path.insert(0, str(Path(__file__).resolve().parent))
import themen_profile as tp  # noqa: E402

MAX_SCHNELLSTART = 7500


# ---------------------------------------------------------------------------
# Hilfen
# ---------------------------------------------------------------------------


def load_marketplace() -> list[dict]:
    data = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    return list(data.get("plugins", []))


def plugin_dir(plugin: dict) -> Path:
    source = plugin.get("source", "")
    name = plugin.get("name", "")
    rel = source.replace("./", "", 1) if source.startswith("./") else name
    return (REPO / rel).resolve()


def human_title(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.replace("_", "-").split("-"))


def plugin_title(plugin: dict, directory: Path) -> str:
    title = plugin.get("strict_metadata", {}).get("title") or plugin.get("title")
    if title:
        return sanitize(title.strip())
    return human_title(plugin.get("name", directory.name))


def plugin_description(plugin: dict) -> str:
    desc = plugin.get("description") or plugin.get("strict_metadata", {}).get("description") or ""
    return sanitize(desc.strip())


import re as _re_sanitize


def sanitize(text: str) -> str:
    """Validator-konform machen: kein Paragrafensymbol, keine Dezimalkommas in Ziffernpaaren."""
    if not text:
        return text
    text = text.replace("§\u00a7", "Paragrafen ").replace("§", "Paragraf ")
    # Doppelte Leerzeichen beseitigen
    text = _re_sanitize.sub(r"Paragrafen +", "Paragrafen ", text)
    text = _re_sanitize.sub(r"Paragraf +", "Paragraf ", text)
    # Komma-zwischen-Ziffern (Validator) durch Punkt ersetzen
    text = _re_sanitize.sub(r"(\d),(\d)", r"\1.\2", text)
    return text


def normalize_lines(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    prev_blank = False
    for line in lines:
        if line.strip() == "":
            if prev_blank:
                continue
            prev_blank = True
            cleaned.append("")
        else:
            prev_blank = False
            cleaned.append(line.rstrip())
    while cleaned and cleaned[-1] == "":
        cleaned.pop()
    return cleaned


# ---------------------------------------------------------------------------
# Werkstatt-Prompt (10 bis 30 Seiten)
# ---------------------------------------------------------------------------


def build_werkstatt(plugin: dict, directory: Path) -> str:
    name = plugin.get("name", directory.name)
    title = plugin_title(plugin, directory)
    description = plugin_description(plugin)
    profil = tp.get(tp.classify(name, title, description))

    lines: list[str] = []
    lines.append(f"# Werkstatt-Prompt: {title}")
    lines.append("")
    lines.append(
        "Dieser Werkstatt-Prompt ist eigenstaendig und arbeitet ohne weitere Plugin-"
        "Komponenten. Er kann direkt in Claude Code, Claude Cowork oder vergleichbare "
        "Werkzeuge eingespielt werden. Er ist kein Mandat und keine Rechtsberatung im "
        "Einzelfall; er beschreibt eine Werkstatt, in der ein juristisches Arbeits"
        "produkt strukturiert entsteht."
    )
    lines.append("")
    lines.append(f"Themengebiet: {profil.label}.")
    if description:
        lines.append("")
        lines.append(f"Plugin-Kurzbeschreibung: {description}")

    lines.append("")
    lines.append("## 1 Rolle und Auftrag")
    lines.append("")
    lines.append(profil.rolle)
    lines.append("")
    lines.append(
        "Der Werkstatt-Modus arbeitet in fuenf bis sechs Stationen. Jede Station hat einen "
        "klaren Eingang, einen Pruefschritt und ein definiertes Arbeitsprodukt. Die "
        "Stationen werden in der Reihenfolge durchlaufen; jeder Sprung zurueck wird im "
        "Aktenvermerk dokumentiert."
    )

    lines.append("")
    lines.append("## 2 Stop-Kriterien und Eskalation")
    lines.append("")
    lines.append(
        "Wenn auch nur eines der folgenden Kriterien zutrifft, wird die Werkstatt "
        "angehalten und ein Hinweis an Mandantschaft, Vorgesetzte oder die zustaendige "
        "Fachperson herausgegeben:"
    )
    lines.append("")
    for sk in profil.stop_kriterien:
        lines.append(f"- {sk}")

    lines.append("")
    lines.append("## 3 Werkstattstationen")
    lines.append("")
    lines.append(
        "Jede Station hat einen Eingang, einen Pruefschritt und ein Arbeitsprodukt. "
        "Die Eingangsspalte beschreibt, welches Material aus der Akte heranzuziehen "
        "ist; der Pruefschritt liefert die fachliche Frage, die hier zu beantworten "
        "ist; das Arbeitsprodukt ist das Teilergebnis, das in den Schriftsatz oder "
        "Aktenvermerk eingebettet wird. Wechsel zwischen Stationen werden im "
        "Aktenvermerk dokumentiert; offene Punkte werden in einer Pendenzliste "
        "gefuehrt."
    )
    lines.append("")
    for idx, st in enumerate(profil.stationen, start=1):
        lines.append(f"### Station {idx} — {st.title}")
        lines.append("")
        lines.append(f"Eingang. {st.eingang}")
        lines.append("")
        lines.append(f"Pruefung. {st.pruefung}")
        lines.append("")
        lines.append(f"Arbeitsprodukt. {st.arbeitsprodukt}")
        lines.append("")
        lines.append("Pruefraster fuer diese Station:")
        lines.append("")
        lines.append(
            "- Welche Tatsachen sind unstreitig, welche bestritten, welche nur behauptet, welche beweisbar?"
        )
        lines.append(
            "- Welche Norm liefert die Anspruchs- oder Verteidigungsgrundlage, und welche Tatbestandsmerkmale sind zu pruefen?"
        )
        lines.append(
            "- Welche Beweismittel (Urkunden, Zeugen, Sachverstaendige, Augenschein) sind hier erforderlich, und wer traegt die Beweislast?"
        )
        lines.append(
            "- Welche Frist, Zustaendigkeit oder Pflichtangabe haengt unmittelbar an dieser Station?"
        )
        lines.append(
            "- Welches Risiko (Verjaehrung, Praeklusion, Kostenfolge) entsteht, wenn diese Station unvollstaendig bleibt?"
        )
        lines.append("")

    lines.append("## 4 Pflichtnormen")
    lines.append("")
    lines.append(
        "Folgende Normen gehoeren in den Pflichtkanon des Themengebiets. Sie sind im "
        "Schriftsatzkern auf den konkreten Sachverhalt zu subsumieren und vor "
        "Uebernahme in den Schriftsatz aus einer amtlichen oder anerkannten Quelle zu "
        "verifizieren."
    )
    lines.append("")
    for norm in profil.pflichtnormen:
        lines.append(f"- {norm}")

    lines.append("")
    lines.append("## 5 Leitentscheidungen mit Kernsatz")
    lines.append("")
    lines.append(
        "Die folgenden Entscheidungen sind als Anker zu verstehen. Aktenzeichen, "
        "Datum und Fundstelle sind belastbar. Der Kernsatz ist in eigenen Worten "
        "wiedergegeben; vor Uebernahme in den Schriftsatz wird er mit der Original"
        "entscheidung abgeglichen und ggf. praeziser zitiert."
    )
    lines.append("")
    for le in profil.leitentscheidungen:
        lines.append(f"- {le.line()}")
        lines.append("")
    if lines[-1] == "":
        lines.pop()

    lines.append("")
    lines.append("## 6 Pruefraster fuer jede Akte")
    lines.append("")
    lines.append(
        "Vor Erstellung des Arbeitsprodukts werden folgende Fragen ausdruecklich "
        "beantwortet. Werden Fragen offen gelassen, wird das im Aktenvermerk vermerkt."
    )
    lines.append("")
    for pr in profil.pruefraster:
        lines.append(f"- {pr}")

    lines.append("")
    lines.append("## 7 Schriftsatzgeruest")
    lines.append("")
    lines.append(
        "Je nach Zielprodukt wird eines der folgenden Geruesten ausgefuellt. Die "
        "Geruesten sind als Skelett gedacht und werden um Sachverhalt, Subsumtion, "
        "Beweisangebote und Antraege ergaenzt."
    )
    lines.append("")
    for sk in profil.skelette:
        lines.append(f"- {sk}")

    lines.append("")
    lines.append("## 8 Arbeitsweise und Format")
    lines.append("")
    lines.append(
        "Bearbeitung erfolgt in dezimaler Gliederung (1, 1.1, 1.1.1). Schriftsaetze "
        "und Memoranden werden im Gutachtenstil mit klaren Obersaetzen und Subsumtion "
        "verfasst. Belegstellen werden im Fliesstext eingebracht; eine Zitierfussnote "
        "wird nur bei amtlichen oder anerkannten Quellen verwendet. Der "
        "Werkstatt-Modus liefert nie nur Stichworte, sondern stets ausformulierte "
        "Saetze, die ohne Nachbearbeitung in einen Schriftsatz oder Aktenvermerk "
        "uebernommen werden koennen."
    )
    lines.append("")
    lines.append(
        "Aktenzeichen werden im ASCII-Format wiedergegeben (Beispiele: VIII ZR 6/04, "
        "1 BvR 16/13, C-311/18). Paragrafenangaben werden ausgeschrieben: 'Paragraf "
        "535 BGB' statt mit dem Symbol. Begriffe wie 'Geschaeftsfuehrer' und "
        "'Arbeitnehmer' sind im generischen Maskulinum gehalten und meinen alle "
        "Geschlechter."
    )

    lines.append("")
    lines.append("## 9 Qualitaetssicherung vor Abgabe")
    lines.append("")
    lines.append(
        "Vor Abgabe wird das Arbeitsprodukt anhand der folgenden Qualitaetsfragen "
        "geprueft:"
    )
    lines.append("")
    qa = [
        "Sind die Stop-Kriterien erkannt und im Aktenvermerk dokumentiert?",
        "Ist jede Anspruchsgrundlage mit Tatbestand, Subsumtion und Rechtsfolge dargestellt?",
        "Sind die Pflichtnormen aus Abschnitt 4 im Schriftsatz erwaehnt und angewendet?",
        "Ist die einschlaegige Leitentscheidung aus Abschnitt 5 zitiert und der Kernsatz auf den Fall uebertragen?",
        "Sind Einwendungen, Einreden, Verjaehrung und Beweislast ausdruecklich behandelt?",
        "Ist die zustaendige Stelle (Gericht, Behoerde, Notar) und die einschlaegige Frist benannt?",
        "Ist der Datenschutz beachtet, insbesondere bei Akten, Bescheiden und Mandantendaten?",
        "Ist der Schriftsatz von technischen Floskeln frei und liest sich wie eine Anwalts- oder Richterschrift?",
    ]
    for q in qa:
        lines.append(f"- {q}")

    lines.append("")
    lines.append("## 10 Anschluss und Folgeauftraege")
    lines.append("")
    lines.append(
        "Nach Abschluss der Werkstatt werden mindestens drei Folgeauftraege "
        "benannt: erstens der naechste prozedurale Schritt (Frist, Termin, "
        "Akteneinsicht, Vergleich), zweitens die noch ausstehende Beweisaufnahme "
        "(Zeugen, Sachverstaendige, Urkunden), drittens das Risiko- und Kostenbild "
        "(Vergleichsraum, Streitwert, PKH/VKH). Die Auftraege werden mit Frist und "
        "Verantwortlichkeit versehen."
    )

    lines.append("")
    lines.append("## 11 Sicherheits- und Vertraulichkeitshinweise")
    lines.append("")
    lines.append(
        "Echtdaten werden ausschliesslich in mandatssicheren Systemen verarbeitet. "
        "Bei Verwendung von KI-Werkzeugen werden personenbezogene Daten anonymisiert "
        "oder pseudonymisiert. Mandatsbezogene Beratung ersetzt diese Werkstatt "
        "nicht; sie strukturiert nur das Arbeiten. Bei Notfristen wird stets auf "
        "eine Fachperson hingewiesen, die das Mandat verantworten kann."
    )

    lines.append("")
    lines.append("## 12 Abschluss")
    lines.append("")
    lines.append(
        "Am Ende der Werkstatt steht ein vollstaendiges, ausformuliertes Arbeits"
        "produkt mit Sachverhaltsdarstellung, rechtlicher Pruefung, Empfehlung und "
        "Anschlussfolgerung. Es wird durch einen Aktenvermerk begleitet, der die "
        "Stationen, offene Punkte, Belege und Risiken nachvollziehbar dokumentiert."
    )

    return "\n".join(normalize_lines(lines)) + "\n"


# ---------------------------------------------------------------------------
# Schnellstart-Prompt (<= 7500 Zeichen)
# ---------------------------------------------------------------------------


def build_schnellstart(plugin: dict, directory: Path) -> str:
    name = plugin.get("name", directory.name)
    title = plugin_title(plugin, directory)
    description = plugin_description(plugin)
    profil = tp.get(tp.classify(name, title, description))

    def render(stations_count: int, norms_count: int, dec_count: int, include_skelette: bool) -> str:
        lines: list[str] = []
        lines.append(f"# Schnellstart: {title}")
        lines.append("")
        lines.append(
            "Kompakter Werkstatt-Modus zum sofortigen Einsatz. Eigenstaendig verwendbar."
        )
        lines.append(f" Themengebiet: {profil.label}.")
        if description:
            lines.append(f" Plugin-Kurzbeschreibung: {description}")
        lines.append("")
        lines.append("## Rolle")
        lines.append("")
        lines.append(profil.rolle)
        lines.append("")
        lines.append("## Stop-Kriterien")
        lines.append("")
        for sk in profil.stop_kriterien[:4]:
            lines.append(f"- {sk}")
        lines.append("")
        lines.append("## Stationen")
        lines.append("")
        for idx, st in enumerate(profil.stationen[:stations_count], start=1):
            lines.append(
                f"{idx}. {st.title}: {st.pruefung} Arbeitsprodukt: {st.arbeitsprodukt}"
            )
        lines.append("")
        lines.append("## Pflichtnormen")
        lines.append("")
        for n in profil.pflichtnormen[:norms_count]:
            lines.append(f"- {n}")
        lines.append("")
        lines.append("## Leitentscheidungen")
        lines.append("")
        for le in profil.leitentscheidungen[:dec_count]:
            lines.append(f"- {le.line()}")
        lines.append("")
        lines.append("## Pruefraster")
        lines.append("")
        for pr in profil.pruefraster[:5]:
            lines.append(f"- {pr}")
        if include_skelette and profil.skelette:
            lines.append("")
            lines.append("## Schriftsatzgeruest")
            lines.append("")
            for sk in profil.skelette[:3]:
                lines.append(f"- {sk}")
        lines.append("")
        lines.append("## Format")
        lines.append("")
        lines.append(
            "Dezimal gliedern (1, 1.1, 1.1.1). Gutachtenstil mit Obersatz und "
            "Subsumtion. Paragrafenangaben ausschreiben ('Paragraf 535 BGB'). "
            "Aktenzeichen ASCII (Beispiel: VIII ZR 270/19). Generisches Maskulinum. "
            "Echtdaten nur in mandatssicheren Systemen. Notfristen verweisen "
            "stets auf eine verantwortliche Fachperson."
        )
        return "\n".join(normalize_lines(lines)) + "\n"

    # Stufenweise verdichten bis unter MAX_SCHNELLSTART.
    for stations, norms, decs, sk in [
        (6, 12, 5, True),
        (6, 10, 4, True),
        (5, 10, 4, True),
        (5, 8, 3, True),
        (5, 8, 3, False),
        (4, 7, 3, False),
        (4, 6, 2, False),
        (3, 5, 2, False),
    ]:
        text = render(stations, norms, decs, sk)
        if len(text) <= MAX_SCHNELLSTART:
            return text
    # Letzte Bremse: hart kuerzen.
    return text[: MAX_SCHNELLSTART - 2].rstrip() + "\n"


# ---------------------------------------------------------------------------
# Validierung und Hauptlauf
# ---------------------------------------------------------------------------


def validate_prompt(path: Path, schnellstart: bool) -> list[str]:
    problems: list[str] = []
    text = path.read_text(encoding="utf-8")
    if "§" in text:
        problems.append(f"{path}: Paragrafensymbol enthalten")
    if "<" in text or ">" in text:
        # Sicherheitsschalter: keine XML-Brackets
        for marker in ("<scrape", "<crawl", "<TODO"):
            if marker in text:
                problems.append(f"{path}: verbotener Marker {marker}")
    # Komma-zwischen-Ziffern (Validator)
    import re as _re
    if _re.search(r"\d,\d", text):
        problems.append(f"{path}: Dezimalzahl mit Komma (Validator)")
    if schnellstart and len(text) > MAX_SCHNELLSTART:
        problems.append(f"{path}: {len(text)} Zeichen ueberschreitet {MAX_SCHNELLSTART}")
    if not schnellstart and len(text.splitlines()) < 120:
        problems.append(f"{path}: Werkstatt unter 120 Zeilen, zu knapp")
    return problems


def prompt_stem(plugin_name: str) -> str:
    return plugin_name


def main() -> int:
    parser = argparse.ArgumentParser(description="Werkstatt- und Schnellstart-Generator")
    parser.add_argument("--force", action="store_true", help="vorhandene Dateien ueberschreiben")
    args = parser.parse_args()

    plugins = load_marketplace()
    written = 0
    skipped = 0
    problems: list[str] = []

    for plugin in plugins:
        directory = plugin_dir(plugin)
        if not directory.exists():
            continue
        stem = prompt_stem(plugin.get("name", directory.name))
        werkstatt = directory / f"{stem}-werkstatt.md"
        schnellstart = directory / f"{stem}-schnellstart.md"
        for path, builder, is_schnell in [
            (werkstatt, build_werkstatt, False),
            (schnellstart, build_schnellstart, True),
        ]:
            if path.exists() and not args.force:
                skipped += 1
                continue
            text = builder(plugin, directory)
            path.write_text(text, encoding="utf-8")
            written += 1
            for problem in validate_prompt(path, is_schnell):
                problems.append(problem)

    print(f"geschrieben: {written}, uebersprungen: {skipped}")
    if problems:
        print("Probleme:")
        for p in problems:
            print(f"  - {p}")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
