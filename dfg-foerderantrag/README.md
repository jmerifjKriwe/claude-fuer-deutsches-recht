# DFG-Förderantrag

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`dfg-foerderantrag`) | [`dfg-foerderantrag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/dfg-foerderantrag.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für die praktische Antragstellung bei der Deutschen Forschungsgemeinschaft: Sachbeihilfe, elan-Formalia, Projektbeschreibung, Finanzplan, Forschungsdaten, Ethik-/KI-Check, Reviewer-Perspektive, Wiedereinreichung und strategische Entscheidung zwischen kleinem schnellen Antrag und großem Prestigeprojekt.

Der Stil ist bewusst nicht bürokratisch. Das Plugin fragt zuerst: Was ist wissenschaftlich stark, was ist realistisch förderbar, was kann schneller entschieden werden und wo ist der große Antrag zwar verführerisch, aber prozessual zäher? Es arbeitet adaptiv: Anfänger bekommen eine geführte Mini-Roadmap; erfahrene Antragsteller bekommen direkt Red-Team, Kürzungsrisiko und Programmstrategie.

## Quellen-Gate

Vor jeder belastbaren Ausgabe aktuelle DFG-Seiten prüfen:

- DFG Sachbeihilfe: themenoffene Einzelförderung, Neuanträge jederzeit, Fortsetzungsanträge spätestens 6 Monate vor Mittelverbrauch.
- DFG Begutachtung: grundsätzlich zwei Gutachten; bei Anträgen bis 200.000 Euro kann ausnahmsweise ein aussagekräftiges externes Gutachten reichen.
- Reinhart-Koselleck-Projekte: 500.000 bis 1,25 Mio. Euro für fünf Jahre in Stufen von 250.000 Euro; nur für herausragende, besonders innovative oder risikobehaftete Projekte, die nicht in normale Verfahren passen.
- DFG-Merkblätter, elan-Vorlagen, fachzuständige Ansprechpersonen und aktuelle Vordruckstände immer live gegen `dfg.de` prüfen.

## Schnellstart

```text
/dfg-foerderantrag:allgemein
```

Der Allgemein-Skill führt in 60 Sekunden durch: Forschungsfrage, Förderprogramm, Summe, Tempo, Zielgruppe der Begutachtung, Vorarbeiten, Risiken, Daten-/Ethikthemen und gewünschtes Ergebnis.

Typische Startpunkte:

| Situation | Start |
| --- | --- |
| "Ich habe nur eine Forschungsidee" | `allgemein` → Mini-Roadmap und Minimalprojekt |
| "Sachbeihilfe oder größer?" | `dfg-foerderstrategie-schnell-oder-gross` |
| "Entwurf liegt vor" | `dfg-reviewer-red-team` → danach Text- und Finanzskills |
| "Ablehnung liegt vor" | `dfg-wiedereinreichung-nach-ablehnung` |

## Skill-Matrix

| Skill | Wofür? |
| --- | --- |
| `allgemein` | Einstieg, Triage, Programmroute und erster Arbeitsplan |
| `dfg-foerderstrategie-schnell-oder-gross` | Entscheidung: kleiner schneller Antrag, normale Sachbeihilfe, Koselleck oder anderes Programm |
| `dfg-sachbeihilfe-elan-formalia` | Sachbeihilfe, elan, Anlagen, Vordrucklogik, formales Gate |
| `dfg-bis-200k-begutachtung-light` | Kleine/mittlere Anträge so bauen, dass sie schnell, klar und begutachtbar sind |
| `dfg-koselleck-500k-125m` | Koselleck-Check: 500.000 bis 1,25 Mio. Euro, Risiko, Profil, Vertrauensvorschuss |
| `dfg-projektbeschreibung-arbeitsprogramm` | Forschungsfrage, Stand der Forschung, Ziele, Arbeitspakete, Meilensteine |
| `dfg-finanzplan-module-personal-geraete` | Personal, Geräte, Reisen, Workshops, Mercator Fellow, Chancengleichheit, Budgetbegründung |
| `dfg-reviewer-red-team` | Gutachterperspektive, Angriffsflächen, Kürzungsrisiken, Ablehnungsgründe |
| `dfg-wiedereinreichung-nach-ablehnung` | Ablehnung auswerten, Gutachten ernst nehmen, Neuaufstellung |
| `dfg-ki-ethik-forschungsdaten` | KI-Nutzung, Vertraulichkeit, Forschungsdatenmanagement, Ethik und Datenschutz |

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `dfg-reviewer-red-team` | DFG-Antrag aus Gutachterperspektive red-teamen: Originalität, Machbarkeit, Arbeitsprogramm, Qualifikation, Umfeld, Bias-Risiken, Kürzungsargumente, Ablehnungsrisiken und Verbesserungsplan. |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabem... |
| `kompendium-02-workflow-mandantenko-bis-spezial-forschungsda` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-forschungsdaten-fristennotiz-und-naechster-schritt) und bewahrt deren Workflow... |
| `kompendium-03-spezial-sachbeihilfe-bis-dfg-eigenanteil-und` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-sachbeihilfe-fristen-form-und-zustaendigkeit, dfg-bis-200k-begutachtung-light, dfg-eigenanteil-und-grundausstattung) und bewahrt deren Workfl... |
| `kompendium-04-dfg-eigene-vorarbeit-bis-dfg-finanzplan-modul` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (dfg-eigene-vorarbeiten-darstellen, dfg-erstantragsteller-besondere-checks, dfg-finanzplan-module-personal-geraete) und bewahrt deren Workflows, Norma... |
| `kompendium-05-dfg-foerderstrategie-bis-dfg-grundsystem-foer` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (dfg-foerderstrategie-schnell-oder-gross, dfg-grossgeraete-und-cluster-antrag, dfg-grundsystem-foerderlinien) und bewahrt deren Workflows, Normanker,... |
| `kompendium-06-dfg-internationale-k-bis-dfg-kollegen-review` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (dfg-internationale-kooperation-aufbau, dfg-ki-ethik-forschungsdaten, dfg-kollegen-review-organisieren) und bewahrt deren Workflows, Normanker, Prüfpr... |
| `kompendium-07-dfg-koselleck-500k-1-bis-dfg-projektbeschreib` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (dfg-koselleck-500k-125m, dfg-praeregistrierung-replication-studies, dfg-projektbeschreibung-arbeitsprogramm) und bewahrt deren Workflows, Normanker,... |
| `kompendium-08-dfg-publikationsstra-bis-dfg-sachbeihilfe-ela` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (dfg-publikationsstrategie-projekt, dfg-replikationskrise-statistik-spezial, dfg-sachbeihilfe-elan-formalia) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-09-dfg-software-veroeff-bis-dfg-wiedereinreichun` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (dfg-software-veroeffentlichung-spezial, dfg-tieforschung-ethik-pflichten, dfg-wiedereinreichung-nach-ablehnung) und bewahrt deren Workflows, Normanke... |
| `kompendium-10-dfg-zeitplan-und-mei-bis-spezial-adaptive-dok` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (dfg-zeitplan-und-meilensteine, dfg-zwischen-und-abschlussbericht, spezial-adaptive-dokumentenmatrix-und-lueckenliste) und bewahrt deren Workflows, No... |
| `kompendium-11-spezial-anfaenger-ri-bis-spezial-dfg-erstprue` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-anfaenger-risikoampel-und-gegenargumente, spezial-antraege-zahlen-schwellen-und-berechnung, spezial-dfg-erstpruefung-und-mandatsziel) und bew... |
| `kompendium-12-spezial-elan-formula-bis-spezial-finanzplan-m` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-elan-formular-portal-und-einreichung, spezial-ethik-abschlussprodukt-und-uebergabe, spezial-finanzplan-mandantenkommunikation-entscheidungsvo... |
| `kompendium-13-spezial-foerderantra-bis-spezial-fuehrung-sch` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-foerderantragssteller-tatbestand-beweis-und-belege, spezial-formalia-red-team-und-qualitaetskontrolle, spezial-fuehrung-schriftsatz-brief-und... |
| `kompendium-14-spezial-grosse-compl-bis-spezial-koselleck-me` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-grosse-compliance-dokumentation-und-akte, spezial-kleine-verhandlung-vergleich-und-eskalation, spezial-koselleck-mehrparteien-konflikt-und-in... |
| `kompendium-15-spezial-profi-behoer-bis-spezial-strategien-i` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-profi-behoerden-gericht-und-registerweg, spezial-reviewer-beweislast-und-darlegungslast, spezial-strategien-internationaler-bezug-und-schnitt... |
| `kompendium-16-spezial-team-sonderf-bis-spezial-team-sonderf` | dfg-foerderantrag: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (spezial-team-sonderfall-und-edge-case) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-schnelle-livequellen-und-rechtsprechungscheck` | Schnelle: Livequellen- und Rechtsprechungscheck im Plugin dfg foerderantrag; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin dfg-foerderantrag: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin dfg-foerderantrag: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin dfg-foerderantrag: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin dfg-foerderantrag: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin dfg-foerderantrag: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin dfg-foerderantrag: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
