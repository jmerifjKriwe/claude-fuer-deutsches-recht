---
name: verkehr-infrastrukturrecht-autonomous-driving
description: "Autonomous Driving im Verkehrs- und Infrastrukturrecht: prüft konkret Zentrales Steuerungsmodul Verkehrs- und Infrastrukturrecht, Autonomes Fahren und Strassenrecht, Spezialfall Buergerentscheid zur Strassenbahn oder Stadtbahn. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Autonomous Driving

## Arbeitsbereich

**Autonomous Driving** ordnet den Fall über die tragenden Prüffelder: Zentrales Steuerungsmodul Verkehrs- und Infrastrukturrecht, Autonomes Fahren und Strassenrecht, Spezialfall Buergerentscheid zur Strassenbahn oder Stadtbahn. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `verkehr-infrastrukturrecht-kommandocenter` | Zentrales Steuerungsmodul Verkehrs- und Infrastrukturrecht: Neues Mandat im Bereich Verkehrsinfrastruktur, Routing auf passenden Subskill. Normen: FStrG, AEG, PBefG, StVO, BauGB, FStrG, GWB (je nach Sachgebiet). Prüfraster: Sachgebiet (Planfeststellung, Sondernutzung, Ladeinfrastruktur, OEPNV, Schulwegsicherheit, Parkraum, Foerderung, Verkehrswende), Mandantenrolle, Verfahrensstand. Output Deal-Karte Verkehrsinfrastruktur mit Ampel und Routing-Empfehlung. Abgrenzung: Verwaltungsrecht allgemein siehe fachanwalt-verwaltungsrecht-Plugin; Energietrassen siehe energietrassen-planfeststellung-rechtsschutz. |
| `autonomous-driving-strassenrecht` | Autonomes Fahren und Strassenrecht: § 1d StVG, autonomes Fahren in Level 4, Genehmigung der zustaendigen Landesbehoerden, Betrieb auf festgelegter Strecke. Schnittstelle zu KI-VO Hochrisikoanwendungen, Datenschutz, Haftungsfragen. Pruefraster fuer Kommunen mit Pilotvorhaben. |
| `buergerentscheid-strassenbahn-spezial` | Spezialfall Buergerentscheid zur Strassenbahn oder Stadtbahn: kommunalrechtliche Voraussetzungen, Verhaeltnis zum Beschluss des Gemeinderats, planungsrechtliche Folgen, Foerderfaehigkeit nach GVFG bei Verzoegerung. Pruefraster. |

## Arbeitsweg

- Rolle und Ziel im Verkehrs- und Infrastrukturrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: VwVfG § 73 Auslegung 1 Monat / Einwendungen 1 Monat, UmwRG § 4 Klagefrist, VwGO § 47 Normenkontrolle 1 Jahr, BVerwGO § 50 Abs. 1 Nr. 6 erstinstanzliche Zuständigkeit BVerwG.
- Tragende Normen verifizieren: FStrG, BWaStrG, AEG, BImSchG, UVPG, ROG, BauGB §§ 38, 246, VwVfG §§ 72-78 (Planfeststellung), VwGO §§ 47 ff., BNatSchG §§ 14, 15, 34, 44, WHG §§ 8, 67, EU-FFH-RL, UmwRG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Vorhabenträger (Bund, Land, DB Netz, Autobahn GmbH), Planfeststellungsbehörde, Anhörungsbehörde, anerkannte Umweltvereinigungen (BUND, NABU), VG, OVG, BVerwG (1. Senat).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Planfeststellungsbeschluss, Erörterungsprotokoll, UVP-Bericht, FFH-Verträglichkeitsstudie, Einwendung, Klage zum BVerwG, Erlaubnis nach § 67 WHG — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `verkehr-infrastrukturrecht-kommandocenter`

**Fokus:** Zentrales Steuerungsmodul Verkehrs- und Infrastrukturrecht: Neues Mandat im Bereich Verkehrsinfrastruktur, Routing auf passenden Subskill. Normen: FStrG, AEG, PBefG, StVO, BauGB, FStrG, GWB (je nach Sachgebiet). Prüfraster: Sachgebiet (Planfeststellung, Sondernutzung, Ladeinfrastruktur, OEPNV, Schulwegsicherheit, Parkraum, Foerderung, Verkehrswende), Mandantenrolle, Verfahrensstand. Output Deal-Karte Verkehrsinfrastruktur mit Ampel und Routing-Empfehlung. Abgrenzung: Verwaltungsrecht allgemein siehe fachanwalt-verwaltungsrecht-Plugin; Energietrassen siehe energietrassen-planfeststellung-rechtsschutz.

# Verkehrs- und Infrastrukturrecht — Kommandocenter

## Zweck

Einstiegspunkt fuer alle Mandate im Verkehrs- und Infrastrukturrecht (oeffentliches Recht, Planungsrecht, Strassenrecht). Erfasst Kontext, bewertet Dringlichkeit und routet.

## Mandatsaufnahme-Triage

**Klaeren Sie zuerst:**

1. **Mandantentyp:** Gemeinde/Stadt, Vorhabentraeger (DB, Strassenbauverwaltung), privater Betroffener (Anlieger, Eigentuemer), Verband, Unternehmen?
2. **Rechtsgebiet:** Strassenplanung (FStrG, LStrG), OEPNV/Schiene (AEG, PBefG), Privatstrassenrecht, Kommunales Strassenrecht?
3. **Verfahrensstadium:** Vorabstimmung, Planfeststellung, Genehmigung, Oeffentlichkeitsbeteiligung, Widerspruch, Verwaltungsklage?
4. **Kritische Frist:** Einwendungsfrist (6 Wochen nach § 73 VwVfG), Widerspruchsfrist (1 Monat § 70 VwGO), Klagefrist (1 Monat § 74 VwGO)?
5. **Sofortmassnahme notwendig?** — Einstweiliger Rechtsschutz (§ 80 VwGO) oder Eilklage?

## Routing-Matrix

| Aufgabe | Subskill |
|---------|---------|
| Planfeststellung / Plangenehmigung | `verkehr-infrastrukturrecht-planfeststellung` |
| Sondernutzungserlaubnis | `verkehr-infrastrukturrecht-sondernutzung` |
| Ladeinfrastruktur | `verkehr-infrastrukturrecht-ladeinfrastruktur` |
| Strassenbahn / OEPNV | `verkehr-infrastrukturrecht-strassenbahn` |
| Schulwegsicherheit | `verkehr-infrastrukturrecht-schulwegsicherheit` |
| Parkraumbewirtschaftung | `verkehr-infrastrukturrecht-parkraumbewirtschaftung` |
| Foerderung / Vergabe | `verkehr-infrastrukturrecht-foerderung-vergabe` |
| Verkehrsplanung | `verkehr-infrastrukturrecht-verkehrsplanung` |
| Verkehrswende | `verkehr-infrastrukturrecht-verkehrswende` |
| Wirtschaftsverkehr | `verkehr-infrastrukturrecht-wirtschaftsverkehr` |
| Verfahrensfragen allgemein | `verkehr-infrastrukturrecht-verfahren` |

## Zentrale Normen im Ueberblick

- **§ 17 FStrG** — Planfeststellung Bundesfernstrassen
- **§ 18 AEG** — Planfeststellung Schiene
- **§ 28 PBefG** — Planfeststellung Strassenbahn
- **§§ 73, 74, 75 VwVfG** — Planfeststellungsverfahren
- **§§ 6 ff. FStrG** — Einschluss, Nutzung, Sondernutzung
- **§§ 42, 47 VwGO** — Anfechtungsklage, Normenkontrolle
- **§§ 80, 123 VwGO** — Einstweiliger Rechtsschutz
- **Art. 14, 28 GG** — Eigentumsschutz, Gemeindeautonomie

## Querschnitts-Rechtsprechung

- Rechtsprechung live pruefen: Planfeststellungsentscheidungen nur mit Gericht, Datum, Aktenzeichen und freier/amtlicher Quelle ausgeben.
- Rechtsprechung live pruefen: Abwaegungsfehler nur anhand verifizierter Entscheidungen einordnen.
- Rechtsprechung live pruefen: Art.-14-Bezuege nur anhand verifizierter Entscheidungen einordnen.

## Harte Leitplanken

- Verfahrensfristen im Planungsrecht sind praelusiv — nie versaeumen.
- Mandantenrolle bestimmt Rechte und Pflichten grundlegend.
- Einstweiliger Rechtsschutz (§ 80 VwGO) bei drohenden Vollzugshandlungen sofort pruefen.
- Anwaltliche Endkontrolle bei Einwendungen, Klagen und Antraegen.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `autonomous-driving-strassenrecht`

**Fokus:** Autonomes Fahren und Strassenrecht: § 1d StVG, autonomes Fahren in Level 4, Genehmigung der zustaendigen Landesbehoerden, Betrieb auf festgelegter Strecke. Schnittstelle zu KI-VO Hochrisikoanwendungen, Datenschutz, Haftungsfragen. Pruefraster fuer Kommunen mit Pilotvorhaben.

# Autonomes Fahren: Strassenrecht

## Spezialwissen: Autonomes Fahren: Strassenrecht
- **Spezialgegenstand:** Autonomes Fahren: Strassenrecht / autonomous driving strassenrecht. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StVG, KI, VO.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `buergerentscheid-strassenbahn-spezial`

**Fokus:** Spezialfall Buergerentscheid zur Strassenbahn oder Stadtbahn: kommunalrechtliche Voraussetzungen, Verhaeltnis zum Beschluss des Gemeinderats, planungsrechtliche Folgen, Foerderfaehigkeit nach GVFG bei Verzoegerung. Pruefraster.

# Buergerentscheid Strassenbahn

## Spezialwissen: Buergerentscheid Strassenbahn
- **Spezialgegenstand:** Buergerentscheid Strassenbahn / buergerentscheid strassenbahn spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** GVFG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


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
2. **Rechtliche Einordnung** - einschlaegige Normen, zustaendige Stellen, Verfahrensart, Darlegungs-/Beweislast und nur verifizierte Rechtsprechung.
3. **Pruefung im Gutachtenstil** - Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** - konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen und Checklisten, wo das die Lesbarkeit erhoeht.
- Anschreiben-, Antrags- oder Klageschriftsatz-Geruest, wenn die Aufgabe das verlangt.
- Quellenliste mit Gericht, Datum, Aktenzeichen, frei pruefbarem Link.

## Quellenregel
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link ausgeben; bei Unsicherheit erst verifizieren oder als zu pruefen markieren.
- Keine Paywall-, Kommentar-, Aufsatz- oder Datenbankfundstelle als tragende Aussage verwenden, wenn sie nicht durch Nutzerquelle oder dokumentierten Live-Zugriff verifiziert ist.
- Keine Kommentar-, Handbuch-, Aufsatz- oder BeckRS-/juris-Blindzitate aus Modellwissen. Literatur nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitskontext dokumentiert ist.
- Annahmen explizit als solche kennzeichnen; keine erfundenen Fundstellen, keine erfundenen Tatsachen, keine erfundenen Behoerdenpraxis-Saetze.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
