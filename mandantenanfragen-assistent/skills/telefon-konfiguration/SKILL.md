---
name: telefon-konfiguration
description: "Verwaltet die Telefonnummern der Kanzlei (Sekretariat und Transkriptionsservice) und setzt sie in die Antwort-Templates ein. Liest aus einer Platzhalter-Konfigurationsdatei kanzlei.json. Laedt wenn der Nutzer 'Telefonnummer konfigurieren', 'Kanzlei-Daten einstellen', 'Sekretariat-Nummer', 'Transkriptions-Telefon' oder 'kanzlei.json bearbeiten' sagt."
---

# Telefon-Konfiguration

Dieser Skill verwaltet die Kanzlei-spezifischen Kontaktdaten — insbesondere Telefonnummern — und stellt sicher, dass alle Antwort-Templates mit den aktuellen Daten befüllt werden.

## Platzhalter-Konfiguration: kanzlei.json

Die Kanzlei hinterlegt ihre Kontaktdaten in einer Datei `kanzlei.json`. Das Beispiel-Format:

```json
{
  "kanzlei": {
    "name": "[KANZLEI-NAME]",
    "adresse": {
      "strasse": "[STRASSE UND HAUSNUMMER]",
      "plz": "[POSTLEITZAHL]",
      "ort": "[ORT]"
    },
    "telefon_sekretariat": "[SEKRETARIATS-TELEFON]",
    "telefon_transkription": "[TRANSKRIPTIONS-TELEFON]",
    "erreichbarkeit": "[Z.B. Mo-Fr 09:00-17:00 Uhr]",
    "email_kanzlei": "[KANZLEI-E-MAIL]",
    "unterzeichnende_ra": "[VORNAME NACHNAME, Rechtsanwalt/Rechtsanwaeltin]",
    "rechtsanwaltsgesellschaft": "[FALLS ZUTREFFEND]"
  }
}
```

### Felder und Verwendung

| Feld | Beschreibung | Verwendung in |
|---|---|---|
| `name` | Vollständiger Kanzleiname | Briefkopf, Schlussformel, Fußzeile |
| `adresse` | Postanschrift der Kanzlei | Briefkopf, Fußzeile |
| `telefon_sekretariat` | Hauptnummer für Terminvergabe | Erstantwort-Body, Dringlichkeits-Hinweis |
| `telefon_transkription` | Nummer des Transkriptionsservices | Transkriptions-Abschnitt |
| `erreichbarkeit` | Bürozeiten | Erstantwort-Body |
| `email_kanzlei` | Haupt-E-Mail-Adresse | Briefkopf, Fußzeile |
| `unterzeichnende_ra` | Name der unterzeichnenden Anwältin/des Anwalts | Schlussformel |
| `rechtsanwaltsgesellschaft` | Partnerschaftsgesellschaft, GmbH o. ä. | Briefkopf, Fußzeile (optional) |

## Platzhalter-Ersetzung

Beim Aufruf des `erstantwort-generator`-Skills werden alle Platzhalter in doppelten eckigen Klammern `[...]` durch die Werte aus `kanzlei.json` ersetzt.

Beispiel-Ersetzung:
- `[SEKRETARIATS-TELEFON]` → `+49 89 12345-0`
- `[TRANSKRIPTIONS-TELEFON]` → `+49 89 12345-99`
- `[KANZLEI-NAME]` → `Müller & Partner Rechtsanwälte`
- `[ERREICHBARKEITSZEITEN]` → `Montag bis Freitag, 09:00 bis 17:00 Uhr`

## Validierung

Bevor die `kanzlei.json` für die Produktion verwendet wird:

1. **Telefonnummer-Format:** Deutsche Nummern im Format `+49 [ORTSVORWAHL] [NUMMER]` oder `0[ORTSVORWAHL] [NUMMER]`. Internationale Nummern im E.164-Format.
2. **Vollständigkeit:** Alle Pflichtfelder müssen ausgefüllt sein. Fehlende Pflichtfelder → Warnung und Verwendung des Platzhalter-Textes.
3. **E-Mail:** Grundlegendes Format `[name]@[domain].[tld]` prüfen.
4. **Transkriptions-Nummer:** Gesondert prüfen — dies ist die Nummer, die im DSGVO-Einwilligungshinweis erscheint. Fehlende oder ungültige Nummer → Transkriptions-Abschnitt deaktivieren und Warnung ausgeben.

## Fehlerfallbehandlung

| Fehlerfall | Verhalten |
|---|---|
| `kanzlei.json` nicht vorhanden | Platzhalter-Text `[KANZLEI-NAME]` etc. in der Antwort belassen; interne Warnung |
| Telefonnummer fehlt | Abschnitt mit dieser Nummer aus der Antwort entfernen; Warnung |
| Transkriptions-Nummer fehlt | Transkriptions-Abschnitt vollständig deaktivieren |
| Ungültiges JSON | Fehler melden; keine Antwort generieren bis korrigiert |

## Anpassung für verschiedene Kanzlei-Konstellationen

### Einzelanwalt / Einzelanwältin

```json
{
  "kanzlei": {
    "name": "Rechtsanwältin Dr. Lena Hoffmann",
    "telefon_sekretariat": "+49 30 98765-0",
    "telefon_transkription": "+49 30 98765-10",
    "unterzeichnende_ra": "Dr. Lena Hoffmann, Rechtsanwältin"
  }
}
```

### Große Kanzlei mit Empfang

```json
{
  "kanzlei": {
    "name": "Steinacker Lichtenberg Partnerschaftsgesellschaft mbB",
    "telefon_sekretariat": "+49 89 12345-0",
    "telefon_transkription": "+49 800 123456-99",
    "erreichbarkeit": "Mo-Do 08:30-18:00 Uhr, Fr 08:30-16:00 Uhr"
  }
}
```

### Kanzlei mit mehreren Standorten

Für jeden Standort eine separate `kanzlei-[standort].json` anlegen und beim Abruf den Standort angeben.

## Verweise auf andere Skills

- `erstantwort-generator` — Hauptabnehmer der Konfigurationsdaten
- `transkriptionsdienst-erklaerung` — benötigt `telefon_transkription`
- `muster-erstantwort` — Platzhalter werden durch diesen Skill befüllt
