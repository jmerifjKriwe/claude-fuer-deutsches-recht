---
name: neutralitaetspruefung
description: "Prueft einen erstellten Aktenauszug auf unzulaessige Wertungen und Erfolgseinschaetzungen und neutralisiert diese. Markiert alle parteiischen Formulierungen Prognosen und Bewertungen und schlaegt neutrale Ersatzformulierungen vor. Sicherheitsgate vor Weitergabe des Auszugs."
---

# Neutralitätsprüfung

## Zweck

Der Aktenauszug muss neutral formuliert sein — er gibt den Stand eines Verfahrens wieder, ohne eine Seite zu bevorzugen oder eine Erfolgsprognose abzugeben. Dieser Skill prüft einen erstellten Aktenauszug auf Neutralitätsverstöße und schlägt Korrekturen vor.

## Verbotene Formulierungstypen

### Erfolgsprognosen (absolut verboten)

| Verboten | Erlaubt |
|---|---|
| „Die Klage wird Erfolg haben" | „Die Klage ist anhängig" |
| „Der Anspruch dürfte begründet sein" | „Die Klägerin macht [Anspruch] geltend" |
| „Die Verjährungseinrede greift durch" | „Die Beklagte erhebt die Verjährungseinrede" |
| „Das Gericht wird … erkennen" | „Das Gericht hat … nicht geäußert" |
| „offensichtlich unbegründet" | „nach Vortrag der Beklagten unbegründet" |

### Wertende Adjektive (zu vermeiden)

- substanzlos, unhaltbar, abwegig, überzeugend, zutreffend, unzutreffend
- zu Recht, zu Unrecht
- offensichtlich, eindeutig (ohne Quellenangabe)

### Parteiische Darstellung

- Ausführliche Wiedergabe des Vortrags einer Seite ohne entsprechende Gegenüberstellung der anderen Seite
- Formulierungen, die implizit eine Seite stärken („Trotz des klaren Wortlauts des Vertrags …")

## Prüfmethodik

### Schritt 1 — Scan auf verbotene Muster

Folgende Muster systematisch suchen:

- `dürfte`, `wird`, `sollte`, `kann davon ausgegangen werden`
- `zu Recht`, `zu Unrecht`, `offensichtlich`, `eindeutig`
- `überzeugt`, `überzeugend`, `substanzlos`, `unhaltbar`
- `Erfolgsaussichten`, `Erfolg haben`, `scheitern`

### Schritt 2 — Parteibalance prüfen

Jeder Abschnitt des Parteivortrag und der Rechtsargumente muss beide Seiten gleichgewichtig darstellen.

### Schritt 3 — Korrekturen vorschlagen

Für jede beanstandete Formulierung wird eine neutrale Ersatzformulierung vorgeschlagen.

## Ergebnis-Format

```markdown
## Neutralitätsprüfung — Ergebnis

### Beanstandungen

| Stelle | Ursprüngliche Formulierung | Ersatzformulierung |
|---|---|---|
| Zusammenfassung Satz 3 | „Der Anspruch dürfte begründet sein" | „Die Klägerin macht den Anspruch geltend" |
| Rechtsargument Zeile 4 | „offensichtlich verjährt" | „nach Vortrag der Beklagten verjährt" |

### Ergebnis

[BESTANDEN / ÜBERARBEITUNG ERFORDERLICH]

Anzahl Beanstandungen: [Zahl]
```

## Qualitätscheck — Checkliste

- [ ] Keine Erfolgsprognose enthalten?
- [ ] Keine wertenden Adjektive ohne Quellenattribution?
- [ ] Parteivortrag beider Seiten gleichgewichtig dargestellt?
- [ ] Fristen neutral als Tatsache, nicht als Gefahr formuliert?
- [ ] Keine implizit parteiische Darstellung?

## Hinweis

Die Neutralitätsprüfung ist kein Korrektorat des Aktenauszugs. Sie prüft ausschließlich auf Wertungen und Prognosen. Sachliche Fehler sind durch Abgleich mit der Akte zu beheben.
