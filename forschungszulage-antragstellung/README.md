# Forschungszulage-Antragstellung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`forschungszulage-antragstellung`) | [`forschungszulage-antragstellung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/forschungszulage-antragstellung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Forschungszulage Riedblick Sensorik GmbH** (`forschungszulage-sensorik-startup-taunus`) | [Gesamt-PDF lesen](../testakten/forschungszulage-sensorik-startup-taunus/gesamt-pdf/forschungszulage-sensorik-startup-taunus_gesamt.pdf) | [`testakte-forschungszulage-sensorik-startup-taunus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-forschungszulage-sensorik-startup-taunus.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für die steuerliche Forschungsförderung nach dem Forschungszulagengesetz: Fördercheck, BSFZ-Bescheinigung, Projektbeschreibung, FuE-Abgrenzung, Bemessungsgrundlage, Finanzamt-Antrag, Auszahlung, Verlust-/Krisenlage, Dokumentation für Außenprüfung, Kumulierung und Nachbesserung.

Das Plugin ist für Unternehmen, Start-ups, Mittelstand, Steuerberaterinnen, Rechtsanwälte, CFOs und Produkt-/Entwicklungsteams gebaut. Es übersetzt technische Entwicklung in die Sprache, die BSFZ und Finanzamt brauchen: Neuheit, Risiko, systematisches Vorgehen, förderfähige Aufwendungen und saubere Belege. Es kann bewusst zwei Geschwindigkeiten: geführter Modus für Einsteiger und harter Ampel-/Cashflow-Modus für Profis.

## Quellen-Gate

Vor jeder belastbaren Ausgabe live prüfen:

- Forschungszulagengesetz auf `gesetze-im-internet.de`, insbesondere §§ 1 bis 7 und § 10 FZulG.
- BSFZ-Antragsverfahren: zweistufig, erst FuE-Bescheinigung bei der BSFZ, dann Antrag beim Finanzamt.
- BMF-Forschungszulage und BMF-Schreiben vom 07.02.2023, soweit noch nicht durch ein neues finales Schreiben ersetzt.
- Änderungen ab 2026: Bemessungsgrundlagenhöchstbetrag 12 Mio. Euro, 20-%-Pauschale für Gemein- und Betriebskosten bei nach dem 31.12.2025 begonnenen Vorhaben, Eigenleistung 100 Euro pro Stunde bis max. 40 Stunden/Woche.

## Skill-Matrix

| Skill | Wofür? |
| --- | --- |
| `forschungszulage-antragstellung-allgemein` | Einstieg, Triage, Förderroute und Projektaufnahme |
| `fz-foerdercheck-kaltstart` | Anspruchsberechtigung, Projektart, Jahre, Risiken, Sofortpotenzial |
| `fz-bsfz-bescheinigung-projektbeschreibung` | BSFZ-Antrag, Vorhabenbeschreibung, technische Neuheit, Risiko |
| `fz-plaedoyer-begruendung-und-verteidigung` | Plädoyer, Begründung und Verteidigung gegenüber BSFZ, Finanzamt, Geschäftsführung, Insolvenzverwaltung oder Einspruchsstelle |
| `fz-fue-definition-frascati-abgrenzung` | Grundlagenforschung, industrielle Forschung, experimentelle Entwicklung |
| `fz-bemessungsgrundlage-2026` | Personal, Eigenleistung, Auftragsforschung, Wirtschaftsgüter, 12-Mio.-Grenze |
| `fz-finanzamt-festsetzung-auszahlung` | Antrag beim Finanzamt, Anrechnung, Auszahlung, Vorauszahlungssenkung |
| `fz-insolvenz-verlust-liquiditaet` | Krise, Verlustjahr, Insolvenz, Forderungs-/Masseblick, Liquidität |
| `fz-dokumentationspaket-betriebspruefung` | Stundenzettel, Projektakte, Kostenbelege, Prüferpaket |
| `fz-kumulierung-beihilfen-agvo` | Doppelförderung, AGVO, andere Zuschüsse, EU/EWR-Auftragsforschung |
| `fz-ablehnung-nachbesserung-einspruch` | BSFZ-Nachforderung, Ablehnung, Finanzamt-Einspruch, Reparatur |
| `fz-roadmap-mehrjahresantrag` | Mehrjahresstrategie, rückwirkende Jahre, Jahreswechsel, Portfolio |

## Typische Startpunkte

| Situation | Start |
| --- | --- |
| "Wir wissen nicht, ob unser Vorhaben FuE ist" | `forschungszulage-antragstellung-allgemein` → `fz-foerdercheck-kaltstart` |
| "Wir müssen den BSFZ-Antrag schreiben" | `fz-fue-definition-frascati-abgrenzung` → `fz-bsfz-bescheinigung-projektbeschreibung` |
| "Wir brauchen ein überzeugendes Plädoyer / eine Begründung" | `fz-plaedoyer-begruendung-und-verteidigung` |
| "Wir wollen wissen, wie viel Geld kommt" | `fz-bemessungsgrundlage-2026` → `fz-finanzamt-festsetzung-auszahlung` |
| "Wir sind im Verlust / in der Krise" | `fz-insolvenz-verlust-liquiditaet` |
| "BSFZ fragt nach oder lehnt ab" | `fz-ablehnung-nachbesserung-einspruch` |

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 71 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abgrenzung-adaptiver-antrag` | Abgrenzung Adaptiver Antrag: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `antragstellung-auszahlung-beihilfen` | Auszahlung Beihilfen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `beihilfen-beweislast-darlegungslast` | Beihilfen: Beweislast, Darlegungslast und Substantiierung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `bemessungsgrundlage-interessen` | Bemessungsgrundlage: Mehrparteienkonflikt und Interessenmatrix: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `bemessungsgrundlage-interessen-bsfz` | Bemessungsgrundlage Interessen Bsfz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `einspruch-sonderfall-edge-case` | Einspruch: Sonderfall und Edge-Case-Prüfung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `finanzamt-quellenkarte` | Finanzamt Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `forsch-bsfz-pruefung-spezial` | Spezialfall BSFZ-Pruefung und Nachfragen: typische Rueckfragen Bescheinigungsstelle, Stellungnahmefrist, Widerspruch. Pruefraster fuer Antragsteller und Steuerberater. |
| `forsch-konzernverbund-forschung-spezial` | Spezialfall Konzernverbundforschung und verbundene Unternehmen: § 3 Abs. 1 FZulG, Auftragsforschung, KMU-Status, Beihilfen-Kumulation. Pruefraster fuer Konzerntochter und Forschungs-GmbH. |
| `forsch-projektbeschreibung-bauleiter` | Bauleiter Projektbeschreibung FZulG: FuE-Definition Frascati, Neuheit, technologisches Risiko, systematische Vorgehensweise. Pruefraster fuer schluessige Darstellung gegenueber BSFZ. |
| `forsch-stundenaufzeichnung-fz-ablehnung` | Forsch Stundenaufzeichnung FZ Ablehnung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `forsch-stundenaufzeichnung-leitfaden` | Leitfaden Stundenaufzeichnung FZulG: zuwendungsfaehige Personalkosten, eigene Beschaeftigte, Auftragsforschung, Dokumentationspflichten. Pruefraster fuer Personalcontrolling. |
| `forschungszulage-antragstellung-abgrenzung-compliance` | Abgrenzung: Compliance-Dokumentation und Aktenvermerk: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-adaptiver-dokumentenmatrix` | Adaptiver: Dokumentenmatrix, Lückenliste und Nachforderung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `forschungszulage-antragstellung-antrag-zahlen-schwellenwerte` | Antrag: Zahlen, Schwellenwerte und Berechnung: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-auszahlung-internationaler-bezug` | Auszahlung: Internationaler Bezug und Schnittstellen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-bsfz-behoerden-gerichts` | Bsfz: Behörden-, Gerichts- oder Registerweg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-definition-abschlussprodukt` | Definition: Abschlussprodukt und Übergabe: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `forschungszulage-antragstellung-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `forschungszulage-antragstellung-foerdercheck-risikoampel` | Foerdercheck: Risikoampel, Gegenargumente und Verteidigungslinien: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-fristen-und-risikoampel` | Fristen- und Risikoampel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-fz-bescheidung-rechtsmittel-bsfz` | FZ Bescheidung Rechtsmittel Bsfz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `forschungszulage-antragstellung-fz-betriebspruefung-strategie` | FZ Betriebspruefung Strategie: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `forschungszulage-antragstellung-fz-fue-abgrenzung-definition` | FZ FUE Abgrenzung Definition: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `forschungszulage-antragstellung-fz-koordinierung-zwei` | FZ Koordinierung Zwei: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `forschungszulage-antragstellung-fz-plaedoyer-begruendung-roadmap` | FZ Plaedoyer Begruendung Roadmap: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `forschungszulage-antragstellung-fzulg-fristen-form` | FZulG: Fristen, Form, Zuständigkeit und Rechtsweg: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-kaltstart-triage` | Adaptiver Einstieg, Mandatsklärung und Routing im Forschungszulage-Plugin. Führt Einsteiger, Technikteams, CFOs und Steuerberater unterschiedlich, klärt Unternehmen, FuE-Vorhaben, Wirtschaftsjahre, BSFZ-Status, Finanzamt-Antrag, Liquidit... |
| `forschungszulage-antragstellung-mandantenkommunikation` | Mandantenkommunikation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-portaltexte-schriftsatz-brief` | Portaltexte: Schriftsatz-, Brief-, Memo- und Plädoyer-Bausteine: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `forschungszulage-antragstellung-redteam-qualitygate` | Red-Team Qualitygate: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `forschungszulage-antragstellung-start-chronologie-fristen` | Start Chronologie Fristen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `forschungszulage-antragstellung-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `forschungszulage-antragstellung-verlust-formular-portal` | Verlust: Formular, Portal und Einreichungslogik: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-antragstellung-workflow-mandantenkommunikation` | Workflow Mandantenkommunikation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `forschungszulage-antragstellung-zeichenbudgets-verhandlung` | Zeichenbudgets: Verhandlung, Vergleich und Eskalation: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-insolvenzlage-red` | Insolvenzlage RED: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `forschungszulage-mandantenentscheidung-antragspfad` | Dokumentation: Mandantenkommunikation und Entscheidungsvorlage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `forschungszulage-projektbeschreibung-bescheinigung` | Forschungszulage: Erstprüfung, Rollenklärung und Mandatsziel: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `fz-ablehnung-nachbesserung-einspruch` | Ablehnung oder Nachforderung bei Forschungszulage strukturiert bearbeiten: BSFZ-Rückfrage, negative Bescheinigung, BSFZ-Widerspruch, Finanzamt-Kürzung, Einspruch nach AO, neue Tatsachen, Beleg- und Textreparatur, Klage Finanzgericht als... |
| `fz-auftragsforschung-vertragsgestaltung` | Auftragsforschung im Sinne § 3 Abs. 4 FZulG: Auftraggeber-Auftragnehmer-Konstellation, Pflichten des Auftraggebers (Risikotragung, Verwertung), foerderfaehige Quote 60 oder 70 Prozent der vereinbarten Vergueng. Pruefraster Vertragsgestal... |
| `fz-bemessungsgrundlage-2026` | Bemessungsgrundlage Forschungszulage ab 2026 belastbar berechnen: eigene FuE-Personalkosten, Eigenleistung 100 Euro je Stunde, Auftragsforschung 70 Prozent EU/EWR, AfA für Wirtschaftsgüter, 20-Prozent-Gemeinkostenpauschale, 12-Mio-Cap, K... |
| `fz-bescheidung-rechtsmittel` | Bescheidung Forschungszulage: Bescheinigungsbescheid BSFZ und Festsetzungsbescheid Finanzamt sind zwei getrennte Verwaltungsakte. Rechtsmittelketten: BSFZ-Widerspruch dann Verpflichtungsklage; Finanzamt-Einspruch dann Klage Finanzgericht... |
| `fz-betriebspruefung-strategie` | Strategie bei Betriebspruefung mit Schwerpunkt Forschungszulage: Vorbereitung, Selbstanzeige bei Fehlern (auch wenn keine Steuerstraftat), Argumentationspakete, Schlussbesprechung. Pruefraster: Stundennachweise, Auftragsforschungsvertrae... |
| `fz-bsfz-bescheinigung-projektbeschreibung` | BSFZ-Antrag und FuE-Projektbeschreibung praxistauglich erstellen: Portaltexte mit Zeichenbudgets, Ausgangsproblem, Stand der Technik, Neuheit, technisches Risiko, systematisches Vorgehen, Arbeitspakete, Prüferlogik, Anti-Floskel-Regeln u... |
| `fz-dokumentationspaket-betriebspruefung` | Dokumentationspaket Forschungszulage prüfungsfest aufbauen: Projektakte mit BSFZ-Antrag und Bescheid, Stundenaufzeichnung je Mitarbeiter Tag Vorhaben, Personalkostenbeleg aus Lohnabrechnung, Auftragsforschungsbeleg mit Vertrag und Rechnu... |
| `fz-finanzamt-festsetzung-auszahlung` | Forschungszulage beim Finanzamt beantragen, festsetzen und auszahlen lassen: ELSTER-Antrag, Vorlage der BSFZ-Bescheinigung, Forschungszulagenbescheid, Anrechnung auf Einkommen- oder Körperschaftsteuer, Auszahlung eines Überschusses, Vora... |
| `fz-foerdercheck-kaltstart` | Schneller Fördercheck Forschungszulage in zehn Minuten: Anspruchsberechtigung, FuE-Kategorie nach Frascati, KMU-Status, Personalkosten-Schwelle, Projektjahre, Kostenarten, BSFZ-/Finanzamt-Status, Kumulierung, Ausschlussrisiken und realis... |
| `fz-fue-abgrenzung-grenzfaelle` | FuE-Definition Grenzfaelle nach Frascati-Manual und FZulG: Neuheit und Unsicherheit, Routinearbeiten gegen Versuch und Irrtum. Beispielszenarien Software-Entwicklung, klinische Studien, Produktoptimierung, Reverse Engineering. Pruefraste... |
| `fz-fue-definition-frascati-abgrenzung` | FuE-Definition für die Forschungszulage praxisnah prüfen: Grundlagenforschung, industrielle Forschung, experimentelle Entwicklung, Frascati-Kriterien (Neuheit, Schöpferisch, Ungewissheit, Systematik, Reproduzierbarkeit), AGVO-Definitione... |
| `fz-historie-und-rechtsgrundlagen` | Historie und Rechtsgrundlagen der steuerlichen Forschungszulage einfuehrend: FZulG seit 2020, Wachstumschancengesetz 2024 mit Erhoehung auf 10 Mio. Euro Bemessungsgrundlage, KMU-Bonus 5 Mio. Euro. Verhaeltnis zu Projektfoerderung (Bund,... |
| `fz-insolvenz-forsch-konzernverbund` | FZ Insolvenz Forsch Konzernverbund: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fz-insolvenz-verlust-liquiditaet` | Forschungszulage in Verlust-, Krisen- und Insolvenzlagen als Liquiditätshebel nutzen: Auszahlung statt bloßer Steuerersparnis, Vorauszahlungssenkung, Massezugehörigkeit, Antragsbefugnis Geschäftsleitung oder Insolvenzverwaltung, Aufrechn... |
| `fz-konzern-und-organschaft-spezial` | Spezialfall Konzern und Organschaft: Zurechnung von FuE-Aktivitaeten zwischen Mutter und Tochter, Auftragsforschung im Konzernverbund, Verrechnungspreise mit Fremdvergleich, KMU-Status bei Konzernzugehoerigkeit nach KMU-Empfehlung 2003 3... |
| `fz-koordinierung-zwei-foerderwege` | Koordinierung Forschungszulage mit anderen Foerderwegen: keine Doppelfoerderung derselben Kosten, aber Kombination ueber Modulgrenze hinweg (ZIM, IGF, Horizon Europe, Landesfoerderung). Pruefraster fuer Kostentrennung, Buchhaltung, Besch... |
| `fz-kumulierung-beihilfen-agvo` | Kumulierung Forschungszulage mit anderen Förderungen und Beihilfen sauber prüfen: AGVO Art. 25, EU/EWR-Auftragsforschung, ZIM, BMBF-Programme, Landesprogramme, De-minimis-Nähe, Horizon, Doppelförderung, Nachweis- und Abzugslogik. Mit Kum... |
| `fz-personalkosten-und-stundennachweis` | Foerderfaehige Personalkosten der Forschungszulage: Bruttoarbeitslohn plus Arbeitgeberanteile, Stundenpauschale 70 Euro Eigenunternehmer, Auftragsforschung 60 Prozent (KMU 70 Prozent). Stundennachweissystem: tagesgenau, Aufgabenbezug, Pl... |
| `fz-plaedoyer-begruendung-und-verteidigung` | Plädoyer, Begründung und Verteidigung der Forschungszulage: macht aus Technik, Belegen, Kosten und Behördenkritik einen überzeugenden Vortrag für BSFZ, Finanzamt, Einspruch, Mandantenmemo oder Geschäftsführungsentscheidung. Mit Argumenta... |
| `fz-roadmap-mehrjahresantrag` | Mehrjahresstrategie Forschungszulage: BSFZ-Bescheinigung für mehrjährige Vorhaben, jährliche Aktualisierung der Stundenaufzeichnung und Projektakte, Folgeanträge knapp halten, Roadmap-Pflege, Liquiditätsplanung über Wirtschaftsjahre, rüc... |
| `fz-start-up-und-personengesellschaft` | Start-up- und Personengesellschafts-Konstellation Forschungszulage: GmbH und Co KG, atypisch stille Beteiligung, Mitunternehmerschaft, Verluste in Anfangsjahren mit Zulage als Liquiditaetshebel. Beispielrechnungen, typische Pruefpunkte.... |
| `insolvenzlage-fehlerkatalog` | Insolvenzlage Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `mandantenentscheidung-einspruch-sonderfall` | Mandantenentscheidung Einspruch Sonderfall: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mehrjahresroadmap-fristennotiz-fz` | Mehrjahresroadmap Fristennotiz FZ: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mehrjahresroadmap-fristennotiz-naechster` | Mehrjahresroadmap: Fristennotiz und nächster Schritt: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `tatbestand-beweis-belege-antragstellung` | Antragstellung: Tatbestandsmerkmale, Beweisfragen und Beleglage: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `verlust-zeichenbudgets` | Verlust Zeichenbudgets: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
