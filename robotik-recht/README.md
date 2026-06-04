# robotik-recht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`robotik-recht`) | [`robotik-recht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/robotik-recht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7** (`robotikrecht-roboterflotte-vellbruck-muenchen`) | [Gesamt-PDF lesen](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

> Großes Robotik-Rechtsplugin für Deutschland und EU. Es führt von der ersten Produktbeschreibung über Rollenklärung, Maschinenverordnung, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Data Act, Marktüberwachung, Rückruf, Verträge und Streitfall bis zur verwertbaren anwaltlichen Ausgabe.

## Wofür dieses Plugin gedacht ist

Robotikrecht ist keine einzelne Norm. Ein physischer Roboter verbindet Maschine, Software, KI, Sensorik, Cloud, Daten, Arbeitsschutz, Produkthaftung und Vertrag. Dieses Plugin soll genau diesen Knoten lösen: schnell genug für den Kaltstart, tief genug für Produktfreigabe, Behördenkontakt und Haftungsstreit.

Typische Fälle:

- kollaborierende Roboter in Produktion und Lager,
- mobile AMR-/AGV-Flotten in Logistik und Krankenhaus,
- Service-, Pflege-, Haushalts- und Sozialroboter,
- Medizin-, Reha- und OP-Robotik,
- Roboter mit Kamera, Mikrofon, Lidar, Biometrie, Telemetrie oder Cloudsteuerung,
- Robot-as-a-Service, Wartung, Updates, Lieferkette und Rückruf,
- Unfall, Beinaheunfall, Cybervorfall, Datenschutzbeschwerde oder Marktüberwachung.

## Arbeitsstil

Der Einstiegsskill `allgemein` fragt nicht abstrakt nach allem, sondern baut sofort eine Arbeitskarte:

1. Rolle und Produkt.
2. Zweckbestimmung und tatsächliche Nutzung.
3. physisches Sicherheitsrisiko.
4. KI- und Softwarefunktion.
5. Daten- und Cyberlage.
6. Fristen, Behörden, Unfall oder Rückruf.
7. Zieloutput.

Danach werden die passenden Spezialskills vorgeschlagen. Das Plugin ist bewusst erweiternd: Es hilft Ingenieurinnen, Inhouse-Teams und Anwältinnen, die richtige Tiefe zu finden, ohne sie in ein starres Formular zu sperren.

## Quellenhygiene

- Normen werden aus amtlichen oder frei zugänglichen Quellen geprüft: EUR-Lex, Gesetze im Internet, Recht.Bund, BAuA, EU-Kommission und Gerichtsseiten.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine BeckRS-/juris-/Kommentar-Blindzitate.
- Technische Normen und harmonisierte Standards werden nicht geraten; Fundstelle, Fassung und Anwendbarkeit live prüfen.

## Kernmodule

- **Einstieg und Workflow:** Kaltstart, Rollenmatrix, Dokumentenintake, Rechtsregime-Matrix, Fristen, Outputwahl, Red-Team.
- **Produktsicherheit:** Maschinenverordnung, MaschinenDG, ProdSG/GPSR, CE, technische Dokumentation, Anleitung, Normen, Marktüberwachung.
- **KI-VO:** Art. 3, Art. 5, Art. 6, Anhang III, Sicherheitskomponenten, Provider-/Deployerpflichten, Human Oversight, Logging, Robustheit.
- **Produkthaftung:** ProdHaftG, neue EU-Produkthaftungsrichtlinie, Fehlerbegriff, Beweislast, Updates, digitale Dienste, Betreiber-Mitverschulden.
- **Datenschutz und Cyber:** Sensorik, DSFA, Beschäftigte, Biometrie, Data Act, CRA, SBOM, Schwachstellenmeldungen, NIS2-Schnittstellen.
- **Sektoren:** Industrie, Logistik, Pflege, Medizin, Haushalt, Kinder, Agrar, Bau, Sicherheit, öffentlicher Raum, Drohnen und Dual-Use.
- **Vertrag und Streit:** RaaS, Wartung, SLA, Lieferkette, Indemnity, Versicherung, Sachverständige, Besichtigung, Rückruf, Vergleich.

## Demonstrationsakte

Die Akte `robotikrecht-roboterflotte-vellbruck-muenchen` zeigt eine verdichtete Robotiklage: Vellbruck Robotics GmbH bringt eine Cobot-/AMR-Flotte, einen Pflegepiloten und eine Cloudsteuerung in den Markt. Es gibt Unfall, Softwareupdate, Marktüberwachung, Datenschutzbeschwerde, Cyber-Schwachstelle, MDR-Nähe, Betreiberfehler, Lieferantenstreit und Versicherungsdruck. Die Akte ist als unordentlicher Datenraum angelegt und hat zusätzlich ein Gesamt-PDF.

## Pflichtdisclaimer für externe Outputs

Jede externe Ausgabe soll knapp klarstellen: KI-gestützte Vorprüfung; keine amtliche Konformitätsbewertung; technische und regulatorische Bewertung hängen von vollständigen Unterlagen, aktuellem Normenstand und Live-Quellenprüfung ab.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Robotik-Recht-Kompass für Deutschland und EU: Einstieg, Rollenklärung, Produktklassifizierung, Maschinenverordnung, KI-VO, Produkthaftung, Datenschutz, Cybersecurity, Marktüberwachung und passende Spezialskills. |
| `kompendium-01-workflow-arbeitswelt-bis-workflow-ce-akte-und` | robotik-recht: Konsolidiertes Skill-Kompendium 01; bündelt 6 frühere Spezialskills (workflow-arbeitswelt-cobot-check, workflow-beschaffung-oeffentlich-privat, workflow-betreiberpflichten-und-training, workflow-beweismatrix-und-logauswert... |
| `kompendium-02-workflow-datenschutz-bis-workflow-internation` | robotik-recht: Konsolidiertes Skill-Kompendium 02; bündelt 6 frühere Spezialskills (workflow-datenschutz-cyber-intake, workflow-first-year-associate-robotik, workflow-fristen-und-uebergangsrecht, workflow-haftungsampel, workflow-ingenieu... |
| `kompendium-03-workflow-ki-vo-integ-bis-workflow-normen-und` | robotik-recht: Konsolidiertes Skill-Kompendium 03; bündelt 6 frühere Spezialskills (workflow-ki-vo-integrationscheck, workflow-laienmodus-robotikrecht, workflow-litigation-vorbereitung, workflow-marktueberwachung-dialog, workflow-mdr-und... |
| `kompendium-04-workflow-open-source-bis-workflow-rechtsregim` | robotik-recht: Konsolidiertes Skill-Kompendium 04; bündelt 6 frühere Spezialskills (workflow-open-source-und-sbom, workflow-post-market-monitoring, workflow-presse-und-krisenkommunikation, workflow-privacy-by-design-sprint, workflow-prod... |
| `kompendium-05-workflow-risikoklass-bis-workflow-update-und` | robotik-recht: Konsolidiertes Skill-Kompendium 05; bündelt 6 frühere Spezialskills (workflow-risikoklassifizierung-schnelltest, workflow-rueckruf-und-field-action, workflow-sachverstaendigenbriefing, workflow-security-by-design-sprint, w... |
| `kompendium-06-workflow-versicherun-bis-beweislast-und-offen` | robotik-recht: Konsolidiertes Skill-Kompendium 06; bündelt 6 frühere Spezialskills (workflow-versicherungs-und-regressakte, workflow-vertrags-und-lieferkettenintake, workflow-zweckbestimmung-und-usecase, robot-as-a-service-vertrag, wartu... |
| `kompendium-07-datenverlust-und-dig-bis-lager-und-intralogis` | robotik-recht: Konsolidiertes Skill-Kompendium 07; bündelt 6 frühere Spezialskills (datenverlust-und-digitaler-schaden, deliktische-haftung-paragraph-823-bgb, haftung-arzt-klinik-hersteller, schadensberechnung-produktionsausfall, cra-pro... |
| `kompendium-08-qualitaetsmanagement-bis-autonome-lieferrobot` | robotik-recht: Konsolidiertes Skill-Kompendium 08; bündelt 6 frühere Spezialskills (qualitaetsmanagement-robotikhersteller, accuracy-robustness-cybersecurity-ai, agile-entwicklung-und-compliance-gates, anwaltliche-quellenhygiene-robotik,... |
| `kompendium-09-barrierefreiheit-und-bis-betriebsanleitung-sp` | robotik-recht: Konsolidiertes Skill-Kompendium 09; bündelt 6 frühere Spezialskills (barrierefreiheit-und-inklusion-robotik, batterie-ladeinfrastruktur-und-brandschutz, bau-und-inspektionsroboter, beschaeftigtendatenschutz-cobot, betreibe... |
| `kompendium-10-biometrie-emotion-un-bis-datensatzqualitaet-u` | robotik-recht: Konsolidiertes Skill-Kompendium 10; bündelt 6 frühere Spezialskills (biometrie-emotion-und-personenerkennung, ce-zeichen-fehlgebrauch-und-abmahnung, chirurgie-und-op-robotik, data-act-roboterdaten, datenminimierung-edge-cl... |
| `kompendium-11-datenschutz-kameras-bis-eu-de-umsetzung-und` | robotik-recht: Konsolidiertes Skill-Kompendium 11; bündelt 6 frühere Spezialskills (datenschutz-kameras-und-sensorik, digitaler-zwilling-und-simulation, dronen-und-robotik-schnittstelle, dsfa-fuer-robotik, dual-use-und-militaerische-robo... |
| `kompendium-12-eu-konformitaetserkl-bis-grundrechte-und-psyc` | robotik-recht: Konsolidiertes Skill-Kompendium 12; bündelt 6 frühere Spezialskills (eu-konformitaetserklaerung-und-einbauerklaerung, foss-und-open-source-komponenten, foundation-model-und-gpai-im-roboter, funkanlagen-und-konnektivitaet,... |
| `kompendium-13-harmonisierte-normen-bis-ki-vo-artikel-3-ki-s` | robotik-recht: Konsolidiertes Skill-Kompendium 13; bündelt 6 frühere Spezialskills (harmonisierte-normen-iso-ts-15066, human-oversight-in-physischer-robotik, importeur-haendler-fulfilment-robotik, ki-training-mit-roboterdaten, ki-vo-anha... |
| `kompendium-14-ki-vo-artikel-6-hoch-bis-kollaborierende-robo` | robotik-recht: Konsolidiertes Skill-Kompendium 14; bündelt 6 frühere Spezialskills (ki-vo-artikel-6-hochrisiko-robotik, ki-vo-deployer-pflichten-robotik, ki-vo-provider-qms-und-risk-management, ki-vo-verbotene-praktiken-robotik, klinisch... |
| `kompendium-15-kommunal-und-behoerd-bis-lieferantenregress-u` | robotik-recht: Konsolidiertes Skill-Kompendium 15; bündelt 6 frühere Spezialskills (kommunal-und-behoerdenrobotik, konformitaetsbescheinigung-robotik-ki, konformitaetsbewertung-modulwahl, landwirtschaftsroboter-und-autonome-feldtechnik,... |
| `kompendium-16-logging-und-traceabi-bis-mitbestimmung-betrie` | robotik-recht: Konsolidiertes Skill-Kompendium 16; bündelt 6 frühere Spezialskills (logging-und-traceability-robotik, marktueberwachung-unterlagenvorlage, maschine-oder-unvollstaendige-maschine, maschinenverordnung-annex-iii-hochrisiko,... |
| `kompendium-17-mobile-roboter-amr-a-bis-prodhaftg-und-neue-p` | robotik-recht: Konsolidiertes Skill-Kompendium 17; bündelt 6 frühere Spezialskills (mobile-roboter-amr-agv, nis2-betreiber-kritische-sektoren, patientenaufklaerung-robotik, pflege-und-assistenzroboter, pilotbetrieb-und-beta-robotik und 1... |
| `kompendium-18-produktakte-gap-anal-bis-quasihersteller-priv` | robotik-recht: Konsolidiertes Skill-Kompendium 18; bündelt 6 frühere Spezialskills (produktakte-gap-analyse, produktbeobachtung-und-field-data, produktfehler-verbrauchererwartung-robotik, produktsicherheit-vs-betriebssicherheit, produkts... |
| `kompendium-19-rehabilitations-und-bis-safety-gate-und-oeff` | robotik-recht: Konsolidiertes Skill-Kompendium 19; bündelt 6 frühere Spezialskills (rehabilitations-und-exoskelett-robotik, remote-update-und-secure-channel, risikobeurteilung-en-iso-12100, rollen-hersteller-anbieter-integrator, rueckruf... |
| `kompendium-20-sbom-und-cyber-dokum-bis-softwareupdate-als-p` | robotik-recht: Konsolidiertes Skill-Kompendium 20; bündelt 6 frühere Spezialskills (sbom-und-cyber-dokumentation, serviceroboter-haushalt-gpsr, sicherheits-und-ueberwachungsroboter, sicherheitskomponente-mit-ki, smart-factory-und-industr... |
| `kompendium-21-sozialer-humanoider-bis-testdaten-und-validi` | robotik-recht: Konsolidiertes Skill-Kompendium 21; bündelt 6 frühere Spezialskills (sozialer-humanoider-roboter, spielzeug-und-kinderroboter, strom-emv-und-niederspannung, systemintegrator-als-hersteller, technische-besichtigung-und-gehe... |
| `kompendium-22-transparenz-und-nutz-bis-versicherungsdeckung` | robotik-recht: Konsolidiertes Skill-Kompendium 22; bündelt 6 frühere Spezialskills (transparenz-und-nutzerinformation, unfallanalyse-chain-of-custody, vergaberecht-robotik-beschaffung, vergleich-und-sanierung-nach-incident, vernunftigerw... |
| `kompendium-23-vigilanz-medizinrobo-bis-zweckbestimmung-enge` | robotik-recht: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (vigilanz-medizinrobotik, vulnerability-disclosure-und-reporting, wesentliche-veraenderung-digital, zweckbestimmung-enge-nutzungsbedingungen) und bewahrt... |
| `workflow-abschlussqualitaet-und-redteam` | Red-Team-Check für jedes Ergebnis: Normenstand, Quellen, fehlende Tatsachen, Gegenargumente, technische Annahmen, Datenschutz und Haftungsfolgen. |
| `workflow-anschluss-skills-router` | Schlägt nach jeder Robotikprüfung passende Anschlussplugins vor: KI-VO, Datenschutz, IT-Recht, Arbeitsrecht, Medizinrecht, Produkthaftung, Vertragsrecht und Prozess. |
| `workflow-dokumentenintake-datenraum` | Liest Robotik-Datenräume mit Anleitungen, CE-Unterlagen, Risikobeurteilung, Logs, Verträgen, Incident Reports und ordnet die nächsten Prüfschritte. |
| `workflow-gutachten-memo-output` | Wählt den passenden Output: Kurzvermerk, Vorstandsvorlage, Gutachten, Behördenantwort, Rückrufplan, Vertragsredline, Klageskizze oder Counsel-Briefing. |
| `workflow-human-robot-interaction-redteam` | Prüft besondere Mensch-Roboter-Interaktion: Nähe, Vertrauen, Manipulation, psychische Belastung, vulnerable Nutzer und klare Grenzen. |
| `workflow-kaltstart-und-routing` | Kaltstart für jedes Robotikmandat: sortiert Produkt, Rolle, Ziel, Frist, Risiko, Rechtsregime und schlägt sofort die passenden Skills im Robotik-Recht-Plugin vor. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
