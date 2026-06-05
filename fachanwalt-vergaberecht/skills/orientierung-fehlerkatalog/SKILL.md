---
name: orientierung-fehlerkatalog
description: "Nutze dies, wenn Orientierung Fehlerkatalog im Plugin Fachanwalt Vergaberecht konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?."
---

# Orientierung Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Fachanwalt Vergaberecht** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `bieterstrategie-go-eforms-ted-eignung-referenzen-erstgespraech`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fachanwalt-vergaberecht-aufklaerung-nachforderung-ruege-zuschlag`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fachanwalt-vergaberecht-facto-eignungspruefung-freiberufliche`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fachanwalt-vergaberecht-olg-orientierung-ruegeschriftsatz-gwb`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `it-sicherheits-konzessionsvergabe-konzvgv-losbildung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `konzvgv-rahmenvereinbarung-international-schnittstelle-sektvo`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `mandantenpadlet-vergabe-triage-vergaberecht-nachhaltigkeit`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `olg-vergabesenat-resilienz-sicherheit-ruegeschriftsatz-erstellen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `rahmenvereinbarung-abrufe-angebotsoeffnung-formfehler`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `schwellenwerte-livecheck-architektenrecht-fachanwalt-konzession`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
