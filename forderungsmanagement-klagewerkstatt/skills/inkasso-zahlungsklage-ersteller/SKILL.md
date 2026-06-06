---
name: inkasso-zahlungsklage-ersteller
description: "Erstellt eine Zahlungsklage fuer einen gewerblichen Glaeubiger nach abgeschlossenem Inkassovorlauf. Setzt aussergerichtliche Mahnung und Verzug voraus und bringt Inkassokosten Verzugszinsen und Pauschale 40 Euro mit ein. Pinpoints BGB 286 BGB 288 RDG 13 ZPO 253. Liefert klagefertiges DOCX und Markdown."
---

# Inkasso-Zahlungsklage Ersteller

Standardpfad fuer gewerbliche Glaeubiger mit aussergerichtlichem Inkassovorlauf. Klage knuepft nahtlos an die Mahnstrecke an.

## Pruefliste vor Klagefertigung

| Punkt | Pflicht |
|---|---|
| aussergerichtliche Mahnung erfolgt | ja Beleg Datum |
| Verzug eingetreten | nach BGB 286 |
| Forderung faellig | konkrete Faelligkeit |
| Inkassokosten dokumentiert | Inkassovertrag und Rechnung |
| Mandantenfreigabe | schriftlich |

## Inkassokosten als Verzugsschaden

Inkassokosten sind ersatzfaehig wenn der Schuldner in Verzug ist und die Beauftragung notwendig und zweckmaessig war BGB 280 286. Hoehe ist auf das beschraenkt was eine Rechtsanwaeltin nach RVG haette berechnen koennen RDG 13c.

## Verzugszinsen

- B2C fuenf Prozentpunkte ueber Basiszinssatz BGB 288 Abs. 1
- B2B neun Prozentpunkte ueber Basiszinssatz BGB 288 Abs. 2
- Pauschale 40 Euro nur B2B Hauptforderung BGB 288 Abs. 5

## Muster Antrag inklusive Inkassokosten

```
Die Beklagte wird verurteilt an die Klaegerin
einen Betrag von [Hauptsumme] Euro nebst Zinsen
in Hoehe von neun Prozentpunkten ueber dem
Basiszinssatz seit [Datum]
sowie weitere [Inkassokosten] Euro nebst Zinsen
in Hoehe von fuenf Prozentpunkten ueber dem
Basiszinssatz seit Rechtshaengigkeit sowie
40 Euro Verzugskostenpauschale zu zahlen.
```

## Norm-Pinpoints

- BGB 280 286 288
- RDG 13 13c
- ZPO 253

## Quellen

- [BGB 288](https://www.gesetze-im-internet.de/bgb/__288.html)
- [RDG 13](https://www.gesetze-im-internet.de/rdg/__13.html)
