---
name: fahrlaessigkeit-fehlerkatalog
description: "Fahrlaessigkeit Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Fahrlaessigkeit Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Phishing Vorfall Prüfer** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `675u-675w-banking`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `arbeitnehmer-haftung-bgb-675u-phish-ceo`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `aufsicht-bafin-bank-strategie-banking-app`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bankpflichten-beweislast-beweislast-bgb`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bea-notfall-bgb-675v-erstkontakt-mandant`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `call-interessen-faelle-freistehender`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `grobe-online-phishing`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `klage-fristennotiz-vorfall-phish-banking`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `phish-incident-phish-meldepflichten-arten-erkennen`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
