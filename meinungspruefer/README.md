# Meinungsprüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`meinungspruefer`) | [`meinungspruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/meinungspruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Meinungsprüfer - Grenzfälle im Alltag** (`meinungspruefer-grenzfaelle-alltag`) | [Gesamt-PDF lesen](../testakten/meinungspruefer-grenzfaelle-alltag/gesamt-pdf/meinungspruefer-grenzfaelle-alltag_gesamt.pdf) | [`testakte-meinungspruefer-grenzfaelle-alltag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-meinungspruefer-grenzfaelle-alltag.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für die Prüfung von Äußerungen nach einfachem Recht, Verfassungsrecht, Europarecht und Rechtsvergleich: Meinung oder Tatsachenbehauptung, Beleidigung, üble Nachrede, Verleumdung, Personen des politischen Lebens, Wahrnehmung berechtigter Interessen, zivilrechtliche Unterlassung, Widerruf, Geldentschädigung, Plattform- und Social-Media-Kontext, EGMR/EuGH/GRCh, OLG-/KG-Praxis und US-Supreme-Court-Vergleich.

**Keine Rechtsberatung.** Das Plugin erzeugt eine strukturierte Vorprüfung und dokumentierbare Arbeitsprodukte zur anwaltlichen Kontrolle. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle verwendet.

## Start

```
/meinungspruefer:allgemein
```

Der Einstieg fragt schnell ab: exakter Wortlaut, Medium, Publikum, Anlass, Vorgeschichte, Betroffene, Tatsachenkern, Belege, Wiederholungsgefahr, gewünschter Output und Risikotoleranz. Danach routet er zu den passenden Spezialskills.

## Skills (36)

| Skill | Zweck |
|---|---|
| `allgemein` | Schöner Einstieg, Schnelltriage, Quellenhygiene und Routing |
| `schnelltriage-aeusserung` | Erste Ampel für Strafrecht, Zivilrecht, Plattform und arbeits-/schulbezogene Risiken |
| `zitat-und-kontextaufnahme` | Wortlaut, Kontext, Adressatenkreis, Medium und Vorgeschichte sauber erfassen |
| `meinung-tatsache-abgrenzung` | Meinung, Tatsache, gemischte Äußerung und Tatsachenkern trennen |
| `mehrdeutigkeit-sinnermittlung` | Sinnermittlung, Durchschnittspublikum und nicht ehrverletzende Deutungen |
| `beleglage-tatsachenbehauptung` | Belegmatrix für Tatsachen, Verdachtsäußerung und erwiesen unwahre Behauptung |
| `strafrecht-185-beleidigung` | § 185 StGB mit Art.-5-GG-Abwägung |
| `ueble-nachrede-186` | § 186 StGB, Nichterweislichkeit und Tatsachenkern |
| `verleumdung-187` | § 187 StGB, Wissen um Unwahrheit und Belegprüfung |
| `personen-politisches-leben-188` | § 188 StGB, Person des politischen Lebens, Öffentlichkeit und Erschwerung des Wirkens |
| `wahrnehmung-berechtigter-interessen-193` | § 193 StGB, Beschwerde, Bewertung, Mandats-/Arbeits-/Bürgerkontext |
| `strafantrag-194-und-verfahren` | Strafantrag, Antragsberechtigte, Fristen, Privatklage, Einstellungsoptionen |
| `schmaehkritik-formalbeleidigung-menschenwuerde` | Enge Ausnahmen ohne Normalabwägung |
| `abwaegung-art-5-gg` | Verfassungsrechtlicher Abwägungskern nach Art. 5 GG |
| `machtkritik-amtstraeger` | Amtsträger, Behörden, Bürgermeister, Schule, Justiz und Machtkritik |
| `arbeitgeber-betrieb-kantine` | Arbeitsplatz, Kantine, Kollegium, Betriebsrat, arbeitsrechtliche Nebenfolgen |
| `schule-elternchat` | Schule, Elternchat, Lehrkräfte, Schulleitung und pädagogischer Konflikt |
| `soziale-medien-x-linkedin` | X, LinkedIn, Kommentarspalten, Sichtbarkeit, Prangerwirkung, Screenshots |
| `kommunalrecht-buergermeister` | Kommunale Debatte, Bauprojekt, Ratssitzung, Amts- und Privatrolle |
| `satire-ironisierung-pinocchio` | Satire, Überzeichnung, Pinocchio-Vergleich, Lügenvorwurf als Wertung oder Tatsache |
| `schimpfwort-lackaffe-und-spott` | Spottbegriffe wie Lackaffe im Kontext prüfen |
| `zivilrecht-unterlassung-widerruf-schadensersatz` | APR, §§ 823, 1004 BGB analog, § 824 BGB und Beseitigungsansprüche |
| `presserecht-plattformen-loeschung-dsa` | Medien, Plattformmeldungen, Löschung, Sperrung und DSA-Schnittstellen |
| `europarecht-emrk-grch` | Art. 10 EMRK, Art. 11 GRCh, unions- und konventionsfreundliche Lesart |
| `egmr-art-10-rechtsprechung` | EGMR-Leitlinien zu öffentlicher Debatte, Werturteil, Tatsachengrundlage, Art.-8-/Art.-10-Abwägung, Hyperlinks und Drittkommentaren |
| `eugh-grch-art-11-rechtsprechung` | EuGH/GRCh bei Plattformen, Suchmaschinen, Datenschutz, Uploadfiltern, De-Referenzierung und journalistischen Zwecken |
| `olg-kg-praxis-rechtsprechung` | Obergerichtliche Praxis zu Unterlassung, Sinnermittlung, Social Media, Verdachtsäußerung, Plattformlabel und Tenorrisiko |
| `rechtsvergleich-usa-supreme-court` | US-Supreme-Court-Vergleich zu First Amendment, actual malice, public concern, opinion, parody, threats und incitement |
| `beweissicherung-screenshots` | Screenshots, Metadaten, Zeugen, URLs, Löschungen, Chatverläufe |
| `risikomatrix-ampel` | Ergebnis als Grün/Gelb/Rot mit Unsicherheiten und nächstem Schritt |
| `gegendarstellung-entschuldigung-deeskalation` | Reaktionsoptionen ohne unnötige Eskalation |
| `abmahnung-strafanzeige-reaktion` | Eingang von Abmahnung, Strafanzeige, Anhörung oder Plattformmeldung bearbeiten |
| `schriftsatz-stellungnahme-verteidigung` | Verteidigungs- und Erwiderungsbausteine |
| `output-memo-pruefvermerk` | Dokumentierter Prüfvermerk mit Zitat, Kontext, Normen und Ergebnis |
| `testakte-auswertung` | Die Testakte strukturiert auswerten |
| `rechtsprechungsbank-verifiziert` | Verifizierte Rechtsprechung mit Datum, Aktenzeichen und freier Quelle |

## Quellenstand

Stand: 05/2026. Kernnormen: Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, §§ 185-188, 192-194 StGB, §§ 823, 824, 1004 BGB analog, § 22 KUG bei Bildern und DSA-Schnittstellen bei Plattformen. Leitentscheidungen sind im Skill `rechtsprechungsbank-verifiziert` dokumentiert; der USA-Vergleich ist ausdrücklich nur Vergleich, kein Import amerikanischer Standards in die deutsche Prüfung.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Meinungsprüfer. Fragt Wortlaut, Kontext, Medium, Publikum, Tatsachenkern, Belege, betroffene Person, Anlass, Vorgeschichte, gewünschtes Ziel und Risiko ab; schlägt passende Spezial-Skills z... |
| `kompendium-01-workflow-chronologie-bis-workflow-fristen-und` | meinungspruefer: Konsolidiertes Skill-Kompendium 01; bündelt 2 frühere Spezialskills (workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-02-egmr-art-10-rechtspr-bis-eugh-grch-art-11-rec` | meinungspruefer: Konsolidiertes Skill-Kompendium 02; bündelt 2 frühere Spezialskills (egmr-art-10-rechtsprechung, eugh-grch-art-11-rechtsprechung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-03-olg-kg-praxis-rechts-bis-rechtsprechungsbank` | meinungspruefer: Konsolidiertes Skill-Kompendium 03; bündelt 2 frühere Spezialskills (olg-kg-praxis-rechtsprechung, rechtsprechungsbank-verifiziert) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-04-spezial-meinung-fris-bis-strafantrag-194-und` | meinungspruefer: Konsolidiertes Skill-Kompendium 04; bündelt 2 frühere Spezialskills (spezial-meinung-fristen-form-und-zustaendigkeit, strafantrag-194-und-verfahren) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-05-zivilrecht-unterlass-bis-abmahnung-strafanzei` | meinungspruefer: Konsolidiertes Skill-Kompendium 05; bündelt 2 frühere Spezialskills (zivilrecht-unterlassung-widerruf-schadensersatz, abmahnung-strafanzeige-reaktion) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-06-abwaegung-art-5-gg-bis-arbeitgeber-betrieb` | meinungspruefer: Konsolidiertes Skill-Kompendium 06; bündelt 2 frühere Spezialskills (abwaegung-art-5-gg, arbeitgeber-betrieb-kantine) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-07-beleglage-tatsachenb-bis-beweissicherung-scre` | meinungspruefer: Konsolidiertes Skill-Kompendium 07; bündelt 2 frühere Spezialskills (beleglage-tatsachenbehauptung, beweissicherung-screenshots) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-08-europarecht-emrk-grc-bis-gegendarstellung-ent` | meinungspruefer: Konsolidiertes Skill-Kompendium 08; bündelt 2 frühere Spezialskills (europarecht-emrk-grch, gegendarstellung-entschuldigung-deeskalation) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-09-kommunalrecht-buerge-bis-machtkritik-amtstrae` | meinungspruefer: Konsolidiertes Skill-Kompendium 09; bündelt 2 frühere Spezialskills (kommunalrecht-buergermeister, machtkritik-amtstraeger) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-10-mehrdeutigkeit-sinne-bis-meinung-tatsache-abg` | meinungspruefer: Konsolidiertes Skill-Kompendium 10; bündelt 2 frühere Spezialskills (mehrdeutigkeit-sinnermittlung, meinung-tatsache-abgrenzung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-11-personen-politisches-bis-presserecht-plattfor` | meinungspruefer: Konsolidiertes Skill-Kompendium 11; bündelt 2 frühere Spezialskills (personen-politisches-leben-188, presserecht-plattformen-loeschung-dsa) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-12-rechtsvergleich-usa-bis-risikomatrix-ampel` | meinungspruefer: Konsolidiertes Skill-Kompendium 12; bündelt 2 frühere Spezialskills (rechtsvergleich-usa-supreme-court, risikomatrix-ampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-13-satire-ironisierung-bis-schimpfwort-lackaffe` | meinungspruefer: Konsolidiertes Skill-Kompendium 13; bündelt 2 frühere Spezialskills (satire-ironisierung-pinocchio, schimpfwort-lackaffe-und-spott) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-14-schmaehkritik-formal-bis-schnelltriage-aeusse` | meinungspruefer: Konsolidiertes Skill-Kompendium 14; bündelt 2 frühere Spezialskills (schmaehkritik-formalbeleidigung-menschenwuerde, schnelltriage-aeusserung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-15-schriftsatz-stellung-bis-schule-elternchat` | meinungspruefer: Konsolidiertes Skill-Kompendium 15; bündelt 2 frühere Spezialskills (schriftsatz-stellungnahme-verteidigung, schule-elternchat) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-16-soziale-medien-x-lin-bis-spezial-aeusserungsr` | meinungspruefer: Konsolidiertes Skill-Kompendium 16; bündelt 2 frühere Spezialskills (soziale-medien-x-linkedin, spezial-aeusserungsrecht-tatbestand-beweis-und-belege) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-17-spezial-beleidigung-bis-spezial-meinungsprue` | meinungspruefer: Konsolidiertes Skill-Kompendium 17; bündelt 2 frühere Spezialskills (spezial-beleidigung-risikoampel-und-gegenargumente, spezial-meinungspruefer-erstpruefung-und-mandatsziel) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-18-spezial-nachrede-sch-bis-spezial-tatsache-dok` | meinungspruefer: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (spezial-nachrede-schriftsatz-brief-und-memo-bausteine, spezial-tatsache-dokumentenmatrix-und-lueckenliste) und bewahrt deren Workflows, Normanker, Prüf... |
| `kompendium-19-spezial-ueble-behoer-bis-spezial-verleumdung` | meinungspruefer: Konsolidiertes Skill-Kompendium 19; bündelt 2 frühere Spezialskills (spezial-ueble-behoerden-gericht-und-registerweg, spezial-verleumdung-verhandlung-vergleich-und-eskalation) und bewahrt deren Workflows, Normanker, Prüf... |
| `kompendium-20-strafrecht-185-belei-bis-testakte-auswertung` | meinungspruefer: Konsolidiertes Skill-Kompendium 20; bündelt 2 frühere Spezialskills (strafrecht-185-beleidigung, testakte-auswertung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-21-ueble-nachrede-186-bis-verleumdung-187` | meinungspruefer: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (ueble-nachrede-186, verleumdung-187) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-22-wahrnehmung-berechti-bis-zitat-und-kontextauf` | meinungspruefer: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (wahrnehmung-berechtigter-interessen-193, zitat-und-kontextaufnahme) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `output-memo-pruefvermerk` | Erzeugt den finalen Prüfvermerk zum Meinungsfall mit Sachverhalt, Wortlaut, Kontext, Normen, Rechtsprechung, Subsumtion, Risikoampel, Belegliste, Alternativformulierungen und Handlungsempfehlung. |
| `spezial-stgb-livequellen-und-rechtsprechungscheck` | Stgb: Livequellen- und Rechtsprechungscheck im Plugin meinungspruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin meinungspruefer: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin meinungspruefer: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin meinungspruefer: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
