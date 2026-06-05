---
name: law-firm-access-control-action-item-appeal
description: "Law Firm Feedback Loop, Access Control Roles, Action Item Owner Matrix, Appeal Decision Gate: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Law Firm Feedback Loop, Access Control Roles, Action Item Owner Matrix, Appeal Decision Gate, Associate Workbench

## Arbeitsbereich

In diesem Skill wird **Law Firm Feedback Loop, Access Control Roles, Action Item Owner Matrix, Appeal Decision Gate, Associate Workbench** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `law-firm-feedback-loop` | Law Firm Feedback Loop: steuert Mandant gibt Feedback ohne Gesichtsverlust; Kanzlei verbessert sich messbar zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `access-control-roles` | Access Control Roles: steuert Rollen, Berechtigungen, Need-to-know, externe Dienstleister und Austritt aus dem Matter zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `action-item-owner-matrix` | Action-Item Owner Matrix: steuert Wer schuldet was bis wann: Kanzlei, Inhouse, Fachabteilung, Gericht, Gegner, Gutachter zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `appeal-decision-gate` | Rechtsmittel Decision Gate: steuert Berufung/Revision/Beschwerde: Frist, Kosten, Chancen, Business-Ziel und Gremienfreigabe zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `associate-workbench` | Associate Workbench: steuert Associate bekommt klare Aufgaben, Kontext, Deadline, Qualitätsmaßstab und Feedback zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |

## Arbeitsweg

Für **Law Firm Feedback Loop, Access Control Roles, Action Item Owner Matrix, Appeal Decision Gate, Associate Workbench** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `kanzlei-mandant-lifecycle` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `law-firm-feedback-loop`

**Fokus:** Law Firm Feedback Loop: steuert Mandant gibt Feedback ohne Gesichtsverlust; Kanzlei verbessert sich messbar zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Law Firm Feedback Loop

## Fachkern: Law Firm Feedback Loop
- **Spezialgegenstand:** Law Firm Feedback Loop wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Nutze diesen Skill im Plugin **Kanzlei-Mandant Lifecycle**, wenn der Fall genau in diese Lage führt. Ziel ist keine allgemeine Belehrung, sondern ein steuerbarer Arbeitsweg mit Dokumentenlogik, Risikoampel, nächstem Schritt und sauberem Quellencheck.

**Fokus:** Mandant gibt Feedback ohne Gesichtsverlust; Kanzlei verbessert sich messbar

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** Relationship Governance, Datenschutz, Qualitätsmanagement und Eskalationskultur.
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

## 2. `access-control-roles`

**Fokus:** Access Control Roles: steuert Rollen, Berechtigungen, Need-to-know, externe Dienstleister und Austritt aus dem Matter zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Access Control Roles

## Fachkern: Access Control Roles
- **Spezialgegenstand:** Access Control Roles wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Nutze diesen Skill im Plugin **Kanzlei-Mandant Lifecycle**, wenn der Fall genau in diese Lage führt. Ziel ist keine allgemeine Belehrung, sondern ein steuerbarer Arbeitsweg mit Dokumentenlogik, Risikoampel, nächstem Schritt und sauberem Quellencheck.

**Fokus:** Rollen, Berechtigungen, Need-to-know, externe Dienstleister und Austritt aus dem Matter

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** DSGVO, Geschäftsgeheimnisgesetz, BRAO § 43e und IT-Sicherheit.
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

## 3. `action-item-owner-matrix`

**Fokus:** Action-Item Owner Matrix: steuert Wer schuldet was bis wann: Kanzlei, Inhouse, Fachabteilung, Gericht, Gegner, Gutachter zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Action-Item Owner Matrix

## Fachkern: Action-Item Owner Matrix
- **Spezialgegenstand:** Action-Item Owner Matrix wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Nutze diesen Skill im Plugin **Kanzlei-Mandant Lifecycle**, wenn der Fall genau in diese Lage führt. Ziel ist keine allgemeine Belehrung, sondern ein steuerbarer Arbeitsweg mit Dokumentenlogik, Risikoampel, nächstem Schritt und sauberem Quellencheck.

**Fokus:** Wer schuldet was bis wann: Kanzlei, Inhouse, Fachabteilung, Gericht, Gegner, Gutachter

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** Projektmanagement, Mandatsvertrag, Fristenrecht und Beweislogik.
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

## 4. `appeal-decision-gate`

**Fokus:** Rechtsmittel Decision Gate: steuert Berufung/Revision/Beschwerde: Frist, Kosten, Chancen, Business-Ziel und Gremienfreigabe zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Rechtsmittel Decision Gate

## Fachkern: Rechtsmittel Decision Gate
- **Spezialgegenstand:** Rechtsmittel Decision Gate wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Nutze diesen Skill im Plugin **Kanzlei-Mandant Lifecycle**, wenn der Fall genau in diese Lage führt. Ziel ist keine allgemeine Belehrung, sondern ein steuerbarer Arbeitsweg mit Dokumentenlogik, Risikoampel, nächstem Schritt und sauberem Quellencheck.

**Fokus:** Berufung/Revision/Beschwerde: Frist, Kosten, Chancen, Business-Ziel und Gremienfreigabe

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** ZPO/Verfahrensrecht, Kostenrecht, Mandatsvertrag und Organpflichten.
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

## 5. `associate-workbench`

**Fokus:** Associate Workbench: steuert Associate bekommt klare Aufgaben, Kontext, Deadline, Qualitätsmaßstab und Feedback zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Associate Workbench

## Fachkern: Associate Workbench
- **Spezialgegenstand:** Associate Workbench wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Nutze diesen Skill im Plugin **Kanzlei-Mandant Lifecycle**, wenn der Fall genau in diese Lage führt. Ziel ist keine allgemeine Belehrung, sondern ein steuerbarer Arbeitsweg mit Dokumentenlogik, Risikoampel, nächstem Schritt und sauberem Quellencheck.

**Fokus:** Associate bekommt klare Aufgaben, Kontext, Deadline, Qualitätsmaßstab und Feedback

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** Berufsrecht, Supervision, Mandatsvertrag und Ausbildung.
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
