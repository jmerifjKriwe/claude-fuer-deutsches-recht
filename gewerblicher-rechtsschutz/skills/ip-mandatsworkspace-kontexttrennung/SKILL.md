---
name: ip-mandatsworkspace-kontexttrennung
description: "Kanzlei mit mehreren Mandanten im gewerblichen Rechtsschutz muss Kontext zwischen Mandaten strikt trennen. Mandatsverwaltung IP-Kanzlei. Prüfraster: Anlegen Auflisten Wechseln Schließen oder Trennen des aktiven Mandats Mandantenkontext für alle Folge-Skills. Output: aktives Mandat gesetzt und bestätigte Kontexttrennung. Abgrenzung zu gewerblicher-rechtsschutz-kaltstart-interview (Kanzlei-Profil) und allen Sach-Skills."
---

# Mandatsworkspace, Kontexttrennung und Fristensteuerung

## Zweck

Anwälte und Patentanwälte arbeiten gleichzeitig an mehreren Mandaten. Ein Mandatsarbeitsbereich hält den Kontext eines Mandanten oder einer Angelegenheit von jedem anderen getrennt. Diese Skill verwaltet diese Bereiche.

Der Standardzustand ist **deaktiviert**. Syndikusrechtsanwälte und Inhouse-Teams (ein Mandant) arbeiten auf Praxisebene; Mandatsarbeitsbereiche sind für sie unsichtbar. Sie aktivieren sich beim Erstkonfigurationsgespräch für externe Anwälte (Einzel-, Klein- und Großkanzleien) oder durch manuelle Einrichtung.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

## Eingaben

Befehlsargument (erstes Token):

- `neu <kurzzeichen>` — neuen Mandatsarbeitsbereich anlegen
- `liste` — alle Mandate mit Status und aktivem Mandat anzeigen
- `wechseln <kurzzeichen>` — aktives Mandat umstellen
- `schliessen <kurzzeichen>` — Mandat archivieren
- `kein` — von jedem Mandat trennen, auf Praxisebene arbeiten

## Rechtlicher Rahmen

### Berufsrechtliche Rahmenbedingungen

- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht des Rechtsanwalts; Mandatsgeheimnis; Grundlage der Mandatskontexttrennung
- **§ 43a Abs. 4 BRAO** — Verbot der Vertretung widerstreitender Interessen (Interessenkonflikt); Mandate müssen getrennt geführt werden
- **§ 203 Abs. 1 Nr. 3 StGB** — Verletzung von Privatgeheimnissen durch Rechtsanwälte; strafrechtliche Absicherung der Vertraulichkeit
- **§ 50 BRAO** — Aufbewahrungspflichten für Handakten (mind. 5 Jahre); Archivierung schließt Mandatsarbeitsbereiche nicht; Löschung ist ausgeschlossen
- **§ 2 BORA** — Berufsrechtliche Pflichten; Grundsatz der anwaltlichen Unabhängigkeit

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Kommentare

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Feuerich/Weyland/Böhnlein, BRAO, 10. Aufl. 2022, § 50 Rn. 1 ff. (Handaktenaufbewahrung)

## Ablauf

### Schritt 1: Vorbedingung prüfen

Praxiskonfigurationsdatei lesen. Falls `Mandatsarbeitsbereiche: ✗` (Standardeinstellung für Inhouse-Teams):

> Mandatsarbeitsbereiche sind deaktiviert — Sie sind als Inhouse-Praxis mit einem Mandanten konfiguriert; das Plugin arbeitet automatisch auf Praxisebene. Wenn Sie tatsächlich über mehrere externe Mandate hinweg arbeiten, führen Sie das Erstkonfigurationsgespräch erneut aus und wählen Sie die Kanzlei-Einstellung. Andernfalls benötigen Sie `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-mandat-arbeitsbereich` nicht.

Kein Fehler — der deaktivierte Zustand ist der erwartete für Inhouse-Nutzer.

### Schritt 2: Befehlsverarbeitung

Auf das erste Token des Arguments dispatchen.

---

#### Befehl `neu <kurzzeichen>`

1. Prüfen, ob das Kurzzeichen nicht bereits in `mandate/<kurzzeichen>/` oder `mandate/_archiv/<kurzzeichen>/` vorhanden ist. Bei Kollision: anderen Namen wählen lassen.
2. Aufnahmeinterview durchführen (in einem Durchgang):
   - **Mandant** — vertretene Partei oder interne Geschäftseinheit
   - **Gegenpartei** — andere Seite (kann mehrere umfassen; kann "unbekannter Drittverletzer" bei Watch-Treffern sein)
   - **Mandatstyp** — für gewerblichen Rechtsschutz: Markenschutz / Markenverletzung / Schutzrechtsübertragung / Patentverletzung / FTO-Gutachten / IP-Klauselprüfung / OSS-Compliance / Portfolioverwaltung / Störerhaftung / Sonstiges
   - **Vertraulichkeitsstufe** — standard | erhöht | Clean-Team (erhöht bei besonderer Sensibilität, Clean-Team häufig bei FTO-Gutachten und Patentkäufen)
   - **Wesentliche Tatsachen** — 2–5 Sätze: Worum geht es, wer sind die Beteiligten, was steht auf dem Spiel
   - **Mandatsspezifische Abweichungen von der Standardposition** (z. B. "Mandant wünscht nur schriftliche Kommunikation", "Gegenpartei ist Geschäftspartner — maßvoller Ton")
   - **Verbundene Mandate** — Kurzzeichen zusammenhängender Mandate
3. `mandate/<kurzzeichen>/mandat.md` mit der unten angegebenen Vorlage schreiben.
4. `mandate/<kurzzeichen>/verlauf.md` mit einem einzigen Eröffnungseintrag anlegen.
5. Leere `mandate/<kurzzeichen>/notizen.md` anlegen.
6. **Nicht** automatisch zum neuen Mandat wechseln. Fragen: "Möchten Sie jetzt zu `<kurzzeichen>` wechseln?"

---

#### Befehl `liste`

`mandate/*/mandat.md` aufzählen. Aus jeder Datei Status und Kurzzeichen entnehmen. Tabelle ausgeben:

| Kurzzeichen | Mandant | Mandatstyp | Status | Eröffnet | Aktiv |
|---|---|---|---|---|---|

Aktives Mandat mit `*` markieren. `_archiv/*` unter gesonderter Überschrift "Archivierte Mandate" anführen.

---

#### Befehl `wechseln <kurzzeichen>`

1. Prüfen, ob `mandate/<kurzzeichen>/mandat.md` vorhanden. Falls nicht: `neu <kurzzeichen>` anbieten.
2. `Aktives Mandat:`-Zeile in der Praxiskonfigurationsdatei auf `<kurzzeichen>` aktualisieren.
3. Dem Nutzer die mandat.md-Zusammenfassung zeigen, damit er das richtige Mandat bestätigen kann.

---

#### Befehl `schliessen <kurzzeichen>`

1. `mandate/<kurzzeichen>/` auf Existenz prüfen.
2. "Geschlossen"-Eintrag mit aktuellem Datum an `mandate/<kurzzeichen>/verlauf.md` anhängen.
3. `mandate/<kurzzeichen>/` nach `mandate/_archiv/<kurzzeichen>/` verschieben.
4. War das geschlossene Mandat das aktive Mandat: `Aktives Mandat:` auf `kein — nur Praxisebene` setzen.

---

#### Befehl `kein`

`Aktives Mandat:` in der Praxiskonfigurationsdatei auf `kein — nur Praxisebene` setzen. Bestätigung an den Nutzer.

## Ausgabeformat

### Vorlage `mandat.md`

<!-- BEGIN ausformulierungspflicht (autogen) -->
> **Ausformulierungspflicht und Formatstandard.** Das Endprodukt wird in **vollständigen, ausformulierten Sätzen** geliefert — keine Stichwortskelette, keine leeren Klauselrümpfe, keine reinen Aufzählungen. Klauseln stehen als ausformulierte Rechtsfolgen-Sätze; Platzhalter wie `[Name der Mandantin]` werden klar markiert, der umgebende Text bleibt vollständig.
>
> **Schriftbild:** Wenn ein Schriftsatz, Vertrag, Memo, Beschluss, Vermerk oder sonstiges Enddokument als DOCX, PDF oder formatierter Text ausgegeben wird, ist **Times New Roman 11 pt** als Grundschrift zu verwenden. Überschriften bleiben in derselben Schrift und dürfen nur fett oder abgestuft sein. Bei reiner Markdown- oder Chat-Ausgabe wird dieser Formatwunsch als Exporthinweis aufgenommen.
>
> **Nummerierung:** Gliederung ausschließlich dezimal (`1`, `1.1`, `1.1.1` und so weiter). Keine römischen Ziffern, keine Buchstaben- oder Mischgliederung.
<!-- END ausformulierungspflicht (autogen) -->

```markdown
[ARBEITSERGEBNIS-KOPFZEILE — gemäß Mandatsprofil]

# Mandat: [Mandant] — [Kurzbeschreibung]

**Kurzzeichen:** [kurzzeichen]
**Eröffnet:** [JJJJ-MM-TT]
**Status:** aktiv
**Vertraulichkeit:** [standard / erhöht / Clean-Team]

---
## Parteien

**Mandant:** [Name]
**Gegenpartei:** [Name(n)]

## Mandatstyp

[Markenschutz / Markenverletzung / FTO-Gutachten / Patentverletzung / IP-Klauselprüfung / OSS-Compliance / Portfolioverwaltung / Störerhaftung / Sonstiges — mit einzeiliger Begründung]

## Wesentliche Tatsachen

[2–5 Sätze. Worum geht es. Wer sind die Beteiligten. Was steht auf dem Spiel. Was macht dieses Mandat vom Standard abweichend.]

## Mandatsspezifische Abweichungen

*Jede Abweichung von der Praxisstandposition, die nur für dieses Mandat gilt.*

- [z. B. "Durchsetzungsstrategie: hier maßvoll, obwohl Hausstandard aggressiv — Gegenpartei ist wichtiger Handelspartner."]
- [z. B. "Genehmigung für Abmahnungen: zusätzliche Freigabe durch Mandant erforderlich."]
- [z. B. "Clean-Team: Mandatsakten auch bei aktiviertem mandatsübergreifendem Kontext nicht lesbar."]

## Verbundene Mandate

- [kurzzeichen — einzeilige Begründung]

## Vertraulichkeitshinweise

[Bei erhöhter oder Clean-Team-Stufe: warum. Wer darf die Mandatsakten einsehen. Ob mandatsübergreifender Kontext zulässig ist.]
```

### Vorlage `verlauf.md`

```markdown
# Verlauf: [Mandant] — [Kurzbeschreibung]

Nur-Anhänge-Ereignisprotokoll. Neuestes oben.

---

## [JJJJ-MM-TT] — Mandat eröffnet

Aufnahme abgeschlossen. Kurzzeichen: `[kurzzeichen]`. Status: aktiv.
[Ggf. initialer Kontext — z. B. "Eröffnet nach Watch-Treffer auf `APEXLEAF` in Klasse 25."]
```

## Beispiel

**Eingabe:** `/gewerblicher-rechtsschutz:gewerblicher-rechtsschutz-mandat-arbeitsbereich neu bmw-marke-2026`

**Verarbeitung:**
Kurzzeichen prüfen → Aufnahmeinterview starten → `mandat.md` erstellen → `verlauf.md` mit Eröffnungseintrag anlegen → Nutzer fragen, ob zum neuen Mandat gewechselt werden soll.

**Ausgabe (Auszug):**

> Mandatsarbeitsbereich `bmw-marke-2026` angelegt.
>
> | Kurzzeichen | Mandant | Mandatstyp | Status | Eröffnet |
> |---|---|---|---|---|
> | bmw-marke-2026 | BMW AG | Markenschutz | aktiv | 2025-07-15 |
>
> Möchten Sie jetzt zu `bmw-marke-2026` wechseln?

## Risiken und typische Fehler

- **Interessenkonflikte nicht erkennen:** Diese Skill führt keine Interessenkonfliktprüfung durch — das ist Aufgabe des Anwalts und der Kanzlei. Die Aufnahme erfasst nur, was der Nutzer angibt.
- **Archivierung ist keine Löschung:** Geschlossene Mandate bleiben lesbar (§ 50 BRAO — Aufbewahrungspflicht mindestens 5 Jahre). Retention-Policy ist außerhalb des Skill-Umfangs.
- **Mandatsübergreifender Kontext standardmäßig aus:** Die Praxiskonfiguration hat ein `Mandatsübergreifender Kontext:`-Flag. Standardmäßig `aus` — Skill A im Mandat X liest niemals Dateien aus Mandat Y. Das ist die Vertraulichkeitsgarantie.
- **Kurzzeichen-Kollision mit Archiv:** Wird ein Kurzzeichen wiederverwendet, das im Archiv liegt, wird das archivierte Mandat unter `_archiv/<kurzzeichen>/` bewahrt; das neue erhält einen anderen Namen.

## Quellenpflicht

Alle Aussagen zu Vertraulichkeit, Aufbewahrung und Interessenkonflikten müssen auf konkreten Normen beruhen:

- **§ 43a BRAO** (Verschwiegenheit), **§ 43a Abs. 4 BRAO** (widerstreitende Interessen), **§ 203 StGB** (Verletzung von Privatgeheimnissen), **§ 50 BRAO** (Handaktenaufbewahrung)
- Modellannahmen als `[Modellwissen — verifizieren]` kennzeichnen.

## Triage-Fragen bei Mandatseröffnung

Bevor das Mandat angelegt wird, klaere:
1. Ist ein Interessenkonflikt-Check (§ 43a IV BRAO) durchgefuehrt worden?
2. Sind die wesentlichen Mandatsdaten vollstaendig (Mandant, Gegner, Rechtsgebiet, Streitgegenstand)?
3. Wurde der Mandant ueber Honorar und Kostenrisiko aufgeklaert (§ 49b BRAO, § 34 RVG)?
4. Laeuft bereits eine Frist (z.B. Widerspruchsfrist Marke, Abmahnungsfrist), die sofort ins Fristenbuch muss?

## Aktuelle Rechtsprechung

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

> Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

<!-- AUDIT 27.05.2026
Task: Bundle 031 / Halluzinations-Reparatur
Korrektur: Zitat aus "Aktuelle Rechtsprechung"-Block entfernt (bei Zweifel loeschen).
-->
