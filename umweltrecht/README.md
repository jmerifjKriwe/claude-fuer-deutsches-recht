# Umweltrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Umweltrecht: Industrieanlage — Genehmigung, Emissionshandel, Altlast und Transaktion** ([`testakten/umweltrecht-industrieanlage-genehmigung/`](../testakten/umweltrecht-industrieanlage-genehmigung/)).

Direkt-Download als ZIP: [testakte-umweltrecht-industrieanlage-genehmigung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-umweltrecht-industrieanlage-genehmigung.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`umweltrecht`) | [`umweltrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/umweltrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Umweltrecht: Industrieanlage — Genehmigung, Emissionshandel, Altlast und Transaktion** (`umweltrecht-industrieanlage-genehmigung`) | [Gesamt-PDF lesen](../testakten/umweltrecht-industrieanlage-genehmigung/gesamt-pdf/umweltrecht-industrieanlage-genehmigung_gesamt.pdf) | [`testakte-umweltrecht-industrieanlage-genehmigung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-umweltrecht-industrieanlage-genehmigung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Akte Umweltrecht: Industrieanlage — Genehmigung, Emissionshandel, Altlast und Transaktion** (`umweltrecht-industrieanlage-genehmigung`) | [Gesamt-PDF lesen](../testakten/umweltrecht-industrieanlage-genehmigung/gesamt-pdf/umweltrecht-industrieanlage-genehmigung_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-umweltrecht-industrieanlage-genehmigung.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->
Vollständiger Umweltrechts-Assistent für Anlagenbetreiber, Verbände, Investoren, Kommunen und öffentliche Hand: Emissionshandel, Immissionsschutz, Abfall, Wasser, Boden, Naturschutz, Umweltinformation, Verfahren, Sanktionen und Transaktionen.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn ein Anschluss an Register, Behördenportale, E-Mail, beA, Datenraum, Bank, GIS, Tabellen oder Kanzleisoftware fehlt, arbeitet es mit manuellen Uploads oder mit einem gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Eine neue Sache mit `umweltrecht-kommandocenter` starten.
3. Mandant, Ziel, Frist, Dokumente und gewünschtes Ergebnis nennen.
4. Bei fehlenden Systemanschlüssen `Simulation` sagen; das Plugin erzeugt dann realistische Testdaten und erklärt, welche echte Schnittstelle später ersetzt werden müsste.
5. Am Ende immer das Qualitätstor ausgeben lassen: offene Annahmen, Fristen, Rechenprüfung, Anlagen, Zuständigkeiten und nächste Schritte.

## Enthaltene Skills

- `umweltrecht-kommandocenter` - Umweltrecht-Kommandocenter
- `umweltrecht-emissionshandel-tehg` - Emissionshandel und TEHG
- `umweltrecht-immissionsschutz-bimschg` - Immissionsschutz und BImSchG
- `umweltrecht-stoerfall-anlagen` - Störfall, Anlagenbetrieb und Betreiberpflichten
- `umweltrecht-abfall-circular-economy` - Abfallrecht und Circular Economy
- `umweltrecht-wasser-bodenschutz` - Wasser- und Bodenschutzrecht
- `umweltrecht-naturschutz-artenschutz` - Naturschutz und Artenschutz
- `umweltrecht-umweltinformation-uig-ifg` - Umweltinformation nach UIG und IFG
- `umweltrecht-verfahren` - Umweltrechtliche Verwaltungs- und Gerichtsverfahren
- `umweltrecht-bussgeld-sanktionen` - Bußgeld, Sanktionen und Anhörung
- `umweltrecht-transaktionen-dd` - Umweltrechtliche Transaktions-Due-Diligence
- `umweltrecht-compliance-schulung` - Compliance, Beauftragte und Schulung
- `klimaklagen-verbandsklage-umwrg` - Klimaklagen, Verbandsklage UmwRG, EGMR Klima-Seniorinnen
- `lksg-csddd-lieferkettensorgfalt` - Lieferkettensorgfalt LkSG und CSDDD-Richtlinie (EU) 2024/1760
- `esg-greenwashing-csrd` - ESG-Greenwashing, CSRD-Umsetzung, ESRS, UWG-Werbung

## Vorlagen

- `assets/templates/umwelt-mandatskarte.md` - Umweltrecht-Mandatskarte
- `assets/templates/tehg-zuteilung-check.md` - TEHG-Zuteilungs- und Sanktionscheck
- `assets/templates/bimschg-genehmigungsfahrplan.md` - BImSchG-Genehmigungsfahrplan
- `assets/templates/stoerfall-anlagenmatrix.md` - Störfall- und Anlagenpflichtenmatrix
- `assets/templates/abfall-circular-matrix.md` - Abfall- und Circular-Economy-Matrix
- `assets/templates/wasser-boden-pruefplan.md` - Wasser- und Boden-Prüfplan
- `assets/templates/naturschutz-artenschutz-check.md` - Naturschutz- und Artenschutzcheck
- `assets/templates/uig-ifg-verfahren.md` - UIG/IFG-Verfahrenskarte
- `assets/templates/umweltverfahren-fristen.md` - Umwelt-Verfahrens- und Fristenplan
- `assets/templates/bussgeld-verteidigungsplan.md` - Bußgeld-Verteidigungsplan Umwelt
- `assets/templates/umwelt-dd-grid.md` - Umwelt-DD-Grid
- `assets/templates/schulung-beauftragte-plan.md` - Schulungs- und Beauftragtenplan

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen; unsichere Normen und Rechtsprechung werden als Prüfbedarf markiert.
- Zahlen, Fristen, Schwellenwerte und Zuständigkeiten werden sichtbar hergeleitet oder als Annahme gekennzeichnet.
- Ausgabe immer so, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

## Download

- Plugin-ZIP: [umweltrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/umweltrecht.zip)
- Akte: [testakte-umweltrecht-industrieanlage-genehmigung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-umweltrecht-industrieanlage-genehmigung.zip)

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Umweltrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Do... |
| `esg-greenwashing-csrd` | Workflow-Skill zu esg greenwashing csrd. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `klimaklagen-verbandsklage-umwrg` | Workflow-Skill zu klimaklagen verbandsklage umwrg. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `lksg-csddd-lieferkettensorgfalt` | Unternehmen ab 1000 Mitarbeitern muss Lieferketten-Sorgfaltspflichten nach LkSG und kuenftig CSDDD erfuellen. LkSG seit 1.1.2023 CSDDD Richtlinie 2024/1760 Phasing ab 2027. Normen LkSG §§ 3 4 8 11 24 CSDDD Art. 1 ff. Prüfraster Anwendung... |
| `spezial-abfall` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Abfall: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-bimschg` | Vertiefter Spezial-Skill im Plugin umweltrecht zu BImSchG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-boden` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Boden: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-bussgeld` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Bußgeld: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-diligence` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Diligence: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-due` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Due: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-greenwashing-csrd` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Greenwashing CSRD: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-klimaklagen` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Klimaklagen: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-klimaklagen-umwrg` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Klimaklagen UmwRG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-lieferkettensorgfalt` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Lieferkettensorgfalt: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-lieferkettensorgfalt-lksg-csddd-esg` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Lieferkettensorgfalt LkSG CSDDD ESG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-lksg` | Vertiefter Spezial-Skill im Plugin umweltrecht zu LkSG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-naturschutz` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Naturschutz: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-tehg` | Vertiefter Spezial-Skill im Plugin umweltrecht zu TEHG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-uig` | Vertiefter Spezial-Skill im Plugin umweltrecht zu UIG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-umwelt` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Umwelt: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-umweltrecht` | Vertiefter Spezial-Skill im Plugin umweltrecht zu umweltrecht: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-umwrg` | Vertiefter Spezial-Skill im Plugin umweltrecht zu UmwRG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-verfahren` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Verfahren: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-wasser` | Vertiefter Spezial-Skill im Plugin umweltrecht zu Wasser: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `umweltrecht-abfall-circular-economy` | Unternehmen oder Anlagenbetreiber hat Abfall-Frage: Abfalleigenschaft Entsorgungspflichten Nebenprodukt-Einstufung Ende der Abfalleigenschaft. Normen KrWG §§ 3 4 5 7 14 17 EU-Abfallrahmenrichtlinie 2008/98/EG LAGA. Prüfraster Abfalleigen... |
| `umweltrecht-bussgeld-sanktionen` | Unternehmen erhaelt Anhoerung oder Bußgeld-Bescheid wegen Umwelt-Ordnungswidrigkeit und will sich verteidigen. Normen OWiG §§ 55 67 68 BImSchG §§ 62 64 KrWG §§ 69 70 WHG § 103 BNatSchG §§ 69 71a Bußgeld bis 100000 EUR. Prüfraster Tatbest... |
| `umweltrecht-compliance-schulung` | Anlagenbetreiber muss Umwelt-Compliance-Schulungen und Jahresaudit-Plaene erstellen für Immissionsschutzbeauftragte Abfallverantwortliche. Normen BImSchG §§ 53-58 KrWG §§ 59 60 WHG §§ 64 65. Prüfraster Schulungspflichten Dokumentationspf... |
| `umweltrecht-emissionshandel-tehg` | Anlagenbetreiber begutachtet Zuteilungsantrag Monitoring Abgabepflicht oder wehrt DEHSt-Sanktion ab. TEHG §§ 4 5 7 8 9 26 ZuV 2020 BEHG. Abgabe bis 30. April Sanktion 100 EUR je fehlende Tonne CO2. Prüfraster Zuteilungs-Berechnung Monito... |
| `umweltrecht-immissionsschutz-bimschg` | Anlagenbetreiber oder Nachbar: BImSchG-Genehmigung beantragen anfechten oder Nachbar-Drittschutz geltend machen. BImSchG §§ 4 6 10 16 17 4. BImSchV UVPG. Normen BImSchG § 5 Abs. 1 Nr. 1 Drittschutz Rücksichtnahmegebot. Prüfraster Genehmi... |
| `umweltrecht-kommandocenter` | Umweltmandat-Einstieg: Intake Anlagenkarte Behoerdenkarte Fristen Risiken naechstes Arbeitsprodukt. Routing zu BImSchG KrWG WHG BBodSchG TEHG BNatSchG-Skills. Normen je nach Routing. Prüfraster Mandanten-Typ-Identifikation Sachgebiets-Ro... |
| `umweltrecht-naturschutz-artenschutz` | Unternehmen plant Bauvorhaben mit naturschutzrechtlichem Eingriff oder Artenschutz-Konflikt. FFH-Vertraeglichkeit Artenschutz §§ 44 45 BNatSchG Kompensationspflichten. Normen BNatSchG §§ 13-19 34-36 44-45 FFH-RL 92/43/EWG Vogelschutz-RL.... |
| `umweltrecht-stoerfall-anlagen` | Anlagenbetreiber prüft Stoerfallrelevanz betreibt Seveso-III-Anlage oder will DEHSt-Anordnung abwehren. Normen BImSchG 12. BImSchV Stoerfallverordnung Seveso-III-RL. Prüfraster Stoerfallrelevanz-Prüfung Sicherheitsbericht Betreiberpflich... |
| `umweltrecht-transaktionen-dd` | M&A-Transaktion und Anwalt prüft Umwelt-DD-Risiken im Datenraum: Genehmigungen Altlasten Emissionen Abfall Wasser Naturschutz. Normen BImSchG KrWG WHG BBodSchG TEHG Umwelthaftungsrecht. Prüfraster Red-Flags Closing-Conditions Capex-Risik... |
| `umweltrecht-umweltinformation-uig-ifg` | Buerger Verband oder Unternehmen stellt UIG/IFG-Antrag auf Umweltinformation oder wehrt Ablehnung ab. Normen UIG §§ 3 4 8 9 10 IFG §§ 1 3 5 6 9 Auskunftsfrist 1 Monat. Prüfraster Antragsrecht Ausnahmen Geheimnisschutz Drittbeteiligung Wi... |
| `umweltrecht-verfahren` | Umweltrechtssache geht in Verwaltungsgericht: Ausgangsverfahren Anhoerung Widerspruch Eil- und Klageverfahren. Normen VwGO §§ 42 43 47 80 80a 80b 113 123 VwVfG §§ 28 39 UmwRG §§ 1 2 4. Prüfraster Klagebefugnis Praeklusion Eilantrag-Groun... |
| `umweltrecht-wasser-bodenschutz` | Unternehmen beantragt WHG-Erlaubnis oder hat Altlastenverantwortung oder Bodenverunreinigung. Normen WHG §§ 8 9 10 12 57 BBodSchG §§ 4 9 10 12 24 BodSchV. Prüfraster Erlaubnis-Voraussetzungen Altlasten-Haftungskette Sanierungsverantwortl... |
| `uwr-altlasten-pruefung-spezial` | Spezialfall Altlastenpruefung: BBodSchG, Sanierungs- und Untersuchungsanordnung, Sicherungsverantwortlicher, Zustandsstoerer, Verhaltensstoerer, Eigentuemer-Haftung. Pruefraster und Mustertexte fuer Bescheid-Anfechtung. |
| `uwr-einfuehrung-rechtsquellen` | Umweltrecht einfuehrend: BImSchG, BNatSchG, WHG, KrWG, BBodSchG, USchadG, EU-IED, REACH. Pro Norm Anwendungsbereich, Aufsicht, typische Mandantenfragen. Entscheidungstabelle. |
| `uwr-emissionshandel-ets-spezial` | Spezialfall EU-Emissionshandel ETS: Anwendungsbereich, Zuteilung kostenloser Zertifikate, Berichts- und Abgabepflicht, CBAM seit 2026 fuer Importe. Pruefraster fuer Industriebetriebe und Sanktionen bei Verstoss. |
| `uwr-immissionsschutz-praxis` | Immissionsschutzrecht Praxis: § 4 BImSchG genehmigungsbeduerftige Anlagen, 4. BImSchV, Genehmigungsverfahren, Anhoerung, Einwendungen, sofortige Vollziehbarkeit. Pruefraster fuer Anlagenbetreiber und Anwohner. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin umweltrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin umweltrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin umweltrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin umweltrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin umweltrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin umweltrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin umweltrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin umweltrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin umweltrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin umweltrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
