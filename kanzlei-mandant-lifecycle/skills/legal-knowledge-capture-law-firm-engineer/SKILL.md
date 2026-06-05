---
name: legal-knowledge-capture-law-firm-engineer
description: "Legal Knowledge Capture LAW Firm Engineer im Plugin Kanzlei Mandant Lifecycle: prüft konkret Knowledge Capture, Kanzlei-interne Sprache, Legal Engineer Dashboard, Legal Hold Dashboard. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Legal Knowledge Capture LAW Firm Engineer

## Arbeitsbereich

**Legal Knowledge Capture LAW Firm Engineer** ordnet den Fall über die tragenden Prüffelder: Knowledge Capture, Kanzlei-interne Sprache, Legal Engineer Dashboard. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `knowledge-capture` | Knowledge Capture: steuert Mandatswissen in Playbooks, Muster, Risikoentscheidungen und Lessons Learned überführen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `law-firm-internal-language` | Kanzlei-interne Sprache: steuert interne Tasknotizen, Reviewkommentare und Risikoformulierungen mandatsfest halten zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `legal-engineer-dashboard` | Legal Engineer Dashboard: steuert Automatisierung, Datenextraktion, KI-Nutzung, Datenschutz und Outputprüfung im Mandat zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `legal-hold-dashboard` | Legal Hold Dashboard: steuert Legal Holds mit Custodians, Datenquellen, Bestätigung und Review-Fenstern führen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `legal-ops-roadmap` | Legal Ops Roadmap: steuert von E-Mail-Chaos zu Matter-Management, eBilling, Dashboards und Wissensspeicher zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |

## Arbeitsweg

- Rolle und Ziel im Kanzlei Mandant Lifecycle klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `knowledge-capture`

**Fokus:** Knowledge Capture: steuert Mandatswissen in Playbooks, Muster, Risikoentscheidungen und Lessons Learned überführen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Knowledge Capture

## Fachkern: Knowledge Capture
- **Spezialgegenstand:** Knowledge Capture wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Knowledge Capture** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Mandatswissen in Playbooks, Muster, Risikoentscheidungen und Lessons Learned überführen

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** Datenschutz, Mandatsgeheimnis, Urheber-/Nutzungsrechte und Wissensmanagement.
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

## 2. `law-firm-internal-language`

**Fokus:** Kanzlei-interne Sprache: steuert interne Tasknotizen, Reviewkommentare und Risikoformulierungen mandatsfest halten zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Kanzlei-interne Sprache

## Fachkern: Kanzlei-interne Sprache
- **Spezialgegenstand:** Kanzlei-interne Sprache wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Kanzlei-interne Sprache** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** interne Tasknotizen, Reviewkommentare und Risikoformulierungen mandatsfest halten

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** Berufsrecht, Haftung, Mandatsgeheimnis und Wissensmanagement.
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

## 3. `legal-engineer-dashboard`

**Fokus:** Legal Engineer Dashboard: steuert Automatisierung, Datenextraktion, KI-Nutzung, Datenschutz und Outputprüfung im Mandat zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Legal Engineer Dashboard

## Fachkern: Legal Engineer Dashboard
- **Spezialgegenstand:** Legal Engineer Dashboard wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Legal Engineer Dashboard** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Automatisierung, Datenextraktion, KI-Nutzung, Datenschutz und Outputprüfung im Mandat

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** BRAO § 43e, DSGVO, § 203 StGB, AI Act-Schnittstellen und Qualitätssicherung.
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

## 4. `legal-hold-dashboard`

**Fokus:** Legal Hold Dashboard: steuert Legal Holds mit Custodians, Datenquellen, Bestätigung und Review-Fenstern führen zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Legal Hold Dashboard

## Fachkern: Legal Hold Dashboard
- **Spezialgegenstand:** Legal Hold Dashboard wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Legal Hold Dashboard** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Legal Holds mit Custodians, Datenquellen, Bestätigung und Review-Fenstern führen

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** ZPO/StPO/ArbG je nach Fall, Datenschutz und IT-Governance.
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

## 5. `legal-ops-roadmap`

**Fokus:** Legal Ops Roadmap: steuert von E-Mail-Chaos zu Matter-Management, eBilling, Dashboards und Wissensspeicher zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Legal Ops Roadmap

## Fachkern: Legal Ops Roadmap
- **Spezialgegenstand:** Legal Ops Roadmap wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Legal Ops Roadmap** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** von E-Mail-Chaos zu Matter-Management, eBilling, Dashboards und Wissensspeicher

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** Datenschutz, BRAO § 43e, § 203 StGB, DSGVO und IT-Sicherheit.
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
