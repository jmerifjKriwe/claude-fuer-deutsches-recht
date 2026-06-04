---
name: kompendium-21-tk-satellite-starlin-bis-tk-schlichtung-verbr
description: "telekommunikationsrecht: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (tk-satellite-starlink-ntn, tk-schlichtung-verbraucher) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 21 - telekommunikationsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `tk-satellite-starlink-ntn` | Satelliteninternet/NTN: Frequenzen, Genehmigung, Endgeräte, Verbrauchervertrag, Resilienz und nationale Sicherheitsaspekte. |
| `tk-schlichtung-verbraucher` | Verbraucherschlichtung bei TK-Streit: Voraussetzungen, Antrag, Unterlagen, Hemmung/Fristen, Verhältnis zu Klage und BNetzA-Beschwerde. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `tk-satellite-starlink-ntn`

**Frühere Beschreibung:** Satelliteninternet/NTN: Frequenzen, Genehmigung, Endgeräte, Verbrauchervertrag, Resilienz und nationale Sicherheitsaspekte.

# Satellitenkommunikation und NTN

## Einsatz

Für Starlink-/LEO-/NTN-Projekte und Kundenstreit.

## Norm- und Quellenanker

TKG Frequenz/Marktzugang; EU/ITU-Rahmen live prüfen; BNetzA.

## Arbeitsfragen

1. Welche Satelliten-/Bodeninfrastruktur?
2. Welche Frequenz-/Marktzugangslage?
3. Welche Vertrags- und Resilienzrisiken?

## Output

Satelliten-TK-Memo und Genehmigungscheck.

## Red Flags

- ausländische Lizenz genügt angeblich immer
- Endgerät nicht zugelassen
- Resilienzversprechen überzogen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-schlichtung-verbraucher`

**Frühere Beschreibung:** Verbraucherschlichtung bei TK-Streit: Voraussetzungen, Antrag, Unterlagen, Hemmung/Fristen, Verhältnis zu Klage und BNetzA-Beschwerde.

# Verbraucherschlichtung Telekommunikation

## Einsatz

Für Verbraucher, die schnell und kostenschonend Druck aufbauen wollen.

## Norm- und Quellenanker

TKG Schlichtung; Verbraucherstreitbeilegungsrecht; BGB/ZPO.

## Arbeitsfragen

1. Ist Anbieterkontakt erfolgt?
2. Welche Forderung?
3. Welche Belege?

## Output

Schlichtungsantrag und Vergleichsvorschlag.

## Red Flags

- Frist/Verjährung parallel
- Forderung unbeziffert
- Geschäftskundenfall

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
