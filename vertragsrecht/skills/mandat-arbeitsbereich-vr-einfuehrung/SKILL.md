---
name: mandat-arbeitsbereich-vr-einfuehrung
description: "Verwaltet Mandatsarbeitsbereiche — neu anlegen, auflisten, wechseln, abschließen oder von Mandatsebene auf Kanzleiebene wechseln. Lädt, wenn ein Anwalt mit mehreren Mandanten ein neues Mandat anlegen, zum aktiven Mandat wechseln, Mandate auflisten, ein Mandat archivieren oder auf kanzleiweiten Kontext umschalten möchte im Vertragsrecht: prüft konkret die einschlägigen Tatbestandsmerkmale, Fristen, Belege und Rechtsprechung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Arbeitsschritt."
---

# Mandatsarbeitsbereich Vertragsrecht

## Arbeitsbereich

Verwaltet Mandatsarbeitsbereiche — neu anlegen, auflisten, wechseln, abschließen oder von Mandatsebene auf Kanzleiebene wechseln. Lädt, wenn ein Anwalt mit mehreren Mandanten ein neues Mandat anlegen, zum aktiven Mandat wechseln, Mandate auflisten, ein Mandat archivieren oder auf kanzleiweiten Kontext umschalten möchte. Die Prüfung konzentriert sich auf dieses Prüffeld und trennt Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: BGB §§ 305-310, AGBG (alt), EuGH zu Klauseltransparenz (z. B. C-26/13, C-186/16), VerbrG; §§ 305 ff. BGB, NDA, SaaS- — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Zweck

Anwältinnen und Anwälte arbeiten parallel an mehreren Mandaten. Ein
Mandatsarbeitsbereich hält den Kontext eines Mandanten oder Auftrags strikt
von allen anderen getrennt. Diese Skill verwaltet diese Arbeitsbereiche.

Lädt, wenn ein Anwalt mit Mehrfach-Mandantenstruktur (Kanzlei, Außenmandate)
einen Arbeitsbereich anlegen, wechseln, auflisten oder schließen möchte, oder
wenn eine andere Skill wissen muss, in welchem Mandat sie tätig ist.

**Standardzustand: deaktiviert.** Für Syndikusrechtsanwältinnen und
-anwälte (In-house) mit einem einzigen Mandanten/Arbeitgeber läuft das
Plugin automatisch auf Kanzleiebene. Mandatsarbeitsbereiche werden nur für
Kanzleien und Berufsanwälte mit Mehrfach-Mandantenstruktur aktiviert.

## Eingaben

- Unterbefehl: `neu`, `liste`, `wechseln`, `schließen`, `keine`
- Mandats-Kürzel (Slug): Kurzbezeichnung in Kleinbuchstaben mit Bindestrichen
 (z. B. `mueller-kaufvertrag-2026`, `meier-agb-prüfung`, `xyz-gmbh-msa`)
- Für `neu`: Mandantenangaben (Name, Gegenpartei, Vertragsart, Schlüsselfakten)

## Rechtlicher Rahmen

### Kernvorschriften

Die Mandatsverwaltung ist untrennbar mit dem anwaltlichen Berufsrecht
und der anwaltlichen Verschwiegenheitspflicht verbunden:

- § 43a Abs. 2 BRAO — Verschwiegenheitspflicht des Rechtsanwalts;
 Mandatsgeheimnis als Kernpflicht
- § 203 StGB — Verletzung von Privatgeheimnissen; strafrechtlicher Schutz
 des Mandatsgeheimnisses
- § 50 BRAO — Handakten; Aufbewahrungspflicht (5 Jahre nach Abschluss
 des Mandats)
- § 2 BORA — Grundpflichten; Interessenkonflikte müssen geprüft werden
 (Mandate gegen frühere Mandanten oder gleichzeitig gegen denselben
 Mandanten in anderem Verfahren)
- DSGVO Art. 5, 25 — Datenschutz durch Technikgestaltung; mandatsbezogene
 personenbezogene Daten dürfen nicht zwischen Mandaten geteilt werden

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Anwaltliche Verschwiegenheitspflicht; Schadensersatz bei
 Geheimnisbruch durch Anwalt; § 43a BRAO)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Anwaltliche Aufbewahrungspflicht von Handakten; § 50 BRAO)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 (Schutz von Verteidigungsunterlagen; Rechtsanwalt; § 97 StPO analog)

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Ablauf

### Unterbefehle

- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich neu <kuerzel>` — neuen Mandatsarbeitsbereich
 anlegen, kurze Aufnahme durchführen, `mandat.md` schreiben
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich liste` — alle Mandate mit Status und
 aktivem Kürzel auflisten
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich wechseln <kuerzel>` — aktives Mandat setzen
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich schließen <kuerzel>` — Mandat archivieren
 (verschiebt in `_archiv/`, löscht nie)
- `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich keine` — von aktivem Mandat trennen,
 auf Kanzleiebene arbeiten

### Schritt 1 — Kanzleiprofil prüfen

Lies `~/.claude/plugins/config/klotzkette/vertragsrecht/CLAUDE.md`. Prüfe
den Abschnitt `## Mandatsarbeitsbereiche`. Wenn `Aktiviert: ✗`, weise einmal
darauf hin:

> Mandatsarbeitsbereiche sind deaktiviert — Sie sind als In-house-Praxis
> mit einem Mandanten konfiguriert; das Plugin arbeitet automatisch auf
> Kanzleiebene. Wenn Sie tatsächlich mit mehreren Mandanten arbeiten,
> führen Sie `/vertragsrecht:vertragsrecht-kaltstart-interview --redo` aus und wählen
> eine Kanzleisetting-Option. Andernfalls benötigen Sie
> `/mandat-arbeitsbereich` nicht.

### Schritt 2 — Unterbefehl ausführen

Auflösung nach dem ersten Token von `$ARGUMENTE`:

- `neu` → Aufnahme durchführen, `mandate/<kuerzel>/mandat.md` schreiben,
 `verlauf.md` und `notizen.md` anlegen
- `liste` → `mandate/*/mandat.md` aufzählen, Tabelle ausgeben,
 aktives Mandat markieren
- `wechseln` → Zeile `Aktives Mandat:` im Kanzleiprofil aktualisieren
- `schließen` → `mandate/<kuerzel>/` nach `mandate/_archiv/<kuerzel>/`
 verschieben, Abschlussdatum in `verlauf.md` eintragen
- `keine` → `Aktives Mandat:` auf `keine — Kanzleiebene` setzen

### Schritt 3 — Bestätigung vor Schreiben

Dem Nutzer vor jeder Dateiänderung zeigen, was sich ändert, und
Bestätigung einholen.

### Unterbefehl-Logik: `neu <kuerzel>`

1. Prüfen, ob das Kürzel noch nicht in `mandate/<kuerzel>/` oder
 `mandate/_archiv/<kuerzel>/` vorhanden ist. Bei Wiederverwendung:
 anderes Kürzel vorschlagen.
2. Kurzaufnahme durchführen:
 - **Mandant** (vertretene Partei oder interne Geschäftseinheit bei In-house)
 - **Gegenpartei** (andere Seite — kann mehrere sein)
 - **Vertragsart** (Lieferantenvertrag / Dienstleistungsvertrag / NDA /
 SaaS-Abonnement / Nachtrag / Verlängerung / Sonstiges)
 - **Vertraulichkeitsstufe** (Standard / erhöht / Clean-Team)
 - **Schlüsselfakten** (2–5 Sätze: Gegenstand, Beteiligte, Besonderheiten
 gegenüber Standardplaybook)
 - **Mandatsspezifische Abweichungen vom Playbook** (z. B. "Mandant besteht
 auf 24 Monate Haftungsdeckel statt 12; kooperativer Ton, da strategische
 Partnerschaft")
 - **Verwandte Mandate** (Kürzel verbundener Mandate)
3. `mandate/<kuerzel>/mandat.md` nach Vorlage unten schreiben.
4. `mandate/<kuerzel>/verlauf.md` mit einem "Eröffnet"-Eintrag anlegen.
5. Leere `mandate/<kuerzel>/notizen.md` erstellen.
6. **Nicht** automatisch zum neuen Mandat wechseln. Fragen:
 "Möchten Sie jetzt zu `<kuerzel>` wechseln?"

### Unterbefehl-Logik: `liste`

`mandate/*/mandat.md` aufzählen. Erste Zeilen jeder Datei für Status lesen.
Tabelle ausgeben:

| Kürzel | Mandant | Vertragsart | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. Archivierte Mandate unter
"Archivierte Mandate" separat aufführen.

### Unterbefehl-Logik: `wechseln <kuerzel>`

1. Prüfen, ob `mandate/<kuerzel>/mandat.md` existiert. Falls nicht:
 `/vertragsrecht:vertragsrecht-mandat-arbeitsbereich neu <kuerzel>` anbieten.
2. `Aktives Mandat:`-Zeile im Kanzleiprofil auf `<kuerzel>` setzen.
3. `mandat.md`-Zusammenfassung anzeigen, damit der Nutzer das richtige
 Mandat bestätigt.

### Unterbefehl-Logik: `schließen <kuerzel>`

1. Vorhandensein von `mandate/<kuerzel>/` prüfen.
2. Abschlusseintrag mit heutigem Datum in `mandate/<kuerzel>/verlauf.md` hinzufügen.
3. `mandate/<kuerzel>/` nach `mandate/_archiv/<kuerzel>/` verschieben.
4. War das geschlossene Mandat das aktive, `Aktives Mandat:` auf
 `keine — Kanzleiebene` setzen.

### Unterbefehl-Logik: `keine`

`Aktives Mandat:` im Kanzleiprofil auf `keine — Kanzleiebene` setzen.
Mit Nutzer bestätigen.

## Ausgabeformat

### Vorlage `mandat.md`

```markdown
[ARBEITSERGEBNIS-KENNZEICHNUNG — gemäß Kanzleiprofil ## Ausgaben]

# Mandat: [Mandant] — [Kurzbeschreibung]

**Kürzel:** [kürzel]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [Standard / erhöht / Clean-Team]

---

## Parteien

**Mandant:** [Name]
**Gegenpartei:** [Name(n)]

## Vertragsart

[Lieferantenvertrag / Dienstleistungsvertrag / NDA / SaaS-Abonnement /
Nachtrag / Verlängerung / Sonstiges — mit einem Satz Begründung]

## Schlüsselfakten

[2–5 Sätze: Vertragsgegenstand, beteiligte Personen, Risikolage,
Besonderheiten gegenüber dem Standard-Playbook.]

## Mandatsspezifische Abweichungen vom Playbook

*Jede Abweichung vom kanzleiweiten Playbook, die nur dieses Mandat betrifft.*

- [z. B. "Haftungsobergrenze: Mandant besteht auf 24 Monate, nicht
 Kanzleistandard 12."]
- [z. B. "Ton: beziehungserhaltend — Gegenpartei ist strategischer Partner."]
- [z. B. "Gerichtsstand: muss München sein."]

## Verwandte Mandate

- [Kürzel — ein Satz warum verwandt]

## Vertraulichkeitshinweise

[Bei erhöhter Vertraulichkeit oder Clean-Team: Begründung, wer Einsicht hat,
ob mandatsübergreifender Kontext trotz globaler Einstellung unzulässig ist.]
```

### Vorlage `verlauf.md` (Seed)

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Append-only Ereignisprotokoll. Aktuellster Eintrag oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Kürzel: `[kürzel]`. Status: aktiv.
[Anfangskontext — z. B. "Eröffnet auf eingehenden MSA-Entwurf von
[Gegenpartei]."]
```

## Ablagestruktur

```
~/.claude/plugins/config/klotzkette/vertragsrecht/
├── CLAUDE.md # Kanzleiprofil
└── mandate/
 ├── <kuerzel>/
 │ ├── mandat.md # Mandantenangaben, Schlüsselfakten, Abweichungen
 │ ├── verlauf.md # Datiertes Protokoll (Ereignisse, Entscheidungen, Entwürfe)
 │ ├── notizen.md # Freie Arbeitsnotizen
 │ └── ausgaben/ # Skill-Ausgaben für dieses Mandat (optional)
 └── _archiv/
 └── <kuerzel>/ # Geschlossene Mandate — lesbar, nicht aktiv
```

Kürzel sind Kleinbuchstaben mit Bindestrichen. Beispiele:
`mueller-kaufvertrag-2026`, `meier-agb-prüfung`, `xyz-gmbh-nda`.

## Mandatsübergreifender Kontext

Das Kanzleiprofil enthält eine `Mandatsübergreifender-Kontext:`-Option.
Standardmäßig `aus` — eine Skill, die in Mandat A arbeitet, liest **nie**
Dateien aus `mandate/B/`. Das ist die Vertraulichkeitsgarantie.

Bei `ein` darf eine Skill mandatsübergreifend lesen **nur** auf ausdrückliche
Nutzeranfrage. Auch dann gilt: Standardmäßig nur aktives Mandat laden,
es sei denn, der Nutzer fragt explizit nach einer mandatsübergreifenden Ansicht.

## Beispiel

**Szenario:** Kanzlei übernimmt Prüfung eines IT-Dienstleistungsvertrags
für Mandantin GmbH gegen Lieferant X.

```
/vertragsrecht:vertragsrecht-mandat-arbeitsbereich neu mueller-it-vertrag-2026
```

Kurzaufnahme ergibt:
- Mandant: Müller GmbH
- Gegenpartei: IT-Lieferant X GmbH
- Vertragsart: Dienstleistungsvertrag
- Besonderheit: Mandant besteht auf unbeschränkter Gewährleistung für
 datenschutzkritische Komponenten

Slug `mueller-it-vertrag-2026` angelegt mit Abweichung:
"Gewährleistung: kein Verjährungsverkürzung für Datenschutz-Komponenten."

## Risiken und typische Fehler

- **Kein Interessenkonflikt-Check.** Diese Skill führt keine automatische
 Konfliktprüfung durch — das ist Aufgabe des Anwalts. Die Aufnahme erfasst,
 was der Nutzer erklärt; sie ersetzt keine Prüfung nach § 43a BRAO, § 3
 BORA.
- **Löschen ist verboten.** Abschließen bedeutet Archivieren. Keine
 Mandatsakte wird gelöscht — Aufbewahrungspflicht nach § 50 BRAO (5 Jahre).
- **Kürzel-Kollision prüfen.** Wird ein Kürzel eines archivierten Mandats
 wiederverwendet, das archivierte Mandat unter `_archiv/<kuerzel>/` belassen.
- **Mandatsübergreifender Kontext bleibt aus.** Wenn nicht explizit
 eingeschaltet, niemals Dateien eines anderen Mandats lesen.

## Quellenpflicht

Bei mandatsspezifischen Hinweisen zur Vertraulichkeit oder Aufbewahrung:
- § 43a Abs. 2 BRAO (Verschwiegenheit), § 50 BRAO (Handakten)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

<!-- AUDIT 27.05.2026
Quelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=17.12.1998&Aktenzeichen=IX+ZR+196%2F97
Bundle: bundle_047.json
-->
