---
name: aktenzeichen-fehlerkatalog
description: "Nutze dies, wenn Aktenzeichen Fehlerkatalog im Plugin Fachanwalt Arbeitsrecht konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?."
---

# Aktenzeichen Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Fachanwalt Arbeitsrecht** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `allgemein-ar-kuendigungspruefung-fazugang-arbeitgeber`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `ar-aufhebungsvertrag-konkurrenzklausel-fachanwalt-arbeitsrecht`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `ar-betriebsuebergang-ar-einfuehrung-ar-leiharbeit`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `arbeitsgericht-abrechnung-vergleichsverhandlung-strategie-zugang`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `befristung-fao-unwirksam-fristennotiz`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `befristung-tzbfg-bem-verfahren-fazugang-kuendigungsfrist`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `beteiligung-betriebsrat-erstgespraech-mandatsannahme-fachanwalt`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `betriebsrat-betrvg-datum`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `entgtranspg-fachanwalt-kschg`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fachanwalt-arbeitsrecht-bag-betriebsratsanhoerung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
