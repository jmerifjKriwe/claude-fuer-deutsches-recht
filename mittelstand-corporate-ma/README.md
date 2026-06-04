# Mittelständische Kanzlei – Corporate/M&A-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`mittelstand-corporate-ma`) | [`mittelstand-corporate-ma.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mittelstand-corporate-ma.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Share Deal Pellbach Werkzeugbau GmbH & Co. KG — Familiennachfolge mit PE-Beteiligung, Earn-Out, MAC** (`share-deal-familienunternehmen-pellbach-werkzeugbau-passau-nachfolge`) | [Gesamt-PDF lesen](../testakten/share-deal-familienunternehmen-pellbach-werkzeugbau-passau-nachfolge/gesamt-pdf/share-deal-familienunternehmen-pellbach-werkzeugbau-passau-nachfolge_gesamt.pdf) | [`testakte-share-deal-familienunternehmen-pellbach-werkzeugbau-passau-nachfolge.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-share-deal-familienunternehmen-pellbach-werkzeugbau-passau-nachfolge.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Technischer Plugin-Name: `mittelstand-corporate-ma`.

Dies ist das freistehende Corporate/M&A-Plugin für mittelständische Kanzleien für den gesamten Transaktionslebenszyklus: Intake, Aktenanlage, Konflikt-/GwG-/Sanktionscheck, Datenraum, Due Diligence, Tabellenreview, Liquiditätsvorschau, Insolvenzreife, Q&A, SPA/APA, Disclosure Schedules, Signing, Closing, W&I, Public M&A, Fusionskontrolle, Investitionskontrolle, Umwandlungsrecht, Umwandlungssteuerrecht, KG/GmbH & Co. KG, StaRUG, Insolvenzplan, Distressed M&A, Board Paper, PMI, Deal-PMO, Billing, XRechnung/ZUGFeRD-Vorbereitung, GoBD-Protokoll und Closing Bible.

**Wichtig:** Dieses Plugin funktioniert vollständig allein. Alle Kernabläufe, Hilfstabellen, Prüfungsschablonen und Workflows liegen im Plugin selbst; für die hier beschriebenen M&A-Workflows ist keine Zusatzinstallation nötig.

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `mittelstand-corporate-ma.zip` hochladen.
5. Mit einem konkreten Deal-Auftrag starten, zum Beispiel: `Starte das Corporate-M&A-Kommandocenter für diesen Datenraum.`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` enthalten.

## Freistehende Kernmodule

| Modul | Enthaltene Funktion |
| --- | --- |
| Aktenanlage | Deal-Akte, Aktenzeichen, Parteienregister, Ordnerplan, Datenraumspiegel, Closing-Bible-Grundgerüst. |
| Tabellenreview | Interner Review-Würfel für Dokumente, Datenpunkte, Tabellen, Formeln und Perspektiven. |
| Liquiditätsvorschau | 3-Wochen-Prüfung, 13-Wochen-Cash-Bridge, Runway, OPOS, Bankdaten, Distressed-M&A-Ampel. |
| Insolvenzreife | § 17, § 18, § 19 InsO, § 15a InsO, StaRUG-Frühwarnung, Deal-Auswirkungen und Senior-Review-Gate. |
| Fristen/CP | Signing, Closing, Q&A, Regulatory, Register, Board, Ordinary Course, Long Stop Date und PMI. |
| Billing/E-Rechnung | Narratives, Workstream-Rechnung, GoBD-Protokoll, XRechnung-Datenblock, ZUGFeRD-Prüfpaket. |
| Schreibcanvas | Freundlicher Qualitätsbegleiter für SPA, DD-Report, Board Paper, Registertext und Mandatskommunikation. |

## Skill-Landkarte

| Skill | Zweck |
| --- | --- |
| `mittelstand-corporate-ma-automation-monitoring` | Automationen und Monitoring: Entwirft Monitore für Datenraum-Neuzugänge, Q&A, CP-Deadlines, Registerupdates, News, MAR-Signale und PMI-Aufgaben. |
| `mittelstand-corporate-ma-billing-narratives` | Mittelstandsmandat Billing Narratives: erstellt deal-taugliche Time Narratives, Phasenbudgets, Workstream-Rechnungen, Cap/Success-Fee-Hinweise und Matter-Controlling. |
| `mittelstand-corporate-ma-board-paper-business-judgment` | Board Paper und Business Judgment: Erstellt Entscheidungsunterlagen für Vorstand/Geschäftsführung/Aufsichtsrat mit Informationsgrundlage, Alternativen, Risiken und KI-Einsatztransparenz. |
| `mittelstand-corporate-ma-closing-bible-archiv` | Closing Bible und Archiv: Erstellt Closing Bible, Versionierung, Signaturketten, Registerbelege und Deal-Archiv. |
| `mittelstand-corporate-ma-conflict-gwg-sanctions` | Konflikt-, GwG- und Sanktionscheck: Führt Annahmeprüfung für Corporate/M&A: Interessenkonflikte, wirtschaftlich Berechtigte, Sanktionen, PEP, Mittelherkunft, Sektor- und Länder-Risiken. |
| `mittelstand-corporate-ma-datenqualitaet-xai-qualitaetskontrolle` | Datenqualität und XAI-Qualitätskontrolle: Sichert KI-gestützte M&A-Arbeit gegen Halluzination, Bias, Black-Box-Probleme und schlechte Datenqualität ab. |
| `mittelstand-corporate-ma-datenraum-aufbau` | Datenraum-Aufbau: Strukturiert und bestückt virtuelle Datenräume für Private M&A, Public M&A, Carve-out und Distressed-Prozesse. |
| `mittelstand-corporate-ma-datenraum-gap-clean-room` | Datenraum-Gap-Analyse und Clean Room: Prüft Datenraum, Teaser, IM, IRL und Disclosure-Konzept auf Lücken, Widersprüche, Dubletten und Clean-Room-Bedarf. |
| `mittelstand-corporate-ma-deal-intake` | Deal-Intake: Strukturiert neue Transaktionsmandate aus E-Mail, Teaser, NDA, Term Sheet, Teams-Message, Screenshot oder Datenraum-Einladung. |
| `mittelstand-corporate-ma-deal-team-staffing` | Deal-Team und Staffing: Plant Workstreams, Rollen, Kapazitäten, Review-Level und Eskalationswege für große Transaktionen. |
| `mittelstand-corporate-ma-disclosure-schedules` | Disclosure Schedules: Leitet Disclosure Schedules aus Datenraum, DD-Findings, Q&A und SPA-Garantien ab. |
| `mittelstand-corporate-ma-distressed-ma` | Distressed M&A: führt Unternehmenskauf in Krise, vorläufiger Insolvenz, StaRUG, Insolvenzplan oder Asset Deal aus der Insolvenz mit Liquiditäts- und Closing-Fokus. |
| `mittelstand-corporate-ma-due-diligence-commercial-contracts` | Kommerzielle Vertrags-DD: Prüft Kunden-, Lieferanten-, Händler-, SaaS-, Lizenz- und Materialverträge auf Change of Control, Kündigung, Exklusivität, Haftung, IP und Preisrisiken. |
| `mittelstand-corporate-ma-due-diligence-legal` | Legal Due Diligence: Führt standardisierte Legal Due Diligence mit Findings, Materiality, Quellenbelegen, Human-in-the-loop und Red-Flag-Report. |
| `mittelstand-corporate-ma-due-diligence-reporting` | DD Reporting und Legal Fact Book: Erstellt Red-Flag-Report, Full DD Report, Legal Fact Book, Executive Summary und Issues-to-SPA-Mapping. |
| `mittelstand-corporate-ma-expert-calls-transkripte` | Expert Calls und Transkripte: Bereitet Management Presentations, Expert Calls und Transkripte für DD und SPA-Verhandlung auf. |
| `mittelstand-corporate-ma-fair-disclosure-knowledge` | Fair Disclosure und Knowledge: Prüft Wissens-, Kenntnis-, Fair-Disclosure- und Aktenwissen-Klauseln im Lichte von KI-gestützter Datenraumprüfung. |
| `mittelstand-corporate-ma-freundlicher-copilot` | Freundlicher Deal-Copilot: Führt junge Anwender verzeihend durch große Transaktionen, erkennt unausgesprochene Absichten und meldet sich kurz mit hilfreichen Hinweisen. |
| `mittelstand-corporate-ma-gesellschaftsrecht-register` | Corporate Housekeeping und Register: Prüft HRB/HRA, Gesellschafterlisten, Satzungen, Beschlüsse, Vollmachten, Organstellung, Transparenzregister und Corporate Approvals. |
| `mittelstand-corporate-ma-handelsregisterabruf` | Handelsregister- und Registerabruf: Führt offizielle Registerabrufe für Zielgesellschaft, Verkäufer, Erwerber, Beteiligungsketten, KG und Organstellung. |
| `mittelstand-corporate-ma-kaltstart` | Deal-Kaltstart: Nimmt Kanzlei- und Mandantenpräferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sicherheitsregeln. |
| `mittelstand-corporate-ma-kg-personengesellschaften` | KG und Personengesellschaften: Spezialworkflow für KG, GmbH & Co. KG, Fondsvehikel, Kommanditistenwechsel, Einlagen, Haftsumme und Register. |
| `mittelstand-corporate-ma-ki-governance-berufsrecht` | KI-Governance und Berufsrecht: Prüft KI-Einsatz im Transaktionsmandat unter Mandatsgeheimnis, Need-to-know, Datenschutz, KI-VO, Dienstleistereinsatz und Mandantenfreigabe. |
| `mittelstand-corporate-ma-kommandocenter` | Deal-Kommandocenter: Schnellstart für Corporate/M&A-Mandate. Erkennt aus einem Satz, Datenraum, Term Sheet oder Markup den passenden Deal-Workflow und erzeugt Deal-Karte, Ampel, Rollen und nächste Aktion. |
| `mittelstand-corporate-ma-look-and-feel` | Corporate-Cowork-Look: Definiert die sichtbare Oberfläche: sehr ruhig, edel, bläulich-silbern mit warmem Orange für Entscheidungspunkte, dichte Deal-Information statt Marketing. |
| `mittelstand-corporate-ma-matter-file` | Deal-Akte: Legt die Transaktionsakte als Matter Workspace an: Struktur, Workstreams, Datenraumspiegel, Register, Q&A, SPA, Signing, Closing und PMI. |
| `mittelstand-corporate-ma-output-versand-signing` | Output, Signing und Versand: Bereitet Transaktionsoutput vor: Markups, Issues Lists, Reports, Board Papers, Signing Packs, Closing Deliverables, beA/Notar/Email-Versand. |
| `mittelstand-corporate-ma-outside-in-target-screening` | Outside-in Target Screening: Erstellt frühe Zielobjekt- und Pipeline-Analysen aus öffentlichen Informationen, Nachrichten, Registern, Finanzdaten und Branchenhinweisen. |
| `mittelstand-corporate-ma-post-closing-integration` | Post-Closing Integration: Übersetzt DD-Findings, SPA-Pflichten und Synergieannahmen in einen PMI-Plan. |
| `mittelstand-corporate-ma-public-ma-kapitalmarkt-mar` | Public M&A, Kapitalmarkt und MAR: Begleitet börsennotierte Transaktionen: WpUEG-Unterlagen, Ad-hoc-Prüfung, Insiderlisten, Stellungnahmen und Marktgerüchte. |
| `mittelstand-corporate-ma-qa-information-requests` | Q&A und Information Requests: Erzeugt und verwaltet Q&A-Prozess, Information Request Lists, Follow-ups und Antwortqualität. |
| `mittelstand-corporate-ma-rechtsprechungsrecherche` | Corporate-Rechtsprechungsrecherche: Sucht Rechtsprechung und amtliche Quellen für Corporate/M&A, Umwandlung, Organpflichten, Kapitalmarkt, Insolvenz und Restrukturierung. |
| `mittelstand-corporate-ma-regulatory-fdi-merger-control` | Fusionskontrolle und Investitionskontrolle: Erstellt Freigabe-Landkarte für Kartellrecht, Fusionskontrolle, AWV/FDI, Sektorregulierung und Multi-Jurisdiction-Filings. |
| `mittelstand-corporate-ma-restructuring-starug-insolvenzplan` | StaRUG und Insolvenzplan: unterstützt Restrukturierungsfälle mit Planoptionen, Gläubigerklassen, Liquiditätsprüfung, Antragspflichten, Distressed M&A und Zeitplan. |
| `mittelstand-corporate-ma-signing-closing-conditions` | Signing, Closing und CPs: Führt Signing-to-Closing: Conditions Precedent, Ordinary Course, Bring-down, Closing Deliverables, Funds Flow und Closing Bible. |
| `mittelstand-corporate-ma-simulation-bidder-process` | Bieterprozess-Simulation: Simuliert einen beschleunigten achtstündigen Seller-side oder Buy-side M&A-Tag mit Datenraum, Q&A, Markup, CPs und Board Call. |
| `mittelstand-corporate-ma-spa-apa-entwurf` | SPA/APA-Entwurf: Erstellt und strukturiert Kaufvertragsentwürfe für Share Deal und Asset Deal aus Term Sheet, DD-Findings und Transaktionsstruktur. |
| `mittelstand-corporate-ma-steps-plan-pmo` | Deal-PMO und Steps Plan: Extrahiert aus Verträgen, DD und Gremienunterlagen konkrete Steps Plans für Pre-Signing, Signing-to-Closing und Post-Closing. |
| `mittelstand-corporate-ma-tabellenreview-3d-datenraum` | 3D-Tabellenreview im Datenraum: verbindet M&A-Datenraumprüfung mit interner Review-Matrix für Dokumente, Datenpunkte und Perspektiven Recht/Steuer/Wirtschaft. |
| `mittelstand-corporate-ma-teaser-im-processdocs` | Teaser, IM und Prozessdokumente: Unterstützt Seller-side bei Investment Teaser, Information Memorandum, NDA, Process Letter und Bieterkommunikation. |
| `mittelstand-corporate-ma-transaktionsstruktur` | Transaktionsstrukturierung: Entwickelt Strukturvarianten für Share Deal, Asset Deal, Carve-out, Joint Venture, Verschmelzung, Spaltung, Formwechsel, Roll-over und Managementbeteiligung. |
| `mittelstand-corporate-ma-translations-multijurisdictional` | Multi-Jurisdiction und Übersetzungen: Koordiniert lokale Kanzleien, Übersetzungen, Rechtsvergleich und Multi-Jurisdiction-Matrizen. |
| `mittelstand-corporate-ma-umwandlungsrecht` | Umwandlungsrecht: Bearbeitet Verschmelzung, Spaltung, Ausgliederung, Formwechsel, Einbringung und Vorfeld-Carve-outs nach Umwandlungsrecht. |
| `mittelstand-corporate-ma-umwandlungssteuerrecht` | Umwandlungssteuerrecht: Erfasst umwandlungssteuerliche Strukturfragen als Arbeitsmatrix für Steuerteam und Corporate-Team. |
| `mittelstand-corporate-ma-vertragsmarkup-key-issues` | Markup und Key Issues: Analysiert SPA/APA/NDA/Process-Letter-Markups, erstellt Key Issues Lists und Gegenmarkup-Vorschläge nach Parteiperspektive. |
| `mittelstand-corporate-ma-wi-insurance` | W&I-Versicherung: Bereitet W&I-Prozess, Underwriting, DD-Berichte, KI-DD-Transparenz und Deckungsausschlüsse vor. |
| `mittelstand-ma-aktenanlage` | Freistehende M&A-Aktenanlage: eröffnet Deal-Akte, Aktenzeichen, Parteienregister, Ordnerstruktur, Datenraumspiegel, Vertraulichkeitsstufen und Closing-Bible-Grundgerüst mit vollständig interner Arbeitslogik. |
| `mittelstand-ma-erechnung-gobd` | Freistehender Billing-, GoBD- und E-Rechnungsworkflow für M&A-Mandate: erzeugt Narratives, Workstream-Abrechnung, XRechnung-XML, ZUGFeRD-Prüfpaket und revisionssicheren Buchungsnachweis. |
| `mittelstand-ma-fristen-cp-kalender` | Freistehender Deal-Fristen- und CP-Kalender: führt Signing-, Closing-, Q&A-, Regulatory-, Register-, Board-, Ordinary-Course- und Restrukturierungsfristen im M&A-Mandat. |
| `mittelstand-ma-insolvenzreife` | Freistehender Insolvenzreife- und StaRUG-Schwellencheck für M&A: prüft Zahlungsunfähigkeit, drohende Zahlungsunfähigkeit, Überschuldung, Antragspflichten und Deal-Auswirkungen intern. |
| `mittelstand-ma-liquiditaetsvorschau` | Freistehende Liquiditätsvorschau für Corporate/M&A und Distressed M&A: prüft 3-Wochen-Liquidität, 13-Wochen-Cash-Bridge, Runway, OPOS, Bankdaten und Insolvenzschwellen intern. |
| `mittelstand-ma-schreibcanvas` | Freistehender Corporate-Schreibcanvas: begleitet SPA, Replik, Board Paper, Mandatsvereinbarung, DD-Report und Registertext mit freundlichen substanz- und belegorientierten Hinweisen. |
| `mittelstand-ma-tabellenreview` | Freistehender Tabellenreview für Corporate/M&A: prüft Dokumente, Datenpunkte, Tabellen, Formeln und Perspektiven als interne Review-Matrix mit vollständig interner Review-Logik. |

## Typische Workflows

- Buy-side: Target Screening -> NDA -> Aktenanlage -> Datenraum -> Tabellenreview -> Legal DD -> Q&A -> SPA-Markup -> Signing/Closing -> PMI.
- Sell-side: Teaser/IM -> Datenraumaufbau -> Vendor DD/Fact Book -> Bieter-Q&A -> Disclosure Schedules -> Vertragsverhandlung.
- Public M&A: Insider-/MAR-Prüfung -> Angebotsunterlage/Stellungnahme -> Kapitalmarktkommunikation -> Closing-Auflagen.
- Restrukturierung: Liquiditätsvorschau -> Insolvenzreifecheck -> StaRUG/Insolvenzplan -> Distressed M&A -> Gerichtsschritte -> Closing.
- Corporate Reorganisation: Umwandlung -> Umwandlungssteuerrecht -> Register/Notar -> Carve-out -> Closing.
- Billing: Zeitnachweise -> Narratives -> Workstream-Rechnung -> XRechnung/ZUGFeRD-Prüfpaket -> GoBD-Protokoll.

## Sicherheitsleitplanken

- Keine echte Transaktionsberatung ohne menschliche Letztprüfung.
- Keine Mandatsgeheimnisse, Insiderinformationen, Datenraumzugangsdaten oder Clean-Room-Daten in nicht freigegebene Systeme.
- KI-DD immer als `KI-gestützt`, `stichprobenvalidiert` oder `voll menschlich validiert` kennzeichnen.
- Register-, Rechtsprechungs-, Gesetzes- und Datenraumbelege müssen verifizierbar sein.
- Public M&A, MAR, WpÜG, Kartellrecht, Investitionskontrolle, Sanktionen, StaRUG, Zahlungsunfähigkeit und Überschuldung sind rote Schwellen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Mittelstand Corporate Ma-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeit... |
| `beirat-kaltstart-und-zielbild` | GmbH-Beirat im Plugin mittelstand-corporate-ma: Beirat Kaltstart Und Zielbild; konkretisierter Spezial-Workflow mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `beirat-red-team-satzung` | GmbH-Beirat im Plugin mittelstand-corporate-ma: Beirat Red Team Satzung; konkretisierter Spezial-Workflow mit Prüfachsen, Red Flags, Varianten, Quellenhygiene und verwertbarem Output. |
| `kompendium-01-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-rechtsprechungsrecherche, mittelstand-ma-fristen-cp-kalender, beirat-musterklauseln, mittelstand-corporate-ma-spa-apa... |
| `kompendium-02-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-vertragsmarkup-key-issues, beirat-haftung, mittelstand-corporate-ma-billing-narratives, mittelstand-corporate-ma-tabe... |
| `kompendium-03-mittelstand-corporat-bis-beirat-abgrenzung-au` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-umwandlungssteuerrecht, mittelstand-ma-tabellenreview, rechtsabteilung-earn-out-bei-mittelstandsverkauf, beirat-abgre... |
| `kompendium-04-beirat-amtszeit-und-bis-beirat-beschlussfass` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (beirat-amtszeit-und-rotation, beirat-bank-und-sanierung, beirat-beratungsfunktion, beirat-beschlussfassung) und bewahrt deren Workflows, Norma... |
| `kompendium-05-beirat-beschlussmaen-bis-beirat-compliance-un` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (beirat-beschlussmaengel, beirat-bestellung-und-abberufung, beirat-budget-und-businessplan, beirat-compliance-und-internal-investigation) und b... |
| `kompendium-06-beirat-datenschutz-u-bis-beirat-fakultativer` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (beirat-datenschutz-und-ki, beirat-deadlock-mechanik, beirat-entscheidungsbefugnisse, beirat-fakultativer-aufsichtsrat-52-gmbhg) und bewahrt de... |
| `kompendium-07-beirat-familiengesel-bis-beirat-geschaeftsord` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (beirat-familiengesellschaft, beirat-geschaeftsfuehrerabberufung, beirat-geschaeftsfuehrerbestellung, beirat-geschaeftsordnung) und bewahrt der... |
| `kompendium-08-beirat-immobilien-un-bis-beirat-interessenkon` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (beirat-immobilien-und-investitionen, beirat-informationsrechte, beirat-insolvenznaehe, beirat-interessenkonflikte) und bewahrt deren Workflows... |
| `kompendium-09-beirat-katalog-wesen-bis-beirat-nachfolge` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (beirat-katalog-wesentlicher-geschaefte, beirat-kontrollfunktion, beirat-mitbestimmung-abgrenzung, beirat-nachfolge) und bewahrt deren Workflow... |
| `kompendium-10-beirat-private-equit-bis-beirat-sitzung-und-p` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (beirat-private-equity-investor, beirat-register-und-notar, beirat-satzungsgrundlage, beirat-sitzung-und-protokoll) und bewahrt deren Workflows... |
| `kompendium-11-beirat-startup-inves-bis-beirat-verguetung` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (beirat-startup-investor-director, beirat-streit-gesellschafter, beirat-transaktionen-ma, beirat-verguetung) und bewahrt deren Workflows, Norma... |
| `kompendium-12-beirat-verschwiegenh-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (beirat-verschwiegenheit, beirat-veto-rechte, beirat-zustimmungsvorbehalte, mittelstand-corporate-ma-automation-monitoring) und bewahrt deren W... |
| `kompendium-13-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-board-paper-business-judgment, mittelstand-corporate-ma-closing-bible-archiv, mittelstand-corporate-ma-conflict-gwg-s... |
| `kompendium-14-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-datenraum-aufbau, mittelstand-corporate-ma-datenraum-gap-clean-room, mittelstand-corporate-ma-deal-intake, mittelstan... |
| `kompendium-15-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-disclosure-schedules, mittelstand-corporate-ma-distressed-ma, mittelstand-corporate-ma-due-diligence-commercial-contr... |
| `kompendium-16-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-due-diligence-reporting, mittelstand-corporate-ma-expert-calls-transkripte, mittelstand-corporate-ma-fair-disclosure-... |
| `kompendium-17-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-gesellschaftsrecht-register, mittelstand-corporate-ma-handelsregisterabruf, mittelstand-corporate-ma-kg-personengesel... |
| `kompendium-18-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 18; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-kommandocenter, mittelstand-corporate-ma-look-and-feel, mittelstand-corporate-ma-matter-file, mittelstand-corporate-m... |
| `kompendium-19-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 19; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-post-closing-integration, mittelstand-corporate-ma-public-ma-kapitalmarkt-mar, mittelstand-corporate-ma-qa-informatio... |
| `kompendium-20-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 20; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-restructuring-starug-insolvenzplan, mittelstand-corporate-ma-signing-closing-conditions, mittelstand-corporate-ma-sim... |
| `kompendium-21-mittelstand-corporat-bis-mittelstand-corporat` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 21; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-teaser-im-processdocs, mittelstand-corporate-ma-transaktionsstruktur, mittelstand-corporate-ma-translations-multijuri... |
| `kompendium-22-mittelstand-corporat-bis-mittelstand-ma-insol` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 22; bündelt 4 frühere Spezialskills (mittelstand-corporate-ma-wi-insurance, mittelstand-ma-aktenanlage, mittelstand-ma-erechnung-gobd, mittelstand-ma-insolvenzreife) und bewahrt d... |
| `kompendium-23-mittelstand-ma-liqui-bis-rechtsabteilung-fami` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (mittelstand-ma-liquiditaetsvorschau, mittelstand-ma-schreibcanvas, rechtsabteilung-betriebsuebergang-im-asset-deal, rechtsabteilung-familienge... |
| `kompendium-24-rechtsabteilung-gara-bis-v90-beirat-gmbh-zust` | mittelstand-corporate-ma: Konsolidiertes Skill-Kompendium 24; bündelt 3 frühere Spezialskills (rechtsabteilung-garantiekatalog-ohne-grosskanzlei-overkill, rechtsabteilung-vendor-due-diligence-fuer-versteckte-altlasten, v90-beirat-gmbh-zu... |
| `mittelstand-corporate-ma-kaltstart` | Deal-Kaltstart: Nimmt Kanzlei- und Mandantenpraeferenzen für Corporate/M&A auf: Dealtypen, Playbooks, Materiality, Reporting, Abrechnung, KI-Governance und Sicherheitsregeln. |
| `mittelstand-corporate-ma-output-versand-signing` | Output, Signing und Versand: Bereitet Transaktionsoutput vor: Markups, Issues Lists, Reports, Board Papers, Signing Packs, Closing Deliverables, beA/Notar/Email-Versand. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
