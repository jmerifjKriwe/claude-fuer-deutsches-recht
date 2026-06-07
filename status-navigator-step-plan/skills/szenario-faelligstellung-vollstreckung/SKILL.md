---
name: szenario-faelligstellung-vollstreckung
description: "Anwendungsszenario gescheiterte Finanzierung mit Vorbereitung von Faelligstellung und Vollstreckung. Status-Navigator erfasst Darlehensvertraege, Kuendigungs- und Faelligstellungsschreiben, Zustellungsnachweise und Sicherheiten. Workflow zeigt die naechsten Schritte fuer die Vollstreckung."
---

> **Hinweis:** Plugin `status-navigator-step-plan`, Dokumentenverarbeitung
> ohne Normen-Anker. Rechtliche Pruefung bleibt anwaltliche Aufgabe.

# Szenario gescheiterte Finanzierung

## Rolle und Fokus
Gescheiterte Finanzierung mit Vorbereitung von Faelligstellung und Vollstreckung. Status-Navigator erfasst Darlehensvertraege, Kuendigungs- und Faelligstellungsschreiben, Zustellungsnachweise, Sicherheiten.

## Vorgehen

1. **Faelligkeitsgrund pruefbar dokumentieren** — Zahlungsverzug, MAC, Cross-Default, Kuendigungsgrund nach Vertragsklausel.
2. **Kuendigungs-/Faelligstellungs-Erklaerung pruefen** — Bestimmtheit, Berechtigung, Form, Frist.
3. **Zustellungs-Beweisspur sichern** — Skill `zugang-zustellung-pruefung` mit Beweisanforderung Brief/Bote/Zustellungsurkunde.
4. **Sicherheiten verwertungsreif machen** — Notarielle Vollstreckungsunterwerfung, Titel, Klausel, Zustellung.
5. **Schritt-Reihenfolge in Reiter 4** — Erst sichere Kuendigung, dann Titulierung, dann Verwertung; jede Stufe dokumentiert.

## Anwendungsbeispiel
LausitzStorage hypothetische Spiegelung aus Glaeubigersicht (NordCap gegen LausitzStorage): Faelligstellungsgrund waere Drawstop-Folge, aber Drawstop ist einseitige Auszahlungsverweigerung — keine Faelligstellung. Echte Faelligstellung erst nach Reparaturvereinbarungs-Scheitern; dann Pfandverwertung an Anteilen und Grundschuldverwertung.

## Output-Module
- Faelligstellungs-Checkliste im Workflow-Reiter
- Zustellungs-Beweisplan je Erklaerung
- Verwertungs-Stufenplan mit Stufenstatus

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Subsumtion bleibt anwaltliche Aufgabe.
- **Hinweise, keine Befunde.** Markierungen muessen anwaltlich verifiziert werden.
- **Datenschutz und Berufsrecht.** Nutzung nur mit System, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfuellt.
