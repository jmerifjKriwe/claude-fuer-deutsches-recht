---
name: immobiliendarlehen-fehlerkatalog
description: "Nutze dies, wenn Immobiliendarlehen Fehlerkatalog im Plugin Fachanwalt Bank Kapitalmarktrecht konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?."
---

# Immobiliendarlehen Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Fachanwalt Bank Kapitalmarktrecht** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `allgemein-bk-bafin-workflow-chronologie`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `anlageberatung-fehlerhaft-cybertrading-anlagebetrug`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `anlageberatungsfehler-bankrecht-akkreditiv-buergschaft-erste`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `bankaufsicht-erlaubnis-emissionsprospekt-mandantenentscheidung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `bankrecht-buergschaft-aval-garantieabruf-eilrechtsschutz`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `bankrecht-privatbuergschaft-bankrecht-regress-bk-aufsicht`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `beratungshaftung-haftung-beweislast-bk-cum`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `bk-bankenfehlberatung-bk-einfuehrung-bk-mandantenrouting`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `bk-mifid-bk-prip-erstgespraech-mandatsannahme`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fehlerhaft-fristennotiz-kapitalmarktrecht-bk-emissionsprospekt`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
