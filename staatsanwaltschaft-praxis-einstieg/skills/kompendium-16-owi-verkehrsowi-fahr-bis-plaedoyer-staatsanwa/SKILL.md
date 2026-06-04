---
name: kompendium-16-owi-verkehrsowi-fahr-bis-plaedoyer-staatsanwa
description: "staatsanwaltschaft-praxis-einstieg: Konsolidiertes Skill-Kompendium 16; bündelt 5 frühere Spezialskills (owi-verkehrsowi-fahrverbot-punkte, owi-vorlage-an-amtsgericht-sta-check, pflichtverteidigung-aus-sta-sicht, plaedoyer-beweiswuerdigung-strafmass, plaedoyer-staatsanwaltschaft) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 16 - staatsanwaltschaft-praxis-einstieg

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `owi-verkehrsowi-fahrverbot-punkte` | Verkehrsordnungswidrigkeiten: Fahrverbot, Punkte, Messung, Halter- und Fahrerfrage aus StA-Sicht: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene. |
| `owi-vorlage-an-amtsgericht-sta-check` | Vorlage der OWi-Akte an das Amtsgericht: Staatsanwaltschaft als Filter, nicht als Anklageschreiberin: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene. |
| `pflichtverteidigung-aus-sta-sicht` | Pflichtverteidigung aus Sicht der Staatsanwaltschaft: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `plaedoyer-beweiswuerdigung-strafmass` | Plädoyer: Beweiswürdigung und Strafmaß sauber bauen: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `plaedoyer-staatsanwaltschaft` | Plädoyer der Staatsanwaltschaft: Praxis-Skill für neue Staatsanwälte zu Schuldfrage, Beweiswürdigung, Strafzumessung, Nebenfolgen und Antrag klar und fair darstellen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `owi-verkehrsowi-fahrverbot-punkte`

**Frühere Beschreibung:** Verkehrsordnungswidrigkeiten: Fahrverbot, Punkte, Messung, Halter- und Fahrerfrage aus StA-Sicht: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene.

# Verkehrsordnungswidrigkeiten: Fahrverbot, Punkte, Messung, Halter- und Fahrerfrage aus StA-Sicht

## Fachkern: Verkehrsordnungswidrigkeiten: Fahrverbot, Punkte, Messung, Halter- und Fahrerfrage aus StA-Sicht
- **Spezialgegenstand:** Verkehrsordnungswidrigkeiten: Fahrverbot, Punkte, Messung, Halter- und Fahrerfrage aus StA-Sicht wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Staatsanwaltschaft Praxis-Einstieg**, wenn eine Akte nicht als klassische Strafsache, sondern als Ordnungswidrigkeit oder gerichtliches Bußgeldverfahren läuft. Arbeite rollenrein: Verwaltungsbehörde, Staatsanwaltschaft, Gericht, Betroffener und Nebenbeteiligte nicht vermischen.

## Kaltstart

1. Verfahrensart klären: Strafverfahren, reine OWi-Sache, Mischfall oder Übergang zwischen beiden.
2. Zuständigkeit klären: Verwaltungsbehörde, Staatsanwaltschaft, Amtsgericht, Jugendrichter, Landgericht bei Datenschutz-Sonderfall oder Rechtsbeschwerdegericht.
3. Verfahrensstand markieren: Anhörung, Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde oder Vollstreckung.
4. Akte sichern: Bußgeldbescheid, Zustellungsnachweis, Einspruch, Anhörung, Mess-/Prüfunterlagen, Behördenvermerk, Beweismittel, Nebenfolgen und Fristen.
5. Sprache korrigieren: keine Anklage und kein Strafbefehl, sondern Bußgeldbescheid; im Termin keine reflexhafte Strafprozess-Rhetorik.

## Arbeitsprodukt

Gib je nach Lage einen Kurzvermerk, Verfügungsvorschlag, Nachermittlungsauftrag, Sitzungszettel, Antrag, Einstellungsvotum, Rechtsbeschwerde-Check oder Abschlussverfügung aus. Immer mit Frist, Zuständigkeit, Beweisproblem, Gegenposition und nächstem Schritt.

## Norm- und Verfahrensanker

StVG, StVO, BKatV, FeV; §§ 65 ff., 79, 80 OWiG; Spezialverjährung live prüfen.

## Fachlicher Fokus

Der Skill hilft im Termin und bei Vorlagen in Verkehrs-OWi: Messverfahren, Eichung, Fahreridentifizierung, Vorsatz/Fahrlässigkeit, Regelfahrverbot, Absehen gegen Erhöhung der Geldbuße und Rechtsbeschwerderisiko.

## Prüfschritte

- Was ist der konkrete Tatvorwurf und welche Bußgeldnorm trägt ihn wirklich?
- Ist der Bußgeldbescheid inhaltlich und zustellungstechnisch belastbar?
- Ist der Einspruch wirksam, beschränkt oder unklar?
- Fehlen Ermittlungen, Behördenauskünfte, Messunterlagen oder Anhörungen?
- Ist eine Einstellung nach § 47 OWiG sachgerecht oder braucht es eine gerichtliche Klärung?
- Muss die Staatsanwaltschaft am Termin teilnehmen, schriftlich Stellung nehmen oder reicht die Vorlage?

## Typische Fehler

- Bußgeldverfahren wie eine kleine Strafsache behandeln und die Opportunitätslogik übersehen.
- Die Verwaltungsbehörde als bloße Aktenlieferantin behandeln, obwohl sie oft die Sachkunde trägt.
- Fristen und Zustellungen unterschätzen, weil die Sache vermeintlich klein ist.
- Datenschutz- oder Unternehmensbußgelder ohne Spezialverweisung prüfen.
- Im Termin nicht klar sagen können, ob Einstellung, Aufrechterhaltung, Herabsetzung oder Rechtsbeschwerde die richtige Linie ist.

## Quellenhygiene

Normen zuerst amtlich prüfen: OWiG auf gesetze-im-internet.de, Spezialgesetz, RiStBV und bei Datenschutz Art. 83 DSGVO sowie § 41 BDSG. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle verwenden; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 2. `owi-vorlage-an-amtsgericht-sta-check`

**Frühere Beschreibung:** Vorlage der OWi-Akte an das Amtsgericht: Staatsanwaltschaft als Filter, nicht als Anklageschreiberin: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene.

# Vorlage der OWi-Akte an das Amtsgericht: Staatsanwaltschaft als Filter, nicht als Anklageschreiberin

## Fachkern: Vorlage der OWi-Akte an das Amtsgericht: Staatsanwaltschaft als Filter, nicht als Anklageschreiberin
- **Spezialgegenstand:** Vorlage der OWi-Akte an das Amtsgericht: Staatsanwaltschaft als Filter, nicht als Anklageschreiberin wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Staatsanwaltschaft Praxis-Einstieg**, wenn eine Akte nicht als klassische Strafsache, sondern als Ordnungswidrigkeit oder gerichtliches Bußgeldverfahren läuft. Arbeite rollenrein: Verwaltungsbehörde, Staatsanwaltschaft, Gericht, Betroffener und Nebenbeteiligte nicht vermischen.

## Kaltstart

1. Verfahrensart klären: Strafverfahren, reine OWi-Sache, Mischfall oder Übergang zwischen beiden.
2. Zuständigkeit klären: Verwaltungsbehörde, Staatsanwaltschaft, Amtsgericht, Jugendrichter, Landgericht bei Datenschutz-Sonderfall oder Rechtsbeschwerdegericht.
3. Verfahrensstand markieren: Anhörung, Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde oder Vollstreckung.
4. Akte sichern: Bußgeldbescheid, Zustellungsnachweis, Einspruch, Anhörung, Mess-/Prüfunterlagen, Behördenvermerk, Beweismittel, Nebenfolgen und Fristen.
5. Sprache korrigieren: keine Anklage und kein Strafbefehl, sondern Bußgeldbescheid; im Termin keine reflexhafte Strafprozess-Rhetorik.

## Arbeitsprodukt

Gib je nach Lage einen Kurzvermerk, Verfügungsvorschlag, Nachermittlungsauftrag, Sitzungszettel, Antrag, Einstellungsvotum, Rechtsbeschwerde-Check oder Abschlussverfügung aus. Immer mit Frist, Zuständigkeit, Beweisproblem, Gegenposition und nächstem Schritt.

## Norm- und Verfahrensanker

§§ 68, 69, 71, 75 OWiG; § 46 OWiG; GVG/StPO sinngemäß.

## Fachlicher Fokus

Dieser Skill baut den Prüfvermerk, bevor eine Bußgeldakte ans Gericht weitergeht: zuständiges Amtsgericht, Vollständigkeit der Akte, Zustellung, Einspruch, Beweismittel, Verjährung, erkennbare Einstellungsgründe, erforderliche Nachermittlung und ob eine Teilnahme der Staatsanwaltschaft am Termin sinnvoll ist.

## Prüfschritte

- Was ist der konkrete Tatvorwurf und welche Bußgeldnorm trägt ihn wirklich?
- Ist der Bußgeldbescheid inhaltlich und zustellungstechnisch belastbar?
- Ist der Einspruch wirksam, beschränkt oder unklar?
- Fehlen Ermittlungen, Behördenauskünfte, Messunterlagen oder Anhörungen?
- Ist eine Einstellung nach § 47 OWiG sachgerecht oder braucht es eine gerichtliche Klärung?
- Muss die Staatsanwaltschaft am Termin teilnehmen, schriftlich Stellung nehmen oder reicht die Vorlage?

## Typische Fehler

- Bußgeldverfahren wie eine kleine Strafsache behandeln und die Opportunitätslogik übersehen.
- Die Verwaltungsbehörde als bloße Aktenlieferantin behandeln, obwohl sie oft die Sachkunde trägt.
- Fristen und Zustellungen unterschätzen, weil die Sache vermeintlich klein ist.
- Datenschutz- oder Unternehmensbußgelder ohne Spezialverweisung prüfen.
- Im Termin nicht klar sagen können, ob Einstellung, Aufrechterhaltung, Herabsetzung oder Rechtsbeschwerde die richtige Linie ist.

## Quellenhygiene

Normen zuerst amtlich prüfen: OWiG auf gesetze-im-internet.de, Spezialgesetz, RiStBV und bei Datenschutz Art. 83 DSGVO sowie § 41 BDSG. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle verwenden; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## 3. `pflichtverteidigung-aus-sta-sicht`

**Frühere Beschreibung:** Pflichtverteidigung aus Sicht der Staatsanwaltschaft: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Pflichtverteidigung aus Sicht der Staatsanwaltschaft

## Fachkern: Pflichtverteidigung aus Sicht der Staatsanwaltschaft
- **Spezialgegenstand:** Pflichtverteidigung aus Sicht der Staatsanwaltschaft wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Staatsanwaltschaft Praxis-Einstieg**, wenn genau diese Speziallage angesprochen ist. Fuehre die Nutzerin oder den Nutzer knapp, praktisch und beweisorientiert: erst Lage klaeren, dann Normen live pruefen, dann ein Arbeitsprodukt erzeugen.

**Fokus:** § 140 StPO, notwendige Verteidigung, Beiordnung, Beschleunigung und Rechtsmittelrisiko

## Kaltstart

1. Rolle, Ziel und Entscheidungsdruck klaeren.
2. Verfahrensstand, Fristen, Zuständigkeit und irreversible Risiken markieren.
3. Aktenbasis ordnen: sichere Tatsachen, bestrittene Tatsachen, fehlende Unterlagen.
4. Eingriffsintensität, Berufs-/Amtsgeheimnisse, Datenschutz und Persönlichkeitsrechte sichtbar machen.
5. Sofortpfad anbieten: Was muss heute entschieden, beantragt, beantwortet oder dokumentiert werden?

## Prüfprogramm

- **Normenanker:** StPO, StGB, GVG, RiStBV, JGG, OWiG, Nebenstrafrecht und einschlägige Landesvorgaben live prüfen
- **Tatsachenarbeit:** Beweisquelle, Beweiswert, Gegenbeweis, Dokumentationslücke und mögliche Fehlinterpretation trennen.
- **Verfahrensarbeit:** Form, Frist, Zuständigkeit, Anhörung, Akteneinsicht, Rechtsbehelf und Zustellungsweg prüfen.
- **Gegenposition:** Die stärkste Gegenansicht formulieren und sagen, was sie praktisch bedeutet.
- **Entscheidung:** Eine vertretbare Handlungsempfehlung mit Risikoampel und nächstem Schritt liefern.

## Spezielle Leitplanken

- Keine echten Aktengeheimnisse oder personenbezogenen Daten in ungeprüfte Systeme eingeben.
- Entlastende Umstände aktiv mitdenken; die Staatsanwaltschaft ist nicht Parteivertreterin.
- Bei Grundrechtseingriffen Verhältnismäßigkeit und Richtervorbehalt zuerst prüfen.

## Output

Erzeuge je nach Auftrag Vermerk, Ermittlungsauftrag, Verfügung, Anklagebaustein, Strafbefehlsantrag, Sitzungsnotiz oder Plädoyerbaustein.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei unsicherer oder neuer Rechtslage ausdrücklich sagen, was live nachzusehen ist und welche Quelle dafür zuerst aufgerufen werden soll.

## 4. `plaedoyer-beweiswuerdigung-strafmass`

**Frühere Beschreibung:** Plädoyer: Beweiswürdigung und Strafmaß sauber bauen: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Plädoyer: Beweiswürdigung und Strafmaß sauber bauen

## Fachkern: Plädoyer: Beweiswürdigung und Strafmaß sauber bauen
- **Spezialgegenstand:** Plädoyer: Beweiswürdigung und Strafmaß sauber bauen wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Staatsanwaltschaft Praxis-Einstieg**, wenn genau diese Speziallage angesprochen ist. Fuehre die Nutzerin oder den Nutzer knapp, praktisch und beweisorientiert: erst Lage klaeren, dann Normen live pruefen, dann ein Arbeitsprodukt erzeugen.

**Fokus:** Tatnachweis, Zweifel, Strafzumessung, Nebenfolgen und faire Sprache

## Kaltstart

1. Rolle, Ziel und Entscheidungsdruck klaeren.
2. Verfahrensstand, Fristen, Zuständigkeit und irreversible Risiken markieren.
3. Aktenbasis ordnen: sichere Tatsachen, bestrittene Tatsachen, fehlende Unterlagen.
4. Eingriffsintensität, Berufs-/Amtsgeheimnisse, Datenschutz und Persönlichkeitsrechte sichtbar machen.
5. Sofortpfad anbieten: Was muss heute entschieden, beantragt, beantwortet oder dokumentiert werden?

## Prüfprogramm

- **Normenanker:** StPO, StGB, GVG, RiStBV, JGG, OWiG, Nebenstrafrecht und einschlägige Landesvorgaben live prüfen
- **Tatsachenarbeit:** Beweisquelle, Beweiswert, Gegenbeweis, Dokumentationslücke und mögliche Fehlinterpretation trennen.
- **Verfahrensarbeit:** Form, Frist, Zuständigkeit, Anhörung, Akteneinsicht, Rechtsbehelf und Zustellungsweg prüfen.
- **Gegenposition:** Die stärkste Gegenansicht formulieren und sagen, was sie praktisch bedeutet.
- **Entscheidung:** Eine vertretbare Handlungsempfehlung mit Risikoampel und nächstem Schritt liefern.

## Spezielle Leitplanken

- Keine echten Aktengeheimnisse oder personenbezogenen Daten in ungeprüfte Systeme eingeben.
- Entlastende Umstände aktiv mitdenken; die Staatsanwaltschaft ist nicht Parteivertreterin.
- Bei Grundrechtseingriffen Verhältnismäßigkeit und Richtervorbehalt zuerst prüfen.

## Output

Erzeuge je nach Auftrag Vermerk, Ermittlungsauftrag, Verfügung, Anklagebaustein, Strafbefehlsantrag, Sitzungsnotiz oder Plädoyerbaustein.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei unsicherer oder neuer Rechtslage ausdrücklich sagen, was live nachzusehen ist und welche Quelle dafür zuerst aufgerufen werden soll.

## 5. `plaedoyer-staatsanwaltschaft`

**Frühere Beschreibung:** Plädoyer der Staatsanwaltschaft: Praxis-Skill für neue Staatsanwälte zu Schuldfrage, Beweiswürdigung, Strafzumessung, Nebenfolgen und Antrag klar und fair darstellen; mit Datenschutz-/Aktengeheimniswarnung, RiStBV-/StPO-Quellencheck, Verfügungsvorschlag und nächstem Schritt.

# Plädoyer der Staatsanwaltschaft

## Fachkern: Plädoyer der Staatsanwaltschaft
- **Spezialgegenstand:** Plädoyer der Staatsanwaltschaft wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Staatsanwaltschaft Praxis-Einstieg**, wenn die Akte, der Nutzer oder der Kaltstart auf dieses Thema zeigt. Arbeite nicht wie ein Lehrbuch, sondern wie ein sorgfältiger Praxisbegleiter: erst ordnen, dann prüfen, dann ein verwertbares Arbeitsprodukt liefern.

**Fokus:** Schuldfrage, Beweiswürdigung, Strafzumessung, Nebenfolgen und Antrag klar und fair darstellen

## Kaltstart in fünf Schritten

1. Rolle und Ziel klären: Wer handelt, wer ist betroffen, welches Ergebnis wird gebraucht?
2. Frist, Zuständigkeit, Verfahrensstand und irreversible Risiken markieren.
3. Vorliegende Dokumente, Beweise, Zahlen, Aktenzeichen, Bescheide oder Beschlüsse erfassen.
4. Unsichere Tatsachen als offen markieren und nicht durch Modellwissen ersetzen.
5. Einen Minimalpfad anbieten: Was muss heute passieren, was kann später vertieft werden?

## Prüf- und Arbeitslogik

- **Normenanker:** StPO, StGB, GVG, RiStBV, JGG, OWiG, einschlägiges Nebenstrafrecht und landesrechtliche Verwaltungsvorschriften live prüfen
- **Tatsachenarbeit:** sichere Tatsachen, streitige Tatsachen, fehlende Unterlagen und Beweisprobleme trennen.
- **Verfahrensarbeit:** Zuständigkeit, Form, Frist, Anhörung, Akteneinsicht, Dokumentationspflicht und Rechtsbehelf prüfen.
- **Gegenansicht:** eine ernsthafte Gegenposition formulieren und sagen, wie man sie entkräftet oder akzeptiert.
- **Praxisentscheidung:** nicht nur prüfen, sondern eine handhabbare nächste Handlung vorschlagen.


## Spezielle Leitplanken

- Keine echten Aktengeheimnisse oder personenbezogenen Daten in ungeprüfte Systeme eingeben.
- Entlastende Umstände aktiv mitdenken; die Staatsanwaltschaft ist nicht Parteivertreterin.
- Bei Grundrechtseingriffen Verhältnismäßigkeit und Richtervorbehalt zuerst prüfen.

## Output

Erzeuge je nach Auftrag: Verfügung, Ermittlungsauftrag, Vermerk, Anklagebaustein, Strafbefehlsantrag, Sitzungsnotiz oder Plädoyerbaustein. Am Ende immer: Risikoampel, offene Punkte, Quellencheck und nächster Schritt.

## Quellenhygiene

Keine erfundenen Fundstellen. Rechtsprechung nur mit Gericht, Entscheidungsdatum, Aktenzeichen und frei oder amtlich prüfbarer Quelle. Bei aktuellem Behörden-, Kammer-, Berufs- oder Wettbewerbsrecht zuerst die amtliche Normfassung und die zuständige Behörden- oder Kammerseite prüfen.
