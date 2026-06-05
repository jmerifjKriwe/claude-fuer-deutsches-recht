---
name: betreuungsrecht-betreuung-grenzueberschreitend-betreuungsantrag
description: "Betreuung Grenzueberschreitend Betreuungsantrag im Plugin Betreuungsrecht: prüft konkret Grenzueberschreitende Betreuung, Betreuungsantrag § 1814 BGB, Kommunikation mit dem Betreuungsgericht für Angehörige und. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Betreuung Grenzueberschreitend Betreuungsantrag

## Arbeitsbereich

Dieser Skill behandelt **Betreuung Grenzueberschreitend Betreuungsantrag** als zusammenhängenden Arbeitsgang im Plugin Betreuungsrecht. Im Mittelpunkt steht die Prüfung von Grenzueberschreitende Betreuung, Betreuungsantrag § 1814 BGB, Kommunikation mit dem Betreuungsgericht für Angehörige und. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `betreuung-grenzueberschreitend` | Grenzueberschreitende Betreuung: Haager Erwachsenenschutzuebereinkommen 2000, Anerkennung in Deutschland und im EU-Ausland, anwendbares Recht. Output: Pruefraster fuer im Ausland lebende Betroffene. |
| `betreuungsantrag-erstellen` | Betreuungsantrag § 1814 BGB: Antragsteller, Betroffener, Aufgabenkreise, vorhandene Vorsorgevollmacht, gewuenschte Person als Betreuer, Begruendung Erforderlichkeit. Output: Antragsschriftsatz an Betreuungsgericht. |
| `betreuungsgericht-kommunikation-fuer-angehoerige` | Kommunikation mit dem Betreuungsgericht für Angehörige und ehrenamtliche Betreuer: formuliert kurze, sachliche Briefe, Genehmigungsanfragen, Sachstandsmitteilungen, Rückfragen, Fristverlängerungen und Unterlagenpakete ohne Behördenangst und ohne unnötige Selbstbelastung. |

## Arbeitsweg

- Rolle und Ziel im Betreuungsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BtOG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `betreuung-grenzueberschreitend`

**Fokus:** Grenzueberschreitende Betreuung: Haager Erwachsenenschutzuebereinkommen 2000, Anerkennung in Deutschland und im EU-Ausland, anwendbares Recht. Output: Pruefraster fuer im Ausland lebende Betroffene.

# Grenzueberschreitende Betreuung

## Spezialwissen: Grenzueberschreitende Betreuung
- **Spezialgegenstand:** Grenzueberschreitende Betreuung / betreuung grenzueberschreitend. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** EU.
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

## 2. `betreuungsantrag-erstellen`

**Fokus:** Betreuungsantrag § 1814 BGB: Antragsteller, Betroffener, Aufgabenkreise, vorhandene Vorsorgevollmacht, gewuenschte Person als Betreuer, Begruendung Erforderlichkeit. Output: Antragsschriftsatz an Betreuungsgericht.

# Betreuungsantrag erstellen

## Spezialwissen: Betreuungsantrag erstellen
- **Spezialgegenstand:** Betreuungsantrag erstellen / betreuungsantrag erstellen. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGB.
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

## 3. `betreuungsgericht-kommunikation-fuer-angehoerige`

**Fokus:** Kommunikation mit dem Betreuungsgericht für Angehörige und ehrenamtliche Betreuer: formuliert kurze, sachliche Briefe, Genehmigungsanfragen, Sachstandsmitteilungen, Rückfragen, Fristverlängerungen und Unterlagenpakete ohne Behördenangst und ohne unnötige Selbstbelastung.

# Betreuungsgericht-Kommunikation für Angehörige

## Zweck

Dieser Skill hilft ehrenamtlichen Betreuern, mit dem Betreuungsgericht knapp, vollständig und respektvoll zu kommunizieren. Das Ziel ist: Gericht bekommt, was es zur Aufsicht braucht; der Betreuer verrennt sich nicht in lange Erzählungen.

## Grundton

- sachlich,
- belegbar,
- kurz,
- ohne Vorwürfe,
- ohne medizinische Details, die für die konkrete Frage nicht nötig sind,
- mit klarer Bitte: Auskunft, Genehmigung, Fristverlängerung, Bestätigung, Hinweis.

## Typische Outputs

- Erstes Anschreiben nach Bestellung.
- Bitte um Einführungsgespräch.
- Nachfrage: Welche Formulare/Vordrucke nutzt dieses Gericht?
- Fristverlängerung für Vermögensverzeichnis oder Bericht.
- Genehmigungsanfrage bei Wohnungsaufgabe, Grundstück, Erbe, riskanter Anlage, Heimvertrag, Kontosperre.
- Sachstandsmitteilung bei wesentlicher Änderung.
- Bitte um Hinweis, ob eine Maßnahme genehmigungsbedürftig sein könnte.

## Briefstruktur

```text
Amtsgericht [Ort] - Betreuungsgericht
Az.: [...]
Betreuung: [Name, Geburtsdatum]

Sehr geehrte Damen und Herren,

ich bin mit Beschluss vom [Datum] als ehrenamtliche/r Betreuer/in bestellt.
Mein Aufgabenkreis umfasst: [...]

Anlass dieser Nachricht:
[ein bis drei Sätze]

Ich bitte um:
[konkrete Bitte]

Beigefügte Unterlagen:
1. [...]
2. [...]

Mit freundlichen Grüßen
```

## Sicherheitsregeln

- Vor belastenden Angaben gegen sich selbst oder Familienangehörige kurz innehalten und ggf. anwaltlichen Rat empfehlen.
- Genehmigungspflicht nicht selbst “wegschreiben”; bei Unsicherheit offen fragen.
- Wünsche der betreuten Person nennen: Was will sie, wie wurde das ermittelt?
- Bei Eilbedürftigkeit zuerst telefonische Kontaktaufnahme mit Gericht/Geschäftsstelle erwägen und danach Aktenvermerk erstellen.

## Anschluss-Skills

- `genehmigungspflicht-pruefung`
- `jahresbericht-betreuungsgericht`
- `vermoegensverzeichnis-pruefung`
- `familienbetreuer-alltagscockpit`
- `kalender-reminder-und-fristenmanagement`
