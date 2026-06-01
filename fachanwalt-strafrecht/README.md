# Fachanwalt Strafrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-strafrecht`) | [`fachanwalt-strafrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-strafrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Wirtschaftsstrafsache Bankert — U-Haft, Betrug, Steuerhinterziehung, LG Frankfurt** (`wirtschaftsstrafsache-uhaft-bankert-frankfurt`) | [Gesamt-PDF lesen](../testakten/wirtschaftsstrafsache-uhaft-bankert-frankfurt/gesamt-pdf/wirtschaftsstrafsache-uhaft-bankert-frankfurt_gesamt.pdf) | [`testakte-wirtschaftsstrafsache-uhaft-bankert-frankfurt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wirtschaftsstrafsache-uhaft-bankert-frankfurt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **Wirtschaftsstrafsache Bankert — U-Haft, Betrug, Steuerhinterziehung, LG Frankfurt** (`wirtschaftsstrafsache-uhaft-bankert-frankfurt`) | [Gesamt-PDF lesen](../testakten/wirtschaftsstrafsache-uhaft-bankert-frankfurt/gesamt-pdf/wirtschaftsstrafsache-uhaft-bankert-frankfurt_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wirtschaftsstrafsache-uhaft-bankert-frankfurt.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| Fachanwalt Strafrecht (`fachanwalt-strafrecht`, dieses Plugin) | [fachanwalt-strafrecht.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-strafrecht.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `fachanwalt-strafrecht-orientierung` | Orientierung im Strafrecht — FAO-Voraussetzungen Normen typische Mandate Notfristen Quellenprüfung. Plugin für schnelle Verortung. Strafverteidigung im Ermittlungsverfahren (Akteneinsicht § 147 StPO) H… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `akteneinsicht-strafrecht-auswerten` | Strukturierte Auswertung der Strafakte nach Akteneinsicht § 147 StPO. Erstellt Beweismittelverzeichnis (Urkunden Augenscheinsobjekte Zeugen Sachverständige) Personenregister Chronologie Aussagen-Synopse mit Inkonsistenzen Verwertungsverb... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Fachanwalt Strafrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitspl... |
| `erstgespraech-mandatsannahme` | Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen. § 136 StPO Belehrung Schweigerecht... |
| `fachanwalt-strafrecht-adhaesionsverfahren` | Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig Schmerzensgeld oder Schadensersatz geltend machen ohne separaten Zivilprozess. §§ 403-406c StPO Adhaesionsverfahren, §... |
| `fachanwalt-strafrecht-akteneinsicht-beantragen` | Akteneinsicht § 147 StPO durch Verteidiger jederzeit waehrend Ermittlungsverfahren und nach Abschluss. Versagungsgründe § 147 Abs. 2 StPO Gefaehrdung Untersuchungszweck. Beschuldigter selbst nur durch Verteidiger § 147 Abs. 4 StPO. Verle... |
| `fachanwalt-strafrecht-anklage-reaktion` | Reaktion auf Anklageerhebung nach § 199 StPO und Eroefffnungsverfahren: Anwendungsfall Mandant hat Anklageschrift erhalten und Verteidiger muss strategisch auf Eroeffnungsverfahren reagieren. § 199 StPO Eroeffnungsverfahren, § 203 StPO h... |
| `fachanwalt-strafrecht-chatcontrol-csam-anwaltsgeheimnis-53-stpo` | Chat-Control CSAM Anwaltsgeheimnis und § 53 StPO Zeugnisverweigerungsrecht: Anwendungsfall Kanzlei prüft ob Chat-Control-Massnahmen Anwaltsgeheimnis verletzen oder Mandatskommunikation abhoeren koennten. § 53 StPO Zeugnisverweigerungsrec... |
| `fachanwalt-strafrecht-einlassung-vorbereiten` | Schriftliche Einlassung des Beschuldigten vorbereiten oder Schweigen § 136 StPO. Schweigerecht ist Grundrecht und darf nicht nachteilig gewertet werden BGH st. Rspr. Aber Teilschweigen kann gewürdigt werden. Strategie nach Aktenlage Bewe... |
| `fachanwalt-strafrecht-hauptverhandlung-vorbereiten` | Hauptverhandlung im Strafverfahren vorbereiten: Anwendungsfall Strafverteidiger muss Hauptverhandlung strukturiert vorbereiten mit Einlassung Beweisanträgen und Verfahrenstaktik. § 136 StPO Schweigerecht, § 244 StPO Beweisanträge, § 258... |
| `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` | Insolvenzantrag-Massnahmen durch Staatsanwaltschaft im Wirtschaftsstrafrecht: Anwendungsfall Staatsanwaltschaft hat Insolvenzantrag gestellt oder Vermögenswerte beschlagnahmt und Verteidiger muss reagieren. § 283 StGB Bankrott, § 15a Ins... |
| `fachanwalt-strafrecht-nebenklage-opfervertretung` | Nebenklage und Opfervertretung im Strafverfahren: Anwendungsfall Opfer einer Straftat moechte als Nebenklaeger am Verfahren teilnehmen und anwaltliche Vertretung benoetigen. §§ 395-406h StPO Nebenklage, § 403 StPO Adhaesionsantrag, OEG O... |
| `fachanwalt-strafrecht-orientierung` | Orientierung im Strafrecht-Mandat und Workflow-Routing: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und richtigen Spezial-Skill finden. § 136 StPO Belehrung, § 137 StPO Verteidigerrec... |
| `fachanwalt-strafrecht-untersuchungshaft-haftpruefung` | Untersuchungshaft und Haftprüfung nach §§ 112 ff. StPO: Anwendungsfall Mandant wurde verhaftet und Strafverteidiger muss Haftbefehl anfechten oder Haftprüfungsantrag stellen. §§ 112-113 StPO Haftgründe Fluchtgefahr Verdunkelungsgefahr Wi... |
| `fachanwalt-strafrecht-verstaendigung-257c-toa-46a` | Verständigung § 257c StPO und Taeter-Opfer-Ausgleich § 46a StGB vorbereiten: Anwendungsfall Strafverteidiger prüft ob Einigung durch Deal Einstellung oder TOA für Mandanten vorteilhaft ist. § 257c StPO Verständigung Gestaendnis gegen Str... |
| `fachanwalt-strafrecht-wahlverteidiger-mandat` | Wahlverteidiger-Mandat im Strafrecht beginnen: Anwendungsfall Beschuldigter waehlt Strafverteidiger und Erstgespraeach muss Schweigerecht Akteneinsicht Honorar und Strategie klaeren. § 136 StPO Schweigerecht Erstbelehrung, § 137 StPO Ver... |
| `fachanwalt-strafrecht-zeugenbeistand` | Zeugenbeistand im Strafverfahren für Zeugen mit eigenem Rechtsinteresse: Anwendungsfall Person ist als Zeuge geladen hat aber eigenes Aussageverweigerungsrecht oder Selbstbelastungsrisiko und benoetigt anwaltlichen Beistand. § 68b StPO Z... |
| `mandat-triage-strafrecht` | Strukturierte Eingangs-Abfrage für Strafmandate. Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungshaft Vollzug Hausverbot) Beschu... |
| `plaedoyer-vorbereitung-strafverteidigung` | Plaedoyer für Strafverteidigung vorbereiten und strukturieren: Anwendungsfall nach Abschluss der Beweisaufnahme muss Strafverteidiger Schlusspledoyer mit Schuldfrage Strafzumessung und Verfahrenshindernissen vorbereiten. § 258 StPO Schlu... |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Strafverfahren Einspruch und Revision: Anwendungsfall Strafverteidiger muss Einspruch gegen Strafbefehl Revisionsbegründung oder Klageerzwingungsantrag verfassen. §§ 410 ff. StPO Einspruch Strafbefehl,... |
| `spezial-adhaesion-formular-portal-und-einreichung` | Adhaesion: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-aktenaufbereiter-beweislast-und-darlegungslast` | Aktenaufbereiter: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ergaenzt-mandantenkommunikation-entscheidungsvorlage` | Ergaenzt: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ermittlungsverfahren-vergleich-eskalation` | Ermittlungsverfahren: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-fachanwalt-erstpruefung-und-mandatsziel` | Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-hauptverhandlung-livequellen-und-rechtsprechungscheck` | Hauptverhandlung: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-insolvenzantrag-red-team-und-qualitaetskontrolle` | Insolvenzantrag: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-kanzlei-sonderfall-und-edge-case` | Kanzlei: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-livecheck-abschlussprodukt-und-uebergabe` | Livecheck: Abschlussprodukt und Übergabe: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-nebenklage-compliance-dokumentation-und-akte` | Nebenklage: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-nebenstrafrecht-behoerden-gericht-und-registerweg` | Nebenstrafrecht: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-opfervertretung-mehrparteien-konflikt-und-interessen` | Opfervertretung: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-orientierung-fristen-form-und-zustaendigkeit` | Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsquellen-fristennotiz-und-naechster-schritt` | Rechtsquellen: Fristennotiz und nächster Schritt: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-revision-zahlen-schwellen-und-berechnung` | Revision: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-stgb-risikoampel-und-gegenargumente` | Stgb: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-stpo-dokumentenmatrix-und-lueckenliste` | StPO: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-strafrecht-tatbestand-beweis-und-belege` | Strafrecht: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-strafverteidigung-schriftsatz-brief-und-memo-bausteine` | Strafverteidigung: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-zeugenbeistand-internationaler-bezug-und-schnittstellen` | Zeugenbeistand: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `strafr-haftpruefung-haftbeschwerde-workflow` | Workflow Haftpruefung und Haftbeschwerde §§ 117 ff. StPO: dringender Tatverdacht, Haftgrund, Verhaeltnismaessigkeit, Sechsmonatspruefung. Mustertext Haftpruefungsantrag und Haftbeschwerde. |
| `strafr-revision-pruefung-spezial` | Spezialfall Revisionspruefung StPO: § 337 sachlich- und verfahrensrechtliche Revision, Beruhensfrage, Verfahrensruegen Begruendungspflicht § 344 Abs. 2 StPO. Pruefraster fuer Revisionsbegruendung. |
| `strafr-vermoegensabschoepfung-spezial` | Spezialfall Vermoegensabschoepfung §§ 73 ff. StGB nach Reform 2017: Einziehung von Taterzeugnissen, Wertersatzeinziehung, erweiterte Einziehung. Pruefraster fuer Verteidiger und Drittbetroffene. |
| `strafr-wirtschaftsstrafrecht-leitfaden` | Leitfaden Wirtschaftsstrafrecht: Untreue § 266 StGB, Betrug § 263, Bilanzdelikte §§ 331 ff. HGB / § 400 AktG, Compliance-Verteidigung. Pruefraster Wirtschaftsstrafkammer. |
| `vergleichsverhandlung-strategie` | Verhandlungs- und Einigungsstrategie im Strafverfahren: Anwendungsfall Sachverhalt eignet sich für prozessuale Einigung und Strafverteidiger will Verständigung Einstellung oder TOA vorbereiten. § 257c StPO Verständigung, § 153a StPO Eins... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin fachanwalt-strafrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin fachanwalt-strafrecht: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin fachanwalt-strafrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin fachanwalt-strafrecht: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin fachanwalt-strafrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin fachanwalt-strafrecht: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin fachanwalt-strafrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin fachanwalt-strafrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin fachanwalt-strafrecht: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin fachanwalt-strafrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
