---
name: anwaltsschriftsatz-stilrichtlinie
description: "Stilrichtlinie fuer den juristisch sauberen neutralen und fuer Anwaelte lesbaren Aktenauszug: Sprache Gliederung Nomenklatur Abkuerzungskonventionen Tabellengestaltung und Markdown-Formatierung. Verbindliche Stilregeln fuer alle Bausteine des Aktenauszugs."
---

# Anwaltsschriftsatz-Stilrichtlinie

## Zweck

Diese Stilrichtlinie legt verbindliche Regeln für Sprache, Gliederung und Formatierung des Aktenauszugs fest. Sie sichert, dass der Aktenauszug dem professionellen Standard entspricht, den Rechtsanwältinnen und Rechtsanwälte in ihrer täglichen Arbeit erwarten.

## Sprache

### Allgemeine Grundsätze

- **Sachlich und präzise:** Jeder Satz transportiert eine Information. Füllphrasen vermeiden.
- **Juristisch korrekt:** Rechtsbegriffe werden in ihrer gesetzlichen oder gefestigten dogmatischen Bedeutung verwendet.
- **Neutral:** Keine Wertungen, keine Erfolgsprognosen (→ Skill `neutralitaetspruefung`).
- **Aktiv bevorzugen:** „Die Klägerin macht geltend" — nicht „Es wird geltend gemacht".

### Verbotene Begriffe

Keine Begriffe aus dem Bereich kommerzieller Textverarbeitungssoftware oder Assistenzsysteme. Keine Formulierungen wie „basierend auf meiner Analyse" oder „nach meiner Einschätzung". Keine Ich-Form.

### Parteibezeichnungen

- Konsistente Verwendung im gesamten Aktenauszug
- Zulässig: vollständiger Name, Kurzname, Parteibezeichnung (die Klägerin)
- Nicht mischen: nicht „Klägerin" in einem Abschnitt und „Frau Müller" im nächsten
- Abkürzungen (Kl., Bekl.) nur in Tabellen, nicht in Fließtext

### Normen und Paragraphen

- Vollständige Angabe bei erster Nennung: § 634 Nr. 4 i.V.m. § 280 Abs. 1 BGB
- Abkürzung bei Wiederholung möglich: § 634a Abs. 1 Nr. 1 BGB (Verjährung)
- Gesetze stets mit Kurzbezeichnung: BGB, ZPO, StPO, VwGO, ArbGG, SGG, KSchG, GKG

## Gliederung

### Überschriften-Hierarchie

```
# Aktenauszug — [Aktenzeichen]          (H1 — nur einmal)
## Verfahrensidentifikation              (H2 — Bausteine)
### Parteien                             (H3 — Unterabschnitte)
#### Klägerseite                         (H4 — bei Bedarf)
```

### Abschnittstrennungen

Jeder Baustein beginnt auf einer neuen Hierarchieebene. Zwischen Bausteinen eine Leerzeile.

## Tabellen

### Formatierung

- Markdown-Tabellen mit Pipes und Trennzeile
- Spaltenbreite nicht fixieren (Markdown passt sich an)
- Spaltenköpfe fett oder als Header-Zeile

### Tabellenstil

| Gut | Nicht gut |
|---|---|
| Klägerin / Beklagte als Spaltenköpfe | Kl. / Bekl. |
| Kurze präzise Zellinhalte | Lange Fließtextabsätze in Zellen |
| Fundstellen in separater Spalte | Fundstellen ohne Quelle |

## Datumsformat

- Vollständig: TT.MM.JJJJ (z. B. 15.03.2021)
- Kein ISO-Format (2021-03-15) im Aktenauszug-Body
- Monats-/Jahresangaben: März 2021 (nicht 03/2021)

## Beträge

- Immer mit EUR-Präfix: EUR 45.000
- Keine Tausenderpunkte in Zahlen: EUR 45000 oder EUR 45.000 (Punkt als Tausendertrenner ist im Deutschen üblich)
- Keine Abkürzung T€ oder TEUR im Aktenauszug (ausgeschrieben)

## Aktenzeichen

Format: [Gericht-Kürzel] [Senats-/Kammernummer] [Verfahrensart] [Laufnummer]/[Jahr]

Beispiele: 3 O 123/23 (LG) — 12 U 45/24 (OLG) — VI ZR 67/24 (BGH)

## Markdown-Besonderheiten

- Fettdruck (`**Text**`) für Daten in Chronologien
- Kursiv (`*Text*`) sparsam — für Gesetzesbegriffe oder Fremdwörter
- Code-Blöcke (` ``` `) für Musterformulierungen und Vorlagen
- Fristenboxen hervorheben (Tabelle oder Blockquote mit ⚠️)

## Qualitätscheck Stil

- [ ] Keine wertenden Adjektive ohne Quellenattribution?
- [ ] Parteibezeichnungen konsistent?
- [ ] Normen vollständig angegeben?
- [ ] Datumsformat einheitlich TT.MM.JJJJ?
- [ ] Beträge mit EUR-Präfix?
- [ ] Überschriften-Hierarchie korrekt?
