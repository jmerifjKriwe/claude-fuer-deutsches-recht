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
| `aktenauszug-gerichtsverfahren-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `aktenauszug-gerichtsverfahren-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `aktenauszug-gerichtsverfahren-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `aktenauszug-gerichtsverfahren-output-waehlen` | Output wählen im Aktenauszug-Praxis: Diese Output-Weiche für Aktenauszug Gerichtsverfahren entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `aktenauszug-gerichtsverfahren-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `aktenauszug-gerichtsverfahren-spezial-verfahrensidentifikation` | Spezial Verfahrensidentifikation im Aktenauszug-Praxis: prüft konkret Verfahrensidentifikation, Verfahrenszusammenfassung, Erstellt eine chronologische Bullet-Liste aller. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und... |
| `aktenauszug-gerichtsverfahren-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `aktenauszug-mandantenkommunikation-redteam-qualitygate-akzg` | Mandantenkommunikation Redteam Qualitygate Akzg im Aktenauszug-Praxis: prüft konkret Mandantenkommunikation im Plugin, Red-Team Qualitygate im Plugin aktenauszug-gerichtsverfahren, Spezialfall Multiparteienverfahren Konsolidierung mehrer... |
| `aktenauszug-start-chronologie-fristen` | Start Chronologie Fristen im Aktenauszug-Praxis: prüft konkret Einstieg, Schnelltriage und Fallrouting im Aktenauszug, Chronologie und Belegmatrix im Plugin, Fristen- und Risikoampel im Plugin. Liefert priorisierten Output mit Norm-Pinpo... |
| `aktenauszug-strukturpruefung-akzg-bauleiter` | Strukturpruefung Akzg Bauleiter im Aktenauszug-Praxis: prüft konkret Fertig erstellten Aktenauszug auf Vollständigkeit prüfen, Bauleiter Aktenauszug fuer Gerichtsverfahren, Spezialfall Vertraulichkeit und Redaction in Aktenauszuegen. Lie... |
| `aktenauszug-verfahrensidentifikation-gericht` | Verfahrensidentifikation Gericht im Aktenauszug-Praxis: prüft konkret Extrahiert strukturiert alle Verfahrensstammdaten, Anwalt will sich schnell in Akte einarbeiten ohne, Anwalt oder Paralegal erhaelt Gerichtsakte Schriftsaetze. Liefert... |
| `akzg-zeitstrahl-anlagenverzeichnis-extrakt` | Akzg Zeitstrahl Anlagenverzeichnis Extrakt im Aktenauszug-Praxis: prüft konkret Checkliste Zeitstrahl in Aktenauszug, Anwalt sucht alle Anlagen K-/B-/AST-/AG-Verweise in der, Stilrichtlinie für den juristisch sauberen neutralen und. Lief... |
| `anwaltsschriftsatz-beweislast-beweismittel` | Anwaltsschriftsatz Beweislast Beweismittel im Aktenauszug-Praxis: prüft konkret Anwaltsschriftsatz, Beweismittel, Einleitungssatz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `arbeitsgerichtsverfahren-modus-terminkalender` | Arbeitsgerichtsverfahren Modus Terminkalender im Aktenauszug-Praxis: prüft konkret Aktenauszug für ArbGG-Verfahren erstellen, Anwalt will alle prozessrelevanten Fristen und Termine im, Aktenauszug für SGG-Verfahren erstellen. Liefert pri... |
| `beweismittel-gegenueberstellung` | Beweismittel Gegenueberstellung im Aktenauszug-Praxis: prüft konkret Anwalt will Beweisangebote aller Parteien uebersichtlich, Aktenauszug braucht praegnanten Einleitungssatz, Prüft einen erstellten Aktenauszug auf unzulässige. Liefert p... |
| `einarbeitung-fehlerkatalog` | Einarbeitung Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `erstellen-fristennotiz-gerichtsverfahren` | Erstellen Fristennotiz Gerichtsverfahren im Aktenauszug-Praxis: prüft konkret Erstellen, Gerichtsverfahren, Verfahrensgeschichte. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `gegenueberstellung-parteivortraege` | Gegenueberstellung Parteivortraege im Aktenauszug-Praxis: prüft konkret Gegenueberstellung, Parteivortraege, Rechtsargumente. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `parteivortrag-gegenueberstellung` | Parteivortrag Gegenueberstellung im Aktenauszug-Praxis: prüft konkret Erstellt eine Tabelle mit zwei Spalten (Klaegerseite und, Erstellt eine tabellarische Gegenüberstellung der, Erstellt eine chronologische Bullet-Liste aller. Liefert p... |
| `sachverhaltschronologie-textbausteine` | Sachverhaltschronologie Textbausteine im Aktenauszug-Praxis: prüft konkret Sachverhaltschronologie, Schnelle, Stilrichtlinie. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `schwerpunktthemen-identifikation-akten` | Schwerpunktthemen Identifikation Akten im Aktenauszug-Praxis: prüft konkret Anwalt braucht schnellen Überblick über drei bis fuenf, Akten, Aktenauszug. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `strukturierter-strafprozess-modus` | Strukturierter Strafprozess Modus im Aktenauszug-Praxis: prüft konkret Strukturierter, Aktenauszug für StPO-Verfahren erstellen, Aktenauszug für VwGO-Verfahren erstellen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und n... |
| `tabellarische-quellenkarte` | Tabellarische Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `zivilprozess-modus` | Zivilprozess Modus im Aktenauszug-Praxis: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
