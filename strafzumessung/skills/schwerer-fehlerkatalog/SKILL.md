---
name: schwerer-fehlerkatalog
description: "Schwerer Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Schwerer Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Strafzumessung** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `153a-stpo-iii-stpo-bewaehrung-stgb`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bewaehrung-auflagen-bewaehrungswiderruf-56f-freiheitsstrafe-ohne`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bewaehrung-interessen-deutschem-freiheitsstrafe`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `freiheitsstrafe-strafmass-geldstrafe-tagessatzanzahl-vs-stgb`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `geldstrafe-grossen-rechtsmittel-gesamtstrafenfolgen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `gesamtstrafenbildung-stgb-gestaendnis-strafmilderung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `jgg-jugendstrafe-minder-schwerer-nachtraegliche`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `orientierung-triage-paragraph-stgb-besonders`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `regelbeispiele-stgb-strafbefehl`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `strafbefehl-stpo-strafmilderung-stgb-strafrahmen`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
