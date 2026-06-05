---
name: pruefung-fehlerkatalog
description: "Nutze dies, wenn Prüfung Fehlerkatalog im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?."
---

# Prüfung Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Immobilienrechtspraxis** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `case-gegen-grundbuchanalyse`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `case-management-grundbuchanalyse-immo-aufteilungsplan`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `immo-bauliche-veraenderung-energieausweis-gewerbliche-mieter`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `immo-bauvertrag-vob-kaufvertrag-grundstueck-mietkaufvertrag`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `immo-grundschuld-bestellung-makler-honorar-wohnungseigentum`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `immo-immobilienrechtliche-live-beweislast`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `immo-zwangsversteigerung-frist-naechster-rechtsabteilungen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `immor-bauvertrag-vob-erbbaurecht-vertrag-grundstueckskaufvertrag`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `immor-bodenrichtwert-betriebskostenabrechnung-erstellen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
