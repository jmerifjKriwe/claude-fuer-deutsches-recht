---
name: workflow-chronologie-und-belegmatrix
description: "Chronologie und Belegmatrix für IP-Mandate: Sachverhalt zeitlich ordnen, Belege zu Ereignissen zuordnen, Lücken identifizieren und Beweisgrundlage für Abmahnung, EV und Klage aufbauen. Werkzeug für systematische Fallaufbereitung."
---

# Workflow: Chronologie und Belegmatrix

## Zweck

Dieser Skill erstellt eine **Sachverhalts-Chronologie und Belegmatrix** für IP- und Wettbewerbsrechtsmandate. Er ordnet Ereignisse zeitlich, weist Belege zu und identifiziert Lücken in der Beweiskette. Ohne strukturierte Chronologie verliert man in komplexen Fällen den Überblick.

Mandatsbezug: Mandant schildert einen komplexen Sachverhalt mit mehreren Verletzungshandlungen über längere Zeit. Anwalt muss daraus eine klare, zeitliche Abfolge mit Belegen erstellen, bevor er Abmahnung oder EV-Antrag vorbereitet.

## Chronologie-Aufbau

### Schritt 1 – Zeitachse anlegen

Folgende Ereignisse chronologisch erfassen:

| Datum | Ereignis | Beteiligte | Beleg | Status |
|---|---|---|---|---|
| [Datum] | Schutzrecht angemeldet | Mandant | Registerauszug | Gesichert |
| [Datum] | Schutzrecht eingetragen | DPMA/EUIPO | Urkunde | Gesichert |
| [Datum] | Verletzungshandlung erstmals | Verletzer | Screenshot | Gesichert |
| [Datum] | Erstkenntnis Mandant | Mandant | Eidesstattliche Versicherung | Glaubhaft |
| [Datum] | Abmahnung versandt | Mandant | Abmahnschreiben | Gesichert |
| [Datum] | Reaktion Gegenseite | Gegenseite | Antwortschreiben | Gesichert |
| [Datum] | EV beantragt | Mandant | Antragsschrift | Gesichert |
| [Datum] | EV erlassen | Gericht | EV-Beschluss | Gesichert |
| [Datum] | EV vollzogen | GV | Zustellurkunde | Gesichert |
| [Datum] | Verstoß gegen EV | Verletzer | Screenshot | Zu belegen |

### Schritt 2 – Lücken identifizieren

**Lückenkategorien:**

1. **Beleg fehlt ganz:** Ereignis ist beschrieben, aber kein Beweismittel vorhanden.
   → Mandant befragen; nachbeschaffen; eidesstattliche Versicherung?

2. **Beleg unvollständig:** Screenshot ohne Datum; Kaufbeleg ohne Produktangabe.
   → Beleg ergänzen; Screenshot mit Timestamp wiederholen.

3. **Zeitachse unklar:** Mandant weiß nicht genau, wann Erstkenntnis war.
   → Erinnerungsprotokoll; E-Mail-Suche; Browserverlauf.

4. **Beweiskette unterbrochen:** Zwischen Verletzungshandlung und Schaden fehlen Verbindungsglieder.
   → Sachverständigengutachten? Zusätzliche Zeugen?

### Schritt 3 – Belegmatrix erstellen

```
BELEGMATRIX
Mandat: [Mandant ./. Gegenseite]

Spalten: Ereignis | Datum | Beleg | Beweismittelart | Beweiswert | Status
Zeilen: Je ein Ereignis

Legende Status:
G = Gesichert (Beleg vorhanden und geprüft)
P = Plausibel (Ereignis plausibel, Beleg fehlt noch)
L = Lücke (Ereignis unbekannt oder unbelegt)
```

| # | Ereignis | Datum | Beleg | Beweismittelart | Beweiswert | Status |
|---|---|---|---|---|---|---|
| 1 | Schutzrecht eingetragen | _______ | Registerauszug | Urkunde | Hoch | G |
| 2 | Verletzungshandlung | _______ | Screenshot + URL | Augenschein | Mittel | G |
| 3 | Erstkenntnis Mandant | _______ | EV-Antrag Datum | Eidesstattliche Vers. | Mittel | P |
| 4 | Abmahnung zugestellt | _______ | Einschreiben-Rückschein | Urkunde | Hoch | G |
| 5 | EV erlassen | _______ | Beschluss | Urkunde | Hoch | G |
| 6 | EV vollzogen | _______ | Zustellurkunde | Urkunde | Hoch | G |
| 7 | Verstoß gegen EV | _______ | Screenshot nach EV | Augenschein | Mittel | L |

## Besondere Chronologie-Fragen im IP-Recht

### Dringlichkeitszeitachse (EV)

- Wann wurde Verletzung erstmals bekannt (Erstkenntnis)?
- Wie lange zwischen Erstkenntnis und EV-Antrag?
- War Zeitverzögerung begründet (Beweissammlung, Abmahnfrist)?
- Kritische Schwelle: Je nach Gericht 4–8 Wochen.

### Prioritätszeitachse (Marke)

- Wann wurde Voranmeldung eingereicht (Prioritätsdatum)?
- Wann wurde Marke veröffentlicht?
- Wann war Widerspruchsfrist?
- Wann eingetragen?

### Verletzungszeitraum (Schadensersatz)

- Wann begann die Verletzung?
- Wann endete sie (oder endet sie noch)?
- Wie häufig und in welchem Umfang?
- Diese Daten bestimmen die Höhe des Schadensersatzes.

## Lücken-Schließ-Strategie

| Lückentyp | Methode |
|---|---|
| Erstkenntnis unklar | E-Mail-Postfach durchsuchen; Browserverlauf; Zeuge |
| Verletzungsnachweis fehlt | Testkauf; erneuter Screenshot; Wayback Machine |
| Datum der Verletzungshandlung | Domain-Registrierungsdaten; Wayback Machine; Archiv |
| Schaden nicht bezifferbar | Sachverständiger; Lizenzanalogie-Recherche |
| Schutzrecht-Gültigkeit | Live-Abfrage DPMA/EUIPO; Jahresgebühren-Check |

## Output-Format Chronologie

**Kurz-Chronologie für EV-Antrag:**
```
[Datum] – Marke X eingetragen beim DPMA (Anlage 1)
[Datum] – Erstkenntnis der Verletzung durch Y (eidesstattliche Versicherung, Anlage 2)
[Datum] – Screenshot der Verletzungshandlung auf website.de (Anlage 3)
[Datum] – Abmahnung Y versandt (Anlage 4)
[Datum] – Y hat nicht reagiert / hat Abmahnung abgelehnt
[Datum] – EV-Antrag beim LG [Stadt]
```

**Detail-Belegmatrix:** Vollständige Tabelle für interne Akte und Qualitätsprüfung.

## Quellenregel

- Keine externen Rechtsquellen für diesen Prozess-Skill erforderlich.
- Belege auf Aktualität prüfen: Registerauszüge < 3 Monate; Screenshots mit Datum.
- Eidesstattliche Versicherung: Inhalt mit Chronologie abgleichen; keine Widersprüche.

## Anschluss-Skills

- `spezial-rechtsschutz-tatbestand-beweis-und-belege` – Tatbestand und Belegaufbau
- `workflow-dokumentenintake` – Dokumentenerfassung
- `gewr-einstweilige-verfuegung-eilverfahren-spezial` – EV-Antrag
- `spezial-klausel-beweislast-und-darlegungslast` – Beweislastverteilung
