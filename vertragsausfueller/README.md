# Vertragsausfüller

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`vertragsausfueller`) | [`vertragsausfueller.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/vertragsausfueller.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Vertragsausfueller - BSAG Kiosk Huckelriede** (`vertragsausfueller-bsag-kiosk-huckelriede`) | [Gesamt-PDF lesen](../testakten/vertragsausfueller-bsag-kiosk-huckelriede/gesamt-pdf/vertragsausfueller-bsag-kiosk-huckelriede_gesamt.pdf) | [`testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-vertragsausfueller-bsag-kiosk-huckelriede.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Cowork-Plugin für workflowgestütztes Ausfüllen von Vertragsvorlagen und Altverträgen. Ein Nutzer lädt eine Word-Vorlage, einen alten Vertrag, ein Term Sheet oder Freitextdaten hoch. Das Plugin strippt das Dokument, erkennt Felder und Klauseln, fragt fehlende Daten ab, mappt Term-Sheet-Daten auf Vertragsfelder und erstellt daraus einen neuen Vertragsentwurf.

Der BSAG-Mietvertrag und das Term Sheet Kiosk Huckelriede sind als Beispielakte eingebunden.

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `vertragsausfueller.zip` hochladen.
4. Mit einem konkreten Auftrag starten, zum Beispiel: `Fülle diesen Mietvertrag mit den Daten aus dem Term Sheet aus.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install vertragsausfueller@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/` und `assets/` enthalten.

## Workflow

1. Vorlage oder alten Vertrag hochladen.
2. Dokument strippen: Absätze, Tabellen, Platzhalter, Klauseln, Anlagen und Signaturen erkennen.
3. Term Sheet, E-Mail oder Freitextdaten danebenlegen.
4. Feldinventar und Mapping erzeugen.
5. Fehlende Daten freundlich abfragen oder als offene Platzhalter markieren.
6. Clean-Vertrag erstellen.
7. Nur auf ausdrückliche Nachfrage zusätzlich Track Changes oder Redline vorbereiten.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| vaf-kommandocenter | steuert den gesamten Workflow von Upload bis neuem Vertragsentwurf. |
| vaf-docx-stripper | macht aus Word-Dokumenten ein bearbeitbares Vertragsmodell. |
| vaf-template-erkennung | klassifiziert den Vertrag und trennt Fixtext von Variablen. |
| vaf-feldinventar | baut die zentrale Datenmatrix für den Vertrag. |
| vaf-termsheet-mapping | überführt wirtschaftliche Eckdaten in Vertragsklauseln. |
| vaf-rueckfrageninterview | füllt Datenlücken ohne den Nutzer zu überfordern. |
| vaf-bsag-mietvertrag | setzt den Huckelriede-Term-Sheet-Fall in die BSAG-Vorlage um. |
| vaf-klauselentscheidung | verhindert stilles Auswählen riskanter Optionen. |
| vaf-plausibilitaetscheck | härtet den Entwurf vor Versand oder Verhandlung. |
| vaf-clean-output | liefert den ersten belastbaren Vertragsentwurf. |
| vaf-track-changes-nur-nach-frage | setzt die ausdrückliche Nachfragepflicht durch. |
| vaf-redline-qa | kontrolliert Änderungsfassungen vor Herausgabe. |
| vaf-altvertrag-nachziehen | macht aus alten Verträgen neue Entwürfe. |
| vaf-quality-gate | ist die letzte Schleuse vor Vertragserzeugung. |

## BSAG-Beispiel

Die Beispielakte enthält die Word-Vorlage `BSAG-Mietvertrag-Vorlage.docx` und das Term Sheet `BSAG-TermSheet-Kiosk-Huckelriede - Kopie.docx`. Der Spezialskill `vaf-bsag-mietvertrag` mappt daraus insbesondere Mieter, Mietobjekt, Nutzung, Fläche, Miete, Nebenkosten, Kaution, Mietbeginn, Laufzeit, Optionen, Indexierung, Umsatzsteuer, Öffnungszeiten, Konkurrenzschutz, Sortiment, Fettabscheider, Werbung und Versicherung.

## Track-Changes-Regel

Das Plugin erzeugt keine Track-Changes- oder Redline-Fassung stillschweigend. Es fragt immer ausdrücklich: Soll zusätzlich eine Track-Changes- oder Redline-Fassung erstellt werden? Ohne Bestätigung bleibt es bei Clean-Entwurf, Änderungslog und Ausfüllprotokoll.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | vertragsausfueller: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabe... |
| `kompendium-02-workflow-mandantenko-bis-spezial-ausdruecklic` | vertragsausfueller: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-ausdruecklicher-fristennotiz-und-naechster-schritt) und bewahrt deren Workflo... |
| `kompendium-03-spezial-vorlagen-fri-bis-vaf-altvertrag-nachz` | vertragsausfueller: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-vorlagen-fristen-form-und-zustaendigkeit, spezial-vertragsausfueller-erstpruefung-und-mandatsziel, vaf-altvertrag-nachziehen) und bewahrt de... |
| `kompendium-04-vaf-bsag-mietvertrag-bis-vaf-konzern-rahmenve` | vertragsausfueller: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (vaf-bsag-mietvertrag, vaf-klauselentscheidung, vaf-konzern-rahmenvertrag-anpassen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabe... |
| `kompendium-05-vaf-plausibilitaetsc-bis-spezial-altvertraege` | vertragsausfueller: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (vaf-plausibilitaetscheck, vaf-termsheet-mapping, spezial-altvertraege-dokumentenmatrix-und-lueckenliste) und bewahrt deren Workflows, Normanker, Prü... |
| `kompendium-06-spezial-changes-bewe-bis-spezial-erkennen-sch` | vertragsausfueller: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (spezial-changes-beweislast-und-darlegungslast, spezial-docx-tatbestand-beweis-und-belege, spezial-erkennen-schriftsatz-brief-und-memo-bausteine) und... |
| `kompendium-07-spezial-erzeugen-red-bis-spezial-felder-behoe` | vertragsausfueller: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (spezial-erzeugen-red-team-und-qualitaetskontrolle, spezial-fassungen-sonderfall-und-edge-case, spezial-felder-behoerden-gericht-und-registerweg) und... |
| `kompendium-08-spezial-fuehren-mehr-bis-spezial-nachfrage-ab` | vertragsausfueller: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (spezial-fuehren-mehrparteien-konflikt-und-interessen, spezial-mappen-zahlen-schwellen-und-berechnung, spezial-nachfrage-abschlussprodukt-und-ueberga... |
| `kompendium-09-spezial-neue-interna-bis-spezial-strippen-ris` | vertragsausfueller: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (spezial-neue-internationaler-bezug-und-schnittstellen, spezial-rueckfragen-compliance-dokumentation-und-akte, spezial-strippen-risikoampel-und-gegen... |
| `kompendium-10-spezial-term-verhand-bis-spezial-vertraege-fo` | vertragsausfueller: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-term-verhandlung-vergleich-und-eskalation, spezial-track-mandantenkommunikation-entscheidungsvorlage, spezial-vertraege-formular-portal-und-... |
| `kompendium-11-vaf-batch-modus-konz-bis-vaf-einfuehrung-proz` | vertragsausfueller: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (vaf-batch-modus-konzern, vaf-docx-stripper, vaf-einfuehrung-prozess) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-12-vaf-feldinventar-bis-vaf-fremdsprachige-v` | vertragsausfueller: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (vaf-feldinventar, vaf-fragebogen-input-leitfaden, vaf-fremdsprachige-vertraege-bilingual) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `kompendium-13-vaf-kommandocenter-bis-vaf-platzhalterlogik` | vertragsausfueller: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (vaf-kommandocenter, vaf-mehrsprachige-vertraege-spezial, vaf-platzhalterlogik-bauleiter) und bewahrt deren Workflows, Normanker, Prüfprogramme und A... |
| `kompendium-14-vaf-quality-gate-bis-vaf-rueckfrageninter` | vertragsausfueller: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (vaf-quality-gate, vaf-redline-qa, vaf-rueckfrageninterview) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-15-vaf-template-erkennu-bis-vaf-track-changes-nu` | vertragsausfueller: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (vaf-template-erkennung, vaf-template-format-und-source, vaf-track-changes-nur-nach-frage) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `kompendium-16-vaf-versionierung-ae-bis-vaf-versionierung-ae` | vertragsausfueller: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (vaf-versionierung-aenderungsverfolgung-spezial) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-sheets-livequellen-und-rechtsprechungscheck` | Sheets: Livequellen- und Rechtsprechungscheck im Plugin vertragsausfueller; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `vaf-clean-output` | Sauberen finalen Vertragsentwurf mit Ausfüllprotokoll erstellen: Anwendungsfall alle Felder sind ausgefüllt und Quality Gate hat grüne Ampel ergeben; nun wird bereinigte Clean-Version für Unterschrift oder Versand erstellt. §§ 125 ff. BG... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin vertragsausfueller: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin vertragsausfueller: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin vertragsausfueller: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin vertragsausfueller: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin vertragsausfueller: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin vertragsausfueller: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
