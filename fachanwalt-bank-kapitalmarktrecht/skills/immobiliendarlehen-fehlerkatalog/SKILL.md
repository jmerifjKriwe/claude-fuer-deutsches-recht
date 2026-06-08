---
name: immobiliendarlehen-fehlerkatalog
description: "Immobiliendarlehen Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Immobiliendarlehen Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Fachanwalt Bank Kapitalmarktrecht** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `fa-bank-kapitalmarkt-bk-bafin-chronologie`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `anlageberatung-fehlerhaft-cybertrading-anlagebetrug`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `anlageberatungsfehler-bankrecht-akkreditiv-buergschaft-erste`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bankaufsicht-erlaubnis-emissionsprospekt-mandantenentscheidung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bankrecht-buergschaft-aval-garantieabruf-eilrechtsschutz`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bankrecht-privatbuergschaft-bankrecht-regress-bk-aufsicht`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `beratungshaftung-haftung-beweislast-bk-cum`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bk-bankenfehlberatung-bk-einfuehrung-bk-mandantenrouting`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bk-mifid-bk-prip-erstgespraech-mandatsannahme`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `fehlerhaft-fristennotiz-kapitalmarktrecht-bk-emissionsprospekt`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
