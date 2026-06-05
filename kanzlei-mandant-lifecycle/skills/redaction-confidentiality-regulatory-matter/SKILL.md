---
name: redaction-confidentiality-regulatory-matter
description: "Redaction Confidentiality Regulatory Matter im Plugin Kanzlei Mandant Lifecycle: prüft konkret Redaction und Confidentiality, Regulatory Matter Command, Regulatory Remediation Plan, Relationship Red Flags. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Redaction Confidentiality Regulatory Matter

## Arbeitsbereich

**Redaction Confidentiality Regulatory Matter** ordnet den Fall über die tragenden Prüffelder: Redaction und Confidentiality, Regulatory Matter Command, Regulatory Remediation Plan. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `redaction-confidentiality` | Redaction und Confidentiality: steuert Schwärzungen, Anlagen, Betriebsgeheimnisse und Gerichts-/Gegnerfassung sauber steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `regulatory-matter-command` | Regulatory Matter Command: steuert Behördenverfahren mit Kanzlei und Inhouse steuern: Auskunft, Akteneinsicht, Frist, Ton zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `regulatory-remediation-plan` | Regulatory Remediation Plan: steuert nach Auflage/Bußgeld/Prüfung Maßnahmenplan, Owner, Nachweis und Kanzleirolle steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `relationship-redflags` | Relationship Red Flags: steuert Warnzeichen: Funkstille, Überraschungsrechnung, Scope-Unklarheit, Strategiedrift, Fristdruck zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |
| `relationship-renewal` | Relationship Renewal: steuert nach Krise oder Erfolg: neue OCG, bessere Reports, neue Teams, neue Preise zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene. |

## Arbeitsweg

- Rolle und Ziel im Kanzlei Mandant Lifecycle klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `redaction-confidentiality`

**Fokus:** Redaction und Confidentiality: steuert Schwärzungen, Anlagen, Betriebsgeheimnisse und Gerichts-/Gegnerfassung sauber steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Redaction und Confidentiality

## Fachkern: Redaction und Confidentiality
- **Spezialgegenstand:** Redaction und Confidentiality wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Redaction und Confidentiality** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Schwärzungen, Anlagen, Betriebsgeheimnisse und Gerichts-/Gegnerfassung sauber steuern

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** GeschGehG, ZPO, Datenschutz, Mandatsgeheimnis und Verfahrensrecht.
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

## 2. `regulatory-matter-command`

**Fokus:** Regulatory Matter Command: steuert Behördenverfahren mit Kanzlei und Inhouse steuern: Auskunft, Akteneinsicht, Frist, Ton zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Regulatory Matter Command

## Fachkern: Regulatory Matter Command
- **Spezialgegenstand:** Regulatory Matter Command wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Regulatory Matter Command** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Behördenverfahren mit Kanzlei und Inhouse steuern: Auskunft, Akteneinsicht, Frist, Ton

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** VwVfG/VwGO/OWiG je nach Behörde, Datenschutz, Berufsrecht und Governance.
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

## 3. `regulatory-remediation-plan`

**Fokus:** Regulatory Remediation Plan: steuert nach Auflage/Bußgeld/Prüfung Maßnahmenplan, Owner, Nachweis und Kanzleirolle steuern zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Regulatory Remediation Plan

## Fachkern: Regulatory Remediation Plan
- **Spezialgegenstand:** Regulatory Remediation Plan wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Regulatory Remediation Plan** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** nach Auflage/Bußgeld/Prüfung Maßnahmenplan, Owner, Nachweis und Kanzleirolle steuern

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** VwVfG/OWiG/Branchenrecht, Datenschutz, Governance und Reporting.
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

## 4. `relationship-redflags`

**Fokus:** Relationship Red Flags: steuert Warnzeichen: Funkstille, Überraschungsrechnung, Scope-Unklarheit, Strategiedrift, Fristdruck zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Relationship Red Flags

## Fachkern: Relationship Red Flags
- **Spezialgegenstand:** Relationship Red Flags wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Relationship Red Flags** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** Warnzeichen: Funkstille, Überraschungsrechnung, Scope-Unklarheit, Strategiedrift, Fristdruck

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** Beratungspflichten, Haftung, Mandatsvertrag und Eskalationsmanagement.
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

## 5. `relationship-renewal`

**Fokus:** Relationship Renewal: steuert nach Krise oder Erfolg: neue OCG, bessere Reports, neue Teams, neue Preise zwischen Kanzlei, Mandant und Rechtsabteilung mit Dashboard, Budget, Fristen, Verantwortlichkeiten, Beziehungspflege und Quellenhygiene.

# Relationship Renewal

## Fachkern: Relationship Renewal
- **Spezialgegenstand:** Relationship Renewal wird als eigener Falltyp behandelt; der Skill muss ein konkretes Ergebnis liefern, nicht nur Einstieg und Routing.
- **Normen-/Quellenanker:** BGB-Dienst-/Geschäftsbesorgungsvertrag, RVG, BRAO/BORA, DSGVO, GeschGehG, ZPO/ArbGG/VwGO je nach Mandat und Legal-Ops-Vorgaben.
- **Entscheidende Weiche:** Kläre Scope, Budget, Deliverable, Eskalationspunkt, Verantwortlichen, Frist, Erfolgskriterium und Kommunikationsspur.
- **Lösungsoutput:** Erzeuge eine fallbezogene Matrix `Norm / Tatbestand / Beleg / Risiko / Gegenargument / nächster Schritt` und benenne passende Anschluss-Skills nur, wenn sie wirklich eine Vertiefung lösen.


## Worum es geht

Dieser Abschnitt bearbeitet **Fachkern: Relationship Renewal** im Bereich **Kanzlei-Mandant Lifecycle**. Er verdichtet Sachverhalt, Rollen, Dokumente, Risiken, Quellen und nächsten Schritt zu einem steuerbaren Arbeitsweg.

**Fokus:** nach Krise oder Erfolg: neue OCG, bessere Reports, neue Teams, neue Preise

## Kaltstart-Fragen

- Wer spricht gerade: Kanzlei, Einzelanwalt, Rechtsabteilung, GC, CFO, Fachabteilung oder Gericht/Behörde?
- Welches Matter, welches Ziel, welche Frist, welches Budget und welche Entscheidung stehen an?
- Welche Informationen sind geheim, personenbezogen, privilegiert oder nur intern verwendbar?
- Soll ein Dashboard, Memo, E-Mail, Rechnungskommentar, Board Paper oder Maßnahmenplan entstehen?

## Prüf- und Arbeitslogik

- **Rechtsanker:** Mandatsvertrag, RVG/BRAO, Datenschutz und Relationship Governance.
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
