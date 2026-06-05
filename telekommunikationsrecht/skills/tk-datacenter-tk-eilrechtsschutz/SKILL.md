---
name: tk-datacenter-tk-eilrechtsschutz
description: "TK Datacenter TK Eilrechtsschutz im Telekommunikationsrecht: prüft konkret Rechenzentrumskonnektivität, Eilrechtsschutz bei Frequenz-, Entgelt-, Zugang-. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Datacenter TK Eilrechtsschutz

## Arbeitsbereich

Dieser Skill behandelt **TK Datacenter TK Eilrechtsschutz** als zusammenhängenden Arbeitsgang im Telekommunikationsrecht. Im Mittelpunkt steht die Prüfung von Rechenzentrumskonnektivität, Eilrechtsschutz bei Frequenz-, Entgelt-. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-datacenter-connectivity` | Rechenzentrumskonnektivität: Carrier Meet-Me, Cross-Connects, SLA, Wegerecht im Gebäude, Datenschutz/Sicherheit und Ausfallhaftung. |
| `tk-eilrechtsschutz-bnetza-beschluss` | Eilrechtsschutz bei Frequenz-, Entgelt-, Zugang-, Nummerierungs- oder Missbrauchsmaßnahmen. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-datacenter-connectivity`

**Fokus:** Rechenzentrumskonnektivität: Carrier Meet-Me, Cross-Connects, SLA, Wegerecht im Gebäude, Datenschutz/Sicherheit und Ausfallhaftung.

# Datacenter Connectivity und Carrier Meet-Me

## Einsatz

Für Rechenzentren, Carrier und Unternehmenskunden.

## Norm- und Quellenanker

BGB; TKG; NIS2/BSI; AGB-Recht.

## Arbeitsfragen

1. Welche Connects und Carrier?
2. Welche Verfügbarkeit und Wartungsfenster?
3. Welche Sicherheitszonen?

## Output

Connectivity-Vertragscheck und Ausfallplan.

## Red Flags

- Cross-Connect ohne klare Verantwortung
- Wartungsfenster zu breit
- Security-Zutritt ungeklärt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-eilrechtsschutz-bnetza-beschluss`

**Fokus:** Eilrechtsschutz bei Frequenz-, Entgelt-, Zugang-, Nummerierungs- oder Missbrauchsmaßnahmen.

# Eilrechtsschutz gegen BNetzA-Beschluss

## Einsatz

Wenn ein BNetzA-Beschluss sofort wirtschaftlich wirkt.

## Norm- und Quellenanker

VwGO §§ 80, 80a, 123; TKG; VwVfG.

## Arbeitsfragen

1. Hat der Rechtsbehelf aufschiebende Wirkung?
2. Welche irreversiblen Nachteile drohen?
3. Wie wird Interessenabwägung belegt?

## Output

Eilantragsskizze und Anlagenliste.

## Red Flags

- Eilbedürftigkeit nicht belegt
- Hauptsachechancen fehlen
- Dritte nicht beigeladen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
