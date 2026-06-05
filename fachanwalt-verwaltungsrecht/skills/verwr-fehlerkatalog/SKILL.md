---
name: verwr-fehlerkatalog
description: "Nutze dies, wenn Verwr Fehlerkatalog im Plugin Fachanwalt Verwaltungsrecht konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?."
---

# Verwr Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Fachanwalt Verwaltungsrecht** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `anfechtungs-eilrechtsschutz-abs-eilrechtsschutz`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `einstweilige-fachanwalt-kanzlei`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `erstgespraech-mandatsannahme-fa-vwgo-anfechtungsklage`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fachanwalt-verwaltungsrecht-drittanfechtung-einstweiliger`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fachanwalt-verwaltungsrecht-verwaltungsakt-rechtsbehelf-vwgo`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `normenkontrolle-ordnungsrecht-interessen-orientierung-sonderfall`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `normenkontrolle-vwgo-orientierung-vwgo-behoerde`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `polizei-polizei-filmen-rechtsschutz-beweislast`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `schnittstelle-verpflichtungsklage-verwaltungsrecht`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
