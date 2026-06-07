---
name: dokumententyp-cap-tables
description: "Erkennt Cap Tables in beliebigem Format (Excel, PDF, eingebettete Tabellen). Erfasst Stichdatum, Gesellschafter und Anteile. Vorbereitung fuer den Konsistenz-Vergleich mehrerer Cap Tables und Abgleich mit den zugrundeliegenden Vertraegen."
---

> **Hinweis:** Plugin `status-navigator-step-plan`, Dokumentenverarbeitung
> ohne Normen-Anker. Rechtliche Pruefung bleibt anwaltliche Aufgabe.

# Dokumententyp Cap Tables

## Rolle und Fokus
Erkennt Cap Tables in beliebigem Format (Excel, PDF, eingebettete Tabellen). Erfasst Stichdatum, Gesellschafter, Anteile. Vorbereitung fuer Konsistenzvergleich mehrerer Versionen.

## Vorgehen

1. **Stichdatum identifizieren** — Datum auf der Cap Table; ohne Datum ist die Tabelle unbrauchbar fuer den Versionsvergleich.
2. **Gesellschafterzeile normalisieren** — Vollstaendige Firmierung, Sitz, Rechtsform.
3. **Anteilsangaben pruefen** — Nennbetrag, prozentuale Beteiligung, Stimmrechte separat erfassen (Spreizung moeglich).
4. **Klassen-Differenzierung** — Stammanteile, Vorzugsanteile, Wandelinstrumente noch nicht gewandelt.
5. **Quellenangabe** — Wer hat die Cap Table erstellt? Datenraum, Mandantenversion, Investor-Update.

## Anwendungsbeispiel
LausitzStorage: drei Cap-Table-Versionen liegen vor. v1 (31.12.2025, von Mandantin), v2 (30.04.2026, von NordCap-Datenraum), v3 (Mai 2026, aus Investor-Update). Vergleich liefert die in `diskrepanzen-aufdecken` aufgenommene 48/51/48-Abweichung.

## Output-Module
- Versionsregister mit Stichdatum, Quelle, Status
- Normalisierte Cap-Table als Vorlage fuer den Konsistenzvergleich
- Querliste an `szenario-cap-table-bereinigung` wenn Abweichungen materiell

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Subsumtion bleibt anwaltliche Aufgabe.
- **Hinweise, keine Befunde.** Markierungen muessen anwaltlich verifiziert werden.
- **Datenschutz und Berufsrecht.** Nutzung nur mit System, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfuellt.
