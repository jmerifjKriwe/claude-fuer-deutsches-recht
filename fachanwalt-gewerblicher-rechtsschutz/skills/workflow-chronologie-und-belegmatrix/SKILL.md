---
name: workflow-chronologie-und-belegmatrix
description: "Chronologie und Belegmatrix im gewerblichen Rechtsschutz: Zeitachse aufbauen, Dokumente chronologisch sortieren, Lücken identifizieren, Beweiskette strukturieren für Verletzungsverfahren, EV, Klagschrift und Mandantenakte."
---

# Chronologie und Belegmatrix

## Aufgabe
Dieser Workflow-Skill hilft beim strukturierten Aufbau der Zeitachse und Belegmatrix: Sachverhalts-Chronologie, Dokumentenordnung und Beweiskette für anwaltliche Verfahren im gewerblichen Rechtsschutz.

## Warum Chronologie und Belegmatrix?

Eine präzise Zeitachse und lückenlose Belegmatrix sind die Basis für:
- **EV-Anträge:** Glaubhaftmachung des Kenntnisdatums (Dringlichkeit); Verletzungsdatum.
- **Klagschriften:** Lückenloser Sachverhaltsvortrag nach § 253 ZPO.
- **Schadensersatzberechnung:** Verletzungszeitraum, Mengen, Umsätze.
- **Widerspruchs- / Löschungsverfahren:** Prioritätsdaten, Erstbenutzungsdaten.
- **Mandantenkommunikation:** Nachvollziehbare Aktenlage für Übergabe.

## Chronologie-Schema

```
[Datum]  Ereignis             Dokument / Beleg        Status
─────────────────────────────────────────────────────────────
[Anmeldetag]  Schutzrecht angemeldet    DPMA-Eingangsbeleg     ✓ vorhanden
[Eintragungs-  Schutzrecht eingetragen  Registerauszug DPMA   ✓ vorhanden
 datum]
[Datum]  Verletzungshandlung  Screenshot URL+Datum    ✓ vorhanden
         erstmalig erkannt
[Datum]  Kenntnis Mandant     E-Mail Mandant an Kanzlei ✓ vorhanden
[Datum]  Beweissicherung      Testkauf mit Quittung   ✓ vorhanden
[Datum]  Abmahnung versandt   Einschreiben-Rückschein ✓ vorhanden
[Datum]  Frist Abmahnung      Fristkalender           ✓ offen
[Datum]  Reaktion Gegenseite  UE / Ablehnung / Keine  ○ ausstehend
[Datum]  EV-Antrag            beA-Sendeprotokoll      ○ ausstehend
```

## Belegmatrix

| Nr. | Dokument | Datum | Bezug im Vortrag | Format | Vorhanden? |
|---|---|---|---|---|---|
| 1 | Registerauszug DPMA | [Datum] | Schutzrecht aktiv | PDF | ✓ |
| 2 | Screenshot Verletzung | [Datum] | Verletzungshandlung | PNG/PDF | ✓ |
| 3 | Testkauf-Quittung | [Datum] | Beweissicherung | Original | ✓ |
| 4 | E-Mail Mandant (Kenntnis) | [Datum] | Dringlichkeit | PDF | ✓ |
| 5 | Abmahnung (Entwurf / Kopie) | [Datum] | Abmahnvoraussetzung | PDF | ✓ |
| 6 | Rückschein / beA-Protokoll | [Datum] | Zustellungsnachweis | Scan | ○ |
| 7 | Eidesstattliche Versicherung | [Datum] | Glaubhaftmachung | Original | ○ |
| 8 | UE der Gegenseite | [Datum] | Wiederholungsgefahr | Original | ○ |
| … | … | … | … | … | ○ |

## Lückenidentifikation

Häufige Dokumentenlücken und Schließungsstrategie:

| Lücke | Schließung |
|---|---|
| Kein Nachweis Erstbenutzung Marke | Alte Rechnungen, Kataloge, Fotos mit Datum beschaffen |
| Verletzungsdatum unklar | Wayback Machine ([web.archive.org](https://web.archive.org)); Notarprotokoll |
| Kenntnisdatum nicht dokumentiert | E-Mail-Korrespondenz suchen; Zeugen befragen; eV Mandant |
| Registerauszug veraltet | Aktuell herunterladen (DPMA-Online); Datum im Auszug sichtbar |
| Testkauf nicht organisiert | Sofortiger Testkauf mit Quittung, Versandbestätigung |
| Schutzschrift (ZSSR) nicht geprüft | [zssr.de](https://www.zssr.de) sofort prüfen |

## Checkliste Chronologie

| Schritt | Erledigt? |
|---|---|
| Anmeldetag / Entstehungsdatum Schutzrecht dokumentiert | ☐ |
| Eintragungsdatum und Verlängerungen im Register | ☐ |
| Erstbenutzungsdatum belegt (§ 4 Nr. 2, § 26 MarkenG) | ☐ |
| Verletzungsdatum und -ort konkret und datiert | ☐ |
| Kenntnisdatum Mandant belegt (Dringlichkeit EV) | ☐ |
| Beweissicherung vollständig (Testkauf, Screenshots) | ☐ |
| Abmahnungsdatum und Zustellungsnachweis | ☐ |
| Reaktion Gegenseite protokolliert | ☐ |
| Verfahrensdaten (EV, Klage) eingetragen | ☐ |

## Anwendungsbeispiel: Markenverletzung

```
Zeitachse Markenverletzung

2020-03-15  Marke "BEISPIEL" beim DPMA angemeldet (Aktenzeichen [XX])
2020-09-01  Eintragung; Registerauszug vom 2020-09-01 vorhanden
2023-11-12  Website Gegenseite: Zeichen "BEISPIEL" auf Startseite entdeckt
            → Beleg: Screenshot Anlage 1 (URL, Datum)
2023-11-12  Mandant informiert Kanzlei via E-Mail
            → Beleg: E-Mail-Ausdruck Anlage 2
2023-11-14  Testkauf von verletzendem Produkt
            → Beleg: Quittung, Foto, eV Anlage 3
2023-11-17  Abmahnung versandt per Einschreiben + beA
            → Beleg: Rückschein, beA-Protokoll Anlage 4
2023-11-24  Fristablauf (10 Tage UE-Frist)
2023-11-25  EV-Antrag beim LG Hamburg
```

## Kaltstart
1. Welcher Fall liegt vor und in welchem Stadium?
2. Welche Dokumente sind bereits vorhanden?
3. Wo sind Lücken in der Zeitachse?
4. Für welchen Zweck wird die Chronologie benötigt (EV / Klageschrift / Mandantenbrief)?
5. Output: Zeitachse aufgefüllt, Belegmatrix, Lückenliste, nächster Schritt?

## Anschluss-Skills
- `workflow-dokumentenintake` – Dokumentenerfassung.
- `spezial-gewerblichen-tatbestand-beweis-und-belege` – Beweismitteldetails.
- `faevvollzug-neu-008-qualitaetsgate-vor-vollziehung` – Qualitätsgate EV.

## Quellenregel
- Normen: [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Wayback Machine: [web.archive.org](https://web.archive.org).
- ZSSR: [zssr.de](https://www.zssr.de).
- Register: [dpma.de](https://www.dpma.de), [euipo.europa.eu](https://euipo.europa.eu).
- Keine BeckRS-, juris- oder Kommentar-Blindzitate aus Modellwissen.
- Annahmen und Lücken ausdrücklich markieren.

## Was dieser Skill nicht macht
- Keine Bewertung ohne vollständige Zeitachse.
- Kein Ersatz für vollständige Mandantenberatung.
