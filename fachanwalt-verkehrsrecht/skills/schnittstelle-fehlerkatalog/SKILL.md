---
name: schnittstelle-fehlerkatalog
description: "Schnittstelle Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Schnittstelle Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Fachanwalt Verkehrsrecht** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-verk-unfallregulierung-workflow-chronologie`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `autonom-bezuege-fachanwalt`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bussgeld-unfall-haftungsquote-vkr-totalschaden`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `erstgespraech-mandatsannahme-verkehr-autonom-fahrerlaubnis`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `fahrerlaubnis-kanzlei-personen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `mandat-triage-schriftsatzkern-substantiierung-315c`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `mpu-vorbereitung-orientierung-regulierungsanforderung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `pflvg-quoten-sonderfall-stgb`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `stvg-verkehr-fristennotiz-vkr-blitzer`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `stvo-unfallregulierung-beweislast-verkehrsrecht`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
