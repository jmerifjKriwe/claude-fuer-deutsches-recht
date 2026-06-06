---
name: anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Betreuungsrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-anschluss-router-workflow-chronologie` — Allgemein Anschluss Router Chronologie
- `aufgabenkreise-festlegen` — Aufgabenkreise Festlegen
- `bericht-betreuer-betreuerpflichten` — Bericht Betreuer Betreuerpflichten
- `betreuer-als-erbe` — Betreuer Als Erbe
- `betreuer-als-registrierung-betreuung-anwaltskosten` — Betreuer Als Registrierung Betreuung Anwaltskosten
- `betreuer-registrierung` — Betreuer Registrierung
- `betreuerpflichten-genehmigung-betreuung-interessen` — Betreuerpflichten Genehmigung Betreuung Interessen
- `betreuung-anwaltskosten-rvg` — Betreuung Anwaltskosten Rvg
- `betreuung-bei-demenz` — Betreuung Bei Demenz
- `betreuung-demenz-erbe-werden-erwachsene-kinder` — Betreuung Demenz Erbe Werden Erwachsene Kinder
- `betreuung-erbe-werden` — Betreuung Erbe Werden
- `betreuung-fuer-erwachsene-kinder` — Betreuung Für Erwachsene Kinder
- `betreuung-grenzueberschreitend` — Betreuung Grenzueberschreitend
- `betreuung-grenzueberschreitend-betreuungsantrag-erstellen` — Betreuung Grenzueberschreitend Betreuungsantrag Erstellen

## Arbeitsweg

- Ergebnis sichten: Welche Betreuungsrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Betreuungsrecht.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
