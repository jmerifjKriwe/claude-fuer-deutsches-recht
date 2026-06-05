# Prozessrecht-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`prozessrecht`) | [`prozessrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/prozessrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Werkvertragsstreit Pohlmann / Saalbau Rosenheim — Baumängel, BGH-Revision, Zurückverweisung** (`zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann`) | [Gesamt-PDF lesen](../testakten/zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann/gesamt-pdf/zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann_gesamt.pdf) | [`testakte-zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-zivilprozess-werkvertragsstreit-saalbau-rosenheim-bgh-revision-pohlmann.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Unterstützung für Prozessanwälte und Syndikusrechtsanwälte bei der Führung eines Mandatsportfolios im deutschen Zivil-, Straf-, Verwaltungs- und Arbeitsrecht. Der Kaltstart-Interview erfasst Risikobereitschaft, Mandatslandschaft und Kanzleistil – der Rahmen, gegen den jedes neue Mandat eingeordnet wird. Einheitliche Aufnahme (Intake) überführt neue Mandate in strukturierte Logeinträge und mandatsbezogene Historiendateien. Statusübersichten und Tiefenbriefings lesen aus dem Log.

Konzipiert für Anwälte, die viele Mandate gleichzeitig betreuen, von denen die meisten durch externe Kanzleien oder Korrespondenzanwälte bearbeitet werden. Dieses Plugin ist ein Denkpartner, kein Mandatsverwaltungssystem. Wenn Sie LawVu, SimpleLegal oder eine vergleichbare Software einsetzen, ersetzt dieses Plugin diese nicht – es ergänzt sie als strukturierte Argumentations- und Analyseschicht.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – zitiert, markiert und abgesichert –, keine rechtliche Schlussfolgerung.** Das Plugin erledigt die Arbeit: liest die Dokumente, wendet Ihr Playbook an, findet die Probleme, entwirft das Memo. Ein Anwalt prüft, verifiziert und entscheidet. Zitate sind nach Quelle gekennzeichnet, damit klar ist, welche aus einem Recherchetool stammen und welche noch zu überprüfen sind. Mandatsgeheimnismarker werden konservativ angewendet, damit keine unbeabsichtigte Offenbarung erfolgt (§ 43a Abs. 2 BRAO, § 203 StGB). Folgenreiche Handlungen – Einreichen, Versenden, Vollstrecken – sind durch ausdrückliche Bestätigung abgesichert.

## Voraussetzungen

Einige Funktionen verweisen auf Outlook- und Kalender-Integrationen. Diese erfordern MCP-Server in Ihrer Umgebung – sie sind nicht im Plugin enthalten. Ohne sie werden Ausgaben als Dateien gespeichert:

- **Outlook MCP** – `/gegenseite-status` erstellt Outlook-Entwürfe, sofern authentifiziert; andernfalls Markdown-Entwürfe in `gegenseite-status/[JJJJ-MM-TT]/[slug].md`.
- **Kalender-MCP** – keine automatische Terminplanung enthalten. Richten Sie eine Wiederholungserinnerung ein, um wöchentliche Befehle aufzurufen.

Das Plugin funktioniert vollständig ohne beide Integrationen; diese sind additiv.

## Für wen ist das?

| Rolle | Hauptverwendung |
|---|---|
| **Prozessanwalt (Kanzlei oder Syndikus)** | Alles – Intake, Triage, Status, Historie, Briefings |
| **Stellvertretender Justiziar / leitender Syndikus** | Portfolio-Übersicht, Vorstandsberichterstattung |
| **Hauptjustiziar / Leiter Rechtsabteilung** | Schneller Portfoliostatus, Tiefeneinblick in einzelne Mandate |
| **Außenanwalt** | Per-Mandat-Verlaufsdokumentation, Schriftsatzentwürfe, Fristen |

## Anwendungsbereich

Das Plugin deckt das **deutsche Zivilprozessrecht (ZPO)** als Kernbereich ab und enthält spezialisierte Skills für:

- **Strafrecht / Strafverteidigung** – StPO, Pflichtverteidigung, Akteneinsicht
- **Digitale StPO-Ermittlungsmaßnahmen** – biometrischer Internetabgleich, KI-Analyseplattformen, Akteneinsicht, Benachrichtigung, Löschung und Verwertungsangriffe
- **Verwaltungsrecht** – VwGO, Widerspruchsverfahren
- **Arbeitsrecht** – ArbGG, einstweiliger Rechtsschutz
- **Familienrecht** – FamFG
- **Steuerrecht** – FGO, BFH
- **Sozialrecht** – SGG, BSG
- **Zwangsvollstreckung** – §§ 704 ff. ZPO
- **Einstweilige Verfügung** – §§ 935, 940 ZPO
- **Mahnverfahren** – §§ 688 ff. ZPO
- **Verkehrsunfallrecht** – StVG, § 115 VVG

Für harte ZPO-Fakten gibt es den Spezialskill `amtlicher-zpo-verfahrenscheck`. Er nutzt den aktuellen amtlichen ZPO-Normkern und trennt Zuständigkeit, Form, Zustellung, Fristen, Klage, Beweis, Mahnverfahren, Vollstreckung, Arrest und einstweilige Verfügung.

## Vorprozessuale Beweiserhebung im deutschen Recht

Informationsbeschaffung erfolgt durch:
- §§ 142, 144 ZPO (gerichtliche Urkundenvorlegung und Augenschein)
- § 810 BGB (Einsichtnahme in Urkunden)
- §§ 242, 259, 260, 666 BGB (Auskunftsansprüche)
- Art. 15 DSGVO (Auskunftsrecht)
- § 254 ZPO (Stufenklage)
- §§ 485 ff. ZPO (Selbständiges Beweisverfahren)

Zum Schutz anwaltlicher Unterlagen: § 43a Abs. 2 BRAO, § 203 StGB; Zeugnisverweigerungsrecht § 383 Abs. 1 Nr. 6 ZPO; Beschlagnahmefreiheit §§ 97, 53 StPO; Editionsverweigerung §§ 142, 383 ZPO.

Urteile sind nicht bindend (außer § 31 BVerfGG). Literatur und Kommentare sind tragende Argumentationsquellen.

## Rechtsgebiete und Verfahrensordnungen

| Verfahren | Rechtsgrundlage |
|---|---|
| Zivilprozess | ZPO, GVG, RVG, GKG |
| Strafprozess | StPO, GVG, RVG |
| Verwaltungsstreit | VwGO, VwVfG |
| Finanzgerichtsbarkeit | FGO, AO |
| Sozialgerichtsbarkeit | SGG, SGB |
| Arbeitsgerichtsbarkeit | ArbGG, KSchG |
| Familiensachen | FamFG, BGB |
| Zwangsvollstreckung | §§ 704–915h ZPO |

## Dateistruktur

```
prozessrecht/
├── CLAUDE.md              # Praxisprofil (vom Kaltstart geschrieben)
├── README.md              # Diese Datei
├── mandate/               # Pro-Mandat-Ordner: mandat.md + verlauf.md
│   └── _log.yaml          # Portfolio-Log aller Mandate
├── demand-letters/        # Ausgehende Schreiben und Entwürfe
├── inbound/               # Eingegangene Schreiben, Mahnungen, Beschlüsse
├── gegenseite-status/             # Korrespondenz mit Gegenseite / Außenanwälten
└── skills/                # Plugin-Skills (automatisch geladen)
```

## Nutzungshinweis

Alle Ausgaben des Plugins sind **Entwürfe zur anwaltlichen Prüfung**. Das Plugin ersetzt keine Rechtsberatung und trifft keine Entscheidungen. Berufsrechtliche Pflichten nach BRAO, BORA, RVG und die anwaltliche Verschwiegenheit nach § 43a Abs. 2 BRAO bleiben unberührt. Für die Überprüfung und Freigabe jedes Dokuments ist stets der verantwortliche Anwalt zuständig.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 25 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtlicher-zpo-proz-bauleiter-eilverfahren` | Amtlicher ZPO Proz Bauleiter Eilverfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anspruchstabelle-gegenseite-interessen` | Anspruchstabelle Gegenseite Interessen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `beweissicherung-einstweilige-verfuegung` | Beweissicherung Einstweilige Verfuegung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `gegenseite-status-mahnbescheid-mahnschreiben` | Gegenseite Status Mahnbescheid Mahnschreiben: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mahnschreiben-entwurf-anwaltsgeheimnis` | Mahnschreiben Entwurf Anwaltsgeheimnis: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mahnschreiben-erhalten-aktualisierung` | Mahnschreiben Erhalten Aktualisierung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mandat-briefing-schliessen-portfolio-status` | Mandat Briefing Schliessen Portfolio Status: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mandat-mandate-prozessrecht` | Mandat Mandate Prozessrecht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `proz-beweismittel-leitfaden-mediationsklage` | Proz Beweismittel Leitfaden Mediationsklage: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `proz-quellenkarte` | Proz Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `prozessrecht-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `prozessrecht-anspruchstabelle-beweislast` | Anspruchstabelle für zivilprozessuales Mandat erstellen: alle Ansprüche und Gegenansprüche tabellarisch erfassen. Normen: §§ 253 261 ZPO. Prüfraster: Anspruchsgrundlage, Betrag, Verjaebrung, Beweisstatus. Output: Anspruchstabelle als Gru... |
| `prozessrecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `prozessrecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `prozessrecht-kaltstart-interview` | Prozessrechtliches Erstinterview strukturiert durchführen: Sachverhalt, Klagebegehren, Fristen, Kosten. Normen: §§ 253 261 ZPO, BRAO. Prüfraster: Anspruchsgrundlage, Zuständigkeit, Verjaebrung, Kostenrisiko. Output: Interviewprotokoll mi... |
| `prozessrecht-mandat-arbeitsbereich-abschnitt` | Mandat Arbeitsbereich Abschnitt: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `prozessrecht-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `prozessrecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `prozessrecht-start-chronologie-fristen` | Start Chronologie Fristen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `prozessrecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `prozessrechtliche-schriftsaetze-status` | Prozessrechtliche Schriftsaetze Status: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `streitwert-verkehrsunfall-vollstreckung` | Streitwert Verkehrsunfall Vollstreckung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verfahrensart-rechtsweg` | Verfahrensart Rechtsweg: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vollstreckung-stpo-biometrischer` | Vollstreckung Stpo Biometrischer: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vorlageanordnung-zeuge-vorbereitung` | Vorlageanordnung Zeuge Vorbereitung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
