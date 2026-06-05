---
name: seit-fehlerkatalog
description: "Nutze dies, wenn Seit Fehlerkatalog im Plugin Fachanwalt Handels Gesellschaftsrecht konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?."
---

# Seit Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Fachanwalt Handels Gesellschaftsrecht** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `ag-vorstandsvertrag-hgr-aktionsbindungsvertrag-hgr`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `allgemein-workflow-chronologie-workflow-fristen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fachanwalt-fao-gesellschafterstreit`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `geschaeftsfuehrerhaftung-holding-strukturplanung-gmbh-cash`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `gesellschafterstreit-handelsvertreterausgleich-ma-due`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `gesellschaftervertrag-geschaeftsfuehrerhaftung-hgr`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `gmbh-beirat-vergleichsverhandlung-strategie`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `gmbhg-handels-handelsvertreterausgleich-international`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `hgb-kanzlei-beweislast-mopeg`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `hgesr-einfuehrung-hgr-due-erstgespraech-mandatsannahme`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
