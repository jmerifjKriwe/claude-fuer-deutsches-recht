---
name: barrierefreiheit-fehlerkatalog
description: "Barrierefreiheit Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Barrierefreiheit Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Barrierefreiheit Web Checker** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `audit-barrierefreiheits-bfsg`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bf-kiosk-bf-mediendienste-bf-pdf`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bfsg-zeitleiste-ecommerce-checkout-en301549-wcag`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bfsgv-schulung-fristennotiz-agentur-abnahme`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bitv-checkout-beweislast-ecommerce`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `erklaerung-interessen-formulare-pdfs`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `formulare-checkout-kontrast-farbe-native-apps`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `pdf-downloads-remediation-roadmap-schulung-rolle`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `pdf-formulare-automatisierter-audit-bf-kanzleiwebsite`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
