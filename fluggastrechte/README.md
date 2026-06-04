# Fluggastrechte

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fluggastrechte`) | [`fluggastrechte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fluggastrechte.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Fluggastrechte – Familie Bräutigam-Zaytuna** (`fluggastrechte-familie-braeutigam`) | [Gesamt-PDF lesen](../testakten/fluggastrechte-familie-braeutigam/gesamt-pdf/fluggastrechte-familie-braeutigam_gesamt.pdf) | [`testakte-fluggastrechte-familie-braeutigam.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fluggastrechte-familie-braeutigam.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Fluggastrechte selber geltend machen — VO (EG) Nr. 261/2004 plus EuGH-Rspr. Tickets erfassen Annullierung vs Verspätung prüfen außergewöhnliche Umstände Distanz und Ausgleich Forderungsschreiben Mahnung Klage Amtsgericht. Vollmacht Familie. Katalog Airline-Standardausreden.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `airline-standardausreden-pruefen` | Katalog typischer Standardausreden der Fluggesellschaften mit Gegenargumenten und Pinpoint auf EuGH-Rechtsprechung. Behandelt technischer Defekt wilder Streik Streik der Gewerkschaft Crew-Engpass verdeckter Konstrukti… |
| Rechtsprechung live prüfen | Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren. |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| `ausnahmen-aussergewoehnliche-umstaende-pruefen` | Prüft die Einrede außergewöhnliche Umstände nach Art. 5 Abs. 3 VO 261/2004. Differenziert zwischen Wetter Vulkanasche Vogelschlag Streik Flugsicherung Streik der eigenen Mitarbeiter wilder Streik technischem Defek… |
| `distanz-und-ausgleich-berechnen` | Berechnet die Ausgleichszahlung nach Art. 7 VO 261/2004. Distanzbestimmung nach Großkreisrechnung zwischen Abflug- und Zielflughafen. Drei Stufen 250 EUR bis 1500 km / 400 EUR mehr als 1500 km innergemeinschaftlich o… |
| `forderungsschreiben-erste-stufe` | Erstes Forderungsschreiben an die Airline. Erfasst Anspruchsteller (alle Passagiere mit Vollmachten) Anspruchsgrundlage Art. 7 VO 261/2004 konkrete Berechnung Frist zur Zahlung (typisch zwei Wochen) Bankverbindung. In… |
| `forderungsschreiben-mahnung` | Zweite Stufe nach Ablauf der Frist aus dem ersten Forderungsschreiben oder nach erfolgloser Reaktion der Airline. Setzt Nachfrist (typisch zehn Tage) bezieht sich auf die erste Forderung weist Verzugszinsen aus und dr… |
| `fluggastrechte-kaltstart-interview` | Kaltstart-Interview für das Fluggastrechte-Plugin. Klärt Anwendungsrolle (eigener Fluggastrechte-Anspruch / Vertretung Familie / Mitreisende). Erfasst Buchungsstammdaten Vertragspartner (Airline IATA-Code) und Reise… |
| `klage-amtsgericht-fluggast` | Klageentwurf zum Amtsgericht in Fluggastrechtsangelegenheiten. Sachliche Zuständigkeit § 23 Nr. 1 GVG bei Streitwert bis zehntausend Euro (i. d. F. seit 01.01.2026). Örtlich wahlweise Abflughafen oder Zielflughafen … |
| `ticket-und-fluginformationen-erfassen` | Erfasst die Falldaten aus hochgeladenen Tickets Buchungsbestätigungen Boardingpässe PDF-Scans Foto-Belegen. Extrahiert Buchungscode (PNR) Flugnummer Datum Abflughafen Zielflughafen geplante Abflugzeit geplante Ankun… |
| `vollmacht-familienmitglieder` | Erzeugt Vollmachten für Mitreisende (Familienmitglieder Freunde) damit der Hauptansprechpartner deren Fluggastrechtsanspruch im Schriftverkehr und im gerichtlichen Verfahren mitvertreten kann. Pro Person eigene Vollm… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `fluggastrechte-anlagen-bauen` | Baut aus den Belegen eines Fluggastrechte-Mandats ein beA-konformes Anlagenkonvolut. Verwendet zum bestehenden Schriftsatz (Forderungsschreiben Mahnung Klage) die Belege Buchungsbestätigung Boardingpass Annullierungsbestätigung E-Mail-Ve... |
| `fluggastrechte-kaltstart-interview` | Kaltstart-Interview für das Fluggastrechte-Plugin. Klaert Anwendungsrolle (eigener Fluggastrechte-Anspruch / Vertretung Familie / Mitreisende). Erfasst Buchungsstammdaten Vertragspartner (Airline IATA-Code) und Reiseplan-Konvention. Schr... |
| `kompendium-01-allgemein-bis-workflow-chronologie` | fluggastrechte: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-anschluss-skills-router, workflow-chronologie-und-belegmatrix) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-02-workflow-fristen-und-bis-workflow-redteam-qua` | fluggastrechte: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-fristen-und-risikoampel, workflow-mandantenkommunikation, workflow-redteam-qualitygate) und bewahrt deren Workflows, Normanker, Prüfprogramme u... |
| `kompendium-03-spezial-rechtsprechu-bis-spezial-geltend-fris` | fluggastrechte: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-rechtsprechung-beweislast-und-darlegungslast, vorverlegung-flug-rechtsprechung, spezial-geltend-fristen-form-und-zustaendigkeit) und bewahrt der... |
| `kompendium-04-spezial-verifikation-bis-airline-bonitaet-und` | fluggastrechte: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (spezial-verifikation-fristennotiz-und-naechster-schritt, abtretung-an-fluggastportal-spezial, airline-bonitaet-und-vollstreckung) und bewahrt deren Work... |
| `kompendium-05-airline-standardausr-bis-anschlussflug-und-re` | fluggastrechte: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (airline-standardausreden-pruefen, annullierung-oder-verspaetung-einordnen, anschlussflug-und-reiseplan) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-06-ausnahmen-aussergewo-bis-distanz-und-ausgleic` | fluggastrechte: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (ausnahmen-aussergewoehnliche-umstaende-pruefen, aussergewoehnliche-umstaende-strikt, distanz-und-ausgleich-berechnen) und bewahrt deren Workflows, Norma... |
| `kompendium-07-flug-anschlussflug-c-bis-flug-ausserordentlic` | fluggastrechte: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (flug-anschlussflug-codeshare-spezial, flug-anspruch-uebersicht, flug-ausserordentlicher-umstand-leitfaden) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-08-flug-massenklage-pro-bis-forderungsschreiben` | fluggastrechte: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (flug-massenklage-prozessfinanzierung-spezial, fluggastrechte-einfuehrung-vo-261, forderungsschreiben-erste-stufe) und bewahrt deren Workflows, Normanker... |
| `kompendium-09-forderungsschreiben-bis-pauschalreise-statt` | fluggastrechte: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (forderungsschreiben-mahnung, klage-amtsgericht-fluggast, pauschalreise-statt-flug-pruefen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Aus... |
| `kompendium-10-rechtsweg-und-gerich-bis-spezial-ausgleich-in` | fluggastrechte: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (rechtsweg-und-gerichtsstand-fluggast, spezial-annullierung-schriftsatz-brief-und-memo-bausteine, spezial-ausgleich-internationaler-bezug-und-schnittstel... |
| `kompendium-11-spezial-aussergewoeh-bis-spezial-erfassen-beh` | fluggastrechte: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-aussergewoehnliche-zahlen-schwellen-und-berechnung, spezial-distanz-mehrparteien-konflikt-und-interessen, spezial-erfassen-behoerden-gericht-und... |
| `kompendium-12-spezial-fluggastrech-bis-spezial-klage-mandan` | fluggastrechte: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-fluggastrechte-erstpruefung-und-mandatsziel, spezial-forderungsschreiben-formular-portal-und-einreichung, spezial-klage-mandantenkommunikation-e... |
| `kompendium-13-spezial-live-sonderf-bis-spezial-mahnung-red` | fluggastrechte: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-live-sonderfall-und-edge-case, spezial-machen-dokumentenmatrix-und-lueckenliste, spezial-mahnung-red-team-und-qualitaetskontrolle) und bewahrt d... |
| `kompendium-14-spezial-selber-tatbe-bis-spezial-umstaende-co` | fluggastrechte: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-selber-tatbestand-beweis-und-belege, spezial-tickets-risikoampel-und-gegenargumente, spezial-umstaende-compliance-dokumentation-und-akte) und be... |
| `kompendium-15-spezial-verspaetung-bis-vollmacht-familienmi` | fluggastrechte: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-verspaetung-verhandlung-vergleich-und-eskalation, ticket-und-fluginformationen-erfassen, vollmacht-familienmitglieder) und bewahrt deren Workflo... |
| `spezial-kaltstart-abschlussprodukt-und-uebergabe` | Kaltstart: Abschlussprodukt und Übergabe im Plugin fluggastrechte; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-pruefen-livequellen-und-rechtsprechungscheck` | Pruefen: Livequellen- und Rechtsprechungscheck im Plugin fluggastrechte; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin fluggastrechte: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin fluggastrechte: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin fluggastrechte: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin fluggastrechte: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin fluggastrechte: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
