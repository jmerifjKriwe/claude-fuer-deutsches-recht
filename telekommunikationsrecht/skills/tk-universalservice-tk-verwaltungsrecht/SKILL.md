---
name: tk-universalservice-tk-verwaltungsrecht
description: "TK Universalservice TK Verwaltungsrecht im Telekommunikationsrecht: prüft konkret Universaldienst/Mindestversorgung mit, Anfechtung, Verpflichtung oder Eilrechtsschutz gegen BNetzA-Beschlüsse. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Universalservice TK Verwaltungsrecht

## Arbeitsbereich

**TK Universalservice TK Verwaltungsrecht** ordnet den Fall über die tragenden Prüffelder: Universaldienst/Mindestversorgung mit, Anfechtung, Verpflichtung oder Eilrechtsschutz gegen BNetzA-Beschlüsse. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-universalservice-mindestversorgung` | Universaldienst/Mindestversorgung mit Telekommunikationsdiensten: Unterversorgung, Anspruch, BNetzA-Verfahren, technische Zumutbarkeit und Alternativen. |
| `tk-verwaltungsrecht-anfechtung-bnetza` | Anfechtung, Verpflichtung oder Eilrechtsschutz gegen BNetzA-Beschlüsse und Nebenbestimmungen. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-universalservice-mindestversorgung`

**Fokus:** Universaldienst/Mindestversorgung mit Telekommunikationsdiensten: Unterversorgung, Anspruch, BNetzA-Verfahren, technische Zumutbarkeit und Alternativen.

# Universaldienst und Mindestversorgung

## Einsatz

Für Orte, Haushalte oder Unternehmen ohne ausreichende Grundversorgung.

## Norm- und Quellenanker

TKG Universaldienst-/Mindestversorgungsregeln live prüfen; EECC; BNetzA-Verfahren.

## Arbeitsfragen

1. Welche Mindestleistung wird nicht erreicht?
2. Welche Anbieter/Technologien sind verfügbar?
3. Welche BNetzA-Schritte wurden eingeleitet?
4. Ist Übergangslösung möglich?

## Output

Unterversorgungsdossier, BNetzA-Antrag/Beschwerde und Technologievergleich.

## Red Flags

- Breitbandwunsch mit Mindestversorgung verwechselt
- Messung fehlt
- Satellit/Mobilfunk nicht geprüft
- kommunaler Ausbau parallel

## Anschluss-Skills

- tk-beweisplan-messung-stoerung-protokoll
- tk-bundesnetzagentur-verfahren-akteneinsicht-fristen

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-verwaltungsrecht-anfechtung-bnetza`

**Fokus:** Anfechtung, Verpflichtung oder Eilrechtsschutz gegen BNetzA-Beschlüsse und Nebenbestimmungen.

# Anfechtung von BNetzA-Beschlüssen

## Einsatz

Für Unternehmen, die BNetzA-Entscheidungen angreifen oder verteidigen.

## Norm- und Quellenanker

VwGO; TKG; VwVfG; Rechtsbehelfsbelehrung live prüfen.

## Arbeitsfragen

1. Welche Klageart?
2. Welche Frist?
3. Welche aufschiebende Wirkung/Eilstrategie?

## Output

Klage-/Eilantragsgerüst und Fristenplan.

## Red Flags

- falsche Frist
- aufschiebende Wirkung unterstellt
- Tenor nicht vollständig gelesen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
