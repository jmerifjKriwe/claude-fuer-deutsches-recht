---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Fachanwalt Internationales Wirtschaftsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `bruessel-cisg-sonderfall-edge` — Bruessel Cisg Sonderfall Edge
- `embargo-fristennotiz-schiedsverfahren-wirtschaftsrecht` — Embargo Fristennotiz Schiedsverfahren Wirtschaftsrecht
- `fachanwalt-internationales-intwr-red` — Fachanwalt Internationales Intwr Red
- `gerichtsstand-rechtswahl-intwr-cisg-intwr-rom` — Gerichtsstand Rechtswahl Intwr Cisg Intwr Rom
- `investitionsschutz-kanzlei-lksg` — Investitionsschutz Kanzlei Lksg
- `iwr-arbitration-iwr-cisg-iwr-rechtswahl` — Iwr Arbitration Iwr Cisg Iwr Rechtswahl
- `iwr-cisg-iwr-brussels-iwr-icc` — Iwr Cisg Iwr Brussels Iwr Icc
- `iwr-einfuehrung-rechtsquellen` — Iwr Einfuehrung Rechtsquellen
- `mandat-triage-schriftsatzkern-substantiierung-aussenhandel` — Mandat Triage Schriftsatzkern Substantiierung Aussenhandel
- `orientierung-iwr-embargo-iwr-eu` — Orientierung Iwr Embargo Iwr Eu
- `sanktionen-erstgespraech-mandatsannahme-cisg` — Sanktionen Erstgespraech Mandatsannahme Cisg
- `schiedsklausel-intwr-eu-sanktions` — Schiedsklausel Intwr Eu Sanktions
- `schiedsklausel-intwr-schiedsklausel-grenzueberschreitender` — Schiedsklausel Intwr Schiedsklausel Grenzueberschreitender

## Arbeitsweg

- Ergebnis sichten: Welche Fachanwalt Internationales Wirtschaftsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Fachanwalt Internationales Wirtschaftsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
