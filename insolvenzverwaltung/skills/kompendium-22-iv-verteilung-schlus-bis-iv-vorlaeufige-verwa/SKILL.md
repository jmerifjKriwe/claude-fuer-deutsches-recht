---
name: kompendium-22-iv-verteilung-schlus-bis-iv-vorlaeufige-verwa
description: "insolvenzverwaltung: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (iv-verteilung-schlussrechnung, iv-vorlaeufige-verwaltung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 22 - insolvenzverwaltung

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `iv-verteilung-schlussrechnung` | Abschlussphase des Insolvenzverfahrens durchführen: Schlussrechnung Schlussbericht Verteilungsverzeichnis Quote Nachtragsverteilung. §§ 196 197 InsO Schlussverteilung §§ 66 67 InsO Schlussrechnung. Prüfraster: Abschlussreife Massekonto Kosten Vergutung Rangklassen Quote Nachtragsrisiken. Output: Schlussrechnung Schlussbericht Verteilungsverzeichnis. Abgrenzung: nicht für laufende Berichte (iv-berichte-gericht-gläubiger). |
| `iv-vorlaeufige-verwaltung` | Erste Massnahmen als vorlaeufliger Insolvenzverwalter nach § 21 InsO umsetzen: Bankkonten Besitz Post Drittschuldner Betrieb. § 21 InsO Sicherungsmassnahmen § 22 InsO Pflichten des vorl. Verwalters. Prüfraster: Beschlussumfang Zustimmungsvorbehalt Postsperre Bankensicherung Drittschuldneranschreiben Kommunikation. Output: Tagesplan Sicherungsprotokoll Kommunikationsschreiben. Abgrenzung: nicht für laufendes Regelverfahren (iv-regelverfahren-eroeffnung). |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `iv-verteilung-schlussrechnung`

**Frühere Beschreibung:** Abschlussphase des Insolvenzverfahrens durchführen: Schlussrechnung Schlussbericht Verteilungsverzeichnis Quote Nachtragsverteilung. §§ 196 197 InsO Schlussverteilung §§ 66 67 InsO Schlussrechnung. Prüfraster: Abschlussreife Massekonto Kosten Vergutung Rangklassen Quote Nachtragsrisiken. Output: Schlussrechnung Schlussbericht Verteilungsverzeichnis. Abgrenzung: nicht für laufende Berichte (iv-berichte-gericht-gläubiger).

# Schlussbericht, Schlussrechnung und Verteilung

## V90 Fachkern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Schlussbericht, Schlussrechnung und Verteilung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Führt die Abschlussphase des Verfahrens: Schlussbericht, Schlussrechnung, Verteilungsverzeichnis, Quote und Nachtragsverteilung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Verwertung abgeschlossen oder weitgehend abgeschlossen ist
- Schlussverteilung vorbereitet wird
- Gericht Schlussbericht oder Schlussrechnung erwartet

## Eingaben

- Massekonto, Buchhaltung, Verwertungserlöse
- Tabelle, Rangklassen, Kosten, Vergütung
- offene Prozesse und Nachtragsrisiken

## Workflow

1. **Abschlussreife** - offene Masse, Prozesse, Steuern und Verwertung prüfen.
2. **Rechnung** - Einnahmen, Ausgaben, Kosten, Vergütung und Belege konsolidieren.
3. **Verteilung** - Rang, Quote, Abschläge und Verteilungsverzeichnis erstellen.
4. **Bericht** - Schlussbericht, Anlagenliste und Nachtragsverteilungsnotiz ausgeben.

## Ausgabe

- Schlussbericht
- Schlussrechnung
- Verteilungsverzeichnis

## Qualitätsgates

- Massekonto stimmt mit Buchhaltung
- Tabelle final geprüft
- Nachtragspositionen markiert

## Rote Schwellen

- offener Prozess mit Quotenwirkung
- nicht gebuchte Kosten
- Rangfehler

## Interne Vorlagen

- assets/templates/schlussbericht-schlussrechnung.md
- assets/templates/verteilungsverzeichnis.md

## Amtliche Erstquellen

- §§ 187 ff. InsO
- §§ 196 ff. InsO

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

## 2. `iv-vorlaeufige-verwaltung`

**Frühere Beschreibung:** Erste Massnahmen als vorlaeufliger Insolvenzverwalter nach § 21 InsO umsetzen: Bankkonten Besitz Post Drittschuldner Betrieb. § 21 InsO Sicherungsmassnahmen § 22 InsO Pflichten des vorl. Verwalters. Prüfraster: Beschlussumfang Zustimmungsvorbehalt Postsperre Bankensicherung Drittschuldneranschreiben Kommunikation. Output: Tagesplan Sicherungsprotokoll Kommunikationsschreiben. Abgrenzung: nicht für laufendes Regelverfahren (iv-regelverfahren-eroeffnung).

# Vorläufige Insolvenzverwaltung

## V90 Fachkern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vorläufige Insolvenzverwaltung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Aufgabe

Führt die ersten Tage nach Bestellung als vorläufiger Insolvenzverwalter mit Zustimmungsvorbehalt oder starker Verwaltung.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Beschluss nach § 21 InsO vorliegt
- Banken, Kasse, Post und Drittschuldner sofort gesichert werden müssen
- der Betrieb bis zur Entscheidung fortgeführt wird

## Eingaben

- Sicherungsbeschluss
- Bank- und Kassenstände
- Debitoren, Kreditoren, Arbeitnehmer, Lieferanten

## Workflow

1. **Befugnisse lesen** - Beschlussumfang, Zustimmungsvorbehalt, Postsperre und Verfügungsverbote auswerten.
2. **Masse sichern** - Banken, Kasse, Forderungen, Warenlager und Schlüssel kontrollieren.
3. **Kommunikation** - Schuldner, Banken, Drittschuldner, Arbeitnehmer und Gericht informieren.
4. **Tagessteuerung** - Zahlungen nur nach Freigabe, Beleg und Masseinteresse dokumentieren.

## Ausgabe

- Sofortmaßnahmenliste
- Bank- und Kassenprotokoll
- Zahlungsfreigabeprotokoll

## Qualitätsgates

- Beschlussbefugnisse werden wörtlich beachtet
- jede Zahlung hat Zweck, Beleg und Freigabe
- Drittschuldner sind informiert

## Rote Schwellen

- Zahlungen außerhalb des Freigabeprozesses
- fehlender Kassensturz
- unklare Eigentums- oder Sicherungsrechte

## Interne Vorlagen

- assets/templates/vorlaeufige-verwaltung-checkliste.md
- assets/templates/zahlungslauf-freigabe.md

## Amtliche Erstquellen

- § 21 InsO
- § 22 InsO

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
