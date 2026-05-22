---
name: aktenauszug-erstellen
description: "Hauptworkflow Aktenauszug: verarbeitet PDFs Schriftsaetze und Akten und erzeugt einen strukturierten Auszug mit sechs Bausteinen — Verfahrensidentifikation Einleitungssatz Absatz-Zusammenfassung Sachverhaltschronologie Verfahrenschronologie tabellarische Gegenueber­stellung Parteivortrag Beweis und Rechtsargumente. Output in Markdown."
---

# Aktenauszug Erstellen — Hauptworkflow

## Leitidee

Wer ein Gerichtsverfahren schnell erfassen muss — sei es beim Mandatswechsel, bei der Einarbeitung eines neuen Sachbearbeiters oder bei der Vorbereitung auf eine mündliche Verhandlung — benötigt einen strukturierten Überblick. Dieser Skill nimmt die gesamte Akte entgegen und erzeugt einen vollständigen Aktenauszug mit allen sechs Bausteinen.

## Voraussetzungen

- Gerichtliche Akte oder wesentliche Teile davon (PDF, Word, maschinenlesbar)
- Optional: Inhaltsverzeichnis der Akte
- Optional: Hinweis auf die Verfahrensart (Zivil, Straf, Verwaltung, Arbeit, Sozial)

## Sechs Bausteine des Aktenauszugs

### Baustein 1 — Verfahrensidentifikation

Gericht, Kammer/Senat, Aktenzeichen, Streitwert, Parteien mit Anwälten, Instanz, Verfahrensart.

### Baustein 2 — Einleitungssatz

Ein bis zwei Sätze, die den Kern des Rechtsstreits nennen: Wer streitet mit wem worüber, welche Hauptnorm ist einschlägig.

### Baustein 3 — Zusammenfassung (Absatz)

Acht bis zehn Sätze: Hintergrund, Streitstand, prozessuale Lage, anstehende Verfahrenshandlungen.

### Baustein 4 — Sachverhaltschronologie

Chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen. Datum fettgedruckt vorangestellt.

### Baustein 5 — Verfahrenschronologie

Chronologische Bullet-Liste der prozessualen Schritte. Fristen und Termine werden hervorgehoben.

### Baustein 6 — Tabellen (Parteivortrag / Beweismittel / Rechtsargumente)

Drei separate Tabellen im Markdown-Format mit Spalten für Klägerseite und Beklagtenseite.

## Arbeitsschritte

1. Akte sichten — Inhaltsverzeichnis oder Seitenstruktur erfassen
2. Verfahrensidentifikation extrahieren (→ Skill `verfahrensidentifikation`)
3. Einleitungssatz formulieren (→ Skill `einleitungssatz-generator`)
4. Zusammenfassungsabsatz schreiben (→ Skill `verfahrenszusammenfassung-absatz`)
5. Sachverhalt chronologisch ordnen (→ Skill `sachverhaltschronologie`)
6. Verfahrensschritte chronologisch ordnen (→ Skill `verfahrenschronologie`)
7. Fristen hervorheben (→ Skill `fristen-und-terminkalender`)
8. Parteivortrag gegenüberstellen (→ Skill `parteivortrag-gegenueberstellung`)
9. Beweismittel tabellarisch erfassen (→ Skill `beweismittel-gegenueberstellung`)
10. Rechtsargumente tabellarisch erfassen (→ Skill `rechtsargumente-gegenueberstellung`)
11. Neutralitätsprüfung (→ Skill `neutralitaetspruefung`)
12. Strukturprüfung (→ Skill `aktenauszug-strukturpruefung`)

## Output-Format

```markdown
# Aktenauszug — [Aktenzeichen]

## Verfahrensidentifikation
...

## Einleitungssatz
...

## Zusammenfassung
...

## Sachverhaltschronologie
- **TT.MM.JJJJ** Beschreibung
- **TT.MM.JJJJ** Beschreibung

## Verfahrenschronologie
- **TT.MM.JJJJ** Beschreibung
- ⚠️ **TT.MM.JJJJ — FRIST:** Beschreibung

## Parteivortrag

| Punkt | Klägerseite | Beklagtenseite |
|---|---|---|

## Beweismittel

| Beweismittel | Klägerseite | Beklagtenseite |
|---|---|---|

## Rechtsargumente

| Aspekt | Klägerseite | Beklagtenseite |
|---|---|---|
```

## Qualitätsgrundsätze

- Keine Erfolgsprognose
- Neutrale Sprache ohne Wertung
- Alle Fristen und Termine hervorgehoben
- Keine KI-Terminologie im Output

## Hinweis

Der Aktenauszug ersetzt nicht die eigene Aktenlektüre. Er ist ein strukturiertes Arbeits- und Kommunikationsmittel für den anwaltlichen Alltag und bedarf der Prüfung durch den verantwortlichen Rechtsanwalt.
