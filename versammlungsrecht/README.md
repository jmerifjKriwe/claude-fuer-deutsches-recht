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
| Versammlung normal planen | `versammlungsrecht-allgemein`, `landesrecht-und-behoerde-finden`, `anzeige-unter-freiem-himmel`, `muster-anzeige-generator` | Anzeige, Fristplan, Behördenkontakt |
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
| `anwaltlicher-an-anzeige-unter` | Anwaltlicher AN Anzeige Unter: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `auflagen-auflagenverstoss-owi` | Auflagen Auflagenverstoss OWI: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bannmeile-schutzbereiche-barrierefreiheit` | Bannmeile Schutzbereiche Barrierefreiheit: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `behoerdenkommunikation-bekanntgabe-social` | Behoerdenkommunikation Bekanntgabe Social: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bescheid-lesen-beweissicherung-am` | Bescheid Lesen Beweissicherung AM: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `blockade-sitzblockade-bundeslaender-synopse` | Blockade Sitzblockade Bundeslaender Synopse: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `camp-dauerversammlung-datenschutz-fotos` | Camp Dauerversammlung Datenschutz Fotos: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `dritte-anwohner-eilversammlung` | Dritte Anwohner Eilversammlung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `eingangsbestaetigung-aktenzeichen-falscher` | Eingangsbestaetigung Aktenzeichen Falscher: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `frist-stunden-kosten-haftung` | Frist Stunden Kosten Haftung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `gefahrenprognose-redteam` | Zerlegt die behördliche Gefahrenprognose und baut eine eigene, realistische Sicherheitslage auf. |
| `gegenveranstaltung-trennung-infostand` | Gegenveranstaltung Trennung Infostand: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `innenraum-versammlung-kooperationsgespraech` | Innenraum Versammlung Kooperationsgespraech: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kundgebung-stationaer-landesrecht-behoerde` | Kundgebung Stationaer Landesrecht Behoerde: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `leiter-verantwortung-mildere-mittel` | Leiter Verantwortung Mildere Mittel: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `muster-anzeige-eilantrag` | Muster Anzeige Eilantrag: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `nachbereitung-aktenvermerk-notfallkarte` | Nachbereitung Aktenvermerk Notfallkarte: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `offizielle-quellen-ordner-auswahl` | Offizielle Quellen Ordner Auswahl: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ordnerliste-mitteilung-partei-gewerkschaft` | Ordnerliste Mitteilung Partei Gewerkschaft: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `polizei-ort-polizeifilmerei-beweissicherung` | Polizei ORT Polizeifilmerei Beweissicherung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `presse-oeffentlichkeitsarbeit-privat` | Presse Oeffentlichkeitsarbeit Privat: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `qualitaetsgate-bekanntgabe-route-aufzug` | Qualitaetsgate Bekanntgabe Route Aufzug: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `schule-universitaet-schutz-vorauseilendem` | Schule Universitaet Schutz Vorauseilendem: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `spontanversammlung-strafrecht-versg` | Spontanversammlung Strafrecht Versg: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `technik-lautsprecher-untatigkeit-schweigen` | Technik Lautsprecher Untatigkeit Schweigen: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verbot-beschraenkung-verkehr-rettungswege` | Verbot Beschraenkung Verkehr Rettungswege: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `versammlungskonzept-wahlkampf-politische` | Versammlungskonzept Wahlkampf Politische: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `versammlungsrecht-kaltstart-triage` | Allgemeiner Kaltstart im Versammlungsrecht: Land und Ort, Art der Versammlung, Frist, Behörde, Risiko und Ziel klären, dann passende Fachmodule und nächsten Output auswählen. |
| `widerspruch-klage` | Widerspruch Klage: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
