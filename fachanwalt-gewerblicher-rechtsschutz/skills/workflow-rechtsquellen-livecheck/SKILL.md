---
name: workflow-rechtsquellen-livecheck
description: "Rechtsquellen-Livecheck im gewerblichen Rechtsschutz: Verifikation von Normen, Rechtsprechung und Behördeninformationen. Quellenhierarchie, Live-Check-Protokoll, zugelassene Quellen und Vorgehensweise bei unsicheren Angaben."
---

# Rechtsquellen-Livecheck

## Aufgabe
Dieser Workflow-Skill sichert die Qualität von Rechtsquellen im gewerblichen Rechtsschutz: Live-Verifikation von Normen, Urteilen und Behördeninformationen vor Ausgabe oder Verwendung in Schriftsätzen.

## Warum Livecheck?

- Normen werden häufig geändert (UWG 2020, UrhG DSM-Umsetzung 2021, UPC 2023, EU AI Act 2024).
- Modellwissen kann veraltete Fassungen enthalten.
- Nicht verifizierte Urteile in Schriftsätzen sind berufsrechtlich riskant.
- Behördenformulare und Gebühren ändern sich regelmäßig.

## Quellenhierarchie

| Priorität | Quelltyp | Verlässlichkeit |
|---|---|---|
| 1 | Amtliche Gesetzesdatenbanken (gesetze-im-internet.de; eur-lex.europa.eu) | Sehr hoch |
| 2 | Behördliche Websites (DPMA, EUIPO, EPA, BGH, BPatG, ZSSR) | Sehr hoch |
| 3 | Offiziell veröffentlichte Gerichtsentscheidungen (bgh.de, bverfg.de, curia.europa.eu) | Sehr hoch |
| 4 | Dejure.org, openjur.de (Volltext-Reproduktionen mit Normenverknüpfung) | Hoch |
| 5 | Kommentare, Lehrbücher, Aufsätze | Mittel (nur mit Bearbeiter, Datum, Fundstelle) |
| 6 | Modellwissen / Trainingsdaten | Nicht ausreichend allein; immer mit Level 1–4 kombinieren |

## Zugelassene Live-Quellen

| Thema | Quelle | Link |
|---|---|---|
| Deutsche Gesetze | gesetze-im-internet.de | [gesetze-im-internet.de](https://www.gesetze-im-internet.de) |
| EU-Recht | EUR-Lex | [eur-lex.europa.eu](https://eur-lex.europa.eu) |
| BGH-Rechtsprechung | BGH-Website | [bundesgerichtshof.de](https://www.bundesgerichtshof.de) |
| BVerfG | BVerfG-Website | [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) |
| BPatG | BPatG-Website | [bundespatentgericht.de](https://www.bundespatentgericht.de) |
| EuGH / EuG | Curia | [curia.europa.eu](https://curia.europa.eu) |
| Normen + Rspr. verknüpft | dejure.org | [dejure.org](https://dejure.org) |
| OLG-/LG-Entscheidungen | openjur.de | [openjur.de](https://openjur.de) |
| DPMA | DPMA-Website | [dpma.de](https://www.dpma.de) |
| EUIPO | EUIPO-Website | [euipo.europa.eu](https://euipo.europa.eu) |
| EPA | EPA-Website | [epo.org](https://www.epo.org) |
| UPC | UPC-Website | [unified-patent-court.org](https://www.unified-patent-court.org) |
| ZSSR | ZSSR | [zssr.de](https://www.zssr.de) |
| WIPO | WIPO-Website | [wipo.int](https://www.wipo.int) |

## Live-Check-Protokoll

Für jede tragende Rechtsquelle:

```
Rechtsquelle: [Normbezeichnung / Aktenzeichen / Entscheidungsname]
Fundstelle: [URL]
Abgerufen am: [Datum]
Aktueller Inhalt: [Kernaussage; Normtext-Auszug oder Urteilstenor]
Veraltet? Nein / Ja → ggf. aktuellere Fassung:
```

## Umgang mit unsicheren Angaben

| Situation | Handlung |
|---|---|
| Aktenzeichen oder Datum unsicher | Ausdrücklich als „zu prüfen" markieren; Quelle angeben |
| Norm geändert (Verweis auf alte Fassung) | Neue Fassung aus gesetze-im-internet.de prüfen |
| Urteil nicht auffindbar | Nicht zitieren; als „Live-Check ausstehend" markieren |
| Gebühr / Frist geändert | Aus aktueller Behördenquelle neu ermitteln |
| Kommentar-Meinung als Tatsache dargestellt | Kommentar-Meinung als solche kennzeichnen (Autor, Werk, Randnummer, Datum) |

## Red-Flag-Liste (niemals ohne Live-Prüfung)

- Jahresgebühren DPMA / EUIPO / EPA (ändern sich regelmäßig).
- EUIPO-Widerspruchsgebühren.
- RVG-Tabellenwerte (bei Gesetzesänderungen).
- UPC-Verfahrensregeln (seit 2023 laufend angepasst).
- EU AI Act Umsetzungsdetails (in Anwendungsphase).
- Länderspezifische Verfahrensregeln (AT, CH, nicht-EU).

## Checkliste Livecheck vor Ausgabe

| Prüfpunkt | Erledigt? |
|---|---|
| Alle zitierten Normen aus gesetze-im-internet.de / EUR-Lex verifiziert | ☐ |
| Alle Urteile mit Gericht, Datum, AZ und Link aus offizieller Quelle | ☐ |
| Behördengebühren aus aktueller Behördenwebsite | ☐ |
| Unsichere Angaben als „zu prüfen" markiert | ☐ |
| Keine Kommentar-Blindzitate ohne Quellenangabe | ☐ |
| Keine Entscheidungen aus Modellwissen ohne Verifikation | ☐ |

## Kaltstart
1. Welche Rechtsquellen müssen für die aktuelle Aufgabe live geprüft werden?
2. Liegen bereits Normen / Aktenzeichen vor, die verifiziert werden sollen?
3. Handelt es sich um ein EU-Verfahren (EUR-Lex + Curia) oder ein nationales Verfahren?
4. Output: Live-Check-Protokoll, verifizierte Quellenangaben, Markierung unsicherer Stellen?

## Plugin-Kontext
Skill gehört zu `fachanwalt-gewerblicher-rechtsschutz`. Er wird von allen anderen Skills aufgerufen, wenn Rechtsquellen ausgegeben werden müssen.

## Was dieser Skill nicht macht
- Keine Interpretation von Quellen (das machen Spezialskills).
- Kein Ersatz für vollständige juristische Würdigung.
- Keine Garantie für Vollständigkeit der Quellen (Lücken ausdrücklich markieren).
