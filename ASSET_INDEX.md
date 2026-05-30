# Release-Asset-Index

Übersicht aller Dateien, die der Release-Workflow (`.github/workflows/release-plugin-zips.yml`) pro Tag-Release `vX.Y.Z` an den GitHub-Release anhängt.

**Stand:** v50.6.1 Schmalfeld-Betreuungsakte vertieft und Übersichten synchronisiert

## Asset-Typen

| Typ | Erkennungsmerkmal | Verwendung |
| --- | --- | --- |
| **plugin** | `<plugin-name>.zip` | Über "Customize Plugins -> Install from .zip" in Claude Code/Cowork hochladen. |
| **fallakte** | `testakte-<aktenname>.zip` | **Kein Plugin.** Mandatsunterlagen für Testzwecke. In den Chat ziehen, nicht in den Plugin-Upload-Dialog. |
| **manifest** | `marketplace.json` | **Kein Plugin.** Marketplace-Manifest für `/plugin marketplace add` und zur manuellen Inspektion. |
| **sammelarchiv** | `alle-plugins-megazip.zip`, `alle-testakten.zip`, `alles-komplettpaket.zip` | Komfort-Downloads für den gesamten Plugin-, Testakten- oder Komplettbestand. |

## Sammel-Assets (3 Stück)

| Asset | Verwendung |
| --- | --- |
| [`alle-plugins-megazip.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-plugins-megazip.zip) | Enthält alle installierbaren Plugin-ZIPs plus `marketplace.json`. Nach dem Entpacken einzelne Plugin-ZIPs über "Install from .zip" laden oder das Manifest prüfen. |
| [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) | Enthält alle Testaktenordner in Originalstruktur. **Kein Plugin-Archiv**; die Akten in den Chat bzw. Arbeitsordner ziehen. |
| [`alles-komplettpaket.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alles-komplettpaket.zip) | Enthält alle Plugin-ZIPs, alle Testakten-ZIPs, `marketplace.json` und die zentralen Übersichten. |

## Plugin-Assets (108 Stück)

In der Reihenfolge der `.claude-plugin/marketplace.json`. URL-Schema:
`https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<name>.zip`

| Plugin | Kurzbeschreibung |
| --- | --- |
| `aktenaufbereiter-strafrecht` | Aktenaufbereiter für die Strafverteidigung. Sechs Excel-fähige Übersichten — Aktenvorblatt; Personenverzeichnis; Tatkomplexe; Beziehungen; Chronologie; Fristen. Fortlaufend ergaenzbar. Erkennt Luecken und Widersprueche. Kein Ersatz für Aktenlektuere. |
| `aktenauszug-gerichtsverfahren` | Strukturierter Aktenauszug für deutsche Gerichtsverfahren: Verfahrensidentifikation Einleitungssatz Verfahrenszusammenfassung Sachverhaltschronologie Verfahrensgeschichte tabellarische Gegenüberstellung der Parteivortraege Beweismittel und Rechtsargumente für schnelle Einarbeitung in Akten. |
| `anlagen-zu-schriftsaetzen` | Zuordnung von Anlagen zu gerichtlichen Schriftsaetzen. Sortiert PDF/Word/Excel nach Schriftsatz-Logik; konvertiert alles nach PDF; benennt beA-konform; stempelt oben rechts Anlage K1/B1/A1 in Arial 12; baut Anlagenkonvolut; Prüfmodus für bereits zugeordnete Anlagen. |
| `arbeitsrecht` | Arbeitsrechtliche Workflows fuer Kuendigung, Befristung, Urlaub, AGG, Aufhebungsvertrag, Betriebsrat, Arbeitszeit, Lohn und Expansion. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und verifizierbarer Quelle verwendet. |
| `arbeitszeugnis-analyse` | Analyse deutscher Arbeitszeugnisse nach Ampelsystem (Rot/Orange/Grün). Geheimcodes, Schaufenster-Drift, negative Codeworte, Steigerungsadverbien. Satzweise Notenmatrix, begründete Gesamtnotenspanne. Vollständiger Mandatsablauf: Erstgespräch, Mandantenbericht, Aufforderungsschreiben, Klagestrategie. |
| `aussenwirtschaft-zoll-sanktionen` | Freistehendes Plugin für Außenwirtschaft, Sanktionen, Zoll, Exportkontrolle, BAFA, TARIC, CBAM, Verbrauchsteuer, AWV, AML/KYC und Ermittlungen. |
| `barrierefreiheit-web-checker` | Web-Barrierefreiheits-Checker für BFSG, BFSGV, BITV 2.0, EN 301 549 und WCAG: Scope, Audit, Tastatur, Screenreader, Formulare, PDFs, Erklärung, Roadmap und Abnahme. |
| `bav-strategie-konzern` | Strategische Beratung zur betrieblichen Altersversorgung in Konzernen: Pensionsmodelle alle fuenf Durchführungswege CTA Pension Buyouts Drei-Stufen-Theorie Versorgungssystem-Harmonisierung internationale Benefits Restrukturierung DB-zu-DC im Duesseldorfer Boutique-Stil. |
| `bereicherungs-und-anfechtungsrecht-pruefer` | Mechanisches Durchprüfen von Bereicherungsrecht §§ 812 ff. BGB, AnfG und Insolvenzanfechtung §§ 129-147 InsO. Mit KI-Screening von Schuldnerakten, § 135 Gesellschafterdarlehen, Bargeschäft § 142 und Verteidigung des Anfechtungsgegners. Keine Rechtsberatung. |
| `berufsrecht-ki-vertragspruefung` | Berufsrechtliche und strafrechtliche Vorprüfung von Vertraegen mit privaten Legal-AI-Anbietern. Für Anwaelte StB WP Patentanwaelte Notare. §§ 43e BRAO 62a StBerG 50a WPO 39c PAO 26a BNotO § 203 StGB. DAV-Stellungnahme. Gutachten Rückfragebrief Klauseln. |
| `betreuungsrecht` | Betreuungsrechtliche Skills für Jahresbericht, Vermögensverzeichnis, Genehmigungspflichten, Kontoanalyse und Verdachtsverträge nach BtOG und BGB. |
| `bgb-at-pruefer` | Großes Prüfplugin zum BGB Allgemeiner Teil: Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, qES, beA, § 130e ZPO, § 46h ArbGG, Anfechtung, Stellvertretung, Fristen und Verjährung. |
| `common-law-kompass` | Freistehendes Common-Law-Plugin für deutsche Wirtschaftsjuristen: UK/US-False-Friends, Vertragsbegriffe, Consideration, Suretyship, Indemnity, UCC, Precedent, Discovery und bilinguale Drafting-Reviews. |
| `corporate-kanzlei` | Corporate-Kanzlei-Plugin: Deal-Kommandocenter, Datenraum, Due Diligence, SPA/APA, Umwandlung, StaRUG, Insolvenzplan, W&I, Signing/Closing, PMI. |
| `datenschutzrecht` | DSGVO/BDSG/TDDDG – PIA/DPIA, AVV-Review, Auskunft Art. 15, Datenpanne Art. 33/34, Drittlandstransfer Art. 44 ff. inkl. US-Transfer, DPF, SCC, TIA und Behördenpaket. |
| `dsa-dma-digitalregulierung` | Digitalregulierung der EU: DSA (VO 2022/2065) und DMA (VO 2022/1925) plus Data Act DGA AI Act NIS-2 DORA CRA eIDAS 2.0 DDG P2B-VO und § 19a GWB. Gatekeeper-Schwellen VLOP-Einordnung Risikobewertung Art. 34 Forschungsdatenzugang Art. 40 Account-Sperre Art. 20-23 Zustellung Art. 13 DSA Klagewege. |
| `einfache-leichte-sprache-jura` | Juristische Texte in Einfache Sprache oder Leichte Sprache übertragen: experimentelle Standard-Annäherung, Zielgruppe klären, Rechtsinhalt sichern und Qualitätsgate nutzen. |
| `email-umformulierer-berufsrecht` | Formuliert unfreundliche, emotionale oder unsachliche E-Mails in hoefliche, sachliche und berufsrechtskonform formulierte Texte um. Fokus auf BRAO/BORA-Konformität, mit Varianten für Steuerberater, Notare und allgemeine berufliche Korrespondenz. |
| `energierecht` | Freistehendes Energierecht-Plugin für Stadtwerke, Versorger, Wärme, Netze, Vertrieb, Industrie, EEG, KWKG, Verfahren, Transaktionen und Projektfinanzierung. |
| `europarecht-kompass` | Freistehendes Europarecht-Plugin gegen deutsche Denkfehler: Vorrang, unmittelbare Wirkung, Richtlinien, Verordnungen, Charta, Grundfreiheiten, Beihilfen, Vorlageverfahren und EU-Drafting. |
| `fachanwalt-agrarrecht` | Plugin Fachanwalt für Agrarrecht. Höferecht (HöfeO Anerbenrecht Länder) Landpachtrecht BGB §§ 581 ff. GAP EU-Direktzahlungen Cross-Compliance Düngeverordnung Pflanzenschutz Tierschutz Forstrecht. Schnittstelle Plugin fachanwalt-erbrecht. |
| `fachanwalt-arbeitsrecht` | Fachanwalt-Arbeitsrecht nach FAO Paragraf 10: KSchG, BetrVG, TzBfG, AGG, EntgTranspG, Urlaub, Betriebsrat, Befristung und Vergleichspraxis. Rechtsprechung nur mit Datum, Aktenzeichen und verifizierter Quelle. |
| `fachanwalt-bank-kapitalmarktrecht` | Plugin Fachanwalt für Bank- und Kapitalmarktrecht. KWG ZAG WpHG WpIG MiFID-II MAR MiCAR Verbraucherkredit Vermögensanlage Beratungshaftung. Schnittstellen Plugin gesellschaftsrecht regulatorisches-recht. |
| `fachanwalt-bau-architektenrecht` | Plugin Fachanwalt für Bau- und Architektenrecht. BGB Werkvertrag VOB-A VOB-B VOB-C HOAI Bauordnungsrecht. Bauvertrag Maengelhaftung Abnahme Vergaberecht. Schnittstellen Plugin fachanwalt-vergaberecht kanzlei-allgemein. |
| `fachanwalt-erbrecht` | Plugin Fachanwalt für Erbrecht. BGB Erbrecht §§ 1922 ff. Pflichtteil Testament Erbschein Erbauseinandersetzung Erbschaftsteuer EU-ErbVO. Schnittstellen Plugin steuerrecht-anwalt-und-berater kanzlei-allgemein. |
| `fachanwalt-familienrecht` | Plugin Fachanwalt für Familienrecht. Orientierung Normen Mandate Fristen Literatur. Familiengericht FamFG Scheidung Sorge Umgang Unterhalt Zugewinn Ehevertrag eingetragene Lebenspartnerschaft. Ergaenzend zum Plugin kanzlei-allgemein. |
| `fachanwalt-gewerblicher-rechtsschutz` | Plugin Fachanwalt für gewerblichen Rechtsschutz nach FAO § 14k. MarkenG. DesignG. UWG. PatG GebrMG. UrhG-Bezuege. Markenanmeldung DPMA EUIPO. UWG-Abmahnung §§ 8 ff. UWG. Designverletzung. Einstweilige Verfuegung Verletzungsklage Lizenzanaloger Schadensersatz. |
| `fachanwalt-handels-gesellschaftsrecht` | Plugin Fachanwalt für Handels- und Gesellschaftsrecht nach FAO § 14i. HGB. AktG. GmbHG. PartGG. UmwG. Geschäftsführerhaftung §§ 43 GmbHG 93 AktG. Gesellschafterstreit Beschlussanfechtung. Handelsvertreterausgleich § 89b HGB. MoPeG GbR seit 2024. Schnittstellen kanzlei-allgemein. |
| `fachanwalt-insolvenz-sanierungsrecht` | Plugin Fachanwalt für Insolvenz- und Sanierungsrecht nach FAO § 14. InsO Eroeffnung Antragspflicht § 15a Gläubigerantrag § 14 InsO. StaRUG Restrukturierungsplan. Insolvenzanfechtung §§ 129 ff. InsO. Schnittstellen insolvenzrecht und steuerrecht-anwalt-und-berater. |
| `fachanwalt-internationales-wirtschaftsrecht` | Plugin Fachanwalt für Internationales Wirtschaftsrecht. CISG Bruessel Ia Rom I Rom II Schiedsverfahren ICC UNCITRAL Investitionsschutz ICSID WTO EU-Aussenhandel LkSG. Schnittstelle Plugin kanzlei-allgemein. |
| `fachanwalt-it-recht` | Plugin Fachanwalt für Informationstechnologierecht. SaaS Software-Lizenz DSGVO BDSG TTDSG TKG NIS2 DDG DSA DMA EU-KI-VO Open-Source. Schnittstellen Plugin datenschutzrecht ki-governance kanzlei-allgemein. |
| `fachanwalt-medizinrecht` | Plugin Fachanwalt für Medizinrecht. Arzthaftung §§ 630a ff. BGB Patientenrechte Vertragsarztrecht Berufsrecht Aerzte SGB V Krankenversicherung MPDG Apothekenrecht. Schnittstellen Plugin sozialrecht-kanzlei kanzlei-allgemein. |
| `fachanwalt-miet-wohnungseigentumsrecht` | Plugin Fachanwalt für Miet- und Wohnungseigentumsrecht nach FAO § 14e. BGB §§ 535 ff. Wohnraummiete und Gewerberaummiete. Mieterhoehung §§ 558 ff. Kündigung §§ 543 569 573 BGB. WEG-Beschlussanfechtung § 44 WEG. BetrKV. Schnittstellen kanzlei-allgemein. |
| `fachanwalt-migrationsrecht` | Plugin Fachanwalt für Migrationsrecht. AufenthG AsylG GFK Dublin-VO Verfahrens-RL Qualifikations-RL StAG. Einbürgerung Familiennachzug Notfrist § 36 AsylG eine Woche. Schnittstellen Plugin rechtsberatungsstelle. |
| `fachanwalt-sozialrecht` | Plugin Fachanwalt für Sozialrecht nach FAO § 11. SGB I-XII und Sozialgerichtsbarkeit SGG. Widerspruch § 84 SGG Klage § 87 SGG Eilantrag § 86b SGG. Buergergeld Erwerbsminderung GdB Pflegegrad Hilfsmittel Eingliederungshilfe. Bescheidanalyse Akteneinsicht PKH Fristenbuch. |
| `fachanwalt-sportrecht` | Plugin Fachanwalt für Sportrecht. Verbandsrecht (DFB FIFA UEFA IOC DOSB) CAS Schiedsverfahren Spielerverträge Doping WADA-Code NADA Sponsoring Persönlichkeitsrechte Veranstalterhaftung. Schnittstelle Plugin gesellschaftsrecht. |
| `fachanwalt-strafrecht` | Plugin Fachanwalt für Strafrecht. Orientierung StPO StGB Nebenstrafrecht. Strafverteidigung Ermittlungsverfahren Hauptverhandlung Revision. Nebenklage Opfervertretung Zeugenbeistand Adhaesion Insolvenzantrag StA. Ergaenzt aktenaufbereiter-strafrecht und kanzlei-allgemein. |
| `fachanwalt-transport-speditionsrecht` | Plugin Fachanwalt für Transport- und Speditionsrecht. HGB §§ 407 ff. Frachtvertrag §§ 453 ff. Spedition CMR COTIF Montrealer Übereinkommen Haager Visby Regeln ADSp. Schnittstelle Plugin kanzlei-allgemein. |
| `fachanwalt-urheber-medienrecht` | Plugin Fachanwalt für Urheber- und Medienrecht. UrhG UWG KUG Recht am eigenen Bild Presserecht Persoenlichkeitsrecht Medienstaatsvertrag. Schnittstellen Plugin gewerblicher-rechtsschutz verlagsredaktion kanzlei-allgemein. |
| `fachanwalt-vergaberecht` | Plugin Fachanwalt für Vergaberecht. GWB §§ 97 ff. VgV UVgO SektVO KonzVgV VOB-A. EU-Vergabe-RL. Nachprüfungsverfahren Vergabekammer und OLG-Vergabesenat. Schnittstelle Plugin fachanwalt-bau-architektenrecht. |
| `fachanwalt-verkehrsrecht` | Plugin Fachanwalt für Verkehrsrecht. StVG StVO PflVG VVG-Bezuege. Verkehrsunfall Personen- und Sachschaden Bußgeld Fahrerlaubnis Verkehrsstrafrecht (§§ 315c 316 StGB). Schnittstelle Plugin kanzlei-allgemein. |
| `fachanwalt-versicherungsrecht` | Plugin Fachanwalt für Versicherungsrecht. VVG VAG Berufsunfähigkeit private Krankenversicherung Lebens- und Rentenversicherung Sachversicherung Haftpflicht D-und-O. Schnittstelle Plugin kanzlei-allgemein. |
| `fachanwalt-verwaltungsrecht` | Plugin Fachanwalt für Verwaltungsrecht. VwGO VwVfG. Anfechtungs- und Verpflichtungsklage Eilrechtsschutz § 80 Abs 5 VwGO einstweilige Anordnung Normenkontrolle Polizei- und Ordnungsrecht. Schnittstelle Plugin kanzlei-allgemein. |
| `fluggastrechte` | Fluggastrechte selber geltend machen nach VO (EG) Nr. 261/2004. Tickets erfassen, Annullierung oder Verspaetung pruefen, aussergewoehnliche Umstaende, Distanz, Ausgleich, Forderungsschreiben, Mahnung und Klage. Rechtsprechung nur nach Live-Verifikation. |
| `forderungsmanagement-klagewerkstatt` | Klagewerkstatt für Forderungsmanagement mit Zuständigkeitsprüfung, Mahnvorlauf, Inkasso-Zahlungsklage und Anspruchs-Gatekeeper: Nur klare, fällige und belegte Forderungen werden zur Klage freigegeben. |
| `fortbestehensprognose` | Fortbestehensprognose § 19 Abs. 2 InsO als Geschäftsführer-Selbstdokumentation. Bilanzstatus Annahmen Plausibilisierung Zwoelf-Monats-Liquiditaet. Sanierungsbausteine Patronatserklärung Comfortletter Rangrücktritt Stundung Forderungsverzicht. IDW S 11 StaRUG. Eskalation bei negativer Prognose. |
| `geldwaeschepraevention-aml-kyc` | Freistehendes Plugin für Geldwäscheprävention, AML, KYC, GwG-Risikoanalyse, UBO, PEP, Sanktionen, FIU/goAML, Transparenzregister und Behördenverfahren. |
| `gesellschaftsgruender` | Gründungsassistent deutsche Gesellschaften (GmbH UG GbR OHG KG GmbH und Co KG PartG mbB gGmbH). Von Rechtsformwahl über Gesellschaftsvertrag und Geschäftsführervertrag bis Notar Handelsregister Gewerbeamt Finanzamt Transparenzregister. MoPeG DiRUG GwG. Kein Ersatz für Anwaltsberatung. |
| `gesellschaftsrecht` | Gesellschaftsrecht – GmbH/AG/Personengesellschaften, M&A-Due-Diligence ohne Discovery (Q&A + Datenraum), Gesellschafterbeschlüsse, HRB/HRA-Anmeldungen, Closing Checklists, Compliance-Fristen. |
| `gesellschaftsrecht-legal-english` | Didaktisches Gesellschaftsrecht — English Business Terms: Corporate Legal English fuer Big-Law-Anfaenger. Dealroom: Cap Table vs Gesellschafterliste; Term Sheet; SHA; Vesting; Drag/Tag; Liquidation Preference; Anti-Dilution; SPA; DD; Notar/HR; Multi-Format-Auswertung; Frankfurt-Startup-Akte. |
| `gewerblicher-rechtsschutz` | Gewerblicher Rechtsschutz – DPMA/EUIPO-Markenrecherche und -anmeldung, Freedom-to-Operate, Patentscreening, UWG- und Urheberrechts-Abmahnung (Versand und Reaktion), Open-Source-Compliance, IP-Klausel-Review, Schutzrechts-Fristen. |
| `grosskanzlei-corporate-ma` | Freistehendes Big-Law-Corporate/M&A-Plugin: Deal-Kommandocenter, Anfänger-/First-Year-Modus, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, UmwG/StaRUG, CP-Kalender, E-Rechnung/GoBD, PMI. |
| `hausarbeitenmacher` | Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten. Führt sokratisch durch Zivilrecht öffentliches Recht Strafrecht mit Ausfluegen in Europarecht und Rechtstheorie. Adressaten-Strategie ohne Schleimerei. Liefert keine fertigen Lösungen sondern führt zur eigenen Subsumtion. |
| `immobilienrechtspraxis` | Werkzeuge fuer immobilienrechtliche Rechtsabteilungen: musterbasierte Vertragserstellung mit Klauselschutz, Vertragspruefung gegen Playbook, Grundbuchanalyse, Sachverhaltsermittlung, Mieteranfragen, Case Management und AVV-Pruefung. Rechtsprechung nur nach Live-Verifikation. |
| `weg-hausverwaltung` | Operatives WEG- und Hausverwaltungs-Plugin fuer Beschluesse, Eigentuemerversammlung, Protokoll, Beschlusssammlung, Wirtschaftsplan, Jahresabrechnung, Hausgeld, Sonderumlage, Betriebskosten, Handwerker, bauliche Veraenderungen, Steckersolar, Wallbox, Verwalter, Beirat und Anwalt-Eskalation. |
| `insolvenzforderungsanmeldungspruefung` | Freistehendes Plugin für die Insolvenzforderungsanmeldungsprüfung: Intake, § 174 InsO, Belege, Grund, Betrag, Rang, vbuH, Nachforderungen, Tabellenimport, Prüfungstermin, Bestreiten, Feststellung, Tabellenauszug und Verteilung. |
| `insolvenzplan-starug-planwerkstatt` | Freistehendes Plugin für Insolvenzplan und StaRUG-Restrukturierungsplan: Intake, Sanierungskonzept, Vergleichsrechnung, Gruppen, Klassen, darstellender und gestaltender Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, Gericht und Planvollzug. |
| `insolvenzrecht` | Insolvenzrechtliche Skills zu Zahlungsunfähigkeit, Überschuldung, Antragspflicht und Gläubigerantrag. |
| `insolvenzverwaltung` | Freistehendes Insolvenzverwaltungs-Plugin aus Sicht von Insolvenzverwalter, Sachwalter und vorläufiger Verwaltung: Regelverfahren, Eigenverwaltung, Schutzschirm, Anfechtung, § 15b InsO, Masse, Forderungsprüfung, Insolvenzplan, StaRUG-Planwerkstatt, Gutachten, Berichte und Schlussrechnung. |
| `jurastudium` | Studium und Referendariat – Prüfungsgespräch nach AG-Tradition, Subsumtionslehre, Methodenlehre (Zivilrecht, Strafrecht, Öffentliches Recht), Rechtsgeschichte, Lernstrategien, Lösungsschemata, Gutachtenstil, Klausurkorrektur, Lernplanung. |
| `juristisches-drafting` | Juristisches Drafting in Word und Cowork: Vertragsklauseln Schriftsätze Boilerplate Haftungsbegrenzung Vertragsstrafe NDA Force Majeure AGB Klage Memos Formatvorlagen Redlines Defensive Drafting Term Sheet Bilingual DE-EN Klauselbibliothek 60 Bausteine. |
| `jveg-kostenpruefer` | Freistehender JVEG-Kostenprüfer für Zeugenentschädigung, Vorschuss, Fahrtkosten, Übernachtung, Verdienstausfall, Sachverständigen- und Dolmetscherkosten, Fristen, Festsetzung, Beschwerde und belegfeste Rechenprotokolle. |
| `kanzlei-allgemein` | Kanzlei-Allgemein-Plugin (fusioniert mit Cowork): edles Kommandocenter Mandatsannahme/GwG Klage/Replik Vertrag Rechtsprechung Handelsregister beA-Journal Rechnung UStVA Fristenbuch Timesheet RVG Versand-Vor-Check Posteingang Mandantenakte Mahnwesen Tagesbrief Geburtstage Weihnachtskarten. |
| `kanzlei-builder-hub` | Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Deployment in die Kanzleiumgebung. |
| `kartellrecht-marktabgrenzung-pruefung` | Kritische kartellrechtliche Pruefinstanz fuer Marktabgrenzungen nach Paragraf 18 GWB sowie Art. 101 und 102 AEUV: SSNIP-Test, Nachfrage- und Angebotsumstellung, raeumlicher Markt, Evidenz, Konsistenz, Red Flags und Marktbeherrschung. Rechtsprechung nur nach Live-Verifikation. |
| `ki-governance` | EU-KI-VO + DSGVO – Use-Case-Triage, KI-Inventar, AIA/DPIA, Vendor-Review, Drift-Monitoring der KI-Richtlinie. |
| `ki-richtlinie-kanzleien` | Erstellt und pflegt eine berufsrechtskonforme KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen mit Anwaelten und Syndikus-Anwaelten. Beruht auf BRAO, BORA, DSGVO, KI-Verordnung sowie BRAK- und DAV-Hinweisen. |
| `ki-vo-ai-act-pruefer` | Mechanik-Workflow zur KI-VO (EU 2024/1689): KI-System-Definition, Rollen, Risikoklassen, Hochrisiko-Diagnose, GPAI, Art. 43-Konformitätsbewertung, CE/EU-DB, Marktbeobachtung und Konformitäts-Evidence-Pack. |
| `krisenfrueherkennung-starug` | Krisenfrüherkennung und Krisenmanagement nach StaRUG: Pflicht zum 24-Monats-Frühwarnsystem nach § 1 StaRUG, § 102 StaRUG Warnpflicht der Berater, Geschäftsführerhaftung, drohende Zahlungsunfähigkeit, integrierte Planung, Restrukturierungsplan und Stabilisierungsanordnung. |
| `legistik-werkstatt` | Legistik-Werkstatt für Ministerien, Bundestag, Fraktionen/Opposition, Länder, Landtage und Normgeber. Baut Referenten- und Kabinettsentwürfe, Vorlagen aus der Mitte, Änderungs-/Entschließungsanträge, Rechtsverordnungen und Satzungen mit Begründung, Synopse, XML und Prüfpfaden. |
| `liquiditaetsplanung` | Liquiditaetsplanung nach deutschem Recht: 3-Wochen-Vorschau, 13/26/52-Wochen-Forecast, Excel-Export, Quote/Luecken-Ampel, Dokumentationspaket und Schnittstellen zu Fortbestehensprognose und Insolvenzrecht. Rechtsprechung nur nach Live-Verifikation. |
| `lobbyregister-bundestag` | Lobbyregister-Bundestag-Superplugin mit 50 geführten Skills für Registrierungspflicht, Ausnahmen, Registereintrag, Regelungsvorhaben, Stellungnahmen, Finanzdaten, Aktualisierung, Verhaltenskodex, Meldung von Verstoessen und Fristen nach LobbyRG. |
| `mandantenanfragen-assistent` | Assistent für Anwaltskanzleien zur Erstantwort auf Mandantenanfragen per E-Mail: dankt foermlich übernimmt die Anrede aus der eingehenden E-Mail nennt die telefonische Terminvergabe bittet um Sachverhalt per E-Mail oder bietet eine Telefon-Transkription mit DSGVO-Einwilligungshinweis an. |
| `markenrecht-fashion-luxus` | Markenrecht-Boutique für Luxus-Modehaeuser - DPMA/EUIPO Alicante/USPTO Lanham Act via NYC-Korrespondenz, alle Markenarten (Wort/Bild/Slogan/Sound/Duft/3D/Position/Haptik/Anti-KI), Widerspruch, Löschung, Verletzung, Produktpiraterie, Selektivvertrieb. |
| `meinungspruefer` | Meinungsprüfer für Äußerungsrecht: Meinung oder Tatsache, Beleidigung, üble Nachrede, Verleumdung, § 188 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR/EuGH, OLG-Praxis, US-Supreme-Court-Vergleich, Zivilrecht, Plattformen, Social Media, Arbeitsplatz, Schule und kommunale Machtkritik. |
| `memorandums-ersteller` | Wandelt Mandantenunterlagen in ein juristisches Memorandum mit Vier-Teile-Gliederung — Sachverhalt mit Quellenreferenz; Ein-Satz-Fragen; Ein-Satz-Antworten; rechtliche Ausführungen mit Pinpoint-Zitierung. Optional Piercing-Questions. Rechtsgebietsneutral. Alias Memorandumsmacher. |
| `methodenlehre-buergerliches-recht` | Methodenlehre und Rechtsanwendung im deutschen buergerlichen Recht aus Anwaltsperspektive. Gutachtenstil. Anspruchsgrundlagen-Reihenfolge. Auslegung Wortlaut System Historie Telos pragmatisch ohne starren Vorrang. Verfassungs- und unionsrechtskonforme Auslegung. Lueckenfuellung. Verjährung. |
| `mietrecht` | Mietrecht für Mieter und Vermieter mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitaetsstaedte. Datenerhebung Mieterhoehungs-Widerspruch Mietsenkungsverlangen Nebenkostenprüfung und Erstellung Mieteranfragen Klageentwurf zum Amtsgericht. |
| `nachbarschaftsstreit-pruefer` | Nachbarrecht und Nachbarschaftsstreit: Überbau, Überhang, Äste/Wurzeln, Grenzbaum, Zaun/Mauer/Hecke, Immissionen, Vertiefung, Notweg, Hammerschlagsrecht, Beweise, Aufforderung, Klage und Vergleich. |
| `mittelstand-corporate-ma` | Freistehendes Mittelstandsmandat-Corporate/M&A-Plugin: Deal-Kommandocenter, Aktenanlage, Datenraum, Legal DD, Tabellenreview, Liquiditätsvorschau, SPA/APA, W&I, Public M&A, Umwandlung, StaRUG/Insolvenzplan, CP-Kalender, E-Rechnung/GoBD, PMI. |
| `nda-abgleich` | Gleicht NDA-Entwurf der Gegenseite gegen eigenen Standard ab und setzt Haltelinien chirurgisch im Word-Aenderungsmodus durch. Ampelmatrix ROT/GELB/GRUEN. Ausgabe .docx mit echten Tracked Changes. Keine Absatzlöschungen, keine Klausel-Neufassungen. |
| `normenkontrolle-bauleitplanung` | Freistehendes Plugin für die Prüfung und Anfechtung von Bebauungsplänen, Flächennutzungsplänen und örtlichen Bauvorschriften nach § 47 VwGO vor BayVGH und OVG. Mandatsperspektive Antragstellervertretung. |
| `patentrecherche` | Patentrecherche für Patentanwaelte agentisch in Espacenet Google Patents DPMAregister DEPATISnet EPO Register WIPO USPTO. Stand der Technik Neuheit § 3 PatG Art. 54 EPUe erfinderische Tätigkeit § 4 PatG Art. 56 EPUe Problem-Solution-Approach FTO CPC IPC INPADOC Recherchebericht. |
| `phishing-vorfall-pruefer` | Freistehender Phishing-Vorfall-Prüfer für Online-Banking: BGB § 675u, § 675v, § 675w, pushTAN, Call-ID-Spoofing, grobe Fahrlässigkeit, Beweislast, Bankpflichten, Schlichtung und Klage. |
| `produktrecht` | Produktrechtliche Skills für Launch-Review, Impressumspflicht nach DDG und PAngV sowie UWG-Bewertungen. |
| `prozessrecht` | Prozessrechtliche Skills für Mandate, Fristen, Mahnbescheid, Eilverfahren, Vollstreckung und Schriftsätze. |
| `rechtsberatungsstelle` | Pro-Bono- und Rechtsberatungsstellen (RDG-konform): Mandantenintake, Fristenkontrolle, Übergabe am Semesterende, mandantenfreundliche Briefe. |
| `regulatorisches-recht` | Aufsichtsrecht – KWG, ZAG, WpHG, GwG, EnWG, TKG, HeilMWerbG, Umsatzsteuer-Voranmeldung, Inkasso/RDG, Regulator-Feeds, Wochendigest. |
| `schriftform-und-textform-bgb` | Formerfordernisse im deutschen Zivilrecht: Schriftform, Textform, qES, Zugang, beA/ERV und Prozessordnungen. Mit Checklisten, Dokumentation und Rechtsprechung nur nach Live-Verifikation. |
| `selbstvertreter-amtsgericht` | Selbstvertretung vor dem Amtsgericht ohne Anwalt: Anfänger-Workflow, Fristen, Zuständigkeit, §23 GVG/§511 ZPO-Grenzen, Klage/Erwiderung/Replik, Beweise, PKH, Termin, Sanity-Check, Rechtsprechungschat, Berufung. |
| `selbstvertreter-sozialgericht` | Selbstvertretung vor dem Sozialgericht ohne Anwalt: Anfänger-Workflow, Widerspruch, Klage, Eilantrag, Pflegegrad, Krankenkasse, Bürgergeld, EM-Rente, GdB, Belege, Gutachten, Kostenfreiheit, Sanity-Check, Rechtsprechungschat, Berufung. |
| `steuerrecht-anwalt-und-berater` | Steuerrecht für Anwalt (anw- FAO § 9) und Steuerberater (stb-): Einspruch Klage FG Aussenprüfung Selbstanzeige, Grundsteuer, Grunderwerbsteuer, Share Deals, Signing Closing, BWA SuSa Lohnbuchhaltung Jahresabschluss. |
| `strafbefehl-verteidiger` | Freistehendes Strafbefehls-Plugin für Verteidigung gegen Strafbefehl, Einspruch, Akteneinsicht, Tagessätze, Nebenfolgen, Pflichtverteidigung, Wiedereinsetzung, Einstellung, Zeugenstrategie und Hauptverhandlung. |
| `strafzumessung` | Strafzumessung nach deutschem Strafrecht vom Strafbefehl bis zur grossen Strafkammer. § 46 StGB Strafzumessungstatsachen Tagessatz Geldstrafe Freiheitsstrafe Bewaehrung § 56 § 49 Regelbeispiele besonders schwerer Fall Verstaendigung § 257c StPO TOA § 46a Gesamtstrafe § 55 JGG. |
| `subsumtions-pruefer` | Interaktiver Subsumtions-Workflow für deutsches Recht und Europarecht: Tatbestandsmerkmale zerlegen, Vier-Schritt-Schema anwenden, Rechtsfolgen und Einreden prüfen. Keine Rechtsberatung. |
| `tabellenreview-3d` | 3D-Tabellenreview als Wuerfel: Spaltenprompts pro Datenpunkt x Zeilenprompts pro Dokument x Arbeitsblatt-Perspektiven (Recht / Steuer / Wirtschaft) gestapelt. Massenprüfung Vertragsstapel M&A-DD Immobilien Vendor-Onboarding mit Excel-Mehrblatt Kreuzblatt-Konsistenz Audit-Trail Belegkette. |
| `umweltrecht` | Freistehendes Umweltrecht-Plugin für BImSchG, TEHG, Abfall, Wasser, Boden, Naturschutz, UIG, Verfahren, Bußgeld, Umwelt-Due-Diligence, Klimaklagen UmwRG, Lieferkettensorgfalt LkSG/CSDDD und ESG-Greenwashing/CSRD. |
| `urteilsbauer-relationsmacher` | Urteils- und Beschluss-Werkstatt für Amts- Land- und Familienrichter sowie Rechtspfleger. Aktenintake Relation Beweiswürdigung mit Richter-Input Tatbestandsmerkmale Tenor Tatbestand Entscheidungsgründe Rechtsmittelbelehrung. Erzeugt DOCX nach Paragraf 313 ZPO. |
| `verfassungsrecht` | Deutsches Verfassungsrecht unter dem Grundgesetz aus Sicht einer Spezialkanzlei. Rechtsprechungsgetrieben mit Live-Recherche auf bundesverfassungsgericht.de. Acht Skills für Gesetzgebungskompetenz formelle und materielle Verfassungsmäßigkeit Grundrechte und Verfassungsbeschwerde. |
| `verkehr-infrastrukturrecht` | Freistehendes Verkehrs- und Infrastrukturrecht-Plugin für Verkehrsplanung, Planfeststellung, Straßenbahn, Ladeinfrastruktur, Parkraum und Verkehrswende. |
| `verkehrsowi-verteidiger` | Freistehendes VerkehrsOWi-Plugin für Bußgeldbescheid, Anhörung, Einspruch, Punkte, Fahrverbot, Rotlicht, Geschwindigkeit, Abstand, Handy, Alkohol, Drogen, Akteneinsicht, Messakte, Zeugenstrategie und Amtsgericht. |
| `verlagsredaktion` | Verlagsdesk fuer juristische und fachliche Verlage: Eingangskorb, Manuskript, Redaktion, Rechtecheck, Zitate, Bildrechte, Autorenkommunikation, Heftplanung, Buchprojekte, Satzfahnen, Metadaten, Marketing und Produktionsuebergabe. |
| `vertragsausfueller` | Freistehendes Vertragsausfüller-Plugin: DOCX-Vorlagen und Altverträge strippen, Felder erkennen, Term Sheets mappen, Rückfragen führen, neue Verträge erzeugen und Track-Changes-Fassungen nur nach ausdrücklicher Nachfrage vorbereiten. |
| `vertragsrecht` | Vertragsrecht – Lieferanten- und Vertriebsverträge, AGB §§ 305 ff. BGB, NDA, SaaS-/MSA-Review, Renewal-Tracking, Eskalations-Routing, Business-Zusammenfassungen. |
| `wandeldarlehen-lebenszyklus` | Begleitet den vollständigen Lebenszyklus eines Wandeldarlehens für GmbH und UG: Vertragserstellung (bilingual/einsprachig), Beurkundungsprüfung, Wandelereignisse, Wandlungsberechnung, Cap-Table-Update, Gesellschafterbeschluss und Notar-Paket. |
| `zitierweise-deutsches-recht` | Deutsche juristische Hauszitierweise v4.0: Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und verifizierbarer Quelle; keine BeckRS-, Kommentar- oder Aufsatz-Blindzitate. Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. |
| `zwangsverwaltung-zvg` | Freistehendes ZVG-Plugin für Zwangsverwaltung und Versteigerung: Beschlagnahme, Besitz, Mieten, Treuhandkonto, Berichte, Verteilung, ZVG-Portal-Recherche, Bieterangebote und Versteigerungsteilnahme. |
| `zwangsvollstreckung` | Plugin Zwangsvollstreckung §§ 704 ff. ZPO: Mahn-/Vollstreckungsbescheid, PfÜB Bank/Arbeit, § 802l Kontensuche, Vermögensauskunft, Räumung, § 800 ZPO Notar, § 201 InsO, ZVG, EU-Kontenpfändung VO 655/2014, § 765a Härtefall, Schuldnerschutz. |

## Fallakten-Assets (63 Stück)

URL-Schema: `https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/<asset>.zip`

**Wichtig:** Diese ZIPs sind **keine Plugins**. Sie enthalten Mandatsunterlagen für Testzwecke und gehören in den Chat, nicht in den Plugin-Upload-Dialog.

| Asset | Inhalt |
| --- | --- |
| `testakte-arbeitszeugnis-analyse-bluehendes-leben.zip` | siehe `testakten/arbeitszeugnis-analyse-bluehendes-leben/` |
| `testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip` | siehe `testakten/aussenwirtschaft-zoll-sanktionen-globalmaschinen/` |
| `testakte-bav-strategie-konzern-meissner-rheinwerk-ag.zip` | siehe `testakten/bav-strategie-konzern-meissner-rheinwerk-ag/` |
| `testakte-bebauungsplan-augsburg-bahnhofsareal.zip` | siehe `testakten/bebauungsplan-augsburg-bahnhofsareal/` |
| `testakte-befristungskontrollklage-vogt-stadtwerke.zip` | siehe `testakten/befristungskontrollklage-vogt-stadtwerke/` |
| `testakte-beispielakte-edelholz-berlin.zip` | siehe `testakten/beispielakte-edelholz-berlin/` |
| `testakte-betreuung-hildegard-sauer.zip` | siehe `testakten/betreuung-hildegard-sauer/` |
| `testakte-betreuung-schmalfeld-kontodaten-vertraege.zip` | siehe `testakten/betreuung-schmalfeld-kontodaten-vertraege/` |
| `testakte-bgb-at-altfraenkische-werkstatt.zip` | siehe `testakten/bgb-at-altfraenkische-werkstatt/` |
| `testakte-bvg-widerspruchsstelle-abschleppen-mobg.zip` | siehe `testakten/bvg-widerspruchsstelle-abschleppen-mobg/` |
| `testakte-common-law-kompass-crossborder-contract.zip` | siehe `testakten/common-law-kompass-crossborder-contract/` |
| `testakte-datenschutz-us-transfer-cloudsuite-rheinmain.zip` | siehe `testakten/datenschutz-us-transfer-cloudsuite-rheinmain/` |
| `testakte-dsa-dma-bayrische-baustube-meissner.zip` | siehe `testakten/dsa-dma-bayrische-baustube-meissner/` |
| `testakte-einfache-leichte-sprache-jura-mandantenbrief.zip` | siehe `testakten/einfache-leichte-sprache-jura-mandantenbrief/` |
| `testakte-energierecht-stadtwerke-quartier.zip` | siehe `testakten/energierecht-stadtwerke-quartier/` |
| `testakte-europarecht-kompass-beihilfe-richtlinie.zip` | siehe `testakten/europarecht-kompass-beihilfe-richtlinie/` |
| `testakte-fluggastrechte-familie-braeutigam.zip` | siehe `testakten/fluggastrechte-familie-braeutigam/` |
| `testakte-fortbestehensprognose-paragrafix-gmbh.zip` | siehe `testakten/fortbestehensprognose-paragrafix-gmbh/` |
| `testakte-geldwaesche-aml-kyc-musterholding.zip` | siehe `testakten/geldwaesche-aml-kyc-musterholding/` |
| `testakte-gesellschaftsgruender-streit-roeschen-tech.zip` | siehe `testakten/gesellschaftsgruender-streit-roeschen-tech/` |
| `testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip` | siehe `testakten/gesellschaftsrecht-legal-english-frankfurt-startup/` |
| `testakte-grosskanzlei-corporate-ma-datenraum.zip` | siehe `testakten/grosskanzlei-corporate-ma-datenraum/` |
| `testakte-grunderwerbsteuer-sharedeal-closing-waldkrone.zip` | siehe `testakten/grunderwerbsteuer-sharedeal-closing-waldkrone/` |
| `testakte-grundsteuer-rosenwinkel-bescheidkette.zip` | siehe `testakten/grundsteuer-rosenwinkel-bescheidkette/` |
| `testakte-inkasso-zahlungsklage-modefuchs.zip` | siehe `testakten/inkasso-zahlungsklage-modefuchs/` |
| `testakte-insolvenzforderungsanmeldungspruefung-phoenix-solar.zip` | siehe `testakten/insolvenzforderungsanmeldungspruefung-phoenix-solar/` |
| `testakte-insolvenzplan-starug-planwerkstatt-metallbau-hansa.zip` | siehe `testakten/insolvenzplan-starug-planwerkstatt-metallbau-hansa/` |
| `testakte-insolvenzverwaltung-moebelwerk-havelberg-regelverfahren.zip` | siehe `testakten/insolvenzverwaltung-moebelwerk-havelberg-regelverfahren/` |
| `testakte-insolvenzverwaltung-nordlicht-handels-kiel.zip` | siehe `testakten/insolvenzverwaltung-nordlicht-handels-kiel/` |
| `testakte-jveg-zeugin-berger-lg-tuebingen.zip` | siehe `testakten/jveg-zeugin-berger-lg-tuebingen/` |
| `testakte-kanzlei-allgemein-alltag.zip` | siehe `testakten/kanzlei-allgemein-alltag/` |
| `testakte-ki-richtlinie-musterkanzlei.zip` | siehe `testakten/ki-richtlinie-musterkanzlei/` |
| `testakte-ki-vo-konformitaetsbescheinigung-bewerberpilot.zip` | siehe `testakten/ki-vo-konformitaetsbescheinigung-bewerberpilot/` |
| `testakte-krisenfrueherkennung-starug-vier-varianten.zip` | siehe `testakten/krisenfrueherkennung-starug-vier-varianten/` |
| `testakte-kuendigungsschutzklage-weber-techlogix.zip` | siehe `testakten/kuendigungsschutzklage-weber-techlogix/` |
| `testakte-legistik-pflichtpostfach.zip` | siehe `testakten/legistik-pflichtpostfach/` |
| `testakte-lobbyregister-buergerinitiative-waldmoor.zip` | siehe `testakten/lobbyregister-buergerinitiative-waldmoor/` |
| `testakte-lobbyregister-dublin-bank-frankfurt-branch.zip` | siehe `testakten/lobbyregister-dublin-bank-frankfurt-branch/` |
| `testakte-lobbyregister-public-affairs-agentur-wasserstoff.zip` | siehe `testakten/lobbyregister-public-affairs-agentur-wasserstoff/` |
| `testakte-lumen-studios-insolvenz-strafverfahren.zip` | siehe `testakten/lumen-studios-insolvenz-strafverfahren/` |
| `testakte-markenrecht-fashion-klotzzkette-vs-brezelmann-donauzon.zip` | siehe `testakten/markenrecht-fashion-klotzzkette-vs-brezelmann-donauzon/` |
| `testakte-meinungspruefer-grenzfaelle-alltag.zip` | siehe `testakten/meinungspruefer-grenzfaelle-alltag/` |
| `testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip` | siehe `testakten/nachbarschaftsstreit-horrorfall-rosengarten/` |
| `testakte-phishing-vorfall-mayer-sparkasse-berlin.zip` | siehe `testakten/phishing-vorfall-mayer-sparkasse-berlin/` |
| `testakte-sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger.zip` | siehe `testakten/sachverstaendigengutachten-ki-vorwurf-lg-regensburg-sieglinger/` |
| `testakte-schriftform-maklervertrag-muenchen-eheleute-haspelbeck.zip` | siehe `testakten/schriftform-maklervertrag-muenchen-eheleute-haspelbeck/` |
| `testakte-schriftform-mietkuendigung-bielefeld-online-pferdedrescher.zip` | siehe `testakten/schriftform-mietkuendigung-bielefeld-online-pferdedrescher/` |
| `testakte-selbstvertreter-amtsgericht-kuechentisch-kaufpreis.zip` | siehe `testakten/selbstvertreter-amtsgericht-kuechentisch-kaufpreis/` |
| `testakte-selbstvertreter-sozialgericht-heizkosten-eilantrag.zip` | siehe `testakten/selbstvertreter-sozialgericht-heizkosten-eilantrag/` |
| `testakte-solis-vision-x-smartglasses.zip` | siehe `testakten/solis-vision-x-smartglasses/` |
| `testakte-sozialrecht-rollstuhl-tannenberg.zip` | siehe `testakten/sozialrecht-rollstuhl-tannenberg/` |
| `testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip` | siehe `testakten/strafbefehl-ladendiebstahl-fahrerflucht/` |
| `testakte-umweltrecht-industrieanlage-genehmigung.zip` | siehe `testakten/umweltrecht-industrieanlage-genehmigung/` |
| `testakte-verkehr-infrastrukturrecht-strassenbahn-ladezonen.zip` | siehe `testakten/verkehr-infrastrukturrecht-strassenbahn-ladezonen/` |
| `testakte-verkehrsowi-rotlicht-tempo.zip` | siehe `testakten/verkehrsowi-rotlicht-tempo/` |
| `testakte-verlagsredaktion-morgenlage-fachverlag.zip` | siehe `testakten/verlagsredaktion-morgenlage-fachverlag/` |
| `testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip` | siehe `testakten/vertragsausfueller-bsag-kiosk-huckelriede/` |
| `testakte-vollstreckungsmappe-mueller-sparkasse-niederrhein.zip` | siehe `testakten/vollstreckungsmappe-mueller-sparkasse-niederrhein/` |
| `testakte-wandeldarlehen-beispielcase.zip` | siehe `testakten/wandeldarlehen-beispielcase/` |
| `testakte-weg-hausverwaltung-hohenzollernhof.zip` | siehe `testakten/weg-hausverwaltung-hohenzollernhof/` |
| `testakte-zwangsverwaltung-friedrichshoefe-berlin.zip` | siehe `testakten/zwangsverwaltung-friedrichshoefe-berlin/` |
| `testakte-zwangsverwaltung-zvg-mietshaus-parkstrasse.zip` | siehe `testakten/zwangsverwaltung-zvg-mietshaus-parkstrasse/` |
| `testakte-zwangsverwaltung-zvg-versteigerung-eppendorf-altbau.zip` | siehe `testakten/zwangsverwaltung-zvg-versteigerung-eppendorf-altbau/` |

## Manifest-Asset (1 Stück)

| Asset | Verwendung |
| --- | --- |
| `marketplace.json` | Marketplace-Manifest mit Plugin-Liste und Beschreibungen. **Kein Plugin.** |

## Asset-Anzahl pro Release

| Typ | Anzahl | Summe |
| --- | --- | --- |
| plugin | 108 | |
| fallakte | 63 | |
| manifest | 1 | |
| sammelarchiv | 3 | |
| **gesamt** | | **175** |

## Verifikation eines Release

```bash
curl -s "https://api.github.com/repos/Klotzkette/claude-fuer-deutsches-recht/releases/latest" \
  | python3 -c "import json,sys; d=json.load(sys.stdin); print('Tag:', d['tag_name']); print('Assets:', len(d['assets'])); [print(' -', a['name']) for a in d['assets']]"
```

Erwartet für `v50.6.1` und `latest`: 175 Assets, davon 108 Plugin-ZIPs, 63 Fallakten-ZIPs mit `testakte-`-Prefix, eine `marketplace.json` und drei Sammelarchive (`alle-plugins-megazip.zip`, `alle-testakten.zip`, `alles-komplettpaket.zip`).
