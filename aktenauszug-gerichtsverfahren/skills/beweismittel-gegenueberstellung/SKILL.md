---
name: beweismittel-gegenueberstellung
description: "Erstellt eine tabellarische Uebersicht aller Beweisangebote: Zeugen Urkunden (mit Anlagenbezeichnung) Sachverstaendige Parteivernehmung und Augenschein getrennt nach Partei und streitigem Punkt. Fundstellen in Schriftsaetzen werden angegeben. Keine Bewertung der Beweiskraft."
---

# Beweismittel — Gegenüberstellung

## Zweck

Die Beweismitteltabelle listet alle in den Schriftsätzen angebotenen Beweismittel beider Parteien auf und ordnet sie den jeweiligen Beweisthemen zu. Sie ermöglicht einen schnellen Überblick über die Beweissituation.

## Zulässige Beweismittel (§ 355 ff. ZPO)

- Zeugenbeweis (§ 373 ff. ZPO)
- Urkundenbeweis (§ 415 ff. ZPO)
- Sachverständigenbeweis (§ 402 ff. ZPO)
- Parteivernehmung (§ 445 ff. ZPO)
- Augenscheinsbeweis (§ 371 ff. ZPO)

## Tabellenstruktur

```markdown
| Beweisthema | Beweismittel | Partei | Bezeichnung / Name | Fundstelle |
|---|---|---|---|---|
| [Streitpunkt] | [Art] | Kläger / Beklagter | [Name / Anlage] | [Schriftsatz Bl.] |
```

## Beispiel

| Beweisthema | Beweismittel | Partei | Bezeichnung / Name | Fundstelle |
|---|---|---|---|---|
| Vertragsinhalt Einweisung | Urkunde | Kläger | Werkvertrag K 1 | Klageschrift Bl. 12 |
| Mangel Dach | Zeuge | Kläger | Heiko Mustermann (Bauleiter) | Klageschrift Bl. 28 |
| Mangel Dach | Sachverständiger | Kläger | Einholung eines Baugutachtens | Klageschrift Bl. 29 |
| Ursache Undichtigkeit | Zeuge | Beklagter | Maria Musterfrau (Mitarbeiterin) | Klageerwiderung Bl. 52 |
| Schadenshöhe | Urkunde | Kläger | Sanierungskostenrechnung K 8 | Replik Bl. 70 |
| Schadenshöhe | Sachverständiger | Beklagter | Gegengutachten (beantragt) | Klageerwiderung Bl. 66 |

## Besondere Hinweise

### Urkundenbeweis

Jede Urkunde wird mit ihrer Anlagenbezeichnung (K 1, B 1 etc.) und einem kurzen Inhaltsvermerk aufgeführt.

### Zeugen

Vollständiger Name (sofern bekannt), Eigenschaft (z. B. „Augenzeuge", „Vertragspartner", „Mitarbeiter"), benennende Partei.

### Sachverständige

Wird ein Gutachten beantragt (nicht bereits vorhanden), so ist das Beweisthema zu nennen. Liegt ein Gutachten bereits vor, wird das Gutachten als Urkunde und der Gutachter als gesondert aufgeführt.

### Parteivernehmung

Selten — nur wenn angeboten oder angeordnet. Partei und Vernehmungsthema benennen.

### Präkludierte Beweismittel

Soweit Beweismittel vom Gericht als verspätet zurückgewiesen wurden, werden sie mit dem Vermerk „[zurückgewiesen]" aufgeführt.

## Qualitätscheck

- [ ] Alle angebotenen Beweismittel erfasst?
- [ ] Beweisthema klar bezeichnet?
- [ ] Anlagenbezeichnung und Fundstelle angegeben?
- [ ] Keine Bewertung der Beweiskraft?
- [ ] Präkludierte Beweismittel gekennzeichnet?
