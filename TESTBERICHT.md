# Testbericht — Klotzkette German Legal Skills

**Erstellt:** 2026-06-10
**Arbeitsstand:** v292.0.0 / Rechtsvergleich auf zwölf europäische Rechtsordnungen ausgebaut (Frankreich, Italien, Spanien, Niederlande, Belgien, Österreich, Luxemburg, Dänemark, Polen, Tschechien, Griechenland, Irland) im `verhaeltnismaessigkeitspruefer`. 212 Plugins, 20.859 Skills, 203 Testakten.
**Plugins gesamt:** 212
**Skills gesamt:** 20859
**Testakten gesamt:** 203

## Kurzbefund

Das Repository ist nach dem v292-Release stabil und uploadfähig. Der `verhaeltnismaessigkeitspruefer` ist von 49 auf 61 Skills angewachsen; die Gruppe „Rechtsvergleich" deckt damit 17 Rechtsordnungen ab (Deutschland mit Vier-Stufen-Schranken-Schranke, Südafrika Section 36, Kanada Oakes-Test, EGMR/EMRK, EuGH/Charta, USA Tiers of Scrutiny sowie 12 europäische Nachbarordnungen).

Alle Übersichten, Sofort-Download-Sektionen und Release-Assets sind synchron: Plugin-Manifests, Marketplace, Top-Level-README, Asset-Index, SKILLS.md und der pro-Plugin-Detailindex stehen auf demselben Stand.

## Kennzahlen

| Kennzahl | Wert |
|---|---:|
| Plugin-Manifests | 212 |
| Skill-Dateien `SKILL.md` | 20859 |
| Testakten-Verzeichnisse | 203 |
| Testakten mit Gesamt-PDF nach Validator | 203 |
| Release-Assets v292.0.0 | 419 (Plugin-ZIPs + Testakten-ZIPs + Sammel-Assets) |
| Rechtsvergleichs-Skills im `verhaeltnismaessigkeitspruefer` | 20 (für 17 Rechtsordnungen) |

## Validatoren

| Check | Ergebnis |
|---|---|
| `python3 scripts/validate-yaml-frontmatter.py` | OK — 0 Fehler, 0 Warnungen |
| `node scripts/validate-plugin-structure.mjs` | OK |
| `python3 scripts/validate-testakten-gesamt-pdf.py` | OK — 203 Testakten |
| `python3 scripts/validate-release-zips.py dist .claude-plugin/marketplace.json` | OK — Release-Workflow ZIP-Build durch (alle 212 Plugins) |
| `git diff --check` | OK |

## Veränderungen v291 → v292

- **12 neue Rechtsvergleich-Skills** im `verhaeltnismaessigkeitspruefer` für Frankreich (CE Triple Test, Conciliation, QPC), Italien (Corte costituzionale Ragionevolezza, Bilanciamento), Spanien (Tribunal Constitucional Juicio de proporcionalidad, Contenido esencial), Niederlande (Art 3:4 Awb, Maxis & Praxis 2022), Belgien (Grondwettelijk Hof Art 10 11 GW), Österreich (VfGH Sachlichkeitsgebot, EMRK im Verfassungsrang), Luxemburg (Cour constitutionnelle Triple Test), Dänemark (Politilov, Retsplejelov), Polen (Trybunał Konstytucyjny Art 31 III), Tschechien (Ústavní soud Pl ÚS 4/94), Griechenland (Art 25 I 4 Syntagma) und Irland (Heaney Test).
- Jeder neue Skill enthält Verfassungsrahmen, Prüfungsstufen mit Leading cases, Wesensgehalts-Funktion, Rezeption europäischer Maßstäbe (EMRK, Charta), Strukturunterschiede-Tabelle zur deutschen Vier-Stufen-Prüfung und einen Live-Recherche-Disclaimer.
- Plugin-Versionsbump 291.0.0 → 292.0.0 für alle 212 Plugins.
- SKILLS.md, `skills-index/`, ASSET_INDEX.md, Top-Level-README, CHANGELOG.md vollständig synchronisiert.

## Konsolidierungslogik

Die Pflege folgt konservativen Regeln:

- Einstieg, Kaltstart, Routing, Dokumentenintake, Rechtsquellencheck, Outputwahl und Quality-Gates bleiben sichtbare Einstiegspunkte.
- Skills mit Zusatzdateien, Assets, References oder Toolmaterial bleiben eigenständig.
- Steuerrechtliche DBA-Skills bleiben als Einzelskills erhalten, weil die Einzelabkommen selbst Arbeitsgegenstand sind.
- Sprechende Skillnamen haben Vorrang vor technischen oder generischen Kürzeln.
- Zusammengeführte Skills müssen freistehend bleiben und dürfen keine Artefakte wie „frühere Beschreibung", „Dieser Skill bündelt" oder unspezifische Sammelüberschriften behalten.

## Offene bewusste Ausnahme

Einige große Fach- und Werkstattplugins bleiben oberhalb einer niedrigen Zielmarke, wenn die sichtbare Auswahl einzelner Fallgruppen praktisch wichtiger ist als weitere Verdichtung. Das gilt insbesondere für stark differenzierte Steuer-, Arbeitszeugnis-, Liquiditäts-, Selbstvertreter- und Fachanwaltsworkflows.

## Residualrisiko

Die Validierung prüft Struktur, Frontmatter, Gesamt-PDF-Verfügbarkeit und grundlegende Markdown-/Git-Sauberkeit. Sie ersetzt keine vollständige fachliche Rechtsprüfung jedes einzelnen Skill-Abschnitts. Für Rechtsprechung, Normstand und Literaturhinweise bleibt die Regel des Repos maßgeblich: nur mit überprüfbarer Quelle, Datum, Aktenzeichen und frei zugänglicher Fundstelle ausgeben, soweit keine Nutzerquelle ausdrücklich bereitgestellt wird.

Die Rechtsvergleichs-Skills enthalten in jedem Land einen Live-Recherche-Disclaimer mit Original-Datenbanken (Légifrance, ArianeWeb, conseil-constitutionnel.fr, cortecostituzionale.it, tribunalconstitucional.es, rechtspraak.nl, const-court.be, ris.bka.gv.at, justice.public.lu, retsinformation.dk, trybunal.gov.pl, usoud.cz, ste.gr, BAILII/courts.ie).
