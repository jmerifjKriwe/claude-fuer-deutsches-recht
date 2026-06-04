# Bundeswehrrecht und Wehrrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`bundeswehrrecht-wehrrecht`) | [`bundeswehrrecht-wehrrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/bundeswehrrecht-wehrrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **KDV-Verfahren Malte Eberhard Rabenow / Berlin-Köln 2026** (`kriegsdienstverweigerung-gewissensantrag-berlin-2026`) | [Gesamt-PDF lesen](../testakten/kriegsdienstverweigerung-gewissensantrag-berlin-2026/gesamt-pdf/kriegsdienstverweigerung-gewissensantrag-berlin-2026_gesamt.pdf) | [`testakte-kriegsdienstverweigerung-gewissensantrag-berlin-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kriegsdienstverweigerung-gewissensantrag-berlin-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Super-Plugin für Soldatenrecht, Wehrbeschwerde, Disziplinarrecht, Wehrpflicht, Reservisten, Versorgung und Bundeswehrverwaltung.

## Wofür dieses Plugin da ist
Bundeswehrrecht mit Soldatengesetz, Wehrbeschwerdeordnung, Wehrdisziplinarordnung, Wehrpflichtgesetz, Reservistenrecht, Soldatenversorgung, Befehlsrecht, Fürsorge und Rechtsschutz.

Das Plugin ist als Arbeitswerkzeug gedacht: Es startet mit einem Kaltstart-Interview, sortiert Unterlagen, prüft Fristen und routet dann in Spezial-Skills. Es soll Anfänger an die Hand nehmen und Profis schnell zu belastbaren Outputs bringen.

## Typischer Workflow
1. **Allgemein-Skill starten:** Rolle, Ziel, Frist, Unterlagen und gewünschtes Ergebnis klären.
2. **Dokumente einlesen:** Verträge, Bescheide, Rechnungen, Tabellen, Registerdaten, Behördenpost oder Screenshots strukturieren.
3. **Spezial-Skill wählen:** Das Plugin schlägt den passenden Skill vor und erklärt, welches Ergebnis damit entsteht.
4. **Live-Quellen prüfen:** Normtext, Behördenseite, EU-Text, Formular oder frei zugängliche Rechtsprechung aktualisieren.
5. **Output erzeugen:** Memo, Antrag, Stellungnahme, Vertragsklausel, Berechnung, Checkliste oder Mandantenbrief.
6. **Red-Team:** Fristen, Zuständigkeit, Zahlen, Quellen und Gegenargumente kontrollieren.

## Quellenanker
- Amtliche Gesetzestexte: gesetze-im-internet.de.
- EU-Recht: EUR-Lex und amtliche Kommissionsseiten.
- Behördenpraxis: zuständige Bundes-/Landesbehörden, Bundesnetzagentur, BaFin, BfArM, G-BA, BKartA oder Länderstellen je nach Thema.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei/amtlich prüfbarer Quelle.

## Skill-Schwerpunkte
| Gruppe | Inhalt |
| --- | --- |
| Einstieg und Workflow | Kaltstart, Dokumentenintake, Fristen, Quellencheck, Output-Wahl, Red-Team |
| Materielle Prüfung | Tatbestände, Ausnahmen, Schwellen, Beweislast, Berechnungen, Rechtsfolgen |
| Verfahren und Kommunikation | Anträge, Anhörungen, Beschwerden, Schriftsätze, Behördenkontakt, Mandantenkommunikation |
| Spezialthemen | Branchen-, Vertrags-, Gebühren-, Aufsichts-, EU- und Edge-Case-Prüfungen |

## Quellen- und Halluzinationsschutz
Dieses Plugin soll keine nicht prüfbaren Fundstellen produzieren. Bei unsicherer oder dynamischer Rechtslage wird der Live-Quellencheck ausdrücklich vorgeschaltet.

## Lizenz
Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Bundeswehrrecht und Wehrrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, erkennt stumme Uploads und schlägt passende Spezial-Skills aus diesem Plugin vor. |
| `kaltstart-bundeswehrrecht` | Kaltstart Bundeswehrrecht: schneller Einstieg und Routing zu den richtigen Spezial-Skills bei unbekanntem Sachverhalt. Norm-/Quellenanker: SG, WBO, WDO, SVG. |
| `kompendium-01-beschwerde-fristen-s-bis-disziplinarverfahren` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (beschwerde-fristen-sofortcheck, bwbes-neu-010-besoldungswiderspruch-soldat-und-fristen, disziplinarverfahren-intake) und bewahrt deren Workfl... |
| `kompendium-02-eilverfahren-konkurr-bis-gerichtliches-diszip` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (eilverfahren-konkurrentenstreit-wehrdienstsenat, fristenkalender-bundeswehrrecht, gerichtliches-disziplinarverfahren-soldat) und bewahrt dere... |
| `kompendium-03-kriegsdienstverweige-bis-truppendienstgericht` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (kriegsdienstverweigerung-verfahren, rechtsbeistand-im-disziplinarverfahren, truppendienstgericht-zustaendigkeit-verfahren) und bewahrt deren... |
| `kompendium-04-wehrbeschwerdeordnun-bis-aerztliche-begutacht` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (wehrbeschwerdeordnung-beschwerde-frist-form, schadenersatz-regress-dienstunfall-material, aerztliche-begutachtung-dienstfaehigkeit) und bewah... |
| `kompendium-05-akteneinsicht-wbo-wd-bis-ausbildung-studium-b` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (akteneinsicht-wbo-wdo, arbeitsrecht-zivile-bundeswehrbeschaeftigte, ausbildung-studium-bundeswehr-rueckforderung-ausbildungskosten) und bewah... |
| `kompendium-06-auslandseinsatz-mand-bis-befehl-verweigern-ge` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (auslandseinsatz-mandat-einsatzregeln, beamtenrecht-bundeswehrverwaltung-abgrenzung, befehl-verweigern-gewissensnot-rechtswidrigkeit) und bewa... |
| `kompendium-07-beschwerde-gegen-beu-bis-beurteilung-konkurre` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (beschwerde-gegen-beurteilung-und-laufbahnentscheidung, besoldung-zulagen-auslandsverwendungszuschlag, beurteilung-konkurrentenstreit-auswahle... |
| `kompendium-08-bundesverwaltungsger-bis-bwbes-neu-002-wehrso` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (bundesverwaltungsgericht-wehrdienstsenate, bwbes-neu-001-soldatenbesoldung-grundgehalt-und-dienstgrad, bwbes-neu-002-wehrsold-freiwilliger-we... |
| `kompendium-09-bwbes-neu-003-auslan-bis-bwbes-neu-005-erschw` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (bwbes-neu-003-auslandsverwendungszuschlag-und-einsatzversorgung, bwbes-neu-004-trennungsgeld-umzugskosten-reisebeihilfe, bwbes-neu-005-erschw... |
| `kompendium-10-bwbes-neu-006-dienst-bis-bwbes-neu-008-heilfu` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (bwbes-neu-006-dienstzeitversorgung-berufsfoerderungsdienst, bwbes-neu-007-soldatenversorgung-dienstunfall-wehrdienstbeschaed, bwbes-neu-008-h... |
| `kompendium-11-bwbes-neu-009-besold-bis-bwbes-neu-012-diszip` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (bwbes-neu-009-besoldung-reservist-wehruebung-und-arbeitgeberausg, bwbes-neu-011-kdv-und-besoldungsfolgen-bei-statuswechsel, bwbes-neu-012-dis... |
| `kompendium-12-bwbes-neu-013-verwen-bis-bwbes-neu-015-ruhens` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (bwbes-neu-013-verwendungsfaehigkeit-tauglichkeit-und-finanzielle, bwbes-neu-014-auslandseinsatz-anerkennung-und-nachweise, bwbes-neu-015-ruhe... |
| `kompendium-13-dienstunfaehigkeit-e-bis-einsatz-unfall-verso` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (dienstunfaehigkeit-entlassung-zurruhesetzung, dienstzeit-soldat-auf-zeit-berufssoldat-fwdl, einsatz-unfall-versorgung-dokumentenplan) und bew... |
| `kompendium-14-einsatzunfall-wehrdi-bis-ernennung-dienstgrad` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (einsatzunfall-wehrdienstbeschaedigung, entlassung-auf-eigenen-antrag, ernennung-dienstgrad-laufbahnrecht) und bewahrt deren Workflows, Norman... |
| `kompendium-15-extremismus-verdacht-bis-gehorsam-befehl-und` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (extremismus-verdachtsfall-sicherheitsrecht, geheimschutz-sicherheitsueberpruefung-sueg, gehorsam-befehl-und-rechtswidriger-befehl) und bewahr... |
| `kompendium-16-gleichstellung-diskr-bis-kameradschaft-achtun` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (gleichstellung-diskriminierung-soldatinnen-soldaten, impfpflicht-tauglichkeit-musterung, kameradschaft-achtungs-und-vertrauenspflicht) und be... |
| `kompendium-17-livecheck-sg-wbo-wdo-bis-mobbing-fuersorgepfl` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (livecheck-sg-wbo-wdo-wpflg-svg, mandantenbrief-soldat-verstaendlich, mobbing-fuersorgepflicht-bundeswehr) und bewahrt deren Workflows, Norman... |
| `kompendium-18-nebentaetigkeit-gesc-bis-personalvertretung-z` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (nebentaetigkeit-geschenkannahme-compliance, personalakte-einsicht-datenschutz, personalvertretung-zivile-beschaeftigte-schnittstelle) und bew... |
| `kompendium-19-pflicht-zum-treuen-d-bis-presseaeusserung-mei` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 19; bündelt 3 frühere Spezialskills (pflicht-zum-treuen-dienen-7-sg, politische-betaetigung-maessigung-neutralitaet, presseaeusserung-meinungsfreiheit-soldat) und bewahrt deren W... |
| `kompendium-20-ptbs-einsatzfolge-be-bis-sanitaetsdienst-heil` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 20; bündelt 3 frühere Spezialskills (ptbs-einsatzfolge-beweisfuehrung, reservistendienst-dienstleistungspflicht, sanitaetsdienst-heilfuersorge) und bewahrt deren Workflows, Norma... |
| `kompendium-21-sexuelle-belaestigun-bis-soldatenbeteiligung` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 21; bündelt 3 frühere Spezialskills (sexuelle-belaestigung-beschwerde-schutzpflicht, social-media-soldat-dienstpflichten, soldatenbeteiligung-vertrauensperson-sbg) und bewahrt de... |
| `kompendium-22-soldatengesetz-recht-bis-status-soldat-beamte` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 22; bündelt 3 frühere Spezialskills (soldatengesetz-rechtsstellung-grundpflichten, soldatenversorgungsgesetz-beschaedigtenversorgung, status-soldat-beamter-zivilbeschaeftigter-kl... |
| `kompendium-23-statusrechte-im-eins-bis-unterhaltssicherung` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 23; bündelt 3 frühere Spezialskills (statusrechte-im-einsatz-urlaub-betreuung, trennungsgeld-umzugskosten-reisekosten, unterhaltssicherung-reservisten) und bewahrt deren Workflow... |
| `kompendium-24-versetzung-kommandie-bis-wehrdisziplinarordnu` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 24; bündelt 3 frühere Spezialskills (versetzung-kommandierung-abordnung, vorlaeufige-dienstenthebung-einbehaltung-bezuege, wehrdisziplinarordnung-einfache-disziplinarmassnahme) u... |
| `kompendium-25-wehrpflicht-wehrdien-bis-wehrstrafrecht-fahne` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 25; bündelt 3 frühere Spezialskills (wehrpflicht-wehrdienst-reservist-routing, wehrpflichtgesetz-spannungs-und-verteidigungsfall, wehrstrafrecht-fahnenflucht-gehorsamsverweigerun... |
| `kompendium-26-wehruebungen-heranzi-bis-widerruf-ernennung-a` | bundeswehrrecht-wehrrecht: Konsolidiertes Skill-Kompendium 26; bündelt 3 frühere Spezialskills (wehruebungen-heranziehungsbescheid, weitere-beschwerde-und-gerichtlicher-antrag-wehrdienstgericht, widerruf-ernennung-arglistige-taeuschung)... |
| `output-beschwerde-antrag-stellungnahme` | Output Beschwerde, Antrag, Stellungnahme: erstellt strukturierte Schriftstücke nach WBO, WDO und VwGO. Norm-/Quellenanker: WBO §§ 6–11, WDO, VwGO. |
| `red-team-bundeswehr-beschwerde` | Red-Team Bundeswehr-Beschwerde: kritische Gegenprüfung einer Beschwerde auf Schwachstellen, Gegenargumente und Verbesserungen. Norm-/Quellenanker: WBO, WDO, VwGO. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
