---
name: versr-pkv-beitragsanpassung-rechtsschutz
description: "Versr Pkv Beitragsanpassung Medizinische Notwendigkeit, Versr Rechtsschutz Deckungsklage Spezial, Versr Regress Subrogation 86 Vvg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Versr Pkv Beitragsanpassung Medizinische Notwendigkeit, Versr Rechtsschutz Deckungsklage Spezial, Versr Regress Subrogation 86 Vvg

## Arbeitsbereich

In diesem Skill wird **Versr Pkv Beitragsanpassung Medizinische Notwendigkeit, Versr Rechtsschutz Deckungsklage Spezial, Versr Regress Subrogation 86 Vvg** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `versr-pkv-beitragsanpassung-medizinische-notwendigkeit` | PKV-Mandate zu Beitragsanpassung § 203 VVG, medizinischer Notwendigkeit, GOÄ/GOZ-Kürzung, Tarifwechsel und Rückforderung. |
| `versr-rechtsschutz-deckungsklage-spezial` | Spezialfall Rechtsschutzversicherungs-Deckungsklage: Wartezeit, Vorvertraglichkeit (BGH IV ZR), Stichentscheid, Streitwert in Deckungsklage. Schiedsverfahren bei Streit ueber Erfolgsaussicht. Pruefraster. |
| `versr-regress-subrogation-86-vvg` | Regress, Legalzession, Quotenvorrecht, Sozialversicherungsträgerregress und Regressabwehr nach Regulierung. |

## Arbeitsweg

Für **Versr Pkv Beitragsanpassung Medizinische Notwendigkeit, Versr Rechtsschutz Deckungsklage Spezial, Versr Regress Subrogation 86 Vvg** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `fachanwalt-versicherungsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `versr-pkv-beitragsanpassung-medizinische-notwendigkeit`

**Fokus:** PKV-Mandate zu Beitragsanpassung § 203 VVG, medizinischer Notwendigkeit, GOÄ/GOZ-Kürzung, Tarifwechsel und Rückforderung.

# FA Versicherungsrecht: PKV Beitrag und Leistung

## Einsatz

Für Versicherte, die PKV-Erhöhungen oder Leistungskürzungen angreifen.

## Norm- und Quellenanker

VVG §§ 192–208, § 203; MB/KK; GOÄ/GOZ; VAG.

## Arbeitsfragen

1. Welche Schreiben und Anpassungen liegen vor?
2. Geht es um Form/Begründung oder medizinische Notwendigkeit?
3. Welche Verjährung und Wirtschaftlichkeit?

## Output

PKV-Prüfmatrix, Auskunftsschreiben und Anspruchsberechnung.

## Red Flags

- Treuhänderfrage isoliert überschätzt
- Rechnung ohne Tarifprüfung
- Verjährung vergessen

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

## 2. `versr-rechtsschutz-deckungsklage-spezial`

**Fokus:** Spezialfall Rechtsschutzversicherungs-Deckungsklage: Wartezeit, Vorvertraglichkeit (BGH IV ZR), Stichentscheid, Streitwert in Deckungsklage. Schiedsverfahren bei Streit ueber Erfolgsaussicht. Pruefraster.

# Versr: Rechtsschutz-Deckung

## Spezialwissen: Versr: Rechtsschutz-Deckung
- **Spezialgegenstand:** Versr: Rechtsschutz-Deckung / versr rechtsschutz deckungsklage spezial. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** BGH, IV, ZR.
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

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `versr-regress-subrogation-86-vvg`

**Fokus:** Regress, Legalzession, Quotenvorrecht, Sozialversicherungsträgerregress und Regressabwehr nach Regulierung.

# FA Versicherungsrecht: Regress § 86 VVG

## Einsatz

Für Mandate nach Zahlung eines Versicherers oder Sozialversicherungsträgers.

## Norm- und Quellenanker

- VVG § 86 für Übergang von Ersatzansprüchen auf den Versicherer und Schutz des Versicherungsnehmers.
- SGB X § 116 für Sozialversicherungsträgerregress; Quotenvorrecht und Kongruenz besonders prüfen.
- BGB §§ 249 ff., 426, 823 ff. je nach Haftungsgrund; ZPO für Streitverkündung, Klage und Beweis.
- Verjährung nach übergegangenem Anspruch, Kenntnislage und Hemmung gesondert bestimmen; keine pauschale Drei-Jahres-Schablone.

## Arbeitsfragen

1. Welche Forderung ist übergegangen?
2. Welche Eigenansprüche bleiben?
3. Welche Verjährung/Rechtsverfolgung?
4. Sind Schadenpositionen kongruent: Sachschaden, Personenschaden, Verdienstausfall, Heilbehandlung, Pflege, Haushaltsführung?
5. Hat ein Vergleich, Abfindung, Erlass oder Anerkenntnis den Regress beeinträchtigt?
6. Besteht ein Familien-/Haushaltsprivileg oder arbeitsrechtliches Haftungsprivileg?

## Output

Regressmatrix, Vergleichsklauseln und Verjährungskalender.

## Red Flags

- Quotenvorrecht vergessen
- Vergleich zerstört Regress
- Forderungsübergang ungeprüft

## Arbeitsstil

Konkrete Normen, konkrete Unterlagen, konkrete nächste Handlung. Keine pauschalen Empfehlungen; Rechtsprechung nur verifiziert mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.
