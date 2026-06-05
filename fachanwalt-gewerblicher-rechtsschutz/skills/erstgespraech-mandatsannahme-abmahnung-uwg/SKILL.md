---
name: erstgespraech-mandatsannahme-abmahnung-uwg
description: "Erstgespraech Mandatsannahme Abmahnung UWG im Plugin Fachanwalt Gewerblicher Rechtsschutz: prüft konkret Erstgespraech im gewerblichen Rechtsschutz strukturieren, UWG-Abmahnung prüfen versenden oder auf Eingang reagieren, Abmahnung oder Vergleich bei Domainnamen-Streit und. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Erstgespraech Mandatsannahme Abmahnung UWG

## Arbeitsbereich

**Erstgespraech Mandatsannahme Abmahnung UWG** ordnet den Fall über die tragenden Prüffelder: Erstgespraech im gewerblichen Rechtsschutz strukturieren, UWG-Abmahnung prüfen versenden oder auf Eingang reagieren, Abmahnung oder Vergleich bei Domainnamen-Streit und. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `erstgespraech-mandatsannahme` | Erstgespraech im gewerblichen Rechtsschutz strukturieren und Mandat aufnehmen. § 14 MarkenG § 139 PatG § 8 UWG § 43a BRAO. Prüfraster: Schutzrecht Verletzungshandlung Parteistellung Eilbedürfnis Fristen. Output: Mandat-Steckbrief Sachverhaltsprotokoll fehlende Unterlagen. Abgrenzung: Einstiegs-Skill; Detailarbeit in Spezialist-Skills. |
| `fachanwalt-gewerblicher-rechtsschutz-abmahnung-uwg` | UWG-Abmahnung prüfen versenden oder auf Eingang reagieren. § 8 UWG Unterlassungsanspruch §§ 3 4 5 UWG Verbotsgrunde §§ 12 13 UWG Durchsetzung. Prüfraster: Verletzungshandlung Abmahnberechtigung Fristen UE Vertragsstrafe Kosten. Output: Abmahnschreiben oder Erwiderung modifizierte UE Kostennote. Abgrenzung: nicht für Markenrecht (fachanwalt-gewerblicher-rechtsschutz-markenanmeldung). |
| `fachanwalt-gewerblicher-rechtsschutz-abmahnung-vergleich-wipo` | Abmahnung oder Vergleich bei Domainnamen-Streit und WIPO-Schiedsverfahren vorbereiten. UDRP WIPO-Schiedsregeln § 14 MarkenG Markenrecht. Prüfraster: Domain-Name Verwechslungsgefahr Boese-Glauben-Registrierung Schiedsstellenzuständigkeit Transferantrag. Output: WIPO-Beschwerde oder Verteidigung Vergleichsangebot. Abgrenzung: nicht für Markenrecht vor EUIPO oder DPMA. |

## Arbeitsweg

- Rolle und Ziel im Plugin Fachanwalt für gewerblichen Rechtsschutz nach FAO § 14k klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `erstgespraech-mandatsannahme`

**Fokus:** Erstgespraech im gewerblichen Rechtsschutz strukturieren und Mandat aufnehmen. § 14 MarkenG § 139 PatG § 8 UWG § 43a BRAO. Prüfraster: Schutzrecht Verletzungshandlung Parteistellung Eilbedürfnis Fristen. Output: Mandat-Steckbrief Sachverhaltsprotokoll fehlende Unterlagen. Abgrenzung: Einstiegs-Skill; Detailarbeit in Spezialist-Skills.

# Erstgespraech und Mandatsannahme im Marken-, Patent-, Design- und Wettbewerbsrecht

## Triage zu Beginn — klaere vor jedem weiteren Schritt

1. Liegt eine **Abmahnung, einstweilige Verfuegung oder Fristmitteilung** vor? Wenn ja: Datum feststellen und sofort Kalender-Alarm setzen.
2. Welches **Schutzrecht** ist betroffen: Marke (MarkenG), Design (DesignG), Patent (PatG), Gebrauchsmuster (GebrMG) oder lauterkeitsrechtlicher Anspruch (UWG)?
3. Sind **mehrere Parteien** am Sachverhalt beteiligt, fuer die ein Interessenkonflikt bestehen koennte (§ 43a Abs. 4 BRAO, § 3 BORA)?
4. Ist der Mandant eine **juristische Person** → Handelsregister, Transparenzregister, wirtschaftlich Berechtigte pruefen (§§ 10 ff. GwG).
5. Was ist das **Endziel** des Mandanten in einem Satz?

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster fuer Marken-, Patent-, Design- und Wettbewerbsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klaegerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: Marken, Designs, Patente, UWG-Abmahnung, Lizenz, Domain
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben. Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantensystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis, bei juristischer Person Handelsregister-/Transparenzregisterauszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG fuer RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, Behoerde.
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klaeren.

### 4. Streitwert und Gebuehrenvereinbarung

Standard-Streitwerte im Bereich Marken-, Patent-, Design- und Wettbewerbsrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag pruefen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Pruefung + Schriftsatz) oder begrenzt (nur Pruefung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzustaendig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Zentrale Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen und Paragrafenkette

- § 43a Abs. 4 BRAO — Interessenkonflikt
- § 3 BORA — Interessenkonflikt Sachzusammenhang
- §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG — Identifizierungspflicht
- § 9 RVG — Vorschussanforderung
- § 3a RVG — Schriftformerfordernis Stundenhonorar
- §§ 195, 199 BGB — Regelverjaehrung 3 Jahre

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjaehrung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Output-Template Mandatsbogen

**Adressat:** intern (Kanzleiakte) — Tonfall sachlich-strukturiert

```
MANDATSBOGEN — MARKEN-/PATENT-/DESIGN-/WETTBEWERBSRECHT

Datum: [TT.MM.JJJJ]
Aktenzeichen: [INTERN]
Mandant: [NAME, Geburtsdatum, Adresse, Telefon, E-Mail]
Gegner: [NAME, Adresse, ggf. anwaltliche Vertretung]
Sachverhalt: [5-10 Saetze]
Ziel des Mandats: [Eine Zeile]
Schutzrecht: [ ] Marke [ ] Design [ ] Patent [ ] UWG [ ] Sonstiges
Frist: [DATUM] — Bereich: [Widerspruch/Abmahnung/Klage/Einspruch]
Konflikt-Check: [ ] geprueft, kein Konflikt [ ] Einwilligung liegt vor
GwG: [ ] Identifizierung erfolgt [ ] Risiko: [niedrig/mittel/hoch]
Vollmacht: [ ] unterschrieben am [DATUM]
Streitwert: ca. [BETRAG] EUR (Schaetzung)
Honorar: [ ] RVG [ ] Stundenhonorar [BETRAG EUR/h] [ ] Pauschale
Vorschuss: [BETRAG] EUR, faellig [DATUM]
Naechste Schritte: 1. [MASSNAHME] bis [DATUM] — 2. [MASSNAHME] bis [DATUM]
```

## Output-Template E-Mail Erstgespraechs-Zusammenfassung

**Adressat:** Mandant — Tonfall verstaendlich-erklaerend

```
Sehr geehrte/r Frau/Herr [NAME],

vielen Dank fuer unser heutiges Gespraech. Ich fasse die wesentlichen Punkte zusammen:

1. Sachverhalt: [Kurzbeschreibung]
2. Handlungsbedarf: [Welche Schritte eingeleitet werden]
3. Naechste Frist: [DATUM] — [Was bis dahin geschieht]
4. Kosten: Auf Basis des Streitwerts von ca. [BETRAG] EUR fallen Anwaltsgebuehren
 nach RVG von ca. [BETRAG] EUR an. [Ggf. Stundenhonorar erlaeutern.]
5. Bitte senden Sie mir bis [DATUM] folgende Unterlagen: [Liste]

Mit freundlichen Gruessen
[KANZLEI / NAME]
```

## Schritt-fuer-Schritt-Workflow

```
Schritt 1: Frist identifizieren
 → Jedes mitgebrachte Schreiben auf Fristen scannen
 → Kalender-Alarm mit 3-Tage-Vorlauf

Schritt 2: Konflikt-Check
 → Mandantensystem abfragen: Gegner, Sachzusammenhang
 → Bei Konflikt: ablehnen und schriftlich mitteilen

Schritt 3: GwG-Pruefung
 → Ausweis kopieren und im Akt ablegen
 → Risikoklasse vermerken

Schritt 4: Vollmacht unterschreiben lassen
 → Allgemeine Vollmacht + ggf. Sondervollmacht

Schritt 5: Streitwert und Honorar festlegen
 → Ersten Schriftsatz / erste Leistung bepreisen
 → Vorschuss anfordern § 9 RVG

Schritt 6: Mandatsbogen ausfuellen
 → Vollstaendig, datiert, abgelegt

Schritt 7: E-Mail-Zusammenfassung binnen 48 h
 → Bestaetigung Strategie, Fristen, Kosten
```

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang.
- Vollmachtsumfang unklar → spaeter Streit mit Mandantin ueber Befugnisse.
- Honorarvereinbarung muendlich → Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk ueber Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag. Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behoerdenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten — aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen):

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl — Spielraum fuer Verjaehrungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang:

1. § 43a Abs. 4 BRAO und § 3 BORA — Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Vertiefung: Fristen im gewerblichen Rechtsschutz

| Verfahren | Frist | Norm |
|-----------|-------|------|
| Widerspruch Marke DPMA | 3 Monate ab Veroeffentlichung | § 42 Abs. 1 MarkenG |
| Widerspruch Marke EUIPO | 3 Monate ab Veroeffentlichung | Art. 46 UMV |
| UWG-Verfuegungsantrag | Dringlichkeit (max. 4 Wochen Kenntniswahrung) | § 12 Abs. 1 UWG |
| Einspruch DPMA (Patent) | 9 Monate ab Erteilung | § 59 Abs. 1 PatG |
| Nichtigkeitsklage Patent | keine Frist (solange Patent laeuft) | § 81 PatG |
| Verjaehrung UWG/MarkenG | 3 Jahre ab Kenntnis | §§ 195, 199 BGB |
| Verjaerungs-Hemmung | Klage, Mahnbescheid, Verhandlung | § 204 BGB |

## Cross-Refs

- `vergleichsverhandlung-strategie` — fuer den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` — fuer den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.

## 2. `fachanwalt-gewerblicher-rechtsschutz-abmahnung-uwg`

**Fokus:** UWG-Abmahnung prüfen versenden oder auf Eingang reagieren. § 8 UWG Unterlassungsanspruch §§ 3 4 5 UWG Verbotsgrunde §§ 12 13 UWG Durchsetzung. Prüfraster: Verletzungshandlung Abmahnberechtigung Fristen UE Vertragsstrafe Kosten. Output: Abmahnschreiben oder Erwiderung modifizierte UE Kostennote. Abgrenzung: nicht für Markenrecht (fachanwalt-gewerblicher-rechtsschutz-markenanmeldung).

## Mandantenfragen beim Kaltstart

1. Welcher konkrete Wettbewerbsverstoß liegt vor — irreführende Werbung (§ 5 UWG), Rechtsbruch (§ 3a UWG), Spam (§ 7 UWG), aggressive Handlung (§ 4a UWG) oder vergleichende Werbung (§ 6 UWG)?
2. Ist die Mandantschaft aktivlegitimiert nach § 8 Abs. 3 UWG — besteht ein konkretes Wettbewerbsverhältnis, oder ist sie qualifizierter Verband?
3. Wann erlangte die Mandantschaft Kenntnis vom Verstoß — Verjährung 6 Monate nach § 11 UWG läuft?
4. Wurde die Mandantschaft bereits abgemahnt, oder plant sie die Abmahnung der Gegenseite?
5. Liegt der Verdacht eines missbräuchlichen Abmahnens der Gegenseite vor (§ 8c UWG) — Massenabmahnungen, übersetzte Vertragsstrafe?
6. Hat die Gegenseite eine Schutzschrift beim Zentralen Schutzschriftenregister hinterlegt?
7. Besteht UWG-Anspruchskonkurrenz mit Marken- oder Designrecht?
8. Welcher Streitwert und damit welche Kostenrisiken sind realistisch?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|------|--------|
| § 3 Abs. 1 UWG | Verbot unlauterer geschäftlicher Handlungen |
| § 3a UWG | Rechtsbruchtatbestand: Verstoß gegen Marktverhaltensregel |
| § 4 Nr. 3 UWG | Mitbewerberschutz: Nachahmungsschutz (ergänzender Leistungsschutz) |
| § 4a UWG | Aggressive geschäftliche Handlungen |
| § 5 UWG | Irreführende Werbung: objektiv unrichtige oder zur Täuschung geeignete Angaben |
| § 5a UWG | Irreführung durch Unterlassen wesentlicher Informationen |
| § 6 UWG | Vergleichende Werbung: zulässig wenn objektiv, nicht irreführend, nicht verunglimpfend |
| § 7 UWG | Unzumutbare Belästigung: E-Mail-Spam, Kalt-Telefonate, Briefkastenwerbung |
| § 8 Abs. 1 UWG | Unterlassungs- und Beseitigungsanspruch |
| § 8 Abs. 3 UWG | Aktivlegitimation: Mitbewerber (Nr. 1), qualifizierte Wirtschaftsverbände (Nr. 2), qualifizierte Verbraucherverbände (Nr. 3), Kammern (Nr. 4) |
| § 8b UWG | Qualifizierte Einrichtungen und Verbände (Liste beim BfJ) |
| § 8c UWG | Rechtsmissbräuchliche Abmahnung: Indizien, Rechtsfolgen (keine Kostenerstattung) |
| § 9 UWG | Schadensersatz bei Verschulden; § 9 Abs. 2 bei Verbraucherbeeinträchtigung |
| § 11 UWG | Verjährung: Unterlassungsanspruch 6 Monate ab Kenntnis; Schadensersatz 3 Jahre §§ 195, 199 BGB |
| § 12 Abs. 1 UWG | Dringlichkeitsvermutung für einstweilige Verfügung |
| § 13 Abs. 3 UWG | Aufwendungsersatz für Abmahnkosten (bei berechtigter Abmahnung) |
| § 13 Abs. 4 UWG | Ausschluss Aufwendungsersatz bei bestimmten Online-Handel-/Datenschutzverstößen |
| § 14 UWG | Gerichtliche Zuständigkeit: LG am Ort der gewerblichen Niederlassung; fliegender Gerichtsstand eingeschränkt |

## Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Kernaussage |
|---------|-------------|-------|-------------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema UWG-Abmahnung

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.


| Schritt | Prüfpunkt | Norm | Rechtsfolge |
|---------|-----------|------|-------------|
| 1 | Geschäftliche Handlung? | § 2 Abs. 1 Nr. 2 UWG | Anwendungsbereich; nicht bei rein privaten Handlungen |
| 2 | Konkreter Verbotstatbestand | §§ 3a, 4, 4a, 5, 5a, 6, 7 UWG; Anhang | Abmahnfähigkeit |
| 3 | Aktivlegitimation § 8 Abs. 3 UWG? | § 8 Abs. 3 Nr. 1–4 UWG | Ohne Aktivlegitimation: keine strafbewehrte UE; Klage unzulässig |
| 4 | Missbrauchsprüfung § 8c UWG | § 8c Abs. 2 UWG (Indizien) | Missbräuchliche Abmahnung: kein Kostenersatz; Gegenanspruch § 8c Abs. 3 UWG |
| 5 | Abmahninhalt: Beanstandung + Unterlassungsaufforderung + Frist | § 13 UWG | Formell mangelhafte Abmahnung löst keinen Kostenersatz aus |
| 6 | Unterlassungserklärung abgegeben? Ausreichend strafbewehrt? | §§ 339 BGB; § 12 UWG | Unzureichende UE = Wiederholungsgefahr bleibt; eV-Antrag nötig |
| 7 | Einstweilige Verfügung nötig? | §§ 935, 940 ZPO; § 12 Abs. 1 UWG | Dringlichkeit; Selbstwiderlegung ab ca. 4 Wochen Untätigkeit |
| 8 | Verjährung geprüft? | § 11 Abs. 1 UWG | 6 Monate ab Kenntnis; Unterbrechung durch Abmahnung oder eV-Antrag |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — UWG-Abmahnung aussprechen oder empfangen | Abmahnungs-Vollmuster und ggf. eAVV-Antrag unten |
| Variante A — Abmahnung ist missbraeuchlich (§ 8c UWG) | Widerspruchsbaustein unten; kein UE unterzeichnen |
| Variante B — Mandant moechte selbst abmahnen | Abmahnungs-Vollmuster unten; Streitwert sorgfaeltig berechnen |
| Variante C — einstweilige Verfuegung noetig | eAVV-Antrag unten; Dringlichkeit pruefen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatz-Bausteine

### Abmahnung (vollständiges Muster)

```
[Briefkopf Kanzlei] [Ort, Datum]

An [Name der Wettbewerberin] - Per Einschreiben/Rückschein -

Wettbewerbsrechtliche Abmahnung gemäß § 13 UWG

Unsere Mandantin: [Unternehmensname]
Ihre Referenz: [Beschreibung des Verstoßes]

Sehr geehrte Damen und Herren,

wir zeigen die Vertretung der [Mandantin] an (Vollmacht Anlage 1).

I. Sachverhalt
Die Mandantin und Ihr Unternehmen sind Mitbewerber i. S. § 2 Abs. 1 Nr. 4 UWG
im Bereich [Branche]. Sie haben am [Datum] auf der Website [URL] / in [Medium]
folgende Aussage veröffentlicht: "[wörtliches Zitat]" (Anlage 2, Screenshot /
Kopie).

II. Rechtliche Würdigung
Die Aussage ist irreführend i. S. § 5 Abs. 1 S. 2 Nr. 1 UWG [alternativ:
Verstoß gegen § 3a UWG durch Verletzung von [Marktverhaltensregel]],
da [Begründung: objektiv unrichtig / geeignet zur Täuschung / Pflichtangabe
fehlend nach §§ 5a, 8 TMG / Impressumspflicht DDG verletzt].

III. Aufforderung
Wir fordern Sie auf:

1. Die beanstandete Werbung / Handlung unverzüglich einzustellen;

2. bis spätestens [Datum] (Frist: 10 Werktage) die anliegende strafbewehrte
 Unterlassungserklärung (Anlage 3) unterzeichnet zurückzusenden;

3. die der Mandantin entstandenen Abmahnkosten gemäß § 13 Abs. 3 UWG
 in Höhe von EUR [Betrag nach RVG; Streitwert EUR [X]; 1.3-Gebühr zzgl.
 Auslagen zzgl. 19 % MwSt.] auf folgendes Konto zu zahlen:
 IBAN: [DE XX XXXX ...]

Bei fruchtlosem Ablauf der Frist werden wir ohne weitere Ankündigung
Antrag auf Erlass einer einstweiligen Verfügung stellen.

Mit freundlichen Grüßen
[Kanzlei, Fachanwalt/Fachanwältin für gewerblichen Rechtsschutz]

--- ANLAGE 3: Strafbewehrte Unterlassungserklärung ---

Die [Schuldnerin], gesetzlich vertreten durch [Vertretung], verpflichtet sich
gegenüber der [Gläubigerin] für jeden Fall der schuldhaften Zuwiderhandlung
zur Zahlung einer Vertragsstrafe nach dem Hamburger Brauch (festzusetzen nach
billigem Ermessen der Gläubigerin, im Streitfall durch das zuständige Gericht
zu überprüfen), das folgende Handlung zu unterlassen:

[Konkrete Verletzungsform — nicht zu weit, nicht zu eng formulieren]

[Ort, Datum, Unterschrift, Firmenstempel]
```

### Antrag einstweilige Verfügung UWG

```
An das Landgericht [Ort]

ANTRAG AUF ERLASS EINER EINSTWEILIGEN VERFÜGUNG
gemäß §§ 935, 940 ZPO iVm § 8 Abs. 1 UWG

Verfügungsklägerin: [Mandantin]
Verfügungsbeklagte: [Wettbewerberin]

Es wird beantragt, der Verfügungsbeklagten unter Androhung der Ordnungsmittel
des § 890 ZPO zu untersagen, im geschäftlichen Verkehr [Verletzungsform].

Dringlichkeit (§ 12 Abs. 1 UWG):
Kenntnis vom Verstoß am [Datum]. Antrag nach [X] Tagen. Keine Schutzschrift
im Zentralen Schutzschriftenregister (§ 945a ZPO) feststellbar.

Glaubhaftmachung:
Anlage AS 1: Eidesstattliche Versicherung [Name];
Anlage AS 2: Screenshot der beanstandeten Werbung [Datum];
Anlage AS 3: Handelsregisterauszug Mandantin (Aktivlegitimation);
Anlage AS 4: Abmahnung vom [Datum] (zur Dokumentation).

Streitwert: EUR [X].

[Ort, Datum]
[Kanzlei, Fachanwalt/Fachanwältin für gewerblichen Rechtsschutz]
```

### Widerspruch gegen missbräuchliche Abmahnung (§ 8c UWG)

```
An [Kanzlei der Abmahnenden] [Ort, Datum]

In Sachen [Abgemahnte] / [Abmahnende]
Az. Ihrer Kanzlei: [Ref.]

Wir zeigen die Vertretung der [Abgemahnten] an (Vollmacht in Anlage).

Die Abmahnung vom [Datum] ist missbräuchlich i. S. § 8c UWG und wird
zurückgewiesen.

Begründung:
[Indizien nach § 8c Abs. 2 UWG, z. B.: Mandantin hat im selben Zeitraum
[X] gleichartige Abmahnungen versandt (§ 8c Abs. 2 Nr. 1); überhöhte
Vertragsstrafe bei geringfügigem Verstoß (§ 8c Abs. 2 Nr. 2); kein
konkretes Wettbewerbsverhältnis (§ 8c Abs. 2 Nr. 5).]

Aufwendungsersatz wird gemäß § 8c Abs. 3 UWG zurückgefordert.

Wir behalten uns vor, unsererseits Klage auf Feststellung der Missbräuchlichkeit
und auf Ersatz unserer Abwehrkosten zu erheben.

[Kanzlei, Datum]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]


## Beweislast

| Beweisthema | Beweislast | Beweismittel |
|------------|-----------|--------------|
| Wettbewerbsverstoß (konkrete Verletzungshandlung) | Abmahnender | Screenshot, Testkauf, eidesstattliche Versicherung |
| Aktivlegitimation (konkretes Wettbewerbsverhältnis) | Abmahnender | Handelsregisterauszüge, Produktkataloge, Website-Vergleich |
| Wiederholungsgefahr entfallen | Abgemahnter | Strafbewehrte Unterlassungserklärung; bei Erstverstoß: strukturelle Änderung |
| Missbrauch § 8c UWG | Abgemahnter | Liste paralleler Abmahnungen; Übersetzung Vertragsstrafe; fehlende eigene wirtschaftliche Tätigkeit |
| Schaden für Schadensersatz § 9 UWG | Abmahnender | Konkrete Umsatzeinbußen; Sachverständiger; Kundenverlust-Belege |
| Verjährung nicht eingetreten | Abmahnender | Kenntnisdatum belegen (z. B. internes Monitoring-Protokoll) |

## Fristen

| Frist | Inhalt | Norm |
|-------|--------|------|
| 6 Monate | Verjährung Unterlassungsanspruch ab Kenntnis des Verstoßes | § 11 Abs. 1 UWG |
| 3 Jahre | Verjährung Schadensersatz | §§ 195, 199 BGB |
| 8–10 Werktage | Übliche Frist zur Abgabe der UE in der Abmahnung | § 13 Abs. 2 Nr. 4 UWG |
| ca. 4 Wochen | Selbstwiderlegungsrisiko bei einstweiliger Verfügung | § 12 Abs. 1 UWG; Rspr. |
| 1 Monat | Widerspruch gegen einstweilige Verfügung | § 924 ZPO |
| 1 Monat | Abschlusserklärung nach Zustellung einstweiliger Verfügung fordern | Praxis; mündliche Verhandlung vermeiden |

## Gegenargumente und Reaktion

| Gegenargument | Herkunft | Reaktion |
|--------------|---------|----------|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Abmahnung ist missbräuchlich (§ 8c UWG)" | Abgemahnter | Gegenprüfung der Indizien; bei klaren Verstößen: Klage trotzdem zulässig und kostenpflichtig für Schuldner |
| "Verstoß ist bagatellmäßig" | Abgemahnter | § 3 Abs. 1 UWG: "spürbar" Erfordernis; bei Schwarze-Liste-Verstößen keine Spürbarkeitserfordernis |
| "Werbung ist Meinung, keine Tatsachenbehauptung" | Abgemahnter | Meinungsäußerung nur bei wertenden Aussagen ohne Tatsachenkern; gemischte Aussagen nach BGH-Kriterien aufteilen |
| "Verjährung abgelaufen" | Abgemahnter | Kenntnisdatum exakt dokumentieren; Verjährungsunterbrechung durch Abmahnung prüfen (Meinungsstreit) |
| "Unterlassungserklärung ist zu weit gefasst" | Abgemahnter | Modifizierte Unterlassungserklärung anbieten; Schutz vor Vertragsstrafe-Inflation durch enge Formulierung |

## Streitwert und Kosten

**Streitwertorientierung (OLG-Streitwertkataloge Wettbewerbssachen):**
- Einfache Irreführung in Werbung: EUR 10.000–30.000.
- Spam-E-Mails (einzeln): EUR 5.000–15.000.
- Influencer-Schleichwerbung: EUR 15.000–30.000.
- Markenverletzung parallel: Erhöhung möglich.
- Fehlende Impressumspflicht (DDG/TMG): EUR 1.000–5.000; § 13 Abs. 4 UWG schließt Aufwendungsersatz häufig aus.

**Anwaltsgebühren aus EUR 20.000 Streitwert:**
- Abmahnung: 1.3-Gebühr VV RVG ca. EUR 1.029 zzgl. Auslagen zzgl. 19 % MwSt.
- Einstweilige Verfügung: Verfahrensgebühr 1.3 + Terminsgebühr 1.2 = ca. EUR 2.000 netto.

**Ordnungsgeld bei Verstoß gegen Unterlassungsurteil/eV:** EUR 5.000–250.000 (§ 890 ZPO); Ordnungshaft bis 6 Monate.

## Strategische Empfehlung

| Situation | Empfehlung | Begründung |
|-----------|------------|-----------|
| Eindeutiger Verstoß, Gegenseite kooperativ | Abmahnung mit kurzer Frist (10 Tage); keine eV | Kostengünstigste Lösung; UE mit Hamburger Brauch ausreichend |
| Verstoß läuft weiter / Gegenseite ignoriert Abmahnung | Sofort einstweilige Verfügung; keine weitere Vorwarnung | Dringlichkeit bleibt erhalten; OLG: Abmahnung unterbricht Dringlichkeit nicht automatisch |
| Verdacht auf missbräuchliche Gegenabmahnung | § 8c UWG-Gegenangriff; Kostenforderung zurückweisen; Negativfeststellungsklage prüfen | Kostenerstattung entfällt; Gegenanspruch nach § 8c Abs. 3 UWG |
| Eigene Werbepraktiken prüfen lassen | Präventiv-Compliance: UWG-Audit der Website, AGB, Impressum, Produktaussagen | § 5a UWG und DDG-Pflichten häufig übersehen |

## Anschluss-Skills

- `fachanwalt-gewerblicher-rechtsschutz-designverletzung` — Designrechtliche Anspruchskonkurrenz
- `fachanwalt-gewerblicher-rechtsschutz-markenanmeldung` — Markenrechtliche Abmahnung analog UWG
- `fachanwalt-gewrechts-ki-vo-50-genai` — Kennzeichnungspflichten KI-generierter Inhalte als UWG-Abmahnungsanker
- `fachanwalt-gewrechts-geschgehg-kollisionen-nda-hinschg-urhg` — Unlautere Verwertung von Geschäftsgeheimnissen

## Quellen

- UWG: https://www.gesetze-im-internet.de/uwg_2004/
- § 8c UWG: https://www.gesetze-im-internet.de/uwg_2004/__8c.html
- BGH I ZR 154/16: https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&az=I%20ZR%20154/16
- BGH I ZR 45/11: https://juris.bundesgerichtshof.de/cgi-bin/rechtsprechung/document.py?Gericht=bgh&Art=en&az=I%20ZR%2045/11
- Zentrales Schutzschriftenregister: https://www.schutzschriftenregister.de/

## 3. `fachanwalt-gewerblicher-rechtsschutz-abmahnung-vergleich-wipo`

**Fokus:** Abmahnung oder Vergleich bei Domainnamen-Streit und WIPO-Schiedsverfahren vorbereiten. UDRP WIPO-Schiedsregeln § 14 MarkenG Markenrecht. Prüfraster: Domain-Name Verwechslungsgefahr Boese-Glauben-Registrierung Schiedsstellenzuständigkeit Transferantrag. Output: WIPO-Beschwerde oder Verteidigung Vergleichsangebot. Abgrenzung: nicht für Markenrecht vor EUIPO oder DPMA.

# Abmahnungs-Vergleich / WIPO-Mediation im gewerblichen Rechtsschutz

## Triage zu Beginn — klaere vor Bearbeitung

1. Mandantenrolle: **Abmahner** (aktiv, Anspruch durchsetzen) oder **Abgemahnter** (reaktiv, Unterlassungserklaerungs-Wirkung begrenzen)?
2. Verletzungs-Art: Marke (§ 14 MarkenG), Design (§ 38 DesignG), UWG (§§ 3 ff. UWG), UrhG (§§ 97 ff. UrhG), Patent (§§ 139 ff. PatG)?
3. Ist die Abmahnung **formal wirksam**? Fehlen: Abmahner-Legitimation, Verletztendarlegung, Bezifferung Streitwert, Fristen-Setzen → ggf. Zurueckweisung ohne Unterlassungserklaerung.
4. Liegt Verdacht auf **Missbrauch** vor (§ 8c UWG)? Serienabmahner, auffaellige Streitwerthoehe, kostentreibende Vertragsstrafe ohne Interesse?
5. Besteht **Internationaler Bezug** → WIPO Mediation erwaegen?
6. Was ist die **BATNA** beider Seiten? Prozesskosten, Erfolgswahrscheinlichkeit, Zeitrahmen?

## Rechtlicher Rahmen

- **§ 8 UWG** — Unterlassungsanspruch
- **§ 8c UWG** — Rechtsmissbrauch bei Abmahnung
- **§ 13 Abs. 3 UWG** — Aufwendungsersatz Abmahnkostenersatz
- **§ 12 Abs. 1 UWG** — Dringlichkeits-Selbstwiderlegung bei einstweiliger Verfuegung
- **§ 14 MarkenG** — Markenverletzung
- **§ 97a UrhG** — Abmahnung im Urheberrecht
- **§§ 339-345 BGB** — Vertragsstrafe
- **WIPO Mediation Rules** / **WIPO Arbitration Rules** (2021)
- **§ 1066 ZPO** — Vollstreckbarkeit Schiedsspruch

## Zentrale Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette bei Reaktion auf Abmahnung

§ 14 MarkenG / § 3 UWG → § 8 UWG (Unterlassungsanspruch) → § 13 Abs. 3 UWG (Kostenerstattung) → §§ 339-345 BGB (Vertragsstrafe) → § 8c UWG (Missbrauch pruefen) → ggf. § 12 UWG (einstweilige Verfuegung bei Scheitern)

## ADR-Pfade

### Pfad 1 — Modifizierte Unterlassungserklaerung

- Statt der vom Abmahner vorgelegten UE eine eigene entwerfen
- Anti-Hammer-Klausel: "nur bei rechtskraeftiger Feststellung der Pflichtverletzung faellt Vertragsstrafe an"
- Reduzierte Vertragsstrafe (typisch 1.000-5.000 EUR statt Hamburger Brauch)
- Schreibvorlage: s. Output-Template unten

### Pfad 2 — Vergleichs-Verhandlung mit Vertragsstrafe-Vereinbarung

- Gegenseitige Konzession
- Lizenzanaloger Schadensersatz (5-15 % auf Umsatz je nach Branche)
- Inverkehrbringen-Rueckkauf, Vernichtungs-Klausel
- Gegenseitige Erledigung gegen Zahlung einer Vergleichssumme

### Pfad 3 — WIPO Mediation (international)

- Bei Marken-/Patentstreit mit Auslandsbezug
- Neutrale Mediatoren WIPO Geneva
- Kostenguenstiger als Klage in mehreren Laendern
- 60-90 Tage Verfahren, vertraulich

### Pfad 4 — WIPO Arbitration

- Endgueltige Entscheidung
- Vollstreckbar nach New Yorker Uebereinkommen
- Bei Lizenz-Streit, Technologie-Transfer

### Pfad 5 — Klage / einstweilige Verfuegung

- Bei haerter Position oder Beweisproblemen
- § 12 UWG einstweilige Verfuegung — Selbstwiderlegungsfrist beachten (max. 4 Wochen Kenntnis)
- Erbieten Sicherheitsleistung bei Eilverfahren

## Schritt-fuer-Schritt-Workflow

```
Schritt 1: Abmahnung formal pruefen
 → Aktivlegitimation des Abmahnenden (§ 8 Abs. 3 UWG)?
 → Verletzungshandlung konkret bezeichnet?
 → Frist gesetzt (ueblicherweise 7-14 Tage)?
 → Streitwertangabe vorhanden?
 → Wenn Formmangel: Zurueckweisung ohne UE erwaegen

Schritt 2: Missbrauchspruefung § 8c UWG
 → Serienabmahner bekannt?
 → Eigeninteresse des Abmahnenden erkennbar?
 → Kosten unverhältnismässig hoch?
 → Wenn Missbrauch: Gegenabmahnung/Negativ-Feststellungsklage

Schritt 3: Verletzungspruefung
 → Tatsachlich Verletzung des Schutzrechts?
 → Ja: UE erwaegen (ggf. modifiziert)
 → Nein: Zurueckweisung mit Begruendung

Schritt 4: Vergleichsstrategie festlegen
 → Modifizierte UE oder volle Anerkennung?
 → Lizenzanaloger Schadensersatz verhandeln?
 → WIPO-Mediation bei internationalem Bezug?

Schritt 5: Reaktion fristgerecht versenden
 → Schriftlich, per Fax oder E-Mail (Empfangsbekenntnis!)
 → Modifizierte UE mit Anti-Hammer-Klausel

Schritt 6: Bei Scheitern
 → einstweilige Verfuegung nach § 12 UWG (Abmahner)
 → Negative Feststellungsklage (Abgemahnter)
```

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Output-Template Modifizierte Unterlassungserklaerung

**Adressat:** Abmahnender/Gegenseite — Tonfall sachlich-juristisch

```
MODIFIZIERTE UNTERLASSUNGSERKLAERUNG

[NAME MANDANT], [ADRESSE]
— im Folgenden "Erklaerungsgebende" —

an:
[NAME ABMAHNER], [ADRESSE]
— im Folgenden "Erklaerungsempfaengerin" —

Betr.: Ihre Abmahnung vom [DATUM], Az. [AKTENZEICHEN]

Die Erklaerungsgebende gibt die folgende modifizierte Unterlassungserklaerung ab:

§ 1 Unterlassungsverpflichtung
Die Erklaerungsgebende verpflichtet sich, es zu unterlassen, [VERLETZUNGSHANDLUNG
GENAUE BESCHREIBUNG] zu begehen, sofern die vorliegend behauptete Verletzung
rechtskraeftig festgestellt ist.

§ 2 Vertragsstrafe
Fuer jeden Fall schuldhafter Zuwiderhandlung nach rechtskraeftiger Feststellung
der Pflichtverletzung verpflichtet sich die Erklaerungsgebende zur Zahlung einer
Vertragsstrafe in Hoehe von [BETRAG] EUR (Anti-Hammer-Klausel: die Vertragsstrafe
ist nur faellig, wenn die Verletzung rechtskraeftig festgestellt ist).

§ 3 Kosten
Ueber die Kostenuebernahme wird gesondert verhandelt.

[ORT, DATUM]
[UNTERSCHRIFT]
[NAME, KANZLEI]
```

## Output-Template Vergleichsangebot

**Adressat:** Abmahnender/Gegenseite — Tonfall sachlich-verhandelnd

```
VERGLEICHSANGEBOT

[KANZLEI], [DATUM]

Ihre Abmahnung vom [DATUM] — unser Zeichen: [AZ]

Sehr geehrte Frau/Herr [NAME],

ohne Praejudiz und unter dem Vorbehalt des Widerrufs unterbreiten wir folgendes
Vergleichsangebot:

1. [MANDANT] zahlt an [ABMAHNER] einen Gesamtbetrag von [BETRAG] EUR zur
 endgueltigen Erledigung aller Ansprueche aus der Verletzungshandlung
 [KURZBESCHREIBUNG].

2. [MANDANT] gibt die modifizierte Unterlassungserklaerung gem. beigefuegtem
 Entwurf ab.

3. Mit Zahlung und UE-Abgabe sind saemtliche wechselseitigen Ansprueche aus
 dem zugrundeliegenden Sachverhalt erledigt.

Dieses Angebot gilt bis [DATUM, ueblicherweise 5 Werktage].

Mit freundlichen Gruessen
[KANZLEI / NAME]
```

## Vertiefung: Vertragsstrafe und Schadensersatz

| Berechnungsmethode | Formel | Nachweis |
|--------------------|--------|----------|
| Lizenzanaloge | Uebliche Lizenzrate x Umsatz mit verletzenden Produkten | Preislisten, Branchenueblichkeit |
| Verletzergewinn | Tatsaechlicher Gewinn des Verletzers | Auskunftsklage § 19 MarkenG |
| Einmaliger Pauschbetrag | Nach Billigkeit, haeufig 5.000-50.000 EUR | Gerichtliche Schaetzung § 287 ZPO |
| Vertragsstrafe | Vereinbarter Betrag je Verstoß | Unterlassungserklaerung |

## Querverweise

- `fachanwalt-gewerblicher-rechtsschutz-uwg-einstweilige-verfuegung` — Eil-Verfahren nach Scheitern
- `fachanwalt-gewerblicher-rechtsschutz-marken-widerspruch` — Marken-Verfahren parallel
- `fachanwalt-gewerblicher-rechtsschutz-orientierung` — Triage
