---
name: metadaten-fehlerkatalog
description: "Metadaten Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Metadaten Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Verlagsredaktion** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `eingangskorb-heftplanung-interessen-juristische-manuskript`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `eingangskorb-triage-entscheidungsmonitor-fremdtext-plagiat`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `lektorat-struktur-manuskriptaufnahme-materialinventar-marketing`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `qualitaetsgate-verlag-quellen-zitate-rechtecheck-urhg`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `redaktion-satzfahnen-verlage-verlagsdesk-sprachlektorat-stil`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `sales-katalog-satzfahne-korrekturlauf-autorenkommunikation`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `verl-abstimmung-lektorat-produktion-satz-rechtsabteilung-audio`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `verl-aussagensicherheit-buchprojekt-bauleiter-email-konvolute`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `verl-fussnoten-quellen-glossar-konsistenz-grammatik-handschrift`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `verl-ideenpool-priorisierung-impressum-pflicht-interview-roh`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.
