---
name: rechenprotokolle-fehlerkatalog
description: "Nutze dies, wenn Rechenprotokolle Fehlerkatalog im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?."
---

# Rechenprotokolle Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Jveg Kostenpruefer** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `beschwerde-dolmetscher-sonderfall-dolmetscherkosten`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fahrtkosten-festsetzung-interessen-freistehender`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `gate-beweislast-jveg-quality`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `jveg-anspruchsberechtigung-antragsgenerator-dolmetscher`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `jveg-dolmetscher-uebersetzer-fahrtkosten-festsetzung-beschwerde`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `jveg-gate-rechenblatt-sachverstaendigenrechnung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `jveg-gerichtsschreiben-jveg-kuerzung-wegfall`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `jveg-sonstige-aufwendungen-uebernachtung-aufwand`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `jveg-vorschuss-kostenrisiko-zeugenentschaedigung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
