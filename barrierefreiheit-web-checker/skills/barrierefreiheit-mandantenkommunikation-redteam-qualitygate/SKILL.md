---
name: barrierefreiheit-mandantenkommunikation-redteam-qualitygate
description: "Mandantenkommunikation Redteam Qualitygate im Plugin Barrierefreiheit Web Checker: prüft konkret Mandantenkommunikation im Plugin, Red-Team Qualitygate im Plugin barrierefreiheit-web-checker, Erstellt Barrierefreiheitserklärung, Feedbackmechanismus. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Mandantenkommunikation Redteam Qualitygate

## Arbeitsbereich

Dieser Skill behandelt **Mandantenkommunikation Redteam Qualitygate** als zusammenhängenden Arbeitsgang im Plugin Barrierefreiheit Web Checker. Im Mittelpunkt steht die Prüfung von Mandantenkommunikation im Plugin, Red-Team Qualitygate im Plugin barrierefreiheit-web-checker, Erstellt Barrierefreiheitserklärung. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin barrierefreiheit-web-checker: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin barrierefreiheit-web-checker: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `erklaerung-feedback-durchsetzung` | Erstellt Barrierefreiheitserklärung, Feedbackmechanismus, Durchsetzungs- und Behördenreaktion. Trennt öffentliche Stellen, BFSG-relevante Dienste und freiwillige Erklärungen. Output: Erklärung, Antwortbrief oder Maßnahmenvermerk. |

## Arbeitsweg

- Rolle und Ziel im Web-Barrierefreiheits-Checker für BFSG, BFSGV, BITV 2 klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BFSG; WCAG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `workflow-mandantenkommunikation`

**Fokus:** Mandantenkommunikation im Plugin barrierefreiheit-web-checker: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten.

# Mandantenkommunikation

## Aufgabe
Dieses Modul bearbeitet: Mandantenkommunikation im Plugin barrierefreiheit-web-checker: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Mandantenkommunikation Barrierefreiheit
- **Anrede + Bezug:** "In Sachen [Mandant] / Ihre BFSG-Konformität"
- **Sachstand kurz:** Anwendungsbereich BFSG (welcher Katalog-Tatbestand), Audit-Stand, Mängelübersicht (Critical/Major/Minor).
- **Empfehlung:** Reihenfolge der Behebung — zuerst Critical (Tastatur, Screenreader, Kontrast, Formularlabels), dann Major, dann Minor.
- **Risikoampel** mit Bezug auf § 37 BFSG (Bußgeld bis 100.000 EUR) und Marktüberwachung § 19 BFSG.
- **Frist:** BFSG seit 28.06.2025; bei laufender Marktüberwachung konkrete Behördenfrist.
- **Kostenhinweis:** RVG/Honorarvereinbarung; bei Audit ggf. Pauschalabrede.
- **Klarheit über Reichweite:** Audit-Methodik (WCAG 2.1 AA via EN 301 549), getestete Seiten/Funktionen — keine Generalaussage aus Stichprobe.

## Praxis-Tipp
Vermeiden Sie die Botschaft "barrierefrei" oder "nicht barrierefrei". Korrekt ist immer: "konform zu WCAG 2.1 AA, geprüft am [Datum] auf [Geltungsbereich]". Die Differenz zwischen Stichprobe und Generalaussage ist haftungsrelevant.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 2. `workflow-redteam-qualitygate`

**Fokus:** Red-Team Qualitygate im Plugin barrierefreiheit-web-checker: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton.

# Red-Team Qualitygate

## Aufgabe
Dieses Modul bearbeitet: Red-Team Qualitygate im Plugin barrierefreiheit-web-checker: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton..

## Einstieg
Prüfe zuerst das vorhandene Material. Stelle nur Rückfragen, die die nächste fachliche Weiche verändern:

1. Wer fragt in welcher Rolle?
2. Was ist das gewünschte Ergebnis?
3. Gibt es Fristen, Termine, Zustellungen, Zahlungen oder Sanktionen?
4. Welche Unterlagen, Daten oder Belege liegen bereits vor?

## Arbeitsworkflow
1. Rolle, Ziel, Frist und Unterlagenlage in höchstens fünf Fragen klären.
2. Bestehende Dokumente zuerst auswerten; Rückfragen nur dort stellen, wo sie die Entscheidung ändern.
3. Passende Fachmodule aus diesem Plugin vorschlagen und begründen.
4. Ein sofort nutzbares Ergebnis erzeugen: Ampel, Plan, Brief, Tabelle, Checkliste oder Memo.

## Red-Team-Prüfpunkte Barrierefreiheit
1. **Anwendungsbereich BFSG (§ 1 BFSG):** Liegt das konkrete Produkt/die Dienstleistung im abschließenden Katalog? Bei Verneinung: keine BFSG-Pflicht — auch nicht analog.
2. **Adressat:** Wirtschaftsakteur § 3 BFSG; Ausnahme Kleinstunternehmen § 3 Abs. 3 BFSG (< 10 Beschäftigte und < 2 Mio. EUR Jahresumsatz/Bilanzsumme).
3. **BFSG vs. BITV 2.0:** Öffentliche Stellen → BITV 2.0 (Bund) / Landesrecht. Privatwirtschaft → BFSG. Diese Trennung wird häufig vermischt.
4. **Geltungsbeginn:** BFSG seit 28.06.2025; bestehende Produkte mit Übergang § 38 BFSG.
5. **Norm-Bezug:** EN 301 549 (harmonisierte Norm) inkorporiert WCAG 2.1 AA. Konformitätsvermutung über EN-Norm; davon abweichend ist Begründungslast.
6. **Audit-Reichweite:** Wurde tatsächlich repräsentativ getestet (Seiten + Funktionen + Geräte + Hilfsmittel)?
7. **Halluzinations-Check:** Keine erfundenen WCAG-Erfolgskriterien oder BITV-Anhang-Bezüge.

## Praxis-Tipp
Verbreiteter Fehler: ein Software-Anbieter wird beraten, "Sie müssen WCAG erfüllen", ohne dass die konkrete Subsumtion unter den BFSG-Katalog § 1 Abs. 2/3 BFSG geleistet wurde. Auch ein B2B-Produkt fällt regelmäßig nicht unter BFSG, was eine bedeutsame Risikoabschätzung verändert.

## Output-Standard
- Kurzbild: worum es geht, was gesichert ist, was offen ist.
- Prüf- oder Bearbeitungsmatrix mit den entscheidenden Punkten.
- Konkreter nächster Schritt mit Frist, Zuständigkeit und Unterlagen.
- Bei Außenkommunikation: knapper, sachlicher Textbaustein ohne unnötige Nebenangaben.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## 3. `erklaerung-feedback-durchsetzung`

**Fokus:** Erstellt Barrierefreiheitserklärung, Feedbackmechanismus, Durchsetzungs- und Behördenreaktion. Trennt öffentliche Stellen, BFSG-relevante Dienste und freiwillige Erklärungen. Output: Erklärung, Antwortbrief oder Maßnahmenvermerk.

# Erklärung, Feedback, Durchsetzung

Dieses Fachmodul prüft Barrierefreiheitserklärungen, Feedbackwege, Beschwerden, Marktüberwachungs- oder Behördenanfragen.

## Inhalt einer guten Erklärung

- Geltungsbereich: Website/App/Dokumente.
- Maßstab: BITV/EN 301 549/WCAG oder freiwilliger Standard.
- Stand der Vereinbarkeit.
- Nicht barrierefreie Inhalte mit Begründung und Maßnahmenplan.
- Erstellungsmethode: Selbstbewertung, externer Audit, Datum.
- Feedbackkontakt.
- Durchsetzungs- oder Beschwerdestelle, falls einschlägig.

## Antwort auf Beschwerde

```text
Vielen Dank für den Hinweis. Wir haben die gemeldete Barriere unter der Vorgangsnummer [...] aufgenommen. Betroffen ist [...]. Wir prüfen den Fehler bis [...] und teilen Ihnen mit, welche Zwischenlösung oder Korrektur vorgesehen ist. Wenn Sie die Information sofort benötigen, stellen wir sie Ihnen in folgender barrierearmer Form bereit: [...].
```

## Red Flags

- Erklärung ist reine Werbeseite.
- "Wir sind WCAG-konform" ohne Auditdatum.
- Feedbackadresse geht ins Leere.
- Bekannte Barrieren werden verschwiegen.
- Keine Alternative für dringende Informationen.

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
