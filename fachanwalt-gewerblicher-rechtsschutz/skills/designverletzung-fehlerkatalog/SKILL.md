---
name: designverletzung-fehlerkatalog
description: "Nutze dies, wenn Designverletzung Fehlerkatalog im Plugin Fachanwalt Gewerblicher Rechtsschutz konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?."
---

# Designverletzung Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Fachanwalt Gewerblicher Rechtsschutz** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `abmahnung-bezuege-designg`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `allgemein-gr-abmahnung-gr-portfolio`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `designverletzung-marken-widerspruch-markenanmeldung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `dpma-interessen-einstweilige-euipo`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `erstgespraech-mandatsannahme-abmahnung-uwg-abmahnung-wipo`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fachanwalt-fao-gebrmg`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `faevvollzug-gegnerische-faevvollzug-grenzueberschreitende`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `faevvollzug-parteibetrieb-gerichtsvollzieher-bea-elektronischer`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `gewerblichen-markenanmeldung-markeng`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `gewrechts-geschgehg-gewrechts-ki-faevvollzug-ev`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
