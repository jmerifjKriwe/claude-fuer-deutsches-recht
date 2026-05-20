---
name: klassifikation-cpc-ipc
description: "Bestimmt die fuer eine Patentrecherche relevanten Klassen in der Cooperative Patent Classification (CPC) und International Patent Classification (IPC). Liest die Erfindungsbeschreibung den Anspruchsentwurf das Datenblatt aus parsen Sachverhalt extrahieren Schluesselbegriffe nennen. Schlaegt Hauptklassen und Nebenklassen vor mit knapper Begruendung warum die Klasse passt. Verweist auf die WIPO IPC Online und auf den Espacenet Classification Browser fuer die endgueltige Verifikation. Beruecksichtigt das Technikgebiet aus dem Kaltstart-Interview. Erinnert daran dass CPC feiner als IPC ist und EPA und USPTO CPC verwenden waehrend einige Aemter nur IPC anbringen. Disclaimer keine amtliche Klassifikation."
---

# klassifikation-cpc-ipc

## Zweck

Damit die anschließende Datenbankrecherche zielgenau läuft, müssen die richtigen **Klassen** bestimmt werden. Eine schlecht gewählte Klasse erzeugt entweder Trefferchaos oder verfehlt einschlägige Treffer komplett.

## Grundlagen

- **CPC** — Cooperative Patent Classification, gemeinsame Klassifikation von EPA und USPTO. Etwa 250.000 Untergruppen, etwa zehnmal feiner als IPC. Verwendet ab 2013, abgelöst hat sie die alte ECLA und die alte USPC.
- **IPC** — International Patent Classification, WIPO-Klassifikation. Etwa 70.000 Untergruppen. Wird global an Patentschriften angebracht, auch von Ämtern, die keine CPC vergeben.
- Eine Anmeldung trägt typischerweise mehrere CPC- und mehrere IPC-Symbole — eine **Hauptklasse** und mehrere **Nebenklassen**.

## Klassen-Schema (Hauptsektionen)

| Sektion | Inhalt |
| --- | --- |
| A | Täglicher Lebensbedarf (Landwirtschaft, Lebensmittel, Bekleidung, Medizinprodukte, Sport) |
| B | Arbeitsverfahren, Transport (Mechanik, Trennen, Mischen, Formen, Drucken, Transport, Verpacken, Mikro/Nano) |
| C | Chemie, Hüttenwesen (anorganische und organische Chemie, Polymere, Metallurgie, Werkstoffe) |
| D | Textilien, Papier |
| E | Bauwesen (Hochbau, Erdarbeiten, Wasserbau, Bergbau) |
| F | Maschinenbau, Beleuchtung, Heizung, Waffen, Sprengen |
| G | Physik (Messen, Optik, Elektrik-Messung, Informatik G06, Akustik, Erkennung, Atomphysik) |
| H | Elektrotechnik (Schaltkreise, Halbleiter H01L, Energie H02, Nachrichtentechnik H04, Hochfrequenz) |
| Y | CPC-Querschnittsschemata (Y02 Klima/CO2, Y04 IoT/Smart Grid, Y10 Cross-Reference) — **nur CPC, nicht IPC** |

## Ablauf

### 1. Erfindungsmaterial einlesen

- Erfindungsbeschreibung
- Anspruchsentwurf
- Datenblatt
- Skizzen / Zeichnungen
- Memo der Patentanwältin

Wenn nur sehr knappes Material vorhanden ist: an `rueckfragen-mandant` weiterleiten.

### 2. Schlüsselbegriffe extrahieren

Maximal 10 Begriffe, gegliedert in:

- **Was tut die Erfindung** (Verfahren, Funktion, Wirkung)
- **Wie ist sie aufgebaut** (Vorrichtungsmerkmale, Komponenten)
- **Wo wird sie eingesetzt** (Anwendungsfeld)
- **Mit welchen Stoffen / Materialien** (bei chemischen Erfindungen)

### 3. Kandidatenklassen sammeln

Zwei Wege parallel:

**a) Espacenet Classification Browser.** Bei den Schlüsselbegriffen den [Espacenet Classification Search](https://worldwide.espacenet.com/patent/cpc-browser) öffnen und die Begriffe nacheinander eingeben. Trefferklassen mit jeweiliger Definition notieren.

**b) Top-Down über Sektion / Klasse.** Aus dem Technikgebiet (Kaltstart-Interview) die wahrscheinliche Sektion wählen, von dort über die [WIPO IPC Online Publication](https://www.wipo.int/classifications/ipc/ipcpub) bis zur Untergruppe navigieren.

### 4. Auswahl Haupt- und Nebenklassen

Vorschlag formulieren:

```
Hauptklasse CPC: H02J 3/00 — Schaltungsanordnungen oder Systeme für die Versorgung oder Verteilung elektrischer Energie
  Entsprechende IPC: H02J 3/00
Nebenklassen CPC:
  - H02J 3/14 — Anpassung der Leistung an den Verbrauch (Lastmanagement)
  - G06Q 50/06 — Energie-, Wasser- oder Gasversorgung
  - Y02E 60/00 — Technologies für die Reduktion von Treibhausgasen (CPC-only)
```

Pro Klasse zwei Sätze Begründung, **warum** sie passt — verankert in den Schlüsselbegriffen.

### 5. Verifikation

- Auf den Espacenet-Klassen-Definitionsseiten die **Anmerkungen** lesen (Hinweise „nicht hier, sondern dort").
- Eine Stichprobe (3–5 bekannte Patente der Mandantin) klassifizieren lassen und prüfen, ob die Klassen aus Schritt 4 dort tatsächlich angebracht sind.

### 6. Übergabe

Die endgültige Klassenliste übergibt das Skill in maschinenlesbarer Form an `agentische-datenbank-recherche`:

```yaml
klassen:
  cpc_haupt: H02J 3/00
  cpc_neben: [H02J 3/14, G06Q 50/06, Y02E 60/00]
  ipc_haupt: H02J 3/00
  ipc_neben: [H02J 3/14, G06Q 50/06]
```

## Hinweise

- **CPC ist feiner.** Wenn EPA-/USPTO-/CN-/KR-Patente recherchiert werden, immer CPC. Wenn ältere Patente vor 2013 oder Patente aus Ländern ohne CPC: zusätzlich IPC.
- **Y-Sektion.** Y02 ist ein CPC-Querschnittsschema für Klimatechnologien — relevant für Energietechnik, Bauwesen, Verkehr. Y04 IoT, Y10 Cross-Reference. **Nicht in IPC** vorhanden.
- **Mehrere Klassen sind die Regel.** Eine moderne Anmeldung hat oft 5–15 CPC-Symbole. Recherche-Klassenset darf großzügig sein; verengt wird über Schlüsselbegriffe und Volltext.
- **Symbol-Syntax.** Sektion (Buchstabe) + Klasse (zweistellig) + Unterklasse (Buchstabe) + Hauptgruppe (1–3 Ziffern) + `/` + Untergruppe (2–6 Ziffern). Beispiel `H04L 9/00` heißt H/H04/H04L/H04L 9/00.

## Disclaimer

> **Hinweis zur Klassifikation.** Die hier vorgeschlagenen CPC- und IPC-Klassen sind eine durch Claude unterstützte **Vorklassifikation** zur Recherche-Steuerung und keine amtliche Klassifikation. Die endgültige Klasseneinordnung einer eigenen Anmeldung erfolgt durch das Patentamt. Für die Recherchesteuerung sind ergänzend Schlüsselbegriffe und Volltextsuchen einzusetzen — keine Klassenrecherche ohne Volltext.
