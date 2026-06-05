---
name: tk-zivilklage-tk-abhoerschnittstellen
description: "TK Zivilklage TK Abhoerschnittstellen im Telekommunikationsrecht: prüft konkret Zivilrechtliche TK-Klagen, TK-Überwachung, Schnittstellen, Auskunftsersuchen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Zivilklage TK Abhoerschnittstellen

## Arbeitsbereich

**TK Zivilklage TK Abhoerschnittstellen** ordnet den Fall über die tragenden Prüffelder: Zivilrechtliche TK-Klagen, TK-Überwachung, Schnittstellen. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-zivilklage-lg-entgelt-schadensersatz` | Zivilrechtliche TK-Klagen: Entgeltforderungen, Rückzahlung, Schadensersatz, SLA, AGB, Minderung und Verbraucher-/Businessstreit. |
| `tk-abhoerschnittstellen-sicherheitsbehoerden` | TK-Überwachung, Schnittstellen, Auskunftsersuchen, Bestandsdaten, Verkehrsdaten, Strafverfolgung und Geheimnisschutz. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-zivilklage-lg-entgelt-schadensersatz`

**Fokus:** Zivilrechtliche TK-Klagen: Entgeltforderungen, Rückzahlung, Schadensersatz, SLA, AGB, Minderung und Verbraucher-/Businessstreit.

# Zivilklage: Entgelt, Schaden, Vertrag

## Einsatz

Für Vertragsstreit ohne unmittelbaren BNetzA-Bescheid.

## Norm- und Quellenanker

BGB; ZPO; TKG Kundenschutz; AGB-Recht.

## Arbeitsfragen

1. Welche Anspruchsgrundlage?
2. Welche Rechnung/Leistung ist streitig?
3. Welche Beweise?

## Output

Klage-/Klageerwiderungsgerüst und Streitwert.

## Red Flags

- Regulierungsfrage als Vorfrage ungeklärt
- Rechnungsdaten fehlen
- AGB nicht einbezogen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-abhoerschnittstellen-sicherheitsbehoerden`

**Fokus:** TK-Überwachung, Schnittstellen, Auskunftsersuchen, Bestandsdaten, Verkehrsdaten, Strafverfolgung und Geheimnisschutz.

# Überwachungsschnittstellen und Behördenauskünfte

## Einsatz

Für Provider, die rechtmäßig kooperieren müssen, aber keine Daten zu viel herausgeben dürfen.

## Norm- und Quellenanker

TKG; TKÜV; StPO; Polizeirecht; Datenschutzrecht.

## Arbeitsfragen

1. Welche Behörde und welcher Rechtsgrund?
2. Welche Datenkategorie?
3. Welche Form-/Anordnungsvoraussetzung?

## Output

Behördenanfrage-Check und Herausgabeprotokoll.

## Red Flags

- informelle Anfrage
- falsche Datenkategorie
- keine Dokumentation

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
