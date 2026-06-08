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
| **Initiative Lausitzer Lebensraum e.V. ./. Polizeipraesidium Cottbus (Polizeiverfuegung Anti-Kohle-Versammlung Forst Lausitz)** (`polizeiverfuegung-versammlung-anti-kohle-pohlmann-forst-lausitz`) | [Gesamt-PDF lesen](../testakten/polizeiverfuegung-versammlung-anti-kohle-pohlmann-forst-lausitz/gesamt-pdf/polizeiverfuegung-versammlung-anti-kohle-pohlmann-forst-lausitz_gesamt.pdf) | [`testakte-polizeiverfuegung-versammlung-anti-kohle-pohlmann-forst-lausitz.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-polizeiverfuegung-versammlung-anti-kohle-pohlmann-forst-lausitz.zip) |
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

Automatisch generierte Komplett-Liste aller 55 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anwaltlicher-an-anzeige-unter` | Entwirft einen anwaltlichen oder sehr sachlichen Laienbrief gegen problematische Behördenkommunikation im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `anzeige-unter-freiem-himmel` | Führt durch die Anzeige einer öffentlichen Versammlung unter freiem Himmel oder eines Aufzugs, ohne sie fälschlich als Genehmigungsantrag zu behandeln im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und... |
| `auflagen-auflagenverstoss-owi` | Prüft Beschränkungen, Auflagen und Nebenbestimmungen auf Rechtsgrundlage, Tatsachenbasis und Verhältnismäßigkeit im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `auflagenverstoss-und-owi` | Prüft Ordnungswidrigkeiten- und Strafrisiken bei nicht angezeigten Versammlungen, Auflagenverstößen und Auflösung im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `bannmeile-schutzbereiche-barrierefreiheit` | Prüft befriedete Bezirke, Bannmeilen und Schutzbereiche um Bundestag, Bundesrat, Landtage und besondere Orte im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `barrierefreiheit-und-inklusion` | Plant barrierearme Versammlungen: Wege, Lautsprecher, Gebärdensprache, Ruhebereiche, Assistenz und sichere Kommunikation im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `behoerdenkommunikation-bekanntgabe-social` | Formuliert kluge Mails und Telefonnotizen an Versammlungsbehörde, Polizei, Ordnungsamt und Straßenverkehrsbehörde im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `bekanntgabe-social-media` | Prüft, wann Flyer, Website, Messenger, Pressemitteilung oder Social-Media-Post die Bekanntgabe oder Einladung auslösen im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `bescheid-lesen-beweissicherung-am` | Analysiert versammlungsrechtliche Bescheide, Auflagenkataloge, Verbote, Telefonnotizen und E-Mails der Behörde im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `beweissicherung-am-versammlungstag` | Erstellt Beweissicherungsplan für Auflagen, Polizeihandeln, Störer, Wetter, Teilnehmerzahl und Ablauf im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `blockade-sitzblockade-bundeslaender-synopse` | Prüft Blockaden, Sitzblockaden, Zufahrtsnähe und Friedlichkeitsgrenzen im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `bundeslaender-synopse` | Erstellt eine Arbeits-Synopse der Landesversammlungsgesetze und markiert, was vor Ausgabe live amtlich zu prüfen ist im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `camp-dauerversammlung-datenschutz-fotos` | Prüft Camps, Mahnwachen, Zelte, Schlafen, Infrastruktur und Dauerversammlungen unter Art. 8 GG im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `datenschutz-fotos-livestream` | Prüft Fotos, Livestreams, Drohnen, Teilnehmerdaten, Ordnerlisten und Polizeiaufnahmen im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `dritte-anwohner-eilversammlung` | Bearbeitet Konflikte mit Anwohnern, Geschäften, Schulen, Kirchen, Kliniken, Botschaften oder sensiblen Orten im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `eilversammlung` | Prüft Eilversammlungen, bei denen ein Veranstalter existiert, der Zweck aber bei voller Fristeinhaltung vereitelt würde im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `eingangsbestaetigung-aktenzeichen-falscher` | Sichert Nachweis von Anzeige, Eingang, Aktenzeichen und behördlicher Zuständigkeit im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `falscher-tag-falscher-ort-einwand` | Reagiert auf Behördeneinwände wie falscher Tag, falscher Ort, sensible Nachbarschaft, parallele Veranstaltung oder politisch unpassender Anlass im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächst... |
| `frist-stunden-kosten-haftung` | Berechnet die versammlungsrechtliche 48-Stunden-Frist bis zur Bekanntgabe oder Einladung und markiert Landesabweichungen im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `gefahrenprognose-redteam` | Zerlegt die behördliche Gefahrenprognose und baut eine eigene, realistische Sicherheitslage auf. |
| `gegenveranstaltung-trennung-infostand` | Plant konkurrierende Versammlungen, Gegenprotest, Pufferzonen und gleichzeitige Grundrechtsausübung im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `infostand-mahnwache-kleinstversammlung` | Prüft Kleinstkundgebung, Mahnwache, Infostand mit politischem Meinungskern und Abgrenzung zur Sondernutzung im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `innenraum-versammlung-kooperationsgespraech` | Grenzt öffentliche und private Versammlungen in geschlossenen Räumen von anzeigepflichtigen Versammlungen unter freiem Himmel ab im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `kaltstart-triage` | Allgemeiner Kaltstart im Versammlungsrecht: Land und Ort, Art der Versammlung, Frist, Behörde, Risiko und Ziel klären, dann passende Fachmodule und nächsten Output auswählen. |
| `kooperationsgespraech` | Bereitet Kooperationsgespräche mit Versammlungsbehörde und Polizei vor und protokolliert sie im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `kosten-haftung-und-versicherung` | Prüft Kosten, Gebühren, Schäden, Haftung, Versicherung und Regress rund um Versammlungen im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `kundgebung-stationaer-landesrecht-behoerde` | Prüft stationäre Kundgebungen, Mahnwachen, Infostände mit Meinungskern und symbolische Orte im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `landesrecht-und-behoerde-finden` | Findet das anwendbare Landesversammlungsgesetz und die konkrete zuständige Versammlungsbehörde oder Polizei anhand von Ort und Route im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitss... |
| `leiter-verantwortung-mildere-mittel` | Erklärt Rolle, Rechte und Pflichten der Versammlungsleitung vor, während und nach der Versammlung im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `mildere-mittel-matrix` | Erstellt eine Matrix milderer Mittel gegen Verbot, Verlegung oder zu breite Auflagen im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `muster-anzeige-eilantrag` | Erstellt eine präzise Anzeige für Kundgebung, Mahnwache, Demonstrationszug, Fahrradaufzug oder Dauerversammlung im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `muster-eilantrag` | Erstellt ein Grundgerüst für verwaltungsgerichtlichen Eilrechtsschutz im Versammlungsrecht im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `nachbereitung-aktenvermerk-notfallkarte` | Erstellt Nachbereitung nach Durchführung, Auflagenproblemen, Polizeikontakt, Presse und möglichem Folgeverfahren im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `notfallkarte-versammlungstag` | Erstellt eine kompakte Notfallkarte für Leitung, Stellvertretung, Ordner und Dokumentationsteam im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `offizielle-quellen-ordner-auswahl` | Erzwingt Live-Check von Gesetz, Behörde, Formular, Rechtsprechung und Landesrecht vor verbindlichem Output im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `ordner-auswahl` | Hilft bei Auswahl, Anzahl, Zuverlässigkeit und Briefing von Ordnerinnen und Ordnern im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `ordnerliste-mitteilung-partei-gewerkschaft` | Erstellt datensparsame Ordnerliste oder Ordnerzahl-Mitteilung an die Behörde nach dem einschlägigen Recht im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `partei-gewerkschaft-verein-veranstalter` | Hilft Parteien, Gewerkschaften, Vereinen, Initiativen und losen Gruppen bei Veranstalterrolle und interner Verantwortlichkeit im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `polizei-ort-polizeifilmerei-beweissicherung` | Gibt Leitfaden für Kommunikation mit Einsatzleitung, Störer, Auflösung, Durchsuchung und Platzverweise am Versammlungstag im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `polizeifilmerei-beweissicherung-kug-201-stgb` | Versammlungsrecht: Polizeieinsätze, Gegenaufnahmen, Beweissicherung, KUG/KunstUrhG, § 201 StGB, § 201a StGB, Presse- und Versammlungsfreiheit, Vor-Ort-Kommunikation und Nachbereitung im Versammlungsrecht. Liefert priorisierten Output mit... |
| `presse-oeffentlichkeitsarbeit-privat` | Hilft bei Pressemitteilungen, Einladungstexten, Veranstalterangabe und Kommunikation ohne unnötige Rechtsrisiken im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `privat-oeffentlich-abgrenzen` | Prüft, ob eine Zusammenkunft öffentlich, privat, vereinsintern, parteiintern, betrieblich oder nur ein Gesprächskreis ist im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `qualitaetsgate-bekanntgabe-route-aufzug` | Letzter Check vor öffentlicher Einladung oder Versand der Anzeige im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `route-aufzug-und-streckenplanung` | Plant Aufzüge und Routen so, dass Versammlungszweck, Verkehr, Sicherheit und Behördeneinwände gut ausbalanciert sind im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `schule-universitaet-schutz-vorauseilendem` | Prüft Schüler-, Studierenden-, Hochschul- und Jugendversammlungen samt Aufsicht, Schulrecht und Hausrecht im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `schutz-vor-vorauseilendem-gehorsam` | Hilft, berechtigte Behördenbelange zu berücksichtigen, ohne die Versammlung aus Angst selbst zu entkernen im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `spontanversammlung-strafrecht-versg` | Prüft echte Spontanversammlungen, bei denen Anlass und Bildung so unmittelbar zusammenfallen, dass vorherige Anzeige nicht möglich war im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeit... |
| `strafrecht-versg-risiken` | Routet Strafbarkeitsrisiken aus VersammlG, StGB, Waffenrecht, Vermummung, Schutzwaffen und Nötigung im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `technik-lautsprecher-untatigkeit-schweigen` | Prüft Lautsprecher, Megaphon, Bühne, Strom, Fahrzeuge, Musik, Projektionen und Lärmschutz im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `untatigkeit-und-schweigen` | Reagiert, wenn Behörde auf Anzeige oder Rückfrage nicht antwortet und der Termin näher rückt im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `verbot-beschraenkung-verkehr-rettungswege` | Entwickelt Gegenstrategie gegen Verbot, faktische Verhinderung oder so einschneidende Beschränkung, dass der Zweck leerläuft im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `verkehr-rettungswege-oepnv` | Bearbeitet Verkehr, ÖPNV, Rettungswege, Baustellen, Umleitungen und Straßenverkehrsbehörden im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `versammlungskonzept-wahlkampf-politische` | Erstellt ein belastbares Versammlungskonzept als Anlage zur Anzeige oder als Antwort auf Behördenfragen im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `wahlkampf-und-politische-kundgebung` | Prüft Wahlkampfstände, Kandidatenauftritte, Parteiveranstaltungen, Gegendemonstrationen und kommunale Neutralitätsfragen im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |
| `widerspruch-klage` | Widerspruch Klage im Versammlungsrecht im Versammlungsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
