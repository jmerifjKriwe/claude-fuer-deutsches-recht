---
name: kompendium-03-einsprachige-vertrag-bis-spezial-vertragserst
description: "wandeldarlehen-lebenszyklus: Konsolidiertes Skill-Kompendium 03; bündelt 2 frühere Spezialskills (einsprachige-vertragsfassung-de, spezial-vertragserstellung-behoerden-gericht-und-registerweg) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 03 - wandeldarlehen-lebenszyklus

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `einsprachige-vertragsfassung-de` | Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten für rein nationale Transaktionen. §§ 488 ff. BGB Darlehen §§ 55 56 GmbHG Kapitalerhohung. Prüfraster: SAFE-Konditionen BGB-Konformität Schriftformerfordernisse Investoren-Sonderrechte. Output: vollständiger Vertragsentwurf auf Deutsch. Abgrenzung: nicht für bilinguale Fassung (bilinguale-vertragserstellung). |
| `spezial-vertragserstellung-behoerden-gericht-und-registerweg` | Vertragserstellung: Behörden-, Gerichts- oder Registerweg im Plugin wandeldarlehen lebenszyklus; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `einsprachige-vertragsfassung-de`

**Frühere Beschreibung:** Wandeldarlehensvertrag auf Deutsch erstellen oder ueberarbeiten für rein nationale Transaktionen. §§ 488 ff. BGB Darlehen §§ 55 56 GmbHG Kapitalerhohung. Prüfraster: SAFE-Konditionen BGB-Konformität Schriftformerfordernisse Investoren-Sonderrechte. Output: vollständiger Vertragsentwurf auf Deutsch. Abgrenzung: nicht für bilinguale Fassung (bilinguale-vertragserstellung).

# Einsprachige Vertragsfassung (nur DE)

## Zweck

Dieser Skill erzeugt aus der bilingualen Fassung eine rein deutsche Vertragsfassung in einspaltigem, lesefreundlichem Word-Dokument. Der materielle Inhalt ist identisch – keine inhaltlichen Unterschiede. Phase A des Lebenszyklus.

## Eingaben

- Fertiger Inhalt der deutschen Spalte der bilingualen Fassung (aus `bilinguale-vertragserstellung`)
- Zieldatei: DOCX, einspaltig
- Gewünschte Schriftgröße und Zeilenabstand (Standard: Times New Roman 12 pt, 1.5-facher Zeilenabstand)
- Seitenränder: Standard 2.5 cm ringsum

## Rechtlicher Rahmen

### Primärnormen
- § 126b BGB (Textform), § 126 BGB (Schriftform)
- § 10.1 Sprachklausel (nur DE-Fassung ohne EN-Spalte – dennoch materiell identisch mit bilingualer Fassung)
- Keine gesonderten Anforderungen: Die einsprachige Fassung unterliegt denselben Formregeln wie die bilinguale Fassung.

### Rechtsprechung
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Vorgehen

### 1. Extraktion der deutschen Textspalte
Aus der bilingualen Tabelle wird exakt der deutsche Text extrahiert. Keine Umformulierungen, keine Kürzungen, keine Ergänzungen.

### 2. Formatierung mit Heading-Stilen
- Heading 1: Vertragsüberschrift (z. B. "Wandeldarlehensvertrag")
- Heading 2: Paragrafenüberschriften (§ 0 Präambel, § 1 Darlehensgewährung, …)
- Heading 3: Unterabschnitte
- Normal: Vertragstext
- Tabellen: nur für Bankverbindung und Berechnungsformeln

### 3. Signaturblock
Vier separate Signaturblöcke mit Platz für Ort, Datum und Unterschrift. DocuSign-Hinweis beibehalten.

### 4. Abschließende Qualitätsprüfung
Prüfen: Alle Paragrafenverweise korrekt? Keine Querverweise auf englische Begriffe? Alle Zahlen konsistent mit bilingualer Fassung?

### 5. Dokument speichern und benennen
Dateiname nach Konvention: `Wandeldarlehen-[Gesellschaft]-[Darlehensgeber]-nur-deutsch.docx`.

### 6. Vergleich mit bilingualer Fassung
Automatischer Abgleich: Jede inhaltlich tragende Aussage der DE-Spalte muss in der einsprachigen Fassung vorhanden sein (1:1-Übertragung). Abweichungen sind Fehler.

## Beispiel-Dokumentstruktur

```
WANDELDARLEHENSVERTRAG
zwischen
[Parteien]

§ 0  Präambel
§ 1  Darlehensgewährung und Auszahlung
§ 2  Laufzeit und Rückzahlung
§ 3  Verzinsung
§ 4  Wandlung
§ 5  Mitwirkungspflichten der Gesellschafterinnen
§ 6  Qualifizierter Rangrücktritt
§ 7  Informationsrechte
§ 8  Vertraulichkeit
§ 9  Form, Beurkundung und Ausfertigung
§ 10 Schlussbestimmungen

[Signaturblock: Gesellschaft, Gesellschafterin 1, Gesellschafterin 2, Darlehensgeber]
```

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| Inhalt weicht von bilingualer Fassung ab | Zwei verschiedene Vertragsfassungen in Umlauf | Einzelne Formulierungen abweichend | Identischer Inhalt |
| Paragrafenverweise falsch | Lückenhaftes Dokument | Ein Verweis fehlerhaft | Alle Verweise korrekt |
| Signaturblock unvollständig | Unterzeichnung verhindert | Ein Block fehlend | Alle vier Blöcke vollständig |
| Schriftgröße und Layout unleserlich | Professioneller Eindruck fehlt | Geringfügige Formatmängel | Lesefreundliches Layout |

## Querverweise

- `wandeldarlehen-lebenszyklus/skills/bilinguale-vertragserstellung/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/unterzeichnung-elektronisch-docusign/SKILL.md`
- `wandeldarlehen-lebenszyklus/skills/textform-vs-schriftform-vs-notariell/SKILL.md`

## Quellen und Updates

Stand: 05/2026. Bei Änderung BGB-Formvorschriften aktualisieren.

## Vertiefung — Aktuelle Rechtsprechung

### Leitsatz-Zitate

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Normen-Ergänzung

§§ 133, 157 BGB (Auslegung) → § 305c Abs. 2 BGB (Unklarheitenregelung AGB) → § 184 GVG (Amtssprache) → §§ 55 Abs. 2, 56 GmbHG (Beurkundung, Sacheinlage)

## 2. `spezial-vertragserstellung-behoerden-gericht-und-registerweg`

**Frühere Beschreibung:** Vertragserstellung: Behörden-, Gerichts- oder Registerweg im Plugin wandeldarlehen lebenszyklus; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Vertragserstellung: Behörden-, Gerichts- oder Registerweg

## Spezialwissen: Vertragserstellung: Behörden-, Gerichts- oder Registerweg
- **Spezialgegenstand:** Vertragserstellung: Behörden-, Gerichts- oder Registerweg / spezial vertragserstellung behoerden gericht und registerweg. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** UG.
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
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Vertragserstellung** prüfen.
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
