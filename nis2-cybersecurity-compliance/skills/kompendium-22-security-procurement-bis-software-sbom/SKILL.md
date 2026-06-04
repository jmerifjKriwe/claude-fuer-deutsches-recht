---
name: kompendium-22-security-procurement-bis-software-sbom
description: "nis2-cybersecurity-compliance: Konsolidiertes Skill-Kompendium 22; bündelt 4 frühere Spezialskills (security-procurement-tender, security-training-management, sektor-und-groessencheck, software-sbom) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 22 - nis2-cybersecurity-compliance

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `security-procurement-tender` | Prüft IT-Security-Anforderungen in Einkauf, Ausschreibung und Beschaffung von SaaS, Hardware, OT, Managed Services und Cyberdienstleistungen. |
| `security-training-management` | Prüft Security-Schulung der Leitung und Mitarbeitenden. |
| `sektor-und-groessencheck` | Ordnet Tätigkeiten in NIS-2-Sektoren und Unternehmensgrößen ein. |
| `software-sbom` | Baut SBOM-Prozess für eigene Software und Lieferanten. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `security-procurement-tender`

**Frühere Beschreibung:** Prüft IT-Security-Anforderungen in Einkauf, Ausschreibung und Beschaffung von SaaS, Hardware, OT, Managed Services und Cyberdienstleistungen.

# Security Procurement Tender

## Wofür dieser Skill da ist

Dieser Skill macht IT-Sicherheit beschaffbar: Er übersetzt NIS-2-/BSIG-, BSI-, Datenschutz- und Betriebsanforderungen in Vergabeunterlagen, RFPs, Leistungsverzeichnisse, Bewertungsmatrizen und Vertragsklauseln. Er ist besonders nützlich, wenn Einkauf schnell einen Anbieter beauftragen will und Legal/CISO verhindern müssen, dass Security erst nach dem Signing diskutiert wird.

## Kaltstartfragen

- Was wird beschafft: SaaS, Cloud, OT-Komponente, Fernwartung, MDM, SOC, Pentest, Hardware, KI-Tool oder Managed Service?
- Welche Daten, Systeme und Standorte sind betroffen?
- Ist der Anbieter Teil einer kritischen Lieferkette oder verarbeitet er besonders sensible Daten?
- Welche Nachweise werden verlangt: BSI C5, ISO 27001, SOC 2, Pentestbericht, SBOM, AVV, Subdienstleisterliste?
- Welche Muss-Kriterien führen zum Ausschluss?

## Arbeitslogik

1. **Bedarf klassifizieren:** Kritikalität, Datenklassen, Betriebsabhängigkeit, Exit-Risiko und Incident-Auswirkung bestimmen.
2. **Muss-Kriterien setzen:** MFA, Verschlüsselung, Logging, Schwachstellenprozess, Meldefristen, Subdienstleisterkontrolle, Exit, Auditrechte und Notfallkontakte.
3. **Nachweise bewerten:** Zertifikat, Testat, Management Assertion und Selbstauskunft nicht gleichsetzen.
4. **Vertrag vorbereiten:** Security Schedule, Incident Clause, Audit Clause, Datenschutz, Geheimnisse, Change Control und Exit.
5. **Entscheidung dokumentieren:** Warum ein Anbieter trotz Restlücken akzeptiert oder ausgeschlossen wurde.

## Typische Stolperstellen

- Einkauf fragt nur nach Preis und Verfügbarkeit.
- Anbieter verweist auf Zertifikate, deren Scope das konkrete Produkt nicht umfasst.
- Security-Anforderungen stehen im Lastenheft, fehlen aber im Vertrag.
- Subdienstleister und Supportzugriffe werden erst nach Go-live sichtbar.

## Ergebnisformat

Erzeuge eine RFP-/Tender-Matrix mit Muss-Kriterien, Bewertungspunkten, Nachweisfeld, Vertragsklausel und roter Ausschlusslogik.

## 2. `security-training-management`

**Frühere Beschreibung:** Prüft Security-Schulung der Leitung und Mitarbeitenden.

# Security Training Management

## Wofür dieser Skill da ist
Pflichtschulungen, Rollenmodule, Vorstandstraining, Nachweise, Wirksamkeit und Sanktionen.

Dieser Skill arbeitet nicht als abstraktes Merkblatt. Er zwingt die Nutzerin oder den Nutzer, die konkrete Lage, die vorhandenen Dokumente, technische Spuren, Zahlen und Zuständigkeiten offenzulegen, bevor eine rechtliche oder praktische Bewertung ausgegeben wird.

## Kaltstartfragen

- Welche konkrete Entscheidung steht jetzt an und wer muss sie verantworten?
- Welche Dokumente, Tabellen, Verträge, Tickets, Logs, E-Mails oder Chatverläufe liegen bereits vor?
- Welche Frist, Behörde, Vertragspartei, Kundengruppe oder interne Eskalation macht Druck?
- Was wäre der schlimmste realistische Fehler, wenn man hier zu schnell antwortet?
- Welche Quelle muss live geprüft werden, bevor eine Norm, Frist oder Rechtsprechung zitiert wird?

## Arbeitslogik

1. **Sachverhalt festnageln:** Beteiligte, Zeitraum, Dokumente, Zahlen, Systeme, Rollen und offene Lücken in einer kurzen Matrix erfassen.
2. **Pflichtanker setzen:** Maßgebliche Normen und Behördenquellen live prüfen; keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate verwenden.
3. **Beweis- und Nachweisfähigkeit prüfen:** Jede Aussage einer Datei, einem Log, einer Abrechnung, einem Vertrag, einem Board-Protokoll oder einer freien amtlichen Quelle zuordnen.
4. **Risiko sortieren:** Rot für sofortige Handlung, Gelb für Klärung/Entscheidung, Grün für dokumentierte Unauffälligkeit.
5. **Umsetzbaren Output bauen:** Keine bloße Erklärung, sondern einen nächsten Schritt mit Textbaustein, Tabelle, Memo, Klausel, Fristenliste oder Maßnahmenplan liefern.

## Fachanker

- Primärer Anker: NIS-2 Art. 20 Leitungsschulung; BSI.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Trainingsmatrix. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

## 3. `sektor-und-groessencheck`

**Frühere Beschreibung:** Ordnet Tätigkeiten in NIS-2-Sektoren und Unternehmensgrößen ein.

# Sektor Und Groessencheck

## Wofür dieser Skill da ist
Mehrspartenunternehmen, Konzernservice, kritische Zulieferer, IT-Dienstleister und Mischbetriebe sauber trennen.

Dieser Skill arbeitet nicht als abstraktes Merkblatt. Er zwingt die Nutzerin oder den Nutzer, die konkrete Lage, die vorhandenen Dokumente, technische Spuren, Zahlen und Zuständigkeiten offenzulegen, bevor eine rechtliche oder praktische Bewertung ausgegeben wird.

## Kaltstartfragen

- Welche konkrete Entscheidung steht jetzt an und wer muss sie verantworten?
- Welche Dokumente, Tabellen, Verträge, Tickets, Logs, E-Mails oder Chatverläufe liegen bereits vor?
- Welche Frist, Behörde, Vertragspartei, Kundengruppe oder interne Eskalation macht Druck?
- Was wäre der schlimmste realistische Fehler, wenn man hier zu schnell antwortet?
- Welche Quelle muss live geprüft werden, bevor eine Norm, Frist oder Rechtsprechung zitiert wird?

## Arbeitslogik

1. **Sachverhalt festnageln:** Beteiligte, Zeitraum, Dokumente, Zahlen, Systeme, Rollen und offene Lücken in einer kurzen Matrix erfassen.
2. **Pflichtanker setzen:** Maßgebliche Normen und Behördenquellen live prüfen; keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate verwenden.
3. **Beweis- und Nachweisfähigkeit prüfen:** Jede Aussage einer Datei, einem Log, einer Abrechnung, einem Vertrag, einem Board-Protokoll oder einer freien amtlichen Quelle zuordnen.
4. **Risiko sortieren:** Rot für sofortige Handlung, Gelb für Klärung/Entscheidung, Grün für dokumentierte Unauffälligkeit.
5. **Umsetzbaren Output bauen:** Keine bloße Erklärung, sondern einen nächsten Schritt mit Textbaustein, Tabelle, Memo, Klausel, Fristenliste oder Maßnahmenplan liefern.

## Fachanker

- Primärer Anker: NIS-2 Anhänge I/II; EU-KMU-Logik; BSIG 2025.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: Sektor-Mapping-Tabelle. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.

## 4. `software-sbom`

**Frühere Beschreibung:** Baut SBOM-Prozess für eigene Software und Lieferanten.

# Software SBOM

## Wofür dieser Skill da ist
Komponenten, Versionen, CVEs, Lizenzen, Kundenanforderungen, CRA-Schnittstelle und Nachverfolgung.

Dieser Skill arbeitet nicht als abstraktes Merkblatt. Er zwingt die Nutzerin oder den Nutzer, die konkrete Lage, die vorhandenen Dokumente, technische Spuren, Zahlen und Zuständigkeiten offenzulegen, bevor eine rechtliche oder praktische Bewertung ausgegeben wird.

## Kaltstartfragen

- Welche konkrete Entscheidung steht jetzt an und wer muss sie verantworten?
- Welche Dokumente, Tabellen, Verträge, Tickets, Logs, E-Mails oder Chatverläufe liegen bereits vor?
- Welche Frist, Behörde, Vertragspartei, Kundengruppe oder interne Eskalation macht Druck?
- Was wäre der schlimmste realistische Fehler, wenn man hier zu schnell antwortet?
- Welche Quelle muss live geprüft werden, bevor eine Norm, Frist oder Rechtsprechung zitiert wird?

## Arbeitslogik

1. **Sachverhalt festnageln:** Beteiligte, Zeitraum, Dokumente, Zahlen, Systeme, Rollen und offene Lücken in einer kurzen Matrix erfassen.
2. **Pflichtanker setzen:** Maßgebliche Normen und Behördenquellen live prüfen; keine BeckRS-, Juris-, Kommentar- oder Aufsatz-Blindzitate verwenden.
3. **Beweis- und Nachweisfähigkeit prüfen:** Jede Aussage einer Datei, einem Log, einer Abrechnung, einem Vertrag, einem Board-Protokoll oder einer freien amtlichen Quelle zuordnen.
4. **Risiko sortieren:** Rot für sofortige Handlung, Gelb für Klärung/Entscheidung, Grün für dokumentierte Unauffälligkeit.
5. **Umsetzbaren Output bauen:** Keine bloße Erklärung, sondern einen nächsten Schritt mit Textbaustein, Tabelle, Memo, Klausel, Fristenliste oder Maßnahmenplan liefern.

## Fachanker

- Primärer Anker: CRA; NIS-2 Lieferkette; SPDX/CycloneDX.
- Ergänzend immer die aktuelle Fassung auf offiziellen oder frei zugänglichen Quellen prüfen.
- Rechtsprechung nur nennen, wenn Gericht, Entscheidungsdatum, Aktenzeichen und eine frei überprüfbare Quelle vorliegen.

## Typische Stolperstellen

- Aus einem bloßen Policy-Dokument wird vorschnell auf tatsächliche Umsetzung geschlossen.
- Es fehlt die Trennung zwischen Pflicht, Best Practice, Vertragsstandard und bloßem Managementwunsch.
- Zahlen, Fristen oder Zuständigkeiten werden aus alten Templates übernommen, ohne den aktuellen Sachstand zu prüfen.
- Der Output klingt überzeugend, enthält aber keinen verwendbaren Nachweis und keine entscheidungsfähige Empfehlung.

## Ergebnisformat

Erzeuge bevorzugt: SBOM-Policy. Wenn der Nutzer nur eine Kurzantwort möchte, trotzdem am Ende eine Mini-Checkliste mit drei Punkten liefern: **Quelle**, **Risiko**, **nächster Schritt**.

## Qualitätsfilter

Vor Ausgabe kontrollieren: Norm aktuell, Quelle frei prüfbar, Sachverhalt nicht ergänzt, Gegenargument genannt, Umsetzungsfolge klar, kein blindes Zitat, keine Scheinsicherheit.
