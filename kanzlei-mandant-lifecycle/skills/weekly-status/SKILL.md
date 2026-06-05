---
name: weekly-status
description: "Weekly Status Report: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Weekly Status Report

## Arbeitsbereich

In diesem Skill wird **Weekly Status Report** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `weekly-status-report` | Weekly Status Report: steuert Wochenbericht mit Done/Doing/Blocked, Fristen, Budget, Risiken und Entscheidungen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |

## Arbeitsweg

Für **Weekly Status Report** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `kanzlei-mandant-lifecycle` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `weekly-status-report`

**Fokus:** Weekly Status Report: steuert Wochenbericht mit Done/Doing/Blocked, Fristen, Budget, Risiken und Entscheidungen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Weekly Status Report

## Fachkern: Weekly Status Report
- **Spezialgegenstand:** Weekly Status Report wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Nutze diesen Skill im Plugin **Kanzlei-Mandant Lifecycle**, wenn der Fall genau in diese Lage führt. Ziel ist keine allgemeine Belehrung, sondern ein steuerbarer Arbeitsweg mit Dokumentenlogik, Risikoampel, nächstem Schritt und sauberem Quellencheck.

**Fokus:** Wochenbericht mit Done/Doing/Blocked, Fristen, Budget, Risiken und Entscheidungen

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** Mandatsvertrag, Verfahrensrecht, Legal Ops und Management Reporting.
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
