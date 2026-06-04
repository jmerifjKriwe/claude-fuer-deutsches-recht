# Grundbuchamt Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`grundbuchamt-praxis`) | [`grundbuchamt-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/grundbuchamt-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Haus Altenau - verlorener Grundschuldbrief, Wegerecht und Kaufpreisfälligkeit** (`grundbuchamt-briefgrundschuld-wegerecht-altenau-2026`) | [Gesamt-PDF lesen](../testakten/grundbuchamt-briefgrundschuld-wegerecht-altenau-2026/gesamt-pdf/grundbuchamt-briefgrundschuld-wegerecht-altenau-2026_gesamt.pdf) | [`testakte-grundbuchamt-briefgrundschuld-wegerecht-altenau-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grundbuchamt-briefgrundschuld-wegerecht-altenau-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Grundbuch-Cockpit für alle, die Auszüge lesen, Urkunden grundbuchtauglich nachweisen, Zwischenverfügungen verstehen und Grundbuchvollzug sauber betreiben müssen. Schwerpunkt ist die praktische Leseführung durch Abteilung I, II und III, damit keine Dienstbarkeit, Vormerkung, Rangstelle oder Briefgrundschuld übersehen wird.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `grundbuchamt-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- [GBO](https://www.gesetze-im-internet.de/gbo/)
- [GBV](https://www.gesetze-im-internet.de/gbvfg/)
- [FamFG Aufgebotsverfahren](https://www.gesetze-im-internet.de/famfg/)
- [BGB Grundstücksrechte](https://www.gesetze-im-internet.de/bgb/)
- [Justizportal des Bundes und der Länder](https://justiz.de/)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 23 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `grundbuch-qualitygate-vor-vollzug` | Prüft Antrag, Bewilligung, Rang, Nachweise, Anlagen, Genehmigungen, Urkundenform und Zahlungslogik. |
| `grundbuchamt-allgemeiner-kaltstart` | Führt durch Eigentum, Belastungen, Vollzugsziel, Grundbuchbezirk, Urkundentyp, Nachweise, Rang, Fristdruck und Kommunikationsweg mit dem Grundbuchamt. |
| `kompendium-01-rechtsprechung-grund-bis-auflassungsvormerkun` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (rechtsprechung-grundbuch-live-verifizieren, aufgebotsverfahren-famfg, auflassungsvormerkung-kaufvertrag) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-02-grundbuchamt-nichtig-bis-amtshaftung-und-voll` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (grundbuchamt-nichtigkeitsrisiko-kaufvertrag, kaufvertrags-check-grundbuch, amtshaftung-und-vollzugsfehler) und bewahrt deren Workflows, Normanker,... |
| `kompendium-03-grundbuchamt-maengel-bis-abteilung-i-eigentum` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (grundbuchamt-maengelmatrix, notariat-vollzugsauftrag-grundbuch, abteilung-i-eigentum-und-erwerbsgrund) und bewahrt deren Workflows, Normanker, Prüf... |
| `kompendium-04-abteilung-ii-dienstb-bis-auflassung-und-eigen` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (abteilung-ii-dienstbarkeit-vormerkung-beschraenkung, abteilung-iii-grundschuld-hypothek-rang, auflassung-und-eigentumsumschreibung) und bewahrt der... |
| `kompendium-05-auslandsurkunden-apo-bis-beschwerde-grundbuch` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (auslandsurkunden-apostille-grundbuch, baulast-ist-nicht-grundbuch, beschwerde-grundbuchsache) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-06-bestandsverzeichnis-bis-dienstbarkeit-wegere` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (bestandsverzeichnis-flurstueck-und-zuschreibung, briefrecht-abtretung-und-loeschung, dienstbarkeit-wegerecht-pruefen) und bewahrt deren Workflows,... |
| `kompendium-07-elektronischer-recht-bis-finanzierung-und-ran` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (elektronischer-rechtsverkehr-grundbuch, familiengerichtliche-genehmigung-grundbuch, finanzierung-und-rangstelle) und bewahrt deren Workflows, Norma... |
| `kompendium-08-gbo-antrag-bewilligu-bis-genehmigungen-landwi` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (gbo-antrag-bewilligung-eintragung, gbr-egbr-grundbuch, genehmigungen-landwirtschaft-verkehrswert) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-09-grundbuch-vollzugslo-bis-grundbuchamt-brief-v` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (grundbuch-vollzugslog, grundbuchamt-amtswiderspruch-und-richtigstellung, grundbuchamt-brief-vs-buchrecht-erklaerung) und bewahrt deren Workflows, N... |
| `kompendium-10-grundbuchamt-eilfall-bis-grundbuchamt-flurber` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (grundbuchamt-eilfall-rangverlust, grundbuchamt-erbbaurecht-schnittstelle, grundbuchamt-flurbereinigung-und-umlegung) und bewahrt deren Workflows, N... |
| `kompendium-11-grundbuchamt-gesamtg-bis-grundbuchamt-insolve` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (grundbuchamt-gesamtgrundschuld-und-mithaft, grundbuchamt-gesellschaftsrechtliche-vertretung, grundbuchamt-insolvenz-auslaendischer-trustee) und bew... |
| `kompendium-12-grundbuchamt-kommuni-bis-grundbuchamt-teilloe` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (grundbuchamt-kommunikation, grundbuchamt-konkurrierende-antraege-rangkonflikt, grundbuchamt-teilloesung-rangfreigabe) und bewahrt deren Workflows,... |
| `kompendium-13-grundbuchamt-verlore-bis-grundbuchamt-vollstr` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (grundbuchamt-verlorene-genehmigung-und-ersatznachweis, grundbuchamt-verwalterzustimmung-weg, grundbuchamt-vollstreckungsunterwerfung) und bewahrt d... |
| `kompendium-14-grundbuchauszug-fuer-bis-grundbuchberichtigun` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (grundbuchauszug-fuer-due-diligence, grundbuchauszug-lesen-abteilung-i-ii-iii, grundbuchberichtigung-erbfall) und bewahrt deren Workflows, Normanker... |
| `kompendium-15-grunderwerbsteuer-un-bis-grundschuldbrief-ver` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (grunderwerbsteuer-unbedenklichkeitsbescheinigung, grundschuld-bestellung-buchgrundschuld, grundschuldbrief-verlust-aufgebot) und bewahrt deren Work... |
| `kompendium-16-insolvenzvermerk-zwa-bis-leitungsrecht-und-en` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (insolvenzvermerk-zwangsversteigerung, kataster-liegenschaftskarte-abgleich, leitungsrecht-und-energieanlagen) und bewahrt deren Workflows, Normanke... |
| `kompendium-17-loeschungsbewilligun-bis-niessbrauch-wohnungs` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (loeschungsbewilligung-bank, nacherbenvermerk-und-verfuegungsbeschraenkung, niessbrauch-wohnungsrecht) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-18-paragraph-29-gbo-for-bis-rangprinzip-und-rang` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (paragraph-29-gbo-formnachweis, prioritaetsmitteilung-und-rangbescheinigung, rangprinzip-und-rangvorbehalt) und bewahrt deren Workflows, Normanker,... |
| `kompendium-19-reallast-und-erbbauz-bis-teilflaechenkauf-und` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 19; bündelt 3 frühere Spezialskills (reallast-und-erbbauzins, sanierungsvermerk-und-vorkaufsrechte-kommune, teilflaechenkauf-und-vermessung) und bewahrt deren Workflows, Normanker, Prü... |
| `kompendium-20-testamentsvollstreck-bis-vorkaufsrecht-wieder` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 20; bündelt 3 frühere Spezialskills (testamentsvollstrecker-grundbuch, vollmacht-vorsorgevollmacht-grundbuch, vorkaufsrecht-wiederkaufsrecht) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-21-weg-teilungsgrundbuc-bis-zwischenverfuegung-p` | grundbuchamt-praxis: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (weg-teilungsgrundbuch, zwischenverfuegung-paragraph-18-gbo) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
