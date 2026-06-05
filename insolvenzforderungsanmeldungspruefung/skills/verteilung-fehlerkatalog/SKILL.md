---
name: verteilung-fehlerkatalog
description: "Nutze dies, wenn Verteilung Fehlerkatalog im Plugin Insolvenzforderungsanmeldungspruefung konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?."
---

# Verteilung Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Insolvenzforderungsanmeldungspruefung** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `feststellung-forderungsgrund-rang-grund`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `iap-anmeldepruefung-bauleiter-aussonderung-absonderung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `iap-rangordnung-ifap-aktenanlage-ifap-beleg`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `ifap-dubletten-serienforderungen-formalpruefung-grund-betrag`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `ifap-insolvenzforderungsanmeldungspruefung-intake`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `ifap-intake-kanalcheck-masseverbindlichkeit-abgrenzen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `ifap-nachtraegliche-anmeldung-pruefungstermin-gate`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `ifap-pruefentscheidung-vbuh`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `ifap-rang-nachrang-schuldnerwiderspruch-streitige-forderung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
