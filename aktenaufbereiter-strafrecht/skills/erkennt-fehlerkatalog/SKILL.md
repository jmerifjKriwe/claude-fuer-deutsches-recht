---
name: erkennt-fehlerkatalog
description: "Erkennt Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Erkennt Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Aktenaufbereiter Strafrecht** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `aktenaufbereiter-strafrecht`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `akteneinsicht-uebersicht-aktenvorblatt-erstellen-anklageschrift`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `beweismittel-katalog-beweisverwertungsverbote-beziehungsmatrix`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `beziehungen-spezial-chronologie-ergaenzbar`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `ersatz-sonderfall-excel-faehige`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `fortlaufend-luecken-personenverzeichnis`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `fristenliste-strafverfahren-aktenlektuere-fristennotiz`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `kronzeugen-regelung-opferzeugen-besondere-personenverzeichnis`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `revision-rechtsfehler-aktenaufbereiter-aktenvorblatt`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
