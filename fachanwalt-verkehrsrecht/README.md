# Fachanwalt Verkehrsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-verkehrsrecht`) | [`fachanwalt-verkehrsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-verkehrsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Verkehrsunfall Tannenbruck — A45 Quotenstreit, OWi, Fahrerlaubnis-Entzug, MPU** (`verkehrsunfall-quotenstreit-tannenbruck-a45`) | [Gesamt-PDF lesen](../testakten/verkehrsunfall-quotenstreit-tannenbruck-a45/gesamt-pdf/verkehrsunfall-quotenstreit-tannenbruck-a45_gesamt.pdf) | [`testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Verkehrsunfall Tannenbruck — A45 Quotenstreit, OWi, Fahrerlaubnis-Entzug, MPU** (`verkehrsunfall-quotenstreit-tannenbruck-a45`) | [Gesamt-PDF lesen](../testakten/verkehrsunfall-quotenstreit-tannenbruck-a45/gesamt-pdf/verkehrsunfall-quotenstreit-tannenbruck-a45_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsunfall-quotenstreit-tannenbruck-a45.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Plugin Fachanwalt für Verkehrsrecht. Orientierung StVG StVO PflVG VVG-Bezüge. Verkehrsunfall Personenschaden Sachschaden Bußgeld Fahrerlaubnis OWi-Verfahren Verkehrsstrafrecht (§§ 315c 316 StGB). Schnittstellen zu Versicherungs- und Strafrecht.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Fachanwalt Verkehrsrecht (`fachanwalt-verkehrsrecht`, dieses Plugin) | [fachanwalt-verkehrsrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-verkehrsrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-verkehrsrecht-orientierung` | Orientierung im Verkehrsrecht — FAO Voraussetzungen Normen typische Mandate Fristen Quellenprüfung. Verkehrsunfall mit Personen- und Sachschaden Schadensregulierung Versicherung Haftpflicht Kasko Bußgeld Fahrerlau… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Fachanwalt Verkehrsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeit... |
| `bussgeld-einspruch-pruefen` | Workflow-Skill zu bussgeld einspruch pruefen. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `erstgespraech-mandatsannahme` | Strukturierter Erstgespraechsleitfaden für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht): Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen. |
| `fachanwalt-verkehr-autonom-1d-stvg` | Unfall mit autonomem Fahrzeug oder Frage zur Haftung bei automatisiertem Fahren. § 1d StVG autonomes Fahren Level 4. Prüfraster: Haftungsverteilung Halter § 7 StVG Fahrer § 18 StVG Hersteller § 1 ProdHaftG Datensaetze Black-Box § 1g StVG... |
| `fachanwalt-verkehrsrecht-bussgeldbescheid-pruefen` | Mandant hat OWi-Bußgeldbescheid erhalten und Anwalt prüft ob Einspruch sinnvoll ist. OWiG §§ 65 ff. StVG § 26 Abs. 3 Verjährung. Prüfraster: Form- und Verfahrensfehler Verjährung 3 Monate ab Tat unterbrochen § 33 OWiG Messverfahren stand... |
| `fachanwalt-verkehrsrecht-fahrerlaubnis-entzug` | Mandant hat Führerschein entzogen bekommen oder befuerchtet Entziehung und fragt nach Möglichkeiten. § 69 StGB strafgerichtlich § 3 StVG verwaltungsrechtlich. Prüfraster: Sperrfrist § 69a StGB vorlaeufige Entziehung § 111a StPO Wiederert... |
| `fachanwalt-verkehrsrecht-mpu-vorbereitung` | Mandant muss MPU ablegen und fragt wie er sich vorbereiten soll. MPU Medizinisch-Psychologische Untersuchung Fahrerlaubnisrecht. Prüfraster: Anlass Alkohol Drogen Punkte Aggression zugelassene Begutachtungsstellen § 66 FeV Vorbereitungsk... |
| `fachanwalt-verkehrsrecht-orientierung` | Einstieg in den Skill-Verbund Verkehrsrecht. Orientierung im Verkehrsrecht FAO Voraussetzungen §§ 14g bis 14i FAO Verkehrsrecht. Typische Mandate Verkehrsunfall Schadensregulierung OWi-Bußgeld Fahrerlaubnis MPU Verkehrsstrafrecht §§ 315c... |
| `fachanwalt-verkehrsrecht-regulierungsanforderung` | Mandant hat Verkehrsunfall und fordert Schadensersatz vom Haftpflichtversicherer des Unfallverursachers. § 115 VVG Direktanspruch §§ 7 17 StVG § 823 BGB. Prüfraster: Direktanspruch Reparatur vs. fiktive Abrechnung Wiederbeschaffungswert... |
| `fachanwalt-verkehrsrecht-tempo-messung-beweis` | Mandant bestreitet korrekte Geschwindigkeitsmessung in Bußgeldbescheid. Tempo-Messung Beweisanfechtung OWiG. Prüfraster: Standardmessgeräte PoliScan Speed Es 3.0 LeivTec XV-3 Multanova PTB-Zulassung Eichschein Messdokumentation Messverfa... |
| `fachanwalt-verkehrsrecht-unfallregulierung-quoten` | Mandant hat Unfall mit Mitverschulden und fragt welche Schadensposten zu welcher Quote durchsetzbar sind. § 254 BGB Mitverschulden Quoten-Modelle. Prüfraster: Schadenstabellen Reparatur Mietwagen Wertminderung Nutzungsausfall Schmerzensg... |
| `fachanwalt-verkehrsrecht-versicherer-quotenverhandlung-vergleich` | Versicherer hat Regulierung angeboten und Anwalt verhandelt Quotenerhöhung oder Vergleich. Versicherer-Verhandlung Unfallregulierung. Prüfraster: Mitverschuldensquote § 254 BGB vorgerichtliche Korrespondenz Schmerzensgeld-Tabellen gerich... |
| `mandat-triage-verkehrsrecht` | Neues Verkehrsrechtsmandat kommt rein und Anwalt muss Sachgebiet klaeren und Fristen prüfen. Eingangs-Triage Verkehrsrecht. Prüfraster: Verfahrensart (Zivilrecht Schadensregulierung OWi Strafrecht Fahrerlaubnis) Unfallart Fristen (Einspr... |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Klage Verkehrsunfall, Einspruch OWi-Bußgeldbescheid, Klage KFZ-Versicherung: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. |
| `spezial-315c` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu 315c: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-315c-316-stgb` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu 315c 316 StGB: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-bezuege` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Bezuege: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-bussgeld` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Bußgeld: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-fachanwalt` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu fachanwalt: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-fachanwalt-verkehrsrecht` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Fachanwalt Verkehrsrecht: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-fahrerlaubnis` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Fahrerlaubnis: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-personen` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Personen: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-pflvg` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu PflVG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-sachschaden` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Sachschaden: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-sachschaden-bussgeld-fahrerlaubnis-v` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Sachschaden Bußgeld Fahrerlaubnis Verkehrsstrafrecht: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-schnittstelle-kanzlei` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Schnittstelle kanzlei: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-stvg` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu StVG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-stvg-stvo-pflvg-vvg` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu StVG StVO PflVG VVG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-stvo` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu StVO: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-verkehrsrecht` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu verkehrsrecht: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-verkehrsstrafrecht` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Verkehrsstrafrecht: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-verkehrsunfall` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Verkehrsunfall: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-verkehrsunfall-personen` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu Verkehrsunfall Personen: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `spezial-vvg` | Vertiefter Spezial-Skill im Plugin fachanwalt-verkehrsrecht zu VVG: prüft Fachfrage, Fristen, Zuständigkeit, Belege, typische Fehler und erzeugt einen nutzbaren Output. |
| `unfall-haftungsquote-berechnen` | Mandant hatte Verkehrsunfall und fragt: Wer haftet wie viel und welche Schadensposten koennen geltend gemacht werden? §§ 7 17 18 StVG iVm § 254 BGB Haftungsquote. Prüfraster: Betriebsgefahr beidseitig Anscheinsbeweis Auffahrunfall Spurwe... |
| `vergleichsverhandlung-strategie` | Vergleichsverhandlungs-Strategie für Verkehrsrecht (Unfall-, OWi- und Verkehrsstrafrecht): ZOPA, BATNA, Verhandlungsfenster, Druckmittel, Settlement-Skript, Vergleichsentwurf und prozessuale Absicherung (Protokoll-/Anwaltsvergleich). |
| `vkr-blitzer-messverfahren-spezial` | Spezialfall Blitzer- und Messverfahren: standardisiertes Messverfahren, Rohmessdaten-Recht des Verteidigers (BVerfG 2 BvR 1167/20), Verwertbarkeit, Beweisantrag Sachverstaendigengutachten. Pruefraster und Schriftsatzbausteine. |
| `vkr-bussgeldverfahren-grundzuege` | Bussgeldverfahren Grundzuege: Anhoerungsbogen, Einspruch innerhalb 2 Wochen, Hauptverhandlung Amtsgericht, Rechtsbeschwerde OLG nach §§ 79 ff. OWiG. Strategien Verteidigung, Punkterabatt bei Punkteabbau-Seminar. Pruefraster. |
| `vkr-einfuehrung-rechtsfelder` | Verkehrsrecht einfuehrend: Verkehrsstrafrecht (Trunkenheit § 316 StGB, Gefaehrdung § 315c StGB, Unfallflucht § 142 StGB), OWi (Bussgeldverfahren), Haftpflicht, Kasko, Fuehrerscheinrecht, FeV, MPU. Entscheidungstabelle. |
| `vkr-totalschaden-fiktiv-spezial` | Spezialfall fiktive Abrechnung beim Totalschaden: Wiederbeschaffungswert minus Restwert, 130-Prozent-Grenze BGH, Verweisung auf guenstigere Reparaturen (BGH-Verweisrechtsprechung). Pruefraster fuer Mandantenberatung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin fachanwalt-verkehrsrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin fachanwalt-verkehrsrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin fachanwalt-verkehrsrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fachanwalt-verkehrsrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin fachanwalt-verkehrsrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fachanwalt-verkehrsrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin fachanwalt-verkehrsrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin fachanwalt-verkehrsrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fachanwalt-verkehrsrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin fachanwalt-verkehrsrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
