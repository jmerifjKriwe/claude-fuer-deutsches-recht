---
name: dokumenten-inventur-grob
description: "Erzeugt eine erste grobe Liste aller vorhandenen Dateien mit Dateiname, Dateityp, Dateigroesse und sichtbarem Datum. Noch keine inhaltliche Pruefung — reine Bestandsaufnahme als Ausgangspunkt fuer die feinere Einordnung."
---

> **Hinweis:** Plugin `status-navigator-step-plan`, Dokumentenverarbeitung
> ohne Normen-Anker. Rechtliche Pruefung bleibt anwaltliche Aufgabe.

# Dokumenten-Inventur grob

## Rolle und Fokus
Erste Sichtung: Dateiname, Dateityp, Dateigroesse, sichtbares Datum. Noch keine inhaltliche Pruefung — Bestandsaufnahme als Ausgangspunkt fuer die feinere Einordnung.

## Vorgehen

1. **Dateilisting erzeugen** — Pfad, Dateiname, Endung, Groesse, mtime, sichtbares Datum aus Dateinamen-Konvention.
2. **Duplikatscheck** — Identische Hashes oder identische Bezeichnungen mit unterschiedlichen Inhalten markieren.
3. **Grobklasse zuordnen** — Vertrag, Beschluss, Erklaerung, Korrespondenz, Cap Table, Bescheid, sonstige.
4. **Lesbarkeitspruefung** — Scan-Qualitaet, OCR-Status, fehlende Seiten, leere Anlagen-Verweise.
5. **In Reiter 1 (Ueberblick) eintragen** — Verfuegbarkeit zunaechst pauschal `vorliegend`.

## Anwendungsbeispiel
LausitzStorage-Mandat: 80 PDFs aus drei Quellen (Datenraum NordCap, Mandantenpostfach, eigene Akte). Grobinventur findet 6 Duplikate (unterschiedliche Versionen des Pachtvertrags), 3 Dateien ohne lesbare Unterschriftsseite, 1 leere Anlage 4 zum Konsortialvertrag.

## Output-Module
- Roh-Inventur als CSV/Excel-Importzeile fuer Reiter 1
- Duplikatsliste mit Empfehlung welche Version fuehrend ist
- Lesbarkeits-Mangelliste (Nachforderung im Datenraum)

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Subsumtion bleibt anwaltliche Aufgabe.
- **Hinweise, keine Befunde.** Markierungen muessen anwaltlich verifiziert werden.
- **Datenschutz und Berufsrecht.** Nutzung nur mit System, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfuellt.
