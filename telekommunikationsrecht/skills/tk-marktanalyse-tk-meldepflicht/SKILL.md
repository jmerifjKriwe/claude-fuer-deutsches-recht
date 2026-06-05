---
name: tk-marktanalyse-tk-meldepflicht
description: "TK Marktanalyse TK Meldepflicht im Telekommunikationsrecht: prüft konkret Marktanalyse, Marktdefinition, SMP/beträchtliche Marktmacht, Konsultation. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Marktanalyse TK Meldepflicht

## Arbeitsbereich

Dieser Skill behandelt **TK Marktanalyse TK Meldepflicht** als zusammenhängenden Arbeitsgang im Telekommunikationsrecht. Im Mittelpunkt steht die Prüfung von Marktanalyse, Marktdefinition, SMP/beträchtliche Marktmacht. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-marktanalyse-betraechtliche-marktmacht` | Marktanalyse, Marktdefinition, SMP/beträchtliche Marktmacht, Konsultation, EU-Abstimmung und Regulierungsverfügung. |
| `tk-meldepflicht-it-sicherheitsvorfall` | Sicherheitsvorfälle bei TK-Anbietern: BNetzA/BSI/DSGVO-Meldungen, Kundenkommunikation, Ursachenanalyse und Abhilfe. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-marktanalyse-betraechtliche-marktmacht`

**Fokus:** Marktanalyse, Marktdefinition, SMP/beträchtliche Marktmacht, Konsultation, EU-Abstimmung und Regulierungsverfügung.

# Marktanalyse und beträchtliche Marktmacht

## Einsatz

Für regulierte Märkte, in denen Zugang/Entgelt nur nach Marktmachtanalyse angeordnet werden kann.

## Norm- und Quellenanker

TKG Marktregulierung; EECC; BNetzA/BEREC/EU-Kommission live prüfen.

## Arbeitsfragen

1. Welcher relevante Markt ist betroffen?
2. Welche Marktanteile, Kontrolle über Infrastruktur und Wettbewerbsparameter liegen vor?
3. Welche Konsultation/Notifizierung läuft?

## Output

Marktanalyse-Memo und Stellungnahme.

## Red Flags

- Marktabgrenzung zu grob
- alte Regulierungsverfügung verwendet
- EU-Konsultation übersehen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-meldepflicht-it-sicherheitsvorfall`

**Fokus:** Sicherheitsvorfälle bei TK-Anbietern: BNetzA/BSI/DSGVO-Meldungen, Kundenkommunikation, Ursachenanalyse und Abhilfe.

# IT-Sicherheitsvorfall und Meldepflicht

## Einsatz

Für Incident Response im TK-Betrieb.

## Norm- und Quellenanker

TKG Sicherheitsvorschriften; BSI-Gesetz/NIS2; DSGVO Art. 33, 34.

## Arbeitsfragen

1. Was ist passiert und welche Dienste betroffen?
2. Welche Meldewege und Fristen?
3. Welche Sofortmaßnahmen?

## Output

Incident-Meldeplan und Vorstandsvorlage.

## Red Flags

- Meldung nur intern
- DSGVO und TKG nicht koordiniert
- Kundenkommunikation zu spät

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
