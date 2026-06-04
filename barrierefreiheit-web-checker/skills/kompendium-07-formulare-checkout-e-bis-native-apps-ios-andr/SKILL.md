---
name: kompendium-07-formulare-checkout-e-bis-native-apps-ios-andr
description: "barrierefreiheit-web-checker: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (formulare-checkout-ecommerce, kontrast-farbe-motion-responsive, native-apps-ios-android-pruefung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 07 - barrierefreiheit-web-checker

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `formulare-checkout-ecommerce` | Prüft Formulare, Login, Suche, Warenkorb, Checkout, Zahlungsstrecke und elektronische Verträge in Webshops. Fokus BFSG/E-Commerce, Fehlermeldungen, Labels, Pflichtfelder, Zeitlimits und Bestellabschluss. Output: Checkout-Audit. |
| `kontrast-farbe-motion-responsive` | Prüft Kontrast, Farbe ohne Farbcodierung, Zoom, Reflow, Textabstände, responsives Layout, Animationen, Motion-Reduction, Hover-Fallen und mobile Nutzung. Output: visuelle Barrierefreiheitsmatrix. |
| `native-apps-ios-android-pruefung` | Native Apps iOS und Android pruefen: Accessibility-API VoiceOver bzw. TalkBack, Plattform-spezifische Pattern, EN 301 549 Klausel 11. Tooling Xcode Accessibility Inspector, Android Accessibility Scanner. Konkrete Code-Beispiele Swift und Kotlin fuer haeufige Probleme. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `formulare-checkout-ecommerce`

**Frühere Beschreibung:** Prüft Formulare, Login, Suche, Warenkorb, Checkout, Zahlungsstrecke und elektronische Verträge in Webshops. Fokus BFSG/E-Commerce, Fehlermeldungen, Labels, Pflichtfelder, Zeitlimits und Bestellabschluss. Output: Checkout-Audit.

# Formulare, Checkout, E-Commerce

Nutze diesen Skill für Webshops, Buchungsstrecken, Login-Portale und digitale Vertragsabschlüsse.

## Prüfpfad

1. Produkt oder Dienstleistung finden.
2. In Warenkorb oder Buchungsstrecke legen.
3. Registrierung oder Gastbestellung.
4. Adresse, Versand, Zahlungsart.
5. Fehler provozieren.
6. Zusammenfassung prüfen.
7. Bestellung/Vertragsschluss und Bestätigung.

## Typische Fehler

- Pflichtfelder nur farblich markiert.
- Fehlermeldung erscheint, wird aber nicht fokussiert oder vorgelesen.
- Captcha ohne Alternative.
- Zahlungsanbieter ist nicht tastaturbedienbar.
- Zeitlimit löscht Warenkorb.
- AGB/Datenschutz-PDF ist nicht barrierefrei.
- Button-Beschriftung unklar: "Weiter" statt "Zahlungspflichtig bestellen" im richtigen Kontext.

## Output

| Schritt | Barriere | Rechts-/Nutzerrisiko | Fix |
| --- | --- | --- | --- |

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.

## Ausgabeformat

- Befund.
- Nutzerwirkung.
- Norm-/Kriteriumsbezug.
- Konkreter Fix.
- Prioritaet und Nachweis fuer die Dokumentation.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `kontrast-farbe-motion-responsive`

**Frühere Beschreibung:** Prüft Kontrast, Farbe ohne Farbcodierung, Zoom, Reflow, Textabstände, responsives Layout, Animationen, Motion-Reduction, Hover-Fallen und mobile Nutzung. Output: visuelle Barrierefreiheitsmatrix.

# Kontrast, Farbe, Motion, Responsive

Nutze diesen Skill für visuelle und responsive Barrierefreiheit.

## Prüffelder

- Text- und Komponenten-Kontrast.
- Informationen nicht nur durch Farbe.
- Zoom bis 200 Prozent ohne Funktionsverlust.
- Reflow bei schmaler Ansicht.
- Textabstände und Zeilenhöhen.
- Animationen, Parallax, Autoplay, blinkende Inhalte.
- prefers-reduced-motion respektieren.
- Touch-Zielgrößen und mobile Bedienbarkeit.

## Matrix

| Komponente | Problem | Nutzerwirkung | Fix |
| --- | --- | --- | --- |
| Button | Kontrast zu niedrig | nicht erkennbar | Farbe/Border anpassen |
| Fehlermeldung | nur rot | Farbwahrnehmung | Icon + Text |
| Slider | Autoplay | Bewegung/Bedienung | Pause/Stop + Motion |

## Priorität

Kontrast und Reflow sind oft schnell zu beheben und stark nutzerwirksam. Animationsprobleme werden gern unterschätzt, weil sie nur manche Nutzerinnen und Nutzer hart treffen.

## Schneller Arbeitsmodus

- Lege den Scope fest: Website, App, PDF, Checkout, Formular, Intranet oder öffentliche Stelle; dazu Normrahmen BFSG/BITV/WAD/EN 301 549/WCAG.
- Beurteile nicht nur formal, sondern aus Nutzersicht: Tastatur, Screenreader, Zoom/Reflow, Kontrast, Fehlermeldungen, Zeitlimits und Dokumentzugang.
- Automatische Scanner sind nur Startpunkt. Markiere False Positives, manuelle Nachpruefung und reproduzierbare Testschritte.
- Formuliere Fixes als Entwickler-Tickets mit Komponente, Problem, Nutzerwirkung, Normbezug, Prioritaet und Re-Test.

## Ausgabeformat

- Befund.
- Nutzerwirkung.
- Norm-/Kriteriumsbezug.
- Konkreter Fix.
- Prioritaet und Nachweis fuer die Dokumentation.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `native-apps-ios-android-pruefung`

**Frühere Beschreibung:** Native Apps iOS und Android pruefen: Accessibility-API VoiceOver bzw. TalkBack, Plattform-spezifische Pattern, EN 301 549 Klausel 11. Tooling Xcode Accessibility Inspector, Android Accessibility Scanner. Konkrete Code-Beispiele Swift und Kotlin fuer haeufige Probleme.

# Native Apps iOS und Android

## Spezialwissen: Native Apps iOS und Android
- **Spezialgegenstand:** Native Apps iOS und Android / native apps ios android pruefung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** API, EN.
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
Dieser Skill gehoert zum Plugin `barrierefreiheit-web-checker`. Er ergaenzt die uebrigen Skills des Plugins um einen vertieften Spezialfall oder eine systematische Einfuehrung. Bei Folgefragen werden andere Skills des Plugins als Anschluss vorgeschlagen.

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
