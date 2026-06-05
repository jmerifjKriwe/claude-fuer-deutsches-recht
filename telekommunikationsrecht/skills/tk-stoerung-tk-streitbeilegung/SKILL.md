---
name: tk-stoerung-tk-streitbeilegung
description: "TK Stoerung TK Streitbeilegung im Telekommunikationsrecht: prüft konkret Internet-/Telefonstörung, Streitbeilegung bei Zugang, Mitnutzung, Entgelt. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Stoerung TK Streitbeilegung

## Arbeitsbereich

**TK Stoerung TK Streitbeilegung** ordnet den Fall über die tragenden Prüffelder: Internet-/Telefonstörung, Streitbeilegung bei Zugang, Mitnutzung. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-stoerung-minderung-ausfallentschaedigung` | Internet-/Telefonstörung: Minderung, Ausfallentschädigung, Entstörungspflichten, Messprotokolle, SLA und Schadensersatz. |
| `tk-streitbeilegung-bnetza` | Streitbeilegung bei Zugang, Mitnutzung, Entgelt, Nummerierung oder Anbieterwechsel mit BNetzA-Beteiligung. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-stoerung-minderung-ausfallentschaedigung`

**Fokus:** Internet-/Telefonstörung: Minderung, Ausfallentschädigung, Entstörungspflichten, Messprotokolle, SLA und Schadensersatz.

# Störung, Minderung und Ausfallentschädigung

## Einsatz

Der Skill bearbeitet juristische Rechte mit ordentlicher technischer Dokumentation.

## Norm- und Quellenanker

TKG Kundenschutz, insbesondere Minderungs-/Entschädigungsregeln live prüfen; BGB §§ 280, 536 analog nur vorsichtig; ZPO.

## Arbeitsfragen

1. Welche vertraglich vereinbarte Leistung fehlt?
2. Wie wurde die Störung gemeldet und dokumentiert?
3. Ist eine BNetzA-konforme Messkampagne nötig?
4. Welche Ausfallentschädigung/Minderung/Schäden sind realistisch?

## Output

Minderungsberechnung, Providerbrief, Schlichtungs-/Klagebasis und Beweisplan.

## Red Flags

- Messung über WLAN
- Störung nicht gemeldet
- Business-SLA ignoriert
- Schadenshöhe nicht kausal belegt

## Anschluss-Skills

- tk-beweisplan-messung-stoerung-protokoll
- tk-schlichtung-verbraucher

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-streitbeilegung-bnetza`

**Fokus:** Streitbeilegung bei Zugang, Mitnutzung, Entgelt, Nummerierung oder Anbieterwechsel mit BNetzA-Beteiligung.

# BNetzA-Streitbeilegung zwischen Unternehmen

## Einsatz

Für schnelle regulatorische Konfliktlösung statt langer Zivilstreitigkeit.

## Norm- und Quellenanker

TKG Streitbeilegungsnormen live prüfen; VwVfG/VwGO.

## Arbeitsfragen

1. Welche Norm eröffnet Streitbeilegung?
2. Welche Vorverhandlungen sind dokumentiert?
3. Welche Entscheidung soll die BNetzA treffen?

## Output

Streitbeilegungsantrag mit Sachverhalt, Antrag und Anlagen.

## Red Flags

- Antrag zu unbestimmt
- keine Verhandlungshistorie
- Zuständigkeit nicht begründet

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
