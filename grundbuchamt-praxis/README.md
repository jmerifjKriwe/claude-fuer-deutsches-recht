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
| `abteilung-ii-iii-grundschuld-auflassung` | Nutze dies, wenn Abteilung Ii Dienstbarkeit Vormerkung Beschraenkung, Abteilung Iii Grundschuld Hypothek Rang, Auflassung Und Eigentumsumschreibung im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Abteilung I... |
| `auslandsurkunden-apostille-baulast-ist` | Nutze dies, wenn Auslandsurkunden Apostille Grundbuch, Baulast Ist Nicht Grundbuch, Beschwerde Grundbuchsache im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Auslandsurkunden Apostille Grundbuch, Baulast Ist... |
| `bestandsverzeichnis-flurstueck-briefrecht` | Nutze dies, wenn Bestandsverzeichnis Flurstueck Und Zuschreibung, Briefrecht Abtretung Und Löschung, Dienstbarkeit Wegerecht Prüfen im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Bestandsverzeichnis Flurstu... |
| `elektronischer-rechtsverkehr` | Nutze dies, wenn Elektronischer Rechtsverkehr Grundbuch, Familiengerichtliche Genehmigung Grundbuch, Finanzierung Und Rangstelle im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Elektronischer Rechtsverkehr G... |
| `gbo-antrag-gbr-egbr-genehmigungen` | Nutze dies, wenn Gbo Antrag Bewilligung Eintragung, Gbr Egbr Grundbuch, Genehmigungen Landwirtschaft Verkehrswert im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Gbo Antrag Bewilligung Eintragung, Gbr Egbr G... |
| `grundbuch-qualitygate-vor-vollzug` | Prüft Antrag, Bewilligung, Rang, Nachweise, Anlagen, Genehmigungen, Urkundenform und Zahlungslogik. |
| `grundbuch-vollzugslog-amtswiderspruch` | Nutze dies, wenn Grundbuch Vollzugslog, Grundbuchamt Amtswiderspruch Und Richtigstellung, Grundbuchamt Brief Vs Buchrecht Erklaerung im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Grundbuch Vollzugslog, Gru... |
| `grundbuchamt-allgemeiner-kaltstart` | Führt durch Eigentum, Belastungen, Vollzugsziel, Grundbuchbezirk, Urkundentyp, Nachweise, Rang, Fristdruck und Kommunikationsweg mit dem Grundbuchamt. |
| `grundbuchamt-eilfall-rangverlust-erbbaurecht` | Nutze dies, wenn Grundbuchamt Eilfall Rangverlust, Grundbuchamt Erbbaurecht Schnittstelle, Grundbuchamt Flurbereinigung Und Umlegung im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Grundbuchamt Eilfall Rangv... |
| `grundbuchamt-gesamtgrundschuld-mithaft` | Nutze dies, wenn Grundbuchamt Gesamtgrundschuld Und Mithaft, Grundbuchamt Gesellschaftsrechtliche Vertretung, Grundbuchamt Insolvenz Auslaendischer Trustee im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Gru... |
| `grundbuchamt-kommunikation-konkurrierende` | Nutze dies, wenn Grundbuchamt Kommunikation, Grundbuchamt Konkurrierende Antraege Rangkonflikt, Grundbuchamt Teilloesung Rangfreigabe im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Grundbuchamt Kommunikatio... |
| `grundbuchamt-maengelmatrix-notariat` | Nutze dies, wenn Grundbuchamt Maengelmatrix, Notariat Vollzugsauftrag Grundbuch, Abteilung I Eigentum Und Erwerbsgrund im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Grundbuchamt Maengelmatrix, Notariat Vol... |
| `grundbuchamt-nichtigkeitsrisiko-kaufvertrags` | Nutze dies, wenn Grundbuchamt Nichtigkeitsrisiko Kaufvertrag, Kaufvertrags Check Grundbuch, Amtshaftung Und Vollzugsfehler im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Grundbuchamt Nichtigkeitsrisiko Kauf... |
| `grundbuchauszug-due-lesen-abteilung` | Nutze dies, wenn Grundbuchauszug Für Due Diligence, Grundbuchauszug Lesen Abteilung I Ii Iii, Grundbuchberichtigung Erbfall im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Grundbuchauszug Für Due Diligence,... |
| `grunderwerbsteuer` | Nutze dies, wenn Grunderwerbsteuer Unbedenklichkeitsbescheinigung, Grundschuld Bestellung Buchgrundschuld, Grundschuldbrief Verlust Aufgebot im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Grunderwerbsteuer... |
| `insolvenzvermerk-zwangsversteigerung-kataster` | Nutze dies, wenn Insolvenzvermerk Zwangsversteigerung, Kataster Liegenschaftskarte Abgleich, Leitungsrecht Und Energieanlagen im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Insolvenzvermerk Zwangsversteiger... |
| `loeschungsbewilligung-bank-nacherbenvermerk` | Nutze dies, wenn Loeschungsbewilligung Bank, Nacherbenvermerk Und Verfuegungsbeschraenkung, Niessbrauch Wohnungsrecht im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Loeschungsbewilligung Bank, Nacherbenverm... |
| `paragraph-gbo-prioritaetsmitteilung` | Nutze dies, wenn Paragraph 29 Gbo Formnachweis, Prioritaetsmitteilung Und Rangbescheinigung, Rangprinzip Und Rangvorbehalt im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Paragraph 29 Gbo Formnachweis, Prior... |
| `reallast-erbbauzins-sanierungsvermerk` | Nutze dies, wenn Reallast Und Erbbauzins, Sanierungsvermerk Und Vorkaufsrechte Kommune, Teilflaechenkauf Und Vermessung im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Reallast Und Erbbauzins, Sanierungsverm... |
| `rechtsprechung-grundbuch-aufgebotsverfahren` | Nutze dies, wenn Rechtsprechung Grundbuch Live Verifizieren, Aufgebotsverfahren Famfg, Auflassungsvormerkung Kaufvertrag im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Rechtsprechung Grundbuch Live Verifizi... |
| `testamentsvollstrecker-grundbuch-vollmacht` | Nutze dies, wenn Testamentsvollstrecker Grundbuch, Vollmacht Vorsorgevollmacht Grundbuch, Vorkaufsrecht Wiederkaufsrecht im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Testamentsvollstrecker Grundbuch, Voll... |
| `verlorene-genehmigung-verwalterzustimmung-weg` | Nutze dies, wenn Grundbuchamt Verlorene Genehmigung Und Ersatznachweis, Grundbuchamt Verwalterzustimmung Weg, Grundbuchamt Vollstreckungsunterwerfung im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Grundbuch... |
| `weg-teilungsgrundbuch-zwischenverfuegung` | Nutze dies, wenn Weg Teilungsgrundbuch, Zwischenverfuegung Paragraph 18 Gbo im Plugin Grundbuchamt Praxis konkret bearbeitet werden soll. Auslöser: Bitte Weg Teilungsgrundbuch, Zwischenverfuegung Paragraph 18 Gbo prüfen.; Erstelle eine A... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
