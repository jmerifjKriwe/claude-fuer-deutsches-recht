---
name: notfall-mutmassliche-off-label
description: "Notfall Mutmassliche OFF Label im Medizinrecht: prüft konkret Notfall und mutmaßliche Einwilligung, Off-Label bei seltener Erkrankung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Notfall Mutmassliche OFF Label

## Arbeitsbereich

Dieser Skill behandelt **Notfall Mutmassliche OFF Label** als zusammenhängenden Arbeitsgang im Medizinrecht. Im Mittelpunkt steht die Prüfung von Notfall und mutmaßliche Einwilligung, Off-Label bei seltener Erkrankung. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `notfall-mutmassliche-einwilligung` | Notfall und mutmaßliche Einwilligung: moderner Medizinrechts-Skill für Bewusstlosigkeit, Zeitdruck, Patientenverfügung, Stellvertreter und Dokumentation. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck. |
| `off-label-rare-disease` | Off-Label bei seltener Erkrankung: moderner Medizinrechts-Skill für Off-Label-Use, Seltenheit, Datenlage, lebensbedrohliche Erkrankung und GKV-Erstattung. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck. |

## Arbeitsweg

- Rolle und Ziel im Plugin Fachanwalt für Medizinrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; BGB §§ 630a-h, MBO-Ä, GKV-Vorgaben, SGB V, PrüfvV, HeilberufsG der Länder; SGB V §§ 27, 39, 92, 109, 137, 295, 301, RisikoStruktAusglV, SGB IV, SGB X, SGG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `notfall-mutmassliche-einwilligung`

**Fokus:** Notfall und mutmaßliche Einwilligung: moderner Medizinrechts-Skill für Bewusstlosigkeit, Zeitdruck, Patientenverfügung, Stellvertreter und Dokumentation. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck.


# Notfall und mutmaßliche Einwilligung

## Fachkern: Notfall und mutmaßliche Einwilligung
- **Spezialgegenstand:** Notfall und mutmaßliche Einwilligung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Notfall und mutmaßliche Einwilligung** im Bereich **Fachanwalt Medizinrecht**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Bewusstlosigkeit, Zeitdruck, Patientenverfügung, Stellvertreter und Dokumentation.

## Kaltstart-Fragen

- Welche Rolle liegt vor: Patient, Arzt, Klinik, Hersteller, Sponsor, KV, Kasse oder Behörde?
- Welche Maßnahme, welches Produkt, welches Datum und welcher Rechtsstand sind entscheidend?
- Gibt es Aufklärung, Einwilligung, Studien-/Registerunterlagen, Produktinformationen oder Meldebelege?
- Geht es um Prävention, Anspruch, Verteidigung, Erstattung, Behörde oder gerichtliche Durchsetzung?

## Prüf- und Arbeitslogik

- **Rechtsanker:** § 630d BGB, Betreuungsrecht, Patientenverfügung, Notfallstandard und Beweislast.
- **Tatsachenanker:** Behandlungs-/Therapiedatum, Rollen, Behandlungsdokumente, Aufklärung, Einwilligung, Freigaben, Befunde, Meldebelege, Beweiswert und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Innovative Medizin ist nicht automatisch Standard und nicht automatisch experimentell; Zeitpunkt und Datenlage sind zu trennen.
- Produkt-, Behandlungs-, Organisations- und Aufklärungsfehler nicht vermischen.
- Bei neuen EU-Regeln Übergangsfristen und nationale Durchführung gesondert prüfen.
- Gesundheitsdaten, Genomdaten und Patientengeheimnisse nur datensparsam verarbeiten.

## Output

- Mandats-/Fallvermerk mit Normenroute und Quellenstand.
- Dokumentenmatrix mit Lücken und Beweiswert.
- Risikoampel Haftung/Regulierung/Datenschutz/Erstattung.
- Nächster Schriftsatz-, Behörden- oder Mandantenkommunikationsbaustein.

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- BGB §§ 630a ff.: https://www.gesetze-im-internet.de/bgb/__630a.html
- BGB § 630h: https://www.gesetze-im-internet.de/bgb/__630h.html
- Product Liability Directive EU 2024/2853: https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32024L2853

## 2. `off-label-rare-disease`

**Fokus:** Off-Label bei seltener Erkrankung: moderner Medizinrechts-Skill für Off-Label-Use, Seltenheit, Datenlage, lebensbedrohliche Erkrankung und GKV-Erstattung. Mit Haftung, Aufklärung, Behördenweg, Beweislogik und Quellencheck.


# Off-Label bei seltener Erkrankung

## Fachkern: Off-Label bei seltener Erkrankung
- **Spezialgegenstand:** Off-Label bei seltener Erkrankung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB §§ 630a ff., SGB V, ärztliches Berufsrecht, GOÄ/EBM, MPDG/MDR, AMG, Krankenhausrecht, Vertragsarztrecht und Arzthaftungsprozess.
- **Entscheidende Weiche:** Trenne Behandlungsfehler, Aufklärung, Dokumentation, Kausalität, Beweislast, Sozialleistungsbezug, Zulassung und Haftpflichtdeckung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Off-Label bei seltener Erkrankung** im Bereich **Fachanwalt Medizinrecht**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Off-Label-Use, Seltenheit, Datenlage, lebensbedrohliche Erkrankung und GKV-Erstattung.

## Kaltstart-Fragen

- Welche Rolle liegt vor: Patient, Arzt, Klinik, Hersteller, Sponsor, KV, Kasse oder Behörde?
- Welche Maßnahme, welches Produkt, welches Datum und welcher Rechtsstand sind entscheidend?
- Gibt es Aufklärung, Einwilligung, Studien-/Registerunterlagen, Produktinformationen oder Meldebelege?
- Geht es um Prävention, Anspruch, Verteidigung, Erstattung, Behörde oder gerichtliche Durchsetzung?

## Prüf- und Arbeitslogik

- **Rechtsanker:** SGB V, BVerfG/Bundessozialgericht nur verifiziert, AMG, Aufklärung und Dokumentation.
- **Tatsachenanker:** Behandlungs-/Therapiedatum, Rollen, Behandlungsdokumente, Aufklärung, Einwilligung, Freigaben, Befunde, Meldebelege, Beweiswert und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Innovative Medizin ist nicht automatisch Standard und nicht automatisch experimentell; Zeitpunkt und Datenlage sind zu trennen.
- Produkt-, Behandlungs-, Organisations- und Aufklärungsfehler nicht vermischen.
- Bei neuen EU-Regeln Übergangsfristen und nationale Durchführung gesondert prüfen.
- Gesundheitsdaten, Genomdaten und Patientengeheimnisse nur datensparsam verarbeiten.

## Output

- Mandats-/Fallvermerk mit Normenroute und Quellenstand.
- Dokumentenmatrix mit Lücken und Beweiswert.
- Risikoampel Haftung/Regulierung/Datenschutz/Erstattung.
- Nächster Schriftsatz-, Behörden- oder Mandantenkommunikationsbaustein.

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- EU HTA Regulation implementation: https://health.ec.europa.eu/health-technology-assessment/implementation-regulation-health-technology-assessment_en
- Joint Clinical Assessments: https://health.ec.europa.eu/health-technology-assessment/implementation-regulation-health-technology-assessment/joint-clinical-assessments_en
