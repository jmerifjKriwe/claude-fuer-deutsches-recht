# aktenauszug-gerichtsverfahren

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`aktenauszug-gerichtsverfahren`) | [`aktenauszug-gerichtsverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aktenauszug-gerichtsverfahren.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

**Version:** 3.2.1
**Autor:** Klotzkette

---

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Plugin erscheint in der Plugin-Liste; alle 21 Skills sind sofort verfügbar.
4. Für Updates: neues ZIP herunterladen und Plugin ersetzen.
5. Hinweis: Das Plugin-ZIP muss direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten — nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Überblick

Das Plugin `aktenauszug-gerichtsverfahren` generiert strukturierte Aktenauszüge für deutsche Gerichtsverfahren. Es richtet sich an Rechtsanwältinnen und Rechtsanwälte, die sich schnell in ein neues oder übernommenes Mandat einarbeiten müssen.

**Einsatzgebiete:**

- Mandatswechsel und Übernahme von laufenden Verfahren
- Einarbeitung neuer Sachbearbeiter in komplexe Akten
- Vorbereitung auf mündliche Verhandlungen
- Strukturierung umfangreicher Akten vor Beratungsgesprächen
- Erstellung von Mandantenberichten zum Verfahrensstand

**Verfahrensarten:**

- Zivilverfahren (ZPO) inkl. Berufung, Revision, einstweilige Verfügung
- Strafverfahren (StPO) inkl. Revision und Wiederaufnahme
- Verwaltungsverfahren (VwGO) inkl. Berufung und Revision
- Arbeitsgerichtsverfahren (ArbGG) inkl. Urteilsverfahren und Beschlussverfahren
- Sozialgerichtsverfahren (SGG) inkl. Berufung und Eilrechtsschutz

## Skills-Übersicht

| Skill | Zweck |
| --- | --- |
| `aktenauszug-erstellen` | Hauptworkflow: erzeugt alle sechs Bausteine des strukturierten Aktenauszugs aus PDFs und Schriftsätzen |
| `verfahrensidentifikation` | Extrahiert Gericht Kammer Aktenzeichen Streitwert Parteien Instanz und Verfahrensart |
| `einleitungssatz-generator` | Verfasst einen prägnanten ein- bis zweiSatz-Kern des Rechtsstreits mit Hauptnorm |
| `verfahrenszusammenfassung-absatz` | Schreibt zusammenfassenden Absatz mit acht bis zehn Sätzen zu Hintergrund Streitstand prozessualer Lage und nächsten Schritten |
| `sachverhaltschronologie` | Chronologische Bullet-Liste aller wesentlichen außerprozessualen Tatsachen mit Datum und Fundstelle |
| `verfahrenschronologie` | Chronologische Bullet-Liste aller prozessualen Schritte mit hervorgehobenen Fristen |
| `parteivortrag-gegenueberstellung` | Tabelle mit Kläger- und Beklagtenposition zu jedem Streitpunkt |
| `beweismittel-gegenueberstellung` | Tabelle aller Beweisangebote (Zeugen Urkunden Sachverständige) nach Partei und Beweisthema |
| `rechtsargumente-gegenueberstellung` | Tabelle der Rechtsargumente beider Parteien mit Anspruchsgrundlagen Einwendungen Einreden und Rechtsprechungsnachweisen |
| `fristen-und-terminkalender` | Identifiziert und hebt alle prozessrelevanten Fristen und Termine hervor |
| `anlagenverzeichnis-extrakt` | Vollständiges Anlagenverzeichnis aller K-/B-Anlagen mit Inhalt und Fundstelle |
| `schwerpunktthemen-identifikation` | Identifiziert drei bis fünf zentrale Rechtsfragen ohne Erfolgsprognose |
| `neutralitaetspruefung` | Prüft den Aktenauszug auf unzulässige Wertungen und Prognosen und schlägt Korrekturen vor |
| `aktenauszug-strukturpruefung` | Vollständigkeitsprüfung aller sechs Bausteine und Qualitätsgrundsätze |
| `zivilprozess-modus` | ZPO-spezifische Einstellungen für ordentliche Klage Berufung Revision und einstweilige Verfügung |
| `strafprozess-modus` | StPO-spezifische Einstellungen für Anklageverfahren Hauptverhandlung und Revision |
| `verwaltungsprozess-modus` | VwGO-spezifische Einstellungen mit Vorverfahren aufschiebender Wirkung und Berufungszulassung |
| `arbeitsgerichtsverfahren-modus` | ArbGG-spezifische Einstellungen mit Gütetermin KSchG-Dreiwochenfrist und Beschlussverfahren |
| `sozialgerichtsverfahren-modus` | SGG-spezifische Einstellungen mit Widerspruchsverfahren Amtsermittlung und Eilrechtsschutz |
| `anwaltsschriftsatz-stilrichtlinie` | Verbindliche Stilregeln für Sprache Gliederung Nomenklatur und Markdown-Formatierung |

## Methodik

Ausführliche Erläuterung der Methodik unter [references/methodik.md](references/methodik.md).

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Beispielprompt

```
Erstelle einen strukturierten Aktenauszug für das anhängende Verfahren vor dem Landgericht Frankfurt am Main (Az. 3 O 456/23). Die Akte enthält Klageschrift, Klageerwiderung und den Beweisbeschluss vom 15.09.2023. Verwende den Zivilprozess-Modus.
```

## Disclaimer

Dieses Plugin erstellt keine Rechtsberatung und gibt keine Erfolgsprognose ab. Die erstellten Aktenauszüge sind Arbeitsinstrumente, die der Prüfung und Freigabe durch den zuständigen Rechtsanwalt bedürfen. Das Plugin ersetzt nicht die eigene Aktenlektüre.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-02-workflow-mandantenko-bis-akzg-multiparteienve` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, akzg-multiparteienverfahren-konsolidierung-spezial) und bewahrt deren Work... |
| `kompendium-03-arbeitsgerichtsverfa-bis-sozialgerichtsverfah` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (arbeitsgerichtsverfahren-modus, fristen-und-terminkalender, sozialgerichtsverfahren-modus) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-04-spezial-erstellen-fr-bis-spezial-verfahrensge` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (spezial-erstellen-fristennotiz-und-naechster-schritt, spezial-gerichtsverfahren-fristen-form-und-zustaendigkeit, spezial-verfahrensgeschi... |
| `kompendium-05-spezial-verfahrensid-bis-verfahrenschronologi` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (spezial-verfahrensidentifikation-dokumentenmatrix, spezial-verfahrenszusammenfassung-rechtsweg-register, verfahrenschronologie) und bewah... |
| `kompendium-06-verfahrensidentifika-bis-aktenauszug-erstelle` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (verfahrensidentifikation, verfahrenszusammenfassung-absatz, aktenauszug-erstellen) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-07-aktenauszug-struktur-bis-akzg-vertraulichkeit` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (aktenauszug-strukturpruefung, akzg-aktenauszug-bauleiter, akzg-vertraulichkeit-redaction-spezial) und bewahrt deren Workflows, Normanker,... |
| `kompendium-08-akzg-zeitstrahl-chec-bis-anwaltsschriftsatz-s` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (akzg-zeitstrahl-checkliste, anlagenverzeichnis-extrakt, anwaltsschriftsatz-stilrichtlinie) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-09-beweismittel-gegenue-bis-neutralitaetspruefun` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (beweismittel-gegenueberstellung, einleitungssatz-generator, neutralitaetspruefung) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-10-parteivortrag-gegenu-bis-sachverhaltschronolo` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (parteivortrag-gegenueberstellung, rechtsargumente-gegenueberstellung, sachverhaltschronologie) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-11-schwerpunktthemen-id-bis-spezial-aktenauszug` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (schwerpunktthemen-identifikation, spezial-akten-mandantenkommunikation-entscheidungsvorlage, spezial-aktenauszug-tatbestand-beweis-und-be... |
| `kompendium-12-spezial-anwaltsschri-bis-spezial-einleitungss` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-anwaltsschriftsatz-beweislast-und-darlegungslast, spezial-beweismittel-mehrparteien-konflikt-und-interessen, spezial-einleitungss... |
| `kompendium-13-spezial-gegenueberst-bis-spezial-rechtsargume` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-gegenueberstellung-zahlen-schwellen-und-berechnung, spezial-parteivortraege-compliance-dokumentation-und-akte, spezial-rechtsargu... |
| `kompendium-14-spezial-sachverhalts-bis-spezial-stilrichtlin` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-sachverhaltschronologie-textbausteine, spezial-schnelle-formular-portal-und-einreichung, spezial-stilrichtlinie-sonderfall-und-ed... |
| `kompendium-15-spezial-strukturiert-bis-verwaltungsprozess-m` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-strukturierter-erstpruefung-und-mandatsziel, strafprozess-modus, verwaltungsprozess-modus) und bewahrt deren Workflows, Normanker... |
| `kompendium-16-zivilprozess-modus-bis-zivilprozess-modus` | aktenauszug-gerichtsverfahren: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (zivilprozess-modus) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-einarbeitung-red-team-und-qualitaetskontrolle` | Einarbeitung: Red-Team und Qualitätskontrolle im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-tabellarische-livequellen-und-rechtsprechungscheck` | Tabellarische: Livequellen- und Rechtsprechungscheck im Plugin aktenauszug gerichtsverfahren; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin aktenauszug-gerichtsverfahren: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin aktenauszug-gerichtsverfahren: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin aktenauszug-gerichtsverfahren: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin aktenauszug-gerichtsverfahren: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin aktenauszug-gerichtsverfahren: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin aktenauszug-gerichtsverfahren: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
