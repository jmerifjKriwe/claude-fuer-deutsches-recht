---
name: schwerpunktthemen-identifikation
description: "Identifiziert drei bis fuenf rechtliche Hauptstreitpunkte des Verfahrens mit Pinpoint-Zitaten aus Schriftsaetzen und ohne Erfolgsprognose. Jeder Streitpunkt wird mit Relevanz fuer den Verfahrensausgang und einschlaegiger Rechtsprechung (soweit in Akte enthalten) dargestellt."
---

# Schwerpunktthemen-Identifikation

## Zweck

Dieser Skill identifiziert die drei bis fünf zentralen Rechtsfragen, auf denen das Verfahren schwerpunktmäßig beruht. Er hilft dem Anwalt, die Prioritäten für die weitere Bearbeitung zu setzen, ohne eine Einschätzung des Ausgangs zu treffen.

## Kriterien für ein Schwerpunktthema

Ein Thema ist Schwerpunkt, wenn:

- Es in mehreren Schriftsätzen kontrovers diskutiert wird
- Das Gericht einen ausdrücklichen Hinweis dazu erteilt hat
- Ein Beweisbeschluss zu diesem Punkt ergangen ist
- Rechtsprechung der Parteien zu diesem Punkt zitiert wird
- Die Entscheidung im Verfahren von diesem Punkt maßgeblich abhängt

## Anzahl

Drei bis fünf Schwerpunktthemen. Bei einfachen Verfahren können es weniger sein; bei komplexen Verfahren werden trotzdem nicht mehr als fünf ausgewiesen — die übrigen Fragen werden in den Tabellen erfasst.

## Outputformat

```markdown
## Schwerpunktthemen

### 1. [Bezeichnung des Schwerpunktthemas]

**Beschreibung:** [Kurze Darstellung der Rechtsfrage]

**Parteiposition Kläger:** [Position ohne Wertung]

**Parteiposition Beklagter:** [Position ohne Wertung]

**Einschlägige Rechtsprechung (aus Akte):** [Zitat mit Aktenzeichen und Datum soweit in Schriftsätzen genannt]

**Fundstellen:** [Schriftsatz Bl. ...]

---
```

## Beispiel

### 1. Verjährung des Mangelbeseitigungsanspruchs

**Beschreibung:** Streitig ist, ob der Schadensersatzanspruch der Klägerin nach § 634a Abs. 1 Nr. 1 BGB (zwei Jahre ab Abnahme) bereits verjährt ist.

**Parteiposition Klägerin:** Verjährungsfrist beginnt erst mit Kenntnis des verdeckten Mangels; Frist läuft noch. Gestützt auf BGH Urt. v. 08.07.2021 — VII ZR 149/20.

**Parteiposition Beklagte:** Fristbeginn ist objektiv der Abnahmezeitpunkt; zwei Jahresfrist bereits abgelaufen. Gestützt auf BGH Urt. v. 12.03.2015 — VII ZR 173/13.

**Fundstellen:** Klageschrift Bl. 30-32; Klageerwiderung Bl. 55-58.

---

### 2. Wirksamkeit der Abnahme unter Vorbehalt

**Beschreibung:** Streitig ist, ob das unterzeichnete Abnahmeprotokoll einen Vorbehalt enthält oder vorbehaltlos ist.

**Parteiposition Klägerin:** Abnahme erfolgte unter Vorbehalt nach § 640 Abs. 1 S. 2 BGB (Bl. 20-21 Anlage K 2).

**Parteiposition Beklagte:** Protokoll enthält keinen Vorbehalt; vorbehaltlose Abnahme liegt vor.

**Fundstellen:** Klageschrift Bl. 20-22; Klageerwiderung Bl. 48-50.

## Hinweis

Schwerpunktthemen werden neutral dargestellt. Die Identifikation eines Themas als Schwerpunkt bedeutet keine Einschätzung, welche Seite in dieser Frage Recht hat.
