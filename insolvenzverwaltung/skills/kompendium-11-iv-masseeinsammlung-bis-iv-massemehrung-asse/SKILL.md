---
name: kompendium-11-iv-masseeinsammlung-bis-iv-massemehrung-asse
description: "insolvenzverwaltung: Konsolidiertes Skill-Kompendium 11; bündelt 2 frühere Spezialskills (iv-masseeinsammlung, iv-massemehrung-asset-realisation) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 11 - insolvenzverwaltung

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `iv-masseeinsammlung` | Massepositionen erfassen und realisieren: Bankguthaben Debitoren Herausgabeansprüche Versicherungen Rückstaende. §§ 80 148 InsO Verwaltungsbefugnis und Massezugehoerigkeit. Prüfraster: Massekarte Priorisierung realisierbare Forderungen Sicherungsrechte Drittschuldneranschreiben. Output: Massekarte Drittschuldnerschreiben Herausgabeanforderungen. Abgrenzung: nicht für aktive Massemehrung durch Verkauf oder Klage (iv-massemehrung-asset-realisation). |
| `iv-massemehrung-asset-realisation` | Verwertungsstrategie und Massemehrung entwickeln wenn Masse niedrig oder Quote ungewiss ist. §§ 159 160 InsO Verwertung § 133 InsO Vorsatzanfechtung § 15b InsO Haftungsansprüche. Prüfraster: Werthebel Assets Prozesse Anfechtung D und O Vergleichspotenzial Kosten-Nutzen. Output: Verwertungskonzept Strategiematrix Beschlussvorlage. Abgrenzung: nicht für reine Masseeinsammlung (iv-masseeinsammlung) oder Betriebsfortführung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `iv-masseeinsammlung`

**Frühere Beschreibung:** Massepositionen erfassen und realisieren: Bankguthaben Debitoren Herausgabeansprüche Versicherungen Rückstaende. §§ 80 148 InsO Verwaltungsbefugnis und Massezugehoerigkeit. Prüfraster: Massekarte Priorisierung realisierbare Forderungen Sicherungsrechte Drittschuldneranschreiben. Output: Massekarte Drittschuldnerschreiben Herausgabeanforderungen. Abgrenzung: nicht für aktive Massemehrung durch Verkauf oder Klage (iv-massemehrung-asset-realisation).

# Masseeinsammlung

## V90 Fachkern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Masseeinsammlung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Erfasst und realisiert Massepositionen: Geld, Forderungen, Herausgabeansprüche, Versicherungen, Debitoren, Rückstände und streitige Ansprüche.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Massebestand unvollständig ist
- Banken, Kunden, Versicherer oder Drittschuldner angeschrieben werden müssen
- kurzfristig Liquidität für Kosten und Fortführung gebraucht wird

## Eingaben

- Banklisten, OPOS, Debitoren, Verträge
- Anlagenverzeichnis, Versicherungen, Prozesslisten
- Korrespondenz mit Drittschuldnern

## Workflow

1. **Massekarte** - Alle potenziellen Massepositionen mit Beleg, Schuldner, Fälligkeit und Durchsetzbarkeit anlegen.
2. **Priorisieren** - schnell realisierbare Forderungen vor streitigen Ansprüchen; Sicherheiten trennen.
3. **Anschreiben** - Drittschuldner-, Bank-, Kunden- und Herausgabeschreiben vorbereiten.
4. **Nachhalten** - Zahlungseingänge matchen, Mahnstufen und Klageoptionen steuern.

## Ausgabe

- Masseeinsammlungsregister
- Drittschuldneranschreiben
- Einziehungs- und Mahnplan

## Qualitätsgates

- Absonderungsrechte geprüft
- Fälligkeit und Anspruchsgrund dokumentiert
- Eingänge mit Forderungen gematcht

## Rote Schwellen

- Zahlung an Schuldner statt Massekonto
- ungeklärte Sicherungsabtretung
- Verjährung oder Ausschlussfrist

## Interne Vorlagen

- assets/templates/masseverzeichnis.md
- assets/templates/massenachverfolgung.csv

## Amtliche Erstquellen

- §§ 80 ff. InsO
- §§ 166 ff. InsO

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `iv-massemehrung-asset-realisation`

**Frühere Beschreibung:** Verwertungsstrategie und Massemehrung entwickeln wenn Masse niedrig oder Quote ungewiss ist. §§ 159 160 InsO Verwertung § 133 InsO Vorsatzanfechtung § 15b InsO Haftungsansprüche. Prüfraster: Werthebel Assets Prozesse Anfechtung D und O Vergleichspotenzial Kosten-Nutzen. Output: Verwertungskonzept Strategiematrix Beschlussvorlage. Abgrenzung: nicht für reine Masseeinsammlung (iv-masseeinsammlung) oder Betriebsfortführung.

# Massemehrung und Verwertung

## V90 Fachkern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Massemehrung und Verwertung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Sucht über bloße Masseeinsammlung hinaus nach Werthebeln: Verwertung, Fortführung, Vergleiche, Prozesse, Prozessfinanzierung und Ansprüche.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Masse niedrig oder Quote unklar ist
- Vermögensgegenstände, Prozesse oder Ansprüche bewertet werden müssen
- Gläubigerausschuss oder Gericht eine Verwertungsstrategie braucht

## Eingaben

- Assetliste, Bewertung, Sicherheiten
- Anfechtungs- und Haftungsmatrix
- Kosten, Prozessrisiken, Kaufinteressenten

## Workflow

1. **Werthebel sammeln** - Assets, Forderungen, Anfechtung, § 15b, D&O, Versicherungen und Vergleiche kartieren.
2. **Wirtschaftlichkeit** - Bruttoerlös, Kosten, Zeit, Sicherungsrechte, Prozessrisiko und Quote schätzen.
3. **Strategie** - Verkauf, Auktion, Vergleich, Klage oder Nichtverfolgung begründen.
4. **Freigabe** - Ausschuss-, Gericht- oder Gläubigerkommunikation vorbereiten.

## Ausgabe

- Massemehrungs-Matrix
- Verwertungsvorschlag
- Kosten-Nutzen-Vermerk

## Qualitätsgates

- Sicherungsrechte abgezogen
- Kosten und Dauer ausgewiesen
- Nichtverfolgung begründet

## Rote Schwellen

- Prozesskosten ohne Deckung
- Interessenkonflikt beim Verkauf
- Vergleich ohne Massevorteil
- Ausländischer office holder will deutsches Asset verwerten, ohne Verfahrenseröffnung, Amt und konkrete Befugnis in deutscher Vollzugsform nachzuweisen
- Verwechslung von Konzernkontrolle mit Eigentum: Insolvenz der ausländischen Mutter bedeutet nicht automatisch Verfügungsbefugnis über Vermögen der deutschen Tochter

## Cross-Border-Asset-Hinweis

Bei US debtor in possession, US trustee, kanadischem trustee/monitor/receiver oder sonstigem ausländischem office holder immer `iv-cross-border-assets-trustee-registervollzug` hinzuziehen. Der Skill klärt Anerkennung, Inzidentprüfung, GmbH-Anteile, Grundbuch, Register, Nachweispaket und Masseinteresse.

## Interne Vorlagen

- assets/templates/masseverzeichnis.md
- assets/templates/verwertung-und-massemehrung.md

## Amtliche Erstquellen

- §§ 159 ff. InsO
- §§ 129 ff. InsO

## Rechtliche Grundlagen und BGH-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Insolvenzverwaltung

§ 56 InsO (Bestellung IV) → § 60 InsO (Haftung) → § 61 InsO (persoenliche Haftung Masseglaeubigeransprueche) → § 66 InsO (Rechnungslegung) → § 69 InsO (Ausschuss-Informationspflicht) → § 160 InsO (Zustimmung bei bedeutenden Massnahmen) → § 208 InsO (Masseunzulaenglichkeit) → §§ 187-216 InsO (Verteilung)

## Triage — Verfahrensstand

Bevor losgelegt wird, klaere:
1. **Verfahrensstatus?** Vorlaeufige Verwaltung (§ 22 InsO) oder Eroeffnung (§ 27 InsO)?
2. **Massedeckung?** § 54/55 InsO: Verfahrenskosten gedeckt? Masseunzulaenglichkeit § 208 droht?
3. **Zustimmungserfordernis § 160 InsO?** Handlung besonders bedeutsam → Glaeubigerausschuss oder -versammlung einbeziehen.
4. **Dokumentation vollstaendig?** Schlussrechnung § 66 InsO vorbereitet?

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
