# Testbericht — Klotzkette German Legal Skills

**Erstellt:** 2026-06-04
**Arbeitsstand:** v209.0.0 / Konsolidierung nach Commit `1a3f44901`
**Plugins gesamt:** 209
**Skills gesamt:** 5629
**Testakten gesamt:** 201

## Kurzbefund

Das Repository ist nach dem großen Skill-Sweep release- und uploadfähig. Die vorher sehr hohe Skill-Zahl wurde nicht durch bloßes Löschen reduziert, sondern durch thematische Kompendien je Plugin verdichtet. Frühere Einzelskills bleiben in den Kompendien mit ihrer Beschreibung, ihrem Body, ihrer Prüfungslogik, ihren Workflows und ihren Outputmustern sichtbar.

Die parallel von Claude/Perplexity eingegangenen Verbesserungen wurden vor dem Push auf `main` eingearbeitet. Insbesondere die 79 substantiellen Skill-Ersetzungen aus `origin/main` wurden beim Rebase nicht verworfen, sondern in die passenden Kompendien übernommen.

## Kennzahlen

| Kennzahl | Wert |
|---|---:|
| Plugin-Manifests | 209 |
| Skill-Dateien `SKILL.md` | 5629 |
| Testakten-Verzeichnisse | 201 |
| Testakten mit Gesamt-PDF nach Validator | 201 |
| Plugins mit mehr als 30 Skills | 2 |
| Bewusste Ausnahmen | `steuerrecht-anwalt-und-berater` mit 89 Skills wegen erhaltener DBA-Einzelskills; `arbeitszeugnis-analyse` mit 50 Skills auf Wunsch im Vor-Konsolidierungszuschnitt |

## Validatoren

| Check | Ergebnis |
|---|---|
| `python3 scripts/validate-yaml-frontmatter.py` | OK — 0 Fehler, 0 Warnungen |
| `node scripts/validate-plugin-structure.mjs` | OK |
| `python3 scripts/validate-testakten-gesamt-pdf.py` | OK — 201 Testakten |
| `python3 scripts/validate-release-zips.py dist .claude-plugin/marketplace.json` | OK — 209 lokal gebaute Plugin-ZIPs |
| `git diff --check` | OK |

## Konsolidierungslogik

Die Verdichtung folgt konservativen Regeln:

- Einstieg, Kaltstart, Routing, Dokumentenintake, Rechtsquellencheck, Outputwahl und Quality-Gates bleiben soweit möglich als sichtbare Einstiegspunkte erhalten.
- Skills mit Zusatzdateien, Assets, References oder Toolmaterial bleiben eigenständig.
- Steuerrechtliche DBA-Skills bleiben als Einzelskills erhalten, weil hier die Einzelabkommen selbst der Arbeitsgegenstand sind.
- Alle übrigen Skills werden innerhalb des jeweiligen Plugins in `kompendium-*`-Skills zusammengeführt.
- In jedem Kompendium gibt es eine Tabelle der früheren Skills und danach die konsolidierten Inhalte als eigene Abschnitte.

Damit sinkt die Bedienlast für Nutzerinnen und Nutzer deutlich, ohne dass das fachliche Material aus den alten Skills aus dem Repository verschwindet.

## Nachgezogene Meta-Pflege

- Root-README auf den aktuellen Stand gebracht: 209 Plugins, 5629 Skills, 201 Testakten.
- Testakten-README auf v209.0.0 und 201 Testakten aktualisiert.
- `SKILLS.md` und `skills-index/` wurden mit den Generatoren neu aufgebaut.
- Veraltete Angaben aus der alten 52-Plugin-/361-Skill-Phase wurden aus diesem Testbericht entfernt.

## Offene bewusste Ausnahme

`steuerrecht-anwalt-und-berater` bleibt mit 89 Skills oberhalb der Zielmarke. Das ist absichtlich: Die Doppelbesteuerungsabkommen und steuerlichen Spezialpfade sollen nicht in einem Sammeltext verschwinden, weil die Nutzerin dort regelmäßig genau ein bestimmtes Abkommen oder eine bestimmte DBA-Konstellation ansteuern will.

`arbeitszeugnis-analyse` bleibt mit 50 Skills ebenfalls oberhalb der Zielmarke. Das Plugin wurde nachträglich wieder auf den Vor-Konsolidierungszuschnitt zurückgestellt, weil seine Ampel-, Codewort-, Zeugnisarten-, Muster- und Prozessskills als einzelne Arbeitspunkte sichtbar bleiben sollen.

## Residualrisiko

Die Validierung prüft Struktur, Frontmatter, Gesamt-PDF-Verfügbarkeit und grundlegende Markdown-/Git-Sauberkeit. Sie ersetzt keine vollständige fachliche Rechtsprüfung jedes einzelnen Skill-Abschnitts. Für Rechtsprechung, Normstand und Literaturhinweise bleibt die Regel des Repos maßgeblich: nur mit überprüfbarer Quelle, Datum, Aktenzeichen und frei zugänglicher Fundstelle ausgeben, soweit nicht eine Nutzerquelle ausdrücklich bereitgestellt wird.
