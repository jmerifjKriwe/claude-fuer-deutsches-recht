---
name: excel-reiter-3-fehlend
description: "Baut Reiter 3 der Step-Plan-Excel: fehlende Dokumente mit Beschaffungsweg. Spalten erforderliches Dokument, angefordert von, zu beschaffen von, Grund der Erforderlichkeit und Status. Sortierung nach Frist. Vorbereitung fuer den Workflow-Reiter."
---

# Reiter 3 Fehlende Dokumente

## Rolle und Fokus
Reiter 3 listet alles, was fehlt oder noch nicht endgueltig vorliegt.
Jede Zeile hier ist eine offene Position, die in den Workflow von
Reiter 4 ueberfuehrt werden muss.

## Vorlage-Bezug
Reiter 3 folgt der Excel-Vorlage. Spalten:

| Spalte | Inhalt |
|---|---|
| Erforderliches Dokument / erforderlicher Nachweis | sprechend |
| Angefordert von | Person oder Kanzlei intern |
| Zu beschaffen von | Quelle: Behoerde, Notar, Vertragspartner |
| Grund der Erforderlichkeit | warum brauchen wir es, mit Querverweis Klausel oder Paragraph |
| Status | offen / Anforderung raus / in Bearbeitung / vorzubereiten / Frist |

## Anwendungsbeispiel
LausitzStorage-Akte: Reiter 3 enthaelt 12 Positionen, sortiert nach Frist:
- 09.06.: Aushaendigung LEAG-Aval (Frist § 11 Pacht ueberzogen)
- 10.06.: Notartermin Klarstellungs-Nachtrag Pacht
- 11.06.: Klarstellungs-Side-Letter Anlage 4
- 18.06.: ILB-Komitee Einzelaval 50Hertz
- 30.06.: BImSchG-Hauptantrag (Drohfrist LEAG)

## Output-Module
- Tabelleneintraege fuer Reiter 3
- Frist-Liste aufsteigend
- Eingangsstapel fuer Reiter 4 (Workflow)
- Optional Reiter 5 (Fristenkontrolle) mit Querverweis

## Grenzen
- **Beschaffungswege koennen sich verschieben.** Behoerdliche Bearbeitungszeiten
  realistisch ansetzen, nicht idealisieren.
- **Frist-Tracking ersetzt keinen Fristenkalender.** Anwaltlicher Fristenkalender
  bleibt verbindlich.

## Plugin-Kontext
Reiter 3 ist die Voraussetzung fuer Reiter 4. Ohne saubere Liste der
fehlenden Stuecke kann kein Workflow gebaut werden.
