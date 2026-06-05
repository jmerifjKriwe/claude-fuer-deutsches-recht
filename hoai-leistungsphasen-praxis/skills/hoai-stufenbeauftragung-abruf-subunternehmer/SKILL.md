---
name: hoai-stufenbeauftragung-abruf-subunternehmer
description: "Stufenbeauftragung Abruf Subunternehmer im HOAI-Leistungsphasen: prüft konkret HOAI-Fachfrage, HOAI-Praxis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Stufenbeauftragung Abruf Subunternehmer

## Arbeitsbereich

**Stufenbeauftragung Abruf Subunternehmer** ordnet den Fall über die tragenden Prüffelder: HOAI-Fachfrage, HOAI-Praxis. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hoai-stufenbeauftragung-abruf-nichtabruf` | HOAI-Fachfrage: Stufenbeauftragung, Optionsabruf, Nichtabruf weiterer Leistungsphasen, Kündigung, Vergütung, Vorleistung und Akquisitionsrisiko im Architektenvertrag prüfen. |
| `hoai-subunternehmer-perspektive` | HOAI-Praxis: prüft, welche Planinformationen Subunternehmer wirklich brauchen; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-teilabnahme-bgb-650s` | HOAI-Praxis: prüft Teilabnahme ab letzter Unternehmerleistung und Haftungsfolgen; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren. |
| `hoai-umbau-modernisierung-zuschlag-bestand` | HOAI-Fachfrage: Umbau, Modernisierung, Instandsetzung, Instandhaltung, Umbauzuschlag, Bestandsschwierigkeit und Abgrenzung zu Neubau/Erweiterung im Honorar- und Leistungsumfang prüfen. |
| `hoai-verbraucherhinweis-honorarvereinbarung` | HOAI-Fachfrage: Honorarvereinbarung mit Verbrauchern nach § 7 HOAI, Textform, Hinweis auf höhere/niedrigere Honorare, Orientierungswerte und Folgen fehlender oder missverständlicher Aufklärung prüfen. |

## Arbeitsweg

- Rolle und Ziel im Hoai Leistungsphasen Praxis klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HOAI §§ 1-13, 14-37 (Objektplanung), 38-52 (Flachbau, Ingenieurbauwerke), BGB §§ 631 ff., VOB/B — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `hoai-stufenbeauftragung-abruf-nichtabruf`

**Fokus:** HOAI-Fachfrage: Stufenbeauftragung, Optionsabruf, Nichtabruf weiterer Leistungsphasen, Kündigung, Vergütung, Vorleistung und Akquisitionsrisiko im Architektenvertrag prüfen.

# Stufenbeauftragung, Abruf Und Nichtabruf

## Einsatz

Dieses Fachmodul bei Verträgen, in denen LPH 1-2, 1-4 oder 1-5 fest beauftragt sind und weitere LPH nur optional abgerufen werden.

## Prüffragen

1. Welche Stufe ist verbindlich beauftragt?
2. Ist der spätere Abruf echte Option, Rahmenvertrag oder faktisch schon zugesagt?
3. Hat der Planer Leistungen der nächsten Stufe vor Abruf erbracht?
4. Gab es Freigaben, Protokolle, Abschläge oder Projektkommunikation, die einen Abruf belegen?
5. Ist Nichtabruf, Kündigung oder freier Wechsel des Planers das richtige Rechtsproblem?

## Normanker

- §§ 631, 648, 650p bis 650r BGB.
- HOAI nur für Honorarorientierung und Leistungsabgrenzung, nicht als automatischer Abruf.

## Output

Eine Stufenmatrix: Stufe, Status, Leistungsnachweis, Vergütungsgrund, Kündigungs-/Nichtabrufrisiko, nächster Brief.

## 2. `hoai-subunternehmer-perspektive`

**Fokus:** HOAI-Praxis: prüft, welche Planinformationen Subunternehmer wirklich brauchen; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Prüft

## Einsatz

Dieser Querschnitts-Skill bearbeitet **prüft, welche Planinformationen Subunternehmer wirklich brauchen** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

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

## 3. `hoai-teilabnahme-bgb-650s`

**Fokus:** HOAI-Praxis: prüft Teilabnahme ab letzter Unternehmerleistung und Haftungsfolgen; für Architekten, Ingenieure, Bauleiter, Bauunternehmen, Anwälte, Sachverständige und Bauherren.

# HOAI Querschnitt: Prüft teilabnahme ab letzter unternehmerleistung und haftungsfolgen

## Einsatz

Dieser Querschnitts-Skill bearbeitet **prüft Teilabnahme ab letzter Unternehmerleistung und Haftungsfolgen** über alle Leistungsphasen hinweg. Er hält die Projektlogik zusammen, bevor einzelne LPH-Fachmodule vertieft werden.

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

## 4. `hoai-umbau-modernisierung-zuschlag-bestand`

**Fokus:** HOAI-Fachfrage: Umbau, Modernisierung, Instandsetzung, Instandhaltung, Umbauzuschlag, Bestandsschwierigkeit und Abgrenzung zu Neubau/Erweiterung im Honorar- und Leistungsumfang prüfen.

# Umbau, Modernisierung Und Bestandsschwierigkeit

## Einsatz

Dieses Fachmodul greift, wenn im Bestand geplant wird und unklar ist, ob Neubau-, Umbau-, Modernisierungs-, Instandsetzungs- oder Instandhaltungslogik gilt. Gerade hier entstehen Honorar- und Haftungsfehler.

## Normanker

- § 2 HOAI Begriffe.
- § 4 HOAI anrechenbare Kosten.
- § 6 HOAI Grundlagen des Honorars.
- §§ 34, 35 HOAI und Anlage 10 für Gebäude/Innenräume.

## Prüfroutine

1. Maßnahme technisch beschreiben: Eingriffstiefe, Bestand, Erweiterung, Nutzungsänderung.
2. Leistungsbild wählen und Bestand separat erfassen.
3. Prüfen, ob Umbau-/Modernisierungszuschlag vereinbart oder plausibel zu verhandeln ist.
4. Besondere Leistungen abgrenzen: Bestandsaufnahme, Schadstoff, Brandschutz, Denkmalschutz, Nutzerumzug.
5. Haftungsfalle markieren: unbekannter Bestand ist kein Freibrief, aber auch kein automatisch übernommenes Risiko.

## Output

Eine Bestand-Honorar-Notiz mit Maßnahmenkategorie, Belegen, Honorarfolge, Zusatzleistungsbedarf und Warntext an Bauherr/Planer.

## 5. `hoai-verbraucherhinweis-honorarvereinbarung`

**Fokus:** HOAI-Fachfrage: Honorarvereinbarung mit Verbrauchern nach § 7 HOAI, Textform, Hinweis auf höhere/niedrigere Honorare, Orientierungswerte und Folgen fehlender oder missverständlicher Aufklärung prüfen.

# Verbraucherhinweis Und Honorarvereinbarung

## Einsatz

Dieses Fachmodul bei privaten Bauherren, Einfamilienhaus, Sanierung, Innenausbau oder kleinen WEG-/Vereinsprojekten, wenn die Honorarvereinbarung unklar ist.

## Normanker

- § 7 HOAI: Honorarvereinbarung in Textform; Hinweis gegenüber Verbrauchern, dass auch höhere oder niedrigere Honorare als die Orientierungswerte vereinbart werden können.
- §§ 650p bis 650r BGB bei Architekten-/Ingenieurvertrag.

## Prüfung

1. Verbraucherstatus prüfen.
2. Textform der Honorarvereinbarung sichern.
3. Verbraucherhinweis suchen: Zeitpunkt, Inhalt, Nachweis.
4. Leistungsumfang und Honorar trennen: Pauschale, Stundensatz, HOAI-Tafel, besondere Leistungen.
5. Missverständnisse aktiv erklären: HOAI ist seit 2021 Orientierung, nicht automatisch zwingender Mindestpreis.

## Output

Ein Honorarprüfblatt mit Wirksamkeitsampel, Aufklärungsdefizit, Nachweisproblem und verständlichem Mandantenbrief.
