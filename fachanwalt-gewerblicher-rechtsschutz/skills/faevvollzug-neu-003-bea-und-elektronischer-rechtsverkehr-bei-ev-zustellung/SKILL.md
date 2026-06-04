---
name: faevvollzug-neu-003-bea-und-elektronischer-rechtsverkehr-bei-ev
description: "BeA und elektronischer Rechtsverkehr bei EV-Zustellung: ERVV, § 130a ZPO, sichere Übermittlungswege, qualifizierte elektronische Signatur, Einreichung über beA bei einstweiligen Verfügungen im gewerblichen Rechtsschutz."
---

# BeA und Elektronischer Rechtsverkehr bei EV-Zustellung

## Aufgabe
Dieser Skill behandelt den elektronischen Rechtsverkehr (ERV) beim Einreichen und Zustellen von einstweiligen Verfügungen: beA (besonderes elektronisches Anwaltspostfach), ERVV, sichere Übermittlungswege und Formvorschriften.

## Rechtsrahmen

| Norm | Inhalt |
|---|---|
| § 130a ZPO | Elektronisches Dokument: Form, Signatur, sichere Übermittlung |
| § 130d ZPO | Nutzungspflicht ERV für Rechtsanwälte ab 1. Januar 2022 |
| ERVV (Elektronischer-Rechtsverkehr-Verordnung) | Technische Standards, zugelassene Übermittlungswege |
| § 174 Abs. 3 ZPO | Elektronische Zustellung an Anwälte über beA |
| § 195 ZPO | Anwaltliche Zustellung: Empfangsbekenntnis |
| § 182 ZPO | Zustellungsurkunde (bei Gerichtsvollzieher-Zustellung) |
| § 929 Abs. 2 ZPO | Vollziehungsfrist 1 Monat |
| BORA § 14 | Pflicht zur Nutzung des beA |

## Elektronische Einreichung beim Gericht

### Pflicht und Technik
- **Nutzungspflicht:** Anwälte sind seit 1.1.2022 verpflichtet, Schriftsätze über sichere Übermittlungswege einzureichen (§ 130d ZPO).
- **Sichere Übermittlungswege (§ 130a Abs. 4 ZPO):**
  - beA (besonderes elektronisches Anwaltspostfach) – Standard für Anwälte.
  - beBPo (besonderes elektronisches Behördenpostfach).
  - EGVP-Client mit Zertifikat.
- **Signaturpflichten:**
  - Qualifizierte elektronische Signatur (QES) des Verfassers, oder
  - Einfache Signatur + sicherer Übermittlungsweg (§ 130a Abs. 3 ZPO: „einfache Signatur" = Name im Dokument).

### EV-Antrag über beA einreichen
1. PDF-Datei erstellen (Schriftsatz + Anlagen als Anhänge).
2. beA öffnen, Empfänger = Gerichts-SAFE-ID des zuständigen Gerichts.
3. Nachricht mit Betreff „EV-Antrag Az. [Az.]" senden.
4. Sendeprotokoll und Eingangsbestätigung sichern.
5. Sofortiger Rückruf bei Sendeproblemen und Notfalleinreichung (Fax, persönlich) dokumentieren.

## Elektronische Zustellung zwischen Anwälten

### § 195 ZPO – Anwaltliche Zustellung
- Antragsteller-Anwalt stellt über beA direkt an beA des Gegner-Anwalts zu.
- Empfangsbekenntnis (EB) erforderlich: Antwort-Nachricht mit Datum des Empfangs.
- Wichtig: EB-Datum = Zustelldatum für Fristberechnung (§ 174 Abs. 4 ZPO).

### Protokoll anwaltliche Zustellung (Vorlage)
```
Empfangsbekenntnis gemäß § 174 Abs. 4 ZPO

Ich/Wir bestätigen den Empfang der nachbezeichneten Schriftstücke:
Beschluss des [Gericht] vom [Datum], Az. [Az.]

Datum des Empfangs (= Zustellungsdatum): [Datum]
[Unterschrift / Stempel der empfangenden Kanzlei]
```

## Häufige Fehler und Fallstricke

| Fehler | Folge | Vermeidung |
|---|---|---|
| Kein Sendeprotokoll gesichert | Vollziehungsnachweis fehlt | Immer PDF-Protokoll aus beA sichern |
| QES vergessen bei formgebundenen Anlagen | Zurückweisung | Signaturcheck vor Versand |
| EB nicht eingeholt | Zustellung streitig | Empfangsaufforderung per beA direkt schicken |
| Notfalleinreichung per Fax ohne Aktennotiz | Beweis- und Haftungsrisiko | Notfalleinreichung sofort dokumentieren |
| Falscher SAFE-ID-Empfänger | Fehlleitung | SAFE-ID des zuständigen Spruchkörpers vorab im Gerichtsregister prüfen |

## Notfallplan bei beA-Ausfall

1. Technische Störung dokumentieren (Screenshot der Fehlermeldung mit Zeitstempel).
2. Alternative Einreichung: Fax oder persönliche Abgabe bei Gericht mit Eingangsstempel.
3. Unverzüglich Notfalleinreichung der Ersatzform beim Gericht nachweisen (§ 130d Satz 2 ZPO: nur bei technischer Unmöglichkeit).
4. Glaubhaftmachung der Unmöglichkeit in separatem Schriftsatz.

## Kaltstart
1. Ist der Schriftsatz bereits fertig und liegt als PDF vor?
2. Welches Gericht (SAFE-ID des Spruchkörpers bekannt)?
3. Soll die Zustellung über beA an gegnerischen Anwalt erfolgen?
4. Liegt ein EB vor oder muss es noch eingeholt werden?
5. Welcher Output: Einreichungsprotokoll, EB-Vorlage, Notfallprotokoll?

## Anschluss-Skills
- `faevvollzug-neu-001-ev-vollziehungscheck-dringlichkeit-titel-zustellung` – Vollziehungsfristen.
- `faevvollzug-neu-002-parteibetrieb-und-gerichtsvollzieher-bei-unterlassungstiteln` – GV-Zustellung.
- `workflow-fristen-und-risikoampel` – Fristenübersicht.

## Quellenregel
- Normen: [gesetze-im-internet.de](https://www.gesetze-im-internet.de) (ZPO, ERVV).
- beA-Informationen: [bea.brak.de](https://www.bea.brak.de).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Was dieser Skill nicht macht
- Kein technischer IT-Support für beA-Softwareprobleme.
- Keine Garantie für aktuelle SAFE-IDs (live im EGVP-Adressbuch prüfen).
- Keine vollständige Mandantenberatung.
