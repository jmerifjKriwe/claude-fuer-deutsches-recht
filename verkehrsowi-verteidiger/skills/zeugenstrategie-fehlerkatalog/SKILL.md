---
name: zeugenstrategie-fehlerkatalog
description: "Zeugenstrategie Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Zeugenstrategie Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Verkehrsowi Verteidiger** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `alkohol-drogen-beweisverwertung-standardisiert-verkehrsowi`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `amtsgericht-drogen-interessen-einspruch`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `anhoerung-verkehrsowi-einspruch-messverfahren-geschwindigkeit`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `fahrverbot-geschwindigkeit-handy`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `hauptverhandlung-sonderfall-messakte-messung-fahrverbot`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `punkte-rotlicht-verkehrsowi`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `simulation-training-verjaehrung-zustellung-zeugen-polizei`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `verkehrsowi-haertefall-fahrverbot-hauptverhandlung-amtsgericht`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `verkehrsowi-punkte-fahrverbot-rechtsbeschwerde-rotlicht-abstand`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
