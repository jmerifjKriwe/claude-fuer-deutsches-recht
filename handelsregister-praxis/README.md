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
| `handelsregister-allgemeiner-kaltstart` | Führt durch das erste Registerproblem: Wer meldet was an, welche Gesellschaft, welches Registerblatt, welches Ziel, welcher Fristdruck, welche Urkunden, welche Entscheidungsperson und welches Eskalationsniveau. |
| `kompendium-01-rechtsprechung-regis-bis-registerrecht-mandat` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (rechtsprechung-register-live-verifizieren, frist-und-vollzugslog-register, registerrecht-mandatsannahme-notarferne) und bewahrt deren Workflows,... |
| `kompendium-02-umzug-registerbezirk-bis-auslandsurkunden-apo` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (umzug-registerbezirk, amtsloeschung-familienloeschung-registerblatt, auslandsurkunden-apostille-legalisation-uebersetzung) und bewahrt deren Wor... |
| `kompendium-03-beanstandung-zwische-bis-chronologischer-regi` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (beanstandung-zwischenverfuegung-antwort, bekanntmachungen-monitoring, chronologischer-registerauszug) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-04-closing-handelregist-bis-eintragung-prozessve` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (closing-handelregister-vollzug, einstweiliger-rechtsschutz-registerstreit, eintragung-prozessvergleich-registerfolge) und bewahrt deren Workflow... |
| `kompendium-05-erlaubnispflichtige-bis-fehlerhafte-eintragu` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (erlaubnispflichtige-taetigkeit-register, famfg-beschwerde-registersache, fehlerhafte-eintragung-berichtigung) und bewahrt deren Workflows, Norma... |
| `kompendium-06-firma-firmenbildung-bis-genossenschaft-regis` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (firma-firmenbildung-und-irrefuehrung, formwechsel-registercheck, genossenschaft-registerschnittstelle) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-07-gesellschafterlisten-bis-gmbh-geschaeftsfuehr` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (gesellschafterlistenstreit-eilstrategie, gmbh-co-kg-registerdoppelvollzug, gmbh-geschaeftsfuehrerbestellung-abberufung) und bewahrt deren Workfl... |
| `kompendium-08-gmbh-gesellschafterl-bis-gmbh-kapitalerhoehun` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (gmbh-gesellschafterliste-paragraph-40, gmbh-gruendung-erstanmeldung, gmbh-kapitalerhoehung-bareinlage) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-09-gmbh-kapitalerhoehun-bis-gmbh-liquidation-und` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (gmbh-kapitalerhoehung-sacheinlage, gmbh-kapitalherabsetzung-und-schutzjahr, gmbh-liquidation-und-loeschung) und bewahrt deren Workflows, Normank... |
| `kompendium-10-gmbh-satzungsaenderu-bis-hgb-publizitaet-para` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (gmbh-satzungsaenderung-und-neufassung, handelsvollmacht-nicht-eintragungsfaehig, hgb-publizitaet-paragraph-15) und bewahrt deren Workflows, Norm... |
| `kompendium-11-insolvenzvermerk-und-bis-kg-kommanditist-eint` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (insolvenzvermerk-und-registereintrag, internationaler-registervergleich, kg-kommanditist-eintritt-austritt-haftsumme) und bewahrt deren Workflow... |
| `kompendium-12-ki-registerakte-hall-bis-notar-registergerich` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (ki-registerakte-halluzinationsschutz, nachlass-und-testamentsvollstrecker-register, notar-registergericht-kommunikation) und bewahrt deren Workf... |
| `kompendium-13-ohg-kg-egbr-mopeg-st-bis-partg-partgmbb-regis` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (ohg-kg-egbr-mopeg-statuswechsel, online-abruf-registerportal-unternehmensregister, partg-partgmbb-register) und bewahrt deren Workflows, Normank... |
| `kompendium-14-prokura-eintragung-u-bis-rechtsabteilung-gese` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (prokura-eintragung-und-widerruf, rechtsabteilung-geschaeftsfuehrerbestellung-mit-auslandsbezug, rechtsabteilung-gesellschafterliste-nach-streit-... |
| `kompendium-15-rechtsabteilung-inso-bis-rechtsabteilung-mope` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (rechtsabteilung-insolvenzvermerk-und-auslaendischer-trustee, rechtsabteilung-kapitalerhoehung-und-zwischenverfuegung, rechtsabteilung-mopeg-gese... |
| `kompendium-16-rechtsschein-und-inn-bis-register-qualitaetsg` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (rechtsschein-und-innenstreit, register-mandantenbrief, register-qualitaetsgate-vor-einreichung) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-17-registerakte-schnell-bis-registerbeweis-im-pr` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (registerakte-schnellscan-und-vollzugskarte, registerauszug-lesen, registerbeweis-im-prozess) und bewahrt deren Workflows, Normanker, Prüfprogram... |
| `kompendium-18-registergericht-roll-bis-registerkosten-und-n` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (registergericht-rollen-rechtspfleger-registerrichter, registergericht-und-datenschutz, registerkosten-und-notarkosten) und bewahrt deren Workflo... |
| `kompendium-19-registerrecht-aktien-bis-registerrecht-digita` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 19; bündelt 3 frühere Spezialskills (registerrecht-aktiengesellschaft-vorstand-aufsichtsrat, registerrecht-beschlussmaengel-und-registervollzug, registerrecht-digitalgruendung) und... |
| `kompendium-20-registerrecht-fehlen-bis-registerrecht-kapita` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 20; bündelt 3 frühere Spezialskills (registerrecht-fehlende-einzahlung, registerrecht-fehlerhafte-geschaeftsfuehreradresse, registerrecht-kapitalgesellschaft-co-kg-komplementaerwech... |
| `kompendium-21-registerrecht-nieder-bis-registerrecht-regist` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 21; bündelt 3 frühere Spezialskills (registerrecht-niederlassung-filiale, registerrecht-registergericht-telefonat-protokoll, registerrecht-registerzeichen-und-aktenzeichen) und bewa... |
| `kompendium-22-registerrecht-schein-bis-registerrecht-umbene` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 22; bündelt 3 frühere Spezialskills (registerrecht-scheinloeschung-und-nachtragsliquidation, registerrecht-se-und-europaeische-gesellschaft, registerrecht-umbenennung-rebranding) un... |
| `kompendium-23-registersperre-und-c-bis-todesfall-gesellscha` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 23; bündelt 3 frühere Spezialskills (registersperre-und-closing-risiko, sitz-inlandsanschrift-und-geschaeftsanschrift, todesfall-gesellschafter-register) und bewahrt deren Workflows... |
| `kompendium-24-transparenzregister-bis-unternehmensgegensta` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 24; bündelt 3 frühere Spezialskills (transparenzregister-schnittstelle, umwandlung-registervollzug, unternehmensgegenstand-beanstandung) und bewahrt deren Workflows, Normanker, Prüf... |
| `kompendium-25-verein-registerschni-bis-vollmacht-und-anmeld` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 25; bündelt 3 frühere Spezialskills (verein-registerschnittstelle, verschmelzung-gmbh-registercheck, vollmacht-und-anmeldung-oeffentliche-beglaubigung) und bewahrt deren Workflows,... |
| `kompendium-26-zweigniederlassung-a-bis-zweigniederlassung-a` | handelsregister-praxis: Konsolidiertes Skill-Kompendium 26; bündelt 1 frühere Spezialskills (zweigniederlassung-auslaendische-gesellschaft) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
