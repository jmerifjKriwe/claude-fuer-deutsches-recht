---
name: kopfdaten-und-aussere-form
description: "Prüfraster und Generierregeln für Briefkopf, Datum, Unterschrift und äußere Form des Arbeitszeugnisses. Fehlerhafte Formalia sind eigenständige Berichtigungspunkte. Enthält die Anforderungen aus BAG (9 AZR 893/98) zur Unterschrift, das Fließtextgebot aus BAG (9 AZR 262/20) und die Regeln zur elektronischen Form seit dem Vierten Bürokratieentlastungsgesetz (ab 1.1.2025)."
---

# Kopfdaten und äußere Form

## Ziel

Die Formalia des Zeugnisses korrekt generieren, damit keine Berichtigungsansprüche aus formalen Mängeln entstehen.

## Prüfposten

| Prüfposten | Soll | Typischer Mangel |
|---|---|---|
| Briefkopf | offizielles Firmenpapier mit vollständiger Anschrift | privates Papier, fehlende Anschrift, veraltete Adresse |
| Datum | Ausstellungsdatum plausibel nahe am Austrittsdatum | fehlendes Datum, unplausibel langes Intervall |
| Überschrift | „Arbeitszeugnis" oder „Zeugnis" | fehlt oder lautet „Beurteilung" (andere Signalwirkung) |
| Position | exakte Funktionsbezeichnung, ggf. mit Hierarchiestufe | zu niedrige Bezeichnung, fehlender Titel |
| Beschäftigungszeitraum | vollständig, ohne Lücken | Lücken, falsches Eintrittsdatum |
| Aufgabenkatalog | umfassend, Schlüsselverantwortungen erwähnt | unvollständig |
| Unterschrift | eigenhändig; genau die Person, die in Maschinenschrift steht | andere Person unterschrieben, fehlende Unterschrift |
| Format | Fließtext | Ankreuzschema, Tabelle, Stichpunkte |

## Unterschrift — Pflicht nach BAG

Nach BAG, Urteil v. 21.09.1999 – 9 AZR 893/98:
- Schließt das Zeugnis mit Name und Funktion einer Person in Maschinenschrift, muss genau diese Person eigenhändig unterschreiben.
- Eine Unterzeichnung durch eine andere Person (z.B. HR-Sachbearbeiter statt dem genannten Vorgesetzten) ist ein formaler Mangel.
- Eine quer durch den Text laufende Unterschrift oder ein Smiley in der Unterschrift sind unzulässige Distanzierungszeichen (LAG Hamm, Beschluss v. 14.11.2016 – 12 Ta 475/16; ArbG Kiel, Urteil v. 18.04.2013 – 5 Ca 80 b/13).

## Fließtextgebot

Ein qualifiziertes Zeugnis in Tabellenform oder als Ankreuzschema erfüllt den Anspruch aus Paragraf 109 GewO regelmäßig nicht (BAG, Urteil v. 27.04.2021 – 9 AZR 262/20).

## Elektronische Form ab 1.1.2025

Seit dem Vierten Bürokratieentlastungsgesetz (in Kraft 1.1.2025) erlaubt Paragraf 109 Abs. 3 GewO die elektronische Form mit Einwilligung des Arbeitnehmers. Voraussetzung: qualifizierte elektronische Signatur (Paragraf 126a BGB). Einfaches PDF, Scan oder E-Mail genügen nicht.

Ohne ausdrückliche Einwilligung gilt: Papierzeugnis mit eigenhändiger Unterschrift.

## Datum-Regeln

- Ausstellungsdatum sollte möglichst nah am Austrittsdatum liegen.
- Rückdatierung auf den letzten Arbeitstag ist üblich und zulässig.
- Ausstellungsdatum deutlich nach dem Austrittsdatum kann auf Verweigerung oder Verzögerung hindeuten — kein automatischer Berichtigungspunkt, aber Kontext prüfen.

## Holschuld

Das Zeugnis ist Holschuld des Arbeitnehmers nach Paragraf 269 BGB (BAG, Urteil v. 08.03.1995 – 5 AZR 848/93) — der Arbeitnehmer holt es ab. Nur ausnahmsweise bei Unzumutbarkeit wird daraus eine Schickschuld.

## Generier-Platzhalter für Formalia

```
[Firmenname] | [Straße, PLZ Ort]

Arbeitszeugnis

[Ort], [Datum]

[Unterschrift]
[Vorname Nachname]
[Funktion]
```

## Stolpersteine

- Unterzeichner und Maschinenschrift-Name stimmen nicht überein — häufiger Praxisfehler.
- Datum fehlt — ist ein formaler Mangel.
- Zeugnis auf privatem Briefpapier statt Firmenpapier.

## Anti-Muster

- Datum des Zeugnisses deutlich vor dem Austrittsdatum setzen (noch aktives Arbeitsverhältnis).
- HR-Generalist als Unterzeichner nennen, obwohl der direkte Vorgesetzte verfügbar wäre.
- Qualifiziertes Zeugnis mit grafischer Tabelle (Schulnoten-Schema) formatieren.
