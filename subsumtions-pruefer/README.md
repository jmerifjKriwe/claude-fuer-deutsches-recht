# Subsumtions-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`subsumtions-pruefer`) | [`subsumtions-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/subsumtions-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Subsumtionskontrolle / Klausurkorrektur — Übung für Fortgeschrittene BGB, Uni Bielefeld, Lehrstuhl Pohlmann-Wittfeldt, SS 2026** (`subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann`) | [Gesamt-PDF lesen](../testakten/subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann/gesamt-pdf/subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann_gesamt.pdf) | [`testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-subsumtions-klausurkorrekt-bgb-fall-fortgeschrittene-uni-bielefeld-pohlmann-eichmann.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Interaktiver Mechanik-Workflow für die juristische Subsumtion nach deutschem Recht und Europarecht. Das Plugin zerlegt Normen in Tatbestandsmerkmale, führt das Vier-Schritt-Schema (Obersatz – Definition – Untersatz – Ergebnis) durch, erfasst Beweisbedarf und erzeugt Ausgabedokumente in verschiedenen Formaten.

**Dieses Plugin ist keine Rechtsberatung.** Es prüft mechanisch eine vom Nutzer behauptete Norm anhand vom Nutzer behaupteter Tatsachen. Die Auswahl der richtigen Norm, die vollständige Sachverhaltsdarstellung und die Bewertung des Ergebnisses bleiben in der Verantwortung des Nutzers und eines zugelassenen Rechtsanwalts.

## Für wen ist dieses Plugin

| Rolle | Primäre Anwendungsfälle |
|---|---|
| Privatpersonen | Verstehen, ob ein Anspruch dem Grunde nach bestehen könnte |
| Paralegal / Rechtsfachwirt | Strukturierte Erstsichtung vor anwaltlicher Prüfung |
| Jurastudent / Referendar | Subsumtionsübung ohne Musterlösung |
| Unternehmensjurist | Schnelle Erstprüfung einer Norm vor Mandatserteilung |
| Behördenmitarbeiter | Strukturiertes Durchprüfen von Tatbestandsvoraussetzungen |

## Abgedeckte Rechtsgebiete

- **Deutsches Recht:** BGB (Schuld-, Sachen-, Familien-, Erbrecht), HGB, StGB, StPO, ZPO, VwGO, VwVfG, GG, AO, SGB, KSchG, AGG, GWB, UWG und Nebengesetze
- **BGB AT:** Für Vertragsschluss, Willenserklärung, Zugang, Geschäftsfähigkeit, Form, Anfechtung, Stellvertretung, Fristen und Verjährung sollte `bgb-at-pruefer` vor oder neben diesem generischen Subsumtions-Plugin geladen werden.
- **Europarecht:** AEUV, EUV, GRCh (Primärrecht); DSGVO, KI-VO, Produkthaftungsrichtlinie, Verbraucherrechterichtlinie, Vergaberichtlinien u. a. (Sekundärrecht); EuGH-Judikatur

## Workflow-Überblick

```
Einstieg
│
├─ triage-rechtsfrage-oder-norm
│   Sachverhalt / Rechtsfrage / Norm erfassen
│
├─ ziel-und-rechtsweg-bestimmung
│   Was will der Nutzer? Welches Gericht?
│
├─ falsche-wiese-warnung
│   Fehlverortungen erkennen
│
├─ de-eu-recht-abgrenzung
│   Welches Recht gilt?
│
Normbestimmung
│
├─ einschlaegige-normen-vorschlagen-de / -eu
├─ norm-historie-und-aenderungen
├─ rechtsprechung-recherche-strategie
│
Subsumtion
│
├─ norm-zerlegen-in-tatbestandsmerkmale
├─ ungeschriebene-merkmale-judikatur
├─ generalklauseln-pruefen
├─ unbestimmte-rechtsbegriffe-pruefen
├─ subsumtion-obersatz-definition-untersatz-ergebnis
├─ beweisbedarf-und-belege-erfassen
├─ darlegungs-und-beweislast-verteilen
├─ gegen-tbm-und-einreden-pruefen
│
Rechtsfolgen
│
├─ rechtsfolge-bestimmen
├─ konkurrenzen-anspruchsgrundlagen
├─ verjaehrung-fristen-pruefen
├─ verfahrensart-bestimmen
├─ eu-vorabentscheidung-pruefen
├─ grundrechte-pruefung-de-und-grch
│
Ausgabe (wählbar)
│
├─ output-juristisch-gestochen-de
├─ output-alltagssprache-de
├─ output-fremdsprachig-en-fr
├─ output-antrag-beschwerde-klageschrift
├─ output-memo-und-mandantenbrief
└─ output-pruefungsdokument-mit-warnhinweisen
```

## Wichtige Warnhinweise

Das System warnt aktiv in folgenden Situationen:

- **Falsche Norm:** Sachverhalt passt nicht zur gewählten Norm (`falsche-wiese-warnung`)
- **Komplexitätsgrenze:** Sachverhalt zu komplex für mechanische Prüfung (`mandatsabbruch-empfehlung-an-fachanwalt`)
- **Generalklauseln:** Kein mechanisch abschließbares Ergebnis möglich (`generalklauseln-pruefen`)
- **Unbestimmte Rechtsbegriffe:** Nur Indiziensammlung, keine Subsumtion (`unbestimmte-rechtsbegriffe-pruefen`)
- **Offene TBM:** Fehlende Belege gefährden das Ergebnis (`beweisbedarf-und-belege-erfassen`)

## Skills (31)

### A. Triage / Workflow-Einstieg

| Skill | Funktion |
|---|---|
| `triage-rechtsfrage-oder-norm` | Interaktive Erfassung der Nutzereingabe |
| `ziel-und-rechtsweg-bestimmung` | Ziel und Rechtsweg ermitteln |
| `falsche-wiese-warnung` | Typische Fehlverortungen erkennen |
| `de-eu-recht-abgrenzung` | Nationales vs. Unionsrecht abgrenzen |
| `mandatsabbruch-empfehlung-an-fachanwalt` | Komplexitätsgrenze erkennen, Fachanwalt empfehlen |

### B. Normbestimmung und Recherche

| Skill | Funktion |
|---|---|
| `einschlaegige-normen-vorschlagen-de` | Deutsche Normen anhand Sachverhalt vorschlagen |
| `einschlaegige-normen-vorschlagen-eu` | EU-Normen anhand Sachverhalt vorschlagen |
| `rechtsprechung-recherche-strategie` | Recherche-Strategie und Fundstellen |
| `norm-historie-und-aenderungen` | Geltende Fassung und Übergangsrecht |
| `kommentar-und-literatur-hinweis` | Standardkommentare und Literaturhinweise |

### C. Tatbestandsmerkmale und Subsumtion

| Skill | Funktion |
|---|---|
| `norm-zerlegen-in-tatbestandsmerkmale` | TBM-Liste mit Definitionen |
| `ungeschriebene-merkmale-judikatur` | Richterrechtlich entwickelte Merkmale |
| `generalklauseln-pruefen` | Generalklauseln — Indizien und Fallgruppen |
| `unbestimmte-rechtsbegriffe-pruefen` | Auslegungsmaßstäbe für unbestimmte Begriffe |
| `subsumtion-obersatz-definition-untersatz-ergebnis` | Vier-Schritt-Schema je TBM |
| `beweisbedarf-und-belege-erfassen` | Beweismittel-Katalog und Tracking |
| `darlegungs-und-beweislast-verteilen` | Beweislast pro TBM |
| `gegen-tbm-und-einreden-pruefen` | Einwendungen und Einreden |

### D. Rechtsfolgen, Konkurrenzen, Verfahren

| Skill | Funktion |
|---|---|
| `rechtsfolge-bestimmen` | Anspruchsinhalt, Höhe, Nebenansprüche |
| `konkurrenzen-anspruchsgrundlagen` | Normkonkurrenzen und Spezialität |
| `verjaehrung-fristen-pruefen` | Verjährung, Hemmung, Neubeginn |
| `verfahrensart-bestimmen` | Passende Verfahrensart und Zuständigkeit |
| `eu-vorabentscheidung-pruefen` | Art. 267 AEUV — Voraussetzungen |
| `grundrechte-pruefung-de-und-grch` | GG und GRCh — Drei-Schritt-Schema |

### E. Output-Erzeugung

| Skill | Funktion |
|---|---|
| `output-juristisch-gestochen-de` | Schriftsatzstil, Rubrum, Tenor |
| `output-alltagssprache-de` | Verständliche Sprache für Betroffene |
| `output-fremdsprachig-en-fr` | Englisch und Französisch (nicht-amtlich) |
| `output-antrag-beschwerde-klageschrift` | Formale Dokument-Bausteine |
| `output-memo-und-mandantenbrief` | Aktennotiz und Mandantenbrief |
| `output-pruefungsdokument-mit-warnhinweisen` | Vollständiges Dokument mit allen Warnhinweisen |

## Lizenz

Apache-2.0 OR MIT — siehe LICENSE im Repository-Root.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 23 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `kompendium-02-workflow-output-waeh-bis-spezial-europarecht` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-output-waehlen, rechtsprechung-recherche-strategie, spezial-europarecht-fristen-form-und-zustaendigkeit) und bewahrt deren Workflows, Norm... |
| `kompendium-03-verfahrensart-bestim-bis-generalklauseln-prue` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (verfahrensart-bestimmen, verjaehrung-fristen-pruefen, generalklauseln-pruefen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemus... |
| `kompendium-04-mandatsabbruch-empfe-bis-darlegungs-und-bewei` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (mandatsabbruch-empfehlung-an-fachanwalt, beweisbedarf-und-belege-erfassen, darlegungs-und-beweislast-verteilen) und bewahrt deren Workflows, Norman... |
| `kompendium-05-de-eu-recht-abgrenzu-bis-einschlaegige-normen` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (de-eu-recht-abgrenzung, einschlaegige-normen-vorschlagen-de, einschlaegige-normen-vorschlagen-eu) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-06-eu-vorabentscheidung-bis-fehlerklasse-bgb-at` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (eu-vorabentscheidung-pruefen, falsche-wiese-warnung, fehlerklasse-bgb-at-training) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `kompendium-07-gegen-tbm-und-einred-bis-kandidatenloesung-su` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (gegen-tbm-und-einreden-pruefen, grundrechte-pruefung-de-und-grch, kandidatenloesung-subsumtion-pruefen) und bewahrt deren Workflows, Normanker, Prü... |
| `kompendium-08-kommentar-und-litera-bis-norm-historie-und-ae` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (kommentar-und-literatur-hinweis, konkurrenzen-anspruchsgrundlagen, norm-historie-und-aenderungen) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-09-norm-zerlegen-in-tat-bis-output-pruefungsdoku` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (norm-zerlegen-in-tatbestandsmerkmale, output-memo-und-mandantenbrief, output-pruefungsdokument-mit-warnhinweisen) und bewahrt deren Workflows, Norm... |
| `kompendium-10-rechtsfolge-bestimme-bis-spezial-interaktiver` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (rechtsfolge-bestimmen, spezial-einreden-compliance-dokumentation-und-akte, spezial-interaktiver-erstpruefung-und-mandatsziel) und bewahrt deren Wor... |
| `kompendium-11-spezial-pruefen-mehr-bis-spezial-rechtsfolgen` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-pruefen-mehrparteien-konflikt-und-interessen, spezial-rechtsberatung-internationaler-bezug-und-schnittstellen, spezial-rechtsfolgen-zahlen-... |
| `kompendium-12-spezial-schema-verha-bis-spezial-subsumtions` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-schema-verhandlung-vergleich-und-eskalation, spezial-schritt-schriftsatz-brief-und-memo-bausteine, spezial-subsumtions-tatbestand-beweis-un... |
| `kompendium-13-spezial-tatbestandsm-bis-spezial-zerlegen-ris` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-tatbestandsmerkmale-dokumentenmatrix-und-lueckenliste, spezial-vier-behoerden-gericht-und-registerweg, spezial-zerlegen-risikoampel-und-geg... |
| `kompendium-14-subsumtion-obersatz-bis-triage-rechtsfrage-o` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (subsumtion-obersatz-definition-untersatz-ergebnis, subsumtions-rewrite-klausurton, triage-rechtsfrage-oder-norm) und bewahrt deren Workflows, Norma... |
| `kompendium-15-unbestimmte-rechtsbe-bis-ziel-und-rechtsweg-b` | subsumtions-pruefer: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (unbestimmte-rechtsbegriffe-pruefen, ungeschriebene-merkmale-judikatur, ziel-und-rechtsweg-bestimmung) und bewahrt deren Workflows, Normanker, Prüfp... |
| `output-alltagssprache-de` | Gibt das Subsumtionsergebnis in verstaendlicher Alltagssprache aus: ohne Fachbegriffe oder mit Erklärung, für Mandanten, Betroffene oder Behoerdenmitarbeiter. Behaelt die Strukturierung bei, vermeidet aber Lateinismen und Fachterminologi... |
| `output-antrag-beschwerde-klageschrift` | Erzeugt Tenor-Bausteine, Rubrum und formale Mindestanforderungen für Antrag, Beschwerde und Klageschrift nach ZPO, VwGO, SGG, FGO und BVerfGG. Gibt Pflichtangaben, Fristen und Einreichungshinweise. Kein anwaltlicher Schriftsatz ohne anwa... |
| `output-fremdsprachig-en-fr` | Gibt das Subsumtionsergebnis auf Englisch oder Franzoesisch aus. Enthaelt obligatorischen Hinweis auf nicht-amtliche Übersetzung und Abweichung von deutschen Originalnormen. Nuetzlich für internationale Mandanten, grenzüberschreitende Sa... |
| `output-juristisch-gestochen-de` | Erzeugt Ausgaben im juristischen Schriftsatzstil auf Deutsch: Antrag-Begründung-Beweismittel-Struktur, Subsumtionsdarstellung im Vier-Schritt, Zitierweise nach BGH-Standard, Rubrum, Tenor. Für Schriftsaetze, Klageschriften, Widersprueche... |
| `spezial-anwenden-livequellen-und-rechtsprechungscheck` | Anwenden: Livequellen- und Rechtsprechungscheck im Plugin subsumtions-pruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin subsumtions-pruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin subsumtions-pruefer: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin subsumtions-pruefer: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
