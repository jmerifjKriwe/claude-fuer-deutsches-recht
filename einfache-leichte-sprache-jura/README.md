# Einfache und Leichte Sprache für juristische Texte

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`einfache-leichte-sprache-jura`) | [`einfache-leichte-sprache-jura.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/einfache-leichte-sprache-jura.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Juristischer Mandantenbrief in Einfacher und Leichter Sprache** (`einfache-leichte-sprache-jura-mandantenbrief`) | [Gesamt-PDF lesen](../testakten/einfache-leichte-sprache-jura-mandantenbrief/gesamt-pdf/einfache-leichte-sprache-jura-mandantenbrief_gesamt.pdf) | [`testakte-einfache-leichte-sprache-jura-mandantenbrief.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-einfache-leichte-sprache-jura-mandantenbrief.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für die Übertragung juristischer Texte in **Einfache
Sprache** oder **Leichte Sprache**. Es richtet sich an Kanzleien, Behörden,
Beratungsstellen, Legal-Design-Teams und alle, die rechtliche Informationen
verständlich, respektvoll und rechtlich belastbar erklären müssen.

## Showcase-Hinweis

Dieses Plugin ist ein Experiment und ein Showcase. Es ist ein Versuch, sich der
Ergebnisrichtung von Einfacher Sprache und Leichter Sprache anzunähern, ohne
eine Standardprüfung oder Konformitätsaussage zu behaupten. Make of this what
you will, dear users: Ihr müsst selbst beurteilen, ob Verfahren, Sprache und
Ergebnis für eure Zielgruppe, euer Medium und euren Rechtstext passen. You are
on your own.

## Zwei Modi

| Modus | Ziel |
| --- | --- |
| Einfache Sprache | Standardsprache bleibt erkennbar. Fachsprache wird erklärt. Der Text wird klarer, kürzer, besser gegliedert und zielgruppenorientiert. |
| Leichte Sprache | Deutlich stärkere Vereinfachung. Kurze Sätze, klare Zeilen, viel Orientierung, erklärtes Fachwort, möglichst eine Aussage pro Satz. Eine Prüfung durch Personen aus der Zielgruppe wird empfohlen. |

## Workflow

1. Ausgangstext hochladen oder einfügen.
2. Zielgruppe, Anlass, Medium und gewünschte Tiefe klären.
3. Juristische Bedeutungen sichern: Rechte, Pflichten, Fristen, Beträge,
   Rechtsfolgen, Zuständigkeiten und Handlungsoptionen.
4. Modus wählen: Einfache Sprache oder Leichte Sprache.
5. Übertragung erstellen.
6. Glossar und Warnhinweise ergänzen.
7. Qualitätsgate laufen lassen.
8. Bei Leichter Sprache: Nutzerprüfung als offenen Schritt markieren, wenn sie
   nicht tatsächlich erfolgt ist.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `elsj-kommandocenter` | steuert Intake, Moduswahl, Zielgruppe, Rechtsinhalt und Ausgabeformat |
| `elsj-einfache-sprache` | überträgt juristische Texte in Einfache Sprache |
| `elsj-leichte-sprache` | überträgt juristische Texte in Leichte Sprache |
| `elsj-juristische-sicherung` | verhindert Bedeutungsverlust bei Rechten, Pflichten, Fristen und Rechtsfolgen |
| `elsj-qualitaetsgate` | prüft Verständlichkeit, Struktur, Glossar, Ton und rechtliche Vollständigkeit |

## Hilfsskript

```bash
python einfache-leichte-sprache-jura/scripts/verstaendlichkeitscheck.py \
  testakten/einfache-leichte-sprache-jura-mandantenbrief/02_einfache_sprache.md \
  --mode einfache
```

Das Skript ist kein Normprüfer. Es findet typische Warnsignale:
lange Sätze, sehr lange Wörter, Passiv-Kandidaten, Nominalstil und fehlende
Orientierungselemente.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-chronologie` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, ls-bescheid-uebersetzen-workflow, workflow-chronologie-und-belegmatrix) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-02-workflow-fristen-und-bis-workflow-redteam-qua` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-fristen-und-risikoampel, workflow-mandantenkommunikation, workflow-redteam-qualitygate) und bewahrt deren Workflows, Normanker,... |
| `kompendium-03-elsj-sozialgerichtsv-bis-spezial-bauen-friste` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (elsj-sozialgerichtsverfahren, elsj-strafverfahren-beschuldigter, spezial-bauen-fristennotiz-und-naechster-schritt) und bewahrt deren Work... |
| `kompendium-04-spezial-einfache-fri-bis-elsj-kommandocenter` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (spezial-einfache-fristen-form-und-zustaendigkeit, elsj-bescheidmodus, elsj-kommandocenter) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-05-elsj-aufenthaltsrech-bis-elsj-einfache-sprach` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (elsj-aufenthaltsrecht-mandant, elsj-betreuung-vormundschaft, elsj-einfache-sprache) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-06-elsj-familienrecht-e-bis-elsj-kommunikation-m` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (elsj-familienrecht-erstgespraech, elsj-juristische-sicherung, elsj-kommunikation-mandant) und bewahrt deren Workflows, Normanker, Prüfpro... |
| `kompendium-07-elsj-leichte-sprache-bis-elsj-pruefkriterien` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (elsj-leichte-sprache, elsj-mietrecht-kuendigungserklaerung, elsj-pruefkriterien-fuer-qualitaet) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-08-elsj-qualitaetsgate-bis-elsj-satzbau-regeln` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (elsj-qualitaetsgate, elsj-rechtsnormen-einfach, elsj-satzbau-regeln) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemus... |
| `kompendium-09-elsj-uebersetzungsab-bis-elsj-zielgruppen-erk` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (elsj-uebersetzungsablauf, elsj-wortebene-haus-glossar, elsj-zielgruppen-erkennen) und bewahrt deren Workflows, Normanker, Prüfprogramme u... |
| `kompendium-10-ls-juristisches-glos-bis-ls-strafprozess-rech` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (ls-juristisches-glossar-bauen, ls-justizportal-pruefen-spezial, ls-strafprozess-rechte-erklaeren-spezial) und bewahrt deren Workflows, No... |
| `kompendium-11-spezial-experimentel-bis-spezial-jura-mandant` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-experimentelle-schriftsatz-brief-und-memo-bausteine, spezial-glossar-sonderfall-und-edge-case, spezial-jura-mandantenkommunikatio... |
| `kompendium-12-spezial-juristische-bis-spezial-klaeren-comp` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-juristische-erstpruefung-und-mandatsziel, spezial-juristisches-beweislast-und-darlegungslast, spezial-klaeren-compliance-dokument... |
| `kompendium-13-spezial-leichte-risi-bis-spezial-rechtsinhalt` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-leichte-risikoampel-und-gegenargumente, spezial-qualitaetsgate-formular-portal-und-einreichung, spezial-rechtsinhalt-mehrparteien... |
| `kompendium-14-spezial-sichern-inte-bis-spezial-standard-ver` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-sichern-internationaler-bezug-und-schnittstellen, spezial-sprache-dokumentenmatrix-und-lueckenliste, spezial-standard-verhandlung... |
| `kompendium-15-spezial-texte-tatbes-bis-spezial-zielgruppe-s` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-texte-tatbestand-beweis-und-belege, spezial-uebertragen-behoerden-gericht-und-registerweg, spezial-zielgruppe-sprachniveau-rechts... |
| `kompendium-16-spezial-zielgruppe-z-bis-spezial-zielgruppe-z` | einfache-leichte-sprache-jura: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (spezial-zielgruppe-zahlen-schwellen-und-berechnung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-annaeherung-livequellen-und-rechtsprechungscheck` | Annaeherung: Livequellen- und Rechtsprechungscheck im Plugin einfache leichte sprache jura; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-nutzen-red-team-und-qualitaetskontrolle` | Nutzen: Red-Team und Qualitätskontrolle im Plugin einfache leichte sprache jura; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin einfache-leichte-sprache-jura: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin einfache-leichte-sprache-jura: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin einfache-leichte-sprache-jura: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin einfache-leichte-sprache-jura: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin einfache-leichte-sprache-jura: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin einfache-leichte-sprache-jura: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
