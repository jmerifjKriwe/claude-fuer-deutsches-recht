---
name: forderungsmanagement-klagewerkstatt-forderung-mietruckstand
description: "Forderung Mietruckstand im Plugin Forderungsmanagement Klagewerkstatt: prüft konkret Mietrueckstand, Forderung gegen Verbraucher, Zwangsvollstreckung Ueberblick. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Forderung Mietruckstand

## Arbeitsbereich

**Forderung Mietruckstand** ordnet den Fall über die tragenden Prüffelder: Mietrueckstand, Forderung gegen Verbraucher, Zwangsvollstreckung Ueberblick. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `forderung-mietruckstand-zahlungsklage` | Mietrueckstand: Zahlungsklage parallel zu Raumungsklage § 543 BGB. Pflicht Mahnung? In der Regel nicht erforderlich (kalendermaessig bestimmt). Schonfristregelung § 569 Abs. 3 BGB. Output: Klageschrift Zahlungsklage + Raumungsklage. |
| `forderung-verbraucher-erleichterungen` | Forderung gegen Verbraucher: Verbraucherschutzregeln, AGB-Kontrolle §§ 305 ff. BGB, Belehrungspflichten Verzugskosten § 288 Abs. 4 BGB, Kostenausschluss § 91 ZPO bei Bagatellsachen. Pruefraster. |
| `forderung-zwangsvollstreckung-ueberblick` | Zwangsvollstreckung Ueberblick: Mobiliarvollstreckung Gerichtsvollzieher §§ 808 ff. ZPO, Forderungspfaendung § 829 ZPO, Lohnpfaendung mit Pfaendungstabelle, Immobiliarvollstreckung Zwangshypothek/Versteigerung. Output: Strategiememo Vollstreckung. |

## Arbeitsweg

- Rolle und Ziel im Forderungsmanagement Klagewerkstatt klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `forderung-mietruckstand-zahlungsklage`

**Fokus:** Mietrueckstand: Zahlungsklage parallel zu Raumungsklage § 543 BGB. Pflicht Mahnung? In der Regel nicht erforderlich (kalendermaessig bestimmt). Schonfristregelung § 569 Abs. 3 BGB. Output: Klageschrift Zahlungsklage + Raumungsklage.

# Mietrueckstands-Klage

## Fachkern: Mietrueckstands-Klage
- **Spezialgegenstand:** Mietrueckstands-Klage wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
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

## 2. `forderung-verbraucher-erleichterungen`

**Fokus:** Forderung gegen Verbraucher: Verbraucherschutzregeln, AGB-Kontrolle §§ 305 ff. BGB, Belehrungspflichten Verzugskosten § 288 Abs. 4 BGB, Kostenausschluss § 91 ZPO bei Bagatellsachen. Pruefraster.

# Forderung gegen Verbraucher

## Fachkern: Forderung gegen Verbraucher
- **Spezialgegenstand:** Forderung gegen Verbraucher wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
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

## 3. `forderung-zwangsvollstreckung-ueberblick`

**Fokus:** Zwangsvollstreckung Ueberblick: Mobiliarvollstreckung Gerichtsvollzieher §§ 808 ff. ZPO, Forderungspfaendung § 829 ZPO, Lohnpfaendung mit Pfaendungstabelle, Immobiliarvollstreckung Zwangshypothek/Versteigerung. Output: Strategiememo Vollstreckung.

# Zwangsvollstreckung Ueberblick

## Fachkern: Zwangsvollstreckung Ueberblick
- **Spezialgegenstand:** Zwangsvollstreckung Ueberblick wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB Anspruch/Fälligkeit/Verzug, ZPO Mahn-/Klageverfahren, HGB kaufmännische Belege, Inkassorecht, Verjährung und Zuständigkeit.
- **Entscheidende Weiche:** Nur klare, fällige, beweisbare Forderungen weitergeben; Vertrag, Leistung, Rechnung, Mahnung, Einwendungen, Verjährung und Kosten getrennt prüfen.
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
