---
name: owi-uebergang-revision-sta
description: "Owi Uebergang Strafverfahren 81 82, Revision Sta Verfahrensruegen Vorpruefung, Sicherungsverfahren 413 Stpo, Wirtschaftsstrafverfahren Datenraum Aktenplan: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Owi Uebergang Strafverfahren 81 82, Revision Sta Verfahrensruegen Vorpruefung, Sicherungsverfahren 413 Stpo, Wirtschaftsstrafverfahren Datenraum Aktenplan, Betrug Onlinehandel Beweis Und Schaden

## Arbeitsbereich

In diesem Skill wird **Owi Uebergang Strafverfahren 81 82, Revision Sta Verfahrensruegen Vorpruefung, Sicherungsverfahren 413 Stpo, Wirtschaftsstrafverfahren Datenraum Aktenplan, Betrug Onlinehandel Beweis Und Schaden** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `owi-uebergang-strafverfahren-81-82` | Übergang zwischen Bußgeld- und Strafverfahren: Hinweis, Rollenwechsel und keine Verfahrensfalle: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene. |
| `revision-sta-verfahrensruegen-vorpruefung` | Revision der Staatsanwaltschaft: Vorprüfung: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `sicherungsverfahren-413-stpo` | Sicherungsverfahren und Maßregelantrag: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `wirtschaftsstrafverfahren-datenraum-aktenplan` | Wirtschaftsstrafverfahren: Aktenplan und Datenraum: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |
| `betrug-onlinehandel-beweis-und-schaden` | Betrug im Onlinehandel: Beweis, Schaden, Einstellungs- oder Anklagereife: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt. |

## Arbeitsweg

Für **Owi Uebergang Strafverfahren 81 82, Revision Sta Verfahrensruegen Vorpruefung, Sicherungsverfahren 413 Stpo, Wirtschaftsstrafverfahren Datenraum Aktenplan, Betrug Onlinehandel Beweis Und Schaden** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `staatsanwaltschaft-praxis-einstieg` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `owi-uebergang-strafverfahren-81-82`

**Fokus:** Übergang zwischen Bußgeld- und Strafverfahren: Hinweis, Rollenwechsel und keine Verfahrensfalle: OWiG-Praxis-Skill für junge Staatsanwältinnen und Staatsanwälte mit Zuständigkeitscheck, Bußgeldbescheid/Einspruch, gerichtlichem Verfahren, Sitzungsdienst und Quellenhygiene.

# Übergang zwischen Bußgeld- und Strafverfahren: Hinweis, Rollenwechsel und keine Verfahrensfalle

## Fachkern: Übergang zwischen Bußgeld- und Strafverfahren: Hinweis, Rollenwechsel und keine Verfahrensfalle
- **Spezialgegenstand:** Übergang zwischen Bußgeld- und Strafverfahren: Hinweis, Rollenwechsel und keine Verfahrensfalle wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Staatsanwaltschaft Praxis-Einstieg**, wenn eine Akte nicht als klassische Strafsache, sondern als Ordnungswidrigkeit oder gerichtliches Bußgeldverfahren läuft. Arbeite rollenrein: Verwaltungsbehörde, Staatsanwaltschaft, Gericht, Betroffener und Nebenbeteiligte nicht vermischen.

## Einstieg

1. Verfahrensart klären: Strafverfahren, reine OWi-Sache, Mischfall oder Übergang zwischen beiden.
2. Zuständigkeit klären: Verwaltungsbehörde, Staatsanwaltschaft, Amtsgericht, Jugendrichter, Landgericht bei Datenschutz-Sonderfall oder Rechtsbeschwerdegericht.
3. Verfahrensstand markieren: Anhörung, Bußgeldbescheid, Einspruch, Zwischenverfahren, Vorlage, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde oder Vollstreckung.
4. Akte sichern: Bußgeldbescheid, Zustellungsnachweis, Einspruch, Anhörung, Mess-/Prüfunterlagen, Behördenvermerk, Beweismittel, Nebenfolgen und Fristen.
5. Sprache korrigieren: keine Anklage und kein Strafbefehl, sondern Bußgeldbescheid; im Termin keine reflexhafte Strafprozess-Rhetorik.

## Arbeitsprodukt

Gib je nach Lage einen Kurzvermerk, Verfügungsvorschlag, Nachermittlungsauftrag, Sitzungszettel, Antrag, Einstellungsvotum, Rechtsbeschwerde-Check oder Abschlussverfügung aus. Immer mit Frist, Zuständigkeit, Beweisproblem, Gegenposition und nächstem Schritt.

## Norm- und Verfahrensanker

§§ 81, 82 OWiG; § 265 StPO sinngemäß; Strafklageverbrauch und Tatidentität live prüfen.

## Fachlicher Fokus

Der Skill behandelt Mischfälle: Das Gericht ist an die OWi-Einordnung nicht gebunden, darf aber nur nach Strafgesetz entscheiden, wenn der Betroffene hingewiesen wird und Verteidigungsrechte bekommt. Umgekehrt kann im Strafverfahren eine OWi beurteilt werden. Der Skill baut eine Warnmatrix für rechtliche Gesichtspunkte.

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

## 2. `revision-sta-verfahrensruegen-vorpruefung`

**Fokus:** Revision der Staatsanwaltschaft: Vorprüfung: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Revision der Staatsanwaltschaft: Vorprüfung

## Fachkern: Revision der Staatsanwaltschaft: Vorprüfung
- **Spezialgegenstand:** Revision der Staatsanwaltschaft: Vorprüfung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Staatsanwaltschaft Praxis-Einstieg**, wenn genau diese Speziallage angesprochen ist. Fuehre die Nutzerin oder den Nutzer knapp, praktisch und beweisorientiert: erst Lage klaeren, dann Normen live pruefen, dann ein Arbeitsprodukt erzeugen.

**Fokus:** Sachrüge, Verfahrensrüge, Urteilsauswertung, Frist und Generalstaatsanwaltschaft

## Einstieg

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

## 3. `sicherungsverfahren-413-stpo`

**Fokus:** Sicherungsverfahren und Maßregelantrag: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Sicherungsverfahren und Maßregelantrag

## Fachkern: Sicherungsverfahren und Maßregelantrag
- **Spezialgegenstand:** Sicherungsverfahren und Maßregelantrag wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Staatsanwaltschaft Praxis-Einstieg**, wenn genau diese Speziallage angesprochen ist. Fuehre die Nutzerin oder den Nutzer knapp, praktisch und beweisorientiert: erst Lage klaeren, dann Normen live pruefen, dann ein Arbeitsprodukt erzeugen.

**Fokus:** Schuldunfähigkeit, Gefährlichkeit, Sachverständige und Antragsschrift

## Einstieg

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

## 4. `wirtschaftsstrafverfahren-datenraum-aktenplan`

**Fokus:** Wirtschaftsstrafverfahren: Aktenplan und Datenraum: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Wirtschaftsstrafverfahren: Aktenplan und Datenraum

## Fachkern: Wirtschaftsstrafverfahren: Aktenplan und Datenraum
- **Spezialgegenstand:** Wirtschaftsstrafverfahren: Aktenplan und Datenraum wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Staatsanwaltschaft Praxis-Einstieg**, wenn genau diese Speziallage angesprochen ist. Fuehre die Nutzerin oder den Nutzer knapp, praktisch und beweisorientiert: erst Lage klaeren, dann Normen live pruefen, dann ein Arbeitsprodukt erzeugen.

**Fokus:** Tatkomplexe, Tabellen, Vermerke, Fristen, Zuständigkeit und Abschlussverfügung

## Einstieg

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

## 5. `betrug-onlinehandel-beweis-und-schaden`

**Fokus:** Betrug im Onlinehandel: Beweis, Schaden, Einstellungs- oder Anklagereife: Praxis-Skill für neue Staatsanwältinnen und Staatsanwälte mit StPO-/RiStBV-Check, Beweislogik, Verfügungsvorschlag und nächstem Schritt.

# Betrug im Onlinehandel: Beweis, Schaden, Einstellungs- oder Anklagereife

## Fachkern: Betrug im Onlinehandel: Beweis, Schaden, Einstellungs- oder Anklagereife
- **Spezialgegenstand:** Betrug im Onlinehandel: Beweis, Schaden, Einstellungs- oder Anklagereife wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** StPO, GVG, RiStBV, OWiG, JGG, BtMG, Vermögensabschöpfung, Durchsuchung/Beschlagnahme, Abschlussverfügung und Sitzungsdienst.
- **Entscheidende Weiche:** Ordne Anfangsverdacht, Zuständigkeit, Beweisziel, Maßnahme, Grundrechtseingriff, Verwertbarkeit, Abschlussart und Hauptverhandlungsvorbereitung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Einsatz

Nutze diesen Skill im Plugin **Staatsanwaltschaft Praxis-Einstieg**, wenn genau diese Speziallage angesprochen ist. Fuehre die Nutzerin oder den Nutzer knapp, praktisch und beweisorientiert: erst Lage klaeren, dann Normen live pruefen, dann ein Arbeitsprodukt erzeugen.

**Fokus:** Onlinebetrug, Plattformdaten, Zahlungsfluss, Geschädigtenliste und Anklage-/Strafbefehlstauglichkeit

## Einstieg

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
