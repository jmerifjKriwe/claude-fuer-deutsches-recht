---
name: billing-to-blockbilling-detector-board
description: "Billing TO Blockbilling Detector Board im Plugin Kanzlei Mandant Lifecycle: prüft konkret Billing to XRechnung, Blockbilling Detector, Board Reporting, Budget Baseline und Phasenplan. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Billing TO Blockbilling Detector Board

## Arbeitsbereich

Dieser Skill behandelt **Billing TO Blockbilling Detector Board** als zusammenhängenden Arbeitsgang im Plugin Kanzlei Mandant Lifecycle. Im Mittelpunkt steht die Prüfung von Billing to XRechnung, Blockbilling Detector, Board Reporting und weiteren verwandten Aspekten. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `billing-to-xrechnung` | Billing to XRechnung: steuert Kanzleirechnung in E-Rechnung/XRechnung, Kostenstellen und Prüfüberführen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `blockbilling-detector` | Blockbilling Detector: steuert zu grobe Stundenblöcke, doppelte Arbeit, Reisezeit und interne Abstimmungen prüfen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `board-reporting` | Board Reporting: steuert Vorstand/Aufsichtsrat-Gremium bekommt knappe, belastbare Lage: Risiko, Kosten, Entscheidung, nächste Frist zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `budget-baseline-und-phasen` | Budget Baseline und Phasenplan: steuert Budget nach Phasen, Annahmen, Exclusions, Triggern und Reforecast-Regeln aufsetzen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `budget-overrun-escalation` | Budget Overrun Escalation: steuert Budgetüberschreitung erklären, genehmigen, nachsteuern oder stoppen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |

## Arbeitsweg

- Rolle und Ziel im Kanzlei Mandant Lifecycle klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `billing-to-xrechnung`

**Fokus:** Billing to XRechnung: steuert Kanzleirechnung in E-Rechnung/XRechnung, Kostenstellen und Prüfüberführen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Billing to XRechnung

## Fachkern: Billing to XRechnung
- **Spezialgegenstand:** Billing to XRechnung wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Billing to XRechnung** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Kanzleirechnung in E-Rechnung/XRechnung, Kostenstellen und Prüfüberführen

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** RVG, E-Rechnungspflichten, UStG, GoBD-Schnittstellen und OCG.
- **Tatsachenanker:** Mandatsdatum, Rollen, Scope, Freigaben, Zustellungen, Budgetstand, Beweiswert, Eskalationen und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Keine Mandatsgeheimnisse in ungeprüfte Systeme geben.
- Budget und Erfolgsaussicht nie als Scheingenauigkeit verkaufen.
- Kanzlei- und Mandantensicht trennen und dann bewusst zusammenführen.
- Rechnung, Scope und Beziehung früh klären, bevor Misstrauen entsteht.

## Output

- Dashboard-Karte mit Status, Budget, Ownern und nächstem Schritt.
- Entscheidungsvorlage oder Kommunikationsentwurf für Kanzlei oder Mandant.
- Risiko-/Kosten-/Fristenampel mit Eskalationspunkt.
- Qualitygate: Was darf raus, was muss intern bleiben, was braucht Freigabe?

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- RVG § 3a: https://www.gesetze-im-internet.de/rvg/__3a.html
- BRAO § 43e: https://www.gesetze-im-internet.de/brao/__43e.html
- BRAO § 49b: https://www.gesetze-im-internet.de/brao/__49b.html

## 2. `blockbilling-detector`

**Fokus:** Blockbilling Detector: steuert zu grobe Stundenblöcke, doppelte Arbeit, Reisezeit und interne Abstimmungen prüfen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Blockbilling Detector

## Fachkern: Blockbilling Detector
- **Spezialgegenstand:** Blockbilling Detector wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Blockbilling Detector** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** zu grobe Stundenblöcke, doppelte Arbeit, Reisezeit und interne Abstimmungen prüfen

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** Vergütungsvereinbarung, OCG, RVG und kaufmännische Angemessenheit.
- **Tatsachenanker:** Mandatsdatum, Rollen, Scope, Freigaben, Zustellungen, Budgetstand, Beweiswert, Eskalationen und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Keine Mandatsgeheimnisse in ungeprüfte Systeme geben.
- Budget und Erfolgsaussicht nie als Scheingenauigkeit verkaufen.
- Kanzlei- und Mandantensicht trennen und dann bewusst zusammenführen.
- Rechnung, Scope und Beziehung früh klären, bevor Misstrauen entsteht.

## Output

- Dashboard-Karte mit Status, Budget, Ownern und nächstem Schritt.
- Entscheidungsvorlage oder Kommunikationsentwurf für Kanzlei oder Mandant.
- Risiko-/Kosten-/Fristenampel mit Eskalationspunkt.
- Qualitygate: Was darf raus, was muss intern bleiben, was braucht Freigabe?

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- RVG § 3a: https://www.gesetze-im-internet.de/rvg/__3a.html
- BRAO § 43e: https://www.gesetze-im-internet.de/brao/__43e.html
- BRAO § 49b: https://www.gesetze-im-internet.de/brao/__49b.html

## 3. `board-reporting`

**Fokus:** Board Reporting: steuert Vorstand/Aufsichtsrat-Gremium bekommt knappe, belastbare Lage: Risiko, Kosten, Entscheidung, nächste Frist zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Board Reporting

## Fachkern: Board Reporting
- **Spezialgegenstand:** Board Reporting wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Board Reporting** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Vorstand/Aufsichtsrat-Gremium bekommt knappe, belastbare Lage: Risiko, Kosten, Entscheidung, nächste Frist

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** AktG/GmbHG-Organpflichten, Legal Privilege, Datenschutz und Mandatsvertrag.
- **Tatsachenanker:** Mandatsdatum, Rollen, Scope, Freigaben, Zustellungen, Budgetstand, Beweiswert, Eskalationen und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Keine Mandatsgeheimnisse in ungeprüfte Systeme geben.
- Budget und Erfolgsaussicht nie als Scheingenauigkeit verkaufen.
- Kanzlei- und Mandantensicht trennen und dann bewusst zusammenführen.
- Rechnung, Scope und Beziehung früh klären, bevor Misstrauen entsteht.

## Output

- Dashboard-Karte mit Status, Budget, Ownern und nächstem Schritt.
- Entscheidungsvorlage oder Kommunikationsentwurf für Kanzlei oder Mandant.
- Risiko-/Kosten-/Fristenampel mit Eskalationspunkt.
- Qualitygate: Was darf raus, was muss intern bleiben, was braucht Freigabe?

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- RVG § 3a: https://www.gesetze-im-internet.de/rvg/__3a.html
- BRAO § 43e: https://www.gesetze-im-internet.de/brao/__43e.html
- BRAO § 49b: https://www.gesetze-im-internet.de/brao/__49b.html

## 4. `budget-baseline-und-phasen`

**Fokus:** Budget Baseline und Phasenplan: steuert Budget nach Phasen, Annahmen, Exclusions, Triggern und Reforecast-Regeln aufsetzen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Budget Baseline und Phasenplan

## Fachkern: Budget Baseline und Phasenplan
- **Spezialgegenstand:** Budget Baseline und Phasenplan wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Budget Baseline und Phasenplan** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Budget nach Phasen, Annahmen, Exclusions, Triggern und Reforecast-Regeln aufsetzen

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** RVG/Vergütungsvereinbarung, Legal-Ops-Standards, Kostenrecht und kaufmännische Plausibilität.
- **Tatsachenanker:** Mandatsdatum, Rollen, Scope, Freigaben, Zustellungen, Budgetstand, Beweiswert, Eskalationen und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Keine Mandatsgeheimnisse in ungeprüfte Systeme geben.
- Budget und Erfolgsaussicht nie als Scheingenauigkeit verkaufen.
- Kanzlei- und Mandantensicht trennen und dann bewusst zusammenführen.
- Rechnung, Scope und Beziehung früh klären, bevor Misstrauen entsteht.

## Output

- Dashboard-Karte mit Status, Budget, Ownern und nächstem Schritt.
- Entscheidungsvorlage oder Kommunikationsentwurf für Kanzlei oder Mandant.
- Risiko-/Kosten-/Fristenampel mit Eskalationspunkt.
- Qualitygate: Was darf raus, was muss intern bleiben, was braucht Freigabe?

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- RVG § 3a: https://www.gesetze-im-internet.de/rvg/__3a.html
- BRAO § 43e: https://www.gesetze-im-internet.de/brao/__43e.html
- BRAO § 49b: https://www.gesetze-im-internet.de/brao/__49b.html

## 5. `budget-overrun-escalation`

**Fokus:** Budget Overrun Escalation: steuert Budgetüberschreitung erklären, genehmigen, nachsteuern oder stoppen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Budget Overrun Escalation

## Fachkern: Budget Overrun Escalation
- **Spezialgegenstand:** Budget Overrun Escalation wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Budget Overrun Escalation** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Budgetüberschreitung erklären, genehmigen, nachsteuern oder stoppen

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** RVG/Vergütung, Mandatsvertrag, OCG, Legal Ops und Beziehungspflege.
- **Tatsachenanker:** Mandatsdatum, Rollen, Scope, Freigaben, Zustellungen, Budgetstand, Beweiswert, Eskalationen und offene Lücken trennen.
- **Risikoebenen:** Haftung, Berufsrecht, Datenschutz, Vergütung, Frist, Eskalation, Reputationsrisiko und Governance getrennt ausgeben.
- **Gegenposition:** die beste plausible Gegenansicht formulieren und sagen, welche Unterlage sie trägt oder entkräftet.
- **Entscheidung:** einen Minimalpfad für heute und einen robusten Hauptpfad für die nächsten Arbeitstage vorschlagen.

## Typische Fehlerquellen

- Keine Mandatsgeheimnisse in ungeprüfte Systeme geben.
- Budget und Erfolgsaussicht nie als Scheingenauigkeit verkaufen.
- Kanzlei- und Mandantensicht trennen und dann bewusst zusammenführen.
- Rechnung, Scope und Beziehung früh klären, bevor Misstrauen entsteht.

## Output

- Dashboard-Karte mit Status, Budget, Ownern und nächstem Schritt.
- Entscheidungsvorlage oder Kommunikationsentwurf für Kanzlei oder Mandant.
- Risiko-/Kosten-/Fristenampel mit Eskalationspunkt.
- Qualitygate: Was darf raus, was muss intern bleiben, was braucht Freigabe?

## Quellen- und Aktualitätsgate

Vor tragenden Aussagen live prüfen: amtliche Normfassung, zuständige Behörde/Institution, frei zugängliche Rechtsprechung nur mit Gericht, Datum und Aktenzeichen. Keine BeckRS-/juris-/Kommentar-Blindzitate. Bei dynamischen Medizin-, EU-, Berufsrechts- und Vergütungsfragen immer den Stand des konkreten Tages nennen.

## Nützliche Startquellen

- RVG § 3a: https://www.gesetze-im-internet.de/rvg/__3a.html
- BRAO § 43e: https://www.gesetze-im-internet.de/brao/__43e.html
- BRAO § 49b: https://www.gesetze-im-internet.de/brao/__49b.html
