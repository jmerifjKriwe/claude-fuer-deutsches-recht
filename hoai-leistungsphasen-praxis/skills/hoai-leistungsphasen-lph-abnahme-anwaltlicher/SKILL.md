---
name: hoai-leistungsphasen-lph-abnahme-anwaltlicher
description: "Nutze dies, wenn Hoai Leistungsphasen Router, Hoai Lph 01 Abnahme Und Teilabnahme, Hoai Lph 01 Anwaltlicher Pruefvermerk, Hoai Lph 01 Bauherrnfreigabe, Hoai Lph 01 Bim Und Datenraum im Plugin Hoai Leistungsphasen Praxis konkret bearbeitet werden soll. Auslöser: Bitte Hoai Leistungsphasen Router, Hoai Lph 01 Abnahme Und Teilabnahme, Hoai Lph 01 Anwaltlicher Pruefvermerk, Hoai Lph 01 Bauherrnfreigabe, Hoai Lph 01 Bim Und Datenraum prüfen.; Erstelle eine Arbeitsfassung zu Hoai Leistungsphasen Router, Hoai Lph 01 Abnahme Und Teilabnahme, Hoai Lph 01 Anwaltlicher Pruefvermerk, Hoai Lph 01 Bauherrnfreigabe, Hoai Lph 01 Bim Und Datenraum.; Welche Normen und Nachweise brauche ich?."
---

# Hoai Leistungsphasen Router, Hoai Lph 01 Abnahme Und Teilabnahme, Hoai Lph 01 Anwaltlicher Pruefvermerk, Hoai Lph 01 Bauherrnfreigabe, Hoai Lph 01 Bim Und Datenraum

## Zweck

Dieser Skill ist ein eigenständiger Arbeitsbereich. Er verbindet mehrere sachlich benachbarte Arbeitsmodule. Wähle anhand des Sachverhalts das passende Modul, arbeite dessen Prüfroutine vollständig ab und kombiniere Module nur, wenn der Fall tatsächlich mehrere Themen berührt.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `hoai-leistungsphasen-router` | HOAI-Praxis: ordnet chaotische Unterlagen einer oder mehreren HOAI-Leistungsphasen zu; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-lph-01-abnahme-und-teilabnahme` | HOAI LPH 1 Grundlagenermittlung: ordnet Abnahme, Teilabnahme, Zustandsfeststellung und § 650s BGB; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %. |
| `hoai-lph-01-anwaltlicher-pruefvermerk` | HOAI LPH 1 Grundlagenermittlung: erstellt anwaltliches Kurzmemorandum zum LPH-Stand; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %. |
| `hoai-lph-01-bauherrnfreigabe` | HOAI LPH 1 Grundlagenermittlung: strukturiert Freigabeentscheidung, Protokoll, Vorbehalte und Änderungswünsche; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %. |
| `hoai-lph-01-bim-und-datenraum` | HOAI LPH 1 Grundlagenermittlung: ordnet digitale Modelle, CDE, Planversionen und Zugriffsnachweise; mit Fokus auf Aufgabenstellung klären, Ortsbesichtigung, Untersuchungsbedarf, Beteiligte auswählen, Ergebnisse dokumentieren und Bewertungsanteil 2 %. |

## Arbeitsweg

Für **Hoai Leistungsphasen Router, Hoai Lph 01 Abnahme Und Teilabnahme, Hoai Lph 01 Anwaltlicher Pruefvermerk, Hoai Lph 01 Bauherrnfreigabe, Hoai Lph 01 Bim Und Datenraum** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `hoai-leistungsphasen-praxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `hoai-leistungsphasen-router`

**Fokus:** HOAI-Praxis: ordnet chaotische Unterlagen einer oder mehreren HOAI-Leistungsphasen zu; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Ordnet chaotische unterlagen einer oder mehreren hoai-leistungsphasen zu

## Einsatz

Dieser Querschnitts-Skill bearbeitet **ordnet chaotische Unterlagen einer oder mehreren HOAI-Leistungsphasen zu** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Spezialskills vertieft werden.

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
