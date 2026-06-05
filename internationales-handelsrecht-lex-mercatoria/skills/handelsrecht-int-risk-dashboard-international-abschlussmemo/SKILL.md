---
name: handelsrecht-int-risk-dashboard-international-abschlussmemo
description: "INT Risk Dashboard International Abschlussmemo im Plugin Internationales Handelsrecht Lex Mercatoria: prüft konkret Internationales Handelsrecht. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# INT Risk Dashboard International Abschlussmemo

## Arbeitsbereich

Dieser Skill behandelt **INT Risk Dashboard International Abschlussmemo** als zusammenhängenden Arbeitsgang im Plugin Internationales Handelsrecht Lex Mercatoria. Im Mittelpunkt steht die Prüfung von Internationales Handelsrecht und weiteren verwandten Aspekten. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `ihl-091-risk-dashboard-international-trade` | Internationales Handelsrecht: Risiko-Dashboard für internationale Handelsgeschäfte. Länder-, Währungs-, Lieferanten-, Rechtsdurchsetzungs- und Compliance-Risiken im Überblick. Ampelsystem, Priorisierung und Handlungsempfehlungen. |
| `ihl-092-abschlussmemo-handelsrecht` | Internationales Handelsrecht: Abschlussmemo nach Verhandlung oder Prüfung eines internationalen Handelsfalls. Struktur, Wesentlichkeitsprinzip, Ergebnisdarstellung, Risikobewertung und Board-taugliche Formulierung. |
| `ihl-093-vertiefung-01-quellenmatrix` | Internationales Handelsrecht: Quellenmatrix für internationale Handelsfälle. Systematisierung von Primär- (CISG, PICC, Incoterms, UCP 600), Sekundär- und Tertiärquellen, Datenbanken (CISG-online, jusmundi, trans-lex), Zitierpflichten und Verifikation. |
| `ihl-094-vertiefung-01-streitstand-ohne-blindzitat` | Internationales Handelsrecht: Darstellung von Streitständen ohne Blindzitate. Methodik für kontroverse CISG-Fragen (Art. 55, Art. 35 öffentl.-rechtl. Anforderungen, CISG für Softwareverträge), Schiedsgerichts-Divergenz und Evidenz-basierte Positionierung. |

## Arbeitsweg

- Rolle und Ziel im Internationales Handelsrecht Lex Mercatoria klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: HGB §§ 1-7, 17-37 (Firma/Register), 48-58 (Prokura), 84-92c (Handelsvertreter), 343 ff. (Handelsgeschäfte), 373 ff. (Handelskauf); CISG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `ihl-091-risk-dashboard-international-trade`

**Fokus:** Internationales Handelsrecht: Risiko-Dashboard für internationale Handelsgeschäfte. Länder-, Währungs-, Lieferanten-, Rechtsdurchsetzungs- und Compliance-Risiken im Überblick. Ampelsystem, Priorisierung und Handlungsempfehlungen.

# Risiko-Dashboard Internationaler Handel

## Worum es geht

Ein systematisches Risiko-Dashboard für internationale Handelsgeschäfte aggregiert Länderrisiko (politisch, wirtschaftlich), Gegenpartei-Risiko, Rechtsrisiko (Durchsetzbarkeit, Gerichtsstand, Schiedsort) und Compliance-Risiko (Exportkontrolle, Sanktionen, Korruption). Es dient als Entscheidungshilfe für Führungsgremien.

## Kernnormen / Kernquellen

- **OECD Country Risk Classification**: Länderbewertung für Exportkreditversicherung (1-7)
- **Euler Hermes (Allianz Trade)**: Länderrisikobewertungen A1-D
- **OFAC Country Programs**: US-Sanktionsländerliste
- **Transparency International CPI**: Korruptionswahrnehmungsindex
- **World Bank ICRG**: International Country Risk Guide
- **Export Credit Guarantee Scheme (Hermes-Deckung)**: Bundesdeckungen für Deutsche Exporteure

## Schlüsselbegriffe

- Länderrisiko: Zahlungsunfähigkeits- + politisches Transfer- + Konvertierungsrisiko
- Gegenparteirisiko: Bonitätsprüfung (KreditauskunfteI, Jahresabschlüsse, Trade References)
- Rechtsdurchsetzungsrisiko: NY-Convention-Mitgliedschaft + Schiedsrecht + Justizqualität
- Sanktions-Compliance-Risiko: Sanktionsstatus des Landes, der Gegenpartei, der Güter
- ESG-Risiko: LkSG/CSDDD-Exposur + Reputationsrisiko

## Typische Streitfragen / Anwendungsfälle

1. Neues Land: Wie schnell erstelle ich ein Länderprofil für ein unbekanntes Handelsland?
2. Gegenpartei-Screening: Welche Datenbanken für Bonitäts- und Sanctions-Check?
3. Rechtsdurchsetzungs-Score: Wie bewerte ich Schiedsgerichtsbarkeits-Qualität eines Landes?
4. LkSG-ESG-Risiko: Wie kommt ESG-Risiko ins Dashboard ohne übertriebenen Aufwand?
5. Aggregation: Wie gewichte ich die verschiedenen Risikodimensionen zu einem Gesamtscore?

## Methodik

- Dashboard-Dimensionen: (1) Länder/Politisch, (2) Wirtschaftlich/Währung, (3) Gegenpartei, (4) Recht, (5) Compliance
- Ampelsystem: Rot (kein Geschäft ohne besondere Maßnahmen), Gelb (Monitoring), Grün (Standard)
- Datenquellen: OECD, OFAC, TI CPI, Euler Hermes, World Bank Doing Business-Nachfolger
- Aktualisierung: Quartalsweise oder bei kritischen Ereignissen (Wahlen, Sanktionen, Insolvenz)

## Output

- Risiko-Dashboard-Template (5 Dimensionen × Ampel)
- Länderprofil-Kurzanalyse-Schema
- Datenquellen-Matrix (Kostenlos vs. kostenpflichtig)

## Quellenregel

OECD Country Risk: oecd.org. TI CPI: transparency.org. OFAC: home.treasury.gov. World Bank: worldbank.org. Euler Hermes: allianz-trade.com. Unsicherheit bleibt sichtbar.

## 2. `ihl-092-abschlussmemo-handelsrecht`

**Fokus:** Internationales Handelsrecht: Abschlussmemo nach Verhandlung oder Prüfung eines internationalen Handelsfalls. Struktur, Wesentlichkeitsprinzip, Ergebnisdarstellung, Risikobewertung und Board-taugliche Formulierung.

# Abschlussmemo Internationales Handelsrecht

## Worum es geht

Das rechtliche Abschlussmemo fasst Ergebnisse einer Prüfung eines internationalen Handelsvertrags oder -falls zusammen: anwendbares Recht, wesentliche Risiken, Empfehlungen und nächste Schritte. Es richtet sich an interne oder externe Entscheidungsträger (Rechtsabteilung, Vorstand, Verhandlungsteam).

## Kernnormen / Kernquellen

- **Wesentlichkeitsprinzip**: Nur Risiken ab einer definierten Schwelle werden reportet
- **CISG Art. 25**: Wesentliche Verletzung als Risikokriterium
- **ICC Schiedsregeln Art. 31**: Begründungspflicht des Schiedsgerichts als Memo-Vorbild
- **LkSG § 10**: Dokumentation der Sorgfaltspflichterfüllung — Memo als Compliance-Nachweis
- **Art. 1699 ff. Code Civil (Frankreich)**: Cession de créance — ggf. Recht des Ziellandes

## Schlüsselbegriffe

- Executive Summary: 3-5 Sätze Gesamtbewertung und Handlungsempfehlung
- Risikoampel: Rot/Gelb/Grün mit numerischer Bewertung (Eintrittswahrscheinlichkeit × Schadenshöhe)
- Aktionsplan: Konkrete nächste Schritte mit Verantwortlichkeit und Deadline
- Quellenmatrix: alle zitierten Normen, Verträge, Urteile nachvollziehbar dokumentiert
- Unsicherheitsvermerk: Bereiche wo Rechtslage unklar ist explizit benennen

## Typische Streitfragen / Anwendungsfälle

1. Memo-Format: Einseiter vs. detailliertes Memo — wann welches für Vorstand?
2. Risikobewertung: Wie kommt man zu einer objektiv vertretbaren Risikoampel?
3. Confidentialität: Wie internes Memo vor Discovery-Offenlegung schützen (Anwaltsprivileg)?
4. Quellennachweis: Muss jede CISG-Stelle im Memo mit Fundstelle belegt werden?
5. Update: Wann muss Abschlussmemo aktualisiert werden (Rechtsänderung, neue Rspr.)?

## Methodik

- Memo-Struktur: (1) Executive Summary, (2) Sachverhalt, (3) Rechtliche Analyse, (4) Risiken, (5) Empfehlungen
- Quellenmatrix: Anhang mit allen verwendeten Quellen (Norm, Gericht, Datum, Fundstelle)
- Wesentlichkeit: Risiken unter EUR 50.000 oder unter 5% Vertragsrisiko in Anhang
- Unsicherheit: immer sichtbar lassen — kein unqualifiziertes "ist rechtmäßig"

## Output

- Abschlussmemo-Template (international, CISG-Fokus)
- Risikoampel-Kalkulationsschema
- Quellenmatrix-Vorlage

## Quellenregel

CISG: uncitral.un.org. ICC Regeln 2021: iccwbo.org. LkSG: gesetze-im-internet.de. Schrifttum: Praxis-Handbücher (Anwaltsverlag). Unsicherheit bleibt sichtbar.

## 3. `ihl-093-vertiefung-01-quellenmatrix`

**Fokus:** Internationales Handelsrecht: Quellenmatrix für internationale Handelsfälle. Systematisierung von Primär- (CISG, PICC, Incoterms, UCP 600), Sekundär- und Tertiärquellen, Datenbanken (CISG-online, jusmundi, trans-lex), Zitierpflichten und Verifikation.

# Quellenmatrix Internationales Handelsrecht

## Worum es geht

Eine strukturierte Quellenmatrix systematisiert die relevanten Quellen für internationale Handelsfälle nach Geltungskraft (verbindlich/nicht-verbindlich), Zugänglichkeit und Aktualität. Primärquellen sind Vertragstext, Gesetze und Übereinkommen; Sekundärquellen sind Kommentare und Gutachten; Tertiärquellen Schiedsspruch-Datenbanken und Lehrwerke.

## Kernnormen / Kernquellen

- **uncitral.un.org**: CISG, MLETR, Model Law Schiedsgerichtsbarkeit, UNCITRAL Digest of CISG
- **unidroit.org**: PICC 2016, Kommentare, Case Law Database
- **iccwbo.org**: Incoterms 2020, UCP 600, URDG 758, ICC Regeln 2021, Opinions
- **trans-lex.org (CENTRAL)**: Transnational Law Principles mit Schiedsreferenzen
- **jusmundi.com**: Internationale Schiedssprüche (ICC, LCIA, ICSID — transparente Awards)
- **eur-lex.europa.eu**: EU-Sekundärrecht (Rom I, Brüssel Ia, Dual-Use-VO, Sanktionen)

## Schlüsselbegriffe

- Verbindliche Quellen: ratifizierte Übereinkommen, nationales Recht, Vertragsklauseln
- Soft Law: PICC, Incoterms, UCP 600 — nur verbindlich durch Parteivereinbarung
- Schiedssprüche: kein Präzedenzwert aber überzeugend (persuasive authority)
- UNCITRAL Digest: offizielle Zusammenfassung von CISG-Rechtsprechung (kostenlos)
- CISG-online.ch: Universität Basel — größte CISG-Rechtsprechungsdatenbank

## Typische Streitfragen / Anwendungsfälle

1. Welche Quelle hat Vorrang: nationaler Kommentar oder CISG-Advisory-Council-Opinion?
2. jusmundi.com ICC-Schiedssprüche: Wie viele sind vertraulich und deshalb nicht verfügbar?
3. CENTRAL trans-lex.org: Wie zitiere ich ein Prinzip aus CENTRAL im Schiedsverfahren?
4. UNCITRAL Digest 2016: Ist er aktuell genug oder gibt es neuere Ergänzungen?
5. eur-lex.europa.eu: Wie finde ich konsolidierte Fassung einer EU-Verordnung schnell?

## Methodik

- Quellenrangordnung: (1) Vertragstext, (2) anwendbares Recht, (3) Soft Law, (4) Schiedssprüche, (5) Lit.
- Verifikation: jede Norm mit Fundstelle und Datum der Abrufung belegen
- Schiedssprüche: immer ICC-Award-Nummer und Jahr angeben; nicht nur Beschreibung
- Soft Law: explizit als nicht verbindlich kennzeichnen; Einbeziehungsnachweis prüfen

## Output

- Quellenmatrix-Template (Kategorien × Zugänglichkeit × Verbindlichkeit)
- Datenbanken-Kurzführer (URL, Inhalt, Kosten, Aktualisierung)
- Zitierstil-Leitfaden für internationale Handelsfälle

## Quellenregel

uncitral.un.org, unidroit.org, iccwbo.org, trans-lex.org, jusmundi.com, eur-lex.europa.eu, CISG-online.ch. Alle URLs mit Abrufdatum angeben. Unsicherheit bleibt sichtbar.

## 4. `ihl-094-vertiefung-01-streitstand-ohne-blindzitat`

**Fokus:** Internationales Handelsrecht: Darstellung von Streitständen ohne Blindzitate. Methodik für kontroverse CISG-Fragen (Art. 55, Art. 35 öffentl.-rechtl. Anforderungen, CISG für Softwareverträge), Schiedsgerichts-Divergenz und Evidenz-basierte Positionierung.

# Streitstandsdarstellung ohne Blindzitate

## Worum es geht

Internationale Handelsfälle enthalten viele ungelöste Rechtsfragen. Eine seriöse Streitstandsdarstellung nennt alle Positionen mit echten Belegen — keine Aussagen wie "nach herrschender Meinung" ohne Quelle. Besonders kontrovers: CISG Art. 55 (fehlender Preis), öffentlich-rechtliche Anforderungen nach Art. 35, und CISG-Anwendbarkeit auf Software.

## Kernnormen / Kernquellen

- **CISG Art. 14 vs. Art. 55**: Widerspruch zwischen Angebots-Bestimmtheit und Preis-Auffangnorm
- **CISG Art. 35 Abs. 2 lit. a**: Öffentlich-rechtliche Anforderungen — Verkäufer vs. Käuferland-Recht
- **CISG Art. 2 lit. d**: Anwendbarkeit auf Elektrizität; Software per Analogie?
- **PICC Art. 5.1.7**: Preis-Bestimmung bei Fehlen — Alternative zu CISG Art. 55
- **CISG Advisory Council Opinion No. 4**: Software und CISG
- **CISG-Rspr. BGH VIII ZR 136/01**: BGH zu öffentlich-rechtlichen Standards

## Schlüsselbegriffe

- Blindzitat: Behauptung einer "herrschenden Meinung" ohne benannte Quellen
- Minderheitsmeinung: auch wenn nur 10% der Schiedsgerichte so entscheiden — benennen
- Divergente Rechtsprechung: CISG-online.ch zeigt nationale und internationale Divergenzen
- Schiedsgerichtsbarkeit: keine formale Präzedenzwirkung — aber faktische Konvergenz
- Position A vs. B: strukturierte Gegenüberstellung mit je eigenen Quellen

## Typische Streitfragen / Forschungsfragen

1. CISG Art. 35 öffentlich-rechtliche Anforderungen: Was sagt BGH VIII ZR 136/01 genau?
2. Software-CISG: Welche Gerichte haben Pro/Contra entschieden (bitte mit Fundstelle)?
3. Art. 14 vs. Art. 55: Wie lösen Schiedsgerichte den scheinbaren Widerspruch?
4. CISG Advisory Council Opinion No. 4: Bindungswirkung vor Schiedsgericht?
5. Wie dokumentiere ich einen Streitstand ohne Aussagen zu machen die ich nicht belegen kann?

## Methodik

- Null-Blindzitat-Regel: jede Meinung mit Name des Verfechters und Quelle
- Streitstandsschema: Position A [Quelle 1, 2] vs. Position B [Quelle 3, 4] vs. Position C [...]
- CISG-online.ch: Länderrechtsprechung nach Art. 35 filtern; Divergenzen dokumentieren
- Schiedssprüche: jusmundi.com + CENTRAL trans-lex.org für Schiedsgerichtsstandpunkte

## Output

- Streitstandsschema-Template (3-Positionen-Matrix)
- Quellencheck-Checkliste gegen Blindzitate
- CISG-Hauptstreitfragen-Übersicht mit echten Belegen

## Quellenregel

CISG-online.ch, CISG Advisory Council Opinions (cisgac.com), jusmundi.com, uncitral.un.org. BGH: dejure.org. Alle Zitate mit Gericht, Datum, Aktenzeichen. Unsicherheit bleibt sichtbar.
