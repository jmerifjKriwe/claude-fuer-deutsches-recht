# Insolvenzplan- und StaRUG-Planwerkstatt

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`insolvenzplan-starug-planwerkstatt`) | [`insolvenzplan-starug-planwerkstatt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzplan-starug-planwerkstatt.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Metallbau Hansa GmbH – Insolvenzplan und StaRUG-Restrukturierung** (`insolvenzplan-starug-planwerkstatt-metallbau-hansa`) | [Gesamt-PDF lesen](../testakten/insolvenzplan-starug-planwerkstatt-metallbau-hansa/gesamt-pdf/insolvenzplan-starug-planwerkstatt-metallbau-hansa_gesamt.pdf) | [`testakte-insolvenzplan-starug-planwerkstatt-metallbau-hansa.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-insolvenzplan-starug-planwerkstatt-metallbau-hansa.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Cowork-Plugin für die Erstellung, Prüfung und Härtung von Insolvenzplänen und StaRUG-Restrukturierungsplänen. Es führt vom Kaltstart über Datenraum, Sanierungskonzept, integrierte Planung, Vergleichsrechnung, Gruppen- und Klassenbildung, darstellenden und gestaltenden Teil, Anlagen, Abstimmung, Cram-down, Minderheitenschutz, gerichtliche Schritte und Planvollzug bis zum Monitoring.

## Wofür das Plugin gedacht ist

- Insolvenzplan im Regelverfahren, in Eigenverwaltung und im Schutzschirm.
- StaRUG-Restrukturierungsplan mit Auswahl der Planbetroffenen, Gruppen, Abstimmung, gerichtlichen Instrumenten und Stabilisierung.
- Vergleichsrechnung als zentrales Entscheidungselement mit Planfall, Fortführung ohne Plan, Liquidation, Sicherheiten, Sonderaktiva und Planmehrwert.
- Sanierungskonzept, integrierte Ertrags-, Finanz- und Liquiditätsplanung sowie Maßnahmenprogramm.
- Gerichtsfeste Entwurfsarbeit mit Anlagen, Red-Team-Prüfung, Freigabeampel und Planvollzug.

## Leitprinzip

Das Plugin ist verzeihend im Intake und streng im Ergebnis. Es darf mit chaotischen Tabellen, unvollständigen OPOS-Listen, widersprüchlichen Sicherheitenangaben und unfertigen Managementannahmen starten. Es macht daraus aber keinen scheinbar fertigen Plan. Jede Annahme bleibt sichtbar, jede Zahl bekommt eine Quelle oder Warnung, jede Rechtswirkung wird auf Bestimmtheit, Vergleichsrechnung und Minderheitenschutz zurückgeführt.

## Typischer Ablauf

1. Kaltstart: Rolle, Route, Schuldnerdaten, Krise, Zielbild, Gericht, Fristen und verfügbare Unterlagen erfassen.
2. Datenraum: Jahresabschlüsse, BWA, SuSa, OPOS, Liquidität, Verträge, Sicherheiten, Personal, Steuern und Organunterlagen sortieren.
3. Sanierung: Krisenursachen, Maßnahmen, Fortführungsfähigkeit, Stakeholderbeiträge und integrierte Planung erarbeiten.
4. Vergleich: Planfall, Ohne-Plan-Szenario, Sicherheitenwerte, Sonderaktiva, Kosten, Quoten und Planmehrwert berechnen.
5. Plan bauen: Darstellender Teil, gestaltender Teil, Gruppen oder Klassen, Anlagen, Abstimmung und gerichtliche Route entwerfen.
6. Härtung: Cram-down, Minderheitenschutz, Bestätigungsrisiken, Einwände und Vollzug red-teamen.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| ips-kommandocenter | Route, Material, Risiken und nächste Ausgaben steuern. |
| ips-verfahrenswahl | Den passenden Sanierungsrahmen auswählen. |
| ips-kaltstart-interview | Aus wenigen Angaben eine belastbare Arbeitsakte machen. |
| ips-datenraum-register | Alle Planbausteine belegbar machen. |
| ips-sanierungskonzept | Das wirtschaftliche Fundament des Plans herstellen. |
| ips-integrierte-planung | Zahlen konsistent, nachvollziehbar und gerichtsfähig machen. |
| ips-vergleichsrechnung | Herzstück des Plans rechnen und erklären. |
| ips-insolvenzplan-architektur | Einen vollständigen InsO-Plan strukturieren. |
| ips-starug-plan-architektur | Einen vollständigen Restrukturierungsplan strukturieren. |
| ips-darstellender-teil | Die Entscheidungsgrundlage vollständig machen. |
| ips-gestaltender-teil | Rechtswirkungen bestimmt und vollziehbar formulieren. |
| ips-gruppen-klassenbildung | Abstimmungsarchitektur belastbar machen. |
| ips-sicherheiten-drittsicherheiten | Besicherte Positionen planfest und wertklar behandeln. |
| ips-planbetroffene-auswahl | StaRUG-Eingriffe fokussiert und begründet halten. |
| ips-abstimmung-mehrheiten | Mehrheiten vor dem Termin realistisch prüfen. |
| ips-cramdown-obstruktion | Ablehnende Gruppen gerichtsfest einordnen. |
| ips-minderheitenschutz | Opposition ernst nehmen und Planangriff vermeiden. |
| ips-anlagenpaket | Nichts einreichen, was Anlagenlücken hat. |
| ips-gerichtliche-schritte | Verfahren und Gerichtskommunikation steuern. |
| ips-stabilisierung-starug | Zeit kaufen, ohne die Planroute zu beschädigen. |
| ips-planvollzug-monitoring | Nach Bestätigung die Umsetzung führen. |
| ips-steuern-bilanz-folgen | Planwirkungen nicht an Nebenfolgen scheitern lassen. |
| ips-stakeholder-kommunikation | Akzeptanz für den Plan organisieren. |
| ips-redteam-qualitygate | Den Plan vor Gegnern und Gericht hart prüfen. |

## Grenzen

Das Plugin ersetzt keine anwaltliche, steuerliche oder betriebswirtschaftliche Endprüfung. Es ist ein Arbeits-, Strukturierungs- und Qualitätssicherungswerkzeug. Bei Planbestätigung, gerichtlicher Einreichung, steuerlichen Folgen, Organpflichten, Sicherheitenwerten, Drittsicherheiten und streitigen Gläubigerrechten verlangt es menschliche Freigabe.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ips-kaltstart-interview` | Insolvenzplan- oder StaRUG-Mandat durch strukturiertes Erstgespraech aufgleisen wenn Unterlagen fehlen. §§ 13 15a InsO §§ 29 42 StaRUG Antragspflichten. Prüfraster: Basisdaten Krisenursachen Gläubigerlandschaft Liquiditaetslage Sanierung... |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-02-ips-verfahrenswahl-bis-ips-darstellender-te` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (ips-verfahrenswahl, spezial-restrukturierungsplan-fristen-form-und-zustaendigkeit, ips-darstellender-teil) und bewahrt deren Workflo... |
| `kompendium-03-ips-gerichtliche-sch-bis-ips-steuern-bilanz-f` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (ips-gerichtliche-schritte, ips-kommandocenter, ips-steuern-bilanz-folgen) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `kompendium-04-ips-abstimmung-mehrh-bis-ips-asset-deals-im-p` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (ips-abstimmung-mehrheiten, ips-anlagenpaket, ips-asset-deals-im-plan-grundstuecke-marken-kundendaten) und bewahrt deren Workflows, N... |
| `kompendium-05-ips-cramdown-obstruk-bis-ips-gestaltender-tei` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (ips-cramdown-obstruktion, ips-datenraum-register, ips-gestaltender-teil) und bewahrt deren Workflows, Normanker, Prüfprogramme und A... |
| `kompendium-06-ips-gruppen-klassenb-bis-ips-integrierte-plan` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (ips-gruppen-klassenbildung, ips-insolvenzplan-architektur, ips-integrierte-planung) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-07-ips-minderheitenschu-bis-ips-planvollzug-moni` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (ips-minderheitenschutz, ips-planbetroffene-auswahl, ips-planvollzug-monitoring) und bewahrt deren Workflows, Normanker, Prüfprogramm... |
| `kompendium-08-ips-redteam-qualityg-bis-ips-sicherheiten-dri` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (ips-redteam-qualitygate, ips-sanierungskonzept, ips-sicherheiten-drittsicherheiten) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-09-ips-stabilisierung-s-bis-ips-starug-plan-arch` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (ips-stabilisierung-starug, ips-stakeholder-kommunikation, ips-starug-plan-architektur) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-10-ips-vergleichsrechnu-bis-ipsplan-gruppenbildu` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (ips-vergleichsrechnung, ipsplan-cram-down-spezial, ipsplan-gruppenbildung-leitfaden) und bewahrt deren Workflows, Normanker, Prüfpro... |
| `kompendium-11-ipsplan-planstruktur-bis-sanierungsmoderation` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (ipsplan-planstruktur-bauleiter, ipsplan-prepack-plan-spezial, sanierungsmoderation-94-starug) und bewahrt deren Workflows, Normanker... |
| `kompendium-12-spezial-abstimmung-i-bis-spezial-cram-formula` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-abstimmung-internationaler-bezug-und-schnittstellen, spezial-anlagen-mehrparteien-konflikt-und-interessen, spezial-cram-form... |
| `kompendium-13-spezial-down-red-tea-bis-spezial-gruppen-schr` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-down-red-team-und-qualitaetskontrolle, spezial-gestaltender-zahlen-schwellen-und-berechnung, spezial-gruppen-schriftsatz-bri... |
| `kompendium-14-spezial-insolvenzpla-bis-spezial-klassen-verh` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-insolvenzplan-erstpruefung-und-mandatsziel, spezial-intake-dokumentenmatrix-und-lueckenliste, spezial-klassen-verhandlung-ve... |
| `kompendium-15-spezial-sanierungsko-bis-spezial-teil-complia` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-sanierungskonzept-risikoampel-und-gegenargumente, spezial-starug-tatbestand-beweis-und-belege, spezial-teil-compliance-dokum... |
| `kompendium-16-spezial-vergleichsre-bis-spezial-vergleichsre` | insolvenzplan-starug-planwerkstatt: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (spezial-vergleichsrechnung-behoerden-gericht-und-registerweg) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-darstellender-livequellen-und-rechtsprechungscheck` | Darstellender: Livequellen- und Rechtsprechungscheck im Insolvenzplan und StaRUG: fachlich vertiefter Spezialskill mit Normenradar (InsO/StaRUG/Planrecht), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbre... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin insolvenzplan-starug-planwerkstatt: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin insolvenzplan-starug-planwerkstatt: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin insolvenzplan-starug-planwerkstatt: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin insolvenzplan-starug-planwerkstatt: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin insolvenzplan-starug-planwerkstatt: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin insolvenzplan-starug-planwerkstatt: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
