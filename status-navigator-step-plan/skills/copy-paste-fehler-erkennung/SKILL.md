---
name: copy-paste-fehler-erkennung
description: "Erkennt typische Copy-Paste-Situationen: alte Parteinamen, abweichende Vertragsbezeichnungen, falsche Daten in Standardabsaetzen und uebernommene Klauseln aus Vorlaeuferdokumenten. Liefert eine kommentierte Auffaelligkeitsliste."
---

> **Hinweis:** Plugin `status-navigator-step-plan`, Dokumentenverarbeitung
> ohne Normen-Anker. Rechtliche Pruefung bleibt anwaltliche Aufgabe.

# Copy-Paste-Fehler erkennen

## Rolle und Fokus
Findet uebernommene Textstellen aus Vorlaeuferdokumenten: alte Parteinamen, falsche Datumsangaben in Standardabsaetzen, Verweise auf nicht existente Anhaenge oder Beschluesse.

## Vorgehen

1. **Verweisstellen extrahieren** — Alle Klauseln mit Bezug auf Anlagen, Beschluesse, Vorvertraege, Vollmachten in Liste sammeln.
2. **Verweisziel pruefen** — Existiert das referenzierte Dokument tatsaechlich? Datum stimmig? Bezeichnung identisch?
3. **Parteinamen-Drift** — Im gesamten Dokument vorkommende Firmierungen abgleichen; abweichende Bezeichnungen sind Copy-Paste-Verdacht.
4. **Datumsfeld-Inkonsistenz** — Vertragsrubrum vs. Unterschriftsdatum vs. Datum in Standardabsaetzen vergleichen.
5. **Befund in Anmerkungsspalte Reiter 2** — Pro Fundstelle Kurzhinweis, Detail in eigenem Memo.

## Anwendungsbeispiel
Wandeldarlehen NordCap vom 14.03.2026: § 4 verweist auf 'Gesellschafterbeschluss vom 22.01.2026' — solcher Beschluss existiert nicht; jung uebernommene Klausel aus Wandeldarlehensvorlage einer anderen Portfoliogesellschaft. § 11 nennt 'LausitzWind GmbH' statt 'LausitzStorage 200 GmbH i.G.' an einer Stelle.

## Output-Module
- Auffaelligkeitsliste mit Fundstelle, Verdacht, Verweisziel
- Querliste an Skill `unterschriftspruefung` (Beschluss als Wirksamkeitsbedingung)
- Reparatur-Vorschlag fuer Nachtragsvereinbarung

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Subsumtion bleibt anwaltliche Aufgabe.
- **Hinweise, keine Befunde.** Markierungen muessen anwaltlich verifiziert werden.
- **Datenschutz und Berufsrecht.** Nutzung nur mit System, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfuellt.
