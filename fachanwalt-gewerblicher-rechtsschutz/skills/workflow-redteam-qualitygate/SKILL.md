---
name: workflow-redteam-qualitygate
description: "Red-Team und Qualitätsgate für alle Arbeitsprodukte im gewerblichen Rechtsschutz: Schwachstellenanalyse von Schriftsätzen, Memos, Abmahnungen, EV-Anträgen und Vergleichsentwürfen. Kritische Gegenfragen und Freigabekriterien."
---

# Red-Team und Qualitätsgate

## Aufgabe
Dieser Workflow-Skill führt ein systematisches Red-Team-Review durch: Er sucht Schwächen, Lücken und logische Fehler in Arbeitsprodukten, bevor sie nach außen gehen oder für Entscheidungen verwendet werden.

## Warum Red-Team im IP-Recht?

Fehler in anwaltlichen Arbeitsprodukten haben gravierende Folgen:
- **Schriftsätze:** Klageabweisung durch schlechten Sachvortrag oder Formfehler.
- **EV-Anträge:** § 945 ZPO-Haftung bei ungerechtfertigter EV.
- **Abmahnungen:** Missbräuchliche Abmahnung § 8c UWG; Kostenerstattungspflicht.
- **Vergleichsverträge:** Unklare Klauseln führen zu neuem Streit.
- **Rechtsquellenangaben:** Falsche AZ oder überholte Normen schädigen die Reputation.

## Red-Team-Fragen nach Dokumenttyp

### Abmahnung

| Frage | Prüfergebnis |
|---|---|
| Schutzrecht aktiv und eingetragen? | |
| Beanstandete Handlung konkret und datiert? | |
| UWG: § 13 Abs. 2-Anforderungen vollständig? | |
| Aktivlegitimation belegt? | |
| UE-Muster beigefügt und ausreichend weit? | |
| Vertragsstrafe angemessen (kein § 8c UWG)? | |
| Kostenerstattungsanspruch korrekt berechnet? | |
| Frist realistisch (Dringlichkeit vs. Reaktionszeit)? | |

### EV-Antrag

| Frage | Prüfergebnis |
|---|---|
| Verfügungsanspruch: alle Tatbestandsmerkmale? | |
| Verfügungsgrund: Dringlichkeit noch nicht selbst widerlegt? | |
| Eidesstattliche Versicherung unterschrieben? | |
| Anlagen vollständig nummeriert und beschrieben? | |
| § 945 ZPO-Risiko abgewogen? | |
| Schutzschrift ZSSR geprüft? | |
| Ordnungsmittelhinweis im Tenor? | |
| Streitwert realistisch? | |

### Schriftsatz (Klage / Berufung)

| Frage | Prüfergebnis |
|---|---|
| Rubrum vollständig (Parteien, Gericht)? | |
| Klageanträge vollständig und bestimmt (§ 253 ZPO)? | |
| Sachverhalt lückenlos, chronologisch, ohne Lücken? | |
| Normen aktuell und richtig zitiert? | |
| Beweisangebote vollständig (je Tatsachenbehauptung)? | |
| Keine unverifizierten Urteile? | |
| Kostenantrag enthalten? | |
| ERV-Pflicht beachtet (§ 130d ZPO)? | |

### Memo / Prüfvermerk

| Frage | Prüfergebnis |
|---|---|
| Gutachtenstil korrekt (Obersatz, Definition, Subsumtion)? | |
| Alle relevanten Normen berücksichtigt? | |
| Gegenauffassung / Gegenargumente erwähnt? | |
| Annahmen als solche gekennzeichnet? | |
| Handlungsempfehlung konkret (mit Frist und Verantwortlichen)? | |
| Quellen live verifiziert oder als „zu prüfen" markiert? | |

### Vergleichsentwurf

| Frage | Prüfergebnis |
|---|---|
| Parteien korrekt bezeichnet? | |
| Erledigungsklausel ausreichend weit / eng formuliert? | |
| Vertragsstrafe-Klausel enthalten (wenn Unterlassung fortbesteht)? | |
| Geheimhaltungsklausel eingeschlossen (wenn gewünscht)? | |
| Kostenregelung eindeutig? | |
| GWB / Art. 101 AEUV: Wettbewerbsrechtliche Grenzen geprüft? | |

## Freigabekriterien

Ein Arbeitsprodukt wird freigegeben, wenn:

| Kriterium | Erfüllt? |
|---|---|
| Alle MUSS-Prüfpunkte mit OK bewertet | ☐ |
| Keine offenen Live-Check-Punkte bei tragenden Aussagen | ☐ |
| Annahmen klar markiert | ☐ |
| Mandantenfreigabe eingeholt (bei Außenkommunikation) | ☐ |
| Fristen berechnet und Kalender eingetragen | ☐ |

## Ampel-Bewertung Red-Team

| Ampel | Bedeutung |
|---|---|
| 🟢 Grün | Alle Prüfpunkte OK; Freigabe |
| 🟡 Gelb | 1–2 Punkte offen; Nacharbeit nötig, aber kein K.O.-Kriterium |
| 🔴 Rot | K.O.-Kriterium offen (z.B. Schutzrecht abgelaufen; keine eV); Dokument nicht freigeben |

## Kaltstart
1. Welches Dokument soll reviewed werden (Abmahnung / EV-Antrag / Schriftsatz / Memo / Vergleich)?
2. Liegt das Dokument als Text vor?
3. Gibt es bereits bekannte Schwachstellen?
4. Soll nur eine Checkliste ausgefüllt oder ein vollständiges Review durchgeführt werden?
5. Output: Red-Team-Checkliste ausgefüllt, Ampel-Bewertung, Verbesserungsvorschläge?

## Anschluss-Skills
- `faevvollzug-neu-008-qualitaetsgate-vor-vollziehung` – Qualitätsgate EV-Vollziehung.
- `spezial-designverletzung-red-team-und-qualitaetskontrolle` – Red-Team Design.
- `workflow-rechtsquellen-livecheck` – Quellen-Verifikation.

## Quellenregel
- Dieser Skill bewertet Inhalte; Normen und Urteile werden im Review auf Live-Verifizierung geprüft.
- Quellen: [gesetze-im-internet.de](https://www.gesetze-im-internet.de), [dejure.org](https://dejure.org), [bgh.de](https://www.bundesgerichtshof.de).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.

## Was dieser Skill nicht macht
- Kein inhaltliches Tiefenreview ohne vollständiges Dokument.
- Kein Ersatz für vollständige anwaltliche Prüfung.
