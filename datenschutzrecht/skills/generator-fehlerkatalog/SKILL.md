---
name: generator-fehlerkatalog
description: "Generator Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Generator Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Datenschutzrecht** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `anwendungsfall-triage`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-art-26-joint-controllership-deutsch`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-art-28-dsgvo-grundtatbestand`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-art-28-mindestinhalte-checkliste`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-audit-avv-cloud-avv-eu-avv-konzern-avv`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-audit-und-kontrollrechte`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-bestehender-avv-rolemix-avv-tom-datenpanne-meldung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-cloud-und-subverarbeitung-art-28-iv`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-eu-kommission-musterklauseln-2021-915`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-eu-us-data-privacy-framework-bezug`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
