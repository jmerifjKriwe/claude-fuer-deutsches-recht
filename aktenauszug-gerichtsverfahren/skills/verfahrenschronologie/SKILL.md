---
name: verfahrenschronologie
description: "Erstellt eine chronologische Bullet-Liste aller prozessualen Schritte: Klageeingang Zustellungen Schriftsatzfristen Beweisbeschluesse muendliche Verhandlungen Beweisaufnahme Urteile und Rechtsmittel. Kritische Fristen werden optisch hervorgehoben. Fundstellen werden angegeben."
---

# Verfahrenschronologie

## Zweck

Die Verfahrenschronologie erfasst alle prozessualen Schritte in zeitlicher Reihenfolge. Sie unterscheidet sich von der Sachverhaltschronologie dadurch, dass sie ausschließlich innerhalb des Verfahrens liegende Handlungen und Ereignisse abbildet.

## Was gehört hinein

- Klageeingang / Antragseingang beim Gericht
- Zahlung des Gerichtskostenvorschusses
- Zustellung der Klageschrift / des Arrestgesuchs
- Klageerwiderung und alle weiteren Schriftsätze (mit Datum)
- Richterliche Verfügungen und Hinweisbeschlüsse
- Beweisbeschlüsse
- Terminsladungen
- Mündliche Verhandlungen (mit Ergebnis / Protokollvermerk)
- Beweisaufnahme (Zeugenvernehmung, Sachverständigengutachten)
- Eingang von Gutachten
- Urteile und Beschlüsse (mit Tenor)
- Rechtsmittelfristen und Einlegung von Rechtsmitteln
- Vollstreckungsmaßnahmen

## Was nicht hinein gehört

- Außerprozessuale Ereignisse (→ Sachverhaltschronologie)
- Rechtliche Bewertungen der Schriftsätze

## Formatvorgabe

```
- **TT.MM.JJJJ** [Kurzbeschreibung des prozessualen Schritts] (Fundstelle: [Blatt])
- ⚠️ **TT.MM.JJJJ — FRIST:** [Fristbezeichnung — z. B. Berufungsfrist] (Fundstelle: [Blatt])
```

## Hervorhebung von Fristen

Jede prozessrelevante Frist wird mit dem Präfix `⚠️ FRIST:` gekennzeichnet und ans Ende der Chronologie als eigener Block wiederholt:

```
## Fristen und Termine (Übersicht)

| Frist / Termin | Datum | Status |
|---|---|---|
| Berufungsfrist (§ 517 ZPO) | TT.MM.JJJJ | läuft |
| Begründungsfrist (§ 520 ZPO) | TT.MM.JJJJ | läuft |
| Nächste mündliche Verhandlung | TT.MM.JJJJ | angesetzt |
```

## Beispiele

```
- **08.02.2023** Eingang der Klageschrift beim Landgericht Frankfurt am Main (Bl. 1)
- **15.02.2023** Anforderung des Gerichtskostenvorschusses (Bl. 5)
- **22.02.2023** Einzahlung des Gerichtskostenvorschusses durch Klägerin (Bl. 7)
- **03.03.2023** Zustellung der Klageschrift an Beklagte (Bl. 9)
- **14.04.2023** Eingang der Klageerwiderung (Bl. 12-45)
- **20.06.2023** Terminsladung zur mündlichen Verhandlung am 15.09.2023 (Bl. 48)
- **15.09.2023** Mündliche Verhandlung; Beweisbeschluss über Einholung Sachverständigengutachten (Bl. 60-62)
- **10.01.2024** Eingang des Sachverständigengutachtens (Bl. 80-140)
- **05.04.2024** Verkündung des Urteils; Klage abgewiesen (Bl. 200-215)
- ⚠️ **05.05.2024 — FRIST:** Berufungsfrist gemäß § 517 ZPO (einen Monat ab Zustellung)
```

## Besonderheiten nach Verfahrensart

**Eilverfahren:** Vollziehungsfrist des § 929 Abs. 2 ZPO besonders hervorheben.

**Strafverfahren:** Eröffnungsbeschluss, Ladungen, Hauptverhandlungstermine, Einlegung von Rechtsmitteln nach § 333 ff. StPO.

**Verwaltungsverfahren:** Widerspruchsverfahren als vorgelagerte Phase einschließen; Klagefrist des § 74 VwGO.

## Qualitätscheck

- [ ] Alle prozessualen Schritte erfasst?
- [ ] Chronologisch sortiert?
- [ ] Fristen hervorgehoben?
- [ ] Fristentabelle vorhanden?
- [ ] Keine außerprozessualen Ereignisse enthalten?
