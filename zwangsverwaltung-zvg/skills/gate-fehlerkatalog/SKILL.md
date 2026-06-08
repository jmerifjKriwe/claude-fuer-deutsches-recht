---
name: gate-fehlerkatalog
description: "Gate Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Gate Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Zwangsverwaltung Zvg** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `berichte-beschlagnahme-mietverwaltung-besitz`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `betriebskosten-hausgeld-bieterangebot-bewertung-glaeubiger`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `bieterangebote-mieten-öffentliche`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `insolvenz-schnittstelle-instandhaltung-sicherung-zvg`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `konten-kassenfuehrung-miet-pachtverwaltung-mieteinzug`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `quality-recherche-rechnungslegung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `treuhandkonto-versteigerung-versteigerungsteilnahme`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `versicherungen-gefahren-zvg-versteigerungsteilnahme-zvg`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `verteilung-zwangsverwaltung-aktenanlage-objektcockpit`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
