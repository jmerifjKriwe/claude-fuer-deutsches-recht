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
| `abstimmung-anlagen-interessen-cram` | Abstimmung Anlagen Interessen Cram im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Abstimmung, Anlagen, Cram. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `darstellender-quellenkarte` | Darstellender Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `down-red-gestaltender-gruppen` | Down RED Gestaltender Gruppen im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Down, Gestaltender, Gruppen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `inso-starug-planwerkstatt-start-chronologie-fristen` | Inso Starug Planwerkstatt Start Chronologie Fristen im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Einstieg, Schnelltriage und Fallrouting im Insolvenzplan Starug, Chronologie und Belegmatrix im Plugin, Fristen- und Risikoam... |
| `insolvenzplan-intake-klassen` | Intake Klassen im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Insolvenzplan, Intake, Klassen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `insolvenzplan-starug-ips-abstimmung-mehrheiten-anlagenpaket` | IPS Abstimmung Mehrheiten Anlagenpaket im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Abstimmungsmehrheiten für Insolvenzplan nach InsO und, Pflichtanlagen für Insolvenzplan oder StaRUG-Plan, Asset-Deals im Insolvenzplan str... |
| `insolvenzplan-starug-ips-cramdown-obstruktion-datenraum-register` | IPS Cramdown Obstruktion Datenraum Register im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Obstruktionsverbot und gruppenuebergreifende, Planbegleitenden Datenraum aufbauen und Dokumentenregister, Gestaltenden Teil des Insol... |
| `insolvenzplan-starug-ips-gerichtliche-schritte-kommandocenter` | IPS Gerichtliche Schritte Kommandocenter im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Gerichtliche Verfahrensschritte für Insolvenzplan und, Insolvenzplan- oder StaRUG-Mandat starten und, Steuerliche und bilanzielle Folgen... |
| `insolvenzplan-starug-ips-minderheitenschutz-planbetroffene` | IPS Minderheitenschutz Planbetroffene im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Schlechterstellungsrisiken opponierender Beteiligter, Planbetroffene im StaRUG-Verfahren sachgerecht auswaehlen, Planvollzug nach Bestätigu... |
| `insolvenzplan-starug-ips-redteam-qualitygate-sanierungskonzept` | IPS Redteam Qualitygate Sanierungskonzept im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Insolvenzplan oder StaRUG-Plan vor Einreichung aus, Sanierungskonzept als wirtschaftliche Grundlage für, Absonderungsrechte und Drittsi... |
| `insolvenzplan-starug-planwerkstatt-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `insolvenzplan-starug-planwerkstatt-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `insolvenzplan-starug-planwerkstatt-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `insolvenzplan-starug-planwerkstatt-output-waehlen` | Output wählen im Plugin Insolvenzplan Starug Planwerkstatt: Diese Output-Weiche für Insolvenzplan Starug Planwerkstatt entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste... |
| `insolvenzplan-starug-planwerkstatt-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `insolvenzplan-starug-planwerkstatt-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `insolvenzplan-vergleichsrechnung-quote` | Vergleichsrechnung Quote im Plugin Insolvenzplan Starug Planwerkstatt: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `ips-gruppen-klassenbildung` | IPS Gruppen Klassenbildung im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Abstimmungsgruppen nach InsO und Klassen nach StaRUG, Vollständigen Insolvenzplan nach §§ 217 ff, Integrierte Planrechnung aus GuV Liquiditaet und Bil... |
| `ips-kaltstart-interview` | Insolvenzplan- oder StaRUG-Mandat durch strukturiertes Erstgespraech aufgleisen wenn Unterlagen fehlen. §§ 13 15a InsO §§ 29 42 StaRUG Antragspflichten. Prüfraster: Basisdaten Krisenursachen Gläubigerlandschaft Liquiditaetslage Sanierung... |
| `ips-stabilisierung-stakeholder` | IPS Stabilisierung Stakeholder im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret StaRUG-Stabilisierungsmassnahmen beantragen wenn, Gläubiger Banken Arbeitnehmer Lieferanten Gericht und, Vollständigen StaRUG-Restrukturierungspla... |
| `ips-verfahrenswahl-restrukturierungsplan` | IPS Verfahrenswahl Restrukturierungsplan im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Passenden Sanierungsrahmen auswaehlen und Insolvenzplan, Restrukturierungsplan, Darstellenden Teil des Insolvenzplans oder StaRUG-Plans.... |
| `ips-vergleichsrechnung-ipsplan-cram` | IPS Vergleichsrechnung Ipsplan Cram im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Vergleichsrechnung als Herzstuck des Plans erstellen, Spezialfall gruppenuebergreifender Cram-Down, Leitfaden Gruppenbildung im Insolvenz- un... |
| `ipsplan-planstruktur-prepack-plan` | Ipsplan Planstruktur Prepack Plan im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Bauleiter Planstruktur Insolvenzplan und, Spezialfall Prepack-Plan und Eigenverwaltung, Sanierungsmoderation nach § 94 StaRUG vorbereiten und.... |
| `sanierungskonzept-starug-spezial-teil` | Sanierungskonzept Starug Spezial Teil im Plugin Insolvenzplan Starug Planwerkstatt: prüft konkret Sanierungskonzept, StaRUG, Teil. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
