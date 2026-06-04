# Staatsanwaltschaft Praxis-Einstieg

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`staatsanwaltschaft-praxis-einstieg`) | [`staatsanwaltschaft-praxis-einstieg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/staatsanwaltschaft-praxis-einstieg.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Praxisplugin für neue Staatsanwältinnen, Staatsanwälte und Sitzungsdienst: Ermittlungsverfahren, Polizei, RiStBV, Vermerke, Beschlagnahme, digitale Beweise, Anklage, Strafbefehl, Hauptverhandlung, Plädoyer, Rechtsmittel und gerichtliche Bußgeldverfahren nach OWiG.

## Worum es geht

Dieses Plugin ist ein experimentelles Arbeits- und Lernwerkzeug. Es soll keine echten Amts-, Mandats-, Steuer-, Prüfungs- oder Berufsgeheimnisse aufnehmen, solange die technische und rechtliche Umgebung dafür nicht ausdrücklich freigegeben ist. Es arbeitet am besten mit anonymisierten, abstrahierten oder synthetischen Fällen und mit Dokumenten, die vor der Nutzung datenschutz- und geheimnisschutzrechtlich geprüft wurden.

## Arbeitsweise

Der Allgemein-Skill startet kurz, sortiert Rolle, Verfahrensstand, Frist, Unterlagen und gewünschtes Arbeitsprodukt und routet dann in die passenden Spezial-Skills. Jeder Skill verlangt Quellenhygiene: Normen, Behördenhinweise, Formulare und Rechtsprechung werden vor tragenden Aussagen live aus amtlichen oder frei zugänglichen Quellen geprüft; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Typische Outputs

- Kurzvermerk und Risikoampel
- Checkliste für den nächsten Arbeitstag
- Fragenliste an Behörde, Gericht, Kammer, Mandant, Partei oder Zeugen
- Entwurf für Verfügung, Vermerk, Schriftsatz, Antrag, E-Mail oder Gesprächsleitfaden
- Red-Team-Check gegen Fristenfehler, Zuständigkeitsfehler und Scheingenauigkeit

## OWiG- und Bußgeldspur

Für Ordnungswidrigkeiten arbeitet das Plugin bewusst mit anderer Sprache: kein Anklagesatz, kein Strafbefehl, sondern Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage über die Staatsanwaltschaft, gerichtliches Bußgeldverfahren, Beschlussverfahren, Hauptverhandlung und Rechtsbeschwerde. Die neuen `owi-*`-Skills helfen insbesondere bei Datenschutzbußgeldern, Verkehrs-OWi, Unternehmensgeldbußen, Aufsichtspflichtverletzungen, Umwelt-/Arbeitsschutz-/Produktsicherheits-OWi und der Frage, wann die Staatsanwaltschaft am Termin nach § 75 OWiG teilnehmen sollte.

## Installation

ZIP aus dem aktuellen Release laden und in Claude Code oder Cowork über Customize Plugins installieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein-kaltstart-und-routing` | Allgemeiner Kaltstart und Routing: Praxis-Skill für neue Staatsanwälte zu führt vom ersten Satz oder Dokument in den richtigen Arbeitsmodus; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächs... |
| `dokumentenintake-und-aktenlog` | Dokumentenintake und Aktenlog: Praxis-Skill für neue Staatsanwälte zu ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und näc... |
| `kompendium-01-quellen-und-rechtspr-bis-fristenkalender-staa` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 01; bündelt 5 frühere Spezialskills (quellen-und-rechtsprechungscheck, anfangsverdacht-und-verfahrenseinleitung, beschleunigtes-verfahren-418-stpo, frist-und-zustaendigk... |
| `kompendium-02-ki-und-deepfake-bewe-bis-owi-einspruch-und-zw` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 02; bündelt 5 frühere Spezialskills (ki-und-deepfake-beweise-strafverfahren, mehrfachverfahren-verbindung-trennung, owi-beschlussverfahren-72-und-widerspruch, owi-datens... |
| `kompendium-03-owi-uebergang-strafv-bis-betrug-onlinehandel` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 03; bündelt 5 frühere Spezialskills (owi-uebergang-strafverfahren-81-82, revision-sta-verfahrensruegen-vorpruefung, sicherungsverfahren-413-stpo, wirtschaftsstrafverfahr... |
| `kompendium-04-owi-bussgeldbescheid-bis-rechtsmittel-sta-ber` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 04; bündelt 5 frühere Spezialskills (owi-bussgeldbescheid-inhalt-und-fehler, owi-umwelt-arbeitsschutz-produkt-bussgeld, beschuldigtenvernehmung-anhoerung, polizei-ermitt... |
| `kompendium-05-steuerstrafrecht-koo-bis-anklageschrift-gross` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 05; bündelt 5 frühere Spezialskills (steuerstrafrecht-kooperation-finanzamt, abschlussverfuegung-anfaengerfehler, aktengeheimnis-und-ki-nutzung-sta, anklageschrift-aufba... |
| `kompendium-06-arbeitsstrafrecht-26-bis-bekaempfung-organisi` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 06; bündelt 5 frühere Spezialskills (arbeitsstrafrecht-266a-und-mindestlohn, aufsichtsbeschwerde-und-dienstweg, befangenheit-richter-antrag-sta, befangenheit-richter-sch... |
| `kompendium-07-berufung-sta-einlege-bis-btmg-kcang-sitzungsd` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 07; bündelt 5 frühere Spezialskills (berufung-sta-einlegen-und-begrenzen, beweisantraege-244-stpo-reagieren, beweisverwertungsverbote-sta, btmg-kcang-mischfaelle, btmg-k... |
| `kompendium-08-cybercrime-logfiles-bis-digitale-spuren-mobi` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 08; bündelt 5 frühere Spezialskills (cybercrime-logfiles-und-chain-of-custody, daten-von-plattformen-bestandsdaten, deal-verstaendigung-257c-stpo-sta, digitale-durchsuch... |
| `kompendium-09-durchsuchung-beschla-bis-einziehung-drittbetr` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 09; bündelt 5 frühere Spezialskills (durchsuchung-beschlagnahme-antrag, durchsuchung-kanzlei-arzt-redaktion, einstellung-153-153a-auflagen, einstellung-153-153a-stpo, ei... |
| `kompendium-10-encrochat-anom-sky-e-bis-europaeischer-haftbe` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 10; bündelt 5 frühere Spezialskills (encrochat-anom-sky-ecc-krypto, encrochat-sky-ecc-anom-beweiswert, entscheidungsvorlage, ermittlungsvermerk-schreiben, europaeischer-... |
| `kompendium-11-geldwaesche-krypto-u-bis-hauptverhandlung-sta` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 11; bündelt 5 frühere Spezialskills (geldwaesche-krypto-und-kontoarrest, haeusliche-gewalt-opferschutz-und-beweis, haftbefehl-und-u-haft-antrag, hasskriminalitaet-online... |
| `kompendium-12-insolvenzverschleppu-bis-koerperverletzung-st` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 12; bündelt 5 frühere Spezialskills (insolvenzverschleppung-und-bankrott, internationaler-beweisimport-verwertung, jugendstrafrecht-erziehungsziel, jugendstrafrecht-sta,... |
| `kompendium-13-konfliktverteidigung-bis-opfer-und-nebenklage` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 13; bündelt 5 frühere Spezialskills (konfliktverteidigung-sitzung-ordnung, konfliktverteidigung-souveraen, korruptionsdelikte-amtstraeger-und-healthcare, mandanten-oder-... |
| `kompendium-14-opferrechte-nebenkla-bis-owi-kommunikation-mi` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 14; bündelt 5 frühere Spezialskills (opferrechte-nebenklage-adhaesion, owi-abwesenheit-betroffener-73-74, owi-beweisaufnahme-77-und-beweisantraege, owi-hauptverhandlung-... |
| `kompendium-15-owi-kosten-vollstrec-bis-owi-verjaehrung-verf` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 15; bündelt 5 frühere Spezialskills (owi-kosten-vollstreckung-und-ruecknahme, owi-opportunitaet-einstellung-47, owi-rechtsbeschwerde-79-80, owi-verbandsgeldbusse-30-130,... |
| `kompendium-16-owi-verkehrsowi-fahr-bis-plaedoyer-staatsanwa` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 16; bündelt 5 frühere Spezialskills (owi-verkehrsowi-fahrverbot-punkte, owi-vorlage-an-amtsgericht-sta-check, pflichtverteidigung-aus-sta-sicht, plaedoyer-beweiswuerdigu... |
| `kompendium-17-polizei-zusammenarbe-bis-rechtshilfe-europaei` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 17; bündelt 5 frühere Spezialskills (polizei-zusammenarbeit-ermittlungsauftrag, presse-und-oeffentlichkeit, presseauskunft-und-oeffentlichkeit, protokoll-und-nachbereitu... |
| `kompendium-18-rechtshilfe-internat-bis-schoeffen-befangenhe` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 18; bündelt 5 frühere Spezialskills (rechtshilfe-international, ristbv-finden-anwenden, ristbv-verfuegungstechnik-standard, sachverstaendige-beauftragen-und-befragen, sc... |
| `kompendium-19-schriftsatz-vermerk-bis-sitzungsdienst-refer` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 19; bündelt 5 frühere Spezialskills (schriftsatz-vermerk-und-mustertext, sexualdelikte-aussage-gegen-aussage, sitzungs-und-terminvorbereitung, sitzungsdienst-amtsgericht... |
| `kompendium-20-staatsanwalt-rolle-l-bis-strafbefehl-tagessae` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 20; bündelt 5 frühere Spezialskills (staatsanwalt-rolle-legalitaet-objektivitaet, staatsanwaltschaft-uebergabe-zwischen-dezernaten, stalking-238-stgb-gewschg-schnittstel... |
| `kompendium-21-u-haft-fluchtgefahr-bis-verkehrsstrafrecht-b` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 21; bündelt 5 frühere Spezialskills (u-haft-fluchtgefahr-verhaeltnismaessigkeit, umweltstrafrecht-behoerdenakten, untreue-geschaeftsfuehrer-kontoanalyse, urheber-und-mar... |
| `kompendium-22-verkehrsstrafrecht-s-bis-waffenrecht-und-spre` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 22; bündelt 5 frühere Spezialskills (verkehrsstrafrecht-strafbefehl, vermoegensarrest-einziehung, vermoegensarrest-einziehung-schnellcheck, vollstreckung-und-gnadenschni... |
| `kompendium-23-wirtschaftsstrafsach-bis-zeugenvernehmung-zeu` | staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (wirtschaftsstrafsachen-sachleitung, wohnungsdurchsuchung-gefahr-im-verzug, zeugenmanagement-und-ladungsrisiken, zeugenvernehmung-zeu... |
| `owi-kaltstart-bussgeldverfahren-sta-rolle` | OWiG-Kaltstart: Strafsache oder Ordnungswidrigkeit, Verwaltungsbehörde, Staatsanwaltschaft, Gericht und richtige Verfahrenssprache trennen: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldb... |
| `red-team-qualitygate` | Red-Team-Qualitygate: Praxis-Skill für neue Staatsanwälte zu prüft Ergebnis auf Fristenfehler, Zuständigkeitsfehler, Scheinpräzision und Ton; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und näch... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
