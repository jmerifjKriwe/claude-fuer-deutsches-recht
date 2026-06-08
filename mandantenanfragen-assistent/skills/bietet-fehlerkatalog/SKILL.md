---
name: bietet-fehlerkatalog
description: "Bietet Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Bietet Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Mandantenanfragen Assistent** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `anrede-anwaltskanzleien-bittet`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `dankt-dsgvo-sonderfall-e-mail`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `dringlichkeitsmarker-einwilligung-hinweis-erstantwort-generator`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `erstantwort-foermlich-mail`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `folgekorrespondenz-vorbereiten-konfliktcheck-vorab-ma`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `ma-einfuehrung-ma-erstvermerk-ma-konfliktcheck`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `ma-mandant-manda-erstgespraechsleitfaden-manda-erstkontakt`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `manda-mandatsablehnung-rechtsschutz-eintrittsanfrage`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `mandantenanfragen-anfrage-eingang-anrede-uebernehmen`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
