---
name: tk-mindestvertragslaufzeit-tk-umzug
description: "TK Mindestvertragslaufzeit TK Umzug im Telekommunikationsrecht: prüft konkret TK-Verträge, Umzug bei TK-Vertrag. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# TK Mindestvertragslaufzeit TK Umzug

## Arbeitsbereich

**TK Mindestvertragslaufzeit TK Umzug** ordnet den Fall über die tragenden Prüffelder: TK-Verträge, Umzug bei TK-Vertrag. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-mindestvertragslaufzeit-kuendigung` | TK-Verträge: Mindestlaufzeit, automatische Verlängerung, monatliche Kündbarkeit, Kündigungsbutton/Onlinekündigung, AGB und Nachweis. |
| `tk-umzug-vertragsanpassung` | Umzug bei TK-Vertrag: Fortführung, Sonderkündigung, Leistungsfähigkeit am neuen Standort, Glasfaser-/Kabelanschluss und Kosten. |

## Arbeitsweg

- Rolle und Ziel im Telekommunikationsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: DSGVO Art. 5, 6, 7, 9, 12-22, 25, 28, 30, 32, 33-34, 35, 51-58, 77-83, BDSG §§ 22-25, 26, 30; GWB §§ 1, 2, 18, 19, 20, 33, 35, 36, AEUV Art. 101, 102, FKVO 139/2004; BNetzAG, EnWG §§ 21 ff., TKG, PostG, MessEG, BSI-KritisV, DigiNetzG; TKG (i.d.F. 2021), TKMV, EU-Kodex 2018/1972, DigiNetzG, NIS2-RL, eIDAS — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `tk-mindestvertragslaufzeit-kuendigung`

**Fokus:** TK-Verträge: Mindestlaufzeit, automatische Verlängerung, monatliche Kündbarkeit, Kündigungsbutton/Onlinekündigung, AGB und Nachweis.

# Mindestlaufzeit, Verlängerung, Kündigung

## Einsatz

Der Skill prüft, ob Kunden aus einem Vertrag herauskommen oder Anbieter ihre Laufzeitklauseln sauber gestalten.

## Norm- und Quellenanker

TKG Kundenschutz; BGB §§ 309, 312k, 314; TDDDG bei Onlineabschluss; AGB-Recht.

## Arbeitsfragen

1. Welche Laufzeit wurde wann vereinbart?
2. Welche Verlängerungsmechanik gilt nach aktueller Rechtslage?
3. Wie wurde gekündigt und wie bestätigt?
4. Ist eine außerordentliche Kündigung möglich?

## Output

Kündigungsprüfung, Anbieterbrief, AGB-Redline und Fristenkalender.

## Red Flags

- alte Laufzeitlogik verwendet
- Kündigung im Portal nicht beweisbar
- Businessvertrag mit Verbraucherrecht verwechselt
- Sonderkündigungsgrund nicht dokumentiert

## Anschluss-Skills

- tk-umzug-vertragsanpassung
- tk-output-beschwerde-antrag-klage

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-umzug-vertragsanpassung`

**Fokus:** Umzug bei TK-Vertrag: Fortführung, Sonderkündigung, Leistungsfähigkeit am neuen Standort, Glasfaser-/Kabelanschluss und Kosten.

# Umzug und Telekommunikationsvertrag

## Einsatz

Für Streit, wenn Anbieter am neuen Wohn-/Geschäftsort nicht gleichwertig liefern kann.

## Norm- und Quellenanker

TKG Kundenschutzvorschriften zum Umzug live prüfen; BGB Dauerschuldverhältnis; AGB-Recht.

## Arbeitsfragen

1. Welche Leistung ist am neuen Standort technisch möglich?
2. Wurde Umzug rechtzeitig angezeigt?
3. Welche Laufzeit/Kündigungsfrist gilt?
4. Welche Umzugsgebühren sind vereinbart?

## Output

Umzugsprüfung, Kündigungs-/Fortführungsschreiben und Kostencheck.

## Red Flags

- Anbieter liefert anderes Produkt
- Laufzeit wird neu gestartet
- Umzug ins Ausland
- Hausanschluss fehlt

## Anschluss-Skills

- tk-mindestvertragslaufzeit-kuendigung
- tk-glasfaser-hausanschluss-wegerecht

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
