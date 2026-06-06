---
name: forderungsmanagement-klagewerkstatt-anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Forderungsmanagement Klagewerkstatt** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `belegte-faellige-fmkw` — Belegte Faellige Fmkw
- `bgb-zpo-fmkw-saumselig-fmkw-titulierung` — Bgb Zpo Fmkw Saumselig Fmkw Titulierung
- `fmkw-mahnverfahren-bauleiter` — Fmkw Mahnverfahren Bauleiter
- `fmkw-saumselig-streitig-erfahrung-spezial` — Fmkw Saumselig Streitig Erfahrung Spezial
- `fmkw-titulierung-streckung-leitfaden` — Fmkw Titulierung Streckung Leitfaden
- `fmkw-verbraucherklage-cookies-rdg-spezial` — Fmkw Verbraucherklage Cookies Rdg Spezial
- `fmkw-verbraucherklage-forderung-anwaltshonorar-forderung` — Fmkw Verbraucherklage Forderung Anwaltshonorar Forderung
- `forderung-anwaltshonorar-rvg` — Forderung Anwaltshonorar Rvg
- `forderung-arzthonorar-goae` — Forderung Arzthonorar Goae
- `forderung-aus-werkvertrag-bgb-bau` — Forderung Aus Werkvertrag Bgb Bau
- `forderung-gegen-gesellschafter-13-gmbhg` — Forderung Gegen Gesellschafter 13 Gmbhg
- `forderung-gegen-gesellschafter-insolventen-schuldner-ausland` — Forderung Gegen Gesellschafter Insolventen Schuldner Ausland
- `forderung-gegen-insolventen-schuldner` — Forderung Gegen Insolventen Schuldner

## Arbeitsweg

- Ergebnis sichten: Welche Forderungsmanagement Klagewerkstatt-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Forderungsmanagement Klagewerkstatt.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
