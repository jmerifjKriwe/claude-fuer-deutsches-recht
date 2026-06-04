# Strafzumessung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strafzumessung`) | [`strafzumessung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafzumessung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Strafzumessung Bankert — Untreue, LG Frankfurt / BGH Revision** (`strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung`) | [Gesamt-PDF lesen](../testakten/strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung/gesamt-pdf/strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung_gesamt.pdf) | [`testakte-strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für die **Strafzumessung nach deutschem Strafrecht** — vom Strafbefehl bis zur großen Strafkammer. Adressaten: Strafverteidiger und Staatsanwaltschaft.

## Worum geht es?

Strafzumessung ist die zentrale richterliche Aufgabe nach Schuldspruch: Bestimmung von Strafart und Strafhoehe innerhalb des gesetzlichen Strafrahmens auf Grundlage der **Schuld** (§ 46 Abs. 1 Satz 1 StGB), unter Beruecksichtigung der **praeventiven Wirkungen** (§ 46 Abs. 1 Satz 2 StGB), nach den **Strafzumessungstatsachen** des § 46 Abs. 2 StGB und unter Beachtung des **Doppelverwertungsverbots** (§ 46 Abs. 3 StGB).

Das Plugin deckt die Strafzumessung vom Strafbefehlsverfahren ueber die Hauptverhandlung bis zur Vollstreckung ab, inklusive Bewaehrung, Strafmilderung, Regelbeispielen, Gesamtstrafenbildung, Verstaendigung und Jugendstrafrecht.

## Schnellstart

1. Mit `orientierung-strafzumessung-triage` einsteigen.
2. Rolle (Strafverteidigung, Staatsanwaltschaft) und Verfahrensstadium (Strafbefehl, Anklage, Hauptverhandlung, Urteil, Berufung, nachtraegliche Gesamtstrafe) angeben.
3. Den vom Triage-Skill empfohlenen Spezial-Skill aktivieren.
4. Bei Bedarf parallel mit den Plugins `strafbefehl-verteidiger` oder `fachanwalt-strafrecht` arbeiten.

## Enthaltene Skills

### Block A — Orientierung und Grundlagen
- `orientierung-strafzumessung-triage` — Einstieg, Triage, Spezial-Skill-Routing.
- `paragraph-46-stgb-grundsatz-strafzumessung` — § 46 StGB, Schuld als Grundlage.
- `strafzumessungs-tatsachen-46-ii-stgb` — Katalog § 46 Abs. 2 StGB.
- `strafrahmen-und-strafzumessungsstufen` — Strafrahmen-Logik vor jeder Zumessung.

### Block B — Geldstrafe
- `geldstrafe-tagessatzanzahl-bestimmen` — § 40 Abs. 1 StGB, Tagessatzanzahl als Schuldgroesse.
- `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` — § 40 Abs. 2 StGB, Nettoeinkommen / 30.
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Vorrang Geldstrafe; § 47 StGB.

### Block C — Freiheitsstrafe und Bewaehrung
- `freiheitsstrafe-strafmass-pruefen` — Konkrete Zumessung im Strafrahmen.
- `bewaehrung-56-stgb-positive-sozialprognose` — § 56 StGB.
- `bewaehrung-auflagen-und-weisungen-56b-c-stgb` — §§ 56b, 56c StGB.
- `bewaehrungswiderruf-56f-stgb` — § 56f StGB.
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — U-Haft-Anrechnung § 51 StGB, Reststrafenaussetzung § 57 StGB.

### Block D — Strafmilderung und Schaerfung
- `strafmilderung-49-stgb-zwingend-fakultativ` — § 49 StGB.
- `minder-schwerer-fall-und-besonders-schwerer-fall` — Strafrahmen-Modifikation.
- `regelbeispiele-rechtsprechung` — § 243 StGB, § 263 Abs. 3 StGB u.a.
- `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` — § 46a StGB; BGH 4 StR 232/25.

### Block E — Strafbefehl und kleine Verfahren
- `strafbefehl-strafzumessung-407-stpo` — Strafzumessung im Strafbefehl.
- `153a-stpo-einstellung-gegen-auflage` — Einstellung mit Auflage.

### Block F — Hauptverhandlung und Verstaendigung
- `verstaendigung-257c-stpo-strafzumessung` — § 257c StPO; BVerfG 2 BvR 2628/10; BGH 1 StR 525/11.
- `gestaendnis-und-strafmilderung` — Gestaendnis als Strafmilderungsgrund.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Strafurteil-Begruendung.

### Block G — Gesamtstrafenbildung
- `gesamtstrafenbildung-53-54-stgb-erste-instanz` — §§ 53, 54 StGB.
- `nachtraegliche-gesamtstrafenbildung-55-stgb` — § 55 StGB, Zaesurwirkung, § 460 StPO.
- `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` — BGH-staendige Linie.

### Block H — Sonderfaelle
- `jgg-strafzumessung-jugendstrafe-erziehungsmassregeln` — JGG; § 105 JGG Heranwachsende.

## Querverweise zu anderen Plugins

- `strafbefehl-verteidiger` — Spezial-Plugin Strafbefehlsverfahren.
- `fachanwalt-strafrecht` — Strafrechts-Gesamtverteidigung, Plaedoyer, Revision.
- `verkehrsowi-verteidiger` — Verkehrs-OWi-Strafzumessung.
- `urteilsbauer-relationsmacher` — Urteilsverfassung.
- `subsumtions-pruefer` — vor Schuldspruch.

## Hinweise zur Anwendung

- **Quellenregel beachten**: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Aktenzeichen vor Zitat in **dejure.org** oder **openjur.de** verifizieren. Lizenzierte Datenbanken nur bei vorhandenem Zugang.
- **Keine Praejudizienbindung** (Ausnahme § 31 BVerfGG). BGH-Linien sind argumentationsstuetzend, nicht bindend.
- **Mandantengeheimnis** wahren (§ 43a Abs. 2 BRAO; § 203 StGB).
- **Frueher BGH-Beschluss** zum TOA: BGH, Beschluss vom 20.11.2025 — 4 StR 232/25 (friedensstiftender kommunikativer Prozess).
- **BVerfG zur Verstaendigung**: 2 BvR 2628/10 vom 19.03.2013.
- **BGH-Belehrungspflicht**: 1 StR 525/11 vom 07.02.2012.

## Stand

- 05/2026.
- §§ 38 ff. StGB, §§ 407 ff. StPO, JGG, BtMG.
- Aktualitaetspruefung jaehrlich empfohlen.

## Lizenz

Apache-2.0 OR MIT (siehe Plugin-Root).


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-workflow-chronologie-bis-regelbeispiele-recht` | strafzumessung: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel, regelbeispiele-rechtsprechung) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-02-spezial-strafrecht-f-bis-taeter-opfer-ausglei` | strafzumessung: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (spezial-strafrecht-fristen-form-und-zustaendigkeit, spezial-verfahrensstadium-strafbefehl-bis-kammer, taeter-opfer-ausgleich-46a-stgb-und-schadenswieder... |
| `kompendium-03-153a-stpo-einstellun-bis-bewaehrung-56-stgb-p` | strafzumessung: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (153a-stpo-einstellung-gegen-auflage, 267-iii-stpo-begruendungsanforderungen-strafurteil, bewaehrung-56-stgb-positive-sozialprognose) und bewahrt deren W... |
| `kompendium-04-bewaehrung-auflagen-bis-freiheitsstrafe-ohne` | strafzumessung: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (bewaehrung-auflagen-und-weisungen-56b-c-stgb, bewaehrungswiderruf-56f-stgb, freiheitsstrafe-ohne-bewaehrung-vollstreckung) und bewahrt deren Workflows,... |
| `kompendium-05-freiheitsstrafe-stra-bis-geldstrafe-vs-freihe` | strafzumessung: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (freiheitsstrafe-strafmass-pruefen, geldstrafe-tagessatzanzahl-bestimmen, geldstrafe-vs-freiheitsstrafe-47-stgb) und bewahrt deren Workflows, Normanker,... |
| `kompendium-06-gesamtstrafenbildung-bis-haerteausgleich-bei` | strafzumessung: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (gesamtstrafenbildung-53-54-stgb-erste-instanz, gestaendnis-und-strafmilderung, haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung) und bewahrt der... |
| `kompendium-07-jgg-strafzumessung-j-bis-nachtraegliche-gesam` | strafzumessung: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (jgg-strafzumessung-jugendstrafe-erziehungsmassregeln, minder-schwerer-fall-und-besonders-schwerer-fall, nachtraegliche-gesamtstrafenbildung-55-stgb) und... |
| `kompendium-08-orientierung-strafzu-bis-spezial-besonders-fo` | strafzumessung: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (orientierung-strafzumessung-triage, paragraph-46-stgb-grundsatz-strafzumessung, spezial-besonders-formular-portal-und-einreichung) und bewahrt deren Wor... |
| `kompendium-09-spezial-bewaehrung-m-bis-spezial-freiheitsstr` | strafzumessung: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (spezial-bewaehrung-mehrparteien-konflikt-und-interessen, spezial-deutschem-tatbestand-beweis-und-belege, spezial-freiheitsstrafe-compliance-dokumentatio... |
| `kompendium-10-spezial-geldstrafe-z-bis-spezial-rechtsmittel` | strafzumessung: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-geldstrafe-zahlen-schwellen-und-berechnung, spezial-grossen-risikoampel-und-gegenargumente, spezial-rechtsmittel-und-gesamtstrafenfolgen) und be... |
| `kompendium-11-spezial-regelbeispie-bis-spezial-strafbefehl` | strafzumessung: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-regelbeispiele-internationaler-bezug-und-schnittstellen, spezial-stgb-schriftsatz-brief-und-memo-bausteine, spezial-strafbefehl-dokumentenmatrix... |
| `kompendium-12-spezial-strafkammer-bis-spezial-strafzumessu` | strafzumessung: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-strafkammer-behoerden-gericht-und-registerweg, spezial-strafzumessung-erstpruefung-und-mandatsziel, spezial-strafzumessungstatsachen-vergleich-e... |
| `kompendium-13-strafbefehl-strafzum-bis-strafrahmen-und-stra` | strafzumessung: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (strafbefehl-strafzumessung-407-stpo, strafmilderung-49-stgb-zwingend-fakultativ, strafrahmen-und-strafzumessungsstufen) und bewahrt deren Workflows, Nor... |
| `kompendium-14-strafz-aufklaerungsh-bis-strafz-strafrahmenmi` | strafzumessung: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (strafz-aufklaerungshilfe-kronzeuge-spezial, strafz-sicherungsverwahrung-spezial, strafz-strafrahmenmilderung-leitfaden) und bewahrt deren Workflows, Nor... |
| `kompendium-15-strafz-strafzumessun-bis-tagessatzhoehe-40-ii` | strafzumessung: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (strafz-strafzumessungstatsachen-bauleiter, strafzumessungs-tatsachen-46-ii-stgb, tagessatzhoehe-40-ii-stgb-nettotagesverdienst) und bewahrt deren Workfl... |
| `kompendium-16-verstaendigung-257c-bis-verstaendigung-257c` | strafzumessung: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (verstaendigung-257c-stpo-strafzumessung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-schwerer-red-team-und-qualitaetskontrolle` | Schwerer: Red-Team und Qualitätskontrolle im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-tagessatz-livequellen-und-rechtsprechungscheck` | Tagessatz: Livequellen- und Rechtsprechungscheck im Plugin strafzumessung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin strafzumessung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin strafzumessung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin strafzumessung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin strafzumessung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin strafzumessung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin strafzumessung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
