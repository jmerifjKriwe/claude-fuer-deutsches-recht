---
name: kompendium-22-tk-sla-business-kund-bis-tk-standardangebot-r
description: "telekommunikationsrecht: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (tk-sla-business-kunden-ausfall, tk-standardangebot-reference-offer) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 22 - telekommunikationsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `tk-sla-business-kunden-ausfall` | Geschäftskunden-SLA: Verfügbarkeit, Reaktions-/Entstörzeiten, Credits, Schadensersatz, Haftungsbegrenzung und Force Majeure. |
| `tk-standardangebot-reference-offer` | Standardangebotspflichten, Prüfung von Klauseln, Änderungsanordnung, Zugangsnachfrage und Nichtdiskriminierung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `tk-sla-business-kunden-ausfall`

**Frühere Beschreibung:** Geschäftskunden-SLA: Verfügbarkeit, Reaktions-/Entstörzeiten, Credits, Schadensersatz, Haftungsbegrenzung und Force Majeure.

# Business-SLA und Ausfall

## Einsatz

Für Unternehmen, deren Geschäft an Konnektivität hängt.

## Norm- und Quellenanker

BGB; TKG; AGB-Recht §§ 305 ff. BGB; ZPO.

## Arbeitsfragen

1. Welche SLA-Kennzahl gilt?
2. Wie wird Ausfall gemessen?
3. Welche Haftung ist begrenzt?

## Output

SLA-Claim und Vertrags-Redline.

## Red Flags

- Credit ersetzt Schaden angeblich vollständig
- Messpunkte fehlen
- AGB-Haftung zu weit beschränkt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-standardangebot-reference-offer`

**Frühere Beschreibung:** Standardangebotspflichten, Prüfung von Klauseln, Änderungsanordnung, Zugangsnachfrage und Nichtdiskriminierung.

# Standardangebot und Reference Offer

## Einsatz

Für Vorleistungsangebote, die reguliert, genehmigt oder angegriffen werden.

## Norm- und Quellenanker

TKG; BNetzA-Standardangebotsverfahren; AGB-Recht.

## Arbeitsfragen

1. Welche Klausel behindert Zugang?
2. Welche BNetzA-Festlegung gilt?
3. Ist die Klausel diskriminierend oder unpraktikabel?

## Output

Klausel-Redline und BNetzA-Stellungnahme.

## Red Flags

- SLA zu niedrig
- Kündigungsrechte asymmetrisch
- Bestellprozesse praktisch blockierend

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
