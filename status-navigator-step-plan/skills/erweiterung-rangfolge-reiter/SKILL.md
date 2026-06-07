---
name: erweiterung-rangfolge-reiter
description: "Optionaler Reiter Rangfolge bei mehreren Finanzierungsinstrumenten. Stellt die Rang- und Befriedigungsreihenfolge dar: Senior Secured, Senior Unsecured, Mezzanine, Gesellschafterdarlehen, sonstige Einlagen. Beruht ausschliesslich auf Mandatsangaben und Vertragstext."
---

> **Hinweis:** Plugin `status-navigator-step-plan`, Dokumentenverarbeitung
> ohne Normen-Anker. Rechtliche Pruefung bleibt anwaltliche Aufgabe.

# Erweiterung Rangfolge-Reiter

## Rolle und Fokus
Optionaler Reiter Rangfolge bei mehreren Finanzierungsinstrumenten. Senior Secured, Senior Unsecured, Mezzanine, Gesellschafterdarlehen, sonstige Einlagen — vertraglich vereinbarte Reihenfolge abbilden.

## Vorgehen

1. **Instrumente listen** — Pro Zeile ein Finanzierungsinstrument mit Glaeubiger, Volumen, Faelligkeit.
2. **Vertragliche Rangposition rekonstruieren** — Aus Subordination Agreement, Intercreditor, Sicherheitenpoolvertrag.
3. **Sicherheitenbezug** — Welches Instrument auf welcher Sicherheit; gemeinsamer Pool oder separate Stuecke.
4. **Zinslast und Faelligkeit** — Spalte Restlaufzeit, Zinssatz, Tilgungsplan.
5. **Kein eigenes Rangurteil** — Skill spiegelt nur die vertragliche Vereinbarung. Insolvenzrechtliche Rangfragen bleiben anwaltliche Pruefung.

## Anwendungsbeispiel
LausitzStorage Rangfolge: Senior-Darlehen NordCap (besichert durch Grundschulden und Verpfaendung der Anteile) > Konsortial-Darlehen Stadtwerke Cottbus (besichert durch Sicherungsabtretung Stromabnahmevertrag) > Wandeldarlehen NordCap (unbesichert, nachrangig nach § 39 InsO automatisch nicht — aber vertraglich subordiniert) > Gesellschafter-Stundungen Bauernfeind privat.

## Output-Module
- Rangfolge-Reiter mit Spalten Instrument, Glaeubiger, Volumen, Sicherheit, Rang
- Hinweis-Spalte mit Quellnachweis (welche Klausel begruendet den Rang)
- Pflichthinweis auf anwaltliche Pruefung insolvenzrechtlicher Rangfragen

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Subsumtion bleibt anwaltliche Aufgabe.
- **Hinweise, keine Befunde.** Markierungen muessen anwaltlich verifiziert werden.
- **Datenschutz und Berufsrecht.** Nutzung nur mit System, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfuellt.
