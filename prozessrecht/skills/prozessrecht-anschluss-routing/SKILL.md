---
name: prozessrecht-anschluss-routing
description: "Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad."
---

# Anschluss-Routing

## Einsatzlage

Dieses Anschluss-Routing für **Prozessrecht** wählt nach dem ersten Ergebnis die passende Vertiefung, Eskalation, Fristensicherung oder Dokumentenerstellung.

## Fachlandkarte dieses Plugins

- `allgemein-workflow-chronologie-workflow-fristen` — Allgemein Chronologie Fristen
- `amtlicher-zpo-proz-bauleiter-eilverfahren` — Amtlicher Zpo Proz Bauleiter Eilverfahren
- `anspruchstabelle` — Anspruchstabelle
- `anspruchstabelle-gegenseite-interessen-mahnbescheid` — Anspruchstabelle Gegenseite Interessen Mahnbescheid
- `beweissicherung-chronologie-einstweilige-verfuegung` — Beweissicherung Chronologie Einstweilige Verfuegung
- `gegenseite-status-mahnbescheid-mahnschreiben-aufnahme` — Gegenseite Status Mahnbescheid Mahnschreiben Aufnahme
- `mahnschreiben-entwurf-anwaltsgeheimnis` — Mahnschreiben Entwurf Anwaltsgeheimnis
- `mahnschreiben-erhalten-aktualisierung-aufnahme` — Mahnschreiben Erhalten Aktualisierung Aufnahme
- `mandat-briefing-mandat-schliessen-portfolio-status` — Mandat Briefing Mandat Schliessen Portfolio Status
- `mandat-mandate-prozessrecht` — Mandat Mandate Prozessrecht
- `proz-beweismittel-leitfaden-mediationsklage-guete` — Proz Beweismittel Leitfaden Mediationsklage Guete
- `prozessrecht-kaltstart-interview` — Prozessrecht Kaltstart Interview
- `prozessrecht-mandat-arbeitsbereich-abschnitt` — Prozessrecht Mandat Arbeitsbereich Abschnitt
- `prozessrechtliche-schriftsaetze-status` — Prozessrechtliche Schriftsaetze Status

## Arbeitsweg

- Ergebnis sichten: Welche Prozessrecht-Fragen sind nach diesem Skill beantwortet, welche bleiben offen oder neu entstehen?
- Anschlussweichen identifizieren: drohende Frist (die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren), notwendige Dokumente (Vertragsurkunden, Schriftsätze, Verwaltungsakte, Protokolle, Bescheide und externe Beweismittel des Fachgebiets), nächste Verfahrensstufe oder Sachgebiet.
- Konkreten Folge-Skill aus der Fachlandkarte oben benennen — nicht generisch "weitermachen", sondern Skill-Slug nennen.
- Eskalation an Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen oder Spezialisten klären, wenn der Vorgang die Skill-Grenze überschreitet.
- Mandantenkommunikation vorbereiten: Was muss der Mandant tun, bis wann, welche Unterlagen bringen, welche Risiken sind offen?

## Output

Routing-Entscheidung mit Anschluss-Skill, Reihenfolge, Abbruchkriterien und nächster Aktion innerhalb von Prozessrecht (ZPO/VwGO/StPO/SGG).

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.
