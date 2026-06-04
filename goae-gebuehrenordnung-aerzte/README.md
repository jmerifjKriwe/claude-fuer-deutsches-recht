# GOÄ Gebührenordnung für Ärzte

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`goae-gebuehrenordnung-aerzte`) | [`goae-gebuehrenordnung-aerzte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/goae-gebuehrenordnung-aerzte.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Super-Plugin zur GOÄ: private Arztrechnungen prüfen, erstellen, begründen, beanstanden und prozessual verwerten.

## Wofür dieses Plugin da ist
Gebührenordnung für Ärzte mit Schwellenwerten, Steigerungssätzen, Analogabrechnung, Zielleistungsprinzip, Auslagen, Wahlleistungen, PKV/Beihilfe und Honorarstreit.

Das Plugin ist als Arbeitswerkzeug gedacht: Es startet mit einem Kaltstart-Interview, sortiert Unterlagen, prüft Fristen und routet dann in Spezial-Skills. Es soll Anfänger an die Hand nehmen und Profis schnell zu belastbaren Outputs bringen.

## Typischer Workflow
1. **Allgemein-Skill starten:** Rolle, Ziel, Frist, Unterlagen und gewünschtes Ergebnis klären.
2. **Dokumente einlesen:** Verträge, Bescheide, Rechnungen, Tabellen, Registerdaten, Behördenpost oder Screenshots strukturieren.
3. **Spezial-Skill wählen:** Das Plugin schlägt den passenden Skill vor und erklärt, welches Ergebnis damit entsteht.
4. **Live-Quellen prüfen:** Normtext, Behördenseite, EU-Text, Formular oder frei zugängliche Rechtsprechung aktualisieren.
5. **Output erzeugen:** Memo, Antrag, Stellungnahme, Vertragsklausel, Berechnung, Checkliste oder Mandantenbrief.
6. **Red-Team:** Fristen, Zuständigkeit, Zahlen, Quellen und Gegenargumente kontrollieren.

## Quellenanker
- Amtliche Gesetzestexte: gesetze-im-internet.de.
- EU-Recht: EUR-Lex und amtliche Kommissionsseiten.
- Behördenpraxis: zuständige Bundes-/Landesbehörden, Bundesnetzagentur, BaFin, BfArM, G-BA, BKartA oder Länderstellen je nach Thema.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei/amtlich prüfbarer Quelle.

## Skill-Schwerpunkte
| Gruppe | Inhalt |
| --- | --- |
| Einstieg und Workflow | Kaltstart, Dokumentenintake, Fristen, Quellencheck, Output-Wahl, Red-Team |
| Materielle Prüfung | Tatbestände, Ausnahmen, Schwellen, Beweislast, Berechnungen, Rechtsfolgen |
| Verfahren und Kommunikation | Anträge, Anhörungen, Beschwerden, Schriftsätze, Behördenkontakt, Mandantenkommunikation |
| Spezialthemen | Branchen-, Vertrags-, Gebühren-, Aufsichts-, EU- und Edge-Case-Prüfungen |

## Quellen- und Halluzinationsschutz
Dieses Plugin soll keine nicht prüfbaren Fundstellen produzieren. Bei unsicherer oder dynamischer Rechtslage wird der Live-Quellencheck ausdrücklich vorgeschaltet.

## Lizenz
Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im GOÄ Gebührenordnung für Ärzte-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Spezial-Skills aus diesem Plugin vor. |
| `kaltstart-goae-rechnung-pruefen` | Workflow zur strukturierten Aufnahme, Priorisierung und Ausgabe im Thema Kaltstart GOÄ Rechnung prüfen. |
| `kompendium-01-analoge-bewertung-ne-bis-abschnitt-a-beratung` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (analoge-bewertung-neue-verfahren-innovation, abrechnung-telemedizin-videosprechstunde-goae, abschnitt-a-beratungen-und-untersuchungen) und... |
| `kompendium-02-abschnitt-b-grundlei-bis-abtretung-factoring` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (abschnitt-b-grundleistungen-zuschlaege, abschnitt-c-nichtgebietsbezogene-sonderleistungen, abtretung-factoring-arzthonorar-datenschutz) un... |
| `kompendium-03-analogabrechnung-int-bis-arztbrief-begruendun` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (analogabrechnung-intake-6-goae, arbeitsunfaehigkeitsbescheinigung-privatpatient, arztbrief-begruendung-nachfordern) und bewahrt deren Work... |
| `kompendium-04-arzthonorarprozess-d-bis-begruendung-ueber-sc` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (arzthonorarprozess-dokumentenplan, auslandsbehandlung-deutsche-goae-anwendung, begruendung-ueber-schwellenwert-redigieren) und bewahrt der... |
| `kompendium-05-beihilfe-einwendunge-bis-berufsrecht-ueberhoe` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (beihilfe-einwendungen-und-differenzbetrag, belegarzt-und-konsiliararzt-abrechnung, berufsrecht-ueberhoehte-liquidation) und bewahrt deren... |
| `kompendium-06-erstattung-pkv-vs-ho-bis-gebuehrenrahmen-schw` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (erstattung-pkv-vs-honoraranspruch-patient, faelligkeit-verzug-mahnung-honorarklage, gebuehrenrahmen-schwellenwert-ampel) und bewahrt deren... |
| `kompendium-07-goae-1-anwendungsber-bis-goae-3-verguetungen` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (goae-1-anwendungsbereich-berufliche-leistungen, goae-2-abweichende-vereinbarung-honorarvereinbarung, goae-3-verguetungen-gebuehren-entscha... |
| `kompendium-08-goae-4-selbstaendige-bis-goae-5a-bemessung-im` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (goae-4-selbstaendige-aerztliche-leistung-zielleistungsprinzip, goae-5-bemessung-gebuehrenrahmen-2-3-1-8-1-15-schwelle, goae-5a-bemessung-i... |
| `kompendium-09-goae-5b-standardtari-bis-goae-6a-stationaere` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (goae-5b-standardtarif-pkv, goae-6-gebuehren-fuer-andere-leistungen-analogbewertung, goae-6a-stationaere-minderung-25-prozent-15-prozent) u... |
| `kompendium-10-goae-7-entschaedigun-bis-goae-9-reiseentschae` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (goae-7-entschaedigungen, goae-8-wegegeld, goae-9-reiseentschaedigung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemus... |
| `kompendium-11-goae-10-ersatz-von-a-bis-goae-14-zahlung-durc` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (goae-10-ersatz-von-auslagen, goae-12-faelligkeit-und-rechnungspflicht, goae-14-zahlung-durch-oeffentliche-leistungstraeger) und bewahrt de... |
| `kompendium-12-goae-rechnung-aus-pd-bis-gutachten-atteste-be` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (goae-rechnung-aus-pdf-extrahieren, goae-reform-referentenentwuerfe-beobachten, gutachten-atteste-bescheinigungen) und bewahrt deren Workfl... |
| `kompendium-13-igel-aufklaerung-kos-bis-kosmetische-leistung` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (igel-aufklaerung-kosteninformation, klageerwiderung-honorarprozess, kosmetische-leistungen-medizinische-indikation) und bewahrt deren Work... |
| `kompendium-14-laborleistungen-und-bis-livecheck-goae-text` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (laborleistungen-und-hoechstsatz-besonderheiten, leistungskette-zielleistung-keine-aufspaltung, livecheck-goae-text-und-reformstand) und be... |
| `kompendium-15-m-iii-m-iv-labor-del-bis-materialkosten-ausla` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (m-iii-m-iv-labor-delegation-speziallabor, mandantenmail-patient-freundlich-klar, materialkosten-auslagen-abgrenzung-10-goae) und bewahrt d... |
| `kompendium-16-mehrfachansatz-aussc-bis-notfall-behandlung-a` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (mehrfachansatz-ausschluesse-nebeneinanderberechnung, minderjaehrige-einwilligung-rechnung-schuldner, notfall-behandlung-ausserhalb-sprechs... |
| `kompendium-17-op-komplexe-narkose-bis-plausibilitaetscheck` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (op-komplexe-narkose-assistenz-zuschlaege, patientenbrief-und-einwendung-formulieren, plausibilitaetscheck-rechnung-mathematisch) und bewah... |
| `kompendium-18-psychotherapie-psych-bis-sachverstaendigenfra` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (psychotherapie-psychiatrie-gespraechsleistungen, radiologie-schnittbild-zielleistung, sachverstaendigenfragen-goae-streit) und bewahrt der... |
| `kompendium-19-schlichtungsstelle-a-bis-steigerungssatz-begr` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 19; bündelt 3 frühere Spezialskills (schlichtungsstelle-aerztekammer-honorarstreit, stationaere-privataerztliche-liquidation, steigerungssatz-begruendung-individuell-patienten... |
| `kompendium-20-tabellenexport-goae-bis-wahlleistungsvereinb` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 20; bündelt 3 frühere Spezialskills (tabellenexport-goae-pruefliste, verjaehrung-aerztlicher-honoraranspruch, wahlleistungsvereinbarung-krankenhaus-goae) und bewahrt deren Wor... |
| `kompendium-21-wegegeld-besuch-mehr-bis-zahnaerztliche-schni` | goae-gebuehrenordnung-aerzte: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (wegegeld-besuch-mehrere-patienten, zahnaerztliche-schnittstelle-goz-goae) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `red-team-goae-rechnung-halluzinationscheck` | Red-Team GOÄ Rechnung Halluzinationscheck: prüft die einschlägigen Voraussetzungen, Dokumente, Risiken und Ausnahmen. Norm-/Quellenanker: GOÄ §§ 1-14 und Anlage, BGB Behandlungsvertrag §§ 630a ff., PKV/Beihilfe-Regelungen, Berufsrecht, a... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
