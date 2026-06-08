---
name: einarbeitung-fehlerkatalog
description: "Einarbeitung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Einarbeitung Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Aktenauszug Gerichtsverfahren** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `aktenauszug-strukturpruefung-akzg-bauleiter-vertraulichkeit`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `akzg-zeitstrahl-anlagenverzeichnis-extrakt-anwaltsschriftsatz`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `anwaltsschriftsatz-beweislast-beweismittel-interessen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `arbeitsgerichtsverfahren-modus-terminkalender`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `beweismittel-gegenueberstellung-einleitungssatz-generator`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `erstellen-fristennotiz-gerichtsverfahren-verfahrensgeschichte`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `gegenueberstellung-parteivortraege-rechtsargumente`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `parteivortrag-gegenueberstellung-rechtsargumente`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `sachverhaltschronologie-textbausteine-schnelle-stilrichtlinie`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
