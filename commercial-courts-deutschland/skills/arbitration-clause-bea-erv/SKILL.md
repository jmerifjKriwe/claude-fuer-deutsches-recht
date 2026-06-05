---
name: arbitration-clause-bea-erv
description: "Arbitration Clause BEA ERV im Commercial Courts in Deutschland: prüft konkret Prüft Konflikte zwischen Schieds-, Gerichtsstands-, Escalation- und Commercial-C, Prüft beA/ERV-Einreichung englischer Schriftsätze. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Arbitration Clause BEA ERV

## Arbeitsbereich

Dieser Skill behandelt **Arbitration Clause BEA ERV** als zusammenhängenden Arbeitsgang im Commercial Courts in Deutschland. Im Mittelpunkt steht die Prüfung von Prüft Konflikte zwischen Schieds-, Gerichtsstands-, Escalation- und Commercial-C. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `arbitration-clause-conflict-check` | Prüft Konflikte zwischen Schieds-, Gerichtsstands-, Escalation- und Commercial-Court-Klauseln. |
| `bea-erv-english-pleadings` | Prüft beA/ERV-Einreichung englischer Schriftsätze: Dateiformat, Signatur, Anlagen, Fristen, Empfangsbekenntnis und Kanzlei-Workflow. |

## Arbeitsweg

- Rolle und Ziel im Commercial Courts Deutschland klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: GVG §§ 119, 119b (Commercial Court), ZPO §§ 184a, 614, 1025-1066, AGGVG der Länder, EU-VO 1215/2012 (Brüssel Ia) — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `arbitration-clause-conflict-check`

**Fokus:** Prüft Konflikte zwischen Schieds-, Gerichtsstands-, Escalation- und Commercial-Court-Klauseln.

# Arbitration Clause Conflict

## Fachkern: Arbitration Clause Conflict
- **Spezialgegenstand:** Arbitration Clause Conflict. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Dieser Skill unterstützt Verfahren vor deutschen Commercial Courts oder Commercial Chambers mit internationalem Wirtschaftsbezug. Er liefert eine prozessuale Arbeitsstruktur und, wenn gewünscht, englischen Output. Deutsches Prozessrecht bleibt der Rahmen; englische Sprache bedeutet nicht Common-Law-Verfahren.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### Klauselkonflikt-Prüfraster

| Schritt | Inhalt | Norm/Kategorie |
| --- | --- | --- |
| Klauselbestand erfassen | Schiedsvereinbarung, Gerichtsstandsklausel, Eskalationsklausel (Mediation/Schlichtung), Forenwahl in Rahmen- und Einzelverträgen | §§ 1029 ff. ZPO Schiedsverfahren; § 38 ZPO Gerichtsstand |
| Wirksamkeit Schiedsabrede | Schriftform § 1031 ZPO, Bestimmtheit, Schiedsfähigkeit § 1030 ZPO | ggf. Trennung Hauptvertrag/Schiedsklausel (Severability) |
| Forenkonflikt | Welche Klausel ist die jüngste? Welche ist die speziellere (lex specialis)? | Auslegung §§ 133, 157 BGB |
| Eskalationsstufen | Vorgeschaltete Mediation pflichtig? Sanktionen bei Überspringen | BGH ständige Rechtsprechung: ggf. Klage unzulässig wenn Mediationsstufe nicht durchlaufen |
| Asymmetrische Klauseln | Eine Partei wählen, andere nicht: Wirksamkeit zweifelhaft (AGB-Kontrolle § 307 BGB) | im B2C unwirksam; im B2B Einzelfallprüfung |
| Hybrid: Court vs. Arbitration | Sind beide Forenwege gleichzeitig zulässig oder schließt einer den anderen aus? | Wahl- vs. Konkurrenzklausel |
| Rüge bei Anrufung des "falschen" Forums | Antrag auf Verweisung (§ 281 ZPO) oder Schiedseinrede (§ 1032 ZPO) | rechtzeitig vor Einlassung zur Sache rügen |

### Trade-off Schiedsgericht versus Commercial Court

| Schiedsgericht | Commercial Court |
| --- | --- |
| Vertraulichkeit | Öffentlichkeit § 169 GVG (Ausnahme § 273a ZPO Vertraulichkeitsanordnung Justizstandort-Stärkungsgesetz) |
| Parteibestimmte Schiedsrichter | Staatliche Richter, keine Auswahl |
| Vollstreckung weltweit (New York Convention 1958) | Vollstreckung EU-Inland Brüssel Ia-VO; sonst Anerkennungsverfahren |
| Keine Berufung, nur Aufhebung §§ 1059 ZPO | Revision § 184b GVG zum BGH möglich |
| Kosten oft höher (Schiedsrichterhonorare, Institut) | GKG-Gebühren plus RVG |

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Output-Standard

- **Executive Snapshot:** forum, language, next deadline, procedural risk.
- **Procedural Action:** konkreter nächster Antrag/Schriftsatz/Briefing in der gewünschten Sprache.
- **Evidence and Exhibits:** welche Anlagen tragen welchen Punkt, welche Übersetzung fehlt.
- **Risk Flags:** Zuständigkeit, Sprache, Frist, Geheimnis, Kosten, Rechtsmittel.
- **Follow-up Skills:** passende Skills aus diesem Plugin vorschlagen.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

## Quellenregel

Vor echter Verwendung aktuelle Primärquellen prüfen: GVG, ZPO, einschlägige Landesverordnungen und die Gerichtsseite des zuständigen Landes. Keine erfundenen Gerichtslisten, keine erfundenen Formularpflichten, keine Paywall-Fundstellen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.

## 2. `bea-erv-english-pleadings`

**Fokus:** Prüft beA/ERV-Einreichung englischer Schriftsätze: Dateiformat, Signatur, Anlagen, Fristen, Empfangsbekenntnis und Kanzlei-Workflow.

# beA/ERV

## Fachkern: beA/ERV
- **Spezialgegenstand:** beA/ERV. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** Commercial Courts/Commercial Chambers der Länder, ZPO, GVG, Zuständigkeit, Sprachwahl Englisch/Deutsch, Wortprotokoll, Geheimnisschutz und internationale Zustellung.
- **Entscheidende Weiche:** Gerichtsstand, Streitwert/Sachgebiet, Verfahrenssprache, Vertraulichkeit, Beweisaufnahme, Übersetzung, Protokoll und Vollstreckbarkeit steuern.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Aufgabe

Dieser Skill unterstützt Verfahren vor deutschen Commercial Courts oder Commercial Chambers mit internationalem Wirtschaftsbezug. Er liefert eine prozessuale Arbeitsstruktur und, wenn gewünscht, englischen Output. Deutsches Prozessrecht bleibt der Rahmen; englische Sprache bedeutet nicht Common-Law-Verfahren.

## Einstieg

Stelle höchstens fünf Fragen, sofern die Akte sie nicht beantwortet:

1. Soll der Output auf Deutsch, Englisch oder zweisprachig sein?
2. Welches Gericht/Forum ist vorgesehen oder vereinbart?
3. Welche Klausel, welcher Streitwert und welche Parteien liegen vor?
4. Welche Frist oder Verfahrenshandlung steht als nächstes an?
5. Welche Unterlagen sind schon da: contract, correspondence, notices, expert report, exhibits, prior pleadings?

## Arbeitsworkflow

### beA/ERV-Einreichung englischer Schriftsätze — Praxis-Checkliste

| Punkt | Anforderung | Norm |
| --- | --- | --- |
| Pflicht zur elektronischen Einreichung | seit 01.01.2022 für Rechtsanwälte zwingend (beA-Pflicht) | § 130d ZPO |
| Format der Datei | PDF (idealerweise PDF/A); ZIP für Anlagensammlungen | Verordnungsrecht ERVV |
| Dateigröße | je Nachricht max. 100 MB; bei größeren Schriftsätzen splitten | RAVPV / ERVV |
| Anzahl Anlagen | technische Grenzen beachten; bei vielen Anlagen Index erstellen | Bundle-Index-Skill |
| Qualifizierte elektronische Signatur | Anwalt signiert mit qeS oder per "sicheren Übermittlungsweg" beA-zu-EGVP | § 130a Abs. 3 ZPO |
| Empfangsbestätigung | automatisches Empfangsbekenntnis; Prüfprotokoll prüfen | Beweis der Einreichung |
| Fristwahrung | Eingang bis 24:00 Uhr beim Gericht; vorsorglich Pufferzeit | BGH ständige Rechtsprechung zu Fristbestimmung beA |
| Englische Schriftsätze | technisch behandelt wie deutsche; aber Sprache muss von Spruchkörper akzeptiert sein (§ 184a GVG-Beschluss) | bei rein deutschsprachigen Gerichten zurückweisen-Risiko |
| Anlagenübersetzungen | englische Anlagen technisch zulässig; bei Bedarf beglaubigte Übersetzung gesondert einreichen | JVEG |
| Strukturdaten (XML) | für Mahnverfahren standardisiert; für normale Schriftsätze keine Pflicht | RAVPV |
| beA-Karte und PIN | regelmäßiges Software-Update, Hardware-Token-Validität prüfen | BRAK technische Hinweise |
| Rückläufer / Fehlermeldungen | "Eingangsdokument nicht lesbar" als Risiko bei großen oder verschlüsselten PDFs | vorab Test-Einreichung |

### Trade-off und Praxistipp

- **PDF/A-Konformität:** zwingend für viele Gerichte; reguläres Microsoft-Word-PDF kann zurückgewiesen werden. Lieber Adobe-Acrobat-Export "Save as PDF/A".
- **Anlagen-Bündel:** alle Anlagen in einer ZIP versus einzelne PDF-Dateien — Praxis je Gericht unterschiedlich. Vorher beim Spruchkörper rückfragen.
- **Englische OCR:** englische Anlagen sollten OCR-durchsuchbar sein, damit Richter zitieren können.
- **Notfall-Plan bei beA-Ausfall:** § 130d Satz 2 ZPO ermöglicht ersatzweise Einreichung in Papier mit Glaubhaftmachung der Nichtnutzbarkeit; nur in echten Notfällen.

1. **Forum sichern:** Commercial Court, Commercial Chamber, ordentliches Gericht, Schiedsgericht oder Ausland trennen.
2. **Sprache sichern:** wirksame Englischwahl, notwendige Übersetzungen und deutsch bleibende Verfahrensschritte prüfen.
3. **Prozesshandlung bauen:** Antrag, Schriftsatz, Evidence Map, Timetable, Hearing Script oder Mandantenmemo erstellen.
4. **ZPO-Realität bewahren:** keine US-Discovery, kein Pleading-Theater; Tatsachenvortrag, Beweisangebot, richterliche Prozessleitung und deutsches Kostenrisiko sauber erklären.
5. **Nächsten Schritt festlegen:** Frist, Verantwortliche, Unterlagen, gerichtliche Kommunikation und Mandantenfreigabe.

## Output-Standard

- **Executive Snapshot:** forum, language, next deadline, procedural risk.
- **Procedural Action:** konkreter nächster Antrag/Schriftsatz/Briefing in der gewünschten Sprache.
- **Evidence and Exhibits:** welche Anlagen tragen welchen Punkt, welche Übersetzung fehlt.
- **Risk Flags:** Zuständigkeit, Sprache, Frist, Geheimnis, Kosten, Rechtsmittel.
- **Follow-up Skills:** passende Skills aus diesem Plugin vorschlagen.

## Red Flags

- Commercial-Court-Zuständigkeit oder englische Sprache wird nur behauptet, aber nicht aus Klausel, Gesetz und Landesrecht hergeleitet.
- Englischer Schriftsatz klingt wie US-Litigation und enthält keine ZPO-tauglichen Beweisangebote.
- Anlagen sind englisch/deutsch gemischt, aber Übersetzungs- und Zitierlogik fehlt.
- Geheimhaltungsinteressen werden erst in der mündlichen Verhandlung entdeckt.
- Das Wortprotokoll wird gewünscht, aber nicht rechtzeitig prozessual vorbereitet.

## Quellenregel

Vor echter Verwendung aktuelle Primärquellen prüfen: GVG, ZPO, einschlägige Landesverordnungen und die Gerichtsseite des zuständigen Landes. Keine erfundenen Gerichtslisten, keine erfundenen Formularpflichten, keine Paywall-Fundstellen. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle.
