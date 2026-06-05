# Handelsregister Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`handelsregister-praxis`) | [`handelsregister-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/handelsregister-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Rabenhof Sensorik GmbH - Registergericht Charlottenburg, HRB 246810 B** (`handelsregister-registergericht-rabenhof-gmbh-2026`) | [Gesamt-PDF lesen](../testakten/handelsregister-registergericht-rabenhof-gmbh-2026/gesamt-pdf/handelsregister-registergericht-rabenhof-gmbh-2026_gesamt.pdf) | [`testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsregister-registergericht-rabenhof-gmbh-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Registergerichts-Cockpit für Gesellschaftsrechtler, Notariate, Kanzleien und Rechtsabteilungen. Es ordnet, was eingetragen werden soll, welche Urkunden nötig sind, wer beim Registergericht entscheidet, wie man Beanstandungen beantwortet und wann Beschwerde oder Eilrechtsschutz Sinn ergeben.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `handelsregister-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- [HGB §§ 8 ff., § 15](https://www.gesetze-im-internet.de/hgb/)
- [FamFG Registersachen und Beschwerde](https://www.gesetze-im-internet.de/famfg/)
- [GmbHG Anmeldung, Gesellschafterliste, Kapitalmaßnahmen](https://www.gesetze-im-internet.de/gmbhg/)
- [Registerportal der Länder](https://www.handelsregister.de/)
- [Unternehmensregister](https://www.unternehmensregister.de/)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `beanstandung-zwischenverfuegung` | Nutze dies, wenn Beanstandung Zwischenverfuegung Antwort, Bekanntmachungen Monitoring, Chronologischer Registerauszug im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Beanstandung Zwischenverfuegung Antwor... |
| `closing-handelregister-einstweiliger` | Nutze dies, wenn Closing Handelregister Vollzug, Einstweiliger Rechtsschutz Registerstreit, Eintragung Prozessvergleich Registerfolge im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Closing Handelregister... |
| `erlaubnispflichtige-taetigkeit-famfg` | Nutze dies, wenn Erlaubnispflichtige Taetigkeit Register, Famfg Beschwerde Registersache, Fehlerhafte Eintragung Berichtigung im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte re... |
| `firma-firmenbildung-formwechsel-registercheck` | Nutze dies, wenn Firma Firmenbildung Und Irrefuehrung, Formwechsel Registercheck, Genossenschaft Registerschnittstelle im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Firma Firmenbildung Und Irrefuehrung,... |
| `gesellschafterlistenstreit-eilstrategie-gmbh` | Nutze dies, wenn Gesellschafterlistenstreit Eilstrategie, Gmbh Co Kg Registerdoppelvollzug, Gmbh Geschaeftsfuehrerbestellung Abberufung im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Gesellschafterlisten... |
| `gmbh-gesellschafterliste-paragraph-gruendung` | Nutze dies, wenn Gmbh Gesellschafterliste Paragraph 40, Gmbh Gruendung Erstanmeldung, Gmbh Kapitalerhoehung Bareinlage im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Gmbh Gesellschafterliste Paragraph 40... |
| `gmbh-kapitalerhoehung-sacheinlage` | Nutze dies, wenn Gmbh Kapitalerhoehung Sacheinlage, Gmbh Kapitalherabsetzung Und Schutzjahr, Gmbh Liquidation Und Löschung im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Gmbh Kapitalerhoehung Sacheinlage... |
| `gmbh-satzungsaenderung-handelsvollmacht-nicht` | Nutze dies, wenn Gmbh Satzungsaenderung Und Neufassung, Handelsvollmacht Nicht Eintragungsfaehig, Hgb Publizitaet Paragraph 15 im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Gmbh Satzungsaenderung Und Ne... |
| `handelsregister-allgemeiner-kaltstart` | Führt durch das erste Registerproblem: Wer meldet was an, welche Gesellschaft, welches Registerblatt, welches Ziel, welcher Fristdruck, welche Urkunden, welche Entscheidungsperson und welches Eskalationsniveau. |
| `insolvenzvermerk-registereintrag` | Nutze dies, wenn Insolvenzvermerk Und Registereintrag, Internationaler Registervergleich, Kg Kommanditist Eintritt Austritt Haftsumme im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Insolvenzvermerk Und R... |
| `ki-registerakte-nachlass` | Nutze dies, wenn Ki Registerakte Halluzinationsschutz, Nachlass Und Testamentsvollstrecker Register, Notar Registergericht Kommunikation im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Ki Registerakte Hal... |
| `ohg-kg-online-abruf-partg-partgmbb` | Nutze dies, wenn Ohg Kg Egbr Mopeg Statuswechsel, Online Abruf Registerportal Unternehmensregister, Partg Partgmbb Register im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Ohg Kg Egbr Mopeg Statuswechsel,... |
| `prokura-eintragung-rechtsabteilung` | Nutze dies, wenn Prokura Eintragung Und Widerruf, Rechtsabteilung Geschaeftsfuehrerbestellung Mit Auslandsbezug, Rechtsabteilung Gesellschafterliste Nach Streit Und Ev im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Ausl... |
| `rechtsabteilung-insolvenzvermerk` | Nutze dies, wenn Rechtsabteilung Insolvenzvermerk Und Auslaendischer Trustee, Rechtsabteilung Kapitalerhoehung Und Zwischenverfuegung, Rechtsabteilung Mopeg Gesellschaftsregister Und Ohg Sprung im Plugin Handelsregister Praxis konkret be... |
| `rechtsprechung-register-frist-vollzugslog` | Nutze dies, wenn Rechtsprechung Register Live Verifizieren, Frist Und Vollzugslog Register, Registerrecht Mandatsannahme Notarferne im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Rechtsprechung Register... |
| `rechtsschein-innenstreit-register` | Nutze dies, wenn Rechtsschein Und Innenstreit, Register Mandantenbrief, Register Qualitaetsgate Vor Einreichung im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Rechtsschein Und Innenstreit, Register Manda... |
| `registerakte-schnellscan-registerauszug-lesen` | Nutze dies, wenn Registerakte Schnellscan Und Vollzugskarte, Registerauszug Lesen, Registerbeweis Im Prozess im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Registerakte Schnellscan Und Vollzugskarte, Reg... |
| `registergericht-rollen-datenschutz` | Nutze dies, wenn Registergericht Rollen Rechtspfleger Registerrichter, Registergericht Und Datenschutz, Registerkosten Und Notarkosten im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Registergericht Rolle... |
| `registerrecht-aktiengesellschaft-vorstand` | Nutze dies, wenn Registerrecht Aktiengesellschaft Vorstand Aufsichtsrat, Registerrecht Beschlussmaengel Und Registervollzug, Registerrecht Digitalgruendung im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte... |
| `registerrecht-fehlende-einzahlung-fehlerhafte` | Nutze dies, wenn Registerrecht Fehlende Einzahlung, Registerrecht Fehlerhafte Geschaeftsfuehreradresse, Registerrecht Kapitalgesellschaft Co Kg Komplementaerwechsel im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöse... |
| `registerrecht-niederlassung-registergericht` | Nutze dies, wenn Registerrecht Niederlassung Filiale, Registerrecht Registergericht Telefonat Protokoll, Registerrecht Registerzeichen Und Aktenzeichen im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Regi... |
| `registerrecht-scheinloeschung` | Nutze dies, wenn Registerrecht Scheinloeschung Und Nachtragsliquidation, Registerrecht Se Und Europaeische Gesellschaft, Registerrecht Umbenennung Rebranding im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitt... |
| `registersperre-closing-sitz-inlandsanschrift` | Nutze dies, wenn Registersperre Und Closing Risiko, Sitz Inlandsanschrift Und Geschaeftsanschrift, Todesfall Gesellschafter Register im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Registersperre Und Clos... |
| `transparenzregister-schnittstelle-umwandlung` | Nutze dies, wenn Transparenzregister Schnittstelle, Umwandlung Registervollzug, Unternehmensgegenstand Beanstandung im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Transparenzregister Schnittstelle, Umwan... |
| `umzug-registerbezirk-amtsloeschung` | Nutze dies, wenn Umzug Registerbezirk, Amtsloeschung Familienloeschung Registerblatt, Auslandsurkunden Apostille Legalisation Uebersetzung im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Umzug Registerbez... |
| `verein-registerschnittstelle-verschmelzung` | Nutze dies, wenn Verein Registerschnittstelle, Verschmelzung Gmbh Registercheck, Vollmacht Und Anmeldung Oeffentliche Beglaubigung im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Verein Registerschnittste... |
| `zweigniederlassung-auslaendische` | Nutze dies, wenn Zweigniederlassung Auslaendische Gesellschaft im Plugin Handelsregister Praxis konkret bearbeitet werden soll. Auslöser: Bitte Zweigniederlassung Auslaendische Gesellschaft prüfen.; Erstelle eine Arbeitsfassung zu Zweign... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
