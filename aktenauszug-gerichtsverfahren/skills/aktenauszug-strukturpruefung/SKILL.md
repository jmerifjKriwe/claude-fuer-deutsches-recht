---
name: aktenauszug-strukturpruefung
description: "Prueft die Vollstaendigkeit eines Aktenauszugs auf Verfahrensidentifikation Einleitung Zusammenfassung Sachverhaltschronologie Verfahrensgeschichte Parteivortrag-Tabelle Beweismittel-Tabelle und Rechtsargumente-Tabelle. Prueft ob Fristen hervorgehoben und Sprache neutral sind."
---

# Aktenauszug — Strukturprüfung

## Zweck

Dieser Skill prüft einen erstellten Aktenauszug auf formale Vollständigkeit aller sechs Bausteine und auf die Einhaltung der Qualitätsgrundsätze (Fristen hervorgehoben, Sprache neutral). Er ist das abschließende Qualitätsgate vor der Übergabe an den Mandatsbearbeiter.

## Prüfcheckliste

### Baustein 1 — Verfahrensidentifikation

- [ ] Gericht und Kammer angegeben
- [ ] Aktenzeichen angegeben
- [ ] Instanz und Verfahrensart angegeben
- [ ] Streitwert angegeben (oder als unbekannt markiert)
- [ ] Alle Parteien mit Prozessbevollmächtigten aufgeführt

### Baustein 2 — Einleitungssatz

- [ ] Ein bis zwei Sätze vorhanden
- [ ] Wer streitet mit wem worüber benannt
- [ ] Hauptnorm genannt
- [ ] Keine Wertung enthalten

### Baustein 3 — Zusammenfassung

- [ ] Acht bis zehn Sätze vorhanden
- [ ] Hintergrund dargestellt
- [ ] Aktueller Verfahrensstand benannt
- [ ] Nächste Verfahrenshandlung benannt
- [ ] Keine Wertung / Prognose enthalten

### Baustein 4 — Sachverhaltschronologie

- [ ] Chronologisch sortiert
- [ ] Datum fettgedruckt vorangestellt
- [ ] Wesentliche außerprozessuale Ereignisse vollständig
- [ ] Fundstellen angegeben
- [ ] Keine prozessualen Schritte enthalten

### Baustein 5 — Verfahrenschronologie

- [ ] Chronologisch sortiert
- [ ] Alle prozessualen Schritte erfasst
- [ ] Fristen hervorgehoben (Präfix ⚠️ FRIST)
- [ ] Fristentabelle vorhanden
- [ ] Keine außerprozessualen Ereignisse enthalten

### Baustein 6 — Tabellen

**Parteivortrag:**
- [ ] Tabelle mit zwei Spalten (Kläger / Beklagter)
- [ ] Alle wesentlichen Streitpunkte als Zeilen
- [ ] Fundstellen angegeben

**Beweismittel:**
- [ ] Alle angebotenen Beweismittel erfasst
- [ ] Beweisthema je Beweismittel angegeben
- [ ] Anlagenbezeichnung angegeben

**Rechtsargumente:**
- [ ] Anspruchsgrundlagen beider Seiten erfasst
- [ ] Einwendungen und Einreden erfasst
- [ ] Verjährungsthema behandelt (falls relevant)
- [ ] Rechtsprechung mit Aktenzeichen angegeben

## Qualitätsgrundsätze

- [ ] Neutralitätsprüfung bestanden (keine Wertungen, keine Prognosen)
- [ ] Keine verbotenen Begriffe (keine KI-Terminologie)
- [ ] Fristen an prominenter Stelle (Fristenbox oder Fristentabelle am Anfang)
- [ ] Klare Markdown-Gliederung mit Überschriften

## Ergebnis-Format

```markdown
## Strukturprüfung — Ergebnis

| Baustein | Status | Anmerkung |
|---|---|---|
| Verfahrensidentifikation | ✓ vollständig | — |
| Einleitungssatz | ✓ vollständig | — |
| Zusammenfassung | ⚠️ unvollständig | Nächste Verfahrenshandlung fehlt |
| Sachverhaltschronologie | ✓ vollständig | — |
| Verfahrenschronologie | ✓ vollständig | — |
| Parteivortrag-Tabelle | ✓ vollständig | — |
| Beweismittel-Tabelle | ⚠️ unvollständig | B-Anlagen nicht erfasst |
| Rechtsargumente-Tabelle | ✓ vollständig | — |

**Gesamtergebnis:** ÜBERARBEITUNG ERFORDERLICH
**Offene Punkte:** [Anzahl]
```
