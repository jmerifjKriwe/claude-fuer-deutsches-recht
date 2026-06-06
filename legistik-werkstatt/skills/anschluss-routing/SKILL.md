---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Legistik Werkstatt** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen-legw-bmleh` — Allgemein Chronologie Fristen Legw Bmleh
- `begruendung-allgemein-und-besonders` — Begruendung Allgemein Und Besonders
- `dokumente-rendern-docx-pdf` — Dokumente Rendern Docx Pdf
- `europarechtskonformitaet` — Europarechtskonformitaet
- `folgenabschaetzung-erfuellungsaufwand` — Folgenabschaetzung Erfuellungsaufwand
- `folgenabschaetzung-erfuellungsaufwand-folgenabschaetzung` — Folgenabschaetzung Erfuellungsaufwand Folgenabschaetzung
- `folgenabschaetzung-nachhaltigkeit` — Folgenabschaetzung Nachhaltigkeit
- `formulierungshilfe-bauen` — Formulierungshilfe Bauen
- `gesetzesentwurf-kabinett` — Gesetzesentwurf Kabinett
- `gesetzgebungskompetenz-pruefen` — Gesetzgebungskompetenz Prüfen
- `goldplating-vermeiden` — Goldplating Vermeiden
- `goldplating-vermeiden-inkrafttreten-uebergangsrecht-legistik` — Goldplating Vermeiden Inkrafttreten Uebergangsrecht Legistik
- `inkrafttreten-uebergangsrecht` — Inkrafttreten Uebergangsrecht
- `laender-landtage-legistik-ministerien-opposition` — Länder Landtage Legistik Ministerien Opposition

## Arbeitsweg

- Ergebnis sichten: Welche Legistik Werkstatt-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Legistik-Werkstatt (Gesetzgebung).

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
