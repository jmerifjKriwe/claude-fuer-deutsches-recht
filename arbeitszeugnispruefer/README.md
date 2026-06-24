# Arbeitszeugnispruefer

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Dies ist eines von 232 Plugins dieser Sammlung. Jedes Plugin enthält eine Familie zusammenhängender Skills (`SKILL.md`-Dateien), passende Hilfsdateien, Prüfraster, Vorlagen und in vielen Fällen eine eigene Arbeitsakte. Der vorgesehene Hauptweg ist die Installation über den Marketplace, alternativ als einzelnes Plugin-ZIP. Dann läuft das Plugin mit seinen Skills, Werkzeugen und Testdaten in der dafür vorgesehenen Plugin-Umgebung.

Damit das Plugin auch ohne Plugin-Setup brauchbar bleibt, gibt es zusätzlich zwei reine Markdown-Prompts: einen ausführlichen Werkstatt-Prompt und einen kompakten Schnellstart-Prompt. Beide sind einzelne `.md`-Dateien, die man in eine geeignete Arbeitsumgebung ziehen, einfügen oder per Copy-and-Paste verwenden kann.

## Downloads

In dieser Reihenfolge gedacht: zuerst der vorgesehene Plugin-Weg, danach die Markdown-Alternativen, am Schluss die zugehörigen Testakten.

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`arbeitszeugnispruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/arbeitszeugnispruefer.zip) |
| Großer Prompt (Werkstatt, Alternative ohne Plugin-Setup) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/arbeitszeugnispruefer-werkstatt.md" download><code>arbeitszeugnispruefer-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart, höchstens 7500 Zeichen, Spar-Alternative) | Markdown | <a href="https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/arbeitszeugnispruefer/arbeitszeugnispruefer-schnellstart.md" download><code>arbeitszeugnispruefer-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`alle-testakten.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/alle-testakten.zip) |

> Marketplace-Hinweis: Wer mehrere Plugins gleichzeitig will, fügt nicht jedes Plugin einzeln hinzu, sondern den ganzen Marketplace über `marketplace.json` aus dem [aktuellen Release](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest). Dann sind alle 232 Plugins verfügbar und können einzeln aktiviert werden.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du ein bereits vorliegendes deutsches Arbeitszeugnis Satz für Satz prüfen — Note, Geheimcodes, Auslassungen, Schlussformel — und brauchst eine belastbare Einschaetzung mit Rechtsprechungsanker.

## Wenn du das brauchst

- **Arbeitnehmer** hat ein Zeugnis erhalten und will wissen, welche Note darin codiert ist, bevor er bewirbt oder widerspricht.
- **Fachanwalt für Arbeitsrecht** prüft ein Zeugnis im Mandat auf Berichtigungsanspruch nach Paragraf 109 GewO.
- **Personalabteilung** prüft das eigene Zeugnis vor der Ausstellung gegen die Standards der BAG-Rechtsprechung.
- **Karriereberater oder Outplacement-Berater** sichten Zeugnisse aus dem Lebenslauf ihrer Klienten und brauchen eine schnelle Einordnung.

## Was du am Ende in der Hand hast

Eine Prüfung Satz für Satz mit Ampel-Einschaetzung (rot, orange, gruen), eine begründete Gesamtnotenspanne, eine Liste der Geheimcodes, Drift-Stellen und Auslassungen, ein Mandantenbericht in Klartext sowie auf Wunsch ein Aufforderungsschreiben an den Arbeitgeber zur Berichtigung oder eine Klagestrategie mit Vollstreckungsoption.

## Der Weg dorthin

Zeugnis einlesen → Stammdaten und Vollständigkeit prüfen → Tätigkeitsabschnitt auf Wertigkeitsdrift prüfen → Leistungssaetze auf Zufriedenheitsformel und Steigerungsadverbien prüfen → Verhaltenssaetze auf Personenreihenfolge und Geheimcodes prüfen → Schlussformel auf Note-Mismatch prüfen → Gesamtnote ableiten → Berichtigungspfad oder Annahme empfehlen.

## Workflows

Drei Modi zur Wahl:

- **Schnellpruefung**: Notenschaetzung, Top-Drei-Auffaelligkeiten, Empfehlung in wenigen Saetzen.
- **Vollpruefung**: Satzweise Einschaetzungsmatrix, Geheimcode-Katalog, Drift-Bericht, Schlussformel-Analyse, Mandantenbericht.
- **Berichtigungspfad**: Vollpruefung plus Aufforderungsschreiben an den Arbeitgeber und Klagestrategie mit Beweislastverteilung nach BAG-Linie.

## Direkt-Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Werkstatt-Prompt (autarker großer Prompt) | Markdown | <a href="" download>arbeitszeugnispruefer-werkstatt.md</a> |
| Schnellstart-Prompt (max 7500 Zeichen) | Markdown | <a href="" download>arbeitszeugnispruefer-schnellstart.md</a> |
| Megaprompt-Original (Quelle aus dem Ursprungs-Repo) | Markdown | <a href="" download>arbeitszeugnispruefer-megaprompt-original.md</a> |

## Was dich aufhält

- **Geheimcodes**: Formulierungen wie bemüht sich, im großen und ganzen, lernte schnell kennen und schätzen, verstand es zählen zu unsichtbaren Notenabwertungen.
- **Auslassungen**: Fehlt die Zusammenfassungsformel, fehlen Personengruppen im Verhalten, fehlt die Schlussformel, wirkt das wie eine Abwertung.
- **Drift in der Wertigkeit**: Wenn unwichtige Aufgaben zuerst genannt werden oder Kernaufgaben fehlen, droht Schaufenster-Effekt.
- **Beweislast nach BAG 9 AZR 584.13**: Note 1 oder 2 traegt der Arbeitnehmer, Note 4 oder 5 traegt der Arbeitgeber.
- **Schlussformel-Mismatch**: Schwache Schlussformel bei sonst gutem Zeugnis zieht die Gesamtwirkung herunter.

## Rechtlicher Anker

- Paragraf 109 GewO (Zeugnisanspruch und Berichtigung)
- Paragraf 16 BBiG (Ausbildungszeugnis)
- Paragrafen 241 Absatz 2, 280 Absatz 1 BGB (Nebenpflicht und Schadensersatz)
- BAG-Leitentscheidungen zu Notenstufen, Beweislast, Schlussformel und Zeugnisklarheit (im Werkstatt-Prompt ausführlich)

## Hinweise

Generischer Pruefstand, alle Angaben ohne Gewähr. Jede Nutzerin und jeder Nutzer prüft den Pruefbericht auf Plausibilität und Eignung im konkreten Einzelfall. Keine Rechtsberatung. Keine Garantie für Vollständigkeit oder Aktualität der Rechtsprechung. Bei streitigen Fällen Fachanwalt für Arbeitsrecht hinzuziehen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aeussere-form-und-briefkopf` | Pruefung der aeusseren Form eines Arbeitszeugnisses auf Briefkopf, Fliesstext-Gebot, Unterschrift durch die berechtigte Person und Einhaltung der geschaeftsueblichen Anforderungen nach BAG-Rechtsprechung. |
| `ampel-einschaetzung-pro-satz` | Aufbau der satzweisen Einschaetzungsmatrix als Herzstueck der Zeugnispruefung mit Spalten fuer Originalwortlaut, decodierte Aussage, Notentendenz, Ampelfarbe in Worten und Katalogfundstelle. |
| `aufforderungsschreiben-berichtigung` | Erstellung eines aussergerichtlichen Aufforderungsschreibens an den Arbeitgeber zur Zeugnisberichtigung nach Paragraf 109 GewO mit den acht Pflichtbausteinen und Stilregeln fuer den anwaltlichen Einsatz. |
| `auslassungen-erkennen` | Systematisches Erkennen von Auslassungen im Arbeitszeugnis als schweigendem Negativcode, bei dem fehlende Aussagen zu erwarteten Eigenschaften oder Taetigkeiten einen negativen Schluss beim kundigen Leser ausloesen. |
| `beendigungsgrund-pruefen` | Pruefung der Beendigungsformulierung im Arbeitszeugnis auf kodierte Hinweise zum Trennungsanlass wie Eigenkundigung, Arbeitgeberkundigung oder Aufhebungsvertrag und Identifikation problematischer Distanz- oder Konfliktsignale. |
| `beweislast-bag-9-azr-584-13` | Anwendung der BAG-Beweislastregel im Zeugnisstreit mit Note 3 als Ausgangspunkt und Konsequenzen fuer die Durchsetzungschancen des Mandanten bei Verlangen einer besseren oder Abwehr einer schlechteren Bewertung. |
| `doppelboeden-und-verneinungen` | Erkennung von doppelten Verneinungen und versteckten Abschwaecher-Konstruktionen im Arbeitszeugnis als Negativcodes, die sprachlich positiv klingen aber eine eingeschraenkte oder negative Bewertung transportieren. |
| `einfuehrung-pruefauftrag` | Einstieg in den Pruefauftrag fuer ein vorliegendes deutsches Arbeitszeugnis mit Festlegung des Pruefumfangs nach Paragraf 109 GewO sowie Abgrenzung zwischen einfachem und qualifiziertem Zeugnis. |
| `frequenzadverbien-pruefen` | Pruefung der Frequenzadverbien im Arbeitszeugnis als eigene Adverbklasse mit spezifischer Notenwirkung, die Haeufigkeit statt Qualitaet beschreibt und dadurch von Steigerungsadverbien abzugrenzen ist. |
| `fuehrungskraft-verhalten-pruefen` | Pruefung von Zeugnissen fuer Fuehrungskraefte auf vollstaendige Bewertung von Mitarbeiterfuehrung und Loyalitaet mit Erkennung von Auslassungssignalen und spezifischen Negativcodierungen fuer Fuehrungsverhalten. |
| `geheimcodes-katalog` | Katalog der verbreiteten Geheimcodes der deutschen Zeugnissprache nach Themenbereichen mit Angabe der implizierten riskanten Lesarten und Hinweis auf die Grenzen der Decodierung nach Paragraf 109 Absatz 2 GewO. |
| `intake-und-stammdaten-pruefen` | Erfassung und Pruefung der Stammdaten eines vorgelegten Arbeitszeugnisses auf Vollstaendigkeit und Richtigkeit ohne vorheriges Interview mit dem Mandanten. |
| `klagestrategie-und-vollstreckung` | Aufbau der Klagestrategie fuer die Zeugnisberichtigung mit Musterklageantrag, Streitwertberechnung, Kostenrisiko nach Paragraf 12a ArbGG und Vollstreckungsoptionen nach einem Urteil oder gerichtlichen Vergleich. |
| `mandantenbericht-erstellen` | Erstellung des abschliessenden Mandantenberichts nach der Zeugnispruefung mit Zusammenfassung der Gesamtnotenspanne, Streitstellen-Tabelle, Beweisbedarf und konkreter Handlungsempfehlung. |
| `note-1-formeln-erkennen` | Erkennung und Pruefung von Note-1-Formulierungen im Arbeitszeugnis anhand von Maximalsteigerern und herausragenden Einzelaussagen, die gemeinsam eine Beurteilung auf hoechstem Niveau belegen. |
| `note-2-formeln-erkennen` | Erkennung von Note-2-Formulierungen im Arbeitszeugnis durch Identifikation der Standardsteigerer wie stets oder jederzeit in Verbindung mit positiven Bewertungsaussagen und Abgrenzung zur Note 1. |
| `note-3-formeln-erkennen` | Erkennung von Note-3-Formulierungen im Arbeitszeugnis als rechtlichem Ausgangspunkt der Beweislast und Abgrenzung gegenueber Note 2 durch Fehlen des Zeitsteigerers sowie gegenueber Note 4 durch Fehlen eindeutiger Abschwaecher. |
| `note-4-formeln-erkennen` | Erkennung von Note-4-Formulierungen im Arbeitszeugnis durch Identifikation starker Negativ-Steigerer und klassischer Codephrasen wie bemueht oder im Wesentlichen mit direkter Ampel-Einschaetzung als roter Befund. |
| `note-5-formeln-erkennen` | Erkennung von Note-5- und Note-6-Formulierungen im Arbeitszeugnis als schwerste Negativbefunde mit Pruefanweisung fuer gestapelte Abschwaecher, ironisches Ueberlob und das Fehlen jeder positiven Aussage. |
| `notenstufen-bag-9-azr-386-10` | Anwendung der BAG-Notenstufenmatrix mit Zuordnung von Zufriedenheitsformeln zu Noten 1 bis 6 auf der Grundlage von BAG 9 AZR 386.10 und 9 AZR 352.04 sowie Grenzen des Formulierungsspielraums des Arbeitgebers. |
| `personenreihenfolge-pruefen` | Pruefung der Reihenfolge der Bezugspersonen im Verhaltensabschnitt eines Arbeitszeugnisses als eigenstaendiger Berichtigungspunkt mit hoher Klagbarkeit bei Abweichung vom Standard Vorgesetzte vor Kollegen vor Kunden. |
| `rollen-und-modus-wahl` | Bestimmung der Pruefer-Perspektive und des Ausgabemodus vor der Zeugnisanalyse mit Unterscheidung zwischen Arbeitnehmer- und HR-Perspektive sowie interaktivem und nicht-interaktivem Einsatz. |
| `schaufenster-und-drift-erkennen` | Erkennung von Schaufenster-Drift und Bereichs-Drift in Arbeitszeugnissen als Muster, bei dem ein stark positiver Aufgabenkatalog oder einzelne Abschnitte durch eine schwache Gesamtbeurteilung oder ungleichgewichtige Teilabschnitte konter... |
| `schlussformel-notenwirkung-bewerten` | Bewertung der Notenwirkung der Schlussformel anhand der vorhandenen Bausteine mit Einordnung in die Ampel-Skala und Kommunikation der taktischen Konsequenzen fuer Verhandlung und Klage. |
| `schlussformel-pruefen` | Pruefung der Schlussformel eines Arbeitszeugnisses auf Vollstaendigkeit der fuenf Bausteine Bedauern, Dank, beruflicher Wunsch, persoenlicher Wunsch und Erfolgswunsch mit Bewertung der Signalwirkung nach BAG-Linie. |
| `steigerungsadverbien-pruefen` | Systematische Pruefung der Steigerungsadverbien im Arbeitszeugnis mit Zuordnung jedes Adverbs zu einer Notenwirkung von Maximalsteigerer bis Starknegativsteigerer als zentralem Bewertungswerkzeug der deutschen Zeugnissprache. |
| `taetigkeitsabschnitt-wertigkeit-pruefen` | Pruefung des Taetigkeitsabschnitts eines Arbeitszeugnisses auf Vollstaendigkeit der Aufgabenbeschreibung und Erkennung des Schaufenster-Musters als Kontrast zwischen umfangreichem Aufgabenkatalog und schwacher Leistungsformel. |
| `verhaltensabschnitt-pruefen` | Pruefung des Verhaltensabschnitts eines qualifizierten Arbeitszeugnisses auf korrekte Reihenfolge der Bezugspersonen und adaequate Formulierungsstufe mit Erkennung negativer Verhaltenscodierungen. |
| `zeugnisklarheit-objektiver-empfaengerhorizont` | Pruefung eines Arbeitszeugnisses auf das Gebot der Zeugnisklarheit nach Paragraf 109 Absatz 2 GewO mit Anwendung des objektiven Empfaengerhorizonts als Massstab gemaess der BAG-Rechtsprechung (9 AZR 352.04; 9 AZR 386.10). |
| `zusammenfassungsformel-erkennen` | Erkennung und Decodierung der zusammenfassenden Leistungsbeurteilung als Hauptnotentraeger im Arbeitszeugnis mit Zuordnung der Zufriedenheitsformel zu einer Notenstufe von 1 bis 6. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
