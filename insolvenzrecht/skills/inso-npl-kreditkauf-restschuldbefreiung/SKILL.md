---
name: inso-npl-kreditkauf-restschuldbefreiung
description: "Inso NPL Kreditkauf Restschuldbefreiung im Plugin Insolvenzrecht: prüft konkret Prüft Kreditkauf notleidender Darlehen vor und im, Restschuldbefreiung Verbraucher und Unternehmer, SCHUFA-/Auskunfteieinträge nach Restschuldbefreiung löschen, Prüft Schuldscheindarlehen im Insolvenzverfahren. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Inso NPL Kreditkauf Restschuldbefreiung

## Arbeitsbereich

**Inso NPL Kreditkauf Restschuldbefreiung** ordnet den Fall über die tragenden Prüffelder: Prüft Kreditkauf notleidender Darlehen vor und im, Restschuldbefreiung Verbraucher und Unternehmer, SCHUFA-/Auskunfteieinträge nach Restschuldbefreiung löschen. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `inso-npl-kreditkauf-krzwmg` | Prüft Kreditkauf notleidender Darlehen vor und im Insolvenzverfahren: Kreditkäufer, Kreditdienstleister, Datenschutz, Notices, Sicherheiten und Enforcement. |
| `inso-restschuldbefreiung-und-versagungsgruende` | Restschuldbefreiung Verbraucher und Unternehmer: 3 Jahre Wohlverhaltensphase seit 2020, Versagungsgruende § 290 InsO (Verurteilung wegen Insolvenzstraftat, Vermoegensverschwendung, falsche Angaben). Pruefraster und Mandantenleitfaden. |
| `inso-schufa-restschuldbefreiung-loeschung` | SCHUFA-/Auskunfteieinträge nach Restschuldbefreiung löschen lassen: Insolvenzbekanntmachung, EuGH C-26/22/C-64/22, DSGVO und Neustartstrategie. |
| `inso-schuldschein-darlehen-in-der-insolvenz` | Prüft Schuldscheindarlehen im Insolvenzverfahren: Forderungsanmeldung, Rang, Abtretung, Sicherheiten, Zahlstelle, Gläubigeridentität und Anfechtung. |

## Arbeitsweg

- Rolle und Ziel im Insolvenzrechtliche Skills zu Zahlungsunfähigkeit, Überschuldung, Antragspflicht und Gläubigerantrag klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO §§ 1, 13-22, 35, 39, 47, 55-56, 60, 80, 87, 129, 133, 174, 175, 270 ff., 286-300, StaRUG §§ 1, 29, 31; StaRUG §§ 1, 29, 31, 39, 49-55, 84, 102, IDW S 6, IDW S 11, InsO § 270 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `inso-npl-kreditkauf-krzwmg`

**Fokus:** Prüft Kreditkauf notleidender Darlehen vor und im Insolvenzverfahren: Kreditkäufer, Kreditdienstleister, Datenschutz, Notices, Sicherheiten und Enforcement.

# Insolvenz: NPL-Kreditkauf und KrZwMG

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenz: NPL-Kreditkauf und KrZwMG` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Wofür dieser Arbeitsgang da ist

Fokus auf Erwerb, Anmeldung, Tabelle, Anfechtung, Planbeteiligung und Loan-to-own.

## Rechts- und Praxisanker

Kreditzweitmarktgesetz, InsO, BGB Abtretung, DSGVO, ZVG.

## Workflow

1. Hochgeladenes Finanzierungsdokument, Schuldschein, Transfer Notice, LMA Facility Agreement oder NPL-Portfolio zuerst identifizieren.
2. Parteiperspektive, Deal-Ziel, Fristen, Consent-Erfordernisse, Sicherheiten und Datenschutzfragen klären.
3. Übertragungsweg, Rechtswirkung, offene Dokumente und Risiken in einer Closing-/Verfahrensmatrix darstellen.
4. Bei Insolvenz-/Krisenbezug Rang, Anfechtung, Planrechte, Enforcement und Geschäftsleiterpflichten gesondert prüfen.

## Output

- Transfer-Memo
- Closing-Checkliste
- Risikoampel mit Unterlagenliste
- Notice-/Q&A-Entwurf, falls genügend Angaben vorliegen

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 2. `inso-restschuldbefreiung-und-versagungsgruende`

**Fokus:** Restschuldbefreiung Verbraucher und Unternehmer: 3 Jahre Wohlverhaltensphase seit 2020, Versagungsgruende § 290 InsO (Verurteilung wegen Insolvenzstraftat, Vermoegensverschwendung, falsche Angaben). Pruefraster und Mandantenleitfaden.

# InsO: Restschuldbefreiung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `InsO: Restschuldbefreiung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Spezialwissen: InsO: Restschuldbefreiung
- **Spezialgegenstand:** InsO: Restschuldbefreiung / inso restschuldbefreiung und versagungsgruende. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** InsO.
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

## 3. `inso-schufa-restschuldbefreiung-loeschung`

**Fokus:** SCHUFA-/Auskunfteieinträge nach Restschuldbefreiung löschen lassen: Insolvenzbekanntmachung, EuGH C-26/22/C-64/22, DSGVO und Neustartstrategie.

# Insolvenzrecht: SCHUFA nach Restschuldbefreiung

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenzrecht: SCHUFA nach Restschuldbefreiung` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Einsatz

Für Schuldner nach erteilter Restschuldbefreiung mit blockierter Bonität.

## Norm- und Quellenanker

InsO §§ 286 ff., 300, 301; InsBekV live prüfen; DSGVO Art. 17; EuGH 07.12.2023 C-26/22/C-64/22.

## Arbeitsfragen

1. Wann wurde Restschuldbefreiung erteilt?
2. Welche Einträge stehen wo?
3. Ist öffentliche Bekanntmachung noch abrufbar?

## Output

Löschungsfahrplan, Auskunfts-/Löschungsschreiben und Bonitäts-Neustartplan.

## Red Flags

- Eintrag bei mehreren Auskunfteien
- Bank nutzt Altdaten intern
- öffentliche Registerfrist ungeprüft

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

## 4. `inso-schuldschein-darlehen-in-der-insolvenz`

**Fokus:** Prüft Schuldscheindarlehen im Insolvenzverfahren: Forderungsanmeldung, Rang, Abtretung, Sicherheiten, Zahlstelle, Gläubigeridentität und Anfechtung.

# Insolvenz: Schuldscheindarlehen

## Fachlicher Kern — Insolvenz- und Sanierungsrecht
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Insolvenz: Schuldscheindarlehen` und löse die dort angelegte Fachfrage; keine Flucht in allgemeines Routing, außer eine echte Frist oder Zuständigkeit ist unklar.
- **Normenradar:** InsO §§ 1, 13, 15a, 17, 18, 19, 21, 38 ff., 47, 49 ff., 55, 80, 103 ff., 129-147, 165 ff., 217 ff., 270 ff., 343; StaRUG; COVInsAG/Übergangsrecht nur bei Altzeiträumen; SGB III § 165.
- **Verifizierte Anker:** BGH, Urteil vom 10.02.2005 - IX ZR 211/02 (Grenzen § 133 InsO bei Zwangsvollstreckung/verschlepptem Antrag als Klassiker); ausländische Verfahren: § 343 InsO Anerkennung, kein deutsches Chapter-15-Verfahren, häufig inzidente Prüfung durch Register, Grundbuch, Prozessgericht und Banken.
- **Arbeitsmodus:** Zuerst Insolvenzgrund, Frist, Organpflicht, Verfahrensstand, Sicherheiten, Massebezug und Anfechtungszeitraum klären; dann Sanierungsfähigkeit, Plan/StaRUG, Haftung und Dokumentationsschutz.
- **Outputpflicht:** Krisenzeitachse, Liquiditätsstatus, Anfechtungsmatrix, Sicherheitenradar, IDW-S6-/Sanierungscheck, Register-/Grundbuch-Nachweispaket oder Schriftsatzbaustein.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.


## Wofür dieser Arbeitsgang da ist

Der Skill hilft Verwalter, Schuldner, Investor und Schuldscheingläubiger, wenn Finanzierungsdokumente nicht zur Tabelle passen.

## Rechts- und Praxisanker

InsO §§ 38, 39, 174 ff., 129 ff., BGB §§ 398 ff., Sicherheitenrecht.

## Workflow

1. Hochgeladenes Finanzierungsdokument, Schuldschein, Transfer Notice, LMA Facility Agreement oder NPL-Portfolio zuerst identifizieren.
2. Parteiperspektive, Deal-Ziel, Fristen, Consent-Erfordernisse, Sicherheiten und Datenschutzfragen klären.
3. Übertragungsweg, Rechtswirkung, offene Dokumente und Risiken in einer Closing-/Verfahrensmatrix darstellen.
4. Bei Insolvenz-/Krisenbezug Rang, Anfechtung, Planrechte, Enforcement und Geschäftsleiterpflichten gesondert prüfen.

## Output

- Transfer-Memo
- Closing-Checkliste
- Risikoampel mit Unterlagenliste
- Notice-/Q&A-Entwurf, falls genügend Angaben vorliegen

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.
