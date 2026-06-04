# VerkehrsOWi-Verteidiger

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verkehrsowi-verteidiger`) | [`verkehrsowi-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehrsowi-verteidiger.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Norderhof-Tannenmoor — Abstandsverstoß Section Control BAB 7 Bispingen, Bußgeld und Fahrverbot** (`verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof`) | [Gesamt-PDF lesen](../testakten/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof/gesamt-pdf/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof_gesamt.pdf) | [`testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof.zip) |
| **VerkehrsOWi – Qualifizierter Rotlichtverstoß, Tempoüberschreitung und Fahrverbot** (`verkehrsowi-rotlicht-tempo`) | [Gesamt-PDF lesen](../testakten/verkehrsowi-rotlicht-tempo/gesamt-pdf/verkehrsowi-rotlicht-tempo_gesamt.pdf) | [`testakte-verkehrsowi-rotlicht-tempo.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-rotlicht-tempo.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein freistehender Verteidigungsassistent für Verkehrsordnungswidrigkeiten: vom Anhörungsbogen über Einspruch, Akteneinsicht, Messakte und Punkte bis zur Amtsgerichtsverhandlung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn Register, Kanzleisoftware, beA, E-Mail, Datenraum oder Aktenexport fehlen, arbeitet es mit manuellen Uploads oder mit einem klar gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `verkehrsowi-kommandocenter` starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nicht raten lassen, sondern mit der passenden Vorlage nachfordern oder Simulation ausdrücklich aktivieren.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `verkehrsowi-kommandocenter` - VerkehrsOWi-Kommandocenter
- `verkehrsowi-aktenanlage` - Aktenanlage und Dokumentenregister
- `verkehrsowi-anhoerung-bussgeldbescheid` - Anhörung und Bußgeldbescheid prüfen
- `verkehrsowi-fristen-einspruch` - Fristen und Einspruch
- `verkehrsowi-verjaehrung-zustellung` - Verjährung und Zustellung
- `verkehrsowi-akteneinsicht-messakte` - Akteneinsicht und Messakte
- `verkehrsowi-messverfahren-geschwindigkeit` - Geschwindigkeitsmessung
- `verkehrsowi-rotlicht-abstand-handy` - Rotlicht, Abstand und Handy
- `verkehrsowi-alkohol-drogen-24a` - Alkohol und Drogen nach § 24a StVG
- `verkehrsowi-fahreridentifizierung` - Fahreridentifizierung
- `verkehrsowi-punkte-fahrverbot-flensburg` - Punkte, Fahrverbot und Flensburg
- `verkehrsowi-haertefall-fahrverbot` - Härtefall beim Fahrverbot
- `verkehrsowi-beweisverwertung-standardisiert` - Beweisverwertung und Standardisierung
- `verkehrsowi-zeugen-polizei-strategie` - Zeugen- und Polizeibefragung
- `verkehrsowi-hauptverhandlung-amtsgericht` - Hauptverhandlung vor dem Amtsgericht
- `verkehrsowi-rechtsbeschwerde` - Rechtsbeschwerde
- `verkehrsowi-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `verkehrsowi-mandantenkommunikation` - Mandantenkommunikation
- `verkehrsowi-simulation-training` - Simulation und Training
- `verkehrsowi-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/verkehrsowi-mandatskarte.md` - VerkehrsOWi-Mandatskarte
- `assets/templates/frist-und-verjaehrung.md` - Fristen- und Verjährungsblatt
- `assets/templates/anhoerungsbogen-check.md` - Anhörungsbogen-Check
- `assets/templates/bussgeldbescheid-pruefung.md` - Bußgeldbescheid-Prüfung
- `assets/templates/einspruch-owig-67.md` - Einspruch nach § 67 OWiG
- `assets/templates/akteneinsicht-messakte.md` - Akteneinsicht und Messakte
- `assets/templates/messverfahren-checkliste.md` - Messverfahren-Checkliste
- `assets/templates/fahreridentifizierung.md` - Fahreridentifizierung
- `assets/templates/punkte-fahrverbot-matrix.md` - Punkte- und Fahrverbotsmatrix
- `assets/templates/haertefall-fahrverbot.md` - Härtefallpaket Fahrverbot
- `assets/templates/zeugen-polizei-fragenkatalog.md` - Zeugen- und Polizeifragen
- `assets/templates/hauptverhandlung-amtsgericht.md` - Hauptverhandlung Amtsgericht
- `assets/templates/rechtsbeschwerde-check.md` - Rechtsbeschwerde-Check
- `assets/templates/rechtsprechungsrecherche.md` - Rechtsprechungsrecherche
- `assets/templates/mandantenanschreiben.md` - Mandantenanschreiben
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

## Arbeitsakte

Zum Arbeiten liegt die Akte unter `testakten/verkehrsowi-rotlicht-tempo`. Sie wird im Release als `testakte-verkehrsowi-rotlicht-tempo.zip` bereitgestellt und ist kein Bestandteil des Plugin-ZIPs.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Au... |
| `kompendium-02-workflow-mandantenko-bis-verkehrsowi-rechtspr` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, verkehrsowi-rechtsprechungsrecherche) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-03-spezial-anhoerung-fr-bis-verkehrsowi-messverf` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-anhoerung-fristen-form-und-zustaendigkeit, verkehrsowi-fristen-einspruch, verkehrsowi-messverfahren-geschwindigkeit) und bewahrt deren... |
| `kompendium-04-vowi-tempomessverfah-bis-verkehrsowi-anhoerun` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (vowi-tempomessverfahren-fehlerquellen-spezial, spezial-bussgeldbescheid-tatbestand-beweis-und-belege, verkehrsowi-anhoerung-bussgeldbescheid) u... |
| `kompendium-05-vowi-bussgeldbeschei-bis-verkehrsowi-quality` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (vowi-bussgeldbescheid-pruefung-bauleiter, verkehrsowi-kommandocenter, verkehrsowi-quality-gate) und bewahrt deren Workflows, Normanker, Prüfpro... |
| `kompendium-06-vowi-handyverstoss-s-bis-spezial-alkohol-comp` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (vowi-handyverstoss-spezial, spezial-akteneinsicht-internationaler-bezug-und-schnittstellen, spezial-alkohol-compliance-dokumentation-und-akte)... |
| `kompendium-07-spezial-amtsgericht-bis-spezial-einspruch-do` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (spezial-amtsgericht-mandantenkommunikation-entscheidungsvorlage, spezial-drogen-mehrparteien-konflikt-und-interessen, spezial-einspruch-dokumen... |
| `kompendium-08-spezial-fahrverbot-b-bis-spezial-handy-zahlen` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (spezial-fahrverbot-behoerden-gericht-und-registerweg, spezial-geschwindigkeit-verhandlung-vergleich-und-eskalation, spezial-handy-zahlen-schwel... |
| `kompendium-09-spezial-hauptverhand-bis-spezial-messung-fahr` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (spezial-hauptverhandlung-sonderfall-und-edge-case, spezial-messakte-formular-portal-und-einreichung, spezial-messung-fahrverbot-punkte) und bew... |
| `kompendium-10-spezial-punkte-risik-bis-spezial-verkehrsowi` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-punkte-risikoampel-und-gegenargumente, spezial-rotlicht-schriftsatz-brief-und-memo-bausteine, spezial-verkehrsowi-erstpruefung-und-mand... |
| `kompendium-11-spezial-verteidiger-bis-verkehrsowi-aktenein` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-verteidiger-beweislast-und-darlegungslast, verkehrsowi-aktenanlage, verkehrsowi-akteneinsicht-messakte) und bewahrt deren Workflows, No... |
| `kompendium-12-verkehrsowi-alkohol-bis-verkehrsowi-fahrerid` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (verkehrsowi-alkohol-drogen-24a, verkehrsowi-beweisverwertung-standardisiert, verkehrsowi-fahreridentifizierung) und bewahrt deren Workflows, No... |
| `kompendium-13-verkehrsowi-haertefa-bis-verkehrsowi-mandante` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (verkehrsowi-haertefall-fahrverbot, verkehrsowi-hauptverhandlung-amtsgericht, verkehrsowi-mandantenkommunikation) und bewahrt deren Workflows, N... |
| `kompendium-14-verkehrsowi-punkte-f-bis-verkehrsowi-rotlicht` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (verkehrsowi-punkte-fahrverbot-flensburg, verkehrsowi-rechtsbeschwerde, verkehrsowi-rotlicht-abstand-handy) und bewahrt deren Workflows, Normank... |
| `kompendium-15-verkehrsowi-simulati-bis-verkehrsowi-zeugen-p` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (verkehrsowi-simulation-training, verkehrsowi-verjaehrung-zustellung, verkehrsowi-zeugen-polizei-strategie) und bewahrt deren Workflows, Normank... |
| `kompendium-16-vowi-akteneinsicht-r-bis-vowi-akteneinsicht-r` | verkehrsowi-verteidiger: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (vowi-akteneinsicht-rohmessdaten-leitfaden) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-abstand-livequellen-und-rechtsprechungscheck` | Abstand: Livequellen- und Rechtsprechungscheck im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-zeugenstrategie-red-team-und-qualitaetskontrolle` | Zeugenstrategie: Red-Team und Qualitätskontrolle im Plugin verkehrsowi verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin verkehrsowi-verteidiger: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin verkehrsowi-verteidiger: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin verkehrsowi-verteidiger: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin verkehrsowi-verteidiger: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin verkehrsowi-verteidiger: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin verkehrsowi-verteidiger: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
