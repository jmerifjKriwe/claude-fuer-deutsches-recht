---
name: geas-fehlerkatalog
description: "Geas Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Geas Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Fachanwalt Migrationsrecht** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-abschiebungsabwehr-sofort-arbeitgeber-arbeitsrecht`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `arbeitgeberwechsel-asyl-anhoerung-asylg-ausbildungsduldung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `aufenthaltstitel-ausweisung-start-behoerdenkommunikation-blaue`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `aufenthaltstitel-erstgespraech-mandatsannahme-fachanwalt-asyl`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `ba-zustimmung-beschaeftigungsduldung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `blaue-karte-blaue-karte-bleiberecht-25a-chancenaufenthalt`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `botschaft-visumtermin-workflow-chronologie-dokumentenstapel`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `datenschutz-sicherheit-daueraufenthalt-eu-digitalbeweise-flucht`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `dublin-ueberstellung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `einbuergerung-lebensunterhalt-mehrstaatigkeit-strafen-einreise`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
