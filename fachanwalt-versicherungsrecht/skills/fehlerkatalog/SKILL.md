---
name: fehlerkatalog
description: "Versr Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Versr Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Fachanwalt Versicherungsrecht** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `cyber-loesegeld-versr-cyber-deckungsanfrage`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `deckungsklage-interessen-deckungspruefung-obliegenheiten`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `do-deckungsabwehr-lebensversicherung-rueckkauf`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `erstgespraech-mandatsannahme-berufsunfaehigkeit-klage`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `fachanwalt-kanzlei-krankenversicherung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `klage-versicherer-triage-versicherungsrecht-schriftsatzkern`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `lebens-leistungsablehnung-international-obliegenheitsverletzung`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `ombudsmann-gdv-orientierung-regress-abwehr`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `private-spezial-pruefen-rechtsschutz-beweislast`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
