---
name: kompendium-21-spezial-referenten-z-bis-zirkelschluss-pruefe
description: "legistik-werkstatt: Konsolidiertes Skill-Kompendium 21; bündelt 8 frühere Spezialskills (spezial-referenten-zahlen-schwellen-und-berechnung, spezial-vorlagen-mehrparteien-konflikt-und-interessen, synopse-erstellen, terminologie-konsistenz, verfassungsmaessigkeit-quercheck und 3 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 21 - legistik-werkstatt

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `spezial-referenten-zahlen-schwellen-und-berechnung` | Referenten: Zahlen, Schwellenwerte und Berechnung im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-vorlagen-mehrparteien-konflikt-und-interessen` | Vorlagen: Mehrparteienkonflikt und Interessenmatrix im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `synopse-erstellen` | Synopse als Dreispalten-Tabelle bisheriges Recht neues Recht Aenderungsbefehl erstellen. Anwendungsfall Ressortabstimmung Bundestag oder Bundesrat brauchen vergleichende Darstellung um Aenderungen schnell zu erfassen. Pro geaendertem Paragrafen eine Zeile oder Block pro Stammgesetz eigene Synopsen-Tabelle. Spalten gleich breit druckbar A4 quer oder A3. Output Synopsen-Tabelle Markdown plus DOCX-Vorlage. Anschluss lesefassung-konsolidiert. Abgrenzung zu xml-paralleldarstellung maschinenlesbare Ausgabe. |
| `terminologie-konsistenz` | Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen. Anwendungsfall Entwurf enthaelt neue Legaldefinitionen oder Referent prüft ob Begriffe konsistent verwendet werden und keine ungewollten Abweichungen von bestehenden Legaldefinitionen in anderen Gesetzen vorliegen. Faustregel ein Begriff eine Bedeutung. Prüfung gegen HdR und GGO. Abweichung gerechtfertigt und ausdrücklich oder versehentliche Bruchbildung. Output Begriffsliste kritische Faelle markiert Aenderungsvorschlag. |
| `verfassungsmaessigkeit-quercheck` | Querschnittsprüfung Verfassungsmäßigkeit eines Gesetzesentwurfs oder einer Verordnung. Anwendungsfall Entwurf soll vor Ressortabstimmung oder NKR-Vorlage verfassungsrechtlich abgesichert werden oder Verband prüft eingegangenen Entwurf. Grundrechte Schutzbereich Eingriff Rechtfertigung Verhältnismäßigkeit. Gleichbehandlung Art. 3 GG Berufsfreiheit Art. 12 GG Drei-Stufen-Theorie Eigentum Art. 14 GG Bestimmtheitsgebot Art. 20 Abs. 3 GG bei Strafnormen Art. 103 Abs. 2 GG. Wesentlichkeitstheorie BVerfG Selbstverwaltungsgarantie Art. 28 Abs. 2 GG. Output Querprotokoll konkrete Aenderungsempfehlungen. Abgrenzung zu europarechtskonformität EU-Recht. |
| `verordnungsermaechtigung-art80` | Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird. Anwendungsfall geplante Rechtsverordnung und Anwalt oder Referent fragt ob Ermaechtigungsgrundlage genuegend bestimmt ist. Bestimmtheitstrias Inhalt Zweck Ausmass muessen im ermaechtigenden Gesetz stehen. Prüfung ob Ermaechtigung das Regelungsziel deckt Sub-Delegation Art. 80 Abs. 1 S. 4 GG. Landesebene Landesverfassung parallel zu Art. 80 GG. Wenn Ermaechtigung fehlt zunaechst Gesetzgebungsverfahren. Output Prüfprotokoll Empfehlung Verordnung auf welcher Grundlage oder Ermaechtigung schaerfen. Abgrenzung zu gesetzgebungskompetenz-prüfen Kompetenztitel. |
| `xml-paralleldarstellung` | Maschinenlesbare Paralleldarstellung eines Gesetzesentwurfs in LegalDocML.de oder eNorm-XML erstellen. Anwendungsfall eGesetzgebung BMJ Bundesgesetzblatt online oder automatisierte Weiterverarbeitung erfordert strukturierte XML-Ausgabe. Akoma-Ntoso bzw. eNorm-Schema des Bundes Hauptnorm Aenderungsnorm Begründung Inkrafttreten. Metadaten Federführendes Ressort Aktenzeichen Stand Verfahrensstand Landesrecht analog. Schemavalidierung. Output XML-Datei Schemavalidierungs-Protokoll. Abgrenzung zu synopse-erstellen menschenlesbare Tabelle. |
| `zirkelschluss-pruefen` | Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren. Anwendungsfall Entwurf enthaelt viele Querverweise und soll auf ungewollte Zirkel und tautologische Definitionen geprüft werden. Direkte Zirkel A verweist auf A indirekte Zirkel A verweist B B verweist C C verweist A. Tautologische Definitionen Vermutung der Vermutung. Dynamische Verweisungen auf EU-Recht Prüfung Reichweite statische Verweisungen Datum der Fassung. Erstellt Verweisgraf markiert problematische Kanten. Output Liste der zu entzerrenden Stellen. Anschluss terminologie-konsistenz normenkartierung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `spezial-referenten-zahlen-schwellen-und-berechnung`

**Frühere Beschreibung:** Referenten: Zahlen, Schwellenwerte und Berechnung im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Referenten: Zahlen, Schwellenwerte und Berechnung

## Spezialwissen: Referenten: Zahlen, Schwellenwerte und Berechnung
- **Spezialgegenstand:** Referenten: Zahlen, Schwellenwerte und Berechnung / spezial referenten zahlen schwellen und berechnung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** XML.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Referenten** prüfen.
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

## 2. `spezial-vorlagen-mehrparteien-konflikt-und-interessen`

**Frühere Beschreibung:** Vorlagen: Mehrparteienkonflikt und Interessenmatrix im Plugin legistik werkstatt; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vorlagen: Mehrparteienkonflikt und Interessenmatrix

## Spezialwissen: Vorlagen: Mehrparteienkonflikt und Interessenmatrix
- **Spezialgegenstand:** Vorlagen: Mehrparteienkonflikt und Interessenmatrix / spezial vorlagen mehrparteien konflikt und interessen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** XML.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vorlagen** prüfen.
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

## 3. `synopse-erstellen`

**Frühere Beschreibung:** Synopse als Dreispalten-Tabelle bisheriges Recht neues Recht Aenderungsbefehl erstellen. Anwendungsfall Ressortabstimmung Bundestag oder Bundesrat brauchen vergleichende Darstellung um Aenderungen schnell zu erfassen. Pro geaendertem Paragrafen eine Zeile oder Block pro Stammgesetz eigene Synopsen-Tabelle. Spalten gleich breit druckbar A4 quer oder A3. Output Synopsen-Tabelle Markdown plus DOCX-Vorlage. Anschluss lesefassung-konsolidiert. Abgrenzung zu xml-paralleldarstellung maschinenlesbare Ausgabe.

# Synopse erstellen

> Drei Spalten: vorher, nachher, Änderungsbefehl. Hilft Allen.

## Aufbau einer Synopse

### Tabelle (Format Markdown / DOCX / PDF Landscape)

| Bisheriges Recht | Neues Recht | Änderungsbefehl |
|---|---|---|
| Paragraf 33 HGB (alte Fassung) Wortlaut ... | Paragraf 33 HGB (neue Fassung) Wortlaut ... | Paragraf 33 wird wie folgt gefasst ... |

### Pro Stammgesetz eine eigene Datei

- Synopse_HGB.md
- Synopse_ZPO.md
- Synopse_FamFG.md

### Spaltenbreite

DOCX: ca. 33 Prozent / 33 Prozent / 34 Prozent. Bei langen Sätzen A3 Landscape oder DIN A4 mit kleiner Schrift.

## Kennzeichnung von Änderungen

- Eingefügte Worte: **fett** oder Doppelunterstreichung
- Gestrichene Worte: ~~Durchstreichung~~ oder kursiv mit Hinweis "entfaellt"
- Bei voelliger Neufassung: Spalte "Bisheriges Recht" "Aufgehoben (alte Fassung in Anlage)"

## Lesefassung in separater Datei

Synopse ist gut für den Vergleich. Eine **Lesefassung** zeigt die geänderte Norm in einer einheitlich gelesenen Fassung.

Beispiel "Lesefassung_HGB_Paragraf_33.md" - das ist der Paragraf, wie er nach Inkrafttreten lautet.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 42-48 GGO (Synopse als Bestandteil der Begr.) — §§ 1-4 HdR (Rechtsfoermlichkeit, Vergleichs-Darstellungen) — Art. 76 Abs. 2 GG (Einbringungs-Unterlagen inkl. erlaeuternder Materialien)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anschluss

`lesefassung-konsolidiert`.

## 4. `terminologie-konsistenz`

**Frühere Beschreibung:** Terminologie-Konsistenz im legistischen Entwurf prüfen und Begriffstabelle aufbauen. Anwendungsfall Entwurf enthaelt neue Legaldefinitionen oder Referent prüft ob Begriffe konsistent verwendet werden und keine ungewollten Abweichungen von bestehenden Legaldefinitionen in anderen Gesetzen vorliegen. Faustregel ein Begriff eine Bedeutung. Prüfung gegen HdR und GGO. Abweichung gerechtfertigt und ausdrücklich oder versehentliche Bruchbildung. Output Begriffsliste kritische Faelle markiert Aenderungsvorschlag.

# Terminologie-Konsistenz

> Ein Wort, eine Bedeutung. Quer durch die ganze Rechtsordnung.

## Schritt 1 - Begriffsernte

Alle in der Norm verwendeten Fachbegriffe sammeln. Substantive zuerst, dann Adjektive und Verben, die definierte Bedeutung haben.

## Schritt 2 - Prüfung "schon definiert?"

Pro Begriff suchen:

- Stammgesetz (interne Definition?)
- HGB, BGB, ZPO, StPO, VwGO, SGB I (Allgemeine Begriffe)
- DSGVO (personenbezogene Daten, Verarbeitung, Verantwortlicher etc.)
- EU-VO (DSA, DMA, AI Act, eIDAS 2.0)
- Landesgesetze des betreffenden Landes

## Schritt 3 - Konsistenz-Matrix

| Begriff | Definition Entwurf | Andere Norm | Abweichung | Bewertung | Vorschlag |
|---|---|---|---|---|---|
| Postfach | elektr. Postf. | beA-Verordnung | beA = nur Anwalt | bewusst weiter | OK, andere Bezeichnung wählen |
| Unternehmen | iSd HGB | DSA Art. 3 g | DSA umfasst auch Plattformen ohne HReg | nein | Verweis auf DSA klarstellen |
| Zweigniederlassung | iSd HGB | Niederlassung iSd EU | abweichend | nein | Wahl klarstellen |

## Schritt 4 - HdR-Test

Handbuch der Rechtsförmlichkeit des Bundes (BMJ, 3. Auflage 2008, in Bearbeitung 4. Auflage):

- Bestimmte Begriffe meiden ("etwaige", "gegebenenfalls" - Unbestimmtheit)
- Aktiv statt Passiv
- Singular ist Plural-feindlich, wenn Mehrzahl gemeint ist
- Praesens ist Vergangenheits-feindlich

## Schritt 5 - GGO-Test

Gemeinsame Geschäftsordnung der Bundesministerien (GGO): formale Mindestanforderungen.

## Schritt 6 - Genderaspekt

Geschlechtergerechte Sprache. Bei Personenbezeichnungen entweder:

- Paarform "die Bürgerin oder der Bürger"
- generisches Femininum oder Maskulinum
- neutrale Formulierung "die Person"

Inkonsistenz vermeiden - eine Formel je Gesetz.

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 43-46 HdR (einheitliche Begriffsverwendung, Terminologie-Gebot) — Art. 20 Abs. 3 GG (Bestimmtheitsgebot, Normenklarheit) — § 288 AEUV (EU-Richtlinie verlangt einheitliche terminologische Umsetzung) — §§ 1-5 DIN 1422 (Norm Terminologie-Konsistenz in Rechtstexten)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Begriffstabelle als Anhang zum Entwurf. Kritische Fälle (Bruchbildung) markiert.

## Anschluss

`zirkelschluss-pruefen`, dann `referentenentwurf-bauen`.

## 5. `verfassungsmaessigkeit-quercheck`

**Frühere Beschreibung:** Querschnittsprüfung Verfassungsmäßigkeit eines Gesetzesentwurfs oder einer Verordnung. Anwendungsfall Entwurf soll vor Ressortabstimmung oder NKR-Vorlage verfassungsrechtlich abgesichert werden oder Verband prüft eingegangenen Entwurf. Grundrechte Schutzbereich Eingriff Rechtfertigung Verhältnismäßigkeit. Gleichbehandlung Art. 3 GG Berufsfreiheit Art. 12 GG Drei-Stufen-Theorie Eigentum Art. 14 GG Bestimmtheitsgebot Art. 20 Abs. 3 GG bei Strafnormen Art. 103 Abs. 2 GG. Wesentlichkeitstheorie BVerfG Selbstverwaltungsgarantie Art. 28 Abs. 2 GG. Output Querprotokoll konkrete Aenderungsempfehlungen. Abgrenzung zu europarechtskonformität EU-Recht.

# Verfassungsmaessigkeit-Quercheck

> Nicht jeder Entwurf ist verfassungsgemäß, weil er gut gemeint ist.

## Pruefstation 1 - Welche Grundrechte sind betroffen?

Prüfen pro Adressat:

- Art. 1 GG Menschenwürde
- Art. 2 GG allgemeine Handlungsfreiheit, Recht auf koerperliche Unversehrtheit
- Art. 3 GG Gleichheit
- Art. 4 GG Religionsfreiheit
- Art. 5 GG Meinungsfreiheit, Pressefreiheit, Rundfunk
- Art. 6 GG Ehe und Familie
- Art. 8 GG Versammlung
- Art. 9 GG Vereinigung
- Art. 10 GG Brief- Post- und Fernmeldegeheimnis
- Art. 12 GG Berufsfreiheit
- Art. 13 GG Unverletzlichkeit der Wohnung
- Art. 14 GG Eigentum
- Art. 16 GG Auslieferung
- Art. 17 GG Petitionsrecht

## Pruefstation 2 - Prüfraster pro Grundrecht

1. Schutzbereich (persönlich und sachlich)
2. Eingriff
3. Rechtfertigung
   - verfassungsmaessige Schranke
   - Schranken-Schranken (insbesondere Verhältnismaessigkeit)
     - legitimer Zweck
     - geeignet
     - erforderlich (mildestes Mittel)
     - angemessen

## Pruefstation 3 - Art. 3 GG Gleichbehandlung

Bei Ungleichbehandlung: ist sie sachlich gerechtfertigt? Wenn personenbezogen: strenge Prüfung (neue Formel BVerfG E 88 / 87).

## Pruefstation 4 - Art. 12 GG Berufsfreiheit

Drei-Stufen-Theorie (BVerfGE 7 / 377 Apotheker):
- Berufsausübung: leichter zu rechtfertigen
- Subjektive Zulassung: sachliche Gründe, Verhältnismaessigkeit
- Objektive Zulassung: überwiegende Interessen der Allgemeinheit

## Pruefstation 5 - Art. 14 GG Eigentum

- Inhalts- und Schrankenbestimmung (regelmäßiger Eingriff)
- Enteignung (zugriff auf Eigentum gegen Entschädigung)
- ausgleichspflichtige Inhaltsbestimmung (BVerfG)

## Pruefstation 6 - Art. 20 Abs. 3 GG Rechtsstaat

- Vorrang des Gesetzes
- Vorbehalt des Gesetzes
- Bestimmtheitsgebot (besonders streng bei Eingriffsverwaltung)

## Pruefstation 7 - Art. 103 Abs. 2 GG bei Strafnormen

Bestimmtheitsgebot bei Strafnormen. Der Bürger muss erkennen, was strafbar ist.

## Pruefstation 8 - Wesentlichkeitstheorie

Wesentliche Entscheidungen muss der Gesetzgeber selbst treffen, nicht der Verordnungsgeber.

## Pruefstation 9 - Art. 28 Abs. 2 GG Selbstverwaltungsgarantie

Wenn der Entwurf in kommunale Angelegenheiten eingreift: Eingriff in Selbstverwaltungsgarantie? Erforderlich? Verhältnismaessig?

## Pruefstation 10 - Demokratieprinzip Art. 20 Abs. 2 GG

Bei dynamischen Verweisungen auf EU-Recht oder andere externe Stellen: ist die demokratische Legitimation gewahrt?

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 1 Abs. 3 GG (Grundrechtsbindung) — Art. 3 GG (Gleichheitsgebot) — Art. 12 GG (Berufsfreiheit, Drei-Stufen-Theorie) — Art. 14 GG (Eigentum) — Art. 20 Abs. 3 GG (Wesentlichkeitstheorie, Bestimmtheit) — Art. 28 Abs. 2 GG (kommunale Selbstverwaltung)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Tabellarisches Querprotokoll mit allen einschlaegigen Grundrechten plus Prüfergebnis plus Empfehlung.

## Anschluss

`folgenabschaetzung-erfuellungsaufwand`.

## 6. `verordnungsermaechtigung-art80`

**Frühere Beschreibung:** Verordnungsermaechtigung nach Art. 80 Abs. 1 GG prüfen bevor Rechtsverordnung entworfen wird. Anwendungsfall geplante Rechtsverordnung und Anwalt oder Referent fragt ob Ermaechtigungsgrundlage genuegend bestimmt ist. Bestimmtheitstrias Inhalt Zweck Ausmass muessen im ermaechtigenden Gesetz stehen. Prüfung ob Ermaechtigung das Regelungsziel deckt Sub-Delegation Art. 80 Abs. 1 S. 4 GG. Landesebene Landesverfassung parallel zu Art. 80 GG. Wenn Ermaechtigung fehlt zunaechst Gesetzgebungsverfahren. Output Prüfprotokoll Empfehlung Verordnung auf welcher Grundlage oder Ermaechtigung schaerfen. Abgrenzung zu gesetzgebungskompetenz-prüfen Kompetenztitel.

# Verordnungsermaechtigung Art. 80 GG

> Eine Rechtsverordnung ohne Ermaechtigung ist nichtig. Eine Rechtsverordnung mit zu unbestimmter Ermaechtigung ist nichtig.

## Pruefstation 1 - Existiert eine Ermaechtigungsnorm?

Suche im Fachgesetz nach Paragrafen wie:

- "Das Bundesministerium ... wird ermaechtigt, durch Rechtsverordnung ..."
- "Die Landesregierung wird ermaechtigt ..."

Wenn nichts vorhanden: keine VO möglich. Erst Gesetzgebungsverfahren, um Ermaechtigung zu schaffen.

## Pruefstation 2 - Bestimmtheitstrias Art. 80 Abs. 1 Satz 2 GG

Die Ermaechtigung muss bestimmen:

- **Inhalt** - was die VO regeln darf
- **Zweck** - wozu die VO erlassen werden darf
- **Ausmass** - in welcher Tiefe und Breite

Test: Kann der Bürger aus dem Gesetz vorhersehen, was die VO regeln darf?

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Pruefstation 3 - Sub-Delegation

Art. 80 Abs. 1 Satz 4 GG: Wenn ein Gesetz die Befugnis weiter übertragbar macht, muss das im Gesetz steht ("Diese Befugnis kann durch Rechtsverordnung weiter übertragen werden"). Ohne diese Klausel keine Weiterübertragung.

## Pruefstation 4 - Zustimmung Bundesrat

Manche Ermaechtigungen sehen Zustimmung des Bundesrates vor (Art. 80 Abs. 2 GG, wenn Bundesgesetz der Zustimmung des Bundesrates bedurfte, bedarf in der Regel auch die zugehoerige VO der Zustimmung).

## Pruefstation 5 - Anhörung von Beteiligten

Manche Spezialgesetze verlangen Anhörung von Sachverständigen oder Verbänden vor Erlass der VO (z.B. BImSchG Paragraf 51).

## Pruefstation 6 - Citatum-Pflicht Art. 80 Abs. 1 Satz 3 GG

Die VO muss die Rechtsgrundlage angeben. Format: "Auf Grund des Paragraf X des Y-Gesetzes vom ZZ.ZZ.JJJJ verordnet die Bundesregierung ..."

## Landesebene

Auf Landesebene gilt regelmäßig Art. 80 GG analog über die Landesverfassungen (z.B. Bayerische Verfassung Art. 55 Nr. 2 Satz 3, NRW Art. 70). Die Bestimmtheitstrias gilt auch dort.

## Pruefprotokoll

| Pruefpunkt | Antwort | Quelle |
|---|---|---|
| Ermaechtigungsnorm vorhanden | Ja/Nein | Paragraf X |
| Inhalt klar | Ja/Nein | Wortlaut |
| Zweck klar | Ja/Nein | Wortlaut |
| Ausmass klar | Ja/Nein | Wortlaut |
| Sub-Delegation möglich | Ja/Nein | Wortlaut |
| Bundesrats-Zustimmung | Ja/Nein | Wortlaut + Stammgesetz |
| Anhörungspflichten | Ja/Nein | Spezialgesetz |

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 80 Abs. 1 GG (Ermaechtigungs-Bestimmtheitstrias) — Art. 80 Abs. 1 Satz 4 GG (Sub-Delegation) — Art. 80 Abs. 2 GG (Bundesrats-Zustimmung) — § 51 BImSchG (Beispiel-Ermaechtigungsnorm mit Anhoerungspflicht)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Pruefprotokoll plus Empfehlung:

1. VO kann auf bestehender Grundlage ergehen
2. VO erfordert vorherige Schaerfung der Ermaechtigung im Stammgesetz
3. VO ist nicht das richtige Instrument, formales Gesetz erforderlich (Wesentlichkeitstheorie)

## Anschluss

`normenkartierung` und `referentenentwurf-bauen` (mit korrektem Citatum).

## 7. `xml-paralleldarstellung`

**Frühere Beschreibung:** Maschinenlesbare Paralleldarstellung eines Gesetzesentwurfs in LegalDocML.de oder eNorm-XML erstellen. Anwendungsfall eGesetzgebung BMJ Bundesgesetzblatt online oder automatisierte Weiterverarbeitung erfordert strukturierte XML-Ausgabe. Akoma-Ntoso bzw. eNorm-Schema des Bundes Hauptnorm Aenderungsnorm Begründung Inkrafttreten. Metadaten Federführendes Ressort Aktenzeichen Stand Verfahrensstand Landesrecht analog. Schemavalidierung. Output XML-Datei Schemavalidierungs-Protokoll. Abgrenzung zu synopse-erstellen menschenlesbare Tabelle.

# XML-Paralleldarstellung

> Recht muss auch Maschinen lesbar sein.

## Schemas

### Bund

- **eNorm** des Bundes (XML-Schema des BMJ)
- **LegalDocML.de** (auf Basis Akoma Ntoso, OASIS-Standard)

### Land

Landesrecht-Portale verwenden teilweise eigene XML-Formate, teilweise LegalDocML.de.

## Mindeststruktur

```xml
<akomaNtoso xmlns="http://docs.oasis-open.org/legaldocml/ns/akn/3.0">
  <act name="entwurf-paragraf-33a-hgb">
    <meta>
      <identification source="#bmj">
        <FRBRWork>
          <FRBRthis value="/akn/de/act/2026/pflichtpostfachg"/>
          <FRBRuri value="/akn/de/act/2026/pflichtpostfachg"/>
          <FRBRdate date="2026-05-23" name="Auftragsdatum"/>
          <FRBRauthor href="#bmj"/>
          <FRBRcountry value="de"/>
        </FRBRWork>
      </identification>
    </meta>
    <body>
      <article eId="art_1">
        <num>Artikel 1</num>
        <heading>Aenderung des Handelsgesetzbuchs</heading>
        <paragraph eId="art_1__para_1">
          <content>
            <p>Das Handelsgesetzbuch ... wird wie folgt geaendert: ...</p>
          </content>
        </paragraph>
      </article>
    </body>
  </act>
</akomaNtoso>
```

## Prüfung

Schema-Validierung via xmllint:

```
xmllint --schema akomaNtoso-3.0.xsd --noout entwurf.xml
```

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

§§ 1-5 eGovG (E-Government-Gesetz, Digitalisierungspflichten) — §§ 3a, 3b VwVfG (elektronisches Verwaltungshandeln) — § 2 ERVV (Dokumentenformat-Anforderungen) — ISO 8879 (SGML/XML-Standard) — LegalDocML-Standard (OASIS, Parlamentsgesetze)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

XML-Datei plus Validierungs-Protokoll. Bei Fehlern korrigieren und nochmals validieren.

## Anschluss

`folgenabschaetzung-erfuellungsaufwand`.

## 8. `zirkelschluss-pruefen`

**Frühere Beschreibung:** Zirkelschluesse und kreisfreie Verweisketten im legistischen Entwurf aufspueren. Anwendungsfall Entwurf enthaelt viele Querverweise und soll auf ungewollte Zirkel und tautologische Definitionen geprüft werden. Direkte Zirkel A verweist auf A indirekte Zirkel A verweist B B verweist C C verweist A. Tautologische Definitionen Vermutung der Vermutung. Dynamische Verweisungen auf EU-Recht Prüfung Reichweite statische Verweisungen Datum der Fassung. Erstellt Verweisgraf markiert problematische Kanten. Output Liste der zu entzerrenden Stellen. Anschluss terminologie-konsistenz normenkartierung.

# Zirkelschluss prüfen

> Recht muss eindeutig sein. Wer im Kreis verweist, schafft Unbestimmtheit.

## Klassische Fallgruppen

### A - Direkter Zirkel
Paragraf 5 definiert X als das, was Paragraf 12 sagt - und Paragraf 12 definiert X als das, was Paragraf 5 sagt.

### B - Indirekter Zirkel
A -> B -> C -> A. Bei mehreren Stationen schwerer zu finden.

### C - Tautologische Definition
"Pflichtpostfach ist ein Postfach, das gemäß diesem Gesetz zur Pflicht gemacht wird." - leer.

### D - Vermutung der Vermutung
"Es wird vermutet, dass die Sache abgesandt ist, wenn die Vermutung der Abgabe besteht." - unzulaessig.

### E - Dynamische Verweisung auf eigene Norm
Eine Norm verweist auf "die jeweils gültige Fassung" eines anderen Paragrafen derselben Norm - Vorsicht, das ist meist gewollt, kann aber zum verfassungsrechtlichen Problem werden (Bestimmtheitsgebot bei Strafnormen, Art. 103 Abs. 2 GG).

## Prüfverfahren

### Schritt 1 - Verweisgraf aufbauen

Alle Verweise im Entwurf erfassen: "Quelle-Paragraf X verweist auf Ziel-Paragraf Y". Tabellarisch oder als Mermaid-Graf.

### Schritt 2 - Schleifen detektieren

Algorithmisch (Tarjan / Kosaraju) oder per Hand bei kleinen Entwuerfen: gibt es eine Verweis-Kette, die zur Ausgangsnorm zurueckkehrt?

### Schritt 3 - Dynamik prüfen

Jeden Verweis klassifizieren:
- statisch (mit Datum: "Paragraf 15 in der Fassung vom 01.01.2025")
- dynamisch (ohne Datum: "Paragraf 15")
- gleitend auf EU-Recht (z.B. "Anhang I der RL 2020/2184")

Bei dynamischen Verweisen auf EU-Recht: Demokratieprinzip prüfen. Der nationale Gesetzgeber kann nicht beliebig auf jedes spätere EU-Recht verweisen.

## Prüfliste für den Entwurf

- [ ] Alle Legaldefinitionen sind selbsterklärend (keine Verweisung auf nicht definierte Begriffe)
- [ ] Keine Schleife im Verweisgraf
- [ ] Dynamische Verweise auf eigene Norm sind gewollt und klar
- [ ] Dynamische Verweise auf EU-Recht halten dem Demokratieprinzip stand

## Aktuelle Rechtsprechung & Leitsätze

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

Art. 20 Abs. 3 GG (Bestimmtheitsgebot) — §§ 1-5 HdR (Normenklarheit, Verweisungs-Regeln) — § 307 BGB (Analogie: Zirkelschluss als Klarheits-Verstoß) — §§ 133, 157 BGB (Auslegungsgrundsaetze bei zirkulaeren Formulierungen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ausgabe

Verweisgraf, Liste detektierter Schleifen, Vorschläge zur Entzerrung.

## Anschluss

`referentenentwurf-bauen`, dann `begruendung-allgemein-und-besonders`.
