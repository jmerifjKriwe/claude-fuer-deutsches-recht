---
name: erstellung-fehlerkatalog
description: "Erstellung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Erstellung Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Mietrecht** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `amtlichen-amtsgericht-sonderfall-ausschliesslich`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bundesland-datenerhebung-grossstadt-mietspiegel`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `klageentwurf-amtsgericht-miet-gewerbemiete-mietvertrag-bauleiter`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `lage-ausstattung-mahnung-zahlungsverzug-mandat-triage`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `miet-kuendigungsschutz-miet-mietminderung-mieteranfragen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `mieter-mieteranfragen-mandantenentscheidung-mieterhoehungs`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `mieterhoehung-widersprechen-mieterhoehungsverlangen-erstellen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `mietpreisueberhoehung-wistrg-mietsenkungsverlangen-mietspiegel`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `mietrecht-mietsenkungsverlangen-international-mietspiegel`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
