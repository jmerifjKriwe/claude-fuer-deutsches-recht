---
name: gutachten-fehlerkatalog
description: "Gutachten Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Gutachten Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Berufsrecht Ki Vertragspruefung** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `ai-act-rollen-kanzlei-provider-deployer-api`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `br-ki-vertragspruefung-brki-rollout-chronologie`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `anbietern-belehrung-sonderfall-edge`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `art-50-ki-vo-schriftsatz-marketing-chatbot`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-grenzpruefung-brki-anbieter-brki-eu`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `avv-grenzpruefung-datenschutz`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `berufsrecht-ki-vertragspruefung-kaltstart-interview`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `berufsrechtliche-bnoto-interessen-brao`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `brki-anbieter-due-diligence`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `brki-eu-us-dpf-transferpruefung`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
