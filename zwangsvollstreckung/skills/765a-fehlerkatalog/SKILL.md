---
name: 765a-fehlerkatalog
description: "765a Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# 765a Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Zwangsvollstreckung** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bank-haertefall-inso`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `kontenpfaendung-notar-interessen-online`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `mahnbescheid-fristennotiz-zv-titel-zv-kontensuche`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `pfueb-raeumung-schuldnerschutz-beweislast`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `vermoegensauskunft-vollstreckungsbescheid-vollstreckungstitel`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `zpo-zwangsvollstreckung-zv-abwehr`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `zv-elektronische-zv-eu-zv`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `zv-mahnbescheid-zv-mobiliar-zv-notarielle`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `zv-pfaendungstabelle-zv-pfueb-zv-pfueb`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
