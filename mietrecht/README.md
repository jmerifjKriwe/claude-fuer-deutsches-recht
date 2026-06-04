# Mietrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`mietrecht`) | [`mietrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mietrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Mietstreit Tannenkamp / Strassburger Immobilien GmbH — Altbau Leipzig-Plagwitz, Modernisierung und Mietminderung** (`mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp`) | [Gesamt-PDF lesen](../testakten/mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp/gesamt-pdf/mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp_gesamt.pdf) | [`testakte-mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mietstreit-altbau-rosenbluete-leipzig-modernisierung-und-minderung-tannenkamp.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Mietrecht für Mieter und Vermieter sowie Wohnungseigentumsrecht mit ausschließlich amtlichen Mietspiegel-Quellen pro Bundesland und für Top- und Universitätsstädte. Workflows für Datenerhebung, Mieterhöhungs-Widerspruch, Mietsenkungsverlangen, Nebenkostenprüfung, Mieteranfragen, Kündigung, Kaution, WEG-Beschlussklage und Klageentwurf Amtsgericht.

## Rechtsstand und Quellen-Gate

Für aktuelle Mietrechts- und WEG-Fragen zuerst `/mietrecht:rechtsstand-mai-2026-faktenbank` laden. Der Skill enthält geprüfte freie Anker zu Mietpreisbremse, Modernisierung, Steckersolargeräten, virtueller Eigentümerversammlung, Verwalterabberufung, WEG-baulichen Veränderungen und Störerhaftung.

Keine BeckRS-, juris-, Kommentar- oder Aufsatzzitate aus Modellwissen. Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier Quelle; Mietspiegel nur aus amtlicher kommunaler Quelle oder der mitgelieferten Mietspiegel-Referenz.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Triage und Workflow-Routing im Plugin. Fragt Rolle (Vermieter/Mieter/WEG/Verwalter), Ziel, Fristen, Unterlagen und Risiken ab und schlägt passende Spezial-Skills vor. Bei stummem Upload reagiert der Skill eigenständig: ordnet das Material, prüft Eil- und Fristenhinweise, schlägt den passenden Spezial-Skill vor oder stellt genau eine gezielte Rückfrage. |
| `eigenbedarfskuendigung-erstellen` | Vermietersicht — entwerfe eine ordentliche Kündigung wegen Eigenbedarfs nach § 573 Abs. 2 Nr. 2 BGB. Prüfroutine deckt berechtigtes Interesse (Eigennutzung Familienangehörige Haushaltsangehörige) konkrete Begründ… |
| `klageentwurf-amtsgericht` | Beide Rollen — entwirf eine Klageschrift zum Amtsgericht in einer Mietsache. Sachliche Zuständigkeit für Wohnraummietsachen nach § 23 Nr. 2a GVG ohne Rücksicht auf den Streitwert; bei Geschäftsraummiete allgemeine… |
| `lage-und-ausstattung-erheben` | Strukturierte Datenerhebung für die Einordnung in den Mietspiegel — Adresse Baujahr Wohnfläche Bad Küche Heizung Wohnungsausstattung Gebäudeausstattung. Erfasst alle Merkmale die in qualifizierten Mietspiegeln als… |
| `mahnung-zahlungsverzug-mieter` | Vermietersicht — verfasse Mahnung und ggf. fristlose Kündigung bei Zahlungsverzug des Mieters. Prüfroutine deckt Verzug nach § 286 BGB Fälligkeit der Miete (§ 556b Abs. 1 BGB) Mahnschreiben Aufrechnungsverbot frist… |
| `mandat-triage-mietrecht` | Strukturierte Eingangs-Abfrage für mietrechtliche Mandate. Klärt Mandantenrolle (Vermieter/Mieter/WEG-Eigentümer/Verwalter), Gegenstand (Wohnraum/Gewerbe/WEG) und Sachgebiet (Kündigung, Mieterhöhung, Mietminderung, Modernisierung, Nebenkosten, Mietkaution, Eigenbedarf, Räumung, WEG-Beschluss, WEG-Hausgeld). Fristen-Sofort-Check (§ 573c BGB, § 721 ZPO, § 45 WEG, § 558b BGB). Eskalations-Pfad bei laufenden Fristen. |
| `mieteranfragen-beantworten` | Vermieter- und Hausverwaltungssicht — beantworte Mieteranfragen sachlich und ehrlich. Deckt typische Themen ab (Mietminderung Mangelanzeige Modernisierungsankündigung Schönheitsreparaturen Hausordnung Kaution Eigenb… |
| `mieterhoehung-pruefen-widersprechen` | Mietersicht — prüfe ein Mieterhöhungsverlangen nach ortsüblicher Vergleichsmiete (§§ 558 ff. BGB) auf Form Frist Kappungsgrenze Begründung und entwirf bei Bedarf eine Zustimmungsverweigerung oder Teilzustimmung. P… |
| `mieterhoehungsverlangen-erstellen` | Vermietersicht — verfasse ein Mieterhöhungsverlangen auf ortsübliche Vergleichsmiete (§ 558a BGB) in Textform mit ordnungsgemäßer Begründung (Mietspiegel Sachverständigengutachten oder drei Vergleichswohnungen).… |
| `mietkaution-rueckforderung` | Mietersicht — Workflow zur Rückforderung der Mietkaution nach Beendigung des Mietverhältnisses. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Prüfung mit Gericht, Datum und Aktenzeichen. |
| `mietpreisueberhoehung-wistrg-1954-mietwucher` | Dreistufige Prüfung überhöhter Wohnraummiete: Mietpreisbremse, § 5 WiStrG 1954 als Ordnungswidrigkeit und § 291 StGB als Straftat; mit Mietspiegel-, Beweis-, Rückforderungs- und Behördenpfad. |
| `mietsenkungsverlangen` | Mietersicht — prüfe eine laufende oder bei Vertragsschluss vereinbarte Miete auf Mietpreisbremse (§§ 556d ff. BGB), § 5 WiStrG 1954 (Mietpreisüberhöhung) und § 291 StGB (Mietwucher). Erzeugt ein… |
| `mietspiegel-quellen` | Verweist auf die mitgelieferte Referenz references/mietspiegel-quellen.md mit ausschließlich amtlichen Mietspiegel-Quellen (Bundesländer Top-Städte Universitätsstädte). Nutze diese Referenz immer wenn die ortsüb… |
| `nebenkostenabrechnung-erstellen` | Vermieter- und Hausverwaltungssicht — Workflow für rechtssichere Betriebskostenabrechnungen nach § 556 BGB und BetrKV. Deckt Abrechnungszeitraum Zugangsfrist (zwölf Monate) Umlagefähigkeit Verteilerschlüssel Heizk… |
| `nebenkostenabrechnung-pruefen` | Mietersicht — prüfe eine Betriebskostenabrechnung auf Form (§ 556 Abs. 3 BGB) Frist (Zugang innerhalb von zwölf Monaten nach Abrechnungszeitraum) Umlagefähigkeit nach BetrKV Verteilerschlüssel rechnerische Richtig… |
| `rechtsstand-mai-2026-faktenbank` | Quellen-Gate: Mietpreisbremse, Modernisierung, Steckersolargeräte, virtuelle Eigentümerversammlung, Verwalterabberufung, WEG-bauliche Veränderung und freie BGH-/Normquellen |
| `weg-beschluss-anfechten` | WEG-Sicht — Prüfraster für die Beschlussanfechtung in der Wohnungseigentümergemeinschaft nach §§ 44 ff. WEG (Reform 2020). Beschluss-, Anfechtungs-, Nichtigkeits- und Feststellungsklage. Prüft formelle Mängel (Ladung, Tagesordnung, Beschlussfähigkeit, Mehrheit, Stimmrechtsausschluss) und materielle Mängel (ordnungsmäßige Verwaltung, Treu und Glauben). Klagefrist ein Monat ab Beschluss (§ 45 WEG). |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | mietrecht: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-02-workflow-mandantenko-bis-spezial-vermieter-fr` | mietrecht: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-vermieter-fristen-form-und-zustaendigkeit) und bewahrt deren Workflows, Normanker, Prü... |
| `kompendium-03-klageentwurf-amtsger-bis-miet-mietvertrag-bau` | mietrecht: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (klageentwurf-amtsgericht, miet-gewerbemiete-vertragsklauseln-spezial, miet-mietvertrag-bauleiter) und bewahrt deren Workflows, Normanker, Prüfprogramme und A... |
| `kompendium-04-mr-einfuehrung-vertr-bis-eigenbedarfskuendigu` | mietrecht: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (mr-einfuehrung-vertragstypen, spezial-klageentwurf-beweislast-und-darlegungslast, eigenbedarfskuendigung-erstellen) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-05-lage-und-ausstattung-bis-mandat-triage-mietre` | mietrecht: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (lage-und-ausstattung-erheben, mahnung-zahlungsverzug-mieter, mandat-triage-mietrecht) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-06-miet-kuendigungsschu-bis-mieteranfragen-beant` | mietrecht: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (miet-kuendigungsschutz-checkliste, miet-mietminderung-mangel-spezial, mieteranfragen-beantworten) und bewahrt deren Workflows, Normanker, Prüfprogramme und A... |
| `kompendium-07-mieterhoehung-pruefe-bis-mietkaution-rueckfor` | mietrecht: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (mieterhoehung-pruefen-widersprechen, mieterhoehungsverlangen-erstellen, mietkaution-rueckforderung) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `kompendium-08-mietpreisueberhoehun-bis-mietspiegel-quellen` | mietrecht: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (mietpreisueberhoehung-wistrg-1954-mietwucher, mietsenkungsverlangen, mietspiegel-quellen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemu... |
| `kompendium-09-mr-betriebskostenabr-bis-mr-modernisierung-un` | mietrecht: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (mr-betriebskostenabrechnung-fehler-spezial, mr-kuendigungsschutz-praxis, mr-modernisierung-und-rolling-rent-spezial) und bewahrt deren Workflows, Normanker,... |
| `kompendium-10-nebenkostenabrechnun-bis-rechtsstand-mai-2026` | mietrecht: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (nebenkostenabrechnung-erstellen, nebenkostenabrechnung-pruefen, rechtsstand-mai-2026-faktenbank) und bewahrt deren Workflows, Normanker, Prüfprogramme und Au... |
| `kompendium-11-spezial-amtlichen-ri-bis-spezial-ausschliessl` | mietrecht: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-amtlichen-risikoampel-und-gegenargumente, spezial-amtsgericht-sonderfall-und-edge-case, spezial-ausschliesslich-dokumentenmatrix-und-lueckenliste) un... |
| `kompendium-12-spezial-bundesland-v-bis-spezial-grossstadt-m` | mietrecht: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-bundesland-verhandlung-vergleich-und-eskalation, spezial-datenerhebung-zahlen-schwellen-und-berechnung, spezial-grossstadt-mietspiegel-und-kappung) u... |
| `kompendium-13-spezial-mieter-tatbe-bis-spezial-mieterhoehun` | mietrecht: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-mieter-tatbestand-beweis-und-belege, spezial-mieteranfragen-mandantenentscheidung, spezial-mieterhoehungs-compliance-dokumentation-und-akte) und bewa... |
| `kompendium-14-spezial-mietrecht-er-bis-spezial-mietspiegel` | mietrecht: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-mietrecht-erstpruefung-und-mandatsziel, spezial-mietsenkungsverlangen-international-schnittstellen, spezial-mietspiegel-behoerden-gericht-und-registe... |
| `kompendium-15-spezial-nebenkostenp-bis-spezial-quellen-schr` | mietrecht: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-nebenkostenpruefung-formular-portal-und-einreichung, spezial-prozessstrategie-mieterhoehung, spezial-quellen-schriftsatz-brief-und-memo-bausteine) un... |
| `kompendium-16-spezial-widerspruch-bis-weg-beschluss-anfech` | mietrecht: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (spezial-widerspruch-mehrparteien-konflikt-und-interessen, v90-betriebskostenabrechnung-belege-und-formelpruefer, weg-beschluss-anfechten) und bewahrt deren W... |
| `spezial-erstellung-red-team-und-qualitaetskontrolle` | Erstellung: Red-Team und Qualitätskontrolle im Mietrecht: fachlich vertiefter Spezialskill mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbare... |
| `spezial-universitaetsstaedte-livequellen-check` | Universitaetsstaedte: Livequellen- und Rechtsprechungscheck im Mietrecht: fachlich vertiefter Spezialskill mit Normenradar (BGB/BetrKV/HeizkostenV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und... |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin mietrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin mietrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin mietrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin mietrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin mietrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin mietrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
