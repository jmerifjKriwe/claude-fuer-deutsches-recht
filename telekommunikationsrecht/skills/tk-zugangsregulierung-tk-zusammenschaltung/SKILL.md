---
name: tk-zugangsregulierung-tk-zusammenschaltung
description: "TK Zugangsregulierung TK Zusammenschaltung im Telekommunikationsrecht: prüft konkret Zugang zu Netzen, Vorleistungsprodukten, TAL/Bitstrom, Glasfaser. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Zugangsregulierung TK Zusammenschaltung

## Arbeitsbereich

Dieser Skill behandelt **TK Zugangsregulierung TK Zusammenschaltung** als zusammenhängenden Arbeitsgang im Telekommunikationsrecht. Im Mittelpunkt steht die Prüfung von Zugang zu Netzen, Vorleistungsprodukten, TAL/Bitstrom. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-zugangsregulierung-vorleistung` | Zugang zu Netzen, Vorleistungsprodukten, TAL/Bitstrom, Glasfaser, Nichtdiskriminierung und technische Schnittstellen. |
| `tk-zusammenschaltung-interconnection` | Zusammenschaltung, Terminierung, IP-Interconnection, Qualität, Entgelte und Streitbeilegung. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-zugangsregulierung-vorleistung`

**Fokus:** Zugang zu Netzen, Vorleistungsprodukten, TAL/Bitstrom, Glasfaser, Nichtdiskriminierung und technische Schnittstellen.

# Zugangsregulierung und Vorleistungen

## Einsatz

Für Wettbewerber, die Zugang brauchen, oder Netzbetreiber, die Zugangspflichten erfüllen müssen.

## Norm- und Quellenanker

TKG Zugangsregulierung; BNetzA-Standardangebote; GWB/AEUV.

## Arbeitsfragen

1. Welcher Zugang wird verlangt?
2. Ist Pflicht, freiwilliger Open Access oder Vertrag betroffen?
3. Welche technischen/kommerziellen Bedingungen sind streitig?

## Output

Zugangsantrag/Stellungnahme und Konditionenmatrix.

## Red Flags

- Nichtdiskriminierung nicht belegt
- technische Schnittstelle unklar
- Vertraulichkeit überdehnt

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-zusammenschaltung-interconnection`

**Fokus:** Zusammenschaltung, Terminierung, IP-Interconnection, Qualität, Entgelte und Streitbeilegung.

# Zusammenschaltung und Interconnection

## Einsatz

Für Netzbetreiber, MVNOs und Diensteanbieter bei Interconnection-Konflikten.

## Norm- und Quellenanker

TKG Zusammenschaltung; EECC; BNetzA-Streitbeilegung.

## Arbeitsfragen

1. Welche Netze/Dienste werden verbunden?
2. Welche technischen Spezifikationen und Entgelte gelten?
3. Welche Störung/Verweigerung liegt vor?

## Output

Interconnection-Matrix, Streitbeilegungsantrag und SLA-Check.

## Red Flags

- technische und rechtliche Ebene vermischt
- Terminierungsentgelt veraltet
- QoS nicht gemessen

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
