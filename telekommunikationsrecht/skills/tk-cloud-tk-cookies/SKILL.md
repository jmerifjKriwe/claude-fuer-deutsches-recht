---
name: tk-cloud-tk-cookies
description: "TK Cloud TK Cookies im Telekommunikationsrecht: prüft konkret Cloud-PBX/VoIP, Telemedien-/TK-Schnittstelle. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Cloud TK Cookies

## Arbeitsbereich

Dieser Skill behandelt **TK Cloud TK Cookies** als zusammenhängenden Arbeitsgang im Telekommunikationsrecht. Im Mittelpunkt steht die Prüfung von Cloud-PBX/VoIP, Telemedien-/TK-Schnittstelle. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-cloud-telefonie-voip-compliance` | Cloud-PBX/VoIP: Notruf, Standort, Datenschutz, Aufzeichnung, Ausfallsicherheit, Rufnummern und internationale Nutzer. |
| `tk-cookies-telemedien-ttdsg-tdddg` | Telemedien-/TK-Schnittstelle: Cookies, Einwilligung, Endgerätezugriff, Consent-Banner und Telekommunikationsdienste. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-cloud-telefonie-voip-compliance`

**Fokus:** Cloud-PBX/VoIP: Notruf, Standort, Datenschutz, Aufzeichnung, Ausfallsicherheit, Rufnummern und internationale Nutzer.

# Cloud-Telefonie und VoIP

## Einsatz

Für Unternehmen und Provider mit Teams-/Zoom-/Cloud-Telefonie.

## Norm- und Quellenanker

TKG; TDDDG; DSGVO; Notrufvorschriften; BGB.

## Arbeitsfragen

1. Wer ist Anbieter/Reseller?
2. Wie funktionieren Notruf und Standort?
3. Welche Aufzeichnungen/Logs?

## Output

VoIP-Compliance-Check und Nutzerinformation.

## Red Flags

- Notruf bei Homeoffice falsch
- Aufzeichnung ohne Rechtsgrund
- Rufnummernmissbrauch

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-cookies-telemedien-ttdsg-tdddg`

**Fokus:** Telemedien-/TK-Schnittstelle: Cookies, Einwilligung, Endgerätezugriff, Consent-Banner und Telekommunikationsdienste.

# Cookies, Telemedien und TDDDG-Schnittstelle

## Einsatz

Für Anbieter, die TK-Dienste und Web-/App-Dienste kombinieren.

## Norm- und Quellenanker

TDDDG; DSGVO; ePrivacy; TKG.

## Arbeitsfragen

1. Ist Zugriff auf Endeinrichtung betroffen?
2. Welche Einwilligung ist erforderlich?
3. Wie passt das zu TK-Daten?

## Output

Consent- und Datenflusscheck.

## Red Flags

- Cookie und Verkehrsdaten vermischt
- berechtigtes Interesse überdehnt
- CMP falsch konfiguriert

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
