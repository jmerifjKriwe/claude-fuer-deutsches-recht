---
name: paragraph-fehlerkatalog
description: "Paragraph Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Paragraph Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Schriftform Und Textform Bgb** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `anspruchsformulierungen-formverstoss-buergschaft`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `arbeitsrecht-befristung-schriftform-checker-vertrag`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `elektronische-paragraph-formerfordernisse-ueberblick`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `formwahl-zugang-live-prozessablauf-mandantenentscheidung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `klauselgenerator-formvorbehalt-maklervertrag-paragraph-amtlicher`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `kuendigung-per-mandantenkorrespondenz-zugang-mandantenwarnung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `notarielle-beurkundung-prozessablauf-papier-paragraph`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `prozessordnungen-textform-verifikation`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `sftf-arbeitsvertraege-nachweisgesetz-doppelschriftform-aufhebung`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
