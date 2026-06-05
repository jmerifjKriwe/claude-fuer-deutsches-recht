---
name: immo-bauvertrag-vob-kaufvertrag-grundstueck
description: "Nutze dies, wenn Immo Bauvertrag Vob B, Immo Kaufvertrag Grundstueck, Immo Mietkaufvertrag im Plugin Immobilienrechtspraxis konkret bearbeitet werden soll. Auslöser: Bitte Immo Bauvertrag Vob B, Immo Kaufvertrag Grundstueck, Immo Mietkaufvertrag prüfen.; Erstelle eine Arbeitsfassung zu Immo Bauvertrag Vob B, Immo Kaufvertrag Grundstueck, Immo Mietkaufvertrag.; Welche Normen und Nachweise brauche ich?."
---

# Immo Bauvertrag Vob B, Immo Kaufvertrag Grundstueck, Immo Mietkaufvertrag

## Zweck

Dieser Skill ist ein eigenständiger Arbeitsbereich. Er verbindet mehrere sachlich benachbarte Arbeitsmodule. Wähle anhand des Sachverhalts das passende Modul, arbeite dessen Prüfroutine vollständig ab und kombiniere Module nur, wenn der Fall tatsächlich mehrere Themen berührt.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `immo-bauvertrag-vob-b` | Bauvertrag nach VOB-B oder BGB §§ 650a ff. BGB: Wahl Recht, Abnahme, Maengelrechte, Sicherheiten, Vergutung Stundenlohnarbeiten, Nachtraege. Pruefraster fuer beide Vertragstypen. |
| `immo-kaufvertrag-grundstueck` | Grundstueckskaufvertrag pruefen: § 311b BGB notarielle Beurkundung, Auflassung § 925 BGB, Eintragung Auflassungsvormerkung § 883 BGB, Kaufpreiszahlung, Vollzugspflichten, Sicherheiten. Pruefraster. |
| `immo-mietkaufvertrag` | Mietkaufvertrag: Aufbau, Steuerrecht, Kostenfallen, Reform 2025 (falls relevant). Pruefraster Vor- und Nachteile vs. klassischem Kaufvertrag. |

## Arbeitsweg

Für **Immo Bauvertrag Vob B, Immo Kaufvertrag Grundstueck, Immo Mietkaufvertrag** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `immobilienrechtspraxis` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `immo-bauvertrag-vob-b`

**Fokus:** Bauvertrag nach VOB-B oder BGB §§ 650a ff. BGB: Wahl Recht, Abnahme, Maengelrechte, Sicherheiten, Vergutung Stundenlohnarbeiten, Nachtraege. Pruefraster fuer beide Vertragstypen.

# Bauvertrag VOB-B / BGB

## Fachkern: Bauvertrag VOB-B / BGB
- **Spezialgegenstand:** Bauvertrag VOB-B / BGB wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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
Dieser Skill gehoert zum Plugin `immobilienrechtspraxis`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 2. `immo-kaufvertrag-grundstueck`

**Fokus:** Grundstueckskaufvertrag pruefen: § 311b BGB notarielle Beurkundung, Auflassung § 925 BGB, Eintragung Auflassungsvormerkung § 883 BGB, Kaufpreiszahlung, Vollzugspflichten, Sicherheiten. Pruefraster.

# Grundstueckskaufvertrag

## Fachkern: Grundstueckskaufvertrag
- **Spezialgegenstand:** Grundstueckskaufvertrag wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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
Dieser Skill gehoert zum Plugin `immobilienrechtspraxis`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.

## 3. `immo-mietkaufvertrag`

**Fokus:** Mietkaufvertrag: Aufbau, Steuerrecht, Kostenfallen, Reform 2025 (falls relevant). Pruefraster Vor- und Nachteile vs. klassischem Kaufvertrag.

# Mietkaufvertrag

## Fachkern: Mietkaufvertrag
- **Spezialgegenstand:** Mietkaufvertrag wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB, GBO, WEG, BauGB, ErbbauRG, MaBV, Mietrecht, Grundpfandrechte, Notar-/Registervollzug und öffentlich-rechtliche Lasten.
- **Entscheidende Weiche:** Trenne Eigentum, Besitz, Grundbuchabteilung, Belastung, Fälligkeit, Vollzug, Mängel, Miet-/Nutzungsverhältnis und Finanzierung.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


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
Dieser Skill gehoert zum Plugin `immobilienrechtspraxis`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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

## Was dieser Skill nicht macht
- Kein Ersatz fuer eine vollstaendige Mandantenberatung.
- Keine Festlegung des Mandanten ohne dessen ausdrueckliche Entscheidung.
- Keine Bewertung von Tatsachen, die nicht durch Unterlagen oder klare Mandantenangaben gedeckt sind.
- Bei erkennbaren Interessenkonflikten oder Berufsrechtsfragen Hinweis an den fallfuehrenden Anwalt.
