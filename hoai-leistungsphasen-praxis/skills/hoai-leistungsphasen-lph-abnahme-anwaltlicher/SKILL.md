---
name: hoai-leistungsphasen-lph-abnahme-anwaltlicher
description: "LPH Abnahme Anwaltlicher im HOAI-Leistungsphasen: prüft konkret HOAI-Praxis, HOAI LPH 1 Grundlagenermittlung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# LPH Abnahme Anwaltlicher

## Arbeitsbereich

Dieser Skill behandelt **LPH Abnahme Anwaltlicher** als zusammenhängenden Arbeitsgang im HOAI-Leistungsphasen. Im Mittelpunkt steht die Prüfung von HOAI-Praxis, HOAI LPH 1 Grundlagenermittlung und weiteren verwandten Aspekten. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hoai-leistungsphasen-router` | HOAI-Praxis: ordnet chaotische Unterlagen einer oder mehreren HOAI-Leistungsphasen zu; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-lph-01-abnahme-und-teilabnahme` | HOAI LPH 1 Grundlagenermittlung: ordnet Abnahme, Teilabnahme, Zustandsfeststellung und § 650s BGB; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %. |
| `hoai-lph-01-anwaltlicher-pruefvermerk` | HOAI LPH 1 Grundlagenermittlung: erstellt anwaltliches Kurzmemorandum zum LPH-Stand; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %. |
| `hoai-lph-01-bauherrnfreigabe` | HOAI LPH 1 Grundlagenermittlung: strukturiert Freigabeentscheidung, Protokoll, Vorbehalte und Änderungswünsche; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %. |
| `hoai-lph-01-bim-und-datenraum` | HOAI LPH 1 Grundlagenermittlung: ordnet digitale Modelle, CDE, Planversionen und Zugriffsnachweise; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %. |

## Arbeitsweg

- Rolle und Ziel im Hoai Leistungsphasen Praxis klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HOAI §§ 1-13, 14-37 (Objektplanung), 38-52 (Flachbau, Ingenieurbauwerke), BGB §§ 631 ff., VOB/B — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `hoai-leistungsphasen-router`

**Fokus:** HOAI-Praxis: ordnet chaotische Unterlagen einer oder mehreren HOAI-Leistungsphasen zu; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Ordnet chaotische unterlagen einer oder mehreren hoai-leistungsphasen zu

## Einsatz

Dieser Querschnitts-Skill bearbeitet **ordnet chaotische Unterlagen einer oder mehreren HOAI-Leistungsphasen zu** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

## Arbeitsweise

1. Klär Rolle, Projektart, Leistungsbild, beauftragte LPH, Vertrag, Honorarvereinbarung und aktuellen Konflikt.
2. Ordne die Unterlagen nach LPH, Planstand, Freigabe, Kostenstand, Terminstand und Beweiswert.
3. Trenne HOAI-Grundleistung, besondere Leistung, Bauvertragsrecht, Vergabe, öffentliches Recht und Haftung.
4. Erzeuge ein knappes, anschlussfähiges Arbeitsprodukt für Bauherr, Planer, Bauunternehmen, Anwalt oder Sachverständigen.

## Fachfragen-Routing

Wenn der Fall nicht nur nach einer Leistungsphase, sondern nach einem typischen Streitpunkt fragt, route zusätzlich in den passenden Querschnittsskill:

- Honorargrundlage: `hoai-anrechenbare-kosten-din276-baukostengruppen`, `hoai-mitzuverarbeitende-bausubstanz-bestand`, `hoai-honorarzone-bewertungspunkte-objektliste`.
- Vertrag und Kosten: `hoai-kostenobergrenze-budget-haftung`, `hoai-stufenbeauftragung-abruf-nichtabruf`, `hoai-zielfindungsphase-bgb-650p-650r`, `hoai-verbraucherhinweis-honorarvereinbarung`.
- Änderungen: `hoai-wiederholungsleistungen-planungsaenderung`, `hoai-umbau-modernisierung-zuschlag-bestand`.
- Planungstiefe und Vergabe: `hoai-lph2-variantenuntersuchung-wirtschaftlichkeit`, `hoai-lph5-ausfuehrungsplanung-detailtiefe`, `hoai-lph6-lv-mengen-massen-vergabereife`, `hoai-lph7-bieterspiegel-aufklaerung-vergaberisiko`.
- Bauausführung und Streit: `hoai-lph8-ueberwachungstiefe-stichproben`, `hoai-lph8-rechnungspruefung-nachtraege-vob`, `hoai-lph8-maengel-abnahme-restleistungen`, `hoai-prueffaehige-schlussrechnung-einwendungen`.

## Ergebnis

- LPH-/Vertragsmatrix
- Risikoregister
- konkreter Text- oder Tabellenbaustein
- nächste Prüfschritte

## Quellen- und Qualitätsregeln

- HOAI-Text, insbesondere § 34 und Anlage 10, live gegen Gesetze im Internet prüfen.
- BGB §§ 650p bis 650t bei Architekten-/Ingenieurverträgen berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink; keine Blindzitate.

## 2. `hoai-lph-01-abnahme-und-teilabnahme`

**Fokus:** HOAI LPH 1 Grundlagenermittlung: ordnet Abnahme, Teilabnahme, Zustandsfeststellung und § 650s BGB; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %.

# LPH 1 Grundlagenermittlung: Ordnet abnahme

## Einsatz

Dieser Skill ist nur für **Leistungsphase 1 (Grundlagenermittlung)** gedacht. Er prüft ordnet Abnahme, Teilabnahme, Zustandsfeststellung und § 650s BGB im Kontext dieser Phase: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren. Bewertungsanker für Gebäude/Innenräume: 2 %.

## Arbeitsweise

1. Nimm zuerst nur den LPH-1-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-1-Zweck: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-1-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 1

- Phase: Grundlagenermittlung
- Praktischer Kern: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren
- Bewertungsanker Gebäude/Innenräume: 2 %
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 3. `hoai-lph-01-anwaltlicher-pruefvermerk`

**Fokus:** HOAI LPH 1 Grundlagenermittlung: erstellt anwaltliches Kurzmemorandum zum LPH-Stand; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %.

# LPH 1 Grundlagenermittlung: Erstellt anwaltliches kurzmemorandum zum lph-stand

## Einsatz

Dieser Skill ist nur für **Leistungsphase 1 (Grundlagenermittlung)** gedacht. Er prüft erstellt anwaltliches Kurzmemorandum zum LPH-Stand im Kontext dieser Phase: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren. Bewertungsanker für Gebäude/Innenräume: 2 %.

## Arbeitsweise

1. Nimm zuerst nur den LPH-1-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-1-Zweck: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-1-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 1

- Phase: Grundlagenermittlung
- Praktischer Kern: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren
- Bewertungsanker Gebäude/Innenräume: 2 %
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 4. `hoai-lph-01-bauherrnfreigabe`

**Fokus:** HOAI LPH 1 Grundlagenermittlung: strukturiert Freigabeentscheidung, Protokoll, Vorbehalte und Änderungswünsche; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %.

# LPH 1 Grundlagenermittlung: Strukturiert freigabeentscheidung

## Einsatz

Dieser Skill ist nur für **Leistungsphase 1 (Grundlagenermittlung)** gedacht. Er prüft strukturiert Freigabeentscheidung, Protokoll, Vorbehalte und Änderungswünsche im Kontext dieser Phase: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren. Bewertungsanker für Gebäude/Innenräume: 2 %.

## Arbeitsweise

1. Nimm zuerst nur den LPH-1-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-1-Zweck: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-1-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 1

- Phase: Grundlagenermittlung
- Praktischer Kern: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren
- Bewertungsanker Gebäude/Innenräume: 2 %
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.

## 5. `hoai-lph-01-bim-und-datenraum`

**Fokus:** HOAI LPH 1 Grundlagenermittlung: ordnet digitale Modelle, CDE, Planversionen und Zugriffsnachweise; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %.

# LPH 1 Grundlagenermittlung: Ordnet digitale modelle

## Einsatz

Dieser Skill ist nur für **Leistungsphase 1 (Grundlagenermittlung)** gedacht. Er prüft ordnet digitale Modelle, CDE, Planversionen und Zugriffsnachweise im Kontext dieser Phase: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren. Bewertungsanker für Gebäude/Innenräume: 2 %.

## Arbeitsweise

1. Nimm zuerst nur den LPH-1-Stand auf: vorhandene Pläne, Protokolle, Kosten, Freigaben, offene Entscheidungen und Beteiligte.
2. Vergleiche die Unterlagen mit dem typischen LPH-1-Zweck: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren.
3. Markiere, was Grundleistung, Besondere Leistung, Änderungswunsch, Mitwirkung des Auftraggebers oder Schnittstellenproblem ist.
4. Erzeuge ein Ergebnis, das die nächste Projektentscheidung vorbereitet und zugleich beweisbar dokumentiert.

## Ergebnis

- LPH-1-Prüfmatrix
- fehlende Unterlagen und offene Entscheidungen
- Honorar-/Nachtragsnotiz
- kurzer Textbaustein für Bauherr, Planer, Unternehmer oder Anwalt

## Quellen- und Qualitätsregeln

- HOAI § 34 und Anlage 10 als Primäranker verwenden; andere Leistungsbilder gesondert prüfen.
- BGB §§ 650p bis 650t und Bauvertragsrecht nur dort einbeziehen, wo der Sachverhalt sie auslöst.
- Keine Rechtsprechung aus Modellwissen zitieren; nur verifizierte Entscheidungen mit Gericht, Datum, Aktenzeichen und freiem Link.

## Besonderer Blick in LPH 1

- Phase: Grundlagenermittlung
- Praktischer Kern: Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren
- Bewertungsanker Gebäude/Innenräume: 2 %
- Warnung: Nicht automatisch auf andere HOAI-Leistungsbilder übertragen; erst Leistungsbild und Anlage live bestimmen.
