# Kriegsdienstverweigerung und Wehrdienst

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kriegsdienstverweigerung-wehrdienst`) | [`kriegsdienstverweigerung-wehrdienst.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kriegsdienstverweigerung-wehrdienst.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **KDV-Verfahren Malte Eberhard Rabenow / Berlin-Köln 2026** (`kriegsdienstverweigerung-gewissensantrag-berlin-2026`) | [Gesamt-PDF lesen](../testakten/kriegsdienstverweigerung-gewissensantrag-berlin-2026/gesamt-pdf/kriegsdienstverweigerung-gewissensantrag-berlin-2026_gesamt.pdf) | [`testakte-kriegsdienstverweigerung-gewissensantrag-berlin-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kriegsdienstverweigerung-gewissensantrag-berlin-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Praxisplugin für Kriegsdienstverweigerung aus Gewissensgründen nach Art. 4 Abs. 3 GG und KDVG. Es ist ausdrücklich kein Plugin für Totalverweigerung, Dienstflucht, Befehlsboykott oder politische Leistungsverweigerung. Es behandelt die verfassungsrechtlich loyale Inanspruchnahme eines Grundrechts: Wer nicht gegen sein Gewissen Kriegsdienst mit der Waffe leisten kann, stellt sich nicht außerhalb der Ordnung, sondern beruft sich auf eine ihrer zentralen Gewissensgarantien.

Das Plugin führt von der ersten inneren Klärung über den Antrag beim Bundesamt für das Personalmanagement der Bundeswehr bis zur BAFzA-Entscheidung, Anhörung, Nachreichung, Anerkennung, Ablehnung, Widerspruch, Untätigkeitsklage und Eilrechtsschutz. Es berücksichtigt den Stand 2026 nach dem Wehrdienstmodernisierungsgesetz, insbesondere § 13 KDVG n. F. für ungediente Wehrpflichtige, die vor dem 01.01.2010 geboren wurden.

## Kaltstart

1. **Status klären:** ungedient, wehrpflichtig, vor/nach 01.01.2010 geboren, gemustert, einberufen, Reservist, FWDL, Soldat auf Zeit, Berufssoldat, Soldatin, frühere Soldatin/früherer Soldat?
2. **Ziel klären:** Antrag stellen, Begründung ordnen, Unterlagen vervollständigen, Sachstand erzwingen, Anhörung vorbereiten, Ablehnung angreifen, laufenden Dienstkonflikt entschärfen?
3. **Gewissen klären:** Geht es wirklich um Kriegsdienst mit der Waffe als solcher oder nur um einen bestimmten Krieg, eine politische Lage, Angst, Karriere, Gesundheit oder Totalverweigerung?
4. **Verfahren klären:** Antrag läuft über BAPersBw; BAFzA entscheidet inhaltlich nach Zuleitung. Direkte Übersendung an das BAFzA ist nicht der gesetzliche Standardweg.
5. **Rechtsschutz klären:** Sachstand, Nachreichung, Widerspruch, § 75 VwGO, § 80 VwGO oder § 123 VwGO nur nach Lage und Frist.

## Leitgedanke

Das Plugin soll nicht fertige Gewissensformeln produzieren. Es hilft, eine echte persönliche Entscheidung so zu strukturieren, dass sie rechtlich verständlich wird: Lebensweg, innere Entwicklung, Auslöser, Stabilität, Konsequenzen, Abgrenzung zu bloßer Politik und Plausibilität. Allgemeine Mustersätze sind gefährlich; eine persönliche, wahrhaftige und prüffähige Darstellung ist stärker.

## Typische Outputs

| Situation | Skills | Ergebnis |
| --- | --- | --- |
| Erster Antrag | `allgemein`, `status-routing`, `antrag-bapersbw-form`, `gewissensbegruendung-werkstatt` | Antragspaket mit Lebenslauf- und Begründungsplan |
| Antrag liegt, nichts passiert | `eingang-und-pk-nachweis`, `sachstandsanfrage-und-frist`, `untaetigkeitsklage-vwgo-75` | Sachstandsschreiben, Fristenmatrix, Eskalationsplan |
| Soldat oder Soldatin im Dienst | `aktive-soldaten-prioritaet`, `entlassung-berufssoldat-sg-46`, `entlassung-saz-sg-55`, `dienstpflichten-waehrend-verfahren` | Statusstrategie ohne unnötiges Disziplinarrisiko |
| Anhörung oder Zweifel | `schriftliche-anhoerung-kdvg-6`, `muendliche-anhoerung-vorbereitung`, `zweifel-ausraeumen-gesamtvorbringen` | Antwortentwurf, Anhörungsleitfaden, Belegliste |
| Ablehnung | `ablehnungsbescheid-analyse`, `widerspruch-kdvg-9`, `verwaltungsgericht-kdvg-10` | Rechtsbehelfsplan und Klagegerüst |
| 2026-Sonderfall | `wdmodg-2026-uebergang`, `kdvg-13-neun-monate`, `ungedient-vor-2010` | Prüfung der neuen Sonderregeln |

## Keine Totalverweigerung

Dieses Plugin erklärt bei Bedarf die Abgrenzung, unterstützt aber nicht beim bewussten Bruch mit allen Dienst- und Ersatzdienstpflichten. Der Fokus liegt auf der rechtmäßigen, offenen und dokumentierten Berufung auf das Gewissen gegen den Kriegsdienst mit der Waffe.

## Quellenstrategie

- **Amtlich zuerst:** GG, KDVG, WPflG, SG, VwGO, BAFzA-Hinweise, BAPersBw/Bundeswehr-Hinweise.
- **Rechtsprechung verifiziert:** BVerwG und BVerfG nur mit Datum, Aktenzeichen und freiem Link.
- **Aktualität 2026:** Vor Ausgabe immer prüfen, ob Wehrdienstmodernisierung, Bedarfswehrpflicht oder Verwaltungspraxis geändert wurden.
- **Keine Blindzitate:** keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## Datenschutz und Sicherheit

Gewissensbegründungen, Gesundheitsdaten, Personalakten, Musterungsunterlagen und Soldatenakten sind hochsensibel. In produktiven Verfahren nur in einem dafür freigegebenen, datenschutz- und berufsrechtskonformen System arbeiten.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Kaltstart für Kriegsdienstverweigerung aus Gewissensgründen: Status, Verfahrenslage, Gewissenskern, Antragspfad, Fristen, Rechtsschutz und passende Spezialskills auswählen. |
| `kompendium-01-rechtsprechung-livec-bis-sachstandsanfrage-un` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 01; bündelt 5 frühere Spezialskills (rechtsprechung-livecheck, dienstpflichten-waehrend-verfahren, frist-bei-nachforderung-ein-monat, fristenkalender-kdv, sachstandsanf... |
| `kompendium-02-widerspruch-fristen-bis-akte-fuer-gericht-au` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 02; bündelt 5 frühere Spezialskills (widerspruch-fristen-sonderlagen, ablehnungsbescheid-analyse, ablehnungsgruende-kdvg-7, adressat-und-versandwege, akte-fuer-gericht-... |
| `kompendium-03-akteneinsicht-kdv-bis-anerkennung-und-dien` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 03; bündelt 5 frühere Spezialskills (akteneinsicht-kdv, aktenvernichtung-kdvg-12, aktive-soldaten-prioritaet, aktuelle-lage-2026, anerkennung-und-dienstfolgen) und bewa... |
| `kompendium-04-anerkennung-vorausse-bis-anlagenverzeichnis-k` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 04; bündelt 5 frühere Spezialskills (anerkennung-voraussetzungen-kdvg-5, anerkennungsbescheid-gueltigkeit, angst-karriere-gesundheit-abgrenzen, anhoerungsprotokoll-und-... |
| `kompendium-05-anschreiben-kurz-und-bis-anwaltlicher-brief-b` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 05; bündelt 5 frühere Spezialskills (anschreiben-kurz-und-wuerdig, antrag-bapersbw-form, antrag-zur-niederschrift, anwaltlicher-brief-bafza, anwaltlicher-brief-bapersbw... |
| `kompendium-06-arbeitgeber-und-fehl-bis-auslaendischer-wehrd` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 06; bündelt 5 frühere Spezialskills (arbeitgeber-und-fehlzeit, argumente-die-nicht-tragen, aufschiebende-wirkung-kdvg-3, ausbildungskosten-rueckforderung, auslaendische... |
| `kompendium-07-ausland-aufenthalt-w-bis-begruendung-fuer-akt` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 07; bündelt 5 frühere Spezialskills (ausland-aufenthalt-wehrpflicht, bafza-entscheidungspfad, bedarfswehrpflicht-wpflg-2a, befehl-und-gewissenskonflikt, begruendung-fue... |
| `kompendium-08-begruendung-fuer-ehe-bis-beistand-kirchen-ber` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 08; bündelt 5 frühere Spezialskills (begruendung-fuer-ehemalige-anerkannte, begruendung-fuer-reservisten, begruendung-fuer-ungediente, begruendung-redaktion-ohne-schabl... |
| `kompendium-09-berufliche-folgen-zi-bis-bverwg-2005-pfaff-be` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 09; bündelt 5 frühere Spezialskills (berufliche-folgen-zivil, berufssoldaten-kdv, bescheid-archivieren, beweislast-und-ueberzeugungsbildung, bverwg-2005-pfaff-befehl) u... |
| `kompendium-10-bverwg-2012-sanitaet-bis-checkliste-vor-antra` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 10; bündelt 5 frühere Spezialskills (bverwg-2012-sanitaetsdienst, bverwg-2018-innere-umkehr, bverwg-2021-parteivernehmung, checkliste-nach-antrag, checkliste-vor-antrag... |
| `kompendium-11-datenschutz-gewissen-bis-doppelte-staatsangeh` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 11; bündelt 5 frühere Spezialskills (datenschutz-gewissensakte, dienststelle-kommunikation, disziplinarrisiken-soldaten, disziplinarvorgesetzter-stellungnahme, doppelte... |
| `kompendium-12-eidesstattliche-vers-bis-einstweilige-anordnu` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 12; bündelt 5 frühere Spezialskills (eidesstattliche-versicherung, eilrechtsschutz-drohende-einberufung, einberufung-nach-antrag, eingang-und-pk-nachweis, einstweilige-... |
| `kompendium-13-europa-menschenrecht-bis-fruehere-soldaten-un` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 13; bündelt 5 frühere Spezialskills (europa-menschenrechte-kdv, familie-partnerschaft-gesellschaftsdruck, fehlende-rechtsschutzbelehrung, formularmythen-social-media, f... |
| `kompendium-14-frueherer-abgelehnte-bis-gewissensbegruendung` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 14; bündelt 5 frühere Spezialskills (frueherer-abgelehnter-antrag, fuehrungszeugnis-zweifel, fwdl-probezeit-und-kdv, gesetzliche-vertreter-rechtsbehelfe, gewissensbegru... |
| `kompendium-15-gewissensentscheidun-bis-innere-umkehr-gedien` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 15; bündelt 5 frühere Spezialskills (gewissensentscheidung-massstab, glossar-kdv, grundrecht-art-4-abs-3, humanistische-pazifistische-gruende, innere-umkehr-gediente) u... |
| `kompendium-16-karrierecenter-und-b-bis-klage-ohne-berufung` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 16; bündelt 5 frühere Spezialskills (karrierecenter-und-bapersbw, kdvg-13-neun-monate, kein-totalverweigerungs-tool, ki-nutzung-gewissensbegruendung, klage-ohne-berufun... |
| `kompendium-17-kommunikation-mit-fa-bis-mehrsprachige-orient` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 17; bündelt 5 frühere Spezialskills (kommunikation-mit-familie, kosten-und-auslagen-anhoerung, lebensfuehrung-und-plausibilitaet, lebenslauf-luecken-und-widersprueche,... |
| `kompendium-18-minderjaehrige-antra-bis-musterungsbescheid-b` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 18; bündelt 5 frühere Spezialskills (minderjaehrige-antragstellung, muendliche-anhoerung-vorbereitung, musterung-verweigert-ablehnung, musterungen-und-eignung, musterun... |
| `kompendium-19-notfallplan-vor-dien-bis-politische-motive-ab` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 19; bündelt 5 frühere Spezialskills (notfallplan-vor-dienstantritt, parteivernehmung-vorbereiten, personalakte-und-datenschutz-soldaten, personenkennziffer-und-grundakt... |
| `kompendium-20-presseanfragen-und-k-bis-rechtsanwaltliche-vo` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 20; bündelt 5 frühere Spezialskills (presseanfragen-und-kdv, psychische-belastung-und-beratung, qualitaetsgate-vor-ausgabe, recht-auf-entscheidung-mein-gewissen-schlaef... |
| `kompendium-21-rechtsschutzbeduerfn-bis-sanitaetsdienst-und` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 21; bündelt 5 frühere Spezialskills (rechtsschutzbeduerfnis-pruefen, religioese-weltanschauliche-gruende, reservisten-heranziehung, ruecknahme-oder-verzicht, sanitaetsd... |
| `kompendium-22-schluesselerlebnis-o-bis-sofortvollzug-und-an` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 22; bündelt 5 frühere Spezialskills (schluesselerlebnis-oder-wandel, schriftliche-anhoerung-kdvg-6, sicherheitsueberpruefung-und-extremismus, social-media-und-oeffentli... |
| `kompendium-23-soldat-auf-zeit-kdv-bis-sprachlich-einfache` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 23; bündelt 5 frühere Spezialskills (soldat-auf-zeit-kdv, soldatinnen-und-kdv, spannungs-verteidigungsfall, sprache-der-loyalitaet, sprachlich-einfache-erklaerung) und... |
| `kompendium-24-status-routing-bis-untaetigkeitsklage-v` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 24; bündelt 5 frühere Spezialskills (status-routing, stellungnahmen-dritter, ungedient-ab-2010, ungedient-vor-2010, untaetigkeitsklage-vwgo-75) und bewahrt deren Workfl... |
| `kompendium-25-unterlagenmappe-kdv-bis-vollstaendigkeit-kdv` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 25; bündelt 5 frühere Spezialskills (unterlagenmappe-kdv, verwaltungsakt-oder-informelles-schreiben, verwaltungsgericht-kdvg-10, vollstaendiger-lebenslauf, vollstaendig... |
| `kompendium-26-waffenbesitz-jagd-sc-bis-zeugenauswahl-und-au` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 26; bündelt 5 frühere Spezialskills (waffenbesitz-jagd-schuetzenverein, wahrheitspflicht-und-authentizitaet, wehrpflicht-ruht-ausland, widerspruch-kdvg-9, zeugenauswahl... |
| `kompendium-27-zivildienst-altfaell-bis-zweitbescheid-besche` | kriegsdienstverweigerung-wehrdienst: Konsolidiertes Skill-Kompendium 27; bündelt 4 frühere Spezialskills (zivildienst-altfaelle, ziviler-ersatzdienst-art-12a, zweifel-ausraeumen-gesamtvorbringen, zweitbescheid-bescheinigung) und bewahrt... |
| `nachreichung-fehlender-unterlagen` | Formuliert fristwahrende Nachreichungen nach behördlicher Aufforderung. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
