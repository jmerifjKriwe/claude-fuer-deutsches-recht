---
name: parteivortrag-gegenueberstellung
description: "Erstellt eine Tabelle mit zwei Spalten (Klaegerseite und Beklagtenseite) fuer streitige Sachverhaltsangaben Punkt fuer Punkt. Jeder Streitpunkt wird als eigene Zeile gegenuebergestellt. Fundstellen in Schriftsaetzen werden angegeben. Keine Wertung welcher Vortrag zutreffend ist."
---

# Parteivortrag — Gegenüberstellung

## Zweck

Die Parteivortrag-Tabelle stellt streitige Sachverhaltsangaben der Kläger- und der Beklagtenseite Punkt für Punkt gegenüber. Sie ermöglicht dem Anwalt, auf einen Blick zu erkennen, was tatsächlich streitig ist und was als unstreitig gilt.

## Tabellenstruktur

```markdown
| Streitpunkt | Klägerseite | Beklagtenseite |
|---|---|---|
| [Bezeichnung des Streitpunkts] | [Vortrag Kläger] | [Vortrag Beklagter] |
```

## Kategorien von Streitpunkten

- Vertragsinhalt (Leistungsumfang, Preis, Nebenabreden)
- Tatsächliche Leistungserbringung (wer hat was wann geliefert / erbracht)
- Mängel (ob Mangel vorliegt, wessen Ursache)
- Kenntnis und Verschulden
- Schaden und Schadenshöhe
- Vorgerichtliche Kommunikation (wer hat was gesagt)
- Fristen und Termine (Vereinbartes Lieferdatum etc.)

## Beispiel

| Streitpunkt | Klägerseite | Beklagtenseite |
|---|---|---|
| Leistungsumfang | Auftrag umfasste vollständige Schlüsselübergabe inkl. Einweisung (K 1, Bl. 12) | Einweisung war nicht vereinbart sondern nur Lieferung (B 1, Bl. 40) |
| Mangel Dach | Dach war bei Abnahme undicht nachweislich Wassereintritt im Oktober (K 4, Bl. 26) | Undichtigkeit erst durch unsachgemäße Nutzung entstanden (B 3, Bl. 50) |
| Verschulden | Beklagte kannte Mangel und schwieg (K 5, Bl. 29) | Kein Arglistvorwurf; Mangel war nicht erkennbar (B 4, Bl. 53) |
| Schadenshöhe | Schaden EUR 45.000 belegt durch Gutachten (K 8, Bl. 60) | Überhöhte Schadensberechnung; tatsächlicher Schaden unter EUR 15.000 (B 6, Bl. 65) |

## Unstreitige Punkte

Unstreitige Sachverhaltselemente werden unterhalb der Tabelle als Block „Unstreitiger Sachverhalt" aufgeführt. Sie fließen nicht in die Streitpunkt-Tabelle ein.

## Hinweise

- Pro Zeile genau ein Streitpunkt — nicht mehrere Punkte in einer Zelle
- Vortrag neutral wiedergeben (paraphrasieren, nicht werten)
- Fundstelle in Schriftsatz oder Anlage angeben
- Wenn eine Partei zu einem Punkt schweigt: „Kein Vortrag" in die entsprechende Zelle
- Keine Prognose welcher Vortrag zutrifft

## Qualitätscheck

- [ ] Alle wesentlichen Streitpunkte erfasst?
- [ ] Keine Wertung enthalten?
- [ ] Fundstellen angegeben?
- [ ] Unstreitiger Sachverhalt separat ausgewiesen?
