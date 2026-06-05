---
name: standardklauseln-bauleiter-nda-vertragsstrafe
description: "Standardklauseln Bauleiter NDA Vertragsstrafe im NDA-Abgleich: prüft konkret Bauleiter NDA-Standardklauseln, Vertragsstrafe pruefen, Entwurf. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Standardklauseln Bauleiter NDA Vertragsstrafe

## Arbeitsbereich

Dieser Skill behandelt **Standardklauseln Bauleiter NDA Vertragsstrafe** als zusammenhängenden Arbeitsgang im NDA-Abgleich. Im Mittelpunkt steht die Prüfung von Bauleiter NDA-Standardklauseln, Vertragsstrafe pruefen, Entwurf. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `nda-standardklauseln-bauleiter` | Bauleiter NDA-Standardklauseln: Vertraulichkeitsumfang, Empfaengerkreis, Laufzeit, Rechtsfolgen, Schriftform. Pruefraster fuer mutual und one-way NDA. |
| `nda-vertragsstrafe-pruefen` | Vertragsstrafe pruefen: Hoehe, AGB-Kontrolle §§ 305 ff. BGB, Bestimmtheitsgrundsatz, Schadensersatzkumulation oder Anrechnung. Bei Verbraucher-NDA strengere Grenzen. Bei B2B-Standard: ueblich 5000-25000 EUR pro Vorfall, Kumulation moeglich. |
| `spezial-entwurf-tatbestand-beweis-und-belege` | Entwurf: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin nda abgleich; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

- Rolle und Ziel im NDA-Abgleich und Vertraulichkeitsvereinbarungen klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: Übliche NDA-Dauer 2–5 Jahre nach Vertragsende, GeschGehG-Anspruchsverjährung § 195 BGB 3 Jahre, EuGH C-435/22 zur restriktiven Auslegung, DSGVO Art. 33 Datenpanne 72h.
- Tragende Normen verifizieren: GeschGehG §§ 2 Nr. 1, 3, 4, 5, 6, 7, 8, 9, 10, 17, BGB §§ 145 ff., 280, 339, 343, 305 ff. (AGB-Kontrolle), BDSG § 26, DSGVO Art. 6, 28, 32 (TOM) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Geheimnisinhaber, Empfänger, M&A-Berater, Investmentbanker, externer Dienstleister, Datenschutzbeauftragter, Compliance.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Unilateral NDA, Mutual NDA, Cleanroom-Agreement, Joinder-Erklärung, Term Sheet, AVV nach Art. 28 DSGVO, Verschwiegenheitsanlage — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `nda-standardklauseln-bauleiter`

**Fokus:** Bauleiter NDA-Standardklauseln: Vertraulichkeitsumfang, Empfaengerkreis, Laufzeit, Rechtsfolgen, Schriftform. Pruefraster fuer mutual und one-way NDA.

# NDA: Standardklauseln Bauleiter

## Spezialwissen: NDA: Standardklauseln Bauleiter
- **Spezialgegenstand:** NDA: Standardklauseln Bauleiter / nda standardklauseln bauleiter. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** NDA.
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
2. **Rechtliche Einordnung** - einschlaegige Normen, Rechtsprechung BGH/BVerfG/EuGH, Literatur.
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
- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei pruefbarem Link (`dejure.org`, `openjur.de`, `bundesgerichtshof.de`, `bundesverfassungsgericht.de`, `curia.europa.eu`).
- Keine Zitate aus `anwalt24.de`. Keine `BeckRS` als alleinige Fundstelle bei tragenden Aussagen.
- Aufsaetze mit Verfasser, Zeitschrift, Jahr, Heft (falls relevant) und Seite.
- Kommentare mit Bearbeiter und Randnummer.
- Annahmen explizit als solche kennzeichnen, keine Erfindungen.

## Was dieser Arbeitsgang nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `nda-vertragsstrafe-pruefen`

**Fokus:** Vertragsstrafe pruefen: Hoehe, AGB-Kontrolle §§ 305 ff. BGB, Bestimmtheitsgrundsatz, Schadensersatzkumulation oder Anrechnung. Bei Verbraucher-NDA strengere Grenzen. Bei B2B-Standard: ueblich 5000-25000 EUR pro Vorfall, Kumulation moeglich.

# NDA: Vertragsstrafe pruefen

## Spezialwissen: NDA: Vertragsstrafe pruefen
- **Spezialgegenstand:** NDA: Vertragsstrafe pruefen / nda vertragsstrafe pruefen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** AGB, BGB, NDA, EUR.
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

1. **Sachverhalt fixieren** – streitige und unstreitige Tatsachen trennen, Lueckentafel.
2. **Rechtliche Einordnung** - nur einschlaegige Normen, verifizierte Rechtsprechung und frei pruefbare amtliche Quellen; keine Literatur- oder Datenbankfundstellen erfinden.
3. **Pruefung im Gutachtenstil** – Obersatz, Definition, Subsumtion, Zwischenergebnis.
4. **Handlungsempfehlung** – konkret, mit naechstem Schritt, verantwortlicher Person, Frist.

## Fachpruefraster Vertragsstrafe NDA

### Materielle Anforderungen (§ 339 BGB)

- **Akzessorietaet:** Vertragsstrafe setzt schuldhafte Verletzung der Hauptpflicht voraus (§ 339 i.V.m. § 276 BGB). Verschuldensunabhaengige Strafklauseln sind im Zweifel unwirksam.
- **Bestimmtheit:** Strafversprechen muss inhaltlich klar bestimmt sein: Auf welche konkrete Pflicht bezieht sich die Strafe? Wie wird die Hoehe berechnet? Welche Hoechstgrenze gilt?
- **Verschulden:** Bei AGB-NDA mit Vertragsstrafe ohne Verschulden Verstoss gegen § 307 BGB.

### AGB-Kontrolle (§§ 305 ff. BGB)

- **B2C (Verbraucher-NDA, z.B. Arbeitnehmer in Privatkonstellation):** § 309 Nr. 6 BGB - absolutes Klauselverbot. Vertragsstrafe in AGB gegenueber Verbrauchern stets unwirksam.
- **B2B:** § 310 Abs. 1 BGB lockert direkte Anwendung, aber § 307 BGB Wertungsausstrahlung. Indizien fuer Wirksamkeit: angemessene Hoehe, Verschulden, konkrete Pflichtbenennung, keine Doppelpauschalierung.
- **Arbeitsrecht:** Im Arbeitsverhaeltnis Vertragsstrafe in AGB grundsaetzlich problematisch. § 309 Nr. 6 BGB gilt direkt zwar nicht (kein Verbraucher); aber § 307 BGB. BAG verlangt: enge Bestimmtheit, Hoehe in Bezug zu Bruttomonatsgehalt (Faustregel: max. 1 Brutto-Monatsgehalt pro Verstoss), Anrechnung auf Schadenersatz.

### Branchen-Faustregeln

- **Standard-B2B-NDA:** EUR 5.000 - EUR 25.000 pro Vorfall sind gerichtsfest in den meisten Konstellationen.
- **M&A / Data Room:** Hoehere Strafen ueblich (bis EUR 100.000 pro Vorfall), wenn Datenmenge und Risikolage es rechtfertigen.
- **R&D / Patente:** Strafe orientiert sich am Lizenz-/Investitionswert; Hoehen ueber EUR 250.000 nur bei individueller Aushandlung wirksam.
- **Arbeitnehmer-NDA:** Anlehnung an Bruttomonatsgehalt; pauschale Saetze ueber 1-2 Bruttomonatsgehaelter regelmaessig unwirksam.

### Anrechnung / Kumulation

- **§ 340 Abs. 2 BGB:** Anrechnung der Strafe auf weitergehenden Schadenersatzanspruch ist gesetzlicher Regelfall. Klausel, die explizit Anrechnung ausschliesst (Kumulationsklausel), in AGB regelmaessig unwirksam (§ 307 BGB).
- **Mehrere Verstoesse:** Klarstellen, ob jeder einzelne Verstoss eine eigene Strafe ausloest oder ob Sammelregelung mit Hoechstgrenze gilt.

### Mustertext B2B-NDA (Vertragsstrafe, individualvertraglich verhandelbar)

> Verletzt die empfangende Partei schuldhaft eine Geheimhaltungspflicht aus diesem Vertrag, kann die offenlegende Partei fuer jeden Fall der Verletzung eine Vertragsstrafe in Hoehe von EUR [Betrag] verlangen. Mehrere Verstoesse, die auf demselben einheitlichen Vorgang beruhen, gelten als ein Verstoss. Die Vertragsstrafe wird auf einen weitergehenden, nachzuweisenden Schadenersatzanspruch angerechnet (§ 340 Abs. 2 BGB).

## Plugin-Kontext
Dieses Fachmodul arbeitet den konkreten Schwerpunkt aus, prüft Aktenlage, Normen, Fristen, Belege und Gegenargumente und erzeugt einen unmittelbar nutzbaren nächsten Schritt.

## Output-Module
- Strukturierter Pruefvermerk im Gutachtenstil mit klaren Ueberschriften.
- Tabellen/Checklisten, wo das die Lesbarkeit erhoeht.
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

## 3. `spezial-entwurf-tatbestand-beweis-und-belege`

**Fokus:** Entwurf: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin nda abgleich; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Entwurf: Tatbestandsmerkmale, Beweisfragen und Beleglage

## Spezialwissen: Entwurf: Tatbestandsmerkmale, Beweisfragen und Beleglage
- **Spezialgegenstand:** Entwurf: Tatbestandsmerkmale, Beweisfragen und Beleglage / entwurf tatbestand beweis und belege. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** NDA, ROT, GELB, GRUEN.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Entwurf** prüfen.
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
