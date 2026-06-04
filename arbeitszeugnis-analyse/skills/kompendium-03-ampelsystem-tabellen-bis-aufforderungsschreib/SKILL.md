---
name: kompendium-03-ampelsystem-tabellen-bis-aufforderungsschreib
description: "arbeitszeugnis-analyse: Konsolidiertes Skill-Kompendium 03; bündelt 2 frühere Spezialskills (ampelsystem-tabellenausgabe, aufforderungsschreiben-arbeitgeber) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 03 - arbeitszeugnis-analyse

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `ampelsystem-tabellenausgabe` | Erstellt die standardisierte Ampel-Ausgabetabelle für analysierte Arbeitszeugnisse. Anwendungsfall Zeugnisanalyse ist abgeschlossen und Ergebnis soll in einheitlicher Tabelle mit Satz Ampel Bewertung Notentendenz und Begründung dargestellt werden. Vereinheitlicht Output aller Analyse-Skills für Mandantenbericht und Klagebegründung. Output strukturierte Ampeltabelle als Grundlage für mandantenbericht-zeugnisanalyse und klage-strategie-zeugnisberichtigung. |
| `aufforderungsschreiben-arbeitgeber` | Außergerichtliches Berichtigungsverlangen an den Arbeitgeber. Aufbau mit Mandatsanzeige, konkreter Beanstandung pro Streitstelle (Wortlaut alt, Wortlaut neu, Begründung mit BAG-Rechtsprechung und Geheimcode-Hinweis), Fristsetzung, Klageandrohung und Kostenfolge. Hoeflich-bestimmter Ton, juristisch sauber, ohne Drohgebaerden. Vorlage und Bausteine. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `ampelsystem-tabellenausgabe`

**Frühere Beschreibung:** Erstellt die standardisierte Ampel-Ausgabetabelle für analysierte Arbeitszeugnisse. Anwendungsfall Zeugnisanalyse ist abgeschlossen und Ergebnis soll in einheitlicher Tabelle mit Satz Ampel Bewertung Notentendenz und Begründung dargestellt werden. Vereinheitlicht Output aller Analyse-Skills für Mandantenbericht und Klagebegründung. Output strukturierte Ampeltabelle als Grundlage für mandantenbericht-zeugnisanalyse und klage-strategie-zeugnisberichtigung.

# Ampelsystem-Tabellenausgabe

## V90 Fachkern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Ampelsystem-Tabellenausgabe` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Dieser Skill definiert das Standardausgabeformat für die vollständige Zeugnis-Analyse. Er sammelt die Ergebnisse der einzelnen Analyse-Skills und bringt sie in eine einheitliche, gut lesbare Tabellenstruktur. Das Ampelsystem (Rot/Orange/Grün) macht den Befund auf einen Blick sichtbar und erlaubt eine schnelle Orientierung über die Qualität des Zeugnisses.

Die Haupttabelle enthält für jeden notenrelevanten Satz fünf Spalten: den Satz (als Zitat oder Kurzform), die Ampelfarbe (Grün/Orange/Rot), die Bewertung (Note 1 bis Note 5), die Notentendenz (aufwärts/stabil/abwärts im Gesamtkontext), und eine kurze Begründung (welches Schlüsselwort oder welche Auslassung das Signal ausgelöst hat). Nicht-notenrelevante Sätze wie die Aufgabenbeschreibung erscheinen in einer separaten Übersichtstabelle als "neutral".

Die Farbcodierung folgt festen Regeln: Grün steht für Note 1 und Note 2, Orange für Note 3, Rot für Note 4 und Note 5. Bei gemischten Signalen (z. B. ein Satz mit grüner Leistungsaussage und orangem Abschluss) wird der Satz als Orange gewertet — schwächstes Element bestimmt die Farbe.

Die Gesamtbewertung am Ende der Tabelle fasst die Ampelverteilung zusammen: Anzahl grüner, oranger und roter Sätze, gewichteter Durchschnitt (Leistung mit höherem Gewicht als Verhaltensdetails), und die sich ergebende Gesamtnote als Spanne (z. B. "Note 2 bis Note 3"). Die Spanne ist wichtiger als eine einzelne Zahl, weil Zeugnisse selten exakt eine Note entsprechen.

## Geheimcode-Regeln

| Element | Ampel-Zuordnung |
|---|---|
| Note 1-Formel vorhanden | Grün |
| Note 2-Formel vorhanden | Grün |
| Note 3-Formel vorhanden | Orange |
| Note 4-Formel vorhanden | Rot |
| Note 5-Formel vorhanden | Rot |
| Gemischter Satz (grün + orange) | Orange gesamt |
| Gemischter Satz (grün + rot) | Rot gesamt |
| Fehlende Pflichtaussage | Rot |

## Beispiele

**Beispiel 1 – Ausgabe für Note-1-Zeugnis:**

| Satz | Ampel | Bewertung | Notentendenz | Begründung |
|---|---|---|---|---|
| "stets zur vollsten Zufriedenheit" | Grün | Note 1 | Stabil | Vollständige Maximalformel |
| "stets einwandfrei" (Verhalten) | Grün | Note 1 | Stabil | Maximale Verhaltensformel |
| Vollständige Schlussformel | Grün | Note 1-2 | Stabil | Alle drei Elemente vorhanden |

**Beispiel 2 – Ausgabe für gemischtes Zeugnis:**

| Satz | Ampel | Bewertung | Notentendenz | Begründung |
|---|---|---|---|---|
| "zur vollen Zufriedenheit" | Orange | Note 3 | Abschwächend | Fehlendes "stets" |
| "bemüht" (Leistungsaussage) | Rot | Note 4 | Abwärts | Rotes Signal durch "bemüht" |
| Schlussformel ohne Bedauern | Orange | Note 3 | Abschwächend | Fehlendes Bedauern |

**Beispiel 3 – Gesamtzusammenfassung:** Grüne Sätze: 4 / Orange Sätze: 2 / Rote Sätze: 1 → Gewichtete Gesamtnote: Note 2 bis 3. Empfehlung: Nachverhandlung des roten Satzes und eines orangen Satzes sinnvoll.

## Ausgabeformat

Die Ausgabe umfasst: (1) Übersichtstabelle aller Sätze mit Ampelzuordnung, (2) separate Tabelle der Auslassungen, (3) Ampel-Zusammenfassung (Anzahl je Farbe), (4) Gesamtnoten-Spanne, (5) Handlungsempfehlung (Zeugnis akzeptieren / Nachverhandlung empfehlen / Klage prüfen).

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf qualifiziertes Zeugnis; Wohlwollensgebot und Wahrheitspflicht
- **§ 109 Abs. 2 GewO** — Zeugnis muss klar und verständlich formuliert sein; Codierungen, die Fortkommen erschweren, verstoßen gegen Wohlwollensgebot

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage — vor der Tabellenausgabe klären

1. Welche Analyse-Skills wurden bereits ausgeführt? (Leistungsbeurteilung, Verhaltensbeurteilung, Schlussformel)
2. Liegt ein vollständiges Zeugnisdokument vor oder nur Auszüge?
3. Ist das Ziel: Mandantenbericht, Klageantrag-Vorbereitung oder interne Einschätzung?

## 2. `aufforderungsschreiben-arbeitgeber`

**Frühere Beschreibung:** Außergerichtliches Berichtigungsverlangen an den Arbeitgeber. Aufbau mit Mandatsanzeige, konkreter Beanstandung pro Streitstelle (Wortlaut alt, Wortlaut neu, Begründung mit BAG-Rechtsprechung und Geheimcode-Hinweis), Fristsetzung, Klageandrohung und Kostenfolge. Hoeflich-bestimmter Ton, juristisch sauber, ohne Drohgebaerden. Vorlage und Bausteine.

# Aufforderungsschreiben an den Arbeitgeber

## V90 Fachkern — Arbeitsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Aufforderungsschreiben an den Arbeitgeber` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** BGB §§ 611a, 613a, 615, 623; KSchG §§ 1, 4, 7; TzBfG §§ 14, 15, 16; AGG §§ 1, 3, 7, 15, 22; EntgTranspG §§ 3, 5, 7; BUrlG §§ 1, 3, 7; BetrVG §§ 87, 99, 102; ArbZG; NachwG; SGB IX §§ 164, 167, 168.
- **Verifizierte Anker:** BAG, Urteil vom 23.10.2025 - 8 AZR 300/24 (Entgeltgleichheit, Paarvergleich, Beweislast, bundesarbeitsgericht.de); BAG, Urteil vom 03.06.2025 - 9 AZR 104/24 (kein Verzicht auf gesetzlichen Mindesturlaub im bestehenden Arbeitsverhältnis); bei Kündigungszugang immer § 623 BGB, Zugang nach § 130 BGB, Dreiwochenfrist §§ 4, 7 KSchG und Beweis des konkreten Umschlags trennen.
- **Arbeitsmodus:** Zuerst Status, Zugang, Frist, Beteiligungsrechte, Sonderkündigungsschutz, Beweislast und prozessualen nächsten Schritt sichern; dann erst Materiellrecht vertiefen.
- **Outputpflicht:** Fristenblatt, Zugangsmatrix, Beweisangebot, Mandantenmail, Betriebsrats-/Gegnerbrief oder Klage-/Erwiderungsbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


Nach dem Mandantenbericht und Zustimmung des Mandanten zur Option B (oder als Pflichtschritt vor Klage) wird der Arbeitgeber schriftlich zur Berichtigung aufgefordert. Dieser Skill liefert Aufbau, Bausteine und Mustertext.

## Funktion und Wirkung

Das Aufforderungsschreiben hat drei Funktionen. Es gibt dem Arbeitgeber eine faire Gelegenheit zur Korrektur, schärft die Streitpunkte für eine mögliche Klage und schafft eine saubere Grundlage für Fristsetzung, Verzug und Kostenargumente. Es sollte fast immer vor einer Klage stehen, aber nicht als starre Zulässigkeitsformel behauptet werden.

Der Ton ist hoeflich, sachlich und bestimmt. Drohgebaerden sind kontraproduktiv. Die Klageandrohung erfolgt einmal am Ende, klar und ohne Eskalation. Beleidigungen, Empoerungssprache und ironische Spitzen schwaechen die spaetere Prozessposition.

## Aufbau in acht Bausteinen

### Baustein 1 Mandatsanzeige

Standardformulierung mit Hinweis auf die beigefuegte Vollmacht. Verweis auf die Mandantin oder den Mandanten mit vollem Namen, Geburtsdatum und Beschaeftigungszeitraum.

### Baustein 2 Bezugnahme auf das Zeugnis

Datum des Zeugnisses, Datum der Aushaendigung an den Mandanten, Form (qualifiziertes Zeugnis, einfaches Zeugnis, Zwischenzeugnis). Festhalten, dass das Zeugnis in dieser Form nicht den Anspruechen aus Paragraf 109 GewO genuegt.

### Baustein 3 Rechtsgrundlage

Kurzer Block: Anspruch aus Paragraf 109 Absatz 1 Satz 3 GewO auf wohlwollende Beurteilung. Anspruch aus Paragraf 109 Absatz 2 GewO auf Wahrheit und Klarheit. Hinweis auf staendige Rechtsprechung des BAG zur Beweislastverteilung.

### Baustein 4 Beanstandungen pro Streitstelle

Pro Streitstelle ein Block mit fester Struktur. Zitat des bisherigen Wortlauts in Anfuehrungszeichen. Erlaeuterung, was der Wortlaut in der Zeugnissprache bedeutet (Geheimcode-Hinweis, Drift, Auslassung, Steigerungsadverb). Verweis auf einschlaegige BAG-Entscheidungen oder den Stand der Literatur. Vorschlag fuer die neue Formulierung in Anfuehrungszeichen. Begruendung, warum die neue Formulierung der Wahrheit entspricht und dem Wohlwollensgebot genuegt.

### Baustein 5 Schlussformel und Gesamtbild

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Baustein 6 Fristsetzung

Konkrete kalendermaessige Frist mit Datum (kein "binnen zwei Wochen"). Empfohlen sind zwei bis drei Wochen ab Zugang. Bei Eilbeduerftigkeit (anstehendes Vorstellungsgespraech) kuerzere Frist mit Begruendung. Hinweis auf Verzug bei fruchtlosem Fristablauf.

### Baustein 7 Klageandrohung

Knappe, sachliche Ankuendigung: Sollte das Zeugnis nicht fristgerecht in der vorgeschlagenen Form neu erteilt werden, werde Klage zum Arbeitsgericht erhoben. Keine Eskalation, keine Wiederholung.

### Baustein 8 Kostenfolge und Schluss

Hinweis auf Erstattung der entstandenen Anwaltskosten als Verzugsschaden. Konkrete Bezifferung kann erfolgen oder vorbehalten bleiben. Schlussformel mit Verweis auf Beweisanzeichen (Anlage Vollmacht, Anlage Zeugnis, Anlage Vorzeugnis).

## Mustertext

Sehr geehrte Damen und Herren,

unter Beifuegung der auf uns lautenden Vollmacht zeigen wir die anwaltliche Vertretung der Mandantin [Vorname Name], geboren am [Datum], an. Bei Ihnen bestand vom [Datum] bis zum [Datum] ein Arbeitsverhaeltnis.

Unsere Mandantin hat von Ihnen am [Datum] das beigefuegte qualifizierte Zeugnis erhalten. Das Zeugnis entspricht nicht den Anspruechen aus Paragraf 109 GewO. Aus dem Wohlwollensgebot und dem Wahrheitsgebot ergeben sich Berichtigungspflichten zu mehreren Punkten.

Wir beanstanden im Einzelnen:

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Punkt 2 Schlussformel.** Die Schlussformel enthält keine Dankesformel und kein Bedauern über das Ausscheiden. Ob daraus ein einklagbarer Berichtigungsanspruch folgt, ist nur nach live verifizierter Rechtsprechung zu bewerten. Im vorliegenden Gesamtbild wirkt die knappe Schlussformel jedoch deutlich distanzierend und steht nicht im Einklang mit den übrigen positiven Leistungsbewertungen. Wir bitten deshalb um folgende einvernehmliche Neufassung: "Wir bedauern das Ausscheiden von Frau [Name], danken ihr für die geleistete Arbeit und wünschen ihr für ihren weiteren beruflichen und persönlichen Lebensweg alles Gute."

**Punkt 3 Vorgesetztenbeurteilung.** Trotz unstreitiger Fuehrungsverantwortung enthaelt das Zeugnis keine Aussage zur Vorgesetztenbeurteilung. Diese Auslassung wird im Bewerbungsverkehr als verdecktes Negativsignal gelesen. Wir bitten um Ergaenzung: "Als Vorgesetzte wurde sie von ihren Mitarbeiterinnen und Mitarbeitern stets uneingeschraenkt anerkannt."

[Weitere Punkte analog.]

Wir bitten Sie, das berichtigte Zeugnis bis zum [Datum] in einfacher Form und auf Geschaeftspapier ohne Anlassbezug auf das Berichtigungsverlangen zu erteilen. Sollte das Zeugnis nicht fristgerecht in der vorgeschlagenen Form neu erteilt werden, werden wir Klage zum zustaendigen Arbeitsgericht erheben.

Die durch unsere Einschaltung entstandenen Anwaltskosten machen wir bereits jetzt als Verzugsschaden geltend; eine Bezifferung erfolgt mit gesondertem Schreiben.

Mit freundlichen Gruessen

[Kanzlei]

Anlagen: Vollmacht, Zeugnis vom [Datum], Vorzeugnis vom [Datum]

## Stilregeln

| Regel | Hinweis |
| --- | --- |
| Hoeflich, bestimmt, sachlich | Keine Drohgebaerden, kein Empoerungston |
| Konkrete Wortlaute, nicht "bitte verbessern" | Pro Streitstelle alter und neuer Wortlaut in Anfuehrungszeichen |
| Belege fuer Geheimcodes | BAG-Rechtsprechung, Quellenprüfung, kein Verweis auf interne Notenmatrix |
| Frist kalendermaessig | Konkretes Datum, keine Zeitspanne ohne Anker |
| Klageandrohung nur am Ende | Einmal, knapp, ohne Wiederholung |
| Schlussformel mit Anlagenverzeichnis | Vollmacht, Zeugnis, Vorzeugnis, Korrespondenz |

## Anschluss

Bleibt die Frist fruchtlos, geht es weiter mit `klage-strategie-zeugnisberichtigung`. Bei vollstaendiger Berichtigung folgt ein Abschlussschreiben an den Mandanten und ggf. Kostennote. Bei Teilberichtigung wird neu entschieden: Akzeptanz des Teilerfolgs oder Klage zum Rest.

## Rechtliche Einordnung und Normen

- **§ 109 GewO** — Anspruch auf wohlwollendes qualifiziertes Zeugnis; Berichtigungsanspruch bei Verstoß
- **§ 288 BGB** — Verzugszinsen; Anwaltskosten als Verzugsschaden ab Fristablauf
- **§ 242 BGB** — Treu und Glauben; Verwirkung bei sehr langem Zuwarten ohne Beanstandung

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
