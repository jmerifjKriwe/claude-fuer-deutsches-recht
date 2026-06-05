---
name: tk-beschwerde-tk-beweisplan
description: "Tk Beschwerde Dashboard Bnetza, Tk Beweisplan Messung Stoerung Protokoll: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Beschwerde Dashboard Bnetza, Tk Beweisplan Messung Stoerung Protokoll

## Arbeitsbereich

In diesem Skill wird **Tk Beschwerde Dashboard Bnetza, Tk Beweisplan Messung Stoerung Protokoll** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-beschwerde-dashboard-bnetza` | Dashboard für Massenbeschwerden: Anbieterwechsel, Störung, Rufnummer, Werbeanruf, Rechnung, Missbrauch und Fristen. |
| `tk-beweisplan-messung-stoerung-protokoll` | Technischer Beweisplan für TK-Streit: Breitbandmessung, Ausfallprotokoll, Routerlogs, Technikertermine, Fotos, Tickets, SLA und Zeugen. |

## Arbeitsweg

Für **Tk Beschwerde Dashboard Bnetza, Tk Beweisplan Messung Stoerung Protokoll** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-beschwerde-dashboard-bnetza`

**Fokus:** Dashboard für Massenbeschwerden: Anbieterwechsel, Störung, Rufnummer, Werbeanruf, Rechnung, Missbrauch und Fristen.

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

**Fokus:** Technischer Beweisplan für TK-Streit: Breitbandmessung, Ausfallprotokoll, Routerlogs, Technikertermine, Fotos, Tickets, SLA und Zeugen.

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
