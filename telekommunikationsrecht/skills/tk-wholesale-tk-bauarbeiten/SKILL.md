---
name: tk-wholesale-tk-bauarbeiten
description: "TK Wholesale TK Bauarbeiten im Telekommunikationsrecht: prüft konkret Wholesale-, Reseller- und MVNO-Verträge, Kabelschäden. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Wholesale TK Bauarbeiten

## Arbeitsbereich

Dieser Skill behandelt **TK Wholesale TK Bauarbeiten** als zusammenhängenden Arbeitsgang im Telekommunikationsrecht. Im Mittelpunkt steht die Prüfung von Wholesale-, Reseller- und MVNO-Verträge, Kabelschäden. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-wholesale-reseller-mvno-vertrag` | Wholesale-, Reseller- und MVNO-Verträge: Zugang, SLA, Entgelt, Nummerierung, Kundenschutz, Datenschutz und Exit. |
| `tk-bauarbeiten-kabelschaden` | Kabelschäden: Leitungsauskunft, Verkehrssicherung, Tiefbau, Schadensersatz, Betriebsunterbrechung und Beweissicherung. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-wholesale-reseller-mvno-vertrag`

**Fokus:** Wholesale-, Reseller- und MVNO-Verträge: Zugang, SLA, Entgelt, Nummerierung, Kundenschutz, Datenschutz und Exit.

# Wholesale, Reseller und MVNO-Verträge

## Einsatz

Für Anbieterketten im Mobilfunk/Festnetz.

## Norm- und Quellenanker

TKG; BGB/HGB; GWB; DSGVO/TKG-Datenschutz.

## Arbeitsfragen

1. Wer schuldet Endkundenleistung?
2. Welche Vorleistungen/SLA?
3. Welche Daten- und Nummernverantwortung?

## Output

Vertrags-Redline und Risikoampel.

## Red Flags

- Endkundenpflichten fehlen
- Nummernportierung ungeklärt
- SLA ohne Sanktion

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-bauarbeiten-kabelschaden`

**Fokus:** Kabelschäden: Leitungsauskunft, Verkehrssicherung, Tiefbau, Schadensersatz, Betriebsunterbrechung und Beweissicherung.

# Kabelschaden durch Bauarbeiten

## Einsatz

Für Netzbetreiber, Bauunternehmen und Versicherer.

## Norm- und Quellenanker

BGB §§ 823, 280; TKG Infrastruktur; Straßen-/Baurecht; ZPO.

## Arbeitsfragen

1. Wurde Leitungsauskunft eingeholt?
2. Welche Pläne und Markierungen?
3. Welcher Schaden und Folgeschaden?

## Output

Kabelschaden-Dossier und Anspruchsschreiben.

## Red Flags

- Leitungspläne veraltet
- Folgeschäden unbelegt
- Subunternehmerkette unklar

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
