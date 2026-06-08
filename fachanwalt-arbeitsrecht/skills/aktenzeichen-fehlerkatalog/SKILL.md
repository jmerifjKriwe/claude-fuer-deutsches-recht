---
name: aktenzeichen-fehlerkatalog
description: "Aktenzeichen Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand."
---

# Aktenzeichen Fehlerkatalog

## Einsatzlage

Dieser Fehlerkatalog prüft im Bereich **Fachanwalt Arbeitsrecht** Ergebnisse vor Abgabe, Versand, Einreichung oder Mandantenfreigabe belastbar gegen.

## Fachspezifische Fehlerachsen

- `allgemein-ar-kuendigungspruefung-fazugang-arbeitgeber`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `ar-aufhebungsvertrag-konkurrenzklausel-fachanwalt-arbeitsrecht`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `ar-betriebsuebergang-ar-einfuehrung-ar-leiharbeit`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `arbeitsgericht-abrechnung-vergleichsverhandlung-strategie-zugang`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `befristung-fao-unwirksam-fristennotiz`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `befristung-tzbfg-bem-verfahren-fazugang-kuendigungsfrist`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `beteiligung-betriebsrat-erstgespraech-mandatsannahme-fachanwalt`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `betriebsrat-betrvg-datum`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `entgtranspg-fachanwalt-kschg`: für dieses Thema typischen Fehler aktiv gegenprüfen.
- `fachanwalt-arbeitsrecht-bag-betriebsratsanhoerung`: für dieses Thema typischen Fehler aktiv gegenprüfen.

## Red-Team-Fragen

1. Ist die richtige Rolle, Zuständigkeit und Verfahrensart gewählt?
2. Sind Fristbeginn, Fristende, Form, Zugang und Beweislast getrennt dokumentiert?
3. Gibt es eine Spezialnorm, die die allgemeine Lösung verdrängt?
4. Sind tatsächliche Annahmen als Annahmen markiert und Belege benannt?
5. Enthält der Output unnötige Zugeständnisse, vertrauliche Daten oder ungeprüfte Fundstellen?
6. Ist der nächste Schritt praktisch ausführbar: wer tut was bis wann mit welchem Dokument?

## Heilung

Jeden roten Punkt mit Symptom, Diagnose, Korrektur und verbleibendem Restrisiko ausgeben. Quellenhygiene nach `references/quellenhygiene.md`.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 102 BetrVG
- § 17 KSchG
- § 4 KSchG
- § 14 TzBfG
- § 1 KSchG
- § 17 TzBfG
- § 15 AGG
- § 22 AGG
- § 5 KSchG
- § 66 ArbGG
- § 54 ArbGG
- § 23 KSchG

### Leitentscheidungen

- EuGH C-134/24
- EuGH C-518/20

