---
name: hoai-claim-timeline-dokumentenindex
description: "Claim Timeline Dokumentenindex im HOAI-Leistungsphasen: prüft konkret HOAI-Praxis, HOAI-Fachfrage. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Claim Timeline Dokumentenindex

## Arbeitsbereich

**Claim Timeline Dokumentenindex** ordnet den Fall über die tragenden Prüffelder: HOAI-Praxis, HOAI-Fachfrage. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hoai-claim-timeline` | HOAI-Praxis: baut Zeitstrahl für Pflichtverletzung, Warnung, Entscheidung, Schaden und Frist; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-dokumentenindex-hoai-akte` | HOAI-Praxis: erstellt Aktenindex nach LPH, Datum, Planstand, Version und Beweiswert; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-fachplaner-tga-brandschutz-tragwerk-koordination` | HOAI-Fachfrage: Schnittstellenkoordination zwischen Objektplanung, TGA, Tragwerk, Brandschutz, Bauphysik, Baugrund und Sonderplanern mit Planlauf, Verantwortungsmatrix und Haftungsabgrenzung prüfen. |
| `hoai-foerdermittel-baukosten` | HOAI-Praxis: prüft Fördermittel, Vergabebindungen, Nachweise und Kostenänderungen; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-foerdermittel-vergabebindung-rueckforderung` | HOAI-Fachfrage: Fördermittel, Zuwendungsbescheid, Vergabebindungen, Kostensteigerung, Mittelabruf, Dokumentationspflicht und Rückforderungsrisiko in Planung und Bauüberwachung prüfen. |

## Arbeitsweg

- Rolle und Ziel im Hoai Leistungsphasen Praxis klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HOAI §§ 1-13, 14-37 (Objektplanung), 38-52 (Flachbau, Ingenieurbauwerke), BGB §§ 631 ff., VOB/B — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `hoai-claim-timeline`

**Fokus:** HOAI-Praxis: baut Zeitstrahl für Pflichtverletzung, Warnung, Entscheidung, Schaden und Frist; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Baut zeitstrahl für pflichtverletzung

## Einsatz

Dieser Querschnitts-Skill bearbeitet **baut Zeitstrahl für Pflichtverletzung, Warnung, Entscheidung, Schaden und Frist** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

## Arbeitsweise

1. Klär Rolle, Projektart, Leistungsbild, beauftragte LPH, Vertrag, Honorarvereinbarung und aktuellen Konflikt.
2. Ordne die Unterlagen nach LPH, Planstand, Freigabe, Kostenstand, Terminstand und Beweiswert.
3. Trenne HOAI-Grundleistung, besondere Leistung, Bauvertragsrecht, Vergabe, öffentliches Recht und Haftung.
4. Erzeuge ein knappes, anschlussfähiges Arbeitsprodukt für Bauherr, Planer, Bauunternehmen, Anwalt oder Sachverständigen.

## Ergebnis

- LPH-/Vertragsmatrix
- Risikoregister
- konkreter Text- oder Tabellenbaustein
- nächste Prüfschritte

## Quellen- und Qualitätsregeln

- HOAI-Text, insbesondere § 34 und Anlage 10, live gegen Gesetze im Internet prüfen.
- BGB §§ 650p bis 650t bei Architekten-/Ingenieurverträgen berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink; keine Blindzitate.

## 2. `hoai-dokumentenindex-hoai-akte`

**Fokus:** HOAI-Praxis: erstellt Aktenindex nach LPH, Datum, Planstand, Version und Beweiswert; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Erstellt aktenindex nach lph

## Einsatz

Dieser Querschnitts-Skill bearbeitet **erstellt Aktenindex nach LPH, Datum, Planstand, Version und Beweiswert** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

## Arbeitsweise

1. Klär Rolle, Projektart, Leistungsbild, beauftragte LPH, Vertrag, Honorarvereinbarung und aktuellen Konflikt.
2. Ordne die Unterlagen nach LPH, Planstand, Freigabe, Kostenstand, Terminstand und Beweiswert.
3. Trenne HOAI-Grundleistung, besondere Leistung, Bauvertragsrecht, Vergabe, öffentliches Recht und Haftung.
4. Erzeuge ein knappes, anschlussfähiges Arbeitsprodukt für Bauherr, Planer, Bauunternehmen, Anwalt oder Sachverständigen.

## Ergebnis

- LPH-/Vertragsmatrix
- Risikoregister
- konkreter Text- oder Tabellenbaustein
- nächste Prüfschritte

## Quellen- und Qualitätsregeln

- HOAI-Text, insbesondere § 34 und Anlage 10, live gegen Gesetze im Internet prüfen.
- BGB §§ 650p bis 650t bei Architekten-/Ingenieurverträgen berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink; keine Blindzitate.

## 3. `hoai-fachplaner-tga-brandschutz-tragwerk-koordination`

**Fokus:** HOAI-Fachfrage: Schnittstellenkoordination zwischen Objektplanung, TGA, Tragwerk, Brandschutz, Bauphysik, Baugrund und Sonderplanern mit Planlauf, Verantwortungsmatrix und Haftungsabgrenzung prüfen.

# Fachplanerkoordination TGA, Brandschutz Und Tragwerk

## Einsatz

Dieses Fachmodul greift, wenn Pläne nicht zusammenpassen: Lüftung kollidiert mit Träger, Brandschutz verlangt andere Türen, TGA-Schächte fehlen oder Baugrundannahmen kippen.

## Normanker

- Anlage 10 HOAI Gebäude/Innenräume.
- Je nach Fachplanung §§/Anlagen der HOAI live prüfen.
- § 650p BGB für Koordinationsziel.

## Arbeitsgang

1. Planmatrix nach Disziplin, Index, Datum, Freigabe erstellen.
2. Koordinationspflicht Objektplaner/Fachplaner/Bauherr trennen.
3. Offene Schnittstellen als RFI oder Planprüfpunkt formulieren.
4. Kosten-/Terminfolge und Nachtragsrisiko markieren.
5. Beweis sichern: Wer erhielt welchen Plan wann?

## Output

RACI-Matrix, Kollisionsliste, Planlauf-Entscheidung und Textbaustein für Fachplaner-Runde.

## 4. `hoai-foerdermittel-baukosten`

**Fokus:** HOAI-Praxis: prüft Fördermittel, Vergabebindungen, Nachweise und Kostenänderungen; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Prüft fördermittel

## Einsatz

Dieser Querschnitts-Skill bearbeitet **prüft Fördermittel, Vergabebindungen, Nachweise und Kostenänderungen** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

## Arbeitsweise

1. Klär Rolle, Projektart, Leistungsbild, beauftragte LPH, Vertrag, Honorarvereinbarung und aktuellen Konflikt.
2. Ordne die Unterlagen nach LPH, Planstand, Freigabe, Kostenstand, Terminstand und Beweiswert.
3. Trenne HOAI-Grundleistung, besondere Leistung, Bauvertragsrecht, Vergabe, öffentliches Recht und Haftung.
4. Erzeuge ein knappes, anschlussfähiges Arbeitsprodukt für Bauherr, Planer, Bauunternehmen, Anwalt oder Sachverständigen.

## Ergebnis

- LPH-/Vertragsmatrix
- Risikoregister
- konkreter Text- oder Tabellenbaustein
- nächste Prüfschritte

## Quellen- und Qualitätsregeln

- HOAI-Text, insbesondere § 34 und Anlage 10, live gegen Gesetze im Internet prüfen.
- BGB §§ 650p bis 650t bei Architekten-/Ingenieurverträgen berücksichtigen.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und freiem Fundlink; keine Blindzitate.

## 5. `hoai-foerdermittel-vergabebindung-rueckforderung`

**Fokus:** HOAI-Fachfrage: Fördermittel, Zuwendungsbescheid, Vergabebindungen, Kostensteigerung, Mittelabruf, Dokumentationspflicht und Rückforderungsrisiko in Planung und Bauüberwachung prüfen.

# Fördermittel, Vergabebindung Und Rückforderung

## Einsatz

Dieses Fachmodul bei Kita, Schule, Kommune, Verein, WEG oder gemeinnützigem Träger, wenn Fördermittelbedingungen die Planung, Vergabe und Abrechnung steuern.

## Prüffragen

1. Welche Förderrichtlinie und welcher Bescheid gelten?
2. Gibt es Vergabebindungen, Zweckbindung, Fristen, Publizität, Mittelabruf?
3. Welche Kosten sind förderfähig und welche nur baulich sinnvoll?
4. Welche Planänderung braucht vorherige Zustimmung?
5. Droht Rückforderung wegen Dokumentations- oder Vergabefehler?

## HOAI-Schnittstelle

Fördermittelmanagement ist nicht automatisch jede Grundleistung. Prüfe, ob Beratung, Nachweisführung oder Mittelabruf als besondere Leistung gesondert vereinbart werden müssen.

## Output

Fördermittel-Risikoregister mit Auflage, Nachweis, Frist, verantwortlicher Person, Bau-/Honorarfolge und Text für Zuwendungsgeber.
