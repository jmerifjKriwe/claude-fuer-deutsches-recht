# Megaprompt: handelsvertreterrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 104 Skills des Plugins `handelsvertreterrecht`.

## Inhaltsverzeichnis

1. **kaltstart-triage** — Startet die Handelsvertreterrechtsprüfung für Status, Vertrag, Provision, Kündigung und Ausgleich.
2. **abrechnung-buchauszug-abschlussprovision** — Unterstützt Handelsvertreter und Unternehmer bei Streitigkeiten über Provisionsabrechnungen und den Buchauszug nach § 87…
3. **abschlussprovision** — Prüft den Provisionsanspruch des Abschlussvertreters nach §§ 87 und 87a HGB: Kausalität zwischen Vermittlungstätigkeit u…
4. **agb-kontrolle** — Prüft AGB-Klauseln in Handelsvertreterverträgen auf Wirksamkeit nach §§ 305 ff. BGB und § 92c HGB: unangemessene Benacht…
5. **alleinvertreter-alters-krankheitskuendigung** — Prüft Rechte und Pflichten des Alleinvertreters nach § 87 Abs. 2 HGB: Anspruch auf Bezirksprovision bei Direktabschlüsse…
6. **alters-krankheitskuendigung** — Analysiert Sonderkündigungsrechte bei Alter oder Krankheit des Handelsvertreters nach § 89 Abs. 3 HGB: außerordentliche …
7. **antikorruption-crm-datenschutz-cross-selling** — Prüft Compliance-Anforderungen und Antikorruptionspflichten im Handelsvertrieb: Pflichten des Handelsvertreters nach § 8…
8. **arbeitnehmeraehnlichkeit** — Prüft arbeitnehmerähnliche Stellung des Handelsvertreters nach § 92a HGB: Mindestentgelt, Anwendung von Arbeitsschutzvor…
9. **ausgleich-im-ma-deal** — Analysiert Ausgleichsansprüche bei M&A-Transaktionen: Vertragsübergang nach § 613a BGB analog, Erlöschen des Ausgleichs …
10. **ausgleich-ma-deal-ausgleichsanmeldung** — Berechnet den Ausgleichsanspruch nach § 89b HGB: Rohertragsberechnung auf Basis der Jahresprovision, Prognoseabzug für N…
11. **ausgleichsanmeldung** — Unterstützt bei fristgerechter Anmeldung des Ausgleichsanspruchs nach § 89b Abs. 4 HGB: Einhaltung der Jahresfrist ab Ve…
12. **ausgleichsanspruch-89b** — Analysiert den Ausgleichsanspruch des Handelsvertreters nach § 89b HGB vollständig: Entstehungsvoraussetzungen (neue Kun…
13. **auskunft-einsicht-auslaendischer-principal** — Unterstützt Handelsvertreter bei Auskunfts- und Einsichtsrechten nach § 87c Abs. 2 HGB und § 242 BGB: Umfang des Buchaus…
14. **auslaendischer-principal** — Analysiert Handelsvertreterverträge mit ausländischem Unternehmer: anwendbares Recht nach Rom-I-VO, zwingende Schutzvors…
15. **beweis-sicherung** — Unterstützt Handelsvertreter und Unternehmer bei der Beweissicherung für Provisionsstreitigkeiten: Sicherung von Verträg…

---

## Skill: `kaltstart-triage`

_Startet die Handelsvertreterrechtsprüfung für Status, Vertrag, Provision, Kündigung und Ausgleich._

# Allgemein

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Handelsvertreterrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Wofür dieser Arbeitsgang da ist
Wer ist was, welche Geschäfte, welche Vergütung, welches Gebiet, welches Ende und welcher Anspruch.

Dieser Skill arbeitet nicht als abstraktes Merkblatt. Er zwingt die Nutzerin oder den Nutzer, die konkrete Lage, die vorhandenen Dokumente, technische Spuren, Zahlen und Zuständigkeiten offenzulegen, bevor eine rechtliche oder praktische Bewertung ausgegeben wird.

## Kaltstartfragen

- Welche konkrete Entscheidung steht jetzt an und wer muss sie verantworten?
- Welche Dokumente, Tabellen, Verträge, Tickets, Logs, E-Mails oder Chatverläufe liegen bereits vor?
- Welche Frist, Behörde, Vertragspartei, Kundengruppe oder interne Eskalation macht Druck?
- Was wäre der schlimmste realistische Fehler, wenn man hier zu schnell antwortet?
- Welche Quelle muss live geprüft werden, bevor eine Norm, Frist oder Rechtsprechung zitiert wird?

## Arbeitslogik

1. **Sachverhalt festnageln:** Beteiligte, Zeitraum, Dokumente, Zahlen, Systeme, Rollen und offene Lücken in einer kurzen Matrix erfassen.
2. **Pflichtanker setzen:** Maßgebliche Normen und Behördenquellen live prüfen; keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate verwenden.
3. **Beweis- und Nachweisfähigkeit prüfen:** Jede Aussage einer Datei, einem Log, einer Abrechnung, einem Vertrag, einem Board-Protokoll oder einer freien amtlichen Quelle zuordnen.
4. **Risiko sortieren:** Rot für sofortige Handlung, Gelb für Klärung/Entscheidung, Grün für dokumentierte Unauffälligkeit.
5. **Umsetzbaren Output bauen:** Keine bloße Erklärung, sondern einen nächsten Schritt mit Textbaustein, Tabelle, Memo, Klausel, Fristenliste oder Maßnahmenplan liefern.

## Fachanker

- Primärer Anker: HGB §§ 84-92c; RL 86/653/EWG.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Fallfahrplan. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

---

## Skill: `abrechnung-buchauszug-abschlussprovision`

_Unterstützt Handelsvertreter und Unternehmer bei Streitigkeiten über Provisionsabrechnungen und den Buchauszug nach § 87c HGB: Prüfung von Vollständigkeit und Richtigkeit der Abrechnung, Formulierung von Buchauszugsverlangen, Klageerhebung bei Verweigerung sowie Auswertung übergebener Daten auf L..._

# Provisionsabrechnung und Buchauszug nach § 87c HGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Provisionsabrechnung und Buchauszug nach § 87c HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X stellt fest, dass Unternehmer Y seit 18 Monaten keine vollständige Provisionsabrechnung übermittelt; X verlangt Buchauszug über alle vermittelten und abgeschlossenen Geschäfte nach § 87c Abs. 2 HGB.
- Unternehmer Y bestreitet, dass bestimmte Kunden vom Bezirk des X umfasst waren; X klagt auf Erteilung des Buchauszugs und ergänzende Auskunft.
- Handelsvertreterin Z prüft, ob die vom Unternehmer vorgelegte Abrechnung alle provisionspflichtigen Geschäfte enthält, insbesondere Direktabschlüsse und Folgegeschäfte.

## Erste Schritte

1. Vertrag und Provisionsvereinbarungen sichten; Abrechnungszeitraum und Rückstände bestimmen.
2. Schriftliches Buchauszugsverlangen nach § 87c Abs. 2 HGB formulieren und per Einschreiben übersenden.
3. Gelieferte Buchauszüge auf Vollständigkeit prüfen: alle Kunden, Aufträge, Umsätze, Rabatte, Stornos.
4. Fehlende Positionen in Differenzaufstellung erfassen und Nachforderung beziffern.
5. Bei Verweigerung: Klage auf Erteilung des Buchauszugs (Stufenklage nach § 254 ZPO) vorbereiten.
6. Verjährungsfristen nach § 195 BGB (3 Jahre) und Beginn nach § 199 BGB prüfen.

## Rechtsrahmen

- § 87c HGB — Provisionsabrechnung und Buchauszugsanspruch des Handelsvertreters
- § 87 HGB — Provisionsanspruch und provisionspflichtige Geschäfte
- § 87a HGB — Entstehung und Fälligkeit des Provisionsanspruchs
- § 254 ZPO — Stufenklage (Auskunft und Leistung)
- § 195 BGB — Regelmäßige Verjährungsfrist drei Jahre
- Art. 12 RL 86/653/EWG — Provisionsanspruch des Handelsvertreters

## Prüfraster

- Ist der Buchauszugsanspruch entstanden (Handelsvertretervertrag, provisionspflichtige Geschäfte)?
- Umfasst der vorgelegte Buchauszug alle vertragsrelevanten Geschäfte und Kunden?
- Wurden Stornoreserven oder Rückbuchungen korrekt und nachvollziehbar ausgewiesen?
- Ist der Abrechnungszeitraum vollständig abgedeckt, einschließlich Direktgeschäfte des Unternehmers?
- Besteht ein ergänzender Auskunftsanspruch nach § 87c Abs. 2 HGB bei unklaren Positionen?
- Sind Verjährungsfristen für einzelne Abrechnungsperioden bereits abgelaufen?
- Kommt eine Stufenklage auf Buchauszug, Abrechnung und Zahlung in Betracht?

## Typische Fallstricke

- Buchauszugsverlangen nicht schriftlich oder ohne genaue Periodenangabe gestellt — Beweisschwierigkeiten.
- Verjährung einzelner Provisionsforderungen übersehen, obwohl Buchauszugsanspruch noch offen ist.
- Unternehmer legt unvollständigen Buchauszug vor; Handelsvertreter akzeptiert ohne Gegenkontrolle.
- Stornoreserven ohne vertragliche Grundlage einbehalten — Prüfung der AGB-Konformität versäumt.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 87c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87c.html)
- [§ 87 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87.html)
- [§ 254 ZPO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/__254.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 87c HGB](https://dejure.org/gesetze/HGB/87c.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 9 Rom-I-VO
- Art. 101 AEUV
- Art. 28 DSGVO
- § 14 UStG
- § 19 UStG
- § 5 ArbGG
- § 59 VVG
- § 1 UStG
- § 23 GeschGehG
- § 66c EnWG
- Art. 17 DSGVO
- § 75 AMG

### Leitentscheidungen

- EuGH C-465/04
- EuGH C-381/19
- EuGH C-217/05

---

## Skill: `abschlussprovision`

_Prüft den Provisionsanspruch des Abschlussvertreters nach §§ 87 und 87a HGB: Kausalität zwischen Vermittlungstätigkeit und Vertragsabschluss, Fälligkeit mit Ausführung durch den Unternehmer, Ansprüche bei vorzeitiger Vertragsauflösung sowie Abgrenzung von Abschluss- und Vermittlungsprovision im H..._

# Abschlussprovision des Abschlussvertreters nach §§ 87 und 87a HGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Abschlussprovision des Abschlussvertreters nach §§ 87 und 87a HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter A hat einen Kaufvertrag zwischen Kunde K und Unternehmer U abgeschlossen; U verweigert die Provisionszahlung mit Hinweis auf angeblich fehlende Kausalität der Vermittlung.
- Unternehmer U löst einen vom Vertreter A abgeschlossenen Vertrag einvernehmlich mit dem Kunden auf; A verlangt seine Provision nach § 87a Abs. 3 HGB.
- Handelsvertreter A streitet mit U darüber, ob ein bestimmter Auftrag im Rahmen der Abschlussvertretung oder außerhalb seiner Vollmacht zustande kam.

## Erste Schritte

1. Vertragsart klären: Abschlussvertreter mit Vollmacht oder Vermittlungsvertreter ohne Abschlussvollmacht?
2. Kausalzusammenhang zwischen Tätigkeit des Vertreters und Vertragsabschluss dokumentieren.
3. Fälligkeitszeitpunkt nach § 87a Abs. 1 HGB bestimmen: Ausführung des Geschäfts durch Unternehmer.
4. Provisionssatz und Bemessungsgrundlage aus dem Vertretervertrag ermitteln.
5. Bei vorzeitiger Aufhebung: Prüfung nach § 87a Abs. 3 HGB, ob Aufhebung dem Unternehmer zuzurechnen ist.
6. Verjährung prüfen: §§ 195, 199 BGB; Abschlusszeitpunkt festhalten.

## Rechtsrahmen

- § 87 HGB — Entstehung des Provisionsanspruchs, Kausalität
- § 87a HGB — Fälligkeit und Erlöschen der Provision
- § 87a Abs. 3 HGB — Provision bei nicht ausgeführtem Geschäft ohne Vertreterverschulden
- § 84 HGB — Begriff des Handelsvertreters und Selbständigkeit
- § 54 HGB — Handlungsvollmacht des Abschlussvertreters
- Art. 7 und 8 RL 86/653/EWG — Provisionsanspruch auf abgeschlossene und ausgeführte Geschäfte

## Prüfraster

- Hat der Handelsvertreter den Vertragsabschluss tatsächlich herbeigeführt oder wesentlich mitgewirkt?
- Ist das Geschäft wirksam zustande gekommen und liegt im Vertragsgebiet oder beim Kundenstamm des Vertreters?
- Hat der Unternehmer das Geschäft ausgeführt oder verweigert er dies ohne Verschulden des Vertreters?
- Liegt eine einvernehmliche Aufhebung vor, die dem Unternehmer nach § 87a Abs. 3 HGB zuzurechnen ist?
- Entspricht die berechnete Provision dem vereinbarten Satz und der richtigen Bemessungsgrundlage?
- Ist der Anspruch verjährt oder durch vertragliche Ausschlussfristen erloschen?

## Typische Fallstricke

- Kausalität nicht ausreichend dokumentiert — Unternehmer bestreitet Vermittlungsleistung.
- Fälligkeitszeitpunkt falsch bestimmt: Provision erst fällig, wenn Unternehmer das Geschäft ausführt.
- § 87a Abs. 3 HGB bei einvernehmlicher Vertragsaufhebung übersehen.
- Abschlussvertreter handelt ohne ausreichende Vollmacht — Provisionsanspruch gefährdet.
- Provisionssatz aus alten Vertragsversionen übernommen — aktuelle Fassung nicht geprüft.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 87 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87.html)
- [§ 87a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87a.html)
- [§ 84 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__84.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 87 HGB](https://dejure.org/gesetze/HGB/87.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 9 Rom-I-VO
- Art. 101 AEUV
- Art. 28 DSGVO
- § 14 UStG
- § 19 UStG
- § 5 ArbGG
- § 59 VVG
- § 1 UStG
- § 23 GeschGehG
- § 66c EnWG
- Art. 17 DSGVO
- § 75 AMG

### Leitentscheidungen

- EuGH C-465/04
- EuGH C-381/19
- EuGH C-217/05

---

## Skill: `agb-kontrolle`

_Prüft AGB-Klauseln in Handelsvertreterverträgen auf Wirksamkeit nach §§ 305 ff. BGB und § 92c HGB: unangemessene Benachteiligung bei Provisionsregelungen, Ausgleichsausschlüssen, Wettbewerbsverboten sowie unzulässige Abweichungen vom zwingenden Handelsvertreterrecht nach §§ 84-92c HGB im Handelsv..._

# AGB-Kontrolle im Handelsvertretervertrag nach §§ 305 ff. BGB und § 92c HGB

## Arbeitsbereich

Prüft AGB-Klauseln in Handelsvertreterverträgen auf Wirksamkeit nach §§ 305 ff. BGB und § 92c HGB: unangemessene Benachteiligung bei Provisionsregelungen, Ausgleichsausschlüssen, Wettbewerbsverboten sowie unzulässige Abweichungen vom zwingenden Handelsvertreterrecht nach §§ 84-92c HGB. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um AGB-Kontrolle im Handelsvertretervertrag nach §§ 305 ff. BGB und § 92c HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X erhält vom Unternehmer Y vorformulierte Vertragsbedingungen mit einer Klausel, die den Ausgleichsanspruch vollständig ausschließt; X prüft die Wirksamkeit nach § 89b Abs. 4 HGB.
- Unternehmer Y verwendet eine AGB-Klausel, die Provisionen um 20 % kürzt, wenn der Jahresumsatz ein bestimmtes Ziel verfehlt; die Klausel wird auf Wirksamkeit nach § 307 BGB geprüft.
- Handelsvertreter X findet in seinem Vertrag eine AGB-Klausel, die das Wettbewerbsverbot auf fünf Jahre verlängert und keine Karenzentschädigung vorsieht; X lässt die Klausel auf Verstoß gegen § 90a HGB prüfen.

## Erste Schritte

1. Vertrag auf vorformulierte Klauseln i.S.v. § 305 BGB identifizieren.
2. Zwingende Normen des Handelsvertreterrechts (§§ 84-92c HGB) als Prüfmaßstab herausarbeiten.
3. Einzelne Klauseln auf unangemessene Benachteiligung nach § 307 BGB prüfen.
4. Klauselverbote nach §§ 308, 309 BGB auf handelsvertretertypische Klauseln anwenden.
5. Klauseln, die vom zwingenden Recht abweichen, nach § 92c HGB auf Zulässigkeit prüfen.
6. Nichtige Klauseln identifizieren und Rechtsfolgen (Wegfall, gesetzliche Regelung) bestimmen.

## Rechtsrahmen

- §§ 305–310 BGB — AGB-Recht, Einbeziehung, Inhaltskontrolle
- § 307 BGB — Unangemessene Benachteiligung
- § 92c HGB — Zwingende Vorschriften des Handelsvertreterrechts
- § 89b Abs. 4 HGB — Zwingende Natur des Ausgleichsanspruchs
- § 90a Abs. 1 S. 2 HGB — Mindestinhalt der Wettbewerbsabrede
- Art. 19 RL 86/653/EWG — Unabdingbare Rechte des Handelsvertreters

## Prüfraster

- Sind die streitigen Klauseln AGB i.S.v. § 305 Abs. 1 BGB oder individuell ausgehandelt?
- Weichen die Klauseln von zwingenden Vorschriften der §§ 84-92c HGB ab?
- Liegt eine unangemessene Benachteiligung nach § 307 BGB vor?
- Verstoßen einzelne Klauseln gegen konkrete Klauselverbote der §§ 308, 309 BGB?
- Was sind die Rechtsfolgen der Nichtigkeit — Gesamtnichtigkeit oder Teilwegfall?
- Ist die Klausel durch ergänzende Vertragsauslegung zu ersetzen oder gilt dispositives Recht?

## Typische Fallstricke

- Zwingendes Handelsvertreterrecht (§ 92c HGB) nicht als Maßstab berücksichtigt.
- Kaufmännische AGB-Kontrolle mit verbraucherrechtlichem Maßstab verwechselt.
- Ausgleichsausschlussklauseln als wirksam behandelt, obwohl § 89b Abs. 4 HGB diese verbietet.
- Nichtigkeit der Klausel führt nicht automatisch zur Gesamtnichtigkeit des Vertrags (§ 306 BGB).

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 307 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__307.html)
- [§ 92c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__92c.html)
- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 307 BGB](https://dejure.org/gesetze/BGB/307.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 9 Rom-I-VO
- Art. 101 AEUV
- Art. 28 DSGVO
- § 14 UStG
- § 19 UStG
- § 5 ArbGG
- § 59 VVG
- § 1 UStG
- § 23 GeschGehG
- § 66c EnWG
- Art. 17 DSGVO
- § 75 AMG

### Leitentscheidungen

- EuGH C-465/04
- EuGH C-381/19
- EuGH C-217/05

---

## Skill: `alleinvertreter-alters-krankheitskuendigung`

_Prüft Rechte und Pflichten des Alleinvertreters nach § 87 Abs. 2 HGB: Anspruch auf Bezirksprovision bei Direktabschlüssen des Unternehmers, Abgrenzung zum Alleinvertriebsrecht, Beweislast bei Bestellung eines weiteren Vertreters sowie Schadensersatz bei Verletzung der Alleinvertretungsabrede im H..._

# Alleinvertreter und Bezirksprovision nach § 87 Abs. 2 HGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Alleinvertreter und Bezirksprovision nach § 87 Abs. 2 HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Alleinvertreter A stellt fest, dass Unternehmer U direkte Vertragsabschlüsse mit Kunden im Vertragsgebiet des A tätigt, ohne diesem Provision zu zahlen; A klagt auf Bezirksprovision nach § 87 Abs. 2 HGB.
- Unternehmer U hat einen zweiten Handelsvertreter im gleichen Gebiet eingesetzt; Alleinvertreter A macht Schadensersatz und Unterlassung geltend.
- Alleinvertreter A und Unternehmer U streiten darüber, ob ein Großkunde dem Alleinvertretungsgebiet zuzuordnen ist oder als Key-Account direkt betreut werden darf.

## Erste Schritte

1. Alleinvertretungsklausel im Vertretervertrag auf Umfang und Gebietsdefinition prüfen.
2. Direktgeschäfte des Unternehmers im Gebiet ermitteln und dokumentieren.
3. Provisionsanspruch nach § 87 Abs. 2 HGB für Direktabschlüsse berechnen.
4. Abgrenzung: Alleinvertretung vs. Alleinvertriebsrecht (exklusiver Vertriebshändler).
5. Schadensersatzanspruch bei Verletzung der Alleinvertretungsabrede prüfen.
6. Key-Account-Ausnahmen im Vertrag identifizieren und auf Wirksamkeit prüfen.

## Rechtsrahmen

- § 87 Abs. 2 HGB — Bezirksprovision des Alleinvertreters
- § 87 Abs. 1 HGB — Provisionspflichtige Geschäfte
- § 280 BGB — Schadensersatz bei Verletzung der Alleinvertretungsabrede
- § 86a HGB — Pflicht des Unternehmers zur Unterstützung
- Art. 7 RL 86/653/EWG — Provisionsanspruch auf Gebietsgeschäfte
- § 242 BGB — Treu und Glauben bei Gebietszuweisung

## Prüfraster

- Ist eine Alleinvertretungsabrede wirksam vereinbart und wie ist das Gebiet definiert?
- Hat der Unternehmer im Alleinvertretungsgebiet Direktabschlüsse ohne Zustimmung getätigt?
- Besteht nach § 87 Abs. 2 HGB ein Provisionsanspruch für diese Direktabschlüsse?
- Gibt es vertragliche Key-Account- oder Sonderkundenregelungen, die Direktgeschäfte erlauben?
- Welche Schäden entstehen dem Alleinvertreter durch unbefugte Direktgeschäfte des Unternehmers?
- Ist die Alleinvertretungsabrede nach AGB-Recht wirksam?

## Typische Fallstricke

- Alleinvertretungsgebiet nicht klar definiert — Streit über Zugehörigkeit einzelner Kunden.
- Key-Account-Ausnahmen nicht ausdrücklich vereinbart — Unternehmer kann Direktgeschäfte nicht rechtfertigen.
- Bezirksprovision nach § 87 Abs. 2 HGB mit allgemeiner Provision verwechselt.
- Beweislast für Direktabschlüsse liegt beim Handelsvertreter — Dokumentation erforderlich.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 87 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87.html)
- [§ 86a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__86a.html)
- [§ 280 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__280.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 87 HGB](https://dejure.org/gesetze/HGB/87.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 9 Rom-I-VO
- Art. 101 AEUV
- Art. 28 DSGVO
- § 14 UStG
- § 19 UStG
- § 5 ArbGG
- § 59 VVG
- § 1 UStG
- § 23 GeschGehG
- § 66c EnWG
- Art. 17 DSGVO
- § 75 AMG

### Leitentscheidungen

- EuGH C-465/04
- EuGH C-381/19
- EuGH C-217/05

---

## Skill: `alters-krankheitskuendigung`

_Analysiert Sonderkündigungsrechte bei Alter oder Krankheit des Handelsvertreters nach § 89 Abs. 3 HGB: außerordentliche Kündigung wegen dauerhafter Arbeitsunfähigkeit, angemessene Kündigungsfristen, Auswirkungen auf Ausgleichs- und Provisionsansprüche sowie Gestaltung von Aufhebungsvereinbarungen..._

# Kündigung wegen Alters oder Krankheit des Handelsvertreters nach § 89 Abs. 3 HGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Kündigung wegen Alters oder Krankheit des Handelsvertreters nach § 89 Abs. 3 HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X ist seit 14 Monaten krankheitsbedingt nicht mehr in der Lage, sein Vertretungsgebiet zu bearbeiten; Unternehmer Y will das Vertreterverhältnis beenden und prüft das Vorgehen.
- Handelsvertreter X möchte wegen schwerer Erkrankung selbst kündigen und den Ausgleichsanspruch trotzdem erhalten; er prüft § 89b Abs. 3 Nr. 2 HGB.
- Unternehmer Y kündigt dem 72-jährigen Handelsvertreter X ordentlich; X bestreitet, dass Alter allein ein Kündigungsgrund sei, und verlangt längere Frist.

## Erste Schritte

1. Krankheitsdauer und Prognose ärztlich dokumentieren lassen.
2. Anwendbarkeit von § 89 Abs. 3 HGB (außerordentliche Kündigung bei Dauerunfähigkeit) prüfen.
3. Ordentliche Kündigungsfristen nach § 89 HGB bestimmen und mit Sonderrecht vergleichen.
4. Auswirkung auf Ausgleichsanspruch nach § 89b Abs. 3 Nr. 2 HGB (Kündigung aus gesundheitlichen Gründen) prüfen.
5. Versorgungsansprüche und Sozialversicherungsstatus klären.
6. Aufhebungsvereinbarung als Alternative zur einseitigen Kündigung prüfen.

## Rechtsrahmen

- § 89 Abs. 3 HGB — Außerordentliche Kündigung bei dauerhafter Arbeitsunfähigkeit
- § 89 HGB — Ordentliche Kündigung und Fristen
- § 89b Abs. 3 Nr. 2 HGB — Kein Ausgleichsausschluss bei krankheitsbedingter Kündigung des Vertreters
- § 89a HGB — Kündigung aus wichtigem Grund
- § 241 Abs. 2 BGB — Rücksichtnahmepflicht des Unternehmers
- Art. 18 RL 86/653/EWG — Ausschluss des Ausgleichs nur bei schuldhaftem Verhalten

## Prüfraster

- Liegt eine dauerhafte Unfähigkeit zur Ausübung der Vertretertätigkeit vor?
- Sind die Voraussetzungen für außerordentliche Kündigung nach § 89 Abs. 3 HGB erfüllt?
- Welche Kündigungsfrist gilt bei ordentlicher Kündigung nach § 89 HGB?
- Bleibt der Ausgleichsanspruch nach § 89b Abs. 3 Nr. 2 HGB erhalten?
- Hat der Vertreter selbst aus Gesundheitsgründen gekündigt — Ausgleich nach § 89b Abs. 3 Nr. 2 HGB?
- Sind Versorgungsleistungen oder Pensionszusagen im Vertrag vorhanden?

## Typische Fallstricke

- Außerordentliche Kündigung ohne ärztlichen Nachweis dauerhafter Arbeitsunfähigkeit — angreifbar.
- Ausgleichsanspruch bei krankheitsbedingter Eigenkündigung des Vertreters irrtümlich verneint.
- Ordentliche Kündigung ohne Einhaltung der gesetzlichen Fristen — Unwirksamkeit.
- Diskriminierung wegen Alters als eigenständiger Kündigungsgrund — AGG beachten.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 89 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89.html)
- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [§ 89a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89a.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 89b HGB](https://dejure.org/gesetze/HGB/89b.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 9 Rom-I-VO
- Art. 101 AEUV
- Art. 28 DSGVO
- § 14 UStG
- § 19 UStG
- § 5 ArbGG
- § 59 VVG
- § 1 UStG
- § 23 GeschGehG
- § 66c EnWG
- Art. 17 DSGVO
- § 75 AMG

### Leitentscheidungen

- EuGH C-465/04
- EuGH C-381/19
- EuGH C-217/05

---

## Skill: `antikorruption-crm-datenschutz-cross-selling`

_Prüft Compliance-Anforderungen und Antikorruptionspflichten im Handelsvertrieb: Pflichten des Handelsvertreters nach § 86 HGB zur Interessenwahrung, Offenlegungspflichten bei Interessenkonflikten, Haftungsrisiken bei Bestechungszahlungen nach StGB und Vorgaben des Lieferkettensorgfaltspflichtenge..._

# Compliance und Antikorruption im Handelsvertretervertrieb

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Compliance und Antikorruption im Handelsvertretervertrieb.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel sind konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Unternehmer U erfährt, dass sein Handelsvertreter X Schmiergeldzahlungen an Einkäufer von Kunden geleistet hat; U prüft außerordentliche Kündigung nach § 89a HGB und Schadensersatz.
- Handelsvertreter X soll für ausländischen Unternehmer Y in einem Hochrisikoland tätig werden; X fragt nach Compliance-Anforderungen und Haftungsrisiken.
- Unternehmer U erhält eine behördliche Anfrage wegen möglicher Bestechlichkeit durch seinen Handelsvertreter X; U klärt seine Haftung und Meldepflichten.

## Erste Schritte

1. Vertrag auf Compliance-Klauseln, Offenlegungspflichten und Antikorruptionsklauseln prüfen.
2. Pflichten des Handelsvertreters nach § 86 HGB (Interessenwahrung, Weisungsbefolge) analysieren.
3. Strafrechtliche Haftungsrisiken nach §§ 299, 333 StGB prüfen.
4. LkSG-Anforderungen bei internationaler Vertriebsstruktur klären.
5. Kündigung wegen Compliance-Verstoß nach § 89a HGB auf Verhältnismäßigkeit prüfen.
6. Schadensersatz nach § 280 BGB und § 89a Abs. 2 HGB berechnen.

## Rechtsrahmen

- § 86 Abs. 1 HGB — Interessenwahrungspflicht des Handelsvertreters
- § 89a HGB — Außerordentliche Kündigung wegen Compliance-Verstoß
- §§ 299, 333 StGB — Bestechlichkeit und Bestechung im Geschäftsverkehr
- § 30 OWiG — Verbandsgeldbuße bei Mitarbeiterkorruption
- § 3 LkSG — Sorgfaltspflichten im Lieferkettengesetz
- § 280 BGB — Schadensersatz bei Pflichtverletzung

## Prüfraster

- Hat der Handelsvertreter seine Interessenwahrungspflicht nach § 86 HGB verletzt?
- Liegt ein Compliance-Verstoß vor, der eine außerordentliche Kündigung rechtfertigt?
- Haftet der Unternehmer für Handlungen seines Handelsvertreters Dritten gegenüber?
- Sind LkSG-Sorgfaltspflichten im internationalen Vertrieb eingehalten?
- Hat der Unternehmer ausreichende Compliance-Maßnahmen implementiert?
- Welche strafrechtlichen Risiken bestehen für Handelsvertreter und Unternehmer?

## Typische Fallstricke

- Compliance-Verstöße des Handelsvertreters führen zu Haftung des Unternehmers als Auftraggeber.
- Kündigung wegen Compliance-Verstoß ohne vorherige Abmahnung bei heilbaren Verstößen unwirksam.
- LkSG-Anforderungen bei indirekten Lieferanten über Handelsvertreter übersehen.
- Strafrechtliches Risiko für Unternehmer bei Duldung von Korruption durch Handelsvertreter.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Zwingende Vorschriften nach § 92c HGB können vertraglich nicht abgebedungen werden;
entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) sowie Kündigung (§§ 89, 89a HGB).

## Quellen

- [§ 86 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__86.html)
- [§ 89a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89a.html)
- [§ 299 StGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/stgb/__299.html)
- [LkSG auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/lksg/)
- [Dejure § 86 HGB](https://dejure.org/gesetze/HGB/86.html)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- Art. 9 Rom-I-VO
- Art. 101 AEUV
- Art. 28 DSGVO
- § 14 UStG
- § 19 UStG
- § 5 ArbGG
- § 59 VVG
- § 1 UStG
- § 23 GeschGehG
- § 66c EnWG
- Art. 17 DSGVO
- § 75 AMG

### Leitentscheidungen

- EuGH C-465/04
- EuGH C-381/19
- EuGH C-217/05

---

## Skill: `arbeitnehmeraehnlichkeit`

_Prüft arbeitnehmerähnliche Stellung des Handelsvertreters nach § 92a HGB: Mindestentgelt, Anwendung von Arbeitsschutzvorschriften, Abgrenzung zur echten Arbeitnehmerstellung, wirtschaftliche Abhängigkeit als Tatbestandsmerkmal und Sozialversicherungsrecht bei Einkommen unter der Grenze im Handels..._

# Arbeitnehmerähnlicher Handelsvertreter nach § 92a HGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Arbeitnehmerähnlicher Handelsvertreter nach § 92a HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreterin Z erzielt 95 % ihres Einkommens bei einem einzigen Unternehmer U und fragt, ob ihr arbeitsrechtlicher Schutz nach § 92a HGB zusteht.
- Unternehmer U erhält von der Deutschen Rentenversicherung eine Anfrage zur Scheinselbständigkeit der Vertreterin Z; er klärt, ob eine arbeitnehmerähnliche Stellung vorliegt.
- Handelsvertreter X möchte wissen, ob das Mindestentgelt nach der Handelsvertreter-Mindestentgelts-Verordnung auf ihn Anwendung findet.

## Erste Schritte

1. Einkommensquellen des Handelsvertreters analysieren: Anteil des Einkommens beim Hauptunternehmer.
2. Prüfung der wirtschaftlichen Abhängigkeit nach § 92a Abs. 1 HGB (mehr als ein Drittel des Einkommens).
3. Anwendbarkeit der Handelsvertreter-Mindestentgeltsverordnung prüfen.
4. Sozialversicherungsrechtlichen Status parallel klären (§ 7 SGB IV).
5. Abgrenzung Arbeitnehmerähnlichkeit von echter Arbeitnehmerstellung nach BAG-Kriterien.
6. Vertragsgestaltung auf Weisungsabhängigkeit und persönliche Leistungspflicht untersuchen.

## Rechtsrahmen

- § 92a HGB — Arbeitnehmerähnlicher Handelsvertreter
- § 84 Abs. 1 HGB — Selbständigkeit als Abgrenzungsmerkmal
- § 7 SGB IV — Begriff der Beschäftigung, Scheinselbständigkeit
- § 5 Abs. 3 ArbGG — Zuständigkeit der Arbeitsgerichte für arbeitnehmerähnliche Personen
- § 92b HGB — Einfirmenvertreter
- Art. 1 Abs. 2 RL 86/653/EWG — Anwendungsbereich der Richtlinie

## Prüfraster

- Wie hoch ist der Anteil des Einkommens vom Hauptunternehmer — übersteigt er ein Drittel?
- Besteht persönliche Leistungspflicht oder darf der Vertreter Untervertreter einsetzen?
- Hat der Handelsvertreter eigene unternehmerische Organisation oder ist er vollständig eingegliedert?
- Ist wirtschaftliche Abhängigkeit i.S.v. § 92a HGB gegeben?
- Welcher Rechtsweg ist zuständig — ordentliche Gerichte oder Arbeitsgericht nach § 5 Abs. 3 ArbGG?
- Ist die Mindestentgeltsverordnung anwendbar und wird sie eingehalten?

## Typische Fallstricke

- Arbeitnehmerähnlichkeit mit Scheinselbständigkeit gleichgesetzt — unterschiedliche Rechtsfolgen.
- Sozialversicherungsrechtliche Konsequenzen bei Scheinselbständigkeit nicht berücksichtigt.
- Zuständigkeit der Arbeitsgerichte nach § 5 Abs. 3 ArbGG übersehen.
- Einkommensschwelle nicht korrekt berechnet — Mehrjahresbetrachtung erforderlich.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 92a HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__92a.html)
- [§ 84 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__84.html)
- [§ 7 SGB IV auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/sgb_4/__7.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 92a HGB](https://dejure.org/gesetze/HGB/92a.html)

---

## Skill: `ausgleich-im-ma-deal`

_Analysiert Ausgleichsansprüche bei M&A-Transaktionen: Vertragsübergang nach § 613a BGB analog, Erlöschen des Ausgleichs nach § 89b Abs. 3 Nr. 3 HGB bei Übertragung der Agentur, Gestaltungsmöglichkeiten im Share- vs. Asset-Deal, Haftungszuweisung zwischen Veräußerer und Erwerber sowie Due-Diligenc..._

# Ausgleichsanspruch bei M&A-Transaktionen und Unternehmensübergang

## Arbeitsbereich

Analysiert Ausgleichsansprüche bei M&A-Transaktionen: Vertragsübergang nach § 613a BGB analog, Erlöschen des Ausgleichs nach § 89b Abs. 3 Nr. 3 HGB bei Übertragung der Agentur, Gestaltungsmöglichkeiten im Share- vs. Asset-Deal, Haftungszuweisung zwischen Veräußerer und Erwerber sowie Due-Diligence-Checkliste. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Ausgleichsanspruch bei M&A-Transaktionen und Unternehmensübergang.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X erfährt, dass Unternehmer Y sein Unternehmen an Erwerber Z verkauft hat; X klärt, ob sein Ausgleichsanspruch gegen Y oder Z geltend zu machen ist.
- Erwerber Z übernimmt im Asset-Deal alle Handelsvertreterverträge; er prüft, ob bestehende Ausgleichsansprüche auf ihn übergehen oder ob Y haftet.
- Im Share-Deal verbleibt der Unternehmer als GmbH; Handelsvertreter X klärt, ob die Veräußerung der Gesellschaftsanteile seine Rechte berührt.

## Erste Schritte

1. Transaktionsstruktur bestimmen: Share-Deal (Anteile) vs. Asset-Deal (Betrieb/Verträge).
2. Vertragsübergang bei Asset-Deal nach § 613a BGB analog oder vertraglicher Übernahme prüfen.
3. Ausgleichsanspruch nach § 89b Abs. 3 Nr. 3 HGB: erlischt er bei Vertragsübertragung?
4. Haftungsverteilung zwischen Veräußerer und Erwerber in SPA und Übergangsvertrag prüfen.
5. Ausgleichsrückstellungen in der Bilanz des Unternehmers identifizieren.
6. Due-Diligence-Checkliste für offene Ausgleichsansprüche aller Handelsvertreter erstellen.

## Rechtsrahmen

- § 89b Abs. 3 Nr. 3 HGB — Ausschluss des Ausgleichs bei Übertragung der Agentur
- § 89b Abs. 1 HGB — Entstehungsvoraussetzungen des Ausgleichsanspruchs
- § 613a BGB — Betriebsübergang (analog bei Vertragsübernahme)
- § 25 HGB — Haftung des Erwerbers bei Firmenfortführung
- § 414 BGB — Schuldübernahme
- Art. 17 RL 86/653/EWG — Ausgleichsanspruch bei Vertragsende

## Prüfraster

- Handelt es sich um einen Share-Deal oder Asset-Deal?
- Gehen Handelsvertreterverträge auf den Erwerber über?
- Erlischt der Ausgleichsanspruch nach § 89b Abs. 3 Nr. 3 HGB durch Agenturübertragung?
- Wer haftet für Ausgleichsansprüche — Veräußerer, Erwerber oder beide gesamtschuldnerisch?
- Sind bestehende Ausgleichsansprüche in der Due Diligence identifiziert und bewertet?
- Schützt der Kaufvertrag den Erwerber durch Freistellungs- oder Garantieklauseln?

## Typische Fallstricke

- Ausgleichsansprüche in der Due Diligence nicht erfasst — unerwartete Haftung des Erwerbers.
- § 89b Abs. 3 Nr. 3 HGB zu weit ausgelegt — nicht jede Unternehmensübertragung schließt Ausgleich aus.
- Keine klare Haftungsverteilung im SPA — Veräußerer und Erwerber streiten über Freistellung.
- Rückstellungen für Ausgleichsansprüche unzureichend bewertet — Kaufpreisrisiko.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [§ 613a BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__613a.html)
- [§ 25 HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__25.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 89b HGB](https://dejure.org/gesetze/HGB/89b.html)

---

## Skill: `ausgleich-ma-deal-ausgleichsanmeldung`

_Berechnet den Ausgleichsanspruch nach § 89b HGB: Rohertragsberechnung auf Basis der Jahresprovision, Prognoseabzug für Neukundenentwicklung, Abzinsung, Billigkeitskorrektur sowie Höchstbetragsgrenze einer durchschnittlichen Jahresvergütung nach § 89b Abs. 2 HGB und richtlinienkonformer EuGH-Recht..._

# Berechnung des Ausgleichsanspruchs nach § 89b HGB

## Arbeitsbereich

Berechnet den Ausgleichsanspruch nach § 89b HGB: Rohertragsberechnung auf Basis der Jahresprovision, Prognoseabzug für Neukundenentwicklung, Abzinsung, Billigkeitskorrektur sowie Höchstbetragsgrenze einer durchschnittlichen Jahresvergütung nach § 89b Abs. 2 HGB und richtlinienkonformer EuGH-Rechtsprechung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Berechnung des Ausgleichsanspruchs nach § 89b HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie einschlägige BGH- und EuGH-Rechtsprechung ein.
Der Skill zielt auf konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X beendet nach 12 Jahren das Vertreterverhältnis mit Unternehmer Y; X berechnet seinen Ausgleichsanspruch auf Basis der Neukundenprovision der letzten fünf Jahre.
- Unternehmer Y bestreitet die Höhe des Ausgleichs und beauftragt eine Gegenkalkulation unter Berücksichtigung von Kundenabwanderungen und Prognoseabzügen.
- Handelsvertreterin Z ermittelt den Höchstbetrag nach § 89b Abs. 2 HGB als Kappungsgrenze und vergleicht ihn mit der Rohertragsmethode.

## Erste Schritte

1. Jahresprovision der letzten fünf Vertragsjahre aus Abrechnungen ermitteln.
2. Neukundenanteil und wesentlich erweiterter Altkundenanteil herausrechnen.
3. Prognoseabzug für zukünftige Kundenabwanderung schätzen und dokumentieren.
4. Abzinsung des zukünftigen Vorteils für den Unternehmer berechnen.
5. Höchstbetrag nach § 89b Abs. 2 HGB (durchschnittliche Jahresvergütung der letzten fünf Jahre) bestimmen.
6. Billigkeitskorrektur nach § 89b Abs. 1 S. 1 HGB prüfen — Unbilligkeit senkt den Anspruch.

## Rechtsrahmen

- § 89b Abs. 1 HGB — Entstehungsvoraussetzungen und Billigkeit
- § 89b Abs. 2 HGB — Höchstbetrag eine durchschnittliche Jahresvergütung
- § 89b Abs. 3 HGB — Ausschlussgründe
- § 89b Abs. 4 HGB — Anmeldefrist ein Jahr nach Vertragsende
- Art. 17 Abs. 2 RL 86/653/EWG — Berechnungsrahmen des Ausgleichs
- EuGH C-381/19 — Saint-Gobain: Billigkeit bei der Berechnung

## Prüfraster

- Welche Provisionen entfallen auf Neukunden oder wesentliche Erweiterung bestehender Kunden?
- Welcher Prognoseabzug ist für Kundenabwanderung nach Vertragsende sachgerecht?
- Übersteigt der berechnete Rohausgleich den Höchstbetrag nach § 89b Abs. 2 HGB?
- Erfordert die Billigkeit eine Korrektur des errechneten Betrags nach oben oder unten?
- Ist die Ausgleichsanmeldung fristgerecht innerhalb eines Jahres erfolgt?
- Gibt es Ausschlussgründe nach § 89b Abs. 3 HGB, die den Anspruch zum Erlöschen bringen?

## Typische Fallstricke

- Neukundenprovision nicht sauber vom Stammkundenumsatz getrennt — fehlerhafte Berechnungsgrundlage.
- Höchstbetrag nach § 89b Abs. 2 HGB übersehen — Anspruch wird zu hoch angesetzt.
- Prognoseabzug zu pauschal geschätzt — gerichtlich angreifbar.
- Anmeldefrist nach § 89b Abs. 4 S. 2 HGB versäumt — Anspruch erlischt.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien sind: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Praktisch relevant sind insbesondere: Provisionsabrechnungen und Buchauszug (§ 87c HGB),
nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Ausgleichsanspruch (§ 89b HGB).
Zwingende Vorschriften zum Schutz des Handelsvertreters nach § 92c HGB können vertraglich
nicht abgebedungen werden; entgegenstehende Klauseln sind nach § 134 BGB nichtig.

## Quellen

- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [Art. 17 RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [EuGH C-381/19 Saint-Gobain auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A62019CJ0381)
- [Dejure § 89b HGB](https://dejure.org/gesetze/HGB/89b.html)
- [BGH Rechtsprechung Openjur](https://openjur.de/)

---

## Skill: `ausgleichsanmeldung`

_Unterstützt bei fristgerechter Anmeldung des Ausgleichsanspruchs nach § 89b Abs. 4 HGB: Einhaltung der Jahresfrist ab Vertragsende, Inhalt und Form der Anmeldung, Wahrung gegenüber dem Unternehmer und Rechtsfolgen bei Fristversäumnis; Musterschreiben für Handelsvertreter und Unternehmerseite im H..._

# Anmeldung des Ausgleichsanspruchs nach § 89b Abs. 4 HGB

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Anmeldung des Ausgleichsanspruchs nach § 89b Abs. 4 HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel sind konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X hat das Vertreterverhältnis mit Unternehmer Y im März beendet; X prüft, bis wann er den Ausgleichsanspruch anmelden muss und was die Anmeldung enthalten soll.
- Unternehmer Y bestreitet den Ausgleich mit dem Argument, die Anmeldung sei nach Ablauf der Jahresfrist des § 89b Abs. 4 HGB erfolgt.
- Handelsvertreter X meldet den Ausgleich vorsorglich an, bevor die genaue Höhe berechnet ist; er klärt, ob eine Anmeldung dem Grunde nach ausreicht.

## Erste Schritte

1. Datum der Vertragsbeendigung exakt bestimmen (Zeitpunkt der Kündigung oder Aufhebung).
2. Frist berechnen: ein Jahr ab Vertragsende nach § 89b Abs. 4 S. 2 HGB.
3. Anmeldungsschreiben dem Grunde nach formulieren; genaue Höhe muss noch nicht feststehen.
4. Anmeldung per Einschreiben mit Rückschein oder Boten mit Empfangsbestätigung übermitteln.
5. Fristablauf im Kalender notieren und Bestätigung des Erhalts anfordern.
6. Gleichzeitig Provisionsabrechnungen für Ausgleichsberechnung anfordern.

## Rechtsrahmen

- § 89b Abs. 4 S. 2 HGB — Jahresfrist für die Anmeldung des Ausgleichs
- § 89b Abs. 1 HGB — Entstehungsvoraussetzungen des Ausgleichsanspruchs
- § 89b Abs. 2 HGB — Höchstbetrag des Ausgleichs
- § 130 BGB — Wirksamkeit einer empfangsbedürftigen Willenserklärung
- § 193 BGB — Fristverlängerung bei Fristende an Sonn- oder Feiertag
- Art. 17 RL 86/653/EWG — Ausgleichsanspruch nach Vertragsende

## Prüfraster

- Wann endete der Handelsvertretervertrag genau?
- Ist die Jahresfrist nach § 89b Abs. 4 S. 2 HGB noch nicht abgelaufen?
- Enthält die Anmeldung zumindest den Anspruch dem Grunde nach?
- Ist die Anmeldung dem Unternehmer oder seinen Bevollmächtigten zugegangen?
- Wurde der Zugang der Anmeldung dokumentiert (Einschreiben, Empfangsbestätigung)?
- Greift eine Verlängerung nach § 193 BGB, weil der Jahrestag auf einen Feiertag fällt?

## Typische Fallstricke

- Jahresfrist verpasst — der Ausgleichsanspruch erlischt unwiederbringlich.
- Anmeldung nur mündlich erklärt — Nachweis des Zugangs fehlt.
- Falscher Adressat: Anmeldung geht an Niederlassung statt an Hauptsitz des Unternehmers.
- Fristbeginn falsch berechnet: Nicht Kündigungsdatum, sondern Datum der Vertragsbeendigung ist maßgeblich.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Zwingende Vorschriften nach § 92c HGB können vertraglich nicht abgebedungen werden;
entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) sowie Kündigung (§§ 89, 89a HGB).

## Quellen

- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [§ 130 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__130.html)
- [§ 193 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__193.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 89b HGB](https://dejure.org/gesetze/HGB/89b.html)

---

## Skill: `ausgleichsanspruch-89b`

_Analysiert den Ausgleichsanspruch des Handelsvertreters nach § 89b HGB vollständig: Entstehungsvoraussetzungen (neue Kunden, wesentliche Erweiterung), Höchstbetrag von einer Jahresprovision, Ausschlussgründe nach § 89b Abs. 3 HGB, Berechnung nach der BGH-Stufenmethode sowie Anmeldefrist nach § 89..._

# Ausgleichsanspruch nach § 89b HGB — Entstehung, Berechnung und Durchsetzung

## Arbeitsbereich

Analysiert den Ausgleichsanspruch des Handelsvertreters nach § 89b HGB vollständig: Entstehungsvoraussetzungen (neue Kunden, wesentliche Erweiterung), Höchstbetrag von einer Jahresprovision, Ausschlussgründe nach § 89b Abs. 3 HGB, Berechnung nach der BGH-Stufenmethode sowie Anmeldefrist nach § 89b Abs. 4 HGB. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Ausgleichsanspruch nach § 89b HGB — Entstehung, Berechnung und Durchsetzung.
Er deckt HGB §§ 84–92c und die EU-Handelsvertreterrichtlinie 86/653/EWG ab.
Ziel: konkrete, umsetzbare Ergebnisse für Handelsvertreter und Unternehmer.
Zwingende Normen (§ 92c HGB) schützen den Handelsvertreter auch bei ausländischer Rechtswahl.
BGH und EuGH haben zentrale Rechtsfragen durch Leitentscheidungen geprägt.

## Mandantenfall

- Handelsvertreter X hat nach fünfjähriger Tätigkeit einen großen Kundenstamm aufgebaut; nach Kündigung durch Unternehmer Y fragt X, wie hoch sein Ausgleich nach § 89b HGB ist.
- Unternehmer Y behauptet, der Ausgleichsanspruch des Handelsvertreters X sei nach § 89b Abs. 3 HGB ausgeschlossen, weil X selbst gekündigt habe; X prüft, ob ein Ausnahmetatbestand greift.
- Anwältin A berechnet den Ausgleich für Handelsvertreter X nach der BGH-Stufenmethode und möchte wissen, welche Provisionsdaten sie für die Berechnung benötigt.

## Erste Schritte

1. Ausgleichsvoraussetzungen nach § 89b Abs. 1 HGB prüfen: neue Kunden, wesentliche Erweiterung.
2. Unternehmervorteile nach Vertragsende als Ausgleichsgrundlage feststellen.
3. Höchstbetrag nach § 89b Abs. 2 HGB: durchschnittliche Jahresprovision der letzten fünf Jahre.
4. Ausschlussgründe nach § 89b Abs. 3 HGB: eigene Kündigung ohne wichtigen Grund, schwere Pflichtverletzung.
5. Anmeldung des Ausgleichs innerhalb eines Jahres nach Vertragsende nach § 89b Abs. 4 HGB.
6. BGH-Stufenmethode anwenden: Rohausgleich, Abwanderungsquote, Billigkeitskorrekturen.

## Rechtsrahmen

- § 89b Abs. 1 HGB — Voraussetzungen: neue Kunden und wesentliche Erweiterung
- § 89b Abs. 2 HGB — Höchstbetrag: eine durchschnittliche Jahresprovision
- § 89b Abs. 3 HGB — Ausschlussgründe: eigene Kündigung ohne wichtigen Grund
- § 89b Abs. 4 HGB — Ausschlussfrist: Anmeldung innerhalb eines Jahres
- Art. 17 RL 86/653/EWG — Europäischer Mindeststandard für den Ausgleich
- § 92c HGB — Ausgleich ist zwingend: vorherige Einschränkung unwirksam

## Prüfraster

- Liegen neue Kunden oder wesentliche Geschäftserweiterung als Ausgleichsvoraussetzung vor?
- Hat der Unternehmer nach Vertragsende nachhaltige Vorteile aus dem Kundenstamm?
- Greift ein Ausschlussgrund nach § 89b Abs. 3 HGB (eigene Kündigung ohne wichtigen Grund)?
- Ist die Anmeldefrist von einem Jahr nach § 89b Abs. 4 HGB gewahrt?
- Überschreitet der Rohausgleich den Höchstbetrag von einer Jahresprovision?
- Sind Billigkeitskorrekturen nach § 89b Abs. 1 S. 1 HGB vorzunehmen?

## Typische Fallstricke

- Ausschlussfrist nach § 89b Abs. 4 HGB versäumt — Anspruch erloschen.
- Eigene Kündigung ohne wichtigen Grund — Ausschlussgrund nach § 89b Abs. 3 HGB.
- Rohausgleich über Höchstbetrag berechnet — Korrektur nach § 89b Abs. 2 HGB vergessen.
- Neue Kunden nicht dokumentiert — Ausgleichsgrundlage nicht nachweisbar.

## Hintergrund und Kontext

Das Handelsvertreterrecht steht im fünften Buch des HGB (§§ 84 bis 92c).
Es gilt als Sonderprivatrecht zwischen Arbeits- und allgemeinem Handelsrecht.
Die EU-Handelsvertreterrichtlinie 86/653/EWG setzt europäische Mindeststandards.
Kernprinzipien: Selbständigkeit, Provisionsanspruch, Buchauszug, Ausgleich bei Vertragsende.
Nachvertragliches Wettbewerbsverbot (§ 90a HGB) und Delkredere (§ 86b HGB) regeln Sonderlagen.
Zwingende Vorschriften nach § 92c HGB schützen den Handelsvertreter.
Entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Für grenzüberschreitende Sachverhalte bestimmt die Rom-I-Verordnung das anwendbare Recht.
Zwingende Normen wie Ausgleich (§ 89b HGB) und Buchauszug (§ 87c HGB) stehen nicht zur Disposition.
Bei Statusfragen (Selbständigkeit) ist das Statusfeststellungsverfahren nach § 7a SGB IV maßgeblich.

## Quellen

- [§ 89b HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__89b.html)
- [§ 92c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__92c.html)
- [Art. 17 RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [BGH-Entscheidungen auf bgh.de](https://www.bgh.de/entscheidungen/entscheidungen-online)
- [Dejure § 89b HGB](https://dejure.org/gesetze/HGB/89b.html)

---

## Skill: `auskunft-einsicht-auslaendischer-principal`

_Unterstützt Handelsvertreter bei Auskunfts- und Einsichtsrechten nach § 87c Abs. 2 HGB und § 242 BGB: Umfang des Buchauszugsanspruchs, Einsicht in Geschäftsbücher, Durchsetzung bei Verweigerung durch den Unternehmer sowie Stufenklage auf Auskunft und Leistung nach § 254 ZPO im Handelsvertreterrecht._

# Auskunfts- und Einsichtsrechte des Handelsvertreters nach § 87c HGB

## Arbeitsbereich

Unterstützt Handelsvertreter bei Auskunfts- und Einsichtsrechten nach § 87c Abs. 2 HGB und § 242 BGB: Umfang des Buchauszugsanspruchs, Einsicht in Geschäftsbücher, Durchsetzung bei Verweigerung durch den Unternehmer sowie Stufenklage auf Auskunft und Leistung nach § 254 ZPO. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Auskunfts- und Einsichtsrechte des Handelsvertreters nach § 87c HGB.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel sind konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X verlangt Einsicht in die Kundenabrechnungen des Unternehmers Y, um die Vollständigkeit seiner Provisionen zu prüfen; Y verweigert dies.
- Unternehmer Y bestreitet, dass X ein Recht auf Einsicht in Vertragsunterlagen hat, die über den Buchauszug nach § 87c HGB hinausgehen.
- Handelsvertreter X erhebt Stufenklage: er klagt zunächst auf Buchauszug, dann auf Abrechnung und schließlich auf Zahlung der ermittelten Provision.

## Erste Schritte

1. Buchauszugsanspruch nach § 87c Abs. 2 HGB formal geltend machen.
2. Ergänzenden Auskunftsanspruch nach § 242 BGB (Treu und Glauben) prüfen.
3. Umfang klären: Kunden, Zeitraum, Umsätze, Rabatte, Stornos, Direktgeschäfte.
4. Stufenklage nach § 254 ZPO vorbereiten: Buchauszug, Abrechnung, Zahlung.
5. Einstweiligen Rechtsschutz bei dringendem Bedarf prüfen.
6. Verjährungsfristen für Provisionsansprüche parallel überwachen.

## Rechtsrahmen

- § 87c Abs. 2 HGB — Buchauszugsanspruch des Handelsvertreters
- § 87c Abs. 3 HGB — Recht auf Einsicht in Bücher und Belege
- § 242 BGB — Auskunftsanspruch nach Treu und Glauben
- § 254 ZPO — Stufenklage
- § 259 BGB — Pflicht zur Rechnungslegung
- Art. 12 RL 86/653/EWG — Provisionsabrechnungspflicht

## Prüfraster

- Ist der Buchauszugsanspruch nach § 87c Abs. 2 HGB formal geltend gemacht?
- Umfasst der Anspruch auch Direktgeschäfte des Unternehmers im Bezirk des Vertreters?
- Besteht ein weitergehender Einsichtsanspruch nach § 87c Abs. 3 HGB oder § 242 BGB?
- Ist eine Stufenklage nach § 254 ZPO die geeignete Klageart?
- Wurden Fristen für Provisionsansprüche durch die Auskunftsstufe gewahrt?
- Liegt eine Pflichtverletzung des Unternehmers durch Verweigerung der Auskunft vor?

## Typische Fallstricke

- Auskunftsanspruch zu eng auf Buchauszug beschränkt — Einsichtsrecht nach § 87c Abs. 3 HGB nicht ausgeschöpft.
- Stufenklage ohne klare Bezifferung der Leistungsstufe erhoben — Klage unzulässig.
- Verjährung der Provisionsansprüche während des Auskunftsstreits eingetreten.
- Direktgeschäfte des Unternehmers nicht in den Auskunftsantrag einbezogen.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Zwingende Vorschriften nach § 92c HGB können vertraglich nicht abgebedungen werden;
entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) sowie Kündigung (§§ 89, 89a HGB).

## Quellen

- [§ 87c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87c.html)
- [§ 242 BGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/bgb/__242.html)
- [§ 254 ZPO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/__254.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [Dejure § 87c HGB](https://dejure.org/gesetze/HGB/87c.html)

---

## Skill: `auslaendischer-principal`

_Analysiert Handelsvertreterverträge mit ausländischem Unternehmer: anwendbares Recht nach Rom-I-VO, zwingende Schutzvorschriften nach § 92c HGB und Art. 17 ff. RL 86/653/EWG auch bei Rechtswahl, Gerichtsstandsvereinbarungen sowie Anerkennung ausländischer Urteile und Schiedssprüche im Handelsvert..._

# Handelsvertretervertrag mit ausländischem Unternehmer — Internationales Privatrecht

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Handelsvertretervertrag mit ausländischem Unternehmer — Internationales Privatrecht.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel sind konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X mit Sitz in Deutschland vertritt einen US-amerikanischen Unternehmer Y; nach Vertragsende streitet X um den Ausgleichsanspruch und fragt, ob deutsches Recht gilt.
- Unternehmer Y (Frankreich) hat im Vertrag englisches Recht und London-Schiedsklausel vereinbart; Handelsvertreter X prüft, ob zwingende deutsche Schutzvorschriften trotzdem gelten.
- Handelsvertreter X will ein britisches Urteil gegen ausländischen Unternehmer Y in Deutschland vollstrecken lassen.

## Erste Schritte

1. Rechtswahl im Vertrag prüfen: welches Recht ist vereinbart?
2. Anwendbares Recht nach Art. 3 und 4 Rom-I-VO bestimmen.
3. Zwingende Schutzvorschriften des Staates des gewöhnlichen Aufenthalts des Handelsvertreters nach Art. 9 Rom-I-VO prüfen.
4. EU-Richtlinien-Schutz: Art. 17 ff. RL 86/653/EWG gilt in allen EU-Mitgliedstaaten.
5. Gerichtsstand nach EuGVVO bestimmen; Schiedsklausel auf Wirksamkeit prüfen.
6. Vollstreckung ausländischer Urteile nach EuGVVO oder bilateralen Abkommen klären.

## Rechtsrahmen

- Art. 3 und 4 Rom-I-VO — Rechtswahl und anwendbares Recht ohne Rechtswahl
- Art. 9 Rom-I-VO — Eingriffsnormen des Forumstaats
- § 92c HGB — Zwingende Vorschriften auch bei ausländischem Recht
- Art. 17 ff. RL 86/653/EWG — Mindeststandards für alle EU-Staaten
- Art. 25 EuGVVO — Gerichtsstandsvereinbarungen
- § 328 ZPO — Anerkennung ausländischer Urteile

## Prüfraster

- Welches Recht gilt nach Rechtswahl oder Art. 4 Rom-I-VO?
- Sind zwingende deutsche Schutzvorschriften als Eingriffsnormen nach Art. 9 Rom-I-VO anwendbar?
- Gilt die RL 86/653/EWG, weil der Handelsvertreter in einem EU-Mitgliedstaat tätig ist?
- Ist die Gerichtsstandsklausel wirksam und welches Gericht ist zuständig?
- Kann ein ausländisches Urteil in Deutschland vollstreckt werden?
- Sind Schiedsklauseln wirksam und nach welchem Recht wird das Schiedsgericht entscheiden?

## Typische Fallstricke

- Rechtswahl schließt zwingende deutsche Normen nicht aus — § 92c HGB und Art. 9 Rom-I-VO beachten.
- Ausländisches Recht kennt keinen Ausgleichsanspruch — trotzdem anwendbar, wenn RL 86/653/EWG gilt.
- Vollstreckung in Drittstaaten (USA, Schweiz) ohne bilaterales Anerkennungsabkommen schwierig.
- Gerichtsstandsklausel für Verbraucher oder arbeitnehmerähnliche Personen unter Umständen unwirksam.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Zwingende Vorschriften nach § 92c HGB können vertraglich nicht abgebedungen werden;
entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) sowie Kündigung (§§ 89, 89a HGB).

## Quellen

- [Rom-I-VO auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32008R0593)
- [§ 92c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__92c.html)
- [RL 86/653/EWG auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A31986L0653)
- [EuGVVO auf EUR-Lex](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX%3A32012R1215)
- [Dejure § 92c HGB](https://dejure.org/gesetze/HGB/92c.html)

---

## Skill: `beweis-sicherung`

_Unterstützt Handelsvertreter und Unternehmer bei der Beweissicherung für Provisionsstreitigkeiten: Sicherung von Verträgen, Abrechnungen, E-Mails, CRM-Daten und Kundenkorrespondenz; selbständiges Beweisverfahren nach §§ 485 ff. ZPO; digitale Beweismittel und deren Verwertbarkeit vor Gericht im Ha..._

# Beweissicherung im Handelsvertreterstreit nach §§ 485 ff. ZPO

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 84-92c, EuGH zu Ausgleichsanspruch, BGB §§ 305 ff.; § 89b, Wettbewerbsverbot; § 90a und Vertriebsmodelle — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Überblick

Unterstützt bei rechtlichen Fragen rund um Beweissicherung im Handelsvertreterstreit nach §§ 485 ff. ZPO.
Er deckt die wichtigsten Normen des deutschen Handelsvertreterrechts nach HGB §§ 84–92c ab
und bezieht die EU-Handelsvertreterrichtlinie 86/653/EWG sowie BGH- und EuGH-Rechtsprechung ein.
Ziel sind konkrete, umsetzbare Ergebnisse: Schriftsätze, Berechnungen, Vertragsentwürfe und Prüfvermerke.
Sowohl die Handelsvertreter- als auch die Unternehmerseite werden abgedeckt.

## Mandantenfall

- Handelsvertreter X ahnt, dass Unternehmer Y Unterlagen vernichten wird; X beantragt ein selbständiges Beweisverfahren nach § 485 ZPO zur Sicherung von Buchauszug und Abrechnungen.
- Unternehmer Y will beweisen, dass der Handelsvertreter X Kunden abgeworben hat; Y sichert E-Mails und CRM-Daten als Beweismittel.
- Handelsvertreter X hat Sprachnachrichten und WhatsApp-Verläufe mit Unternehmer Y; er fragt, ob diese als Beweismittel vor Gericht verwertbar sind.

## Erste Schritte

1. Relevante Beweismittel identifizieren: Verträge, Abrechnungen, E-Mails, CRM-Daten, Protokolle.
2. Beweismittel sofort sichern: Ausdrucke, Screenshots mit Zeitstempel, Metadaten.
3. Selbständiges Beweisverfahren nach § 485 ZPO prüfen bei Gefahr der Vernichtung.
4. Digitale Beweismittel auf Authentizität und Manipulationsfreiheit prüfen.
5. Zeugen benennen und Zeugenerklärungen vorbereiten.
6. Beweislastverteilung in der konkreten Streitigkeit analysieren.

## Rechtsrahmen

- §§ 485–494a ZPO — Selbständiges Beweisverfahren
- § 286 ZPO — Freie Beweiswürdigung
- § 371 ZPO — Augenscheinsbeweis bei Dateien und digitalen Daten
- § 416 ZPO — Privaturkunden als Beweismittel
- § 87c Abs. 2 HGB — Buchauszugsanspruch als Informationsgrundlage
- § 823 Abs. 2 BGB — Schadensersatz bei unbefugtem Zugriff auf Beweismittel

## Prüfraster

- Welche Beweismittel sind für die Streitigkeit entscheidend?
- Besteht Vernichtungsgefahr, die ein selbständiges Beweisverfahren rechtfertigt?
- Sind digitale Beweismittel authentifizierbar und gerichtsverwertbar?
- Wer trägt die Beweislast — Handelsvertreter oder Unternehmer?
- Sind WhatsApp- oder E-Mail-Verläufe datenschutzkonform als Beweismittel einzuführen?
- Wurden Beweismittel rechtzeitig gesichert oder droht Beweisvereitelung?

## Typische Fallstricke

- Digitale Beweise ohne Metadaten gesichert — Authentizität angreifbar.
- Selbständiges Beweisverfahren zu spät beantragt — Unterlagen bereits vernichtet.
- Datenschutzrechtliche Verwertungsverbote bei heimlich aufgezeichneten Gesprächen.
- Beweislastumkehr bei Beweisvereitelung durch Unternehmer nicht ausgenutzt.

## Hintergrund und Kontext

Das deutsche Handelsvertreterrecht ist im fünften Buch des HGB in den §§ 84 bis 92c geregelt.
Es setzt die EU-Handelsvertreterrichtlinie 86/653/EWG in nationales Recht um.
Kernprinzipien: Selbständigkeit des Handelsvertreters, Provisionsanspruch, Informationsrechte,
Ausgleichsanspruch bei Vertragsende sowie Schutz vor einseitiger Benachteiligung.
BGH und EuGH haben das Handelsvertreterrecht durch zahlreiche Entscheidungen geprägt,
insbesondere zur Berechnung des Ausgleichs, zur Richtlinienkonformität und zu Ausschlussgründen.
Zwingende Vorschriften nach § 92c HGB können vertraglich nicht abgebedungen werden;
entgegenstehende Klauseln sind nach § 134 BGB nichtig.
Praktisch zentral: Provision (§ 87 HGB), Buchauszug (§ 87c HGB), Ausgleich (§ 89b HGB),
Wettbewerbsverbot (§ 90a HGB) sowie Kündigung (§§ 89, 89a HGB).

## Quellen

- [§ 485 ZPO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/__485.html)
- [§ 286 ZPO auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/zpo/__286.html)
- [§ 87c HGB auf gesetze-im-internet.de](https://www.gesetze-im-internet.de/hgb/__87c.html)
- [Dejure § 485 ZPO](https://dejure.org/gesetze/ZPO/485.html)
- [Dejure § 87c HGB](https://dejure.org/gesetze/HGB/87c.html)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

