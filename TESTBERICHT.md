# Testbericht — Klotzkette German Legal Skills

**Erstellt:** 2026-06-05
**Arbeitsstand:** v213.0.0 / Freistehende Skilltexte nach Konsolidierungs- und Boilerplate-Politur
**Plugins gesamt:** 210
**Skills gesamt:** 9115
**Testakten gesamt:** 201

## Kurzbefund

Das Repository ist nach der Politur der verdichteten Skilltexte release- und uploadfähig. Der neue Stand bewahrt die verdichteten Inhalte, entfernt aber die sichtbare Entstehungsgeschichte aus den Skills: keine Formeln wie "Dieser Skill bündelt", keine `Arbeitsmodule`-Überschriften, keine `Kompendium`-/`Sammelskill`-Artefakte, keine generischen "gehört zum Plugin"-Absätze und keine `Nutze diesen Skill`-/`Dieses Fachmodul greift ...`-Starter in den geprüften Skillanfängen.

Die parallel eingegangenen Verbesserungen aus dem vorherigen Release bleiben erhalten. Der neue Schwerpunkt liegt darauf, dass zusammengeführte Skills für Nutzerinnen und Nutzer wieder wie eigenständige, auswählbare Fachskills wirken.

## Kennzahlen

| Kennzahl | Wert |
|---|---:|
| Plugin-Manifests | 210 |
| Skill-Dateien `SKILL.md` | 9115 |
| Testakten-Verzeichnisse | 201 |
| Testakten mit Gesamt-PDF nach Validator | 201 |
| Skillnamen-/Artefakt-Scan | 0 alte Autogen-Muster, 0 `Nutze dies`, 0 Einwort-/Zahlenslugs, 0 `Kompendium`-/`Sammelskill`-Namen, 0 `bündelt`-/`Arbeitsmodul`-Artefakte, 0 `Nutze diesen Skill`-/`Dieses Fachmodul greift ...`-Starter in Skillanfängen |
| Bewusste Ausnahmen | Einige große Fach- und Werkstattplugins bleiben umfangreicher, wo Einzelzugriff praktisch wichtiger ist als weitere Verdichtung. |

## Validatoren

| Check | Ergebnis |
|---|---|
| `python3 scripts/validate-yaml-frontmatter.py` | OK — 0 Fehler, 0 Warnungen |
| `node scripts/validate-plugin-structure.mjs` | OK |
| `python3 scripts/validate-testakten-gesamt-pdf.py` | OK — 201 Testakten |
| `python3 scripts/validate-release-zips.py dist .claude-plugin/marketplace.json` | OK — lokale ZIP-Simulation für alle Marketplace-Plugins |
| `git diff --check` | OK |

## Konsolidierungslogik

Die Pflege folgt konservativen Regeln:

- Einstieg, Kaltstart, Routing, Dokumentenintake, Rechtsquellencheck, Outputwahl und Quality-Gates bleiben soweit möglich als sichtbare Einstiegspunkte erhalten.
- Skills mit Zusatzdateien, Assets, References oder Toolmaterial bleiben eigenständig.
- Steuerrechtliche DBA-Skills bleiben als Einzelskills erhalten, weil hier die Einzelabkommen selbst der Arbeitsgegenstand sind.
- Sprechende Skillnamen haben Vorrang vor technischen oder generischen Kürzeln.
- Zusammengeführte Skills müssen freistehend bleiben und dürfen keine Artefakte wie "frühere Beschreibung", "Dieser Skill bündelt" oder unspezifische Sammelüberschriften behalten.

Damit sinkt die Bedienlast für Nutzerinnen und Nutzer, ohne dass fachliches Material aus den alten Skills aus dem Repository verschwindet.

## Nachgezogene Meta-Pflege

- Root-README auf den aktuellen Stand gebracht: 210 Plugins, 9115 Skills, 201 Testakten.
- Testakten-README auf v213.0.0 und 201 Testakten geprüft.
- `SKILLS.md` und `skills-index/` wurden mit den Generatoren neu aufgebaut.
- Veraltete Angaben aus der alten 52-Plugin-/361-Skill-Phase wurden aus diesem Testbericht entfernt.
- Nach v211 wurden 2906 `SKILL.md`-Dateien zusätzlich sprachlich nachpoliert, damit verdichtete Skills nicht mehr wie Generator- oder Konsolidierungsartefakte starten.

## Offene bewusste Ausnahme

Einzelne große Fach- und Werkstattplugins bleiben oberhalb einer niedrigen Zielmarke, wenn die sichtbare Auswahl einzelner Fallgruppen praktisch wichtiger ist als weitere Verdichtung. Das gilt insbesondere für stark differenzierte Steuer-, Arbeitszeugnis-, Liquiditäts-, Selbstvertreter- und Fachanwaltsworkflows.

## Residualrisiko

Die Validierung prüft Struktur, Frontmatter, Gesamt-PDF-Verfügbarkeit und grundlegende Markdown-/Git-Sauberkeit. Sie ersetzt keine vollständige fachliche Rechtsprüfung jedes einzelnen Skill-Abschnitts. Für Rechtsprechung, Normstand und Literaturhinweise bleibt die Regel des Repos maßgeblich: nur mit überprüfbarer Quelle, Datum, Aktenzeichen und frei zugänglicher Fundstelle ausgeben, soweit nicht eine Nutzerquelle ausdrücklich bereitgestellt wird.
