---
name: kompendium-07-tk-beschwerde-dashbo-bis-tk-beweisplan-messun
description: "telekommunikationsrecht: Konsolidiertes Skill-Kompendium 07; bündelt 2 frühere Spezialskills (tk-beschwerde-dashboard-bnetza, tk-beweisplan-messung-stoerung-protokoll) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 07 - telekommunikationsrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `tk-beschwerde-dashboard-bnetza` | Dashboard für Massenbeschwerden: Anbieterwechsel, Störung, Rufnummer, Werbeanruf, Rechnung, Missbrauch und Fristen. |
| `tk-beweisplan-messung-stoerung-protokoll` | Technischer Beweisplan für TK-Streit: Breitbandmessung, Ausfallprotokoll, Routerlogs, Technikertermine, Fotos, Tickets, SLA und Zeugen. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `tk-beschwerde-dashboard-bnetza`

**Frühere Beschreibung:** Dashboard für Massenbeschwerden: Anbieterwechsel, Störung, Rufnummer, Werbeanruf, Rechnung, Missbrauch und Fristen.

# BNetzA-Beschwerde-Dashboard

## Einsatz

Für Kanzleien, Unternehmen und Verbraucherzentralen mit vielen TK-Fällen.

## Norm- und Quellenanker

TKG; VwVfG; Verbraucherrecht; BNetzA-Formulare live prüfen.

## Arbeitsfragen

1. Welche Beschwerdekategorie?
2. Welche Belege und Status?
3. Welche Eskalation?

## Output

Beschwerdeboard, Statusliste und Standardtexte.

## Red Flags

- Beschwerden ohne Kategorie
- keine Ticketnummern
- Fristen nicht verfolgt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-beweisplan-messung-stoerung-protokoll`

**Frühere Beschreibung:** Technischer Beweisplan für TK-Streit: Breitbandmessung, Ausfallprotokoll, Routerlogs, Technikertermine, Fotos, Tickets, SLA und Zeugen.

# Beweisplan: Messung, Störung, Protokoll

## Einsatz

Für Verbraucher und Geschäftskunden, die nicht nur behaupten wollen, dass Internet oder Telefon schlecht waren.

## Norm- und Quellenanker

TKG Kundenschutz; BGB Leistungsstörung; ZPO Beweis; BNetzA-Breitbandmessungsvorgaben live prüfen.

## Arbeitsfragen

1. Welche vertragliche Leistung ist geschuldet?
2. Welche Messmethode ist anerkannt und reproduzierbar?
3. Welche Störung wurde wann wem gemeldet?
4. Welche wirtschaftlichen Folgen sind belegbar?

## Output

Mess- und Störungsdossier, Belegliste, Minderungs-/Schadensersatzbasis und Providerbrief.

## Red Flags

- Speedtest ohne Methodik
- WLAN-Problem als Leitungsproblem
- Ticketnummern fehlen
- SLA nicht gelesen

## Anschluss-Skills

- tk-stoerung-minderung-ausfallentschaedigung
- tk-sla-business-kunden-ausfall

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
