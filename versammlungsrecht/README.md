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
| `anwaltlicher-an-anzeige-unter` | Anwaltlicher AN Anzeige Unter im Versammlungsrecht: prüft konkret Entwirft einen anwaltlichen oder sehr sachlichen Laienbrief, Führt durch die Anzeige einer öffentlichen Versammlung. Liefert priorisierten Output mit Norm-Pinpoints, Risik... |
| `auflagen-auflagenverstoss-owi` | Auflagen Auflagenverstoss OWI im Versammlungsrecht: prüft konkret Prüft Beschränkungen, Auflagen und Nebenbestimmungen auf Rechtsgrundlage, Tatsac, Prüft Ordnungswidrigkeiten- und Strafrisiken bei nicht. Liefert priorisierten Output mit... |
| `bannmeile-schutzbereiche-barrierefreiheit` | Bannmeile Schutzbereiche Barrierefreiheit im Versammlungsrecht: prüft konkret Prüft befriedete Bezirke, Bannmeilen und Schutzbereiche um Bundestag, Bundesrat, Plant barrierearme Versammlungen. Liefert priorisierten Output mit Norm-Pinpoi... |
| `behoerdenkommunikation-bekanntgabe-social` | Behoerdenkommunikation Bekanntgabe Social im Versammlungsrecht: prüft konkret Formuliert kluge Mails und Telefonnotizen an, Polizei, Ordnu, Prüft. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `bescheid-lesen-beweissicherung-am` | Bescheid Lesen Beweissicherung AM im Versammlungsrecht: prüft konkret Analysiert versammlungsrechtliche Bescheide, Auflagenkataloge, Verbote, Telefonn. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `blockade-sitzblockade-bundeslaender-synopse` | Blockade Sitzblockade Bundeslaender Synopse im Versammlungsrecht: prüft konkret Prüft Blockaden, Sitzblockaden, Zufahrtsnähe und Friedlichkeitsgrenzen, Erstellt eine Arbeits-Synopse der Landesversammlungsgesetze. Liefert priorisierten Ou... |
| `camp-dauerversammlung-datenschutz-fotos` | Camp Dauerversammlung Datenschutz Fotos im Versammlungsrecht: prüft konkret Prüft Camps, Mahnwachen, Zelte, Schlafen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `dritte-anwohner-eilversammlung` | Dritte Anwohner Eilversammlung im Versammlungsrecht: prüft konkret Bearbeitet Konflikte mit Anwohnern, Geschäften, Schulen, Kirchen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `eingangsbestaetigung-aktenzeichen-falscher` | Eingangsbestaetigung Aktenzeichen Falscher im Versammlungsrecht: prüft konkret Sichert Nachweis von Anzeige, Eingang, Aktenzeichen und behördlicher Zuständigke, Reagiert auf Behördeneinwände wie falscher Tag. Liefert priorisierten Output... |
| `frist-stunden-kosten-haftung` | Frist Stunden Kosten Haftung im Versammlungsrecht: prüft konkret Berechnet die versammlungsrechtliche 48-Stunden-Frist bis, Prüft Kosten, Gebühren, Schäden. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `gefahrenprognose-redteam` | Zerlegt die behördliche Gefahrenprognose und baut eine eigene, realistische Sicherheitslage auf. |
| `gegenveranstaltung-trennung-infostand` | Gegenveranstaltung Trennung Infostand im Versammlungsrecht: prüft konkret Plant konkurrierende Versammlungen, Gegenprotest, Pufferzonen und gleichzeitige, Prüft Kleinstkundgebung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoam... |
| `innenraum-versammlung-kooperationsgespraech` | Innenraum Versammlung Kooperationsgespraech im Versammlungsrecht: prüft konkret Grenzt öffentliche und private Versammlungen in, Bereitet Kooperationsgespräche mit Versammlungsbehörde und. Liefert priorisierten Output mit Norm-Pinpoints,... |
| `kundgebung-stationaer-landesrecht-behoerde` | Kundgebung Stationaer Landesrecht Behoerde im Versammlungsrecht: prüft konkret Prüft stationäre Kundgebungen, Mahnwachen, Infostände mit Meinungskern und symbo, Findet das anwendbare Landesversammlungsgesetz und die. Liefert priorisierte... |
| `leiter-verantwortung-mildere-mittel` | Leiter Verantwortung Mildere Mittel im Versammlungsrecht: prüft konkret Erklärt Rolle, Rechte und Pflichten der Versammlungsleitung vor, während und nac, Erstellt eine Matrix milderer Mittel gegen Verbot. Liefert priorisierten Output mit... |
| `muster-anzeige-eilantrag` | Muster Anzeige Eilantrag im Versammlungsrecht: prüft konkret Erstellt eine präzise Anzeige für Kundgebung, Mahnwache, Demonstrationszug, Fahr. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `nachbereitung-aktenvermerk-notfallkarte` | Nachbereitung Aktenvermerk Notfallkarte im Versammlungsrecht: prüft konkret Erstellt Nachbereitung nach Durchführung, Auflagenproblemen, Polizeikontakt, Pre. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `offizielle-quellen-ordner-auswahl` | Offizielle Quellen Ordner Auswahl im Versammlungsrecht: prüft konkret Erzwingt Live-Check von Gesetz, Behörde, Formular, Rechtsprechung und Landesrech. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `ordnerliste-mitteilung-partei-gewerkschaft` | Ordnerliste Mitteilung Partei Gewerkschaft im Versammlungsrecht: prüft konkret Erstellt datensparsame Ordnerliste oder, Hilft Parteien, Gewerkschaften, Vereinen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem S... |
| `polizei-ort-polizeifilmerei-beweissicherung` | Polizei ORT Polizeifilmerei Beweissicherung im Versammlungsrecht: prüft konkret Gibt Leitfaden für Kommunikation mit Einsatzleitung, Störer, Auflösung, Durchsuc. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem S... |
| `presse-oeffentlichkeitsarbeit-privat` | Presse Oeffentlichkeitsarbeit Privat im Versammlungsrecht: prüft konkret Hilft bei Pressemitteilungen, Einladungstexten, Veranstalterangabe und Kommunika, Prüft. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem S... |
| `qualitaetsgate-bekanntgabe-route-aufzug` | Qualitaetsgate Bekanntgabe Route Aufzug im Versammlungsrecht: prüft konkret Letzter Check vor öffentlicher Einladung oder Versand der, Plant Aufzüge und Routen so, dass Versammlungszweck, Verkehr. Liefert priorisierten Output mit Norm-Pi... |
| `schule-universitaet-schutz-vorauseilendem` | Schule Universitaet Schutz Vorauseilendem im Versammlungsrecht: prüft konkret Prüft Schüler-, Studierenden-, Hochschul- und Jugendversammlungen samt Aufsicht, Hilft. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächst... |
| `spontanversammlung-strafrecht-versg` | Spontanversammlung Strafrecht Versg im Versammlungsrecht: prüft konkret Prüft echte Spontanversammlungen, bei denen Anlass und Bildung so unmittelbar zu, Routet Strafbarkeitsrisiken aus VersammlG, StGB. Liefert priorisierten Output mit N... |
| `technik-lautsprecher-untatigkeit-schweigen` | Technik Lautsprecher Untatigkeit Schweigen im Versammlungsrecht: prüft konkret Prüft Lautsprecher, Megaphon, Bühne, Strom. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `verbot-beschraenkung-verkehr-rettungswege` | Verbot Beschraenkung Verkehr Rettungswege im Versammlungsrecht: prüft konkret Entwickelt Gegenstrategie gegen Verbot, faktische Verhinderung oder so einschnei, Bearbeitet Verkehr, ÖPNV. Liefert priorisierten Output mit Norm-Pinpoints, Ri... |
| `versammlungskonzept-wahlkampf-politische` | Versammlungskonzept Wahlkampf Politische im Versammlungsrecht: prüft konkret Erstellt ein belastbares Versammlungskonzept als Anlage zur, Prüft Wahlkampfstände, Kandidatenauftritte, Parteiveranstaltungen. Liefert priorisierten Output mit... |
| `versammlungsrecht-kaltstart-triage` | Allgemeiner Kaltstart im Versammlungsrecht: Land und Ort, Art der Versammlung, Frist, Behörde, Risiko und Ziel klären, dann passende Fachmodule und nächsten Output auswählen. |
| `widerspruch-klage` | Widerspruch Klage im Versammlungsrecht: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
