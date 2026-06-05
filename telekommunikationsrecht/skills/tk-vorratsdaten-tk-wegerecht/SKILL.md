---
name: tk-vorratsdaten-tk-wegerecht
description: "TK Vorratsdaten TK Wegerecht im Telekommunikationsrecht: prüft konkret Vorratsdatenspeicherung, Quick Freeze, Sicherheitsbehördenanfragen und EuGH/BVer, Wegerecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Vorratsdaten TK Wegerecht

## Arbeitsbereich

Dieser Skill behandelt **TK Vorratsdaten TK Wegerecht** als zusammenhängenden Arbeitsgang im Telekommunikationsrecht. Im Mittelpunkt steht die Prüfung von Vorratsdatenspeicherung, Quick Freeze, Sicherheitsbehördenanfragen und EuGH/BVer. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-vorratsdaten-speicherung-eugh-bverfg` | Vorratsdatenspeicherung, Quick Freeze, Sicherheitsbehördenanfragen und EuGH/BVerfG-Linie live prüfen. |
| `tk-wegerecht-oeffentliche-wege` | Wegerecht, Mitverlegung, Baustellenkoordination, Zustimmung, Wiederherstellung und Streit mit Straßenbaulastträgern. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-vorratsdaten-speicherung-eugh-bverfg`

**Fokus:** Vorratsdatenspeicherung, Quick Freeze, Sicherheitsbehördenanfragen und EuGH/BVerfG-Linie live prüfen.

# Vorratsdaten und Speicherpflichten

## Einsatz

Für Provider und Betroffene bei Speicher-/Auskunftspflichten.

## Norm- und Quellenanker

TKG/TTDSG/TDDDG; DSGVO; GRCh; GG; EuGH/BVerfG nur verifiziert zitieren.

## Arbeitsfragen

1. Welche Pflicht oder Anfrage liegt vor?
2. Welche Datenart und Eingriffsintensität?
3. Welche aktuelle EuGH/BVerfG-Rechtsprechung ist einschlägig?

## Output

Speicherpflichten-Memo und Behördenantwort.

## Red Flags

- alte Vorratsdatenlage verwendet
- Bestandsdaten/Verkehrsdaten verwechselt
- Richtervorbehalt ungeprüft

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-wegerecht-oeffentliche-wege`

**Fokus:** Wegerecht, Mitverlegung, Baustellenkoordination, Zustimmung, Wiederherstellung und Streit mit Straßenbaulastträgern.

# Wegerecht für öffentliche Wege

## Einsatz

Für Netzbau auf öffentlichen Wegen.

## Norm- und Quellenanker

TKG Wegerechte live prüfen; Straßenrecht Bund/Länder; VwVfG/VwGO.

## Arbeitsfragen

1. Welche Straße/Fläche und welcher Träger?
2. Welche Zustimmung/Anzeige?
3. Welche Nebenbestimmungen und Wiederherstellungspflichten?

## Output

Wegerechtsantrag, Nebenbestimmungscheck und Bauzeitenplan.

## Red Flags

- falscher Straßenbaulastträger
- kommunale Sondernutzung überdehnt
- Wiederherstellungskosten ungeklärt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
