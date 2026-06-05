---
name: forensische-prompt-gutachten-erstellen
description: "Forensische Prompt Gutachten Erstellen im Plugin Berufsrecht Ki Vertragspruefung: prüft konkret Forensische Pruefung Prompt-Injection-Risiko, Erstelle das zusammenfassende Vorprüfungs-Gutachten zum, Spezialfall Kanzleisoftware mit KI-Funktionen (RA-MICRO, Datev DMS. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Forensische Prompt Gutachten Erstellen

## Arbeitsbereich

**Forensische Prompt Gutachten Erstellen** ordnet den Fall über die tragenden Prüffelder: Forensische Pruefung Prompt-Injection-Risiko, Erstelle das zusammenfassende Vorprüfungs-Gutachten zum, Spezialfall Kanzleisoftware mit KI-Funktionen (RA-MICRO. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `forensische-pruefung-prompt-injection` | Forensische Pruefung Prompt-Injection-Risiko: Indirekte Prompt-Injection ueber hochgeladene Dokumente, RAG-Vergiftung, Datenexfiltration. Pruefraster fuer Reviewer-Audit, Sandbox-Test, Sicherheits-Hardening durch Anbieter. Pflicht des Anwalts. |
| `gutachten-erstellen` | Erstelle das zusammenfassende Vorprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat Ampelbewertung Lückenliste Handlungsempfehlung. Ausdrücklich keine Rechtsberatung sondern strukturierte Argumentationshilfe für das Anbietergespräch. |
| `kanzleisoftware-spezial-mandantendaten` | Spezialfall Kanzleisoftware mit KI-Funktionen (RA-MICRO, Datev DMS, Acta Nova, vRA): Mandantendaten in Cloud, KI-Funktion Volltextsuche, Diktat, Vertragsanalyse. Pruefraster fuer Einwilligung Mandant, Auftragsverarbeitung, Loeschkonzepte. |

## Arbeitsweg

- Rolle und Ziel im Berufsrecht Ki Vertragspruefung klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BRAO, BORA, FAO, BNotO, StBerG, WPO, PAO; StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 43e BRAO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `forensische-pruefung-prompt-injection`

**Fokus:** Forensische Pruefung Prompt-Injection-Risiko: Indirekte Prompt-Injection ueber hochgeladene Dokumente, RAG-Vergiftung, Datenexfiltration. Pruefraster fuer Reviewer-Audit, Sandbox-Test, Sicherheits-Hardening durch Anbieter. Pflicht des Anwalts.

# Prompt-Injection: Pruefung

## Spezialwissen: Prompt-Injection: Pruefung
- **Spezialgegenstand:** Prompt-Injection: Pruefung / forensische pruefung prompt injection. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** RAG.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Verträge, Auszuege liegen vor?
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

## 2. `gutachten-erstellen`

**Fokus:** Erstelle das zusammenfassende Vorprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat Ampelbewertung Lückenliste Handlungsempfehlung. Ausdrücklich keine Rechtsberatung sondern strukturierte Argumentationshilfe für das Anbietergespräch.

# Vorprüfungs-Gutachten erstellen

## Fachkern: Vorprüfungs-Gutachten erstellen

- **KI-/Berufsrechtsproblem (Vorprüfungs-Gutachten erstellen):** Erstelle das zusammenfassende Vorprüfungs-Gutachten zum KI-Anbietervertrag. Aufbau Eingangsdaten Norm-Adapter Prüfpunkte Erforderlichkeit Verschwiegenheit Belehrung Subunternehmer Strafprozess TOM Drittstaat Ampelbewertung Lückenliste Handlungsempfehlung. Ausdrücklich keine Rechtsberatung sondern strukturierte Argumentationshilfe für das Anbietergespräch.
- **Normenanker:** BRAO, BORA, § 203 StGB, § 204 StGB, DSGVO/BDSG, Dienstleisterregelungen der freien Berufe, Auftragsverarbeitung und technische Geheimnisschutzrealität.
- **Entscheidende Weiche:** Mustertext, Anbieterbehauptung, technische Wirklichkeit, Berufsgeheimnis und Datenschutzrolle müssen getrennt bleiben.
- **Arbeitsprodukt:** Vertragsbaustein, Gutachtenstruktur, Redline oder Anbieter-Fragenliste; Ergebnis bleibt Vorprüfung und wird nicht als fertige Berufsrechtsfreigabe ausgegeben.

## Zweck

Das Gutachten fasst alle Einzelprüfungen zu einem strukturierten Dokument zusammen. Es ist intern für die Kanzlei bestimmt, kann aber auszugsweise als Argumentationsgrundlage gegenüber dem Anbieter verwendet werden.

## Aufbau

### 1. Eingangsdaten

Aus `berufsrecht-ki-vertragspruefung-kaltstart-interview`. Beruf, Anbieter, Produkt, Datenarten, Vertragstyp, Anlagen.

### 2. Norm-Adapter

Aus `parallelnormen-andere-berufe`. Tabelle der einschlägigen Normen. Hinweis auf § 203 StGB als Klammer.

### 3. Maßstab

Maßstab sind zuerst die geltenden Normen und ihre Gesetzesmaterialien. Berufsrechtliche Stellungnahmen, Kammerhinweise und Fachdebatten werden nur als Auslegungshilfe verarbeitet und in ihrer Bindungswirkung kenntlich gemacht.

### 4. Einzelne Prüfpunkte

Pro Skill ein Abschnitt:

- **Erforderlichkeit** (`erforderlichkeit-dokumentieren`)
- **Verschwiegenheitsklausel** (`verschwiegenheitsklausel-pruefen`)
- **Strafrechtliche Belehrung** (`strafrechtliche-belehrung-pruefen`)
- **Subunternehmer-Regelung** (`subunternehmer-regelung-pruefen`)
- **Strafprozessuale Regelung** (`strafprozessuale-regelung-pruefen`)
- **TOM und Zertifizierungen** (`tom-und-zertifizierungen-pruefen`)
- **Cloud Act und Drittstaat** (`cloud-act-und-drittstaat-pruefen`)
- **AVV-Grenzprüfung Datenschutz** (`avv-grenzpruefung-datenschutz`) — als Schnittstelle

Jeder Abschnitt enthält:

- die einschlägige Norm
- die vertretbare Auslegungslinie und Gegenpositionen
- die konkrete Bewertung am vorgelegten Vertrag (Ampel grün/gelb/rot)
- Lücken und offene Punkte

### 5. Gesamtampel

| Bereich | Ampel | Bemerkung |
|---|---|---|
| Erforderlichkeit | | |
| Verschwiegenheitsklausel | | |
| Strafrechtliche Belehrung | | |
| Subunternehmer | | |
| Strafprozessuale Absicherung | | |
| TOM und Zertifizierungen | | |
| Drittstaat | | |
| AVV (Schnittstelle) | | |

### 6. Handlungsempfehlung

Drei Stufen:

- **Annehmbar** (alles grün, gelbe Punkte dokumentieren) — Vertrag nutzbar nach Annahme
- **Nachverhandelbar** (überwiegend grün/gelb, klare rote Punkte) — Rückfragebrief und Klauselvorschläge versenden
- **Nicht annehmbar** (mehrere rote Punkte, strukturelle Probleme) — Anbieterwechsel oder grundlegende Vertragsneuverhandlung

### 7. Anlagen

- Tabellarische Bewertung pro Prüfpunkt
- Lückenliste (priorisiert)
- Verweise auf Rückfragebrief und Klauselvorschläge

## Schlussklausel im Gutachten

Am Ende jedes Gutachtens steht:

> Dieses Vorprüfungs-Gutachten ist keine Rechtsberatung. Es ist eine strukturierte Argumentationshilfe für das Anbietergespräch. Die abschließende berufsrechtliche und strafrechtliche Beurteilung im konkreten Einzelfall bleibt der nutzenden Kanzlei beziehungsweise einer beauftragten Spezialkanzlei vorbehalten. Quellenbasis: geltende Gesetzestexte, Gesetzesmaterialien, verifizierbare Kammerhinweise, Rechtsprechung und aktueller berufsrechtlicher Debattenstand.

## Stil

- Sachlich, kurz
- Tabellen wo möglich
- Keine Marketing-Sprache
- Disclaimer am Anfang und am Ende
- Bezeichne Anbieterversprechen klar als "Aussage Anbieter, noch nicht im Vertrag" oder "im Vertrag (Fundstelle)"

## Output-Format

Markdown, ca. 5 bis 10 Seiten. PDF-Export optional via Plugin `office`.

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zentrale Normen (Paragrafenkette)

- §§ 43a Abs. 2, 43e BRAO; §§ 57, 62a StBerG; §§ 43, 50a WPO; §§ 39a, 39c PAO; §§ 18, 26a BNotO
- §§ 203, 204 StGB — Straftatbestände
- §§ 53a, 97 StPO — Strafprozessuale Absicherung
- Art. 28, 32 DSGVO — Datenschutzrechtliche Parallelprüfung

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage zu Beginn

1. Wurden alle Einzelprüfungen aus den Teilskills (Verschwiegenheit, Belehrung, Subunternehmer, Strafprozess, TOM, Drittstaat) durchgeführt?
2. Liegen alle Vertragsdokumente vor (Hauptvertrag, AGB, AVV, Subunternehmerliste, TOM-Anlage)?
3. Sind offene Punkte aus dem Rückfragebrief beantwortet?
4. Welches Ergebnis soll das Gutachten haben (Freigabe / Nachverhandlung / Ablehnung)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — datenschutzrechtliches Gutachten erstellen | Vollgutachten-Format nach Template unten |
| Variante A — nur kurze Stellungnahme noetig | Kurzgutachten-Format; Normenkette komprimieren |
| Variante B — politisch heikle Einschaetzung fuer Mandanten | Ergebnis-offen formulieren; Risiken deutlich benennen |
| Variante C — internes Compliance-Memo ohne externe Wirkung | Schlankeres Format; auf Vollzitierung teilweise verzichten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template — Vorprüfungs-Gutachten (Auszug)

**Adressat:** Kanzlei intern (ggf. auszugsweise für Anbieter) — Tonfall: sachlich-juristisch

```
Vorpruefungs-Gutachten KI-Anbietervertrag
Datum: [DATUM] | Verfasser: [SACHBEARBEITER]
Anbieter: [NAME] | Produkt: [PRODUKT]
Beruf: [BERUF] | Norm-Adapter: § [NORM]

I. Eingangsdaten
[Aus Kaltstart-Interview]

II. Normrahmen
Berufsrecht: § [NORM] [GESETZ]
Strafrecht: §§ 203, 204 StGB
Datenschutz: Art. 28, 32 DSGVO
Strafprozess: §§ 53a, 97 StPO

III. Einzelprüfungen (Ampeltabelle)
| Pruefpunkt | Ampel | Begruendung |
|-------------------------|-------|-------------|
| Erforderlichkeit | | |
| Verschwiegenheitsklausel| | |
| Belehrung §§ 203/204 | | |
| Subunternehmer | | |
| Strafprozess §§ 53a/97 | | |
| TOM / Zertifizierungen | | |
| Drittstaat / CLOUD Act | | |
| AVV Art. 28 DSGVO | | |

IV. Gesamtergebnis
[GRUEN / GELB / ROT]

V. Handlungsempfehlung
[Annehmbar / Nachverhandelbar / Nicht annehmbar]
[Konkrete naechste Schritte]

VI. Disclaimer
Dieses Vorpruefungs-Gutachten ist keine Rechtsberatung. Es ist strukturierte
Argumentationshilfe. Abschließende Beurteilung bleibt der nutzenden Kanzlei
beziehungsweise einer beauftragten Spezialkanzlei vorbehalten.
Quellen: geltende Gesetzestexte, Gesetzesmaterialien, verifizierbare Kammerhinweise, Rechtsprechung und aktueller berufsrechtlicher Debattenstand.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## 3. `kanzleisoftware-spezial-mandantendaten`

**Fokus:** Spezialfall Kanzleisoftware mit KI-Funktionen (RA-MICRO, Datev DMS, Acta Nova, vRA): Mandantendaten in Cloud, KI-Funktion Volltextsuche, Diktat, Vertragsanalyse. Pruefraster fuer Einwilligung Mandant, Auftragsverarbeitung, Loeschkonzepte.

# Kanzleisoftware-KI

## Spezialwissen: Kanzleisoftware-KI
- **Spezialgegenstand:** Kanzleisoftware-KI / kanzleisoftware mandantendaten. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** KI, RA, MICRO, DMS.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Frage zu Beginn nur ab, was fuer den naechsten Schritt unverzichtbar ist. Wenn Material vorliegt, mit dem Material arbeiten und nur eine gezielte Rueckfrage stellen.

1. **Rolle und Ziel:** Wer fragt, welche Rolle, welcher gewuenschte Output (Memo, Schriftsatz, Tabelle, Checkliste)?
2. **Sachverhalt:** Welche unstreitigen Tatsachen liegen vor, was ist streitig, was fehlt noch?
3. **Fristen:** Gibt es Termine, Fristen, eilbeduerftige Schritte?
4. **Unterlagen:** Welche Dokumente, Bescheide, Verträge, Auszuege liegen vor?
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
