---
name: rechtsquellen-fehlerkatalog
description: "Nutze dies, wenn Rechtsquellen Fehlerkatalog im Plugin Fachanwalt Erbrecht konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.."
---

# Rechtsquellen Fehlerkatalog

## Einsatzlage

Nutze diesen Fehlerkatalog, wenn ein Ergebnis im Bereich **Fachanwalt Erbrecht** vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegengeprüft werden soll.

## Fachspezifische Fehlerachsen

- `allgemein-workflow-chronologie-workflow-fristen`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `berater-interessen-beweislast-darlegungslast`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `erb-einfuehrung-erb-erstgespraech-erb-internationales`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `erb-nachlassinventar-erb-pflichtteilsanspruch-erb`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `erbengemeinschaft-blockade-erstgespraech-mandatsannahme`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `erbfall-eu-mandat-triage-pflichtteil-auskunft`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `erbfall-intake-erbrecht-erbschein`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `erbschein-antrag-orientierung-pflichtteilsberechnung`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `fachanwalt-kanzlei-livecheck`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.
- `krypto-wallet-erbschaftsteuer-steuerrecht`: typischen Fehler aus diesem Fachpfad aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
