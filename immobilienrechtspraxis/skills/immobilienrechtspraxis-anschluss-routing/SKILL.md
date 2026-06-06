---
name: immobilienrechtspraxis-anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Immobilienrechtspraxis** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `case-gegen-grundbuchanalyse` — Case Gegen Grundbuchanalyse
- `case-management-grundbuchanalyse-immo-aufteilungsplan` — Case Management Grundbuchanalyse Immo Aufteilungsplan
- `immo-bauliche-veraenderung-energieausweis-gewerbliche-mieter` — Immo Bauliche Veraenderung Energieausweis Gewerbliche Mieter
- `immo-bauvertrag-vob-kaufvertrag-grundstueck-mietkaufvertrag` — Immo Bauvertrag Vob Kaufvertrag Grundstueck Mietkaufvertrag
- `immo-grundschuld-bestellung-makler-honorar-wohnungseigentum` — Immo Grundschuld Bestellung Makler Honorar Wohnungseigentum
- `immo-immobilienrechtliche-live-beweislast` — Immo Immobilienrechtliche Live Beweislast
- `immo-zwangsversteigerung-frist-naechster-rechtsabteilungen` — Immo Zwangsversteigerung Frist Naechster Rechtsabteilungen
- `immor-bauvertrag-vob-erbbaurecht-vertrag-grundstueckskaufvertrag` — Immor Bauvertrag Vob Erbbaurecht Vertrag Grundstueckskaufvertrag
- `immor-bodenrichtwert-betriebskostenabrechnung-erstellen` — Immor Bodenrichtwert Betriebskostenabrechnung Erstellen
- `klauselschutz-vertragserstellung-vertragspruefung` — Klauselschutz Vertragserstellung Vertragspruefung
- `management-mieteranfragen-interessen-musterbasierte` — Management Mieteranfragen Interessen Musterbasierte
- `mieteranfragen-bearbeitung-projekt-arbeitsweise` — Mieteranfragen Bearbeitung Projekt Arbeitsweise
- `sachverhaltsermittlung-verifikation-sonderfall-werkzeuge` — Sachverhaltsermittlung Verifikation Sonderfall Werkzeuge

## Arbeitsweg

- Ergebnis sichten: Welche Immobilienrechtspraxis-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Immobilienrechtspraxis.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
