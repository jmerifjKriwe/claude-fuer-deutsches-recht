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
| `abstimmung-anlagen-interessen-cram` | Nutze dies, wenn Spezial Abstimmung Internationaler Bezug Und Schnittstellen, Spezial Anlagen Mehrparteien Konflikt Und Interessen, Spezial Cram Formular Portal Und Einreichung im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbei... |
| `allgemein-workflow-chronologie-fristen` | Nutze dies, wenn Allgemein, Workflow Chronologie Und Belegmatrix, Workflow Fristen Und Risikoampel im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Allgemein, Workflow Chronologie Und Belegmatr... |
| `anschluss-routing` | Nutze dies, wenn Anschluss-Routing im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Insolvenzplan Starug Planwerkstatt.; Welche Unterlagen brauchen Sie?; Welcher S... |
| `darstellender-quellenkarte` | Nutze dies, wenn Darstellender Quellenkarte im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `dokumente-intake` | Nutze dies, wenn Dokumentenintake im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `down-red-gestaltender-gruppen` | Nutze dies, wenn Spezial Down Red Team Und Qualitaetskontrolle, Spezial Gestaltender Zahlen Schwellen Und Berechnung, Spezial Gruppen Schriftsatz Brief Und Memo Bausteine im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet we... |
| `einstieg-routing` | Nutze dies, wenn Einstieg und Routing im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Insolvenzplan Starug Planwerkstatt.; Welche Unterlagen brauchen Sie?; Welche... |
| `insolvenzplan-intake-klassen` | Nutze dies, wenn Spezial Insolvenzplan Erstpruefung Und Mandatsziel, Spezial Intake Dokumentenmatrix Und Lueckenliste, Spezial Klassen Verhandlung Vergleich Und Eskalation im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet w... |
| `ips-abstimmung-ips-anlagenpaket-ips-asset` | Nutze dies, wenn Ips Abstimmung Mehrheiten, Ips Anlagenpaket, Ips Asset Deals Im Plan Grundstuecke Marken Kundendaten im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Ips Abstimmung Mehrheiten,... |
| `ips-cramdown-ips-datenraum-ips-gestaltender` | Nutze dies, wenn Ips Cramdown Obstruktion, Ips Datenraum Register, Ips Gestaltender Teil im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Ips Cramdown Obstruktion, Ips Datenraum Register, Ips G... |
| `ips-gerichtliche-ips-ips-steuern` | Nutze dies, wenn Ips Gerichtliche Schritte, Ips Kommandocenter, Ips Steuern Bilanz Folgen im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Ips Gerichtliche Schritte, Ips Kommandocenter, Ips Ste... |
| `ips-gruppen-ips-architektur-ips-integrierte` | Nutze dies, wenn Ips Gruppen Klassenbildung, Ips Insolvenzplan Architektur, Ips Integrierte Planung im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Ips Gruppen Klassenbildung, Ips Insolvenzpla... |
| `ips-ips-sanierungskonzept-ips-sicherheiten` | Nutze dies, wenn Ips Redteam Qualitygate, Ips Sanierungskonzept, Ips Sicherheiten Drittsicherheiten im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Ips Redteam Qualitygate, Ips Sanierungskonze... |
| `ips-kaltstart-interview` | Insolvenzplan- oder StaRUG-Mandat durch strukturiertes Erstgespraech aufgleisen wenn Unterlagen fehlen. §§ 13 15a InsO §§ 29 42 StaRUG Antragspflichten. Prüfraster: Basisdaten Krisenursachen Gläubigerlandschaft Liquiditaetslage Sanierung... |
| `ips-minderheitenschutz-ips-planbetroffene-ips` | Nutze dies, wenn Ips Minderheitenschutz, Ips Planbetroffene Auswahl, Ips Planvollzug Monitoring im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Ips Minderheitenschutz, Ips Planbetroffene Auswa... |
| `ips-stabilisierung-ips-stakeholder-ips-plan` | Nutze dies, wenn Ips Stabilisierung Starug, Ips Stakeholder Kommunikation, Ips Starug Plan Architektur im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Ips Stabilisierung Starug, Ips Stakeholde... |
| `ips-verfahrenswahl-restrukturierungsplan-ips` | Nutze dies, wenn Ips Verfahrenswahl, Spezial Restrukturierungsplan Fristen Form Und Zustaendigkeit, Ips Darstellender Teil im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Ips Verfahrenswahl, S... |
| `ips-vergleichsrechnung-ipsplan-cram` | Nutze dies, wenn Ips Vergleichsrechnung, Ipsplan Cram Down Spezial, Ipsplan Gruppenbildung Leitfaden im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Ips Vergleichsrechnung, Ipsplan Cram Down S... |
| `ipsplan-planstruktur-prepack-plan` | Nutze dies, wenn Ipsplan Planstruktur Bauleiter, Ipsplan Prepack Plan Spezial, Sanierungsmoderation 94 Starug im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Ipsplan Planstruktur Bauleiter, Ip... |
| `output-waehlen` | Nutze dies, wenn Output wählen im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Output wählen prüfen.; Erstelle eine Arbeitsfassung zu Output wählen.; Welche Normen und Nachweise brauche ich?. |
| `quellen-livecheck` | Nutze dies, wenn Rechtsquellen-Livecheck im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `sanierungskonzept-starug-spezial-teil` | Nutze dies, wenn Spezial Sanierungskonzept Risikoampel Und Gegenargumente, Spezial Starug Tatbestand Beweis Und Belege, Spezial Teil Compliance Dokumentation Und Akte im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden... |
| `unterlagen-luecken` | Nutze dies, wenn Unterlagen und Lücken im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `vergleichsrechnung` | Nutze dies, wenn Spezial Vergleichsrechnung Behörden Gericht Und Registerweg im Plugin Insolvenzplan Starug Planwerkstatt konkret bearbeitet werden soll. Auslöser: Bitte Spezial Vergleichsrechnung Behörden Gericht Und Registerweg prüfen.... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
