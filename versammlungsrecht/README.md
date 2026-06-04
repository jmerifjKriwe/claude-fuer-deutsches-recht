# Versammlungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`versammlungsrecht`) | [`versammlungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versammlungsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Verfassungsbeschwerde Klimacamp Initiative Saarbruecken — Art. 8 GG / Versammlungsfreiheit / Bannmeile Landtag** (`verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg`) | [Gesamt-PDF lesen](../testakten/verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg/gesamt-pdf/verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg_gesamt.pdf) | [`testakte-verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verfassungsbeschwerde-versammlungsfreiheit-klimacamp-saarbruecken-art-8-gg-tannenberg.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Praxisplugin für Menschen, Organisationen und anwaltliche Teams, die eine Versammlung unter freiem Himmel, einen Aufzug, eine Mahnwache, ein Camp oder eine konfliktträchtige Kundgebung rechtlich sauber anzeigen, durchführen oder gegen Behördeneingriffe verteidigen wollen.

Das Plugin denkt Versammlungsrecht nicht als Bittgang zur Behörde. Es startet bei Art. 8 GG: friedlich, ohne Waffen, grundsätzlich ohne Erlaubnis. Zugleich nimmt es ernst, dass Versammlungen im öffentlichen Raum geplant werden müssen: richtige Behörde, richtige Frist, klare Leitung, Ordner, Route, Technik, Rettungswege, Kooperationsgespräch, Auflagenprüfung und Eilrechtsschutz, wenn die Behörde ausweicht oder überzieht.

## Kaltstart

1. **Wo?** Bundesland, Stadt, Route, Platz, Bannmeile, mehrere Behördenbezirke?
2. **Was?** Außenversammlung, Aufzug, Innenversammlung, private Runde, Mahnwache, Infostand, Camp, Gegenversammlung?
3. **Wann?** Termin, Bekanntgabezeitpunkt, Einladung, Social-Media-Post, Eil- oder Spontanversammlung?
4. **Wer?** Veranstalter, Leitung, Stellvertretung, Ordner, Organisation, Kontaktkanal?
5. **Wofür?** Anzeige erstellen, Behördenfragen beantworten, Auflagen prüfen, Verbot abwehren, Eilrechtsschutz, Tag-der-Versammlung-Plan?

## Leitgedanke

- **Anzeige statt Genehmigung:** Öffentliche Versammlungen unter freiem Himmel werden angezeigt; die Behörde soll planen und schützen, nicht politisch vorsortieren.
- **Landesrecht zuerst:** Viele Länder haben eigene Versammlungsgesetze. Das Plugin fragt deshalb immer nach Ort und Bundesland.
- **Kooperation ohne Selbstzensur:** Behördenbelange werden ernst genommen, aber Ort, Zeit, Thema und Ausdrucksform bleiben Teil der grundrechtlich geschützten Versammlung.
- **Konkrete Gefahr statt Behördenbauchgefühl:** Auflagen und Verbote müssen tatsachenbasiert und verhältnismäßig sein.
- **Schnelle Outputs:** Anzeige, Ordnerliste, Kooperationsagenda, Behördenbrief, Eilantrag, Notfallkarte und Nachbereitungsvermerk.

## Typische Outputs

| Situation | Passende Skills | Ergebnis |
| --- | --- | --- |
| Versammlung normal planen | `allgemein`, `landesrecht-und-behoerde-finden`, `anzeige-unter-freiem-himmel`, `muster-anzeige-generator` | Anzeige, Fristplan, Behördenkontakt |
| Einladung soll heute raus | `frist-48-stunden-bekanntgabe`, `bekanntgabe-social-media`, `qualitaetsgate-vor-bekanntgabe` | Kommunikationskalender und Go/No-Go |
| Spontane oder eilige Demo | `spontanversammlung`, `eilversammlung`, `behoerdenkommunikation` | Kurzmeldung, Aktenvermerk, Polizeisprechzettel |
| Behörde will verlegen oder verbieten | `auflagen-pruefen`, `falscher-tag-falscher-ort-einwand`, `verbot-und-beschraenkung-abwehren`, `muster-eilantrag` | Gegenbrief und Eilrechtsschutz-Gerüst |
| Ordner und Tag selbst | `ordner-auswahl`, `ordnerliste-und-mitteilung`, `polizei-vor-ort-deeskalation`, `notfallkarte-versammlungstag` | Briefing, Liste, Notfallkarte |
| Camp, Technik, Verkehr | `camp-dauerversammlung`, `technik-lautsprecher-musik`, `verkehr-rettungswege-oepnv` | Konzept und mildere Mittel |

## Quellenstrategie

- **Bundesrecht:** Art. 8 GG, Versammlungsgesetz, VwGO.
- **Landesrecht:** jeweiliges Landesversammlungsgesetz und Zuständigkeitsregel.
- **Behördenpraxis:** offizielle Onlineformulare und Hinweise der konkreten Versammlungsbehörde.
- **Rechtsprechung:** nur mit Gericht, Datum, Aktenzeichen und frei überprüfbarem Link.
- **Keine Blindzitate:** keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen.

## Berufs- und Datenschutzhinweis

Bei echten Mandaten keine sensiblen personenbezogenen Daten, politischen Mitgliedschaften, Teilnehmerlisten oder Behördenakten in ungeprüfte Systeme laden. Ordnerlisten, Minderjährigendaten, Gesundheitsdaten und Polizeikommunikation sind datensensibel. Für produktiven Kanzleieinsatz ist das jeweils eigene Datenschutz-, Berufsrechts- und Hosting-Setup maßgeblich.

## Lizenz

Apache-2.0 OR MIT. Siehe Repository-Stammverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Allgemeiner Kaltstart im Versammlungsrecht: Land und Ort, Art der Versammlung, Frist, Behörde, Risiko und Ziel klären, dann passende Spezialskills und nächsten Output auswählen. |
| `gefahrenprognose-redteam` | Zerlegt die behördliche Gefahrenprognose und baut eine eigene, realistische Sicherheitslage auf. |
| `kompendium-01-frist-48-stunden-bek-bis-kosten-haftung-und-v` | versammlungsrecht: Konsolidiertes Skill-Kompendium 01; bündelt 2 frühere Spezialskills (frist-48-stunden-bekanntgabe, kosten-haftung-und-versicherung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-02-anwaltlicher-brief-a-bis-anzeige-unter-freiem` | versammlungsrecht: Konsolidiertes Skill-Kompendium 02; bündelt 2 frühere Spezialskills (anwaltlicher-brief-an-behoerde, anzeige-unter-freiem-himmel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-03-auflagen-pruefen-bis-auflagenverstoss-und` | versammlungsrecht: Konsolidiertes Skill-Kompendium 03; bündelt 2 frühere Spezialskills (auflagen-pruefen, auflagenverstoss-und-owi) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-04-bannmeile-schutzbere-bis-barrierefreiheit-und` | versammlungsrecht: Konsolidiertes Skill-Kompendium 04; bündelt 2 frühere Spezialskills (bannmeile-schutzbereiche, barrierefreiheit-und-inklusion) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-05-behoerdenkommunikati-bis-bekanntgabe-social-m` | versammlungsrecht: Konsolidiertes Skill-Kompendium 05; bündelt 2 frühere Spezialskills (behoerdenkommunikation, bekanntgabe-social-media) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-06-bescheid-lesen-bis-beweissicherung-am-v` | versammlungsrecht: Konsolidiertes Skill-Kompendium 06; bündelt 2 frühere Spezialskills (bescheid-lesen, beweissicherung-am-versammlungstag) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-07-blockade-sitzblockad-bis-bundeslaender-synops` | versammlungsrecht: Konsolidiertes Skill-Kompendium 07; bündelt 2 frühere Spezialskills (blockade-sitzblockade-friedlichkeit, bundeslaender-synopse) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-08-camp-dauerversammlun-bis-datenschutz-fotos-li` | versammlungsrecht: Konsolidiertes Skill-Kompendium 08; bündelt 2 frühere Spezialskills (camp-dauerversammlung, datenschutz-fotos-livestream) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-09-dritte-anwohner-laer-bis-eilversammlung` | versammlungsrecht: Konsolidiertes Skill-Kompendium 09; bündelt 2 frühere Spezialskills (dritte-anwohner-laerm-geschaeft, eilversammlung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-10-eingangsbestaetigung-bis-falscher-tag-falsche` | versammlungsrecht: Konsolidiertes Skill-Kompendium 10; bündelt 2 frühere Spezialskills (eingangsbestaetigung-und-aktenzeichen, falscher-tag-falscher-ort-einwand) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-11-gegenveranstaltung-u-bis-infostand-mahnwache` | versammlungsrecht: Konsolidiertes Skill-Kompendium 11; bündelt 2 frühere Spezialskills (gegenveranstaltung-und-trennung, infostand-mahnwache-kleinstversammlung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-12-innenraum-versammlun-bis-kooperationsgespraec` | versammlungsrecht: Konsolidiertes Skill-Kompendium 12; bündelt 2 frühere Spezialskills (innenraum-versammlung-abgrenzen, kooperationsgespraech) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-13-kundgebung-stationae-bis-landesrecht-und-beho` | versammlungsrecht: Konsolidiertes Skill-Kompendium 13; bündelt 2 frühere Spezialskills (kundgebung-stationaer-platzwahl, landesrecht-und-behoerde-finden) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-14-leiter-verantwortung-bis-mildere-mittel-matri` | versammlungsrecht: Konsolidiertes Skill-Kompendium 14; bündelt 2 frühere Spezialskills (leiter-verantwortung, mildere-mittel-matrix) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-15-muster-anzeige-gener-bis-muster-eilantrag` | versammlungsrecht: Konsolidiertes Skill-Kompendium 15; bündelt 2 frühere Spezialskills (muster-anzeige-generator, muster-eilantrag) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-16-nachbereitung-und-ak-bis-notfallkarte-versamm` | versammlungsrecht: Konsolidiertes Skill-Kompendium 16; bündelt 2 frühere Spezialskills (nachbereitung-und-aktenvermerk, notfallkarte-versammlungstag) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-17-offizielle-quellen-l-bis-ordner-auswahl` | versammlungsrecht: Konsolidiertes Skill-Kompendium 17; bündelt 2 frühere Spezialskills (offizielle-quellen-livecheck, ordner-auswahl) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-18-ordnerliste-und-mitt-bis-partei-gewerkschaft` | versammlungsrecht: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (ordnerliste-und-mitteilung, partei-gewerkschaft-verein-veranstalter) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-19-polizei-vor-ort-dees-bis-polizeifilmerei-bewe` | versammlungsrecht: Konsolidiertes Skill-Kompendium 19; bündelt 2 frühere Spezialskills (polizei-vor-ort-deeskalation, polizeifilmerei-beweissicherung-kug-201-stgb) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-20-presse-und-oeffentli-bis-privat-oeffentlich-a` | versammlungsrecht: Konsolidiertes Skill-Kompendium 20; bündelt 2 frühere Spezialskills (presse-und-oeffentlichkeitsarbeit, privat-oeffentlich-abgrenzen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-21-qualitaetsgate-vor-b-bis-route-aufzug-und-str` | versammlungsrecht: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (qualitaetsgate-vor-bekanntgabe, route-aufzug-und-streckenplanung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-22-schule-universitaet-bis-schutz-vor-vorauseil` | versammlungsrecht: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (schule-universitaet-jugendliche, schutz-vor-vorauseilendem-gehorsam) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-23-spontanversammlung-bis-strafrecht-versg-ris` | versammlungsrecht: Konsolidiertes Skill-Kompendium 23; bündelt 2 frühere Spezialskills (spontanversammlung, strafrecht-versg-risiken) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-24-technik-lautsprecher-bis-untatigkeit-und-schw` | versammlungsrecht: Konsolidiertes Skill-Kompendium 24; bündelt 2 frühere Spezialskills (technik-lautsprecher-musik, untatigkeit-und-schweigen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-25-verbot-und-beschraen-bis-verkehr-rettungswege` | versammlungsrecht: Konsolidiertes Skill-Kompendium 25; bündelt 2 frühere Spezialskills (verbot-und-beschraenkung-abwehren, verkehr-rettungswege-oepnv) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-26-versammlungskonzept-bis-wahlkampf-und-politi` | versammlungsrecht: Konsolidiertes Skill-Kompendium 26; bündelt 2 frühere Spezialskills (versammlungskonzept, wahlkampf-und-politische-kundgebung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-27-widerspruch-klage-ei-bis-widerspruch-klage-ei` | versammlungsrecht: Konsolidiertes Skill-Kompendium 27; bündelt 1 frühere Spezialskills (widerspruch-klage-eilrechtsschutz) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
