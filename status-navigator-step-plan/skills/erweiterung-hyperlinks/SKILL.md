---
name: erweiterung-hyperlinks
description: "Verknuepft die Tabelleneintraege mit den Originaldokumenten in der Dokumentenablage. Hyperlinks von der Tabelle zum jeweiligen Original ermoeglichen schnellen Sprung in den Volltext."
---

> **Hinweis:** Plugin `status-navigator-step-plan`, Dokumentenverarbeitung
> ohne Normen-Anker. Rechtliche Pruefung bleibt anwaltliche Aufgabe.

# Erweiterung Hyperlinks zur Ablage

## Rolle und Fokus
Verknuepft Tabelleneintraege mit Originaldokumenten in der Ablage. Sprung von der Tabelle zum Volltext spart Sucherei bei jeder Folgepruefung.

## Vorgehen

1. **Stabile Ablagestruktur festlegen** — Ordnerbaum mit Vertragsklasse, Nummer, Datum; keine Umbenennung nach Verlinkung.
2. **Relative oder absolute Pfade** — Bei Datenraum: absoluter Link; bei lokaler Akte: relativer Pfad zur Mappe.
3. **Hyperlink-Spalte je Reiter einfuegen** — Klick-Sprung direkt aus der Statuszeile.
4. **Anlagen separat verlinken** — Nicht nur Hauptdokument, sondern auch Schluesselanlagen wie Cap Table-Version, Beschluss, Anhaenge.
5. **Linkbruch-Pruefung als Wartung** — Periodischer Check ob alle Links erreichbar; rote Markierung bei Bruch.

## Anwendungsbeispiel
LausitzStorage-Akte: Reiter 1 verlinkt alle 19 Hauptdokumente in den Mandantsfileshare. Anlage 4 zum Konsortialvertrag bekommt Platzhalter-Link `_FEHLT_` damit beim Klick sofort sichtbar ist dass die Anlage in Reiter 3 nachverfolgt wird.

## Output-Module
- Hyperlink-Spalte je Reiter (relativer Pfad)
- Platzhalter-Link `_FEHLT_` fuer in Reiter 3 verfolgte Luecken
- Wartungspruefung als Eintrag in `erweiterung-laufende-aktualisierung`

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Subsumtion bleibt anwaltliche Aufgabe.
- **Hinweise, keine Befunde.** Markierungen muessen anwaltlich verifiziert werden.
- **Datenschutz und Berufsrecht.** Nutzung nur mit System, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfuellt.
