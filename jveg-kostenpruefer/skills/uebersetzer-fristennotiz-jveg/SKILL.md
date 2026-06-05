---
name: uebersetzer-fristennotiz-jveg
description: "Nutze dies, wenn Spezial Uebersetzer Fristennotiz Und Naechster Schritt, Jveg Sachverstaendigenrechnung Bauleiter, Jveg Aktenstripper im Plugin Jveg Kostenpruefer konkret bearbeitet werden soll. Auslöser: Bitte Spezial Uebersetzer Fristennotiz Und Naechster Schritt, Jveg Sachverstaendigenrechnung Bauleiter, Jveg Aktenstripper prüfen.; Erstelle eine Arbeitsfassung zu Spezial Uebersetzer Fristennotiz Und Naechster Schritt, Jveg Sachverstaendigenrechnung Bauleiter, Jveg Aktenstripper.; Welche Normen und Nachweise brauche ich?."
---

# Spezial Uebersetzer Fristennotiz Und Naechster Schritt, Jveg Sachverstaendigenrechnung Bauleiter, Jveg Aktenstripper

## Zweck

Dieser Skill ist ein eigenständiger Arbeitsbereich. Er verbindet mehrere sachlich benachbarte Arbeitsmodule. Wähle anhand des Sachverhalts das passende Modul, arbeite dessen Prüfroutine vollständig ab und kombiniere Module nur, wenn der Fall tatsächlich mehrere Themen berührt.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `spezial-uebersetzer-fristennotiz-und-naechster-schritt` | Uebersetzer: Fristennotiz und nächster Schritt im Plugin jveg kostenpruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `jveg-sachverstaendigenrechnung-bauleiter` | Bauleiter Sachverstaendigenrechnung JVEG: Honorargruppen, Zeitaufwand, Auslagen, Mehrwertsteuer. Pruefraster Sachverstaendiger und Kostenfestsetzung. |
| `jveg-aktenstripper` | JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren: Termine, Stunden, Auslagen. Normen: §§ 2 ff. JVEG. Prüfraster: Terminsprotokoll, Stundennachweis, Belegstruktur. Output: Extrahierter Datensatz für Kostenprüfung. Abgrenzung: nicht Kostenberechnung. |

## Arbeitsweg

Für **Spezial Uebersetzer Fristennotiz Und Naechster Schritt, Jveg Sachverstaendigenrechnung Bauleiter, Jveg Aktenstripper** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `jveg-kostenpruefer` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `spezial-uebersetzer-fristennotiz-und-naechster-schritt`

**Fokus:** Uebersetzer: Fristennotiz und nächster Schritt im Plugin jveg kostenpruefer; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Uebersetzer: Fristennotiz und nächster Schritt

## Fachkern: Uebersetzer: Fristennotiz und nächster Schritt
- **Spezialgegenstand:** Uebersetzer: Fristennotiz und nächster Schritt wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Uebersetzer** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 2. `jveg-sachverstaendigenrechnung-bauleiter`

**Fokus:** Bauleiter Sachverstaendigenrechnung JVEG: Honorargruppen, Zeitaufwand, Auslagen, Mehrwertsteuer. Pruefraster Sachverstaendiger und Kostenfestsetzung.

# JVEG: Sachverstaendigenrechnung

## Fachkern: JVEG: Sachverstaendigenrechnung
- **Spezialgegenstand:** JVEG: Sachverstaendigenrechnung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Vertraege, Auszuege liegen vor?
5. **Format:** Wie ausfuehrlich, fuer wen, in welcher Tonalitaet?

## Pruefraster

Der Output muss als verwertbares Arbeitsprodukt aufgebaut sein:

1. **Sachverhalt fixieren** - streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieser Skill gehoert zum Plugin `jveg-kostenpruefer`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `jveg-aktenstripper`

**Fokus:** JVEG-relevante Daten aus Gerichtsakten und Gutachterunterlagen extrahieren: Termine, Stunden, Auslagen. Normen: §§ 2 ff. JVEG. Prüfraster: Terminsprotokoll, Stundennachweis, Belegstruktur. Output: Extrahierter Datensatz für Kostenprüfung. Abgrenzung: nicht Kostenberechnung.

# JVEG-Aktenstripper

## Fachkern: JVEG-Aktenstripper
- **Spezialgegenstand:** JVEG-Aktenstripper wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** JVEG, GKG/KostR-Schnittstellen, Festsetzungsverfahren, Beschwerde, Vorschuss, Entschädigung, Sachverständigenvergütung und Belegpflicht.
- **Entscheidende Weiche:** Trenne Rolle Zeuge/Sachverständiger/Dolmetscher, Zeitaufwand, Auslagen, Verdienstausfall, Vorschuss, Frist und Belegwert.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Aufgabe
Extrahiere alle vergütungsrelevanten Daten aus Gerichtsschreiben, Anträgen, Rechnungen und Belegen und überführe sie in eine strukturierte, prüfbare JVEG-Datenmatrix.

## Triage — kläre vor dem Ausstreifen

1. **Dokumenttyp:** Liegt eine Rechnung, ein Kostenfestsetzungsantrag, ein Gerichtsschreiben oder ein Vorschussantrag vor?
2. **Anspruchsberechtigter:** Sachverständiger, Zeuge, Dolmetscher, Übersetzer oder ehrenamtlicher Richter?
3. **Verfahren:** In welchem Gericht und welchem Aktenzeichen ist der Anspruch entstanden?
4. **Beleglage:** Welche Belege (Fahrtkosten, Übernachtung, Quittungen) liegen im Original vor?
5. **Fristen:** Wurde die Dreimonatsfrist des § 23 JVEG bereits gewahrt oder droht Erlöschen?

## Zentrale Normen
- § 1 JVEG (Anwendungsbereich)
- § 2 JVEG (Anspruchsberechtigte)
- § 3 JVEG (Vorschuss)
- § 23 JVEG (Dreimonatsfrist / Erlöschen)
- §§ 5–7 JVEG (Fahrtkosten)
- §§ 8–10 JVEG (Sachverständige)
- §§ 13–16 JVEG (Dolmetscher/Übersetzer)
- §§ 19–22 JVEG (Zeugen)

## Rechtsprechung
1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
3. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
4. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Startet bei
Erhalt von Gerichtsschreiben, Rechnung oder Antrag im JVEG-Kontext.

## Arbeitsweise
1. Dokumententyp bestimmen und Anspruchsberechtigten identifizieren.
2. Alle Positionen mit Betrag, Norm und Beleg in die Matrix einlesen.
3. Fristen prüfen (§ 23 JVEG).
4. Vollständigkeitscheck: fehlende Belege markieren.
5. Matrix an nachgelagerte Prüf-Skills übergeben.

## Output-Template

| Position | Betrag (EUR) | Norm | Beleg | Status |
|---|---|---|---|---|
| Fahrtkosten | 00,00 | § 5 JVEG | Quittung | offen |
| Zeitversäumnis | 00,00 | § 22 JVEG | — | offen |
| Übernachtung | 00,00 | § 7 JVEG | Hotelrechnung | offen |
| **Summe** | **00,00** | | | |

**Offene Belege:** [Liste]
**Fristenstatus § 23 JVEG:** [Datum Leistungserbringung / Fristende]

## Ausgabe
Strukturierte JVEG-Datenmatrix; jede Position mit Norm, Betrag und Belegnummer.

## Leitplanken
- Keine Rechtsberatung; Prüfung auf Plausibilität und Normkonformität.
- Beträge werden nicht gerundet; Originalwerte aus Dokumenten übernehmen.
- Hinweis: Keine Rechtsberatung. Ausgaben dienen der internen Arbeitsvorbereitung.
