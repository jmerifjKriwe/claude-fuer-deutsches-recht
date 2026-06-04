---
name: faevvollzug-neu-008-qualitaetsgate-vor-vollziehung
description: "Qualitätsgate vor EV-Vollziehung: Letzter Check vor Zustellung der einstweiligen Verfügung. Titel, Dringlichkeit, Zustellungsweg, Schutzschrift, Kosten-Nutzen, Red-Team-Fragen, Rücknahmeoptionen im gewerblichen Rechtsschutz."
---

# Qualitätsgate vor EV-Vollziehung

## Aufgabe
Dieser Skill ist der letzte Qualitätscheck vor der Vollziehung einer einstweiligen Verfügung: Vollständigkeit des Titels, Dringlichkeit, Zustellungsweg, Red-Team-Analyse, Kostenrisiken und Rücknahmeoptionen.

## Warum dieses Qualitätsgate?

Die Vollziehung einer einstweiligen Verfügung ist reversibel kaum möglich. Vollzogene, aber fehlerhafte oder zu früh vollzogene Verfügungen können:
- Schadensersatzpflicht nach § 945 ZPO auslösen (bei ungerechtfertigter EV).
- Dringlichkeit durch späteres Zuwarten widerlegen.
- Kostenrisiken durch unnötige Eskalation schaffen.
- Verhandlungsposition verschlechtern.

## Red-Team-Fragen vor Vollziehung

**Zum Verfügungsanspruch:**
- Ist das Schutzrecht eingetragen / wirksam entstanden (Registerauszug geprüft)?
- Sind alle Anspruchsvoraussetzungen (Verwechslungsgefahr, Verletzungshandlung, Aktivlegitimation) sauber belegt?
- Gibt es Gegenrechte (Erschöpfung § 24 MarkenG, Prior Use, eigene ältere Schutzrechte der Gegenseite)?
- Hat die Gegenseite bereits eine Schutzschrift hinterlegt (ZSSR gecheckt)?

**Zum Verfügungsgrund:**
- Dringlichkeit noch unversehrt? Kenntnisdatum dokumentiert?
- Keine Selbstwiderlegung durch Zuwarten (Kammer-spezifische Frist beachten)?
- Dringlichkeit glaubhaft gemacht (§ 294 ZPO, eidesstattliche Versicherung)?

**Zum Titel:**
- Unterlassungsformulierung klar und vollstreckbar?
- Ordnungsmittelandrohung (§ 890 Abs. 2 ZPO) im Tenor?
- Vollstreckbare Ausfertigung vorhanden (§ 724 ZPO)?

**Zum Zustellungsweg:**
- Zustellungsform gewählt und Zustellungsadresse verifiziert?
- Vollziehungsfrist berechnet und eingetragen?

## Qualitätsgate-Checkliste

| Prüfpunkt | Status (Ja/Nein/Offen) | Priorität |
|---|---|---|
| Schutzrecht aktiv und eingetragen (Registerauszug DPMA/EUIPO) | ☐ | MUSS |
| Verletzungshandlung konkret dokumentiert (Datum, Form, Beweis) | ☐ | MUSS |
| Aktivlegitimation belegt (Inhaber / Lizenznehmer) | ☐ | MUSS |
| Schutzschrift ZSSR geprüft ([zssr.de](https://www.zssr.de)) | ☐ | MUSS |
| Dringlichkeit: Kenntnis-Datum belegt, Frist eingehalten | ☐ | MUSS |
| Titel mit Ordnungsmittelandrohung § 890 Abs. 2 ZPO | ☐ | MUSS |
| Vollstreckbare Ausfertigung vorhanden | ☐ | MUSS |
| Vollziehungsfrist berechnet (1 Monat § 929 Abs. 2 ZPO) | ☐ | MUSS |
| Zustellungsadresse verifiziert | ☐ | MUSS |
| Kosten-Nutzen-Analyse: Vollziehungskosten vs. Schutzinteresse | ☐ | SOLL |
| Gegenseite zur einvernehmlichen Lösung kontaktiert? | ☐ | KANN |
| Hauptsacheklage vorbereitet (falls EV scheitert) | ☐ | SOLL |

## § 945 ZPO – Schadensersatzrisiko

Wird die einstweilige Verfügung aufgehoben oder der Hauptsacheanspruch abgewiesen, hat der Antragsgegner Anspruch auf Schadensersatz gemäß § 945 ZPO – **ohne Verschulden** des Antragstellers (verschuldensunabhängig).

**Risikofaktoren für § 945 ZPO:**
- Anspruch war von Anfang an nicht begründet.
- Dringlichkeit war nicht gegeben (Selbstwiderlegung).
- Schutzrecht wurde nach EV für nichtig erklärt.

**Gegenmaßnahme:** Sorgfältige Prüfung vor Vollziehung; bei Zweifeln Abmahnung zuerst oder Aufhebungsrisiko einpreisen.

## Entscheidungsbaum Vollziehung

```
Alle MUSS-Punkte erfüllt?
  Nein → Nicht vollziehen; Lücken schließen
  Ja  →
        Gegenrechte (Erschöpfung, Prior Use) ausgeschlossen?
          Nein → Strategie neu bewerten; ggf. Abmahnung statt EV
          Ja  →
                § 945-Risiko vertretbar?
                  Nein → Mandantenfreigabe einholen
                  Ja  → Vollziehung durchführen
```

## Kaltstart
1. Liegt vollstreckbare Ausfertigung des Beschlusses vor?
2. Ist die Dringlichkeit noch unversehrt (Kenntnisdatum, Kammer-Frist)?
3. Schutzschrift beim ZSSR hinterlegt?
4. Welcher konkrete Punkt des Qualitätsgates ist unklar oder offen?
5. Output: Checkliste ausgefüllt, Risikomemo, Mandantenbrief, Entscheidungsvorlage?

## Anschluss-Skills
- `faevvollzug-neu-001-ev-vollziehungscheck-dringlichkeit-titel-zustellung` – Vollziehungsfristen.
- `faevvollzug-neu-005-gegnerische-schutzschrift-auswerten` – Schutzschrift-Analyse.
- `workflow-redteam-qualitygate` – Übergreifendes Red-Team-Gate.

## Quellenregel
- Normen: [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- ZSSR: [zssr.de](https://www.zssr.de).
- Rechtsprechung: [dejure.org](https://dejure.org), [bgh.de](https://www.bundesgerichtshof.de).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Was dieser Skill nicht macht
- Kein Ersatz für vollständige anwaltliche Prüfung.
- Keine Garantie gegen § 945 ZPO-Haftung (einzelfallabhängig).
