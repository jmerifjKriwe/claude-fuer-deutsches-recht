---
name: schnittstelle-fehlerkatalog
description: "Nutze dies, wenn Schnittstelle Fehlerkatalog im Plugin Fachanwalt Verkehrsrecht konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?."
---

# Schnittstelle Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Fachanwalt Verkehrsrecht** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `allgemein-verk-unfallregulierung-workflow-chronologie`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `autonom-bezuege-fachanwalt`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `bussgeld-unfall-haftungsquote-vkr-totalschaden`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `erstgespraech-mandatsannahme-verkehr-autonom-fahrerlaubnis`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fahrerlaubnis-kanzlei-personen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `mandat-triage-schriftsatzkern-substantiierung-315c`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `mpu-vorbereitung-orientierung-regulierungsanforderung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `pflvg-quoten-sonderfall-stgb`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `stvg-verkehr-fristennotiz-vkr-blitzer`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `stvo-unfallregulierung-beweislast-verkehrsrecht`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
