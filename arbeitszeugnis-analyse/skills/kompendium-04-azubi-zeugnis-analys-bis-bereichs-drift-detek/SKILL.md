---
name: kompendium-04-azubi-zeugnis-analys-bis-bereichs-drift-detek
description: "arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 04; bündelt 2 frühere Spezialskills (azubi-zeugnis-analyse, bereichs-drift-detektor) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 04 - arbeitszeugnis-analyse

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `azubi-zeugnis-analyse` | Analyse von Ausbildungszeugnissen nach § 16 BBiG bei Zeugnisstreit oder Berichtigungsverlangen. Anwendungsfall Auszubildender hat Ausbildungszeugnis erhalten das er für schlecht haelt. Normen § 16 BBiG Zeugnispflicht § 109 GewO analog. Prüfraster Lernfortschritt Berufsschulleistungen praktische Ausbildungsaufgaben Verhalten im Betrieb Ampelzuordnung branchenspezifische Formulierungen. Output Ampeltabelle mit Notentendenzen Begründungen und Verbesserungsvorschlaegen. Abgrenzung zu leistungsbeurteilung-analyse und schlussformel-bewertung (Arbeitszeugnisse Erwachsener). |
| `bereichs-drift-detektor` | Erkennt das Schaufenster-Pattern in Arbeitszeugnissen: einzelne Spitzensaetze suggerieren Note eins, waehrend benachbarte Saetze zum selben Themenbereich nur Note drei tragen. Tracked Drift pro Themenbereich (Fachkenntnisse, Arbeitsweise, Engagement, Innovation, Erfolg, Sozialverhalten) und schlaegt Alarm bei systematischer Notenspreizung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `azubi-zeugnis-analyse`

**Frühere Beschreibung:** Analyse von Ausbildungszeugnissen nach § 16 BBiG bei Zeugnisstreit oder Berichtigungsverlangen. Anwendungsfall Auszubildender hat Ausbildungszeugnis erhalten das er für schlecht haelt. Normen § 16 BBiG Zeugnispflicht § 109 GewO analog. Prüfraster Lernfortschritt Berufsschulleistungen praktische Ausbildungsaufgaben Verhalten im Betrieb Ampelzuordnung branchenspezifische Formulierungen. Output Ampeltabelle mit Notentendenzen Begründungen und Verbesserungsvorschlaegen. Abgrenzung zu leistungsbeurteilung-analyse und schlussformel-bewertung (Arbeitszeugnisse Erwachsener).

# Ausbildungszeugnis-Analyse (Azubi-Zeugnis)

## V90 Fachkern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Ausbildungszeugnis-Analyse (Azubi-Zeugnis)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Das Ausbildungszeugnis nach § 16 BBiG unterscheidet sich grundlegend vom Arbeitszeugnis für Angestellte. Es beurteilt nicht die berufliche Leistung einer Vollkraft, sondern den Lern- und Entwicklungsfortschritt während der Ausbildung. Die Formulierungen sind anders, der Maßstab ist ein anderer, und die Ampelsignale folgen teilweise anderen Mustern.

Das Ausbildungszeugnis enthält üblicherweise vier Hauptblöcke: (1) Beschreibung der Ausbildungsstelle und des Ausbildungsberufs, (2) Beurteilung der praktischen Ausbildungsleistung im Betrieb, (3) Beurteilung der Berufsschulleistungen (sofern zutreffend), und (4) Verhalten im Betrieb und in der Berufsschule sowie eine Schlussformel. Fehlt der Berufsschulabschnitt, kann das bei einem dualen Ausbildungsberuf ein orangefarbenes Signal sein.

Die Lernfortschritts-Beurteilung verwendet andere Superlative als das normale Zeugnis: "hat die Ausbildungsinhalte schnell und sicher aufgenommen" ist grün; "hat sich die Ausbildungsinhalte angeeignet" ist orange; "war bereit, die Ausbildungsinhalte zu erlernen" ist rot (das "bereit" entspricht dem "bemüht" im Vollkraft-Zeugnis). Die Berufsschulbeurteilung kann auf Zeugnisse verweisen oder eine eigene Einschätzung bieten.

Verhaltensformeln im Azubi-Zeugnis sind tendenziell milder und entwicklungsbezogener als im Vollkraft-Zeugnis. Formulierungen wie "hat sich positiv entwickelt" sind für einen Azubi grün, für eine Führungskraft wäre sie orange. Der Alters- und Entwicklungskontext muss immer mitgedacht werden.

## Geheimcode-Regeln

| Azubi-Formulierung | Bedeutung | Ampel |
|---|---|---|
| "schnell und sicher aufgenommen" | Hervorragender Lernfortschritt | Grün |
| "zuverlässig die Ausbildungsinhalte angeeignet" | Guter Lernfortschritt | Grün |
| "hat sich die Inhalte erarbeitet" | Befriedigender Fortschritt | Orange |
| "war bereit zu erlernen" | Unterdurchschnittlicher Fortschritt | Rot |
| Fehlender Berufsschulabschnitt (duale Ausbildung) | Mögliche Schulprobleme | Orange |
| "hat sich positiv entwickelt" | Für Azubi: gut; für Vollkraft: schwach | Grün (Azubi) |
| "pünktlich und zuverlässig" | Wichtiges Grundverhalten | Grün |
| Fehlende Pünktlichkeitsaussage | Fehlzeiten/Verspätungen | Orange |

## Beispiele

**Beispiel 1 – Grünes Azubi-Zeugnis:** "Herr Müller hat die Ausbildungsinhalte stets schnell und sicher aufgenommen, zeigte großes Interesse an seinem Ausbildungsberuf und zeichnete sich durch hervorragende Berufsschulleistungen aus."

**Beispiel 2 – Orange Azubi-Zeugnis:** "Frau Weber hat sich die Ausbildungsinhalte erarbeitet und dabei guten Willen gezeigt. Die Berufsschulleistungen entsprachen den Anforderungen." — Kein Superlativ, kein Engagement, keine Begeisterung.

**Beispiel 3 – Rotes Azubi-Zeugnis:** "Herr Bauer war stets bereit, die Ausbildungsinhalte zu erlernen, und hat die Anforderungen im Wesentlichen erfüllt." — "Bereit" + "im Wesentlichen" = doppeltes rotes Signal.

**Beispiel 4 – Fehlender Berufsschulabschnitt:** Zeugnis eines Industriekaufmanns (duale Ausbildung) ohne jede Aussage zur Berufsschule → orangefarbenes Signal.

**Beispiel 5 – Vollständige positive Schlussformel:** "Wir bedauern es sehr, Frau Klein am Ende ihrer Ausbildung zu verlieren, und danken ihr herzlich für ihr Engagement. Wir empfehlen sie uneingeschränkt." — Starkes Signal für einen Übernahme- oder Weiterempfehlungswunsch.

## Ausgabeformat

Der Skill gibt eine azubi-spezifische Checkliste aus (Lernfortschritt / Praxis / Berufsschule / Verhalten / Schlussformel / Weiterempfehlung), gefolgt von der Ampeltabelle mit azubi-adjustierten Bewertungsmaßstäben und einer Empfehlung (Zeugnis annehmen / nachverhandeln / anfordern falls fehlt).

## Rechtliche Einordnung und Normen

- **§ 16 BBiG** — Anspruch des Auszubildenden auf qualifiziertes Zeugnis nach Beendigung der Ausbildung
- **§ 13 BBiG** — Pflichten des Auszubildenden; Pflichtverletzungen dürfen nur bei tragfähiger Tatsachengrundlage in die Beurteilung einfließen
- Allgemeine Zeugnisgrundsätze zu Wahrheit, Klarheit und Wohlwollen sind bei Ausbildungszeugnissen entsprechend zu berücksichtigen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage — vor der Azubi-Analyse

1. Abschlusszeugnis oder Zwischenzeugnis (§ 16 Abs. 2 BBiG)?
2. Duales Ausbildungsverhältnis? → Berufsschulbewertung vorhanden?
3. Ausbildung abgebrochen? → Nur Anspruch auf einfaches Zeugnis nach § 16 Abs. 1 BBiG
4. Beendigungsgrund: Bestehen der Prüfung oder Kündigung/Aufhebung?

## 2. `bereichs-drift-detektor`

**Frühere Beschreibung:** Erkennt das Schaufenster-Pattern in Arbeitszeugnissen: einzelne Spitzensaetze suggerieren Note eins, waehrend benachbarte Saetze zum selben Themenbereich nur Note drei tragen. Tracked Drift pro Themenbereich (Fachkenntnisse, Arbeitsweise, Engagement, Innovation, Erfolg, Sozialverhalten) und schlaegt Alarm bei systematischer Notenspreizung.

# Bereichs-Drift-Detektor (Schaufenster-Pattern)

## V90 Fachkern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Bereichs-Drift-Detektor (Schaufenster-Pattern)` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Ein Zeugnis kann handwerklich gut aussehen und trotzdem in der Gesamtschau eine schlechtere Note tragen als die Spitzensätze suggerieren. Das geschieht, wenn der Aussteller jedem Themenbereich einen starken Eröffnungssatz (Note 1) voranstellt und unmittelbar darauf einen abschwächenden Folgesatz (Note 3) zum selben Thema platziert. Der unbedarfte Leser bleibt an den ersten Sätzen hängen und übersieht die Korrektur. Eingeweihte lesen die Drift und schließen auf eine systematische Abwertung.

Der Skill bildet acht Themenbereiche ab, in denen sich Drift typischerweise verbirgt: Fachkenntnisse, Weiterbildung und Lernbereitschaft, strategisches und konzeptionelles Denkvermögen, Arbeitsweise und Sorgfalt, Eigeninitiative und Engagement, Innovationsfähigkeit, Arbeitsergebnisse und Erfolge sowie Sozialverhalten gegenüber Vorgesetzten, Kollegen und Externen. Innerhalb jedes Bereichs werden alle zugehörigen Sätze gesammelt und mit einer Einzelnote belegt. Die Spreizung zwischen Höchst- und Niedrigsnote pro Bereich ergibt den Drift-Wert.

Eine Drift von zwei Stufen oder mehr innerhalb desselben Themenbereichs ist ein eigenständiges rotes Signal und wird in der Gesamtnoten-Aggregation gesondert berücksichtigt. Eine Drift von einer Stufe ist ein oranges Signal und deutet auf bewusste Vorsicht des Ausstellers hin. Eine bereichsübergreifende, gleichbleibend hohe Bewertung ohne Drift gilt als authentisch grün.

Besonders heikel sind Drifts in den weichen Bereichen Lernbereitschaft, Innovation und Sozialverhalten: Sie betreffen genau jene Eigenschaften, die ein einstellender Arbeitgeber für Zukunftsentscheidungen am stärksten gewichtet. Ein Spitzenwert bei Fachkenntnissen mit gleichzeitiger Drift bei Lernbereitschaft signalisiert: Der Kandidat kann was er kann, aber wenig Neues mehr.

## Geheimcode-Regeln

| Drift-Befund | Signalwirkung | Ampel |
|---|---|---|
| Note eins und Note drei zum selben Themenbereich direkt aufeinanderfolgend | Schaufenster-Eroeffnung mit kodierter Korrektur | Rot |
| Spreizung zwei Stufen innerhalb eines Bereichs | Systematische Abwertung | Rot |
| Spreizung eine Stufe innerhalb eines Bereichs | Bewusste Vorsicht | Orange |
| Drift bei Lernbereitschaft trotz starker Fachkenntnisse | Stagnationssignal | Rot |
| Drift bei Sozialverhalten trotz starker Leistungsteile | Konfliktsignal | Rot |
| Drift bei Innovation trotz starker Arbeitsweise | Routinesignal | Orange |
| Bereichsuebergreifend konstante Note eins | Authentisch grün | Grün |

## Beispiele

**Beispiel 1 – Klassische Schaufenster-Drift bei Lernbereitschaft:** Satz A: "verfuegt auch in Randbereichen seines vielfaeltigen Aufgabenbereiches ueber aeusserst profundes Fachwissen" (Note 1). Satz B unmittelbar darauf: "nahm in eigener Initiative regelmaessig erfolgreich an internen und externen Weiterbildungsseminaren teil" (Note 3). Beide gehoeren zum Themenbereich Fachwissen/Lernen. Drift zwei Stufen, Rot.

**Beispiel 2 – Drift bei Arbeitsweise und Innovation:** Satz A: "fuehrte er jederzeit vollkommen selbststaendig, aeusserst sorgfaeltig und planvoll durchdacht aus" (Note 1). Satz B: "war Neuem gegenueber aufgeschlossen, fand gute neue Ideen und innovative Ansaetze" (Note 3, da "gute" statt "hervorragende" und keine Steigerungsadverbien). Drift zwei Stufen im weichen Bereich, Rot.

**Beispiel 3 – Drift im Sozialverhalten trotz Top-Erfolg:** Satz A: "Arbeitsergebnisse lagen stets sehr weit ueber unseren Anforderungen" (Note 1). Satz B im Sozialteil: "war ein geschaetzter Ansprechpartner, sein persoenliches Verhalten war einwandfrei" (Note 3, da "einwandfrei" ohne "stets" und "geschaetzt" ohne Steigerung). Themen unterschiedlich, aber Drift in einem heiklen Bereich, Rot.

**Beispiel 4 – Drift eine Stufe:** "aeusserst motiviert die gesetzten Ziele beharrlich zu verfolgen" (Note 1) und kurz darauf "zeigte eine hohe Lernbereitschaft" (Note 2 bis 3). Eine Stufe, Orange.

**Beispiel 5 – Keine Drift, authentisch:** Alle Saetze im Bereich Fachkenntnisse tragen durchgehend Steigerungsadverbien und Superlative auf Note-1-Niveau. Keine Drift, Grün.

## Ausgabeformat

Der Skill gibt aus: pro Themenbereich eine Tabelle mit den enthaltenen Saetzen, der Einzelnote je Satz, dem hoechsten und niedrigsten Wert sowie der Drift-Spreizung. Anschliessend eine Bereichsbilanz mit Drift-Wert, Ampelzuordnung und Hinweis auf besonders heikle Bereiche (Lernbereitschaft, Innovation, Sozialverhalten). Am Ende eine Gesamtdrift-Einschaetzung mit Empfehlung: Akzeptieren, Nachverhandeln einzelner Saetze, Klagepruefung.

## Rechtliche Einordnung und Normen

- **§ 109 Abs. 2 GewO** — Zeugnis muss klar und verständlich sein; widersprüchliche Bewertungen im selben Themenbereich verstoßen gegen Wohlwollensgebot
- **§ 242 BGB** — Treu und Glauben; innerhalb desselben Zeugnisabschnitts darf der Arbeitgeber nicht gleichzeitig Bestnoten und Mängel bescheinigen

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage — vor der Drift-Prüfung

1. Welche Themenblöcke sind im Zeugnis enthalten? (Fachkenntnisse, Motivation, Qualität, Teamverhalten, Führung, Schluss)
2. Wurde die Zufriedenheitsformel bereits ausgewertet? (Satzweise-Notenmatrix-Skill?)
3. Ziel der Drift-Analyse: Klageantrag-Vorbereitung oder Mandantenberatung?
