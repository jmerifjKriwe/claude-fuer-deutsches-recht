# Megaprompt: deutsche-rechtsgeschichte

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 132 Skills des Plugins `deutsche-rechtsgeschichte`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Deutsche Rechtsgeschichte: Kaltstart, Aktenlandkarte, Quellenprüfung, Fachmodul-Routing und erste verwertbare Ausgabe.
2. **drg-neu-020-historische-verfassungsvergleiche-als-argumentations** — Deutsche Rechtsgeschichte: Historische Verfassungsvergleiche als Argumentationshilfe mit konkreter Fachprüfung, Quellenh…
3. **bgb-1900-und-soziale-frage** — Deutsche Rechtsgeschichte: BGB 1900 und die soziale Frage. Kritik von Anton Menger und Otto von Gierke, fehlender Arbeit…
4. **abschlussmemo-historische-tragfaehigkeit** — Deutsche Rechtsgeschichte: Abschlussmemo zur historischen Tragfaehigkeit einer juristischen Argumentation. Prueft, ob hi…
5. **rechtspolitische-narrative-enteignung** — Deutsche Rechtsgeschichte: Rechtspolitische Narrative pruefen. Wie man politisch geladene historische Erzaehlungen (Bism…
6. **reichskammergericht-und-reichshofrat** — Deutsche Rechtsgeschichte: Reichskammergericht (1495-1806) und Reichshofrat (1497-1806). Aufbau, Zuständigkeit, Rezeptio…
7. **gute-rechtsgeschichte-fuer-laien** — Deutsche Rechtsgeschichte: Verstaendlich erklaertes historisches Recht für Nicht-Juristen. Didaktische Aufbereitung von …
8. **quellenkritik-archiv-und-edition** — Deutsche Rechtsgeschichte: Quellenkritik für Archivfunde und historische Editionen. Ueberlieferungskritik, Editionsvergl…
9. **gemeines-recht-und-partikularrecht** — Deutsche Rechtsgeschichte: Gemeines Recht und Partikularrecht im 16.-19. Jahrhundert. Ius commune vs. Territorialrecht, …
10. **kontinuitaet-und-bruch-pruefen** — Deutsche Rechtsgeschichte: Kontinuitaet und Bruch pruefen. Methodisches Werkzeug um echte Rechtsbrueche (NS-Machtueberna…
11. **sachsenspiegel-und-landrechte** — Deutsche Rechtsgeschichte: Sachsenspiegel (ca. 1220-1235) und mittelalterliche Landrechte. Eike von Repgow, Landrecht un…
12. **bverfg-und-nachkriegskonsolidierung** — Deutsche Rechtsgeschichte: BVerfG und Nachkriegskonsolidierung. Errichtung des BVerfG 1951, Fruehe Leitentscheidungen (S…
13. **juristenausbildung-und-pruefungswesen** — Deutsche Rechtsgeschichte: Juristenausbildung und Pruefungswesen. Universitaetsrechtsstudium seit Mittelalter, Referenda…
14. **preussisches-allgemeines-landrecht** — Deutsche Rechtsgeschichte: Preussisches Allgemeines Landrecht (ALR) von 1794. Entstehung unter Friedrich dem Grossen und…
15. **seminar-und-vortrag-rechtsgeschichte** — Deutsche Rechtsgeschichte: Seminarvorbereitung und Vortrag. Strukturierung eines rechtshistorischen Referats oder Semina…

---

## Skill: `kaltstart-triage`

_Deutsche Rechtsgeschichte: Kaltstart, Aktenlandkarte, Quellenprüfung, Fachmodul-Routing und erste verwertbare Ausgabe._

# Deutsche Rechtsgeschichte - Allgemeiner Einstieg

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Deutsche Rechtsgeschichte** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Startfragen

1. Was soll entstehen: Verständnis, Gutachten, Vertragsbaustein, Risiko-Dashboard, Unterrichtseinheit, Board-Memo oder Streitstrategie?
2. Welche Quelle liegt vor: Normtext, Vertrag, Handelsdokument, Archivstück, Behördenseite, Schiedsklausel, Register, E-Mail oder Datenraum?
3. Welche Rechtsordnung, Epoche, Institution, Branche oder Gegenpartei ist betroffen?
4. Gibt es Live-Check-Bedarf wegen Tagesrecht, Sanktionen, Exportkontrolle, Behördenpraxis oder aktueller Rechtsprechung?
5. Welche Ausgabe braucht die Nutzerin in welcher Tiefe?

## Kernanker

- Quellenkritik: Normtext, Edition, Archiv, Urteil, Verwaltungspraxis, Lehrbuchtradition
- Epochenlogik: mittelalterliche Rechtsvielfalt, Rezeption, Kodifikationen, Reich/Weimar/NS/DDR/BRD/EU
- Dogmengeschichte: Eigentum, Vertrag, Familie, Strafrecht, Verwaltung, Verfassung, Handelsrecht
- Warnregel: keine Gegenwartsnorm unbemerkt in historische Quellen hineinlesen

---

## Skill: `drg-neu-020-historische-verfassungsvergleiche-als-argumentations`

_Deutsche Rechtsgeschichte: Historische Verfassungsvergleiche als Argumentationshilfe mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis: Deutsche Rechtsgeschichte: Historische Verfassungsvergleiche als Argumentationshi..._

# Deutsche Rechtsgeschichte: Historische Verfassungsvergleiche als Argumentationshilfe mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Deutsche Rechtsgeschichte: Historische Verfassungsvergleiche als Argumentationshilfe mit konkreter Fachprüfung, Quellenhygiene, Fehlerbremse und verwertbarem Arbeitsergebnis.

### Deutsche Rechtsgeschichte: 020 Historische Verfassungsvergleiche Als Argumentations

## Bedeutung der Verfassungsgeschichte

- BVerfG zieht regelmaessig historische Vergleiche heran.
- Methodisch: hermeneutische Auslegung des Grundgesetzes mit Blick auf Vorgaenger.

## Vergleichsachsen

### Paulskirchenverfassung 1848/49 → GG
- Grundrechte als Ursprung.
- BVerfG zitiert Paulskirche selten direkt, aber als ideengeschichtlicher Hintergrund.

### WRV 1919 → GG
- BVerfG E 2, 1: WRV ist nicht im selben Sinne fortgesetzt wie BGB.
- BVerfG hat in zentralen Fragen die WRV-Verfassungsrechtsprechung anerkannt.
- Konkrete Kontinuitaet: Art. 137 III WRV iVm Art. 140 GG (Religionsgemeinschaften).

### NS-Zeit → GG
- Radbruch'sche Formel: "Gesetzliches Unrecht und uebergesetzliches Recht" (Sueddeutsche Juristen-Zeitung 1946 S. 105).
- Praktische Anwendung der Radbruchschen Formel durch BVerfG **BVerfGE Band 95 Rn 96** (Mauerschuetzen-Beschluss vom 24. Oktober 1996 - 2 BvR 1851/94 u.a.) und BGH **BGHSt 39 Rn 1**, **BGHSt 39 Rn 168**, **BGHSt 41 Rn 101** (Mauerschuetzen).
- **Nicht zu verwechseln**: **BVerfGE Band 23 Rn 98** (Beschluss vom 14. Februar 1968 - 2 BvR 557/62) betrifft die Nichtigkeit der **NS-Ausbuergerung deutscher Juden** (11. Verordnung zum Reichsbuergergesetz vom 25. November 1941) und ist nicht das Mauerschuetzen-Verfahren.

### DDR-Verfassung → GG
- BVerfG hat DDR-Recht nicht generell verworfen.
- Spezifische Streitfragen ueber Bodenreform und Vermoegensrecht.

## Methodenvorschlag für Argumentation

1. Welche Vorgaengerverfassung enthielt eine vergleichbare Norm?
2. Welche Funktion hatte sie damals?
3. Welche Lehren zog der Verfassungsgeber des GG?
4. Welche Bedeutung im aktuellen Konzept?

## Beispiele

### Art. 1 Abs. 1 GG (Menschenwuerde)
- Kein direktes Vorbild in WRV oder Paulskirche.
- Reaktion auf NS-Zeit.
- "Wesensgehaltsgarantie" als Konsequenz.

### Art. 5 Abs. 1 GG (Meinungsfreiheit)
- Paulskirche § 143 (Grundrechte): Pressefreiheit.
- WRV Art. 118: gleicher Schutz.
- GG: keine Vorzensur.

### Art. 79 Abs. 3 GG (Ewigkeitsklausel)
- Erstmals im GG.
- Reaktion auf Erfahrung der Weimarer Selbstaufgabe durch Ermaechtigungsgesetz.

---

## Skill: `bgb-1900-und-soziale-frage`

_Deutsche Rechtsgeschichte: BGB 1900 und die soziale Frage. Kritik von Anton Menger und Otto von Gierke, fehlender Arbeitnehmerschutz im BGB, Mieterrecht und spaetere soziale Ausformung durch Rechtsprechung und Sondergesetze im Deutsche Rechtsgeschichte._

# BGB 1900 und die soziale Frage

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Das BGB 1900 war auf formaler Gleichheit und Vertragsfreiheit aufgebaut, ohne die realen Machtungleichgewichte zu beruecksichtigen. Anton Mengers Das buergerliche Recht und die besitzlosen Volksklassen (1890) analysierte dies scharf: Das BGB schuetze Eigentuemer und Kreditgeber, nicht Mieter und Arbeitnehmer. Otto von Gierke kritisierte den fehlenden deutschen Genossenschaftsgeist. Die soziale Luecke wurde durch Sondergesetze gefuellt: Gewerbegerichtsgesetz 1890, BGB-Ergaenzungen durch Arbeitnehmerrecht, Mieterschutz im Ersten Weltkrieg. Die Rechtsprechung nutzte BGB § 242 (Treu und Glauben) als Korrektiv. Das 20. Jh. brachte schliesslich Arbeitnehmerschutzrecht (BetrVG, KSchG), Mieterschutz (BGB §§ 535 ff.), und Verbraucherschutz.

## Kernnormen / Kernquellen

- **BGB § 242**: Treu und Glauben, sozialrechtliches Korrektivinstrument
- **BGB § 618**: Fuersorgepflicht des Arbeitgebers (1900 bereits im BGB)
- **Gewerbegerichtsgesetz 1890 (RGBl. 1890, 141)**: Arbeitsgerichtliche Vorlaeufernorm
- **Mieterschutzverordnung 1917**: Erster staatlicher Mietschutz im Weltkrieg
- **KSchG 1951 (BGBl. I 1951, 499)**: Kuendigungsschutzgesetz als BGB-Ergaenzung

## Akteure und Institutionen

- **Anton Menger** (1841-1906): Sozialkritiker des BGB
- **Otto von Gierke** (1841-1921): Deutschrechtliche und soziale BGB-Kritik
- **Reichsgericht (RG)**: Nutzung von § 242 als Sozialkorrektur
- **Weimarer Arbeitsbewegung**: Treiber für Arbeitnehmerschutzgesetze

## Typische Streitfragen / Forschungsfragen

1. War das BGB 1900 bewusst "arbeitgeberfreundlich" oder einfach neutral nach damaligem Verstaendnis?
2. § 242 BGB: Hat das RG damit die sozialen Luecken sinnvoll geschlossen?
3. Mieterschutz: Warum erst 1917? War Krieg als Anlass notwendig?
4. BetrVG 1952/1972: Welcher Teil der Sozialkritik ist ins Gesetz eingegangen?
5. Verbraucherschutz ab 1970er: Laesst sich das als Fortsetzung der Menger-Forderungen lesen?

## Methodik

- Menger Das buergerliche Recht (1890): Erstausgabe zitieren
- BGB § 242 und § 618: gesetze-im-internet.de; historisch Mugdan Bd. II
- KSchG: gesetze-im-internet.de
- Sekundaerliteratur: Knut Wolfgang Noerr, Privatrechtsgeschichte der Weimarer Republik

---

## Skill: `abschlussmemo-historische-tragfaehigkeit`

_Deutsche Rechtsgeschichte: Abschlussmemo zur historischen Tragfaehigkeit einer juristischen Argumentation. Prueft, ob historische Quellen eine heutige Rechtsposition tragen oder ob Anachronismus oder Lueckenbeweis vorliegt im Deutsche Rechtsgeschichte._

# Abschlussmemo historische Tragfaehigkeit

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Das Abschlussmemo historische Tragfaehigkeit ist ein Qualitaetssicherungsinstrument für rechtshistorische Argumente in heutigen Texten (Gutachten, Schriftsaetze, Gesetzesbegr√ündungen). Es prueft: (1) Sind die historischen Quellen korrekt identifiziert? (2) Tragt die Quelle die Behauptung tatsaechlich? (3) Liegt ein Anachronismus vor? (4) Gibt es Luecken in der Argumentationskette? (5) Sind Unsicherheiten sichtbar gemacht? Ergebnis ist ein strukturiertes Memo mit Ampelbewertung: Gruen (Quelle traegt), Gelb (Einschraenkung noetig), Rot (Quelle traegt nicht).

## Kernnormen / Kernquellen

- **BVerfGE 62, 1 (1982)**: BVerfG-Methodik der historischen Auslegung
- **BGB § 133**: Wille des Erklaerenden / Gesetzgebers als Auslegungsziel
- **Mugdan, Materialien BGB** (1899): Massstab für BGB-historische Argumente
- **GG Art. 79 Abs. 3**: Ewigkeitsklausel als Massstab für historische Verfassungsargumente
- **Einigungsvertrag 1990 (BGBl. II 1990, 885)**: Massstab für DDR-Rechtsuebergangsargumente

## Akteure und Institutionen

- **BVerfG**: Pruefungsmassstab für historische Verfassungsargumente
- **BGH**: Zivilrechtliche historische Auslegung, z. B. BGB-Materialien
- **Bundesarchiv**: Primaerquellen-Lieferant für historische Argumentationsbasis
- **BReg Rechtsabteilung**: Nutzer von historischer Argumentation in Gesetzesbegr√ündungen

## Typische Streitfragen / Forschungsfragen

1. Wann hat historische Auslegung Vorrang vor Wortlaut oder Systematik?
2. Wie geht man mit Luecken in der historischen Quellenlage um?
3. Kann eine fehlerhafte historische Behauptung im Schriftsatz anfechtbar sein?
4. Ermächtigungsgesetz 1933 als Praezedenz: Welche historischen Argumente sind taboo?
5. EU-Recht und nationale Rechtsgeschichte: Darf man vorunionale Geschichte als EU-Auslegung einbringen?

## Methodik

- Quellencheck: Primaerquelle lesen, nicht nur Sekundaerautor zitieren
- Anachronismus-Test: Haette ein Jurist der betreffenden Epoche die Argumentation verstanden?
- Lueckentest: Gibt es Epochen ohne Quellenbeleg in der Argumentationskette?
- Unsicherheitsmarkierung: Worte wie vermutlich, nach bisherigem Forschungsstand usw.

---

## Skill: `rechtspolitische-narrative-enteignung`

_Deutsche Rechtsgeschichte: Rechtspolitische Narrative pruefen. Wie man politisch geladene historische Erzaehlungen (Bismarckstaat, Sozialstaat-Errungenschaft, NS als Zivilisationsbruch) historisch-quellenkritisch einordnet im Deutsche Rechtsgeschichte._

# Rechtspolitische Narrative pruefen

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Rechtspolitische Narrative sind verdichtete Erzaehlungen ueber die Bedeutung historischer Ereignisse für heutige Rechtspositionen. Beispiele: Sozialversicherung als Bismarck-Errungenschaft, WRV als gescheitertes Experiment, NS als absoluter Zivilisationsbruch, BGB als Arbeitgeberrecht, Wiedervereinigung als Erfolgsgeschichte. Diese Narrative haben politische Funktionen, aber methodisch muss man fragen: Was sagen die Quellen wirklich? Sind die Schlussfolgerungen belegt oder projiziert? Welche Gegennarrative gibt es? Ein geprueftes Narrativ ist sachlich praeziser und widersteht Gegenarrumenten besser.

## Kernnormen / Kernquellen

- **WRV Art. 119-165**: Wirtschafts- und Sozialordnung als Narrativ-Gegenstand
- **Bismarcks Sozialversicherung 1883-1889**: Narrative als Befriedungs- oder Schutzrecht
- **Radbruch-Formel SJZ 1946, 105**: NS-Rechtsbruch-Narrativ
- **Einigungsvertrag 1990**: Wiedervereinigungsnarrativ
- **GG Art. 20 (Sozialstaatsprinzip)**: Verfassungsrechtliche Kodifikation eines Narrativs

## Akteure und Institutionen

- **Bismarck**: Sozialversicherung als kontrollierte Sozialpolitik (sein Narrativ)
- **SPD und Gewerkschaften**: Sozialversicherung als Arbeitererrungenschaft (Gegennarrativ)
- **Radbruch**: NS-Rechtsbruch-Narrativ nach 1945
- **Medien und Politik**: Verbreitung und Modifikation der Narrative

## Typische Streitfragen / Forschungsfragen

1. Bismarcksche Sozialversicherung: Befriedung oder echter Sozialschutz?
2. WRV-Scheitern: War es unvermeidlich oder kontingent?
3. GG als Erfolgsgeschichte: Werden seine Defizite ausgeblendet?
4. NS-Zivilisationsbruch: Erlaubt das Narrativ, die Kontinuitaetsfrage zu umgehen?
5. Wiedervereinigung als Vollendung: Was wurde dabei nicht erwaehnt?

## Methodik

- Narrative identifizieren und isolieren
- Quellentest: Tragen die Quellen das Narrativ?
- Gegenquellen suchen: Was widerspricht dem Narrativ?
- Nuancierung: Kern des Narrativs beibehalten, Uebertreibungen korrigieren

---

## Skill: `reichskammergericht-und-reichshofrat`

_Deutsche Rechtsgeschichte: Reichskammergericht (1495-1806) und Reichshofrat (1497-1806). Aufbau, Zuständigkeit, Rezeption des gelehrten Rechts, Konkurrenz beider Gerichte und Bedeutung als Vorlaeufer moderner Obergerichte im Deutsche Rechtsgeschichte._

# Reichskammergericht und Reichshofrat

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Das Reichskammergericht (RKG) wurde 1495 auf dem Wormser Reichstag gegründet (RKGOrdnung 1495, RGBl. 1495 [Neue Sammlung]). Es war das erste staendige zentrale Reichsgericht und schrieb die Anwendung des gemeinen Rechts (roemisch-kanonisches Recht) vor. 1527 nach Speyer verlegt, blieb es bis 1806 taetig. Der Reichshofrat (1497/1559) war das kaiserliche Konkurrenzgericht in Wien mit anderer Zusammensetzung und weniger strenger Bindung an das gelehrte Recht. Beide Gerichte bildeten die Spitze der Reichsgerichtsbarkeit. Die Besetzung des RKG (Haefte Reichsstaende, Haefte kaiserliche Ernennung) spiegelte die reichsstaendische Verfassung wider.

## Kernnormen / Kernquellen

- **Reichskammergerichtsordnung 1495**: Gruendungsdokument und Verfahrensordnung
- **Jungster Reichsabschluss 1654**: Letzte grosse RKG-Reform
- **Kammerzielerordnung**: Finanzierung des RKG durch Reichsstaedte und Reichsstaende
- **Wahlkapitulationen** (ab 1519): Sicherung der RKG-Existenz durch Kaiserwahl-Bedingungen

## Akteure und Institutionen

- **Maximilian I.** (1459-1519): Gruender des RKG 1495
- **Kameralrichter** (Praesidenten und Beisitzer): Richterliches Kollegium des RKG
- **Prokuratoren und Advokaten am RKG**: Rechtsanwaltschaft vor dem Reichsgericht
- **Ferdinand I.** (1503-1564): Ausbau des Reichshofrats

## Typische Streitfragen / Forschungsfragen

1. Konkurrenz RKG vs. Reichshofrat: Welches Gericht war "besser"?
2. Evokationsrecht des Kaisers: Konnte der Kaiser Sachen dem RKG entziehen?
3. Kameralakten: Welche Verfahrensakten sind erhalten, welche vernichtet?
4. Wirksamkeit: Hat das RKG tatsaechlich Frieden im Reich gesichert?
5. 1806 und Ende des Alten Reichs: Was wurde aus den haengenden RKG-Verfahren?

## Methodik

- RKG-Ordnung 1495: historische Edition (Neue und Vollstaendigere Sammlung der Reichsabschluesse)
- RKG-Kameralakten: Landesarchive (Speyer, Frankfurt); Inventar Smend (1911)
- Sekundaerliteratur: Bernhard Diestelkamp, Wolfgang Sellert, Klaus Malettke

---

## Skill: `gute-rechtsgeschichte-fuer-laien`

_Deutsche Rechtsgeschichte: Verstaendlich erklaertes historisches Recht für Nicht-Juristen. Didaktische Aufbereitung von Sachsenspiegel, BGB-Entstehung, Weimarer Republik oder NS-Unrecht für Unterricht und Oeffentlichkeit im Deutsche Rechtsgeschichte._

# Gute Rechtsgeschichte für Laien

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Rechtsgeschichte für Nicht-Juristen erfordert eine andere Sprache und Struktur als Facharbeit. Kernaufgabe: komplexe historische Rechtsinstitute in zugaenglicher Sprache erklaeren, ohne Praezision zu opfern. Das bedeutet: Fremdwoerter erklaeren (Pandektistik = Systematisierung des roemischen Rechts durch Kommentatoren), Epochen mit anschaulichen Ankerpunkten benennen (Sachsenspiegel = erster grosser Rechtstext in Mitteldeutsch), und Gegenwartsrelevanz herstellen (Warum praegt das BGB 1900 bis heute unser Vertragsrecht?).

## Kernnormen / Kernquellen

- **Sachsenspiegel** (ca. 1220-1235): Erster grosser Rechtstext in niederdeutscher Volkssprache
- **BGB 1900**: 2385 Paragraphen, gepraegt von Pandektistik und Vertragsliberalismus
- **WRV 1919**: Erste demokratische Gesamtverfassung, aber gescheitert
- **GG 1949 Art. 1-19**: Grundrechtskatalog als Reaktion auf NS-Unrecht
- **EInigungsvertrag 1990**: Rechtliche Grundlage der deutschen Wiedervereinigung

## Akteure und Institutionen

- **Eike von Repgow** (ca. 1180-1233): Sachsenspiegel-Verfasser, erster bekannter Rechtsautor Deutschlands
- **Hugo Preuß** (1860-1925): Demokratischer Verfassungsrechtler, WRV-Hauptautor
- **Konrad Adenauer** (1876-1967) und **Carlo Schmid** (1896-1979): Politiker des Parlamentarischen Rates 1948-49
- **Theodor Heuss** (1884-1963): Erster Bundespräsident, Zeichnete GG

## Typische Streitfragen / Forschungsfragen

1. Wie erklaert man Rechtskontinuitaet und Rechtsbruch für ein Laienpublikum?
2. NS-Recht: Wie vermittelt man, dass auch Unrechtsregime ein Rechtssystem haben?
3. Sachsenspiegel als Illustration: Was kann man aus 800 Jahre altem Text für heute lernen?
4. BGB und Gleichberechtigung: Warum hatte das BGB 1900 kein gleiches Eherecht?
5. Verstaendlichkeit vs. Praezision: Wo ist die Grenze bei Vereinfachung?

## Methodik

- Analoge Vergleiche nutzen: Sachsenspiegel ist wie heutiges BGB, nur auf Pergament
- Zeitlinie und Ankerpunkte statt abstrakter Epochendefinition
- Konkrete Beispiele: Ein Erbfall im Sachsenspiegel vs. BGB vs. heute
- Quellen nennen, aber nicht als Fussnoten, sondern als weiterführende Literatur am Ende

---

## Skill: `quellenkritik-archiv-und-edition`

_Deutsche Rechtsgeschichte: Quellenkritik für Archivfunde und historische Editionen. Ueberlieferungskritik, Editionsvergleich, Archivrecherche in Bundes- und Landesarchiven sowie Umgang mit Handschriften und Druckausgaben im Deutsche Rechtsgeschichte._

# Quellenkritik: Archiv und Edition

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Quellenkritik ist die Grundoperation der Rechtsgeschichte. Sie unterscheidet Ueberlieferungsform (Original, Abschrift, Druck, Digitalisat), Entstehungskontext (Kanzleipraxis, Legislativverfahren, Gerichtspraxis) und Editionszustand (kritische Edition, Regeste, Faksimile). Fuer die deutsche Rechtsgeschichte sind das Bundesarchiv (Koblenz/Berlin), die Landesarchive, das Geheime Staatsarchiv Preussischer Kulturbesitz sowie digitale Sammlungen wie ALEX und MGH-Online die zentralen Anlaufstellen.

## Kernnormen / Kernquellen

- **Bundesarchivgesetz (BArchG)** i.d.F. vom 10. Maerz 2017 (BGBl. I S. 410): Zugang zu Bundesarchivgut
- **Landesarchivgesetze** (z. B. LArchG NRW): Sperrfristen 30 Jahre, Personendaten 10 Jahre nach Tod
- **Mugdan, Die gesamten Materialien zum BGB** (1899, 6 Bde.): Standardedition der BGB-Motive und Protokolle
- **MGH** (Monumenta Germaniae Historica): kritische Edition mittelalterlicher Quellen seit 1826

## Akteure und Institutionen

- **Bundesarchiv Koblenz/Berlin**: Hauptarchiv für Reichs- und Bundesakten
- **Landesarchive**: Regionalbestaende, Verwaltungs- und Gerichtsakten
- **MGH Muenchen**: Kritische Edition mittelalterlicher Quellen
- **ALEX/OeNB Wien**: Digitale Reichsgesetzblatt-Sammlung

## Typische Streitfragen / Forschungsfragen

1. Kritische Edition vs. Faksimile: Wann genuegt welche Quelle?
2. Umgang mit fehlenden Archivalien: Was tun wenn Primaerakten vernichtet wurden (NS, Krieg)?
3. Handschriftliche Quellen vs. Druckausgabe: Welche hat Vorrang beim Sachsenspiegel?
4. Archivzugang und Datenschutz: Wann sind Archivgut-Sperrfristen rechtshistorisch relevant?
5. Digitalisierung und Authentizitaet: Sind Digitalisate gleich reliabel wie Originale?

## Methodik

- Ueberlieferungskette nachzeichnen: Original, Abschrift, Edition, Digitalisat
- Editionsvergleich: mehrere Editionen bei wichtigen Textstellen gegenlesen
- Bundesarchiv-Online: invenio.bundesarchiv.de für Findbuecher
- MGH: mgh.de für Volltext-Zugang zu mittelalterlichen Editionen

---

## Skill: `gemeines-recht-und-partikularrecht`

_Deutsche Rechtsgeschichte: Gemeines Recht und Partikularrecht im 16.-19. Jahrhundert. Ius commune vs. Territorialrecht, Subsidiaritaet des roemischen Rechts, Preussens Sonderweg und Aufloesung durch die BGB-Kodifikation im Deutsche Rechtsgeschichte._

# Gemeines Recht und Partikularrecht

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Das Verhaeltnis von gemeinrechtlicher Doktrin (ius commune, roemisch-kanonisch) und territorialem Partikularrecht (Stadtrechte, Landrechte, Feudalrechte) praegt die Rechtswirklichkeit des fruehneuzeitlichen Deutschlands. Das gemeine Recht galt subsidiaar: Es trat zurueck, wenn Partikularrecht vorhanden war. In der Praxis war die Trennung fliessend: Gerichte wandten das gelehrte Recht an, auch wo Partikularrecht bestand. Das ALR 1794 versuchte, in Preussen das Nebeneinander zu beenden. Erst das BGB 1900 schuf endgueltig einen einheitlichen zivilrechtlichen Rechtsraum für das gesamte Deutsche Reich.

## Kernnormen / Kernquellen

- **Digestentitel D. 1.1 und D. 1.3**: Ius commune-Grundlagen
- **ALR 1794 Einleitung §§ 1-23**: Preussisches Verhaeltnis zum gemeinen Recht
- **EGBGB Art. 2 (1900)**: Aufhebung des gemeinen Rechts mit BGB-Inkrafttreten
- **Corpus Iuris Civilis** als subsidiaeres Gemeines Recht bis 1900

## Akteure und Institutionen

- **Heinrich Dernburg** (1829-1907): Pandektenrechtler, letzter bedeutender Kommentator vor BGB
- **Georg Friedrich Puchta** (1798-1846): Gemeines Recht als wissenschaftliches System
- **Paul von Roth** (1820-1892): Partikularrecht und kodifikatorische Einheit
- **Bayerisches, Oesterreichisches, Preussisches Partikularrecht**: Groesste Territorien mit eigenem Recht

## Typische Streitfragen / Forschungsfragen

1. War das Prinzip lex specialis (Partikularrecht vor gemeinrechtlicher Subsidiaritaet) konsequent durchgefuehrt?
2. Welche Rechtsgebiete blieben laengste dem Partikularrecht: Erbrecht? Familienrecht? Sachenrecht?
3. ALR und gemeines Recht in Preussen: Hat das ALR das gemeine Recht wirklich verdraengt?
4. Verfahrensrechtliche Aspekte: Welches Recht wandten Gerichte in Grenzfaellen an?
5. BGB und Restpartikularrechte: Was blieb durch EGBGB-Vorbehalte als Landesrecht?

## Methodik

- ALR: historische Druckausgaben und ALEX/OeNB
- Gemeines Recht: Dernburg Pandekten (6. Aufl. 1884-1887) als Schluessellehrbuch
- EGBGB: gesetze-im-internet.de für aktuell geltende Uebergangsvorschriften
- Coing Handbuch (1973-88): Europaeische Kontextualisierung des gemeinen Rechts

---

## Skill: `kontinuitaet-und-bruch-pruefen`

_Deutsche Rechtsgeschichte: Kontinuitaet und Bruch pruefen. Methodisches Werkzeug um echte Rechtsbrueche (NS-Machtuebernahme 1933 / Kriegsende 1945 / GG 1949 / Wiedervereinigung 1990) von Schein-Bruechen zu unterscheiden im Deutsche Rechtsgeschichte._

# Kontinuitaet und Bruch pruefen

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Die Frage nach Kontinuitaet und Bruch ist eine der grundlegendsten der deutschen Rechtsgeschichte. Scheinbare Brueche: 1945 schien das Recht neu zu beginnen, aber viele NS-Juristen arbeiteten weiter. 1990 schien DDR-Recht beendet, aber viele DDR-Regelungen galten uebergangsweise fort. Echte Brueche: 1933 Ermächtigungsgesetz als Bruch mit der WRV; 1945 Totalzusammenbruch. Das Pruef-Instrument fragt: (1) Normkontinuitaet (gleicher Gesetzestext?), (2) Institutionenkontinuitaet (gleiche Behörden, Gerichte?), (3) Personalkaontinuitaet (gleiche Richter, Beamten?), (4) Dogmatikkontinuitaet (gleiche Rechtsbegriffe und Prinzipien?).

## Kernnormen / Kernquellen

- **Ermächtigungsgesetz 1933 (RGBl. I 1933, 141)**: Bruch-Dokument WRV
- **Kontrollratsgesetz Nr. 1 (ABl. KR 1945, 6)**: Aufhebung NS-Recht, formeller Bruch
- **GG Art. 123 Abs. 1**: Fortgeltung alten Rechts (Normkontinuitaet trotz Bruch)
- **Einigungsvertrag Art. 8**: Ueberleitung BRD-Recht auf DDR, formeller Bruch DDR-Recht
- **GG Art. 143**: Uebergangsrecht für neue Länder

## Akteure und Institutionen

- **Alliierter Kontrollrat (1945-1948)**: Rechtliche Neuordnung nach NS-Bruch
- **BVerfG**: Fortgeltungsfragen (BVerfGE 6, 389 zur NS-Gesetzgebung)
- **Treuhandanstalt**: Institutionen-Diskontinuitaet 1990 als bewusste Entscheidung
- **Wissenschaft**: Personalkaontinuitaet-Debatte (Mueller Furchtbare Juristen)

## Typische Streitfragen / Forschungsfragen

1. 1945: War es ein Rechtsbruch oder nur Herrschaftsbruch bei Normkontinuitaet?
2. Kontrollratsrecht: Hat es NS-Recht vollstaendig beseitigt oder Luecken gelassen?
3. 1990 und Personalkaontinuitaet: DDR-Richter nach der Wende?
4. GG Art. 123: Welche Altgesetze galten nach 1949 noch?
5. BVerfGE und NS-Gesetzgebung: Hat das BVerfG konsequent NS-Normen abgelehnt?

## Methodik

- Kontrollratsgesetz Nr. 1: historische Edition (ABl. KR 1945)
- Ermächtigungsgesetz 1933: ALEX/OeNB
- GG Art. 123 und 143: gesetze-im-internet.de
- BVerfGE zur NS-Normfortgeltung: bverfg.de

---

## Skill: `sachsenspiegel-und-landrechte`

_Deutsche Rechtsgeschichte: Sachsenspiegel (ca. 1220-1235) und mittelalterliche Landrechte. Eike von Repgow, Landrecht und Lehnrecht, Dreistaendeordnung, Ueberlieferung in Handschriften und Einfluss auf spaeteres Recht im Deutsche Rechtsgeschichte._

# Sachsenspiegel und Landrechte

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Der Sachsenspiegel ist die bedeutendste Rechtsquelle des deutschen Mittelalters. Eike von Repgow verfasste ihn um 1220-1235 in niederdeutscher Sprache (urspruenglich Latein). Er gliedert sich in Landrecht (saekulares Recht, Erbrecht, Strafrecht, Prozessrecht) und Lehnrecht (Lehen, Lehnspflichten). Charakteristisch ist die Dreistaendeordnung (Koenig, Ritter/Adel, Bauern/Buerger) und das Schild-System der Lehnspyramide. Der Sachsenspiegel hatte Einfluss auf spaetere Rechtsspiegel (Schwabenspiegel, Deutschenspiegel) und wurde in ca. 460 Handschriften ueberliefert.

## Kernnormen / Kernquellen

- **Sachsenspiegel Landrecht I 1**: Anfang des Landrechts, Gottesgebot und weltliches Recht
- **Sachsenspiegel Ldr. I 34**: Eigentumsschutz, nemo plus iuris-Grundsatz
- **Sachsenspiegel Ldr. II 12**: Erbrecht und Verwandtschaft
- **Sachsenspiegel Ldr. III 42 § 3**: Stadtrecht und Marktrecht
- **Sachsenspiegel Lehnrecht 1-3**: Lehnskette und Lehnspflichten

## Akteure und Institutionen

- **Eike von Repgow** (ca. 1180-1233): Autor des Sachsenspiegels, Ministeriale im Bistum Halberstadt
- **Hoyer von Falkenstein**: Auftraggeber nach Eikes eigenem Zeugnis im Prolog
- **Glossatoren des 14. Jh.**: Johannes von Buch (ca. 1325) als Kommentator
- **MGH-Editoren (19./20. Jh.)**: Karl August Eckhardt, kritische Sachsenspiegel-Edition

## Typische Streitfragen / Forschungsfragen

1. War der Sachsenspiegel Gewohnheitsrecht-Aufzeichnung oder Normsetzung?
2. Lateinisches Original oder niederdeutsche Urform: Was war die echte Erstfassung?
3. Sachenspiegelrecht und roemisches Recht: In welchem Verhaeltnis standen sie?
4. Geltungsbereich: War der Sachsenspiegel Partikularrecht Sachsens oder ueberre gionales Recht?
5. Rezeption durch Glossatoren: Hat Johanns von Buch Glosse das Sachsenspiegelrecht verfaelscht?

## Methodik

- Sachsenspiegel-Text: MGH-Edition von Karl August Eckhardt (1955/56) oder Faksimile-Ausgaben der Heidelberger Handschrift
- Textvergleich: Landrecht-Handschriften unterscheiden sich erheblich
- Sekundaerliteratur: Clausdieter Schott, Karl Kroeschell, Karin Nehlsen-von Stryk
- Keine Gegenwartsbegriffe (Eigentumsrecht, Schuldrecht) unreflektiert anwenden

---

## Skill: `bverfg-und-nachkriegskonsolidierung`

_Deutsche Rechtsgeschichte: BVerfG und Nachkriegskonsolidierung. Errichtung des BVerfG 1951, Fruehe Leitentscheidungen (SRP-Verbot BVerfGE 2-1, KPD-Verbot BVerfGE 5-85), Elfes-Urteil und Aufbau der Grundrechtsdogmatik im Deutsche Rechtsgeschichte._

# BVerfG und Nachkriegskonsolidierung

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Das Bundesverfassungsgericht (BVerfG) wurde am 7. September 1951 in Karlsruhe errichtet. Die fruehen Leitentscheidungen praegten das politische Profil der BRD: SRP-Verbot (BVerfGE 2, 1, 1952): Erste Parteiverbotsklage, NS-Nachfolgepartei. KPD-Verbot (BVerfGE 5, 85, 1956): Verbot der Kommunistischen Partei, Auseinandersetzung mit der DDR. Elfes-Urteil (BVerfGE 6, 32, 1957): Allgemeine Handlungsfreiheit aus Art. 2 Abs. 1 GG. Lueths Boykottaufruf (BVerfGE 7, 198, 1958): Drittwirkung der Grundrechte, Ausstrahlungswirkung. Diese Entscheidungen gruendeten die demokratische Kultur der BRD auf verfassungsrechtlichem Fundament.

## Kernnormen / Kernquellen

- **BVerfGE 2, 1** (1952): SRP-Verbot, Art. 21 Abs. 2 GG
- **BVerfGE 5, 85** (1956): KPD-Verbot, streitbare Demokratie
- **BVerfGE 6, 32** (1957): Elfes, allgemeine Handlungsfreiheit Art. 2 Abs. 1 GG
- **BVerfGE 7, 198** (1958): Lueths Urteil, Ausstrahlungswirkung der Grundrechte
- **BVerfGG 1951 (BGBl. I 1951, 243)**: Verfahrensrecht des BVerfG

## Akteure und Institutionen

- **Hermann Hoepker Aschoff** (1883-1954): Erster BVerfG-Praesident
- **Gerhard Leibholz** (1901-1982): BVerfG-Richter, Parteienstaat-Lehre
- **Erich Lueths** (1902-1991): Klaeger im Lueths-Urteil, Hamburger Senatspressechef
- **SRP und KPD**: Verbotene Parteien

## Typische Streitfragen / Forschungsfragen

1. War das KPD-Verbot 1956 mit dem Verhueltnis zur SRP 1952 konsistent?
2. Lueths-Urteil: Ist die Ausstrahlungswirkung der Grundrechte dogmatisch sauber?
3. Parteiverbot als demokratisches Instrument: Schutzt es die Demokratie oder staerrkt es den Staat?
4. BVerfGG und Richterwahl: War das Zwei-Drittel-Quorum von Anfang an vorgesehen?
5. Fruehe BRD-Verfassungsidentitaet: Wie stark praegte das BVerfG die westdeutsche Demokratie?

## Methodik

- BVerfGE: bverfg.de für vollstaendige Entscheidungen (BVerfGE 2, 1; 5, 85; 6, 32; 7, 198)
- BVerfGG: gesetze-im-internet.de
- Sekundaerliteratur: Uwe Wesel, Geschichte des Rechts (1. und 2. Teil)
- Leibholz Strukturprobleme der modernen Demokratie (1958): historische Ausgabe

---

## Skill: `juristenausbildung-und-pruefungswesen`

_Deutsche Rechtsgeschichte: Juristenausbildung und Pruefungswesen. Universitaetsrechtsstudium seit Mittelalter, Referendariat, Erste und Zweite Staatspruefung, NS-Gleichschaltung der Ausbildung und Reformen bis heute im Deutsche Rechtsgeschichte._

# Juristenausbildung und Pruefungswesen

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Die Juristenausbildung in Deutschland ist historisch gewachsen. Das mittelalterliche Rechtsstudium in Bologna wurde ab dem 13. Jh. an deutschen Universitaeten (Heidelberg 1386, Koeln 1388, Erfurt 1392) eingebaut. Im 19. Jh. entstand das Referendariatsystem: Erste Staatspruefung nach Universitaet, Referendariat als praktische Ausbildung, Zweite Staatspruefung (Assessorexamen). Das NS-Regime schaltete die Juristenausbildung gleich: Juedinnen und Juden wurden ausgeschlossen, nationalsozialistische Inhalte eingefuehrt. Nach 1945 normalisierte sich die Ausbildung, aber Reformen blieben spaerlich. Das Juristenausbildungsgesetz regelt heute landesrechtlich; das DRiG bestimmt Bundesgrundsaetze.

## Kernnormen / Kernquellen

- **DRiG § 5 (BGBl. I 1961, 713)**: Befahigung zum Richteramt, Zweiexamens-System
- **DRiG §§ 5-7**: Erste Pruefung, Vorbereitungsdienst, Zweite Pruefung
- **JAG der Länder** (z. B. NRW JAG 2003): Einzelheiten der Juristenausbildung
- **Erste Verordnung zur Durchfuehrung des Berufsbeamtengesetzes 1933 (RGBl. I 1933, 245)**: Judenausschluss aus Staatsdienst und damit aus juristischen Staatsberufen

## Akteure und Institutionen

- **Universitaet Heidelberg (gegr. 1386)**: Erste deutsche Volluniversitaet mit Rechtsfakultaet
- **Friedrich Savigny** als Universitaetsprofessor: Akademisches Leitbild für Juristenausbildung
- **NS-Reichsjustizministerium**: Gleichschaltung des Jurastudiums
- **Deutsche Richterakademie (Trier/Wustrau)**: Richterfortbildung seit 1966

## Typische Streitfragen / Forschungsfragen

1. Einstufige vs. zweistufige Juristenausbildung: Wurde die einstufige Ausbildung zu Unrecht aufgegeben?
2. Universitaets-Schwerpunktbereichspruefung seit 2003: Sinnvolle Reform oder Absenkung?
3. NS-Gleichschaltung: Wie praegend war sie für die Nachkriegsjuristengeneration?
4. Referendariat: Wessen Interessen bedient das heutige Referendariat?
5. Bologna-Reform im Jura-Studium: Warum wurde die Einheitlichkeit erhalten?

## Methodik

- DRiG: gesetze-im-internet.de
- JAG der Länder: jeweilige Landesrechtsportale (z. B. recht.nrw.de)
- NS-Hochschulrecht: RGBl. I 1933, 245 via ALEX/OeNB
- Sekundaerliteratur: Bernd Rueers Rechtstheorie und Uwe Wesels Geschichte des Rechts

---

## Skill: `preussisches-allgemeines-landrecht`

_Deutsche Rechtsgeschichte: Preussisches Allgemeines Landrecht (ALR) von 1794. Entstehung unter Friedrich dem Grossen und Svarez, kasuistische Kodifikationstechnik, Inhalt und Scheitern als gesamtdeutsches Zivilrecht im Deutsche Rechtsgeschichte._

# Preussisches Allgemeines Landrecht (ALR 1794)

## Historische Quellenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `Art. 20 Abs. 3 GG` — rechtsstaatlicher Gegenwartsanker.
- `Art. 1 Abs. 1 GG` — Menschenwuerde als Zäsur- und Kontinuitaetsmassstab.
- `Art. 123 Abs. 1 GG` — Fortgeltung vorkonstitutionellen Rechts.
- `Art. 125 GG` — Fortgeltung als Bundesrecht.
- `Art. 126 GG` — Meinungsverschiedenheiten ueber Fortgeltung.
- `Art. 20 Einigungsvertrag` — öffentlicher Dienst und Rechtsuebergang.
- `Art. 21 Einigungsvertrag` — Verwaltungsvermögen.
- `Art. 22 Einigungsvertrag` — Finanzvermoegen.
- `§ 1 VermG` — Anwendungsbereich Vermögensgesetz.
- `§ 3 VermG` — Rückübertragung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Das Allgemeine Landrecht für die Preussischen Staaten (ALR) trat am 1. Juni 1794 in Kraft (Preussisches Gesetzblatt 1794). Es umfasste ca. 17000 Paragraphen und war die umfassendste Rechtskodifikation vor dem Code Civil. Grundlage war Vernunftrecht (Svarez, Cocceji). Die Kodifikationstechnik war kasuistisch: Einzelfaelle loesen statt Generalklauseln. Das ALR regelte alle Rechtsgebiete: Privatrecht, Familienrecht, Erbrecht, Grundbesitz, Staendeverhaeltnisse und öffentliches Recht. Es galt in Preussen bis 1900 (Ablosung durch BGB) und hatte erheblichen Einfluss auf ostmitteleuropaeische Rechtsordnungen.

## Kernnormen / Kernquellen

- **ALR I 1**: Recht und Rechtspflichten im Ueberblick
- **ALR I 5-6 (Vertragsrecht)**: Vertragsfreiheit mit sozialstaatlichen Einschraenkungen
- **ALR I 8 (Eigentumsrecht)**: Eigentumsinhalt und Nutzungsrecht
- **ALR II 1 (Eherecht)**: Ehe als buergerlicher Vertrag
- **ALR II 14 (Staedte und Staende)**: Staendische Gliederung
- **ALR Einleitung §§ 1-23**: Methodische und vernunftrechtliche Grundlagen

## Akteure und Institutionen

- **Friedrich II. (der Grosse)** (1712-1786): Politischer Initiator des ALR
- **Samuel von Cocceji** (1679-1755): Erster Konzipient unter Friedrich II.
- **Carl Gottlieb Svarez** (1746-1798): Hauptredaktor des ALR
- **Johann Heinrich Casimir von Carmer** (1720-1801): Justizminister und Auftraggeber Svarez'

## Typische Streitfragen / Forschungsfragen

1. ALR als Vernunftrechtskodifikation oder Staatsabsolutismusinstrument?
2. Kasuistik des ALR: War sie Schwaeche oder bewusste Entscheidung für Rechtssicherheit?
3. Warum scheiterte das ALR als gesamtdeutsches Zivilrecht?
4. Staendischer Aufbau des ALR: Modernisierung oder Konservierung von Feudalstrukturen?
5. ALR und BGB 1900: Was blieb als Einfluss? Was wurde aufgegeben?

## Methodik

- ALR: historische Druckausgaben Svarez' (1794) oder Faksimile; ALEX/OeNB
- BGB-Vergleich: Mugdan Bd. I-VI für fachliche Einordnung
- Sekundaerliteratur: Reinhart Koselleck, Preussen zwischen Reform und Revolution (1967)
- Keine Anwendung heutiger BGB-Kategeorien auf ALR ohne expliziten Vergleich

---

## Skill: `seminar-und-vortrag-rechtsgeschichte`

_Deutsche Rechtsgeschichte: Seminarvorbereitung und Vortrag. Strukturierung eines rechtshistorischen Referats oder Seminarvortrags zu Sachsenspiegel, BGB-Entstehung, Weimar oder NS-Recht mit quellengestuetzten Thesen im Deutsche Rechtsgeschichte._

# Seminar und Vortrag Rechtsgeschichte

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: historisch — Verjährung nach jeweiliger Quelle; heutige Relevanz über Art. 184 ff. EGBGB und Auslegungshilfe für Grundrechtsverständnis.
- Tragende Normen verifizieren: Sachsenspiegel, Schwabenspiegel, Carolina (CCC 1532), Preußisches ALR 1794, Code civil (1804), Sächsisches BGB 1865, BGB 1900, WRV 1919, GG 1949; rechtshistorische Quellen MGH, Constitutiones — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Rechtshistoriker, Quelleneditionen, Lehrstühle für deutsche Rechtsgeschichte, Verfassungsrechtler (Auslegungshintergrund), Restitutionsverfahren mit historischem Anker.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Quellenedition, rechtshistorisches Gutachten, Vorlesungsskript, dogmenhistorischer Aufsatz, Verfassungsentstehungsgeschichte — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Worum es geht

Ein rechtshistorisches Seminar oder Referat braucht andere Kompetenzen als ein dogmatisches Gutachten. Kern ist die quellenkritische These: Warum gilt das, was ich behaupte, und welche Quelle belegt es? Das Seminarreferat in der Rechtsgeschichte folgt typischerweise: (1) Fragestellung und Einordnung, (2) Quellen und Methode, (3) historische Entwicklung, (4) Wendepunkte und Kontroversen, (5) Gegenwartsrelevanz und Fazit. Praxisrelevant sind: Sachsenspiegel-Seminare (Quellenkritik Handschriften), BGB-Entstehungsseminare (Mugdan-Arbeit), WRV-Seminare (Art. 48-Debatte), NS-Rechtsseminare (Widerstandsrecht).

## Kernnormen / Kernquellen

- **Sachsenspiegel Ldr. I 1-5**: Typische Textstellen für Seminareinstieg
- **Mugdan, Die gesamten Materialien zum BGB** (1899): Pflichtlektuere für BGB-Entstehungsseminar
- **WRV Art. 48 und Art. 76**: Zentrale Streitartikel für WRV-Seminar
- **Ermächtigungsgesetz 1933 (RGBl. I 1933, 141)**: Kernquelle für NS-Rechtsseminar
- **GG Art. 1, 20 Abs. 4**: Wuerdegarantie und Widerstandsrecht als GG-Reaktion auf NS

## Akteure und Institutionen

- **Eike von Repgow**: Sachsenspiegel-Verfasser, zentrale Person in Sachsenspiegel-Seminaren
- **Bernhard Windscheid** (1817-1892): Pandektist, Brucke zwischen Roemischem Recht und BGB
- **Hugo Preuß** (1860-1925): WRV-Architekt
- **Ernst Fraenkel** (1898-1975): Doppelstaat (1941), Schluessel zum Verstaendnis des NS-Rechts

## Typische Streitfragen / Forschungsfragen

1. Wie zitiert man Handschriften des Sachsenspiegels im Seminar korrekt?
2. Muendliche vs. schriftliche Kultur im mittelalterlichen Recht: Wie erklaere ich das im Vortrag?
3. BGB-Entstehung: Welche Stelle in Mugdan für welche These?
4. Art. 48 WRV: War Bruenings Notverordnungspolitik verfassungsmaessig?
5. NS-Recht: Kann man das als Recht bezeichnen? (Radbruch-Formel und ihre Grenzen)

## Methodik

- Klares Thesenpapier mit Quellen-Map vor dem Vortrag erstellen
- Sachsenspiegel-Handschriften: MGH-Digitalisate, Landesbibliotheken
- Mugdan-Belegkette: Motiv → Protokoll → Text
- WRV-Dokumente: documentArchiv.de, Reichsgesetzblatt-ALEX
- NS-Quellen: ALEX/ÖNB für RGBl. I

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

