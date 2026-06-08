---
name: rechenprotokolle-fehlerkatalog
description: "Rechenprotokolle Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Rechenprotokolle Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Jveg Kostenpruefer** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `beschwerde-dolmetscher-sonderfall-dolmetscherkosten`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `fahrtkosten-festsetzung-interessen-freistehender`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `gate-beweislast-jveg-quality`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `jveg-anspruchsberechtigung-antragsgenerator-dolmetscher`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `jveg-dolmetscher-uebersetzer-fahrtkosten-festsetzung-beschwerde`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `jveg-gate-rechenblatt-sachverstaendigenrechnung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `jveg-gerichtsschreiben-jveg-kuerzung-wegfall`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `jveg-sonstige-aufwendungen-uebernachtung-aufwand`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `jveg-vorschuss-kostenrisiko-zeugenentschaedigung`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
