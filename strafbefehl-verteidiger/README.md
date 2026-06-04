# Strafbefehl-Verteidiger

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strafbefehl-verteidiger`) | [`strafbefehl-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafbefehl-verteidiger.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **LUMEN Studios GmbH — Insolvenz- und Wirtschaftsstrafverfahren** (`lumen-studios-insolvenz-strafverfahren`) | [Gesamt-PDF lesen](../testakten/lumen-studios-insolvenz-strafverfahren/gesamt-pdf/lumen-studios-insolvenz-strafverfahren_gesamt.pdf) | [`testakte-lumen-studios-insolvenz-strafverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) |
| **Strafbefehl – Ladendiebstahl und Fahrerflucht** (`strafbefehl-ladendiebstahl-fahrerflucht`) | [Gesamt-PDF lesen](../testakten/strafbefehl-ladendiebstahl-fahrerflucht/gesamt-pdf/strafbefehl-ladendiebstahl-fahrerflucht_gesamt.pdf) | [`testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein freistehender Strafbefehls-Assistent für Kanzleien: vom Fristnotruf über Akteneinsicht und Einspruch bis zur beschränkten Rechtsfolgenstrategie oder Hauptverhandlung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn Register, Kanzleisoftware, beA, E-Mail, Datenraum oder Aktenexport fehlen, arbeitet es mit manuellen Uploads oder mit einem klar gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `strafbefehl-kommandocenter` starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nicht raten lassen, sondern mit der passenden Vorlage nachfordern oder Simulation ausdrücklich aktivieren.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `strafbefehl-kommandocenter` - Strafbefehl-Kommandocenter
- `strafbefehl-aktenanlage` - Aktenanlage Strafbefehl
- `strafbefehl-fristen-einspruch` - Frist und Einspruch nach § 410 StPO
- `strafbefehl-akteneinsicht-147` - Akteneinsicht
- `strafbefehl-zulaessigkeit-407` - Zulässigkeit des Strafbefehls
- `strafbefehl-inhalt-409-pruefung` - Inhaltsprüfung nach § 409 StPO
- `strafbefehl-einspruch-beschraenkung` - Einspruch beschränken oder nicht
- `strafbefehl-wiedereinsetzung` - Wiedereinsetzung
- `strafbefehl-pflichtverteidiger` - Pflichtverteidigung
- `strafbefehl-polizeifilmerei-201-kug` - Film-, Foto- und Tonaufnahmen von Polizeieinsätzen
- `strafbefehl-tagessaetze-geldstrafe` - Tagessätze und Geldstrafe
- `strafbefehl-nebenfolgen-fahrerlaubnis` - Nebenfolgen
- `strafbefehl-beweis-und-einlassung` - Beweis und Einlassung
- `strafbefehl-zeugen-befragungsstrategie` - Zeugenbefragung
- `strafbefehl-hauptverhandlung-vorbereitung` - Hauptverhandlung vorbereiten
- `strafbefehl-abwesenheit-vertretung` - Abwesenheit und Vertretung
- `strafbefehl-einstellung-153-153a-170` - Einstellung und Verständigung
- `strafbefehl-deal-verstaendigung` - Gesprächsstrategie mit Gericht und Staatsanwaltschaft
- `strafbefehl-rechtsmittel-nach-urteil` - Rechtsmittel nach Urteil
- `strafbefehl-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `strafbefehl-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/strafbefehl-mandatskarte.md` - Strafbefehl-Mandatskarte
- `assets/templates/frist-einspruch-410.md` - Frist und Einspruch nach § 410 StPO
- `assets/templates/akteneinsicht-147.md` - Akteneinsicht nach § 147 StPO
- `assets/templates/strafbefehl-inhaltspruefung.md` - Inhaltsprüfung Strafbefehl
- `assets/templates/einspruch-unbeschraenkt.md` - Unbeschränkter Einspruch
- `assets/templates/einspruch-beschraenkt.md` - Beschränkter Einspruch
- `assets/templates/wiedereinsetzung.md` - Wiedereinsetzung
- `assets/templates/pflichtverteidiger-check.md` - Pflichtverteidiger-Check
- `assets/templates/tagessaetze.md` - Tagessatzprüfung
- `assets/templates/einlassungsstrategie.md` - Einlassungsstrategie
- `assets/templates/zeugen-fragenkatalog.md` - Zeugenfragen
- `assets/templates/hauptverhandlung-plan.md` - Hauptverhandlung
- `assets/templates/einstellung-153-153a.md` - Einstellung nach §§ 153, 153a StPO
- `assets/templates/nebenfolgen-fahrerlaubnis.md` - Nebenfolgen
- `assets/templates/rechtsmittel-nach-urteil.md` - Rechtsmittel nach Urteil
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Au... |
| `kompendium-02-workflow-mandantenko-bis-strafbefehl-rechtspr` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, strafbefehl-rechtsprechungsrecherche) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-03-spezial-gegen-friste-bis-strafbefehl-aktenanl` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-gegen-fristen-form-und-zustaendigkeit, strafbefehl-fristen-einspruch, strafbefehl-aktenanlage) und bewahrt deren Workflows, Normanker,... |
| `kompendium-04-strafbefehl-kommando-bis-spezial-akteneinsich` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (strafbefehl-kommandocenter, strafbefehl-quality-gate, spezial-akteneinsicht-behoerden-gericht-und-registerweg) und bewahrt deren Workflows, Nor... |
| `kompendium-05-spezial-deal-beweisl-bis-spezial-einspruchsen` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (spezial-deal-beweislast-und-darlegungslast, spezial-einspruch-risikoampel-und-gegenargumente, spezial-einspruchsentscheidung-und-folgen) und be... |
| `kompendium-06-spezial-einstellung-bis-spezial-hauptverhand` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (spezial-einstellung-compliance-dokumentation-und-akte, spezial-fahrerlaubnis-mandantenentscheidung, spezial-hauptverhandlung-international-schn... |
| `kompendium-07-spezial-nebenfolgen-bis-spezial-strafbefehls` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (spezial-nebenfolgen-verhandlung-vergleich-und-eskalation, spezial-strafbefehl-dokumentenmatrix-und-lueckenliste, spezial-strafbefehls-erstpruef... |
| `kompendium-08-spezial-tagessaetze-bis-spezial-verteidiger` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (spezial-tagessaetze-schriftsatz-brief-und-memo-bausteine, spezial-verstaendigung-sonderfall-und-edge-case, spezial-verteidiger-formular-portal-... |
| `kompendium-09-spezial-verteidigung-bis-spezial-zeugenstrate` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (spezial-verteidigung-tatbestand-beweis-und-belege, spezial-wiedereinsetzung-zahlen-schwellen-und-berechnung, spezial-zeugenstrategie-mehrpartei... |
| `kompendium-10-stbv-einspruch-straf-bis-stbv-strafbefehl-aus` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (stbv-einspruch-strafbefehl-leitfaden, stbv-fahrerlaubnis-bei-strafbefehl-spezial, stbv-strafbefehl-auslaendischer-mandant-spezial) und bewahrt... |
| `kompendium-11-stbv-strafbefehl-pru-bis-strafbefehl-aktenein` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (stbv-strafbefehl-pruefung-bauleiter, strafbefehl-abwesenheit-vertretung, strafbefehl-akteneinsicht-147) und bewahrt deren Workflows, Normanker,... |
| `kompendium-12-strafbefehl-beweis-u-bis-strafbefehl-einspruc` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (strafbefehl-beweis-und-einlassung, strafbefehl-deal-verstaendigung, strafbefehl-einspruch-beschraenkung) und bewahrt deren Workflows, Normanker... |
| `kompendium-13-strafbefehl-einstell-bis-strafbefehl-inhalt-4` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (strafbefehl-einstellung-153-153a-170, strafbefehl-hauptverhandlung-vorbereitung, strafbefehl-inhalt-409-pruefung) und bewahrt deren Workflows,... |
| `kompendium-14-strafbefehl-nebenfol-bis-strafbefehl-polizeif` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (strafbefehl-nebenfolgen-fahrerlaubnis, strafbefehl-pflichtverteidiger, strafbefehl-polizeifilmerei-201-kug) und bewahrt deren Workflows, Norman... |
| `kompendium-15-strafbefehl-rechtsmi-bis-strafbefehl-wiederei` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (strafbefehl-rechtsmittel-nach-urteil, strafbefehl-tagessaetze-geldstrafe, strafbefehl-wiedereinsetzung) und bewahrt deren Workflows, Normanker,... |
| `kompendium-16-strafbefehl-zeugen-b-bis-strafbefehl-zulaessi` | strafbefehl-verteidiger: Konsolidiertes Skill-Kompendium 16; bündelt 2 frühere Spezialskills (strafbefehl-zeugen-befragungsstrategie, strafbefehl-zulaessigkeit-407) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-aktenanlage-red-team-und-qualitaetskontrolle` | Aktenanlage: Red-Team und Qualitätskontrolle im Plugin strafbefehl verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-pflichtverteidigung-livequellen-und-rechtsprechungscheck` | Pflichtverteidigung: Livequellen- und Rechtsprechungscheck im Plugin strafbefehl verteidiger; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin strafbefehl-verteidiger: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin strafbefehl-verteidiger: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin strafbefehl-verteidiger: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin strafbefehl-verteidiger: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin strafbefehl-verteidiger: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin strafbefehl-verteidiger: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
