---
name: folgekorrespondenz-vorbereiten
description: "Bereitet einen Skeleton-Eintrag fuer CRM und Aktenanlage vor sodass die Sekretariatsmitarbeitende die Anfrage schnell weiterfuehren kann: Name Mail Telefon Anliegen-Stichwort Dringlichkeit Datum Sprachkennung Konfliktcheck-Status. Laedt wenn der Nutzer 'CRM Eintrag erstellen', 'Akte anlegen', 'Mandantenvorgang vorbereiten', 'Sekretariat Eintrag' oder 'Aktennotiz Erstanfrage' sagt."
---

# Folgekorrespondenz-Vorbereiten

Dieser Skill erstellt auf Basis der geparsten Eingangsanfrage einen fertigen Skeleton-Eintrag für das CRM-System oder die manuelle Aktenanlage. Ziel: Die Sekretariatsmitarbeitende kann den Vorgang sofort weiterführen, ohne Informationen erneut aus der Originalmail suchen zu müssen.

## Skeleton-Eintrag: Standardformat

```
=== NEUER VORGANG — ERSTANFRAGE ===
Eingangsdatum:     [DATUM UND UHRZEIT]
Eingangskanal:     E-Mail

--- KONTAKT ---
Name:              [NACHNAME, VORNAME] | [Titel falls vorhanden]
E-Mail:            [ABSENDER-ADRESSE]
Telefon:           [TELEFONNUMMER oder „nicht genannt"]
Postanschrift:     [ADRESSE oder „nicht genannt"]
Sprache:           [DE / EN / FR / IT / Sonstiges]

--- ANLIEGEN ---
Rechtsgebiet:      [Ersteinschätzung: z. B. Arbeitsrecht / Mietrecht / Strafrecht]
Stichwörter:       [Kommagetrennte Liste — max. 5 Begriffe]
Beteiligte:        [Gegner / Behörde / weitere Parteien oder „nicht genannt"]
Sachverhalt-Kurzfassung:
  [2-4 Sätze aus dem Parsing — wortwörtlich oder eng paraphrasiert]

--- DRINGLICHKEIT ---
Stufe:             [HOCH / MITTEL / NIEDRIG / UNBEKANNT]
Begründung:        [Frist, Termin, Eile-Signal oder „kein Hinweis"]
Massnahme:         [Sofortiger Anwaltsrückruf erforderlich / Normale Bearbeitung / Abwarten]

--- STATUS ---
Spam-Check:        [KLAR / VERDÄCHTIG / SPAM]
Konfliktcheck:     [AUSSTEHEND — vor Terminvergabe durchführen!]
Erstantwort:       [VERSENDET am DATUM / AUSSTEHEND]
Transkription:     [AKTIV / NICHT AKTIV]

--- INTERNE NOTIZEN ---
[Platz für manuelle Ergänzungen der Sekretariatsmitarbeitenden]

=== ENDE SKELETON-EINTRAG ===
```

## Felder im Detail

### Eingangsdatum und -kanal

- Automatisch befüllt mit dem aktuellen Zeitstempel (ISO 8601: `YYYY-MM-DD HH:MM`)
- Eingangskanal: E-Mail, Telefon, Kontaktformular, Post — für E-Mail-basierte Anfragen stets „E-Mail"

### Kontakt-Felder

Aus dem Parsing-Skill (`anfrage-eingang-parser`) übernommen. Fehlende Felder werden mit „nicht genannt" markiert und für manuelle Ergänzung hervorgehoben.

### Rechtsgebiet-Ersteinschätzung

**Wichtig:** Dies ist eine nicht-verbindliche Ersteinschätzung des Parsing-Algorithmus. Sie dient der Vorsortierung im Sekretariat und darf NICHT als rechtliche Einschätzung an die anfragende Person weitergegeben werden.

Mögliche Rechtsgebiete (Auswahl):
- Arbeitsrecht, Mietrecht, Familienrecht, Erbrecht, Strafrecht
- Gesellschaftsrecht, Vertragsrecht, Schadensersatz
- Verwaltungsrecht, Sozialrecht, Steuerrecht
- Verkehrsrecht, Insolvenzrecht, IP-Recht
- Sonstiges / Unbekannt

### Dringlichkeitsstufen

| Stufe | Beschreibung | Sofortmaßnahme |
|---|---|---|
| HOCH | Frist erkannt, Haftungsrisiko, bevorstehende Verhandlung | Anwalt ruft sofort zurück |
| MITTEL | Zeitdruck vorhanden, aber keine akute Frist | Rückmeldung innerhalb 24h |
| NIEDRIG | Kein Zeitdruck erkennbar | Rückmeldung im normalen Ablauf |
| UNBEKANNT | Keine Aussage zu Dringlichkeit möglich | Wie MITTEL behandeln |

### Konfliktcheck-Status

Standardmäßig: `AUSSTEHEND`. Die Sekretariatsmitarbeitende trägt nach Durchführung des Konfliktchecks ein:
- `KLAR — kein Konflikt erkannt` oder
- `KONFLIKT — Mandat nicht möglich` oder
- `KONFLIKT — Rücksprache mit RA erforderlich`

### Transkriptions-Status

- `AKTIV` wenn die anfragende Person den Transkriptionsservice nutzen soll/wird
- `NICHT AKTIV` bei Standardverfahren mit schriftlicher Sachverhaltsschilderung

## Integration in gängige CRM-Systeme

Dieser Skill gibt einen Text-basierten Skeleton aus, der in alle gängigen Systeme eingefügt werden kann:

- **RA-MICRO:** Als neue Akte anlegen; Felder manuell übertragen; Aktenzeichen generieren.
- **Advoware:** Neues Mandat anlegen; Kontaktdaten übertragen; Status auf „Erstanfrage" setzen.
- **DATEV Anwalt:** Neues Verfahren anlegen; Mandantenakte erstellen.
- **Eigenentwicklung / Excel:** Tabellenzeile; CSV-Import möglich.

## Ausgabe

```
SKELETON-EINTRAG BEREIT
Für CRM-System oder manuelle Akte kopieren und einfügen.
Ausstehende Felder sind mit [BITTE ERGÄNZEN] markiert.
Konfliktcheck: AUSSTEHEND — vor Terminvergabe durchführen!
```

## Verweise auf andere Skills

- `anfrage-eingang-parser` — Datenquelle
- `dringlichkeitsmarker` — Dringlichkeitsstufe und Begründung
- `spam-und-massen-anfrage-filter` — Spam-Check-Status
- `konfliktcheck-vorab` — Hinweis auf ausstehenden Konfliktcheck
