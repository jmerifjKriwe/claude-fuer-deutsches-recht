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
| `beanstandung-zwischenverfuegung` | Beanstandung Zwischenverfuegung im Handelsregister-Praxis: prüft konkret Analysiert Registerbeanstandungen, trennt behebbare Formmängel von Rechtsstreit, Erstellt Monitoringplan für Bekanntmachungen, Friststart. Liefert priorisierten Out... |
| `closing-handelregister-einstweiliger` | Closing Handelregister Einstweiliger im Handelsregister-Praxis: prüft konkret Prüft CP/CS, Eintragungsabhängigkeiten, Vollzugsreihenfolge, Escrow. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `erlaubnispflichtige-taetigkeit-famfg` | Erlaubnispflichtige Taetigkeit Famfg im Handelsregister-Praxis: prüft konkret Prüft KWG, ZAG, GewO, Handwerk. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `firma-firmenbildung-formwechsel-registercheck` | Firma Firmenbildung Formwechsel Registercheck im Handelsregister-Praxis: prüft konkret Prüft Firmenkern, Unterscheidbarkeit, Irreführung, Rechtsformzusatz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `gesellschafterlistenstreit-eilstrategie-gmbh` | Gesellschafterlistenstreit Eilstrategie Gmbh im Handelsregister-Praxis: prüft konkret Ordnet Anspruch, einstweilige Verfügung, Registersperre, materiellen Streit und. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächs... |
| `gmbh-gesellschafterliste-paragraph-gruendung` | Gmbh Gesellschafterliste Paragraph Gruendung im Handelsregister-Praxis: prüft konkret Prüft Liste, Prozentangaben, Veränderungsspalte, Notarzuständigkeit. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `gmbh-kapitalerhoehung-sacheinlage` | Gmbh Kapitalerhoehung Sacheinlage im Handelsregister-Praxis: prüft konkret Prüft Sacheinlagebericht, Werthaltigkeit, verdeckte Sacheinlage, Anmeldung und B. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `gmbh-satzungsaenderung-handelsvollmacht-nicht` | Gmbh Satzungsaenderung Handelsvollmacht Nicht im Handelsregister-Praxis: prüft konkret Prüft Beschlussmehrheit, notarielle Beurkundung, vollständige Neufassung, Gegens. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und näc... |
| `handelsregister-kaltstart-routing` | Führt durch das erste Registerproblem: Wer meldet was an, welche Gesellschaft, welches Registerblatt, welches Ziel, welcher Fristdruck, welche Urkunden, welche Entscheidungsperson und welches Eskalationsniveau. |
| `insolvenzvermerk-registereintrag` | Insolvenzvermerk Registereintrag im Handelsregister-Praxis: prüft konkret Prüft Eintragung von Eröffnung, Eigenverwaltung, Aufhebung, Insolvenzplan. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `ki-registerakte-nachlass` | KI Registerakte Nachlass im Handelsregister-Praxis: prüft konkret Zwingt zu Belegpfad, Registerauszug, Aktenzeichen, Normenanker und klarer Kennze. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `ohg-kg-online-abruf-partg-partgmbb` | OHG KG Online Abruf Partg Partgmbb im Handelsregister-Praxis: prüft konkret Prüft kaufmännischen Betrieb, Statuswechsel, Anmeldung, Gesellschafter. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `prokura-eintragung-rechtsabteilung` | Prokura Eintragung Rechtsabteilung im Handelsregister-Praxis: prüft konkret Prüft Einzel-/Gesamtprokura, Filialprokura, Gesamtvertretung, Widerruf. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `rechtsabteilung-insolvenzvermerk` | Rechtsabteilung Insolvenzvermerk im Handelsregister-Praxis: prüft konkret Rechtsabteilungs-Fachmodul für Insolvenzvermerk und, Rechtsabteilungs-Fachmodul für Kapitalerhöhung und, Rechtsabteilungs-Fachmodul für MoPeG-Gesellschaftsregister... |
| `rechtsprechung-register-frist-vollzugslog` | Rechtsprechung Register Frist Vollzugslog im Handelsregister-Praxis: prüft konkret Legt fest, wie Entscheidungen in Registersachen nur mit Gericht, Datum, Aktenzei. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächste... |
| `rechtsschein-innenstreit-register` | Rechtsschein Innenstreit Register im Handelsregister-Praxis: prüft konkret Trennt materielles Gesellschaftsrecht, Registerlage, Vertretungsmacht und Gutgla, Erstellt klare Mandantenupdates. Liefert priorisierten Output mit Norm-Pinpoints... |
| `registerakte-schnellscan-registerauszug-lesen` | Registerakte Schnellscan Registerauszug Lesen im Handelsregister-Praxis: prüft konkret Erstellt eine Vollzugskarte aus Satzung, Beschluss, Anmeldung, Liste. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `registergericht-rollen-datenschutz` | Registergericht Rollen Datenschutz im Handelsregister-Praxis: prüft konkret Klärt Zuständigkeiten, Kommunikationsstil, Entscheidungswege und wann eine Sache, Klärt öffentliche Registerdaten. Liefert priorisierten Output mit Norm-Pinpoint... |
| `registerrecht-aktiengesellschaft-vorstand` | Registerrecht Aktiengesellschaft Vorstand im Handelsregister-Praxis: prüft konkret Prüft Bestellung, Vertretung, Satzungsänderungen, Kapitalmaßnahmen und Eintragun. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächste... |
| `registerrecht-fehlende-einzahlung-fehlerhafte` | Registerrecht Fehlende Einzahlung Fehlerhafte im Handelsregister-Praxis: prüft konkret Prüft Geschäftsführerversicherung, Kontoauszug, Hin- und Herzahlen, verdeckte Sa. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und näc... |
| `registerrecht-niederlassung-registergericht` | Registerrecht Niederlassung Registergericht im Handelsregister-Praxis: prüft konkret Prüft eintragungsfähige Zweigniederlassung, unselbständige Betriebsstätte und Ad, Erstellt kurze Telefonnotiz mit Name, Aktenzeichen. Liefert priorisier... |
| `registerrecht-scheinloeschung` | Registerrecht Scheinloeschung im Handelsregister-Praxis: prüft konkret Prüft Restvermögen, Prozessfähigkeit, Bestellung Nachtragsliquidator und Registe, Prüft SE-Firma. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und näc... |
| `registersperre-closing-sitz-inlandsanschrift` | Registersperre Closing Sitz Inlandsanschrift im Handelsregister-Praxis: prüft konkret Bewertet Sperrwirkung, einstweilige Verfügung, Gesellschafterlistenkonflikt und, Prüft Satzungssitz. Liefert priorisierten Output mit Norm-Pinpoints, R... |
| `transparenzregister-schnittstelle-umwandlung` | Transparenzregister Schnittstelle Umwandlung im Handelsregister-Praxis: prüft konkret Verbindet Handelsregisterdaten mit wirtschaftlich, GwG-Risiken und, Prüft Verschmelzung, Spaltung. Liefert priorisierten Output mit Norm-Pinpoints, Ris... |
| `umzug-registerbezirk-amtsloeschung` | Umzug Registerbezirk Amtsloeschung im Handelsregister-Praxis: prüft konkret Prüft innerörtlich/anderer Bezirk, Satzungsänderung, Registerabgabe, Bekanntmach. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `verein-registerschnittstelle-verschmelzung` | Verein Registerschnittstelle Verschmelzung im Handelsregister-Praxis: prüft konkret Klärt, wann Vereinsregisterlogik statt Handelsregisterlogik greift, Checkt Verschmelzungsvertrag, Zustimmungsbeschlüsse. Liefert priorisierten Output mit... |
| `zweigniederlassung-auslaendische` | Zweigniederlassung Auslaendische im Handelsregister-Praxis: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
