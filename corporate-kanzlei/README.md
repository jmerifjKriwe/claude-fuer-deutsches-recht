# Corporate-Kanzlei-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`corporate-kanzlei`) | [`corporate-kanzlei.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/corporate-kanzlei.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **M&A Asset Deal MedTech — VENERA/FraktoMedis Präzision (Darmstadt)** (`ma-asset-deal-medtech-volkenrath-darmstadt`) | [Gesamt-PDF lesen](../testakten/ma-asset-deal-medtech-volkenrath-darmstadt/gesamt-pdf/ma-asset-deal-medtech-volkenrath-darmstadt_gesamt.pdf) | [`testakte-ma-asset-deal-medtech-volkenrath-darmstadt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ma-asset-deal-medtech-volkenrath-darmstadt.zip) |
| **Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio** (`private-equity-buyout-schuldschein-npl-heidelberg`) | [Gesamt-PDF lesen](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf) | [`testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Technischer Plugin-Name: `corporate-kanzlei`.

Eigenständiges Corporate-Kanzlei-Plugin für große Corporate- und M&A-Mandate: Origination, Outside-in-Assessment, Datenraum, Due Diligence, Tabellenreview, Q&A, SPA/APA, Disclosure Schedules, Knowledge/Fair Disclosure, Signing, Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, Umwandlungssteuerrecht, KG/GmbH & Co. KG, StaRUG, Insolvenzplan, Distressed M&A, Board Paper, PMI, Deal-PMO, Billing und Closing Bible.

Es ist als leistungsstarker Arbeitsrahmen für erfahrene Transaktionsteams gedacht, bleibt aber freundlich genug, um jüngere Anwender Schritt für Schritt durch große Deal-Workflows zu führen.

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `corporate-kanzlei.zip` hochladen.
5. Mit einem konkreten Deal-Auftrag starten, zum Beispiel: `Starte das Corporate-M&A-Kommandocenter für diesen Datenraum.`

Wichtig: Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und optional `references/` enthalten.

## Skill-Landkarte

| Skill | Bereich | Zweck |
| --- | --- | --- |
| corporate-kanzlei-kommandocenter | Deal-Kommandocenter | Schnellstart für Corporate/M&A-Mandate. Erkennt aus einem Satz, Datenraum, Term Sheet oder Markup den passenden Deal-Workflow und erzeugt eine D... |
| corporate-kanzlei-look-and-feel | Corporate-Cowork-Look | Definiert die sichtbare Oberfläche: sehr ruhig, edel, bläulich-silbern mit warmem Orange für Entscheidungspunkte, dichte Deal-Information stat... |
| corporate-kanzlei-kaltstart | Deal-Kaltstart | Nimmt Kanzlei- und Mandantenpräferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sich... |
| corporate-kanzlei-freundlicher-copilot | Freundlicher Deal-Copilot | Führt junge Anwender verzeihend durch große Transaktionen, erkennt unausgesprochene Absichten und meldet sich kurz mit hilfreichen Hinweisen. |
| corporate-kanzlei-deal-intake | Deal-Intake | Strukturiert neue Transaktionsmandate aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message, Screenshot oder Datenraum-Einladung. |
| corporate-kanzlei-matter-file | Deal-Akte | Legt die Transaktionsakte als Matter Workspace an: Struktur, Workstreams, Datenraumspiegel, Register, Q&A, SPA, Signing, Closing und PMI. |
| corporate-kanzlei-conflict-gwg-sanctions | Konflikt-, GwG- und Sanktionscheck | Führt Annahmeprüfung für Corporate/M&A: Interessenkonflikte, wirtschaftlich Berechtigte, Sanktionen, PEP, Mittelherkunft, Sektor- und Länder-... |
| corporate-kanzlei-deal-team-staffing | Deal-Team und Staffing | Plant Workstreams, Rollen, Kapazitäten, Review-Level und Eskalationswege für große Transaktionen. |
| corporate-kanzlei-outside-in-target-screening | Outside-in Target Screening | Erstellt frühe Zielobjekt- und Pipeline-Analysen aus öffentlichen Informationen, Nachrichten, Registern, Finanzdaten und Branchenhinweisen. |
| corporate-kanzlei-teaser-im-processdocs | Teaser, IM und Prozessdokumente | Unterstützt Seller-side bei Investment Teaser, Information Memorandum, NDA, Process Letter und Bieterkommunikation. |
| corporate-kanzlei-datenraum-aufbau | Datenraum-Aufbau | Strukturiert und bestückt virtuelle Datenräume für Private M&A, Public M&A, Carve-out und Distressed-Prozesse. |
| corporate-kanzlei-datenraum-gap-clean-room | Datenraum-Gap-Analyse und Clean Room | Prüft Datenraum, Teaser, IM, IRL und Disclosure-Konzept auf Lücken, Widersprüche, Dubletten und Clean-Room-Bedarf. |
| corporate-kanzlei-due-diligence-legal | Legal Due Diligence | Führt standardisierte Legal Due Diligence mit Findings, Materiality, Quellenbelegen, Human-in-the-loop und Red-Flag-Report. |
| corporate-kanzlei-due-diligence-commercial-contracts | Kommerzielle Vertrags-DD | Prüft Kunden-, Lieferanten-, Händler-, SaaS-, Lizenz- und Materialverträge auf Change of Control, Kündigung, Exklusivität, Haftung, IP und P... |
| corporate-kanzlei-tabellenreview-3d-datenraum | 3D-Tabellenreview im Datenraum | Verbindet M&A-Datenraumprüfung mit dem Tabellenreview-3D-Ansatz: Dokumente x Datenpunkte x Perspektiven Recht/Steuer/Wirtschaft. |
| corporate-kanzlei-qa-information-requests | Q&A und Information Requests | Erzeugt und verwaltet Q&A-Prozess, Information Request Lists, Follow-ups und Antwortqualität. |
| corporate-kanzlei-expert-calls-transkripte | Expert Calls und Transkripte | Bereitet Management Presentations, Expert Calls und Transkripte für DD und SPA-Verhandlung auf. |
| corporate-kanzlei-transaktionsstruktur | Transaktionsstrukturierung | Entwickelt Strukturvarianten für Share Deal, Asset Deal, Carve-out, Joint Venture, Verschmelzung, Spaltung, Formwechsel, Roll-over und Managemen... |
| corporate-kanzlei-umwandlungsrecht | Umwandlungsrecht | Bearbeitet Verschmelzung, Spaltung, Ausgliederung, Formwechsel, Einbringung und Vorfeld-Carve-outs nach Umwandlungsrecht. |
| corporate-kanzlei-umwandlungssteuerrecht | Umwandlungssteuerrecht | Erfasst umwandlungssteuerliche Strukturfragen als Arbeitsmatrix für Steuerteam und Corporate-Team. |
| corporate-kanzlei-kg-personengesellschaften | KG und Personengesellschaften | Spezialworkflow für KG, GmbH & Co. KG, Fondsvehikel, Kommanditistenwechsel, Einlagen, Haftsumme und Register. |
| corporate-kanzlei-gesellschaftsrecht-register | Corporate Housekeeping und Register | Prüft HRB/HRA, Gesellschafterlisten, Satzungen, Beschlüsse, Vollmachten, Organstellung, Transparenzregister und Corporate Approvals. |
| corporate-kanzlei-spa-apa-entwurf | SPA/APA-Entwurf | Erstellt und strukturiert Kaufvertragsentwürfe für Share Deal und Asset Deal aus Term Sheet, DD-Findings und Transaktionsstruktur. |
| corporate-kanzlei-vertragsmarkup-key-issues | Markup und Key Issues | Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschläge nach Parteiperspektive. |
| corporate-kanzlei-disclosure-schedules | Disclosure Schedules | Leitet Disclosure Schedules aus Datenraum, DD-Findings, Q&A und SPA-Garantien ab. |
| corporate-kanzlei-fair-disclosure-knowledge | Fair Disclosure und Knowledge | Prüft Wissens-, Kenntnis-, Fair-Disclosure- und Aktenwissen-Klauseln im Lichte von KI-gestützter Datenraumprüfung. |
| corporate-kanzlei-signing-closing-conditions | Signing, Closing und CPs | Führt Signing-to-Closing: Conditions Precedent, Ordinary Course, Bring-down, Closing Deliverables, Funds Flow und Closing Bible. |
| corporate-kanzlei-regulatory-fdi-merger-control | Fusionskontrolle und Investitionskontrolle | Erstellt Freigabe-Landkarte für Kartellrecht, Fusionskontrolle, AWV/FDI, Sektorregulierung und Multi-Jurisdiction-Filings. |
| corporate-kanzlei-public-ma-kapitalmarkt-mar | Public M&A, Kapitalmarkt und MAR | Begleitet börsennotierte Transaktionen: WpUEG-Unterlagen, Ad-hoc-Prüfung, Insiderlisten, Stellungnahmen und Marktgerüchte. |
| corporate-kanzlei-wi-insurance | W&I-Versicherung | Bereitet W&I-Prozess, Underwriting, DD-Berichte, KI-DD-Transparenz und Deckungsausschlüsse vor. |
| corporate-kanzlei-restructuring-starug-insolvenzplan | StaRUG und Insolvenzplan | Unterstützt Restrukturierungsfälle: StaRUG-Plan, Insolvenzplan, Distressed M&A, Gläubigerklassen, Planbetroffenheit und Zeitplan. |
| corporate-kanzlei-distressed-ma | Distressed M&A | Führt Unternehmenskauf in Krise, vorläufiger Insolvenz, Insolvenzplan oder Asset Deal aus der Insolvenz. |
| corporate-kanzlei-post-closing-integration | Post-Closing Integration | Übersetzt DD-Findings, SPA-Pflichten und Synergieannahmen in einen PMI-Plan. |
| corporate-kanzlei-steps-plan-pmo | Deal-PMO und Steps Plan | Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing. |
| corporate-kanzlei-rechtsprechungsrecherche | Corporate-Rechtsprechungsrecherche | Sucht Rechtsprechung und amtliche Quellen für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung. |
| corporate-kanzlei-handelsregisterabruf | Handelsregister- und Registerabruf | Führt offizielle Registerabrufe für Zielgesellschaft, Verkäufer, Erwerber, Beteiligungsketten, KG und Organstellung. |
| corporate-kanzlei-datenqualitaet-xai-qualitaetskontrolle | Datenqualität und XAI-Qualitätskontrolle | Sichert KI-gestützte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab. |
| corporate-kanzlei-ki-governance-berufsrecht | KI-Governance und Berufsrecht | Prüft KI-Einsatz im Transaktionsmandat unter Mandatsgeheimnis, Need-to-know, Datenschutz, KI-VO, Dienstleistereinsatz und Mandantenfreigabe. |
| corporate-kanzlei-board-paper-business-judgment | Board Paper und Business Judgment | Erstellt Entscheidungsunterlagen für Vorstand/Geschäftsführung/Aufsichtsrat mit Informationsgrundlage, Alternativen, Risiken und KI-Einsatztra... |
| corporate-kanzlei-billing-narratives | Corporate Billing Narratives | Erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. |
| corporate-kanzlei-output-versand-signing | Output, Signing und Versand | Bereitet Transaktionsoutput vor: Markups, Issues Lists, Reports, Board Papers, Signing Packs, Closing Deliverables, beA/Notar/Email-Versand. |
| corporate-kanzlei-due-diligence-reporting | DD Reporting und Legal Fact Book | Erstellt Red-Flag-Report, Full DD Report, Legal Fact Book, Executive Summary und Issues-to-SPA-Mapping. |
| corporate-kanzlei-simulation-bidder-process | Bieterprozess-Simulation | Simuliert einen beschleunigten achtstündigen Seller-side oder Buy-side M&A-Tag mit Datenraum, Q&A, Markup, CPs und Board Call. |
| corporate-kanzlei-automation-monitoring | Automationen und Monitoring | Entwirft Monitore für Datenraum-Neuzugänge, Q&A, CP-Deadlines, Registerupdates, News, MAR-Signale und PMI-Aufgaben. |
| corporate-kanzlei-closing-bible-archiv | Closing Bible und Archiv | Erstellt Closing Bible, Versionierung, Signaturketten, Registerbelege und Deal-Archiv. |
| corporate-kanzlei-translations-multijurisdictional | Multi-Jurisdiction und Übersetzungen | Koordiniert lokale Kanzleien, Übersetzungen, Rechtsvergleich und Multi-Jurisdiction-Matrizen. |

## Typische Workflows

- Buy-side: Target Screening -> NDA -> Datenraum -> Legal DD -> Q&A -> SPA-Markup -> Signing/Closing -> PMI.
- Sell-side: Teaser/IM -> Datenraumaufbau -> Vendor DD/Fact Book -> Bieter-Q&A -> Disclosure Schedules -> Vertragsverhandlung.
- Public M&A: Insider-/MAR-Prüfung -> Angebotsunterlage/Stellungnahme -> Kapitalmarktkommunikation -> Closing-Auflagen.
- Restrukturierung: StaRUG/Insolvenzplan -> Distressed M&A -> Planvergleich -> Stakeholder- und Gerichtsschritte.
- Corporate Reorganisation: Umwandlung -> Umwandlungssteuerrecht -> Register/Notar -> Carve-out -> Closing.

## Sicherheitsleitplanken

- Keine echte Transaktionsberatung ohne menschliche Letztprüfung.
- Keine Mandatsgeheimnisse, Insiderinformationen, Datenraumzugangsdaten oder Clean-Room-Daten in nicht freigegebene Systeme.
- KI-DD immer als `KI-gestuetzt`, `stichprobenvalidiert` oder `voll menschlich validiert` kennzeichnen.
- Register-, Rechtsprechungs-, Gesetzes- und Datenraumbelege müssen verifizierbar sein.
- Public M&A, MAR, WpUEG, Kartellrecht, Investitionskontrolle, Sanktionen, StaRUG und Insolvenzreife sind rote Schwellen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Corporate Kanzlei-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan.... |
| `corporate-kanzlei-kaltstart` | Kaltstart Corporate-Kanzlei: Strukturiert den Einstieg in ein neues Corporate/M&A-Mandat mit Schnellerfassung von Parteien, Dealtyp, Phase, ersten Risiken und naechsten Schritten. Normen: BRAO §§ 43a und 49b; GwG § 10 (KYC); MAR Insider-... |
| `corporate-kanzlei-output-versand-signing` | Signing-Management und Output-Verteilung für M&A-Vertraege: Koordiniert physisches und virtuelles Signing, Signaturseiten-Protokoll, qualifizierte eSignatur (QES), Exekution und Verteilung. Normen: §§ 126 und 126a und 127 BGB (Schriftfor... |
| `kompendium-01-corporate-kanzlei-re-bis-corporate-kanzlei-sp` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 01; bündelt 2 frühere Spezialskills (corporate-kanzlei-rechtsprechungsrecherche, corporate-kanzlei-spa-apa-entwurf) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-02-corporate-kanzlei-ve-bis-corporate-kanzlei-ag` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 02; bündelt 2 frühere Spezialskills (corporate-kanzlei-vertragsmarkup-key-issues, corporate-kanzlei-agio-und-kapitalerhoehungsstruktur) und bewahrt deren Workflows, Normanker, Prüfprogra... |
| `kompendium-03-corporate-kanzlei-fa-bis-corporate-kanzlei-kg` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 03; bündelt 2 frühere Spezialskills (corporate-kanzlei-fair-disclosure-knowledge, corporate-kanzlei-kg-personengesellschaften) und bewahrt deren Workflows, Normanker, Prüfprogramme und A... |
| `kompendium-04-corporate-kanzlei-po-bis-corporate-kanzlei-um` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 04; bündelt 2 frühere Spezialskills (corporate-kanzlei-post-closing-integration, corporate-kanzlei-umwandlungssteuerrecht) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausga... |
| `kompendium-05-corporate-kanzlei-au-bis-corporate-kanzlei-bi` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 05; bündelt 2 frühere Spezialskills (corporate-kanzlei-automation-monitoring, corporate-kanzlei-billing-narratives) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-06-corporate-kanzlei-bo-bis-corporate-kanzlei-cl` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 06; bündelt 2 frühere Spezialskills (corporate-kanzlei-board-paper-business-judgment, corporate-kanzlei-closing-bible-archiv) und bewahrt deren Workflows, Normanker, Prüfprogramme und Au... |
| `kompendium-07-corporate-kanzlei-co-bis-corporate-kanzlei-da` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 07; bündelt 2 frühere Spezialskills (corporate-kanzlei-conflict-gwg-sanctions, corporate-kanzlei-datenqualitaet-xai-qualitaetskontrolle) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-08-corporate-kanzlei-da-bis-corporate-kanzlei-da` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 08; bündelt 2 frühere Spezialskills (corporate-kanzlei-datenraum-aufbau, corporate-kanzlei-datenraum-gap-clean-room) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-09-corporate-kanzlei-de-bis-corporate-kanzlei-de` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 09; bündelt 2 frühere Spezialskills (corporate-kanzlei-deal-intake, corporate-kanzlei-deal-team-staffing) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-10-corporate-kanzlei-di-bis-corporate-kanzlei-di` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 10; bündelt 2 frühere Spezialskills (corporate-kanzlei-disclosure-schedules, corporate-kanzlei-distressed-ma) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-11-corporate-kanzlei-du-bis-corporate-kanzlei-du` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 11; bündelt 2 frühere Spezialskills (corporate-kanzlei-due-diligence-commercial-contracts, corporate-kanzlei-due-diligence-legal) und bewahrt deren Workflows, Normanker, Prüfprogramme un... |
| `kompendium-12-corporate-kanzlei-du-bis-corporate-kanzlei-ex` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 12; bündelt 2 frühere Spezialskills (corporate-kanzlei-due-diligence-reporting, corporate-kanzlei-expert-calls-transkripte) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausg... |
| `kompendium-13-corporate-kanzlei-fr-bis-corporate-kanzlei-ge` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 13; bündelt 2 frühere Spezialskills (corporate-kanzlei-freundlicher-copilot, corporate-kanzlei-gesellschaftsrecht-register) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausg... |
| `kompendium-14-corporate-kanzlei-ha-bis-corporate-kanzlei-ki` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 14; bündelt 2 frühere Spezialskills (corporate-kanzlei-handelsregisterabruf, corporate-kanzlei-ki-governance-berufsrecht) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `kompendium-15-corporate-kanzlei-ko-bis-corporate-kanzlei-lm` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 15; bündelt 2 frühere Spezialskills (corporate-kanzlei-kommandocenter, corporate-kanzlei-lma-facility-und-transfer) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-16-corporate-kanzlei-lo-bis-corporate-kanzlei-ma` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 16; bündelt 2 frühere Spezialskills (corporate-kanzlei-look-and-feel, corporate-kanzlei-matter-file) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-17-corporate-kanzlei-np-bis-corporate-kanzlei-ou` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 17; bündelt 2 frühere Spezialskills (corporate-kanzlei-npl-distressed-loan-transfer, corporate-kanzlei-outside-in-target-screening) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-18-corporate-kanzlei-pu-bis-corporate-kanzlei-qa` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (corporate-kanzlei-public-ma-kapitalmarkt-mar, corporate-kanzlei-qa-information-requests) und bewahrt deren Workflows, Normanker, Prüfprogramme und Au... |
| `kompendium-19-corporate-kanzlei-re-bis-corporate-kanzlei-re` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 19; bündelt 2 frühere Spezialskills (corporate-kanzlei-regulatory-fdi-merger-control, corporate-kanzlei-restructuring-starug-insolvenzplan) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-20-corporate-kanzlei-sc-bis-corporate-kanzlei-si` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 20; bündelt 2 frühere Spezialskills (corporate-kanzlei-schuldschein-darlehen-transfer, corporate-kanzlei-signing-closing-conditions) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-21-corporate-kanzlei-si-bis-corporate-kanzlei-st` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (corporate-kanzlei-simulation-bidder-process, corporate-kanzlei-steps-plan-pmo) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-22-corporate-kanzlei-ta-bis-corporate-kanzlei-te` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (corporate-kanzlei-tabellenreview-3d-datenraum, corporate-kanzlei-teaser-im-processdocs) und bewahrt deren Workflows, Normanker, Prüfprogramme und Aus... |
| `kompendium-23-corporate-kanzlei-tr-bis-corporate-kanzlei-tr` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 23; bündelt 2 frühere Spezialskills (corporate-kanzlei-transaktionsstruktur, corporate-kanzlei-translations-multijurisdictional) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `kompendium-24-corporate-kanzlei-um-bis-corporate-kanzlei-wi` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 24; bündelt 2 frühere Spezialskills (corporate-kanzlei-umwandlungsrecht, corporate-kanzlei-wi-insurance) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-25-spezial-corporate-er-bis-v90-beirat-gmbh-zust` | corporate-kanzlei: Konsolidiertes Skill-Kompendium 25; bündelt 2 frühere Spezialskills (spezial-corporate-erstpruefung-und-mandatsziel, v90-beirat-gmbh-zustimmungskatalog-und-konfliktmatrix) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin corporate-kanzlei: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
