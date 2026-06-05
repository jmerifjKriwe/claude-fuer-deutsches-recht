---
name: tk-beschwerde-tk-beweisplan
description: "TK Beschwerde TK Beweisplan im Telekommunikationsrecht: prüft konkret Dashboard für Massenbeschwerden, Technischer Beweisplan für TK-Streit. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Beschwerde TK Beweisplan

## Arbeitsbereich

Dieser Skill behandelt **TK Beschwerde TK Beweisplan** als zusammenhängenden Arbeitsgang im Telekommunikationsrecht. Im Mittelpunkt steht die Prüfung von Dashboard für Massenbeschwerden, Technischer Beweisplan für TK-Streit. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-beschwerde-dashboard-bnetza` | Dashboard für Massenbeschwerden: Anbieterwechsel, Störung, Rufnummer, Werbeanruf, Rechnung, Missbrauch und Fristen. |
| `tk-beweisplan-messung-stoerung-protokoll` | Technischer Beweisplan für TK-Streit: Breitbandmessung, Ausfallprotokoll, Routerlogs, Technikertermine, Fotos, Tickets, SLA und Zeugen. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
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
