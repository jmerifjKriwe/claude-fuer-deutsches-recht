---
name: tk-abmahnung-tk-anbieterwechsel
description: "TK Abmahnung TK Anbieterwechsel im Telekommunikationsrecht: prüft konkret Abmahnungen bei TK-Marketing, Preiswerbung, Rufnummernmissbrauch, Vergleichsport. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Abmahnung TK Anbieterwechsel

## Arbeitsbereich

Dieser Skill behandelt **TK Abmahnung TK Anbieterwechsel** als zusammenhängenden Arbeitsgang im Telekommunikationsrecht. Im Mittelpunkt steht die Prüfung von Abmahnungen bei TK-Marketing, Preiswerbung, Rufnummernmissbrauch. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-abmahnung-uwg-tkg` | Abmahnungen bei TK-Marketing, Preiswerbung, Rufnummernmissbrauch, Vergleichsportalen und Informationspflichten. |
| `tk-anbieterwechsel-rufnummernmitnahme` | Anbieterwechsel, Versorgungslücke, Rufnummernportierung, Entschädigung, Weiterversorgungspflicht und BNetzA-Beschwerde. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-abmahnung-uwg-tkg`

**Fokus:** Abmahnungen bei TK-Marketing, Preiswerbung, Rufnummernmissbrauch, Vergleichsportalen und Informationspflichten.

# Abmahnung nach UWG/TKG

## Einsatz

Für Wettbewerber, Verbände und Anbieter.

## Norm- und Quellenanker

UWG; TKG; PAngV; TDDDG/DSGVO; BGB.

## Arbeitsfragen

1. Welche Marktverhaltensregel?
2. Welche Werbung/Information ist falsch?
3. Welche Unterlassung und Vertragsstrafe?

## Output

Abmahnungs-/Verteidigungsschreiben und Beweisplan.

## Red Flags

- TKG-Norm keine Marktverhaltensregel geprüft
- Screenshot fehlt
- Unterlassung zu weit

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-anbieterwechsel-rufnummernmitnahme`

**Fokus:** Anbieterwechsel, Versorgungslücke, Rufnummernportierung, Entschädigung, Weiterversorgungspflicht und BNetzA-Beschwerde.

# Anbieterwechsel und Rufnummernmitnahme

## Einsatz

Für Verbraucher und Unternehmen, die beim Wechsel ohne Telefon/Internet oder ohne Rufnummer dastehen.

## Norm- und Quellenanker

TKG §§ 59 und Kundenschutzvorschriften live prüfen; BNetzA-Anbieterwechselinformationen; BGB.

## Arbeitsfragen

1. Wann wurde Wechsel/Portierung beauftragt?
2. Wer ist abgebender und aufnehmender Anbieter?
3. Welche Verzögerung ist wem zurechenbar?
4. Welche Entschädigung oder Beschwerde ist möglich?

## Output

Portierungszeitstrahl, Entschädigungsforderung, BNetzA-Beschwerde und Eskalationsmail.

## Red Flags

- Altanbieter schaltet ab
- Portierungsdatum unklar
- Rufnummer gehört Firma statt Mitarbeiter
- Entschädigung falsch berechnet

## Anschluss-Skills

- tk-schlichtung-verbraucher
- tk-output-beschwerde-antrag-klage

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
