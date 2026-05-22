---
name: fristen-und-terminkalender
description: "Identifiziert und hebt alle prozessrelevanten Fristen und Termine hervor: Klagefrist Berufungsfrist Begründungsfrist muendliche Verhandlung Verkündungstermin Vollziehungsfrist. Fristen werden am Anfang des Aktenauszugs als eigene Box und in der Verfahrenschronologie markiert."
---

# Fristen und Terminkalender

## Zweck

Versäumte Fristen können zum Verlust des Verfahrens oder zur Haftung des Rechtsanwalts führen. Dieser Skill identifiziert alle prozessrelevanten Fristen und Termine aus der Akte und stellt sie prominent dar.

## Fristenarten

### Absolute Fristen (gesetzlich, nicht verlängerbar)

| Frist | Norm | Fristdauer | Berechnung |
|---|---|---|---|
| Berufungsfrist | § 517 ZPO | 1 Monat | ab Zustellung Urteil |
| Berufungsbegründungsfrist | § 520 Abs. 2 ZPO | 2 Monate | ab Zustellung Urteil |
| Revisionsfrist | § 548 ZPO | 1 Monat | ab Zustellung Urteil |
| Revisionsbegründungsfrist | § 551 ZPO | 2 Monate | ab Zustellung Urteil |
| Klagefrist KSchG | § 4 KSchG | 3 Wochen | ab Zugang Kündigung |
| Klagefrist VwGO | § 74 VwGO | 1 Monat | ab Zustellung Widerspruchsbescheid |
| Vollziehungsfrist eV | § 929 Abs. 2 ZPO | 1 Monat | ab Zustellung Beschluss |
| Berufungsfrist ArbGG | § 66 ArbGG | 1 Monat | ab Zustellung Urteil |
| Berufungsfrist SGG | § 151 SGG | 1 Monat | ab Zustellung Urteil |

### Richterliche Fristen (verlängerbar)

- Schriftsatzfristen des Gerichts (Klageerwiderung, Replik, Duplik)
- Frist zur Stellungnahme zu Hinweisbeschlüssen
- Frist zur Einzahlung von Auslagen (Sachverständigenvorschuss)

### Notfristen

Fristen, die nicht verlängerbar sind und bei denen Wiedereinsetzung nur unter engen Voraussetzungen möglich ist (z. B. Berufungsfrist).

## Output-Format (Fristenbox am Anfang)

```
╔══════════════════════════════════════════════════════════╗
║  ⚠️ FRISTEN UND TERMINE — SOFORT PRÜFEN                 ║
╠══════════════════════════════════════════════════════════╣
║ Berufungsfrist:    TT.MM.JJJJ  (§ 517 ZPO)              ║
║ Begründungsfrist:  TT.MM.JJJJ  (§ 520 ZPO)              ║
║ Nächste Verhandlung: TT.MM.JJJJ HH:UU Uhr               ║
║ Schriftsatzfrist:  TT.MM.JJJJ  (richterliche Anordnung) ║
╚══════════════════════════════════════════════════════════╝
```

Alternativ als Markdown-Tabelle:

```markdown
## ⚠️ Fristen und Termine — Sofort prüfen

| Frist / Termin | Datum | Norm | Status |
|---|---|---|---|
| Berufungsfrist | TT.MM.JJJJ | § 517 ZPO | läuft |
| Begründungsfrist | TT.MM.JJJJ | § 520 ZPO | läuft |
| Mündliche Verhandlung | TT.MM.JJJJ | Terminsverfügung | angesetzt |
```

## Berechnungshinweise

- Fristbeginn immer anhand des tatsächlichen Zustellungsdatums aus der Akte ermitteln
- Wenn Zustellungsdatum nicht bekannt: ausdrücklich als „Zustellungsdatum unbekannt — Frist nicht berechenbar" kennzeichnen
- Wochenenden und gesetzliche Feiertage nach § 222 ZPO i.V.m. §§ 187 188 BGB berücksichtigen

## Qualitätscheck

- [ ] Alle gesetzlichen Fristen aus der Akte erfasst?
- [ ] Fristenbox am Anfang des Aktenauszugs?
- [ ] Berechnungsgrundlage (Zustellungsdatum) angegeben?
- [ ] Fehlende Zustellungsdaten als „unbekannt" markiert?
- [ ] Fristen in der Verfahrenschronologie markiert?
