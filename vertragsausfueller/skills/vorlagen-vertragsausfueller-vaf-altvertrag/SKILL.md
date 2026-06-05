---
name: vorlagen-vertragsausfueller-vaf-altvertrag
description: "Vorlagen Vertragsausfueller VAF Altvertrag im Plugin Vertragsausfueller: prüft konkret Vorlagen, Vertragsausfueller, Altvertrag auf neue Vorlage nachziehen und aktualisieren. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Vorlagen Vertragsausfueller VAF Altvertrag

## Arbeitsbereich

**Vorlagen Vertragsausfueller VAF Altvertrag** ordnet den Fall über die tragenden Prüffelder: Vorlagen, Vertragsausfueller, Altvertrag auf neue Vorlage nachziehen und aktualisieren. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `spezial-vorlagen-fristen-form-und-zustaendigkeit` | Vorlagen: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin vertragsausfueller; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-vertragsausfueller-erstpruefung-und-mandatsziel` | Vertragsausfueller: Erstprüfung, Rollenklärung und Mandatsziel im Plugin vertragsausfueller; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `vaf-altvertrag-nachziehen` | Altvertrag auf neue Vorlage nachziehen und aktualisieren: Anwendungsfall bestehendes Vertragsverhältnis soll auf neue Vertragsvorlage überführt werden wegen Parteienwechsel, aktualisierter Klauseln oder Gesetzesänderungen. §§ 305 ff. BGB AGB-Recht, § 622 BGB bei Arbeitsverträgen. Prüfraster Parteienänderungen erkennen, veraltete Klauseln identifizieren, Altlasten markieren, Gesetzesänderungen seit Vertragsschluss einpflegen. Output aktualiserter Vertragsentwurf mit Änderungsprotokoll und offenen Punkten. Abgrenzung zu Template-Erkennung für neue Vorlagen und zu Redline-QA. |

## Arbeitsweg

- Rolle und Ziel im Vertragsausfüller (Lückenschluss in Verträgen) klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: Vertragsspezifisch; § 195 BGB Regelverjährung 3 Jahre, § 14 BGB-InfoV Widerrufsfrist 14 Tage, EuGH-Vorgaben zu Klausel-Transparenz.
- Tragende Normen verifizieren: BGB §§ 133, 157, 305-310 (AGB-Kontrolle), 311b, 311c, 433, 488, 535, 631, 651a, 765, NachwG, FormularG, AGG (Diskriminierungsverbot) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Vertragspartner, Rechtsabteilung, Notar bei Formerfordernis, Datenschutzbeauftragter.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Mustervertrag, Termsheet, Klauselkatalog, Altvertrag, Vertragsentwurf mit Track Changes, AGB-Prüfraster — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `spezial-vorlagen-fristen-form-und-zustaendigkeit`

**Fokus:** Vorlagen: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin vertragsausfueller; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vorlagen: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: Vorlagen: Fristen, Form, Zuständigkeit und Rechtsweg
- **Spezialgegenstand:** Vorlagen: Fristen, Form, Zuständigkeit und Rechtsweg / vorlagen fristen form und zustaendigkeit. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DOCX/PDF sind Dateiformate, keine Rechtsquellen. Je nach Vertrag BGB §§ 145 ff., 241, 280, 305 ff., 311; einschlägige Formvorschriften; bei Einreichung ZPO/beA-Vorgaben; bei Verbrauchern §§ 312 ff., 355 ff. BGB live prüfen.
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

## 2. `spezial-vertragsausfueller-erstpruefung-und-mandatsziel`

**Fokus:** Vertragsausfueller: Erstprüfung, Rollenklärung und Mandatsziel im Plugin vertragsausfueller; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vertragsausfueller: Erstprüfung, Rollenklärung und Mandatsziel

## Spezialwissen: Vertragsausfueller: Erstprüfung, Rollenklärung und Mandatsziel
- **Spezialgegenstand:** Vertragsausfueller: Erstprüfung, Rollenklärung und Mandatsziel / vertragsausfueller erstpruefung und mandatsziel. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** DOCX/PDF sind Dateiformate, keine Rechtsquellen. Je nach Vertrag BGB §§ 145 ff., 241, 280, 305 ff., 311; einschlägige Formvorschriften; bei Einreichung ZPO/beA-Vorgaben; bei Verbrauchern §§ 312 ff., 355 ff. BGB live prüfen.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vertragsausfueller** prüfen.
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

## 3. `vaf-altvertrag-nachziehen`

**Fokus:** Altvertrag auf neue Vorlage nachziehen und aktualisieren: Anwendungsfall bestehendes Vertragsverhältnis soll auf neue Vertragsvorlage überführt werden wegen Parteienwechsel, aktualisierter Klauseln oder Gesetzesänderungen. §§ 305 ff. BGB AGB-Recht, § 622 BGB bei Arbeitsverträgen. Prüfraster Parteienänderungen erkennen, veraltete Klauseln identifizieren, Altlasten markieren, Gesetzesänderungen seit Vertragsschluss einpflegen. Output aktualiserter Vertragsentwurf mit Änderungsprotokoll und offenen Punkten. Abgrenzung zu Template-Erkennung für neue Vorlagen und zu Redline-QA.

# Altvertrag nachziehen


## Triage zu Beginn

1. Handelt es sich um ein deutsches oder grenzüberschreitendes Vertragsverhältnis?
2. Ist der Altvertrag noch vollständig gültig oder sind Änderungsvereinbarungen eingeflossen?
3. Welche Parteien haben seit dem Altvertrag gewechselt (Firmen, Kontaktpersonen)?
4. Gibt es gesetzliche Neuregelungen seit Abschluss des Altvertrags (z.B. Mietrecht, AGB-Recht)?

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen

- § 305, 305c BGB — Einbeziehung und Auslegung von AGB
- § 307 ff. BGB — AGB-Inhaltskontrolle (Generalklausel, Verbotslisten)
- § 550 BGB — Schriftformgebot bei langfristigen Mietverträgen (mehr als 1 Jahr)
- § 195 BGB — Verjährung (regelmäßig 3 Jahre)
- § 313 BGB — Störung der Geschäftsgrundlage (bei wesentlich veränderten Umständen)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Aufgabe

Der Skill macht aus alten Verträgen neue Entwürfe. Er arbeitet freistehend innerhalb des Vertragsausfüller-Plugins und setzt keine anderen Plugins voraus.

## Startet bei

- hochgeladener Word-Vorlage oder altem Vertrag
- Term Sheet, E-Mail, Tabelle oder Freitext mit Eckdaten
- Wunsch nach neuem Vertragsentwurf
- Wunsch nach Redline oder Track Changes

## Workflow

1. Alten Vertrag als Datenquelle, nicht als unkritische Wahrheit behandeln.
2. Übernommene Werte mit Quelle und Vertrauensgrad markieren.
3. Altklauseln, die nicht zur neuen Vorlage passen, als Review-Punkt ausgeben.
4. Bei Konflikten zwischen Altvertrag und neuer Vorlage nachfragen.

## Ausgabe

- Vertragsdatenmatrix
- Rückfragenliste
- Ausfüllprotokoll
- Entwurfs- oder Prüfvermerk
- klare Stopper vor Track Changes, falls noch keine ausdrückliche Bestätigung vorliegt

## Leitplanken

- Originaldateien werden nie überschrieben.
- Track Changes, Redline oder Vergleichsfassung nur nach ausdrücklicher Rückfrage und Bestätigung.
- Offene Werte bleiben sichtbar; sie werden nicht erfunden.
- Juristische Wahlentscheidungen werden erklärt und protokolliert.
