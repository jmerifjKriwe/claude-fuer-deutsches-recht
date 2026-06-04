# Nachbarschaftsstreit-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`nachbarschaftsstreit-pruefer`) | [`nachbarschaftsstreit-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/nachbarschaftsstreit-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Nachbarschaftsstreit Rosengartenstraße** (`nachbarschaftsstreit-horrorfall-rosengarten`) | [Gesamt-PDF lesen](../testakten/nachbarschaftsstreit-horrorfall-rosengarten/gesamt-pdf/nachbarschaftsstreit-horrorfall-rosengarten_gesamt.pdf) | [`testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-nachbarschaftsstreit-horrorfall-rosengarten.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für Nachbarrecht und eskalierte Grundstückskonflikte: Überbau, Überhang, Äste und Wurzeln, Grenzbäume, Einfriedung, Zaun, Mauer, Hecke, Immissionen, Vertiefung, drohender Einsturz, Notweg, Hammerschlags- und Leiterrecht, Beweissicherung, Aufforderungsschreiben, einstweilige Verfügung, Klage und Vergleich.

**Keine Rechtsberatung.** Das Plugin erzeugt strukturierte Prüfungen, Entwürfe und Workflows zur anwaltlichen Kontrolle. Landesnachbarrecht, Baumschutzsatzungen, Bebauungspläne und örtliche Satzungen müssen im konkreten Fall geprüft werden.

## Start

```
/nachbarschaftsstreit-pruefer:allgemein
```

Der Einstieg fragt in kurzer Zeit ab: Grundstücke, Grenze, Bundesland, Streitgegenstand, Gefahr, Beweislage, bisherige Schreiben, gewünschter Ton und Ziel. Danach routet er zu den Spezialskills.

## Skills (20)

| Skill | Zweck |
|---|---|
| `allgemein` | Schöner Einstieg, Fristen-/Gefahrenscan, Routing und Arbeitsplan |
| `nachbarrecht-kaltstart-triage` | Erstaufnahme des Konflikts mit Bundesland, Grundstück, Beteiligten und Risiko |
| `akten-und-grundstuecksaufnahme` | Grundbuch, Liegenschaftskarte, Baulast, Dienstbarkeit, Fotos und Chronologie erfassen |
| `anspruchslandkarte-bgb-nachbarrecht` | Anspruchsgrundlagen nach BGB und Landesrecht sortieren |
| `ueberbau-pruefung` | Überbau nach §§ 912-916 BGB, Widerspruch, Duldung, Rente, Abkauf |
| `ueberhang-aeste-wurzeln` | Überhängende Äste, Wurzeln, Fristsetzung, Selbsthilfe nach § 910 BGB |
| `grenzbaum-und-grenzanlage` | Grenzbaum, Grenzsträucher und gemeinschaftliche Grenzanlagen §§ 921-923 BGB |
| `einfriedung-zaun-mauer-hecke` | Zaun, Mauer, Hecke, Kosten, Standort, Ortsüblichkeit und Landesrecht |
| `immissionen-laerm-geruch-rauch-licht` | Geräusche, Gerüche, Rauch, Licht, Erschütterungen, § 906 BGB |
| `vertiefung-baugrube-stuetzverlust` | Baugrube, Unterfangung, Stütze des Nachbargrundstücks, § 909 BGB |
| `drohender-einsturz-gefahranlage` | Gefährliche Anlagen und Einsturzrisiken, §§ 907, 908 BGB |
| `notweg-zufahrt-wegerecht` | Notweg, Zufahrt, Grunddienstbarkeit, Baulast, §§ 917, 918 BGB |
| `hammerschlags-und-leiterrecht` | Betreten des Nachbargrundstücks für Bau-/Instandhaltungsarbeiten nach Landesrecht |
| `landesnachbarrecht-router` | Bundesland auswählen und landesrechtliche Prüfmodule planen |
| `beweissicherung-ortstermin-fotos` | Ortstermin, Fotoplan, Messpunkte, Sachverständige und selbständiges Beweisverfahren |
| `selbsthilfe-und-eskalationsgrenzen` | Was darf man selbst tun, was nicht, und wann drohen Besitz-/Eigentumsverletzungen? |
| `aufforderungsschreiben-nachbar` | Sachliches, druckvolles Anspruchs- und Fristsetzungsschreiben |
| `einstweilige-verfuegung-und-klage` | Eilrechtsschutz, Unterlassung, Beseitigung, Duldung, Feststellung, Streitwert |
| `vergleich-mediation-nachbarschaftsfrieden` | Vergleich, Nutzungsregelung, Rückschnittplan, Kosten- und Zugangslösung |
| `horrorfall-aktenauswertung` | Große unordentliche Nachbarschaftsakte auswerten und in Arbeitsstränge zerlegen |

## Quellenstand

Stand: 05/2026. Kernnormen: BGB §§ 903, 906-923, 823, 862, 1004; Landesnachbarrechtsgesetze und kommunale Satzungen nach Bundesland/Gemeinde.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-chronologie` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-anschluss-skills-router, workflow-chronologie-und-belegmatrix) und bewahrt deren Workflows, Normanker, Prüfprogramme u... |
| `kompendium-02-workflow-fristen-und-bis-workflow-redteam-qua` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-fristen-und-risikoampel, workflow-mandantenkommunikation, workflow-redteam-qualitygate) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-03-spezial-pruefer-fris-bis-akten-und-grundstuec` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-pruefer-fristennotiz-und-naechster-schritt, spezial-ueberbau-fristen-form-und-zustaendigkeit, akten-und-grundstuecksaufnahme) und... |
| `kompendium-04-anspruchslandkarte-b-bis-beweissicherung-orts` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (anspruchslandkarte-bgb-nachbarrecht, aufforderungsschreiben-nachbar, beweissicherung-ortstermin-fotos) und bewahrt deren Workflows, Norman... |
| `kompendium-05-drohender-einsturz-g-bis-einstweilige-verfueg` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (drohender-einsturz-gefahranlage, einfriedung-zaun-mauer-hecke, einstweilige-verfuegung-und-klage) und bewahrt deren Workflows, Normanker,... |
| `kompendium-06-grenzbaum-und-grenza-bis-horrorfall-aktenausw` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (grenzbaum-und-grenzanlage, hammerschlags-und-leiterrecht, horrorfall-aktenauswertung) und bewahrt deren Workflows, Normanker, Prüfprogramm... |
| `kompendium-07-immissionen-laerm-ge-bis-nach-grenzbebauung-u` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (immissionen-laerm-geruch-rauch-licht, landesnachbarrecht-router, nach-grenzbebauung-ueberhang-spezial) und bewahrt deren Workflows, Norman... |
| `kompendium-08-nach-laermimmissione-bis-nach-nachbarrechtsue` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (nach-laermimmissionen-spezial, nach-mediation-vorrang-leitfaden, nach-nachbarrechtsuebersicht-bauleiter) und bewahrt deren Workflows, Norm... |
| `kompendium-09-notweg-zufahrt-weger-bis-spezial-aeste-risiko` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (notweg-zufahrt-wegerecht, selbsthilfe-und-eskalationsgrenzen, spezial-aeste-risikoampel-und-gegenargumente) und bewahrt deren Workflows, N... |
| `kompendium-10-spezial-aufforderung-bis-spezial-grenzbaum-sc` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-aufforderung-mandantenkommunikation-entscheidungsvorlage, spezial-beweise-red-team-und-qualitaetskontrolle, spezial-grenzbaum-schr... |
| `kompendium-11-spezial-hammerschlag-bis-spezial-immissionen` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-hammerschlagsrecht-formular-portal-und-einreichung, spezial-hecke-zahlen-schwellen-und-berechnung, spezial-immissionen-compliance-... |
| `kompendium-12-spezial-klage-beweis-bis-spezial-nachbarschaf` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-klage-beweislast-und-darlegungslast, spezial-nachbarrecht-erstpruefung-und-mandatsziel, spezial-nachbarschaftsstreit-tatbestand-be... |
| `kompendium-13-spezial-notweg-inter-bis-spezial-vergleich-so` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-notweg-internationaler-bezug-und-schnittstellen, spezial-ueberhang-dokumentenmatrix-und-lueckenliste, spezial-vergleich-sonderfall... |
| `kompendium-14-spezial-vertiefung-m-bis-spezial-zaun-verhand` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-vertiefung-mehrparteien-konflikt-und-interessen, spezial-wurzeln-behoerden-gericht-und-registerweg, spezial-zaun-verhandlung-vergl... |
| `kompendium-15-ueberbau-pruefung-bis-vergleich-mediation` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (ueberbau-pruefung, ueberhang-aeste-wurzeln, vergleich-mediation-nachbarschaftsfrieden) und bewahrt deren Workflows, Normanker, Prüfprogram... |
| `kompendium-16-vertiefung-baugrube-bis-vertiefung-baugrube` | nachbarschaftsstreit-pruefer: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (vertiefung-baugrube-stuetzverlust) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `nachbarrecht-kaltstart-triage` | Erstaufnahme eines Nachbarrechtsfalls: Beteiligte, Grundstücke, Bundesland, Grenze, Streitgegenstand, Gefahr, Fristen, Beweise, bisherige Eskalation und Ziel klären; danach in die passenden Spezialskills routen. |
| `spezial-kaltstart-abschlussprodukt-und-uebergabe` | Kaltstart: Abschlussprodukt und Übergabe im Plugin nachbarschaftsstreit pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-mauer-livequellen-und-rechtsprechungscheck` | Mauer: Livequellen- und Rechtsprechungscheck im Plugin nachbarschaftsstreit pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin nachbarschaftsstreit-pruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin nachbarschaftsstreit-pruefer: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin nachbarschaftsstreit-pruefer: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin nachbarschaftsstreit-pruefer: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin nachbarschaftsstreit-pruefer: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
