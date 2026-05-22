---
name: anlagenverzeichnis-extrakt
description: "Listet alle K-/B-/AST-/AG-Anlagen-Verweise mit Inhalt und Fundstelle in der Akte. Erstellt ein vollstaendiges Anlagenverzeichnis fuer jede Partei mit Anlagenbezeichnung Kurzbeschreibung Schriftsatz und Blattangabe. Erleichtert das schnelle Auffinden einzelner Anlagen."
---

# Anlagenverzeichnis-Extrakt

## Zweck

Umfangreiche Gerichtsakten enthalten oft Hunderte von Anlagen, die über verschiedene Schriftsätze verteilt sind. Dieser Skill erstellt ein geordnetes Anlagenverzeichnis, das alle Anlagen mit Bezeichnung, Inhalt und Fundstelle erfasst.

## Anlagenbezeichnungen

### Klägerseite

- K 1, K 2, K 3 ... (K = Kläger)
- AST 1, AST 2 ... (Antragsteller in Eilverfahren)

### Beklagtenseite

- B 1, B 2, B 3 ... (B = Beklagter)
- AG 1, AG 2 ... (Antragsgegner in Eilverfahren)

### Sonstige

- GA 1, GA 2 ... (Gericht, z. B. Sachverständigengutachten)
- SV 1, SV 2 ... (Sachverständiger)

## Tabellenstruktur

```markdown
| Anlage | Inhalt (kurz) | Datum des Dokuments | Schriftsatz | Blatt |
|---|---|---|---|---|
| K 1 | Werkvertrag vom TT.MM.JJJJ | TT.MM.JJJJ | Klageschrift | 12-18 |
| K 2 | Abnahmeprotokoll | TT.MM.JJJJ | Klageschrift | 19-21 |
| K 3 | Mängelrüge (Schreiben) | TT.MM.JJJJ | Klageschrift | 22 |
```

## Arbeitsschritte

1. Jeden Schriftsatz auf Anlagenverweise (K 1, B 1 etc.) durchsuchen
2. Anlage mit Inhalt und Datum erfassen
3. Schriftsatz und Blattangabe notieren
4. Alle Anlagen nach Partei getrennt tabellarisch listen
5. Auf Vollständigkeit prüfen (keine Lücken in der Nummerierung)

## Hinweise bei Lücken

Fehlende Anlage (z. B. K 4 nicht in der Akte): Eintrag mit dem Vermerk „[nicht in vorliegender Akte]".

## Beispiel (vollständig)

### Klägeranlagen

| Anlage | Inhalt | Datum | Schriftsatz | Blatt |
|---|---|---|---|---|
| K 1 | Werkvertrag | 15.03.2021 | Klageschrift 08.02.2023 | 12-18 |
| K 2 | Abnahmeprotokoll | 02.09.2021 | Klageschrift 08.02.2023 | 19-21 |
| K 3 | Mängelrüge | 14.10.2021 | Klageschrift 08.02.2023 | 22 |
| K 4 | Nachbesserungsprotokoll | 08.11.2021 | Klageschrift 08.02.2023 | 23-24 |
| K 5 | Rücktrittsandrohung | 03.01.2022 | Klageschrift 08.02.2023 | 25 |
| K 6 | Rücktrittserklärung | 15.02.2022 | Klageschrift 08.02.2023 | 26 |

### Beklagtenanlagen

| Anlage | Inhalt | Datum | Schriftsatz | Blatt |
|---|---|---|---|---|
| B 1 | E-Mail-Korrespondenz | versch. | Klageerwiderung 14.04.2023 | 40-44 |
| B 2 | Wartungsprotokoll | 05.09.2021 | Klageerwiderung 14.04.2023 | 45-47 |

## Qualitätscheck

- [ ] Alle Anlagenbezeichnungen aus allen Schriftsätzen erfasst?
- [ ] Lücken in der Nummerierung als fehlend markiert?
- [ ] Inhalt kurz aber aussagekräftig beschrieben?
- [ ] Fundstelle (Schriftsatz und Blatt) angegeben?
