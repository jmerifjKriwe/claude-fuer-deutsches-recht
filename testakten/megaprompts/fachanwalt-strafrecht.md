# Megaprompt: fachanwalt-strafrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 226 Skills des Plugins `fachanwalt-strafrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Anwalts-Dashboard Fachanwalt Strafrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zus…
2. **mandat-triage-strafrecht** — Strukturierte Eingangs-Abfrage für Strafmandate: Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstr…
3. **orientierung-mandat-fachanwaltschaft** — Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafre…
4. **orientierung-fristen-form-und-zustaendigkeit** — Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg.
5. **erstgespraech-mandatsannahme** — Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polize…
6. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
7. **output-waehlen** — Output-Wahl für Fachanwalt Strafrecht: stimmt Adressat (Beschuldigter/Angeklagter, Staatsanwaltschaft, Verletzte/Nebenkl…
8. **adhaesionsverfahren** — Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig S…
9. **anklage-reaktion** — Reaktion auf Anklageerhebung nach § 199 StPO und Eroefffnungsverfahren: Anwendungsfall Mandant hat Anklageschrift erhalt…
10. **chatcontrol-csam-anwaltsgeheimnis-53-stpo** — Chat-Control CSAM Anwaltsgeheimnis und § 53 StPO Zeugnisverweigerungsrecht: Anwendungsfall Kanzlei prüft ob Chat-Control…
11. **hauptverhandlung-vorbereiten** — Hauptverhandlung im Strafverfahren vorbereiten: Anwendungsfall Strafverteidiger muss Hauptverhandlung strukturiert vorbe…
12. **insolvenzantrag-staatsanwaltschaft** — Insolvenzantrag-Massnahmen durch Staatsanwaltschaft im Wirtschaftsstrafrecht: Anwendungsfall Staatsanwaltschaft hat Inso…
13. **nebenklage-opfervertretung** — Nebenklage und Opfervertretung im Strafverfahren: Anwendungsfall Opfer einer Straftat moechte als Nebenklaeger am Verfah…
14. **plaedoyer-vorbereitung-strafverteidigung** — Plaedoyer für Strafverteidigung vorbereiten und strukturieren: Anwendungsfall nach Abschluss der Beweisaufnahme muss Str…
15. **schriftsatzkern-substantiierung** — Substantiierter Schriftsatzkern für Strafverfahren Einspruch und Revision: Anwendungsfall Strafverteidiger muss Einspruc…

---

## Skill: `einstieg-routing`

_Anwalts-Dashboard Fachanwalt Strafrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat._

# Anwalts-Dashboard Fachanwalt Strafrecht

> Vorladung, Durchsuchung, U-Haft, Anklage, Revision — Verfahrensphase entscheidet alles. Identität des Beschuldigten zuerst klären.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 311 II StPO: 1 Woche** sofortige Beschwerde. § 314 StPO: Berufung 1 Woche ab Verkündung. § 341 StPO: Revision 1 Woche ab Verkündung; § 345 StPO: Begründung 1 Monat ab Zustellung. § 33a StPO (Haftprüfung jederzeit). § 67 OWiG: Einspruch Bußgeld 2 Wochen. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Hier kein klassischer Anspruch: Tatvorwurf benennen (Norm + StGB- bzw. Nebenstrafrechts-§). Mitwirkung: Akteneinsicht § 147 StPO, Beweisantrag § 244 StPO, Verteidigerwahl § 137 StPO, Pflichtverteidigung § 140 StPO. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | AG Strafrichter / Schöffengericht (§§ 24 ff. GVG), LG große Strafkammer (§ 74 GVG), OLG (Staatsschutz, § 120 GVG). Bei Jugendlichen: JGG-Spruchkörper. | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Sofortige Beschwerde (1 Woche), Revisionsfrist (1 Woche / 1 Monat) tickt ab Verkündung/Zustellung. 🟠 Hauptverhandlung in 30 Tagen — Beweisanträge vorbereiten.
- **Beweislage:** 🟠 Beschuldigtenaussage NIE ohne Akteneinsicht. 🔴 Belastungszeugen: Konfrontationsrecht Art. 6 III d EMRK ausnutzen. 🟢 Selbstanzeige § 371 AO nur nach umfassender Aktenlage.
- **Wirtschaftlich:** 🔴 Berufstauglichkeit gefährdet (Beamte, Heilberufe, Approbation): parallel berufsrechtliche Schiene mitdenken. 🟠 Vermögensabschöpfung §§ 73 ff. StGB im Blick.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Untersuchungshaft / Haftbefehl** | `strafr-haftpruefung-haftbeschwerde-workflow` | Haftbeschwerde § 304 StPO, Haftprüfung § 117 StPO, mündliche Verhandlung erzwingen |
| Akteneinsicht & Strategie | `akteneinsicht-beantragen` | Antrag § 147 StPO, Wahl Verfahrensschiene, ggf. Schweigen / Einlassungsmemo |
| Beweisantrag vorbereiten | `strafr-dysfunk-beweisantrag-fundament` | Substantiierte Tatsachenbehauptung, Beweismittel, Konnexität |
| Revision prüfen | `revisionsbegruendung-paragraf-344-stpo` | Sach- vs. Verfahrensrüge, absolute Revisionsgründe § 338 StPO |
| Wirtschafts-/Vermögensabschöpfung | `strafr-vermoegensabschoepfung-spezial` | Einziehung §§ 73 ff. StGB, vermögenssichernde Maßnahmen § 111b StPO |

## Norm-Radar (live verifizieren)

- **§ 147 StPO** — Akteneinsicht des Verteidigers
- **§ 137 StPO** — Recht auf Verteidiger jederzeit
- **§ 244 StPO** — Beweisantragsrecht
- **§ 117 StPO** — Haftprüfung
- **§ 341 StPO** — Revisions-Einlegungsfrist (1 Woche)
- **§ 73 StGB** — Einziehung von Taterträgen

## Genau eine Rückfrage (nur wenn nötig)

> Welche **Verfahrensphase** läuft (Ermittlung · Anklage · Hauptverhandlung · Rechtsmittel · Vollstreckung), und sitzt der Mandant **in Haft**?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Leitentscheidungs-Anker (Such-Wegweiser, keine fertigen Zitate)

- **Verständigung § 257c StPO; Mitteilungspflichten** — BVerfG 2. Senat; BGH-Strafsenate — *live verifizieren auf* `bundesverfassungsgericht.de + bundesgerichtshof.de`
- **Beweisantragsrecht § 244 StPO; Konnexität** — BGH-Strafsenate — *live verifizieren auf* `bundesgerichtshof.de`
- **Faires Verfahren / Konfrontationsrecht Art. 6 III d EMRK** — EGMR — *live verifizieren auf* `hudoc.echr.coe.int`
- **Einziehung §§ 73 ff. StGB; verfassungsrechtliche Grenzen** — BVerfG / BGH-Strafsenate — *live verifizieren auf* `bundesverfassungsgericht.de + bundesgerichtshof.de`

> Diese Anker sind Sucheinstieg. Vor jeder Verwendung in Schriftsatz, Memo oder Mandantenbrief: konkrete Entscheidung in der freien Quelle prüfen und Datum, Aktenzeichen, Randnummer abklären. Kuratierte Anker-Sammlung in `references/leitentscheidungen-anker.md`.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.

---

## Skill: `mandat-triage-strafrecht`

_Strukturierte Eingangs-Abfrage für Strafmandate: Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungsha..._

# Strukturierte Eingangs-Abfrage für Strafmandate


## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Plaedoyer Vorbereitung** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Strafrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierte Eingangs-Abfrage für Strafmandate. Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungshaft Vollzug Hausverbot) Beschuldigtenrechte § 136 § 137 § 140 § 141 StPO Pflichtverteidiger-Bestellung Mitbeschuldigte (Konflikt-Check § 43a BRAO § 146 StPO). Sofort-Fristen-Check Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Akteneinsicht § 147 StPO, Rechtsmittel und U-Haft-Eskalation. Routing zu Akteneinsicht, Haftmanagement und Strafprozess-Cockpit.

### Mandat-Triage Strafrecht

## Ablauf — acht Fragen

### Frage 1 — Wer ruft an und für wen?

- Beschuldigter selbst
- Angehöriger
- Polizei (selten — Notdienst)
- Anderer Anwalt (Vertretung)

### Frage 2 — Akute Eilbedürftigkeit?

- Festnahme erfolgt — Vorführung läuft heute
- Untersuchungshaft seit Stunden / Tagen
- Durchsuchung läuft / steht bevor
- Aussage bei Polizei für heute terminiert
- Hauptverhandlung beginnt morgen

**Eskalation:** Festnahme U-Haft Durchsuchung → Telefon-Sofort an Anwalt; binnen einer Stunde Beistand; Anwesenheit bei Vernehmung Pflicht.

### Frage 3 — Verfahrensstadium?

- Ermittlungsverfahren bei Polizei (kein Aktenzeichen StA noch nicht)
- Ermittlungsverfahren bei Staatsanwaltschaft (Az StA vorhanden)
- Zwischenverfahren (Anklage zugestellt — Eröffnungsbeschluss?)
- Hauptverfahren (Hauptverhandlungstermin)
- Berufung / Revision
- Strafvollstreckung
- Strafvollzug (Vollzugsplan Lockerungen Strafaussetzung)

### Frage 4 — Tatvorwurf?

- Norm (§ ggf. StGB Nebengesetz)
- Strafrahmen — Vergehen unter ein Jahr Vergehen ab ein Jahr Verbrechen ab ein Jahr Mindeststrafe (§ 12 StGB)
- Bei Verbrechen oder Strafrahmen ab ein Jahr — notwendige Verteidigung § 140 StPO

### Frage 5 — Haftsituation?

- In Freiheit
- Vorgeführt — Vorführungsbeschluss / Haftbefehl?
- Untersuchungshaft — Haftgründe (Flucht-, Verdunkelungs-, Wiederholungs-)
- Strafvollzug

### Frage 6 — Mitbeschuldigte?

- Wer ist mitbeschuldigt?
- Ist Mitbeschuldigter bereits anwaltlich vertreten?
- Konflikt-Check § 43a Abs. 4 BRAO § 146 StPO Mehrfachverteidigung verboten

### Frage 7 — Aktenstand?

- Aktenstand nachgefragt?
- Akteneinsicht beantragt § 147 StPO
- Bei U-Haft haftrelevante Informationen nach § 147 Abs. 2 S. 2 StPO sichern; in der Regel Akteneinsicht

### Frage 8 — Wirtschaftliche Verhältnisse / Pflichtverteidigung?

- Pflichtverteidigung § 140 § 141 StPO bei notwendiger Verteidigung
- Vergütung nach RVG plus eventuell Honorarvereinbarung

## Routing-Matrix

| Verfahrensstadium | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| U-Haft | `strafprozess-haft-und-besuchsmanagement` | Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Sechs-Monats-Kontrolle § 121 StPO |
| Vorfeld Durchsuchung | Beschwerde § 304 StPO | ggf. nicht statthaft wenn beendet — Feststellungsantrag |
| Polizei-Vernehmung steht an | Verteidigerbeistand § 168c StPO | Termin verlegen oder begleiten |
| Anklage zugestellt | Stellungnahme zur Eröffnung | Frist nach § 201 StPO |
| Anzeige/Anklage § 188 StGB | `strafrecht-spezial-188-stgb-easy-verteidigung` | Strafantrag/besonderes öffentliches Interesse § 194 StGB, vollständiger Äußerungskontext, Art. 5 GG |
| Strafbefehl § 188 StGB | `strafrecht-spezial-188-stgb-anklage-und-strafbefehl` | Einspruch § 410 StPO binnen zwei Wochen ab Zustellung |
| Hauptverhandlung | `akteneinsicht-strafrecht-auswerten` | Beweisanträge vor Schluss Beweisaufnahme |
| Berufung/Revision | `strafprozess-rechtsmittel-und-notfristencockpit` | Berufung/Revision Einlegung binnen 1 Woche; Revisionsbegründung § 345 StPO gesondert berechnen |

## Konflikt-Check

- Mehrfachverteidigung verboten § 146 StPO
- § 43a Abs. 4 BRAO Interessenkollision
- Frühere Vertretung von Mitbeschuldigtem oder Geschädigtem prüfen

## Sofort-Fristen

- **Haftprüfung** § 117 Abs. 1 StPO — jederzeit
- **Haftbeschwerde** § 304 StPO — keine gesetzliche Wochenfrist wie bei sofortiger Beschwerde, aber praktisch sofort vorbereiten
- **Sechs-Monats-Prüfung** OLG § 121 StPO
- **Einspruch Strafbefehl** § 410 StPO zwei Wochen
- **Berufung** § 314 StPO eine Woche
- **Revision** § 341 StPO eine Woche; Revisionsbegründung § 345 StPO grundsätzlich ein Monat nach Ablauf der Einlegungsfrist, bei späterer Urteilszustellung ab Zustellung

## Eskalationspfad

- **Telefon-Sofort** Vorführung Untersuchungshaft Durchsuchung Vernehmung-Termin heute
- **Binnen einer Stunde** Anfahrt zur Vernehmung — Verteidigerbeistand
- **Heute** Akteneinsichtsantrag § 147 StPO, Haftprüfung § 117 StPO oder Haftbeschwerde § 304 StPO prüfen
- **Diese Woche** Stellungnahme Anklage Berufungseinlegung

## Ausgabe

- `triage-protokoll-strafrecht.md` mit acht Fragen
- Aktenanlage Az-Vorschlag
- Fristenbuch-Eintrag (Hauptfrist Vorfrist)
- Mandatsvereinbarung Vorlage mit Pflichtverteidigerbestellungs-Antrag falls notwendig
- Empfehlung Folge-Skill plus Begründung

## Quellen

- StPO §§ 117 121 137 140 141 146 147 168c 201 304 314 341 410
- StGB § 12 (Verbrechen-Vergehen)
- BRAO § 43a
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aktuelle Rechtsprechung Mandat-Triage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen Triage-Check

- § 112 StPO — Haftbefehl (Flucht-, Verdunkelungs-, Wiederholungsgefahr)
- § 117 StPO — Haftpruefungsantrag (jederzeit)
- § 118a StPO — Haftpruefungstermin mit muendlicher Verhandlung
- § 140 StPO — notwendige Verteidigung (Bestellungsgrunde)
- § 141 StPO — Pflichtverteidiger-Bestellung (Zeitpunkt, Ablauf)
- § 146 StPO — Verbot Mehrfachverteidigung
- §§ 10 ff. GwG — Identifizierungspflichten Sorgfaltspflichten Rechtsanwalt

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden: Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverte..._

# Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden


## Arbeitsbereich

**Orientierung** ordnet den Fall über die tragenden Prüfungslinien: Orientierung im Strafrecht-Mandat und Fallrouting, Untersuchungshaft und Haftprüfung nach §§ 112 ff, Verständigung § 257c StPO und Taeter-Opfer-Ausgleich § 46a. Arbeite zuerst die tragende Rechtsfrage heraus; Nebenaspekte werden nur verarbeitet, soweit sie Frist, Zuständigkeit, Beweislast oder das konkrete Arbeitsprodukt tatsächlich beeinflussen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Strafrecht-Mandat und Fallrouting: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und passendes Fachmodul finden. § 136 StPO Belehrung, § 137 StPO Verteidigerrecht, StGB Straftatbestaende. Prüfraster Deliktstyp allgemeines oder Wirtschaftsstrafrecht, Verfahrensstand Ermittlung Anklage Hauptverhandlung, Mandantenrolle Beschuldigter Zeuge Nebenklaeger. Output Mandat-Einordnung mit Weiterleitung zur richtigen Prüfungslinie. Abgrenzung zu Mandat-Triage-Strafrecht für ausführliche Erstaufnahme.

### Fachanwalt für Strafrecht — Orientierung

## FAO-Voraussetzungen

- **Theoretischer Lehrgang** 120 Stunden.
- **Drei Klausuren** zum Strafrecht.
- **60 Fälle** in den letzten drei Jahren, davon mindestens 40 Hauptverhandlungen mit eigener Beteiligung.
- Anmeldung bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| StGB Allgemeiner Teil | §§ 1 ff. StGB |
| StGB Besonderer Teil | §§ 80 ff. StGB |
| Strafverfahren | StPO §§ 1 ff. |
| Strafvollstreckung | StVollstrO StVollzG |
| Nebenstrafrecht | BtMG WaffG AO § 370 (Steuerhinterziehung) |
| Strafrecht Wirtschaft | §§ 263 263a 266 299 StGB GwG |
| Jugendstrafrecht | JGG |
| Beruf Strafverteidiger | § 137 StPO § 138 StPO § 142 StPO Pflichtverteidigung § 140 StPO |

## Typische Mandate

- Ermittlungsverfahren Erstvernehmung
- Untersuchungshaft (§§ 112 ff. StPO Haftprüfungsantrag § 117 StPO Haftbeschwerde § 304 StPO)
- Hauptverhandlung Strafrichter Schöffengericht Schwurgericht
- Verteidigung in Wirtschaftsstrafsachen (Wirtschaftsstrafkammer Landgericht)
- Berufung Revision Verfassungsbeschwerde
- Strafvollstreckung Bewährung Reststrafenaussetzung

## Notfristen

- **Berufung** § 314 StPO — **eine Woche** Notfrist.
- **Revision** § 341 StPO — **eine Woche** Notfrist.
- **Revisionsbegründung** § 345 StPO — **ein Monat**.
- **Beschwerde** § 311 StPO — **eine Woche**.
- **Verfassungsbeschwerde** § 93 BVerfGG — **ein Monat**.
- **Wiedereinsetzung** § 44 StPO — eine Woche.

## Hauptgerichte

- **Amtsgericht** Strafrichter § 25 GVG (Vergehen Privatklage oder keine höhere Strafe als zwei Jahre zu erwarten) Schöffengericht § 28 GVG (bis vier Jahre Straferwartung).
- **Landgericht** Große Strafkammer Wirtschaftsstrafkammer Schwurgericht.
- **OLG** Berufungs- und Revisionsinstanz; Anklage erstinstanzlich bei Staatsschutzdelikten.
- **BGH 1.–5. Strafsenat** Revisionsinstanz.

## Berufsverband

- Deutscher Strafverteidiger e. V. (DSV).
- Vereinigung Berliner Strafverteidiger.
- Strafverteidigervereinigung Niedersachsen / NRW / Bayern.

## Schnittstellen

- **aktenaufbereiter-strafrecht** für Aktenaufbereitung.
- **kanzlei-allgemein** für Fristenbuch und Versand.

## Hinweis

Plugin für Fachanwaltschaft-Orientierung. Tiefe Verteidigung erfordert die Erfahrung des Fachanwalts; insbesondere bei Schwurgerichts- und Wirtschaftsstrafrecht.

## Zentrale Strafrecht-Normen im Ueberblick

- §§ 1-2 StGB — Gesetzlichkeitsprinzip; keine Strafe ohne Gesetz (nullum crimen)
- §§ 13-16 StGB — Begehungs-/Unterlassungsdelikt, Vorsatz, Irrtum
- §§ 20-21 StGB — Schuldunfaehigkeit, verminderte Schuldfaehigkeit
- §§ 46-49 StGB — Strafzumessung, besonderer Milderungsgrund
- § 78 StGB — Verjährungsfristen (z.B. 30 Jahre bei Mord)
- §§ 112-130 StPO — Untersuchungshaft, Haftbefehl, Haftgruende, Haftpruefung
- §§ 136-136a StPO — Beschuldigtenbelehrung, Aussageverweigerungsrecht, Beweisverwertungsverbote
- §§ 140-142 StPO — notwendige Verteidigung, Pflichtverteidiger

## Aktuelle Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `orientierung-fristen-form-und-zustaendigkeit`

_Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg._

# Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg.

## Spezialwissen: Orientierung: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** StPO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Orientierung** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Strafrecht-Orientierung Fristen / Form / Zuständigkeit Bausteine
- **Sachliche Zuständigkeit GVG:**
 - **Strafrichter § 25 GVG:** Privatklagen § 374 StPO; allgemein bis Freiheitsstrafe 2 Jahre, sofern nicht hoeher beantragt.
 - **Schoeffengericht § 28 GVG:** bis Freiheitsstrafe 4 Jahre; alle Strafsachen, die nicht zu hoher Strafkammer oder Strafrichter gehoeren.
 - **Grosse Strafkammer § 76 GVG:** alle Strafsachen ab 4 Jahre erwarteter Freiheitsstrafe; bestimmte Wirtschaftsstrafsachen.
 - **Schwurgericht § 74 II GVG:** Toetungsdelikte §§ 211 ff. StGB, Eingriff in Verkehr mit Todesfolge.
 - **Oberlandesgericht § 120 GVG:** Staatsschutzdelikte (Hochverrat, Landesverrat, Terror).
- **Oertliche Zuständigkeit StPO:**
 - **§ 7 StPO:** Tatort - regelmaessig massgeblich.
 - **§ 8 StPO:** Wohnsitz Beschuldigter.
 - **§ 9 StPO:** Ergreifungsort.
 - **§ 13 StPO:** Verbundene Verfahren.
- **Fristen-Uebersicht (StPO):**
 - **Einspruch Strafbefehl § 410 StPO: 2 Wochen** ab Zustellung.
 - **Berufung § 314 StPO: 1 Woche** ab Verkuendung; Begruendung optional.
 - **Revision § 341 StPO: 1 Woche** Einlegung + § 345 StPO **1 Monat** Begruendung ab Zustellung schriftliche Urteilsausfertigung.
 - **Beschwerde § 311 StPO: 1 Woche** sofortige; § 304 StPO einfache unbefristet.
 - **Wiedereinsetzung § 44 StPO: 1 Woche** ab Wegfall des Hindernisses.
 - **Klageerzwingungsverfahren § 172 II StPO: Antrag 1 Monat** ab Bescheid GenStA.
- **Form-Re-Check:**
 - **Schriftform** zwingend für Rechtsmittel (Berufung, Revision, Beschwerde) und Einspruch.
 - **Unterschrift** Verteidiger / Mandant.
 - **Vollmacht** bei Vertretung.
 - **Begruendungs-Pflicht** Revision (Sach- oder Verfahrensruege; § 344 II StPO Substantiierung Verfahrensruege).
- **Rechtsweg:**
 - AG -> LG (Berufung § 312 StPO) -> OLG (Revision § 333 StPO bei LG-Urteil 1. Instanz oder Berufungsurteil).
 - **Sprungrevision § 335 StPO** moeglich (Sprung Berufung).
 - **Wiederaufnahme § 359 StPO** bei neuen Tatsachen / Beweismitteln.
- **EMRK Art. 6:** angemessene Verfahrensdauer als Korrektiv (Strafmilderung BGH-Linie).

---

## Skill: `erstgespraech-mandatsannahme`

_Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen: Erstgespraeach und Mandatsannahme im Strafrecht: Anwen..._

# Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Erstgespraeach und Mandatsannahme im Strafrecht: Anwendungsfall Beschuldigter oder Verdaechtiger meldet sich nach Polizeivorladung oder Festnahme und Strafverteidiger muss Mandat strukturiert aufnehmen. § 136 StPO Belehrung Schweigerecht, § 137 StPO Verteidigerrecht, § 147 StPO Akteneinsicht. Prüfraster Konflikt-Check, Schweigerecht kommunizieren, Sachverhalt aufnehmen, Akteneinsicht beantragen, Honorarvereinbarung treffen. Output Mandats-Aufnahmeprotokoll mit Sofortmassnahmen-Liste und Belehrungsprotokoll. Abgrenzung zu Wahlverteidiger-Mandat für spezifischen Mandatstyp und zu Mandat-Triage.

### Erstgespraech und Mandatsannahme im Allgemeines und Wirtschaftsstrafrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Allgemeines und Wirtschaftsstrafrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; oft mit Vorladung, Strafbefehl, Durchsuchungsbeschluss, Anklageschrift, U-Haft-Anordnung, Anhörung als Zeuge oder Anklageschrift mit Nebenklage-Option.
- Vor jeder weiteren Bearbeitung: erst Annahme klaeren, Rolle bestimmen (Beschuldigte/r, Verletzte/r oder Nebenklage, Zeuge/in mit Beistand), Konflikt- und GwG-Pruefung, Vollmacht, Gebührenvereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Rollenklarheit und Konstellation (10-15 Min.)

Erste Frage: Wofür braucht Mandantschaft Sie?

- **Beschuldigte oder Angeklagte** - Verteidigung im Strafverfahren.
- **Verletzte oder Anzeigeerstattende** - Beratung, Strafanzeige, Akteneinsicht der Verletzten, ggf. Nebenklage-Anschluss.
- **Zeuginnen oder Zeugen** - Zeugenbeistand gemaess § 68b StPO, Auskunftsverweigerungsrecht gemaess § 55 StPO.
- **Insolvenzverwalter/Geschaeftsfuehrung** mit StA-Berlin-Beruehrung - paralleles Insolvenz-/Strafverfahren.

Standard-Fragenraster:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle und Aktenzeichen StA / Gericht).
- Tatvorwurf in einem Satz (StGB-Paragraf, OWiG, Nebenstrafrecht).
- Konkrete fachliche Stossrichtung: Akteneinsicht, Beschuldigtenvernehmung, U-Haft, Strafbefehl-Einspruch, Hauptverhandlung, Revision, Anklage gegen Beschuldigte/n als Nebenklage.
- Bisherige Korrespondenz (Vorladung, Anhörungsbogen, Durchsuchung, Bescheide).
- **Fristenscreening sofort:** Einspruch gegen Strafbefehl 2 Wochen (§ 410 Abs. 1 StPO), Revisionseinlegung 1 Woche (§ 341 StPO), Revisionsbegruendung 1 Monat (§ 345 StPO), Klageerzwingung 1 Monat (§ 172 Abs. 2 StPO), Antrag auf gerichtliche Entscheidung (§ 23 EGGVG) 1 Monat, Beschwerdefristen § 311 StPO.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantsystem: Mit-Beschuldigte, Verletzte, frueheres Mandat?
- Bei Mehrfach-Beschuldigten zwingend pro Person eigene Verteidigung (§ 146 StPO).
- GwG-Identifizierung: amtlicher Lichtbildausweis, bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Auslandsbezug, Vermoegensherkunft, Tatvorwurf (insbesondere § 261 StGB Geldwaesche, § 370 AO Steuerhinterziehung).
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG, BRAK-Identifizierungsleitfaden).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### 3. Vollmacht und Akteneinsicht

- Strafprozessvollmacht (§§ 137 ff. StPO, BORA, RVG).
- Akteneinsichtsantrag gemaess § 147 StPO (Verteidigung) oder § 406e StPO (Verletzten-/Nebenklagevertretung) oder ohne Sondervorschrift für Zeugenbeistand.
- Bei Pflichtverteidigerbestellung Antrag gemaess § 141 StPO frueh stellen (Belehrung gemaess § 136 Abs. 1 S. 3 StPO).
- Bei Nebenklage: Anschlusserklaerung gemaess § 396 StPO und Pruefung der Nebenklage-Befugnis gemaess § 395 StPO.

### 4. Gebührenvereinbarung im Strafverfahren

Strafrechtsspezifische Gebührentatbestaende statt zivilrechtlicher Streitwert-Logik:

- **RVG-Strafsachen-Tatbestaende** (VV-RVG Teil 4 Abschnitt 1): Grundgebuehr Nr. 4100, Verfahrensgebuehr Ermittlungsverfahren Nr. 4104, Verfahrensgebuehr Gerichtsverfahren erster Instanz Nr. 4106 oder 4112 bzw. 4118 je nach Gericht, Terminsgebuehr Nr. 4108 bzw. Nr. 4114 bzw. Nr. 4120, Hauptverhandlungstag-Zuschlag bei Strafkammer.
- **Bei Bussgeldverfahren:** VV-RVG Teil 5 (Nrn. 5100 ff.).
- **Pflichtverteidigung:** Festgebuehren gemaess RVG-Tabelle Teil 4 Abschnitt 1 mit besonderem Gebührentatbestand für den bestellten Verteidiger.
- **Vereinbarungshonorar / Stundenhonorar:** zulaessig nach § 3a RVG mit Schriftform und ausdruecklichem Hinweis; oberhalb der gesetzlichen Gebuehr ueblich bei Wirtschaftsstrafrecht.
- **Erfolgshonorar:** nur in engen Grenzen gemaess § 4a RVG; im Strafverfahren regelmaessig problematisch (kein Erfolg im klassischen Sinne, Risiko des Wertungs-Widerspruchs).
- **Vorschuss:** Vorschussanforderung nach § 9 RVG, in Strafsachen ueblich pro Instanz oder pro Hauptverhandlungstag.
- **Bei Nebenklage:** Gebühren VV-RVG Teil 4 Abschnitt 2 (Nrn. 4124 ff.). Streitwert-Aequivalent nur für adhaesionsrechtliche Anspruche relevant.
- **Bei Adhaesion (§§ 403 ff. StPO):** Gebühren VV-RVG Teil 4 Abschnitt 6 (Nrn. 4143-4147), berechnet nach Gegenstandswert des geltend gemachten Anspruchs.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Verteidigung durch alle Instanzen) oder begrenzt (nur Akteneinsicht und Gutachten, nur Erstellung Einspruch gegen Strafbefehl, nur Zeugenbeistand für einen Vernehmungstermin).
- **Verweisen:** wenn Spezialgebiet ausserhalb (Wirtschaftsstrafrecht vs. allgemeines Strafrecht), oertlich unzuständig oder Mehrfachbeschuldigtenkonstellation.
- **Ablehnen:** Konflikt mit § 146 StPO, GwG-Hit beim Honorar, fehlende Vertrauensbasis.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Rolle, Konflikt-Check, GwG-Status, Tatvorwurf, Aktenzeichen.
2. **Frist-Liste** (Einspruch, Revisionseinlegung, Revisionsbegruendung, Beschwerdefristen, Anschluss-Frist Nebenklage, U-Haft-Pruefungsfristen § 121 StPO).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Bescheide, Schreiben, Anhörungsbogen).
4. **Naechster-Schritt-Plan:** binnen 24 / 48 / 72 h, Owner, Output (Akteneinsicht stellen, Pflichtverteidigerbeiordnung beantragen, U-Haft-Beschwerde).
5. **Honorarvereinbarung** unterschrieben oder Hinweis auf RVG-Festgebuehr / Pflichtverteidiger-Beiordnung.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO Strafrecht (§ 13 FAO).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- StGB, StPO, BtMG, AO (§§ 369 ff.), OWiG, JGG, Nebenstrafrecht (StVG, WaffG, KCanG, AWG, WiStrG 1954).
- RVG mit VV-RVG Teil 4 (Strafsachen) und Teil 5 (Bussgeldsachen).
- DSGVO und BDSG für den Umgang mit Mandanten- und Verletzten-Daten.

## Typische Fehler im Erstgespraech

- Rolle der Mandantschaft nicht klar getrennt - Mehrfachvertretung Beschuldigter und Nebenklaegerin im gleichen Verfahren ist berufsrechtswidrig.
- Frist uebersehen, weil Mandantschaft sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen, insbesondere Strafbefehl mit Zustellungsdatum).
- Pflichtverteidiger-Antrag erst spaet gestellt - Vergutungsrisiko für Wahlverteidiger bis Beiordnung.
- Akteneinsicht zu spaet beantragt - Hauptverhandlungsvorbereitung leidet.
- Honorarvereinbarung muendlich oder ohne § 3a-RVG-Form - Honorar nur in Hoehe der gesetzlichen Gebuehr durchsetzbar.
- GwG-Pruefung verfehlt - Risiko § 261 StGB beim Honorar-Bezug aus inkriminierter Quelle.

## Praxis-Checkliste

- [ ] Rolle der Mandantschaft eindeutig festgestellt
- [ ] Personalien und Aktenzeichen aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt (auch Mit-Beschuldigte gemaess § 146 StPO)
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Strafprozessvollmacht unterschrieben
- [ ] Akteneinsicht beantragt (§ 147 oder § 406e StPO)
- [ ] Pflichtverteidigerbestellung beantragt, soweit Voraussetzungen vorliegen (§ 140 StPO)
- [ ] Honorarvereinbarung schriftlich (§ 3a RVG) oder Hinweis auf RVG-Festgebuehr
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Strafbefehl mit Einspruchsfrist

Mandantschaft bringt Strafbefehl am Donnerstag, Einspruchsfrist 2 Wochen ab Zustellung. Handlungs-Sequenz:

1. Zustellungsdatum aus Strafbefehl auslesen (Zustellungsurkunde, EB).
2. Akteneinsicht (§ 147 StPO) sofort schicken.
3. Einspruch fristwahrend einlegen, Begruendung nachreichen.
4. Wiedereinsetzung in den vorigen Stand (§§ 44 ff. StPO) als Reserve dokumentieren.

### Konstellation B: U-Haft

Mandantschaft sitzt seit Wochen in U-Haft. Pflichtverteidiger noch nicht beantragt.

1. Pflichtverteidigerbestellung beantragen (§ 140 Abs. 1 Nr. 4 StPO).
2. Akteneinsicht beantragen, soweit § 147 Abs. 2 StPO nicht entgegensteht.
3. Haftpruefung (§ 117 StPO) oder Haftbeschwerde (§ 304 StPO).
4. Mandantengespraech in der JVA terminieren (Sprecherlaubnis).

### Konstellation C: Verletzte/r mit Nebenklage-Option

Mandantschaft ist Opfer einer Sexualstraftat oder schweren Koerperverletzung.

1. Akteneinsichtsantrag für Verletztenvertretung (§ 406e StPO).
2. Pruefung Nebenklagebefugnis (§ 395 StPO).
3. Antrag auf Beiordnung als Opferanwalt (§ 397a StPO).
4. Adhaesion (§§ 403 ff. StPO) und psychosoziale Prozessbegleitung (§ 406g StPO) erwaegen.
5. Cross-Ref: `fachanwalt-strafrecht-nebenklage-opfervertretung`.

### Konstellation D: Zeuge mit Auskunftsverweigerungsrecht

Mandantschaft hat Vorladung als Zeuge in einem Verfahren erhalten, ist aber selber Mit-Beschuldigte/r in anderer Sache.

1. Pruefung § 55 StPO (Selbstbelastungsgefahr) und § 52 StPO (Angehoerigenstellung).
2. Zeugenbeistand gemaess § 68b StPO; Beiordnung gemaess § 68b Abs. 2 StPO bei Bedrohung.
3. Vorbereitung der Aussage und Auskunftsverweigerung in der Vernehmung.
4. Cross-Ref: `fachanwalt-strafrecht-zeugenbeistand`.

### Konstellation E: Wirtschaftsstrafverfahren mit Insolvenzantrag der StA

Mandantschaft ist Geschaeftsfuehrer/in einer GmbH; StA hat Insolvenzantrag gemaess § 14 InsO gestellt, parallel laeuft Strafverfahren wegen Insolvenzverschleppung (§ 15a InsO) oder Untreue (§ 266 StGB).

1. Doppelgleisige Strategie: Strafverteidigung + Insolvenzverteidigung.
2. Pruefung Anhörungsantraege im InsO-Verfahren.
3. Vermoegensabschoepfung gemaess §§ 73 ff. StGB und Beschlagnahme gemaess § 111b StPO im Auge behalten.
4. Cross-Ref: `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft`.

## Mandanten-Erwartungsmanagement

- Realistische Strafmass- und Bewaehrungs-Prognose (nicht: "Wir bekommen sicher Freispruch").
- Verfahrensdauer: Ermittlungsverfahren Wochen bis Monate, Hauptverhandlung Termine pro Instanz, Revision mehrere Monate.
- Verstaendigungschance gemaess § 257c StPO und Einstellung gemaess § 153a StPO als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Mandatsbogen-Muster (Mindestinhalt für Strafsachen)

- Mandantschaft (Name, Geburtsdatum, Anschrift, Telefon, E-Mail).
- Rolle (Beschuldigte, Nebenklaegerin, Zeugin, Insolvenzschuldnerin/GF).
- Aktenzeichen StA / Gericht / Polizei.
- Tatvorwurf (Paragraf, Tatzeit, Tatort).
- Kurzbeschreibung Sachverhalt (5-10 Saetze).
- Ziel des Mandats (eine Zeile).
- Strittige Fragen (bullet).
- Geprueft: Konflikt - GwG - Vollmacht.
- Gebührentatbestaende (Nrn. 4100 ff. VV-RVG / Vereinbarung).
- Frist-Liste.
- Aktenanlage Datum.
- Naechster-Schritt.

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für Verstaendigung gemaess § 257c StPO, Einstellung gemaess § 153a StPO und Adhaesion.
- `schriftsatzkern-substantiierung` (im selben Plugin) für Verteidigungsschriftsaetze (Einspruch, Revision, Klageerzwingung).
- `fachanwalt-strafrecht-nebenklage-opfervertretung` (im selben Plugin) für Verletzten- und Nebenklagevertretung.
- `fachanwalt-strafrecht-zeugenbeistand` (im selben Plugin) für Zeugenbeistand gemaess § 68b StPO.
- `fachanwalt-strafrecht-adhaesionsverfahren` (im selben Plugin) für Adhaesion.
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` (im selben Plugin) für parallelen Insolvenzantrag der StA.
- `kanzlei-allgemein` für Konflikt-, GwG- und Aktenanlage-Routinen.

## Aktuelle Rechtsprechung Erstgespraech / Mandatsannahme

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Erstgespraech Normen-Check

- § 136 Abs. 1 StPO — Beschuldigtenbelehrung: Schweigerecht, Verteidigerwahl
- § 137 StPO — freie Wahl des Verteidigers
- § 140 StPO — notwendige Verteidigung: Katalog der Pflichtfaelle
- § 146 StPO — Verbot Mehrfachvertretung
- §§ 10-17 GwG — Identifizierung, Risikoeinschaetzung, Dokumentation
- § 261 StGB — Geldwaesche: Strafbarkeit auch des Verteidigers bei Vorsatz/Leichtfertigkeit
- § 3a RVG — schriftliche Honorarvereinbarung; Mindestangaben

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** StPO.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Fachanwalt** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Strafrecht-Fachanwalt Erstpruefung Bausteine
- **Mandantenrolle praezisieren:**
 - **Beschuldigter / Angeklagter:** Verteidigerbestellung § 137 StPO; ggf. notwendige Verteidigung §§ 140-141 StPO.
 - **Geschaedigter / Nebenklage § 395 StPO:** Antrag Anschluss; Antragsdelikte (§§ 174-184k StGB, § 230 StGB, § 263a StGB); Zeugnis-Beistand § 68b StPO.
 - **Adhaesionsverfahren §§ 403-406c StPO:** zivilrechtliche Anspruchsverfolgung im Strafverfahren.
 - **Zeuge:** §§ 52 StPO Angehoerigenzeugnis; § 55 StPO Auskunftsverweigerung; Zeugnisbeistand.
 - **Klageerzwingung § 172 StPO:** Verletzter beantragt Erhebung der öffentlichen Klage.
- **Verfahrensstand-Triage:**
 - **Ermittlungsverfahren:** Akteneinsicht § 147 StPO; Stellungnahme StA; Schweigerecht § 136 StPO.
 - **Zwischenverfahren §§ 199-211 StPO:** Eroeffnungsbeschluss-Pruefung; Einwaende § 201 StPO; Hilfsbeweisantraege.
 - **Hauptverhandlung:** Beweisantraege § 244 StPO; Verstaendigung § 257c StPO; Schlussvortrag.
 - **Rechtsmittel:** Berufung § 314 StPO (1 Woche); Revision §§ 341, 345 StPO (1 Woche / 1 Monat); Beschwerde § 304 StPO.
 - **Vollstreckungsverfahren:** Strafrest § 57 StGB; Bewaehrungswiderruf § 56f StGB.
- **Tatvorwurfsklasse:**
 - **Vergehen § 12 II StGB** (Mindeststrafe unter 1 Jahr): Strafbefehl § 407 StPO moeglich.
 - **Verbrechen § 12 I StGB** (Mindeststrafe 1 Jahr): notwendige Verteidigung § 140 I Nr. 2 StPO; Schwurgericht / grosse Strafkammer.
- **Mandantenziel-Hierarchie:**
 - Schuldspruch vermeiden (Freispruch).
 - Einstellung §§ 153, 153a StPO.
 - Strafmilderung.
 - Bewaehrung sichern (§ 56 StGB).
 - Reputation schuetzen (BZRG, FZR, Berufsrecht).
- **Honoraranfrage / Verguetungsvereinbarung § 3a RVG schriftlich** wenn Wahlanwaltsmandat; bei Pflichtverteidigung Festbetragstarif RVG VV 4100 ff.

---

## Skill: `output-waehlen`

_Output-Wahl für Fachanwalt Strafrecht: stimmt Adressat (Beschuldigter/Angeklagter, Staatsanwaltschaft, Verletzte/Nebenkläger), Frist (Revision 1 Woche/1 Mon. § 341 StPO) und Form auf den Zweck ab — typische Outputs: Akteneinsicht-Antrag, Beweisantrag, Plädoyer._

# Output wählen

## Einsatzlage

Diese Output-Weiche für **Fachanwalt Strafrecht** entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist.

## Fachlandkarte dieses Plugins

- `workflow-redteam-qualitygate` — Adhaesionsverfahren Ermittlungsverfahren
- `strafrecht-spezial-aussagepsychologie-staatsanwaltschaft-replik` — Aussagepsychologie Staatsanwaltschaft
- `chatcontrol-csam-anwaltsgeheimnis-53-stpo` — Chatcontrol Csam Einlassung Vorbereiten
- `ergaenzt-mandantenkommunikation-entscheidungsvorlage` — Ergaenzt Fachanwalt Insolvenzantrag RED Team Korrektur
- `fa-strafrecht-quellen-frist-next` — FA Strafrecht Quellen Frist Next
- `freiheitsstrafe-paragraf-57-stgb` — Freiheitsstrafe Paragraf 57 STGB
- `hauptverhandlung-quellenkarte` — Hauptverhandlung Quellenkarte
- `strafrecht-spezial-koerperverletzung-223-stgb-grund` — Koerperverletzung STGB Todesfolge
- `mandat-triage-strafrecht` — Mandat Triage Plaedoyer Vorbereitung
- `nebenklage-compliance-dokumentation-und-akte` — Nebenklage Nebenstrafrecht Opfervertretung
- `notwehr-paragraf-32-stgb` — Notwehr Paragraf 32 STGB
- `orientierung-mandat-fachanwaltschaft` — Orientierung
- `strafrecht-spezial-raub-249-stgb` — Raub Rechtsbeugung
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Ergebnistyp bestimmen: Schriftsatz an Beschuldigter, Strafverteidiger, Staatsanwaltschaft, Ermittlungsrichter, Vorsitzender, Schöffen, Zeuge, Nebenkläger, JVA, Mandantenmemo, Risikobericht, Vertragsentwurf, Entscheidungsvorlage, Behörden-Stellungnahme — was braucht der Mandant wirklich?
- Pflichtformate festlegen: Tenor / Antrag / Begründung (Anspruchsgrundlage, Tatbestand, Subsumtion, Ergebnis); konkrete Norm-Pinpoints im Strafrecht und Strafprozessrecht (StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 53, 53a, 100a, 100b, 102, 105, 112, 116, 136, 137, 140, 141, 147, 152, 153, 153a, 160, 163a, 168c, 169, 170, 200, 201, 203, 244, 257c, 261, 264, 265, 267, 268, 304, 341, 344, 349) einarbeiten.
- Adressat-Klarheit: Sprache, Detailtiefe und juristische Vorbildung des Empfängers berücksichtigen; bei Mandant ohne Vorbildung Klartext-Zusammenfassung voranstellen.
- Beweis- und Anlagenstruktur planen (chronologisch, thematisch, K- und B-Anlagen); Bezugnahmen sauber kennzeichnen.
- Quellenfußnoten und Zitierweise sichern; offene Punkte und Annahmen explizit als solche kennzeichnen.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `adhaesionsverfahren`

_Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig Schmerzensgeld oder Schadensersatz geltend machen ohne separaten Zivilprozess: Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereite..._

# Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig Schmerzensgeld oder Schadensersatz geltend machen ohne separaten Zivilprozess


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Adhaesionsverfahren § 403 StPO im Strafverfahren vorbereiten: Anwendungsfall Opfer will im Strafverfahren gleichzeitig Schmerzensgeld oder Schadensersatz geltend machen ohne separaten Zivilprozess. §§ 403-406c StPO Adhaesionsverfahren, § 823 BGB Schadensersatz, § 253 BGB Schmerzensgeld. Prüfraster Zulässigkeit im Strafverfahren, Antragsschrift-Anforderungen, Beweisangebot, taktische Abwaegung Adhaesion vs. separater Zivilprozess. Output Adhaesionsantrag mit Schadensaufstellung und taktischer Einordnung. Abgrenzung zu Taeter-Opfer-Ausgleich § 46a StGB und zu Verständigung § 257c StPO.

### Adhäsionsverfahren im Strafverfahren

## Kernsachverhalt & Mandantenfragen

Das Adhäsionsverfahren verbindet Strafprozess und Zivilrecht. Es spart der verletzten Person eine eigenständige Zivilklage. Gleichzeitig ist es für die Verteidigung ein Instrument zur Schadensminimierung: Ein Adhäsionsvergleich kann das Strafmaß erheblich beeinflussen (§ 46a StGB).

**8 Kaltstart-Rückfragen:**

1. Was ist die konkrete Straftat und wann wurde sie begangen? Liegt ein Aktenzeichen vor?
2. Welche zivilrechtlichen Schäden sind entstanden: Körperverletzung (Schmerzensgeld), Vermögensschaden (Betrug, Diebstahl), Sachschäden, Verdienstausfall?
3. Liegen ärztliche Atteste, Behandlungsberichte oder Gutachten zur Schadenshöhe vor?
4. Hat die Versicherung (z.B. Krankenversicherung, Unfallversicherung) bereits Leistungen erbracht? Forderungsübergang nach § 116 SGB X prüfen.
5. Ist der/die Angeklagte zahlungsfähig? Pfändbare Vermögenswerte vorhanden oder Insolvenz droht?
6. Besteht parallele Nebenklage oder soll der Adhäsionsantrag ohne Nebenklage gestellt werden?
7. Ist ein außergerichtlicher Vergleich mit dem/der Angeklagten bereits diskutiert oder gescheitert?
8. Welcher Betrag soll konkret geltend gemacht werden, oder soll das Schmerzensgeld dem Ermessen des Gerichts überlassen bleiben?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 403 StPO | Adhäsionsrecht: Verletzte kann vermögensrechtliche Ansprüche aus der Tat im Strafverfahren geltend machen |
| § 404 StPO | Form und Inhalt des Adhäsionsantrags; schriftlich oder zu Protokoll; bis Schluss der Beweisaufnahme |
| § 405 StPO | Adhäsionsvergleich als Vollstreckungstitel; Protokollierung in der Hauptverhandlung |
| § 406 StPO | Entscheidung durch Strafgericht; Grundurteil; Absehen von Entscheidung bei Verfahrensverzögerung |
| § 406a StPO | Rechtsmittel gegen Adhäsionsentscheidung; eingeschränkte Berufungsmöglichkeit |
| § 406b StPO | Vorläufige Vollstreckbarkeit des Adhäsionsurteils |
| § 406c StPO | Vollstreckbarerklärung des Vergleichs |
| § 472a StPO | Kosten des Adhäsionsverfahrens für Verletzte: grundsätzlich kostenfrei |
| § 46a StGB | Täter-Opfer-Ausgleich und Schadenswiedergutmachung als Strafmilderungsgrund |
| § 46 Abs. 2 StGB | Strafzumessung: Schadenswiedergutmachung berücksichtigungsfähig |
| § 253 Abs. 2 BGB | Schmerzensgeld bei Körper-, Gesundheits-, Freiheitsverletzung oder sexueller Selbstbestimmung |
| §§ 249–252 BGB | Art und Umfang des Schadensersatzes; Naturalrestitution, Wertersatz |
| §§ 823–826 BGB | Deliktsrecht: Grundlagen der Schadensersatzpflicht |
| § 830 BGB | Mittäter und Beteiligte haften als Gesamtschuldner |
| § 116 SGB X | Forderungsübergang bei Sozialleistungsträgern (Krankenkasse, Rentenversicherung) |

---

## Leitentscheidungen (Stand Mai 2026)

| Aktenzeichen | Gericht / Datum | Tragende Aussage | Offene Fundstelle |
|---|---|---|---|
| 3 StR 340/24 | BGH (3. Strafsenat), Beschluss 09.01.2025 | Adhäsionsentscheidung im Strafverfahren — Begründungsanforderungen an Schmerzensgeldzumessung; Strafgericht muss die maßgeblichen Zumessungsgesichtspunkte (Verletzungsbild, Dauer, Folgen) erkennbar machen | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=09.01.2025&Aktenzeichen=3+StR+340/24 |
| 4 StR 232/25 | BGH (4. Strafsenat), Beschluss 20.11.2025 | Zusammenspiel TOA / Schadenswiedergutmachung (§ 46a StGB) und Adhäsionsforderung — Strafmilderung setzt kommunikativen Aussöhnungsprozess voraus, nicht nur Zahlung | https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25 |

Weitere Entscheidungen vor Verwendung live in dejure.org/openjur.de mit Gericht, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Prüfschema Adhäsionsverfahren

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Anspruchsgrundlage prüfen: § 823 BGB (Körperverletzung, Sachschaden), § 826 BGB (sittenwidrige Schädigung bei Betrug), § 249/253 BGB (Schaden und Schmerzensgeld) | §§ 249, 253, 823 BGB |
| 2 | Verletzteneigenschaft prüfen: Nur unmittelbar Verletzte (§ 403 StPO); mittelbar Betroffene ausgeschlossen | § 403 StPO |
| 3 | Forderungsübergang prüfen: § 116 SGB X bei Krankenkassenleistungen; Eigenanteil ermitteln | § 116 SGB X |
| 4 | Schadenshöhe ermitteln: Schmerzensgeld nach Tabellen (Hacks/Slizyk); materieller Schaden beziffern; Feststellungsantrag für Zukunftsschäden | § 253 Abs. 2 BGB |
| 5 | Vollstreckungsperspektive prüfen: Zahlungsfähigkeit des/der Angeklagten; Insolvenzsituation; pfändbares Vermögen | §§ 704, 794 ZPO |
| 6 | Adhäsionsantrag formulieren: bestimmter Antrag (Zahlung, Feststellung, Herausgabe); Sachverhalt; Beweismittel | § 404 StPO |
| 7 | Fristwahrung: Antrag bis Beginn der Schlussvorträge (spätestens); frühzeitig einreichen | § 404 Abs. 1 StPO |
| 8 | Vergleichsstrategie aus Verteidigung: § 46a StGB als Strafmilderungsargument; Ratenvereinbarung vorbereiten | § 46a StGB |
| 9 | Vergleich nach § 405 StPO: In Hauptverhandlung protokollieren lassen; wird Vollstreckungstitel | § 405 StPO |
| 10 | Grundurteil und Folgeentscheidung: Bei Bezifferungsproblemen Grundurteil nach § 406 Abs. 1 S. 2 StPO; Quantifizierung im Zivilverfahren | § 406 Abs. 1 S. 2 StPO |
| 11 | Absehen-Antrag der Verteidigung: § 406 Abs. 1 S. 3–6 StPO – wenn Adhäsion Verfahren wesentlich verzögert | § 406 StPO |
| 12 | Vollstreckung: Titel nach § 794 ZPO; Gerichtsvollzieher, Forderungspfändung; bei Insolvenz: Tabellenanmeldung | § 794 ZPO |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Adhaesionsverfahren fuehren | Adhaesionsantrag; Template unten |
| Variante A — Mandant will Strafverfahren trennen | Zivilklage separat; Adhaesion entfaellt |
| Variante B — Strafgericht verweist Adhaesion | Nachfolge-Zivilklage; Bindungswirkung des Strafurteils |
| Variante C — Schadenshoehe unklar | Feststellungsklage zuerst; Leistungsklage nach Konkretisierung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 – Adhäsionsantrag auf Schmerzensgeld

```
An das [Gericht]
Aktenzeichen: [...]

Adhäsionsantrag gemäß §§ 403 ff. StPO

In der Strafsache gegen [Name Angeklagte/r]
wegen [Tatvorwurf]

beantragt die Verletzte [Name] durch ihre anwaltliche Vertretung:

1. Die/den Angeklagte/n wird verurteilt, an die Verletzte
 ein angemessenes Schmerzensgeld zu zahlen, dessen Höhe
 in das Ermessen des Gerichts gestellt wird, jedoch den
 Betrag von [z.B. 15.000 Euro] nicht unterschreiten sollte,
 nebst Zinsen in Höhe von fünf Prozentpunkten über dem
 Basiszinssatz seit Rechtshängigkeit dieses Antrags.

2. Es wird festgestellt, dass die/der Angeklagte verpflichtet
 ist, der Verletzten alle weiteren materiellen und immateriellen
 Schäden zu ersetzen, die aus der Tat vom [Datum] künftig noch
 entstehen, soweit Ansprüche nicht auf Dritte oder Sozial-
 versicherungsträger übergegangen sind.

Begründung:
Die Verletzte erlitt durch die Tat vom [Datum] folgende
Verletzungen: [konkret aufzählen]. Sie wurde [X Tage]
stationär behandelt und befand sich [X Wochen] in ambulanter
Therapie. Behandlungsunterlagen werden als Anlage 1 bis 3
beigefügt.

Das Schmerzensgeld ist nach den Grundsätzen der Ausgleichs-
und Genugtuungsfunktion (§ 253 Abs. 2 BGB) zu bemessen.
Vergleichbare Verletzungen werden in der Rechtsprechung mit
[Betragsbereich] bewertet (Slizyk, Beck'sche Schmerzensgeld-
tabelle, [aktuelle Auflage], Nr. [XX]).

[Ort, Datum]
[Unterschrift]
```

### Baustein 2 – Adhäsionsvergleich (Protokollvorlage)

```
In der Hauptverhandlung am [Datum]
Aktenzeichen: [...]

schließen die Parteien folgenden Vergleich gemäß § 405 StPO:

1. Die/der Angeklagte zahlt an die Verletzte [Name]
 zur Abgeltung sämtlicher Schmerzensgeld- und Schadens-
 ersatzansprüche aus der Tat vom [Datum] einen Betrag
 von [X Euro].

2. Zahlung erfolgt in monatlichen Raten von [X Euro]
 erstmals zum [Datum]; Gesamtfälligkeit bei Zahlungs-
 verzug mit einer Rate.

3. Mit Zahlung des Gesamtbetrags sind alle Ansprüche der
 Verletzten aus der Tat vom [Datum] abgegolten.

4. Die Gerichtskosten des Adhäsionsverfahrens trägt
 [je nach Vereinbarung].

Dieser Vergleich wird als Prozessvergleich nach § 794 Abs. 1
Nr. 1 ZPO protokolliert.

[Unterschriften beider Seiten und Gericht]
```

### Baustein 3 – Verteidigung: Antrag auf Absehen von Entscheidung § 406 Abs. 1 S. 3 StPO

```
An das [Gericht]
Aktenzeichen: [...]

Antrag auf Absehen von der Entscheidung im Adhäsionsverfahren
gemäß § 406 Abs. 1 S. 3 StPO

In der Strafsache gegen [Name Angeklagte/r]

beantragt die Verteidigung,

von einer Entscheidung über den Adhäsionsantrag der Verletzten
abzusehen, da die Entscheidung eine dem Strafverfahren nicht
angemessene Beweisaufnahme erfordern würde und das Strafver-
fahren wesentlich verzögern würde (§ 406 Abs. 1 S. 5 StPO).

Begründung:
Zur Klärung der Schadenshöhe wäre ein medizinisches Sach-
verständigengutachten einzuholen. Der Adhäsionsantrag bezieht
sich auf Schäden in Höhe von [Betrag EUR]. Die Klärung der
Kausalität zwischen Tat und behaupteten Folgeschäden bedarf
einer umfangreichen medizinischen Beurteilung, die den Rahmen
des Strafprozesses sprengt.

[Ort, Datum]
[Unterschrift Verteidigung]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Anspruchsgrundlage (§ 823 BGB) | Verletzte trägt Tatbegehung, Verletzung, Kausalität; im Adhäsionsverfahren erleichtert durch Bindungswirkung des Strafurteils zur Tat |
| Schadenshöhe (Schmerzensgeld) | Verletzte muss Mindestbetrag darlegen; Gericht schätzt nach § 287 ZPO (analog) |
| Forderungsübergang § 116 SGB X | Sozialleistungsträger zeigt Übergang an; Verletzte muss nur Eigenanteil nachweisen |
| Adhäsionsvergleich | Einigung trägt sich selbst; Vollstreckungstitel durch Protokollierung |
| Absehen wegen Verfahrensverzögerung | Gericht entscheidet von Amts wegen; Verteidigung kann Sachverhalt darlegen |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Bis Schluss der Beweisaufnahme | Adhäsionsantrag muss vor Schlussvorträgen gestellt sein | § 404 StPO |
| Ab Urteilszustellung: 1 Woche | Berufung/Revision gegen Adhäsionsausspruch | § 406a StPO |
| Ab Urteilsrechtskraft | Vollstreckung aus Adhäsionsurteil beginnt | § 704, § 794 ZPO |
| 3 Jahre | Verjährung deliktsrechtlicher Ansprüche (§ 195 BGB) ab Kenntnis | § 199 BGB |
| 30 Jahre | Verjährung des titulierten Anspruchs nach § 197 BGB | § 197 BGB |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Adhäsionsantrag verzögert das Strafverfahren" | § 406 Abs. 1 S. 6 StPO — Absehen nur bei wesentlicher Verzögerung; Schmerzensgeld-Antrag wird durch S. 6 a. F. besonders geschützt; aktuelle Begründungsanforderungen siehe BGH 09.01.2025 — 3 StR 340/24 |
| "Forderungsübergang nach § 116 SGB X schließt Adhäsion aus" | Nur soweit Anspruch übergegangen ist; Eigenbeteiligung (Schmerzensgeld soweit nicht gedeckt) verbleibt bei der Verletzten |
| "Angeklagte/r ist insolvent; Adhäsion sinnlos" | § 302 InsO schließt Restschuldbefreiung bei vorsätzlichen unerlaubten Handlungen aus; Titel hat langfristigen Wert |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Adhäsionsantrag kostenfrei für Verletzte | § 472a StPO: keine Gerichtskosten für Verletzte im Adhäsionsverfahren |
| Anwaltsgebühren (Verletztenvertretung) | VV-RVG Nr. 4143 (Verfahrensgebühr), Nr. 4145 (Terminsgebühr), Nr. 4146 (Vergleichsgebühr); Streitwert = Adhäsionsforderung |
| Bei Beiordnung § 397a StPO | Adhäsionsgebühren zusätzlich zur Nebenklagegebühr aus Staatskasse |
| Angeklagter zahlt Kosten bei Adhäsionsverurteilung | Kosten des Adhäsionsverfahrens als Nebenfolge im Strafurteil |
| Angeklagter bei Vergleich § 405 StPO | Kostenregelung im Vergleich frei vereinbar |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Schneller Vollstreckungstitel gewünscht | Adhäsionsantrag frühzeitig stellen; Vergleich nach § 405 StPO anstreben |
| Angeklagter will Strafmilderung | Schadenswiedergutmachung proaktiv anbieten; § 46a StGB nutzen; Vergleich vor Urteil |
| Hohe Schadensummen in Betrugsfall | Adhäsion kombinieren mit Verbleib im Strafverfahren für Bindungswirkung zur Tatbegehung |
| Angeklagter ist insolvent | Adhäsion trotzdem beantragen; § 302 InsO schließt Restschuldbefreiung aus; Titel 30 Jahre vollstreckbar |
| Gericht neigt zu § 406-Absehen | Beweise vorab vollständig vorlegen; Komplexität minimieren; Schmerzensgeld pauschal schätzen lassen |
| Schmerzensgeldzumessung im Strafurteil | Begründungsanforderungen nach BGH 09.01.2025 — 3 StR 340/24 beachten; Verletzungsbild, Dauer, Folgen erkennbar machen |

---

## Anschluss-Skills

- `fachanwalt-strafrecht-nebenklage-opfervertretung` – Nebenklage und Adhäsion kombiniert führen
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` – Adhäsionsforderung in der Insolvenz des Angeklagten
- `plaedoyer-vorbereitung-strafverteidigung` – Schadenswiedergutmachung als Strafmilderungsargument
- `fachanwalt-strafrecht-zeugenbeistand` – Begleitung der Verletzten als Zeugin

---

## Quellen (Stand Mai 2026)

- BGH 09.01.2025 — 3 StR 340/24 (Adhäsion / Schmerzensgeldbegründung): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=09.01.2025&Aktenzeichen=3+StR+340/24
- BGH 20.11.2025 — 4 StR 232/25 (TOA § 46a StGB, kommunikativer Prozess): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25
- §§ 403–406c StPO, § 472a StPO: https://dejure.org/gesetze/StPO/403.html
- Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; weitere Rechtsprechung vor Ausgabe in dejure.org / openjur.de mit Gericht, Datum, Aktenzeichen und Aussage verifizieren.

---

## Skill: `anklage-reaktion`

_Reaktion auf Anklageerhebung nach § 199 StPO und Eroefffnungsverfahren: Anwendungsfall Mandant hat Anklageschrift erhalten und Verteidiger muss strategisch auf Eroeffnungsverfahren reagieren: Reaktion auf Anklageerhebung nach § 199 StPO und Eroefffnungsverf..._

# Reaktion auf Anklageerhebung nach § 199 StPO und Eroefffnungsverfahren: Anwendungsfall Mandant hat Anklageschrift erhalten und Verteidiger muss strategisch auf Eroeffnungsverfahren reagieren


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Reaktion auf Anklageerhebung nach § 199 StPO und Eroefffnungsverfahren: Anwendungsfall Mandant hat Anklageschrift erhalten und Verteidiger muss strategisch auf Eroeffnungsverfahren reagieren. § 199 StPO Eroeffnungsverfahren, § 203 StPO hinreichender Tatverdacht, § 153 StPO Einstellung, § 244 StPO Beweisantrag. Prüfraster Anklage auf Vollständigkeit nach § 200 StPO prüfen, Eroeffnungsantrag auf Schwaechen prufen, Einstellungsantrag oder Beweisantrag taktisch abwaegen. Output Stellungnahme-Schreiben zum Eroefffnungsverfahren mit strategischen Optionen. Abgrenzung zu Hauptverhandlung-Vorbereiten und zu Einlassung-Vorbereiten.

### Anklage-Reaktion

## 1) Anklage-Prüfung

### Pflicht-Inhalte § 200 StPO

- Beschuldigter mit Personalien
- Tatvorwurf mit Zeit, Ort, Mittel
- Strafgesetzliche Bestimmungen
- Anklage-Schluss
- Beweismittel

### Mangelhafte Anklage

- Bei Form-Mangel: Eröffnungs-Antrag-Verweigerung
- Bei Unbestimmtheit: Spezialisierungs-Antrag

## 2) Eröffnungs-Verfahren §§ 199-207 StPO

### Schwurgericht

- Prüfung hinreichender Tatverdacht
- Wahrscheinlichkeit Verurteilung > Freispruch

### Eröffnungs-Beschluss

- Beschluss zur Hauptverhandlung
- Anfechtbar nicht direkt

### Ablehnungs-Antrag § 204 StPO

- Bei mangelndem Tatverdacht
- Verfahrens-Einstellung

## 3) Einstellungs-Anträge

### § 153 StPO — Geringfuegigkeit

- Geringe Schuld
- Kein öffentliches Interesse
- Ohne Auflage

### § 153a StPO — Mit Auflage

- Geldzahlung an gemeinnützige Einrichtung
- Wiedergutmachung
- Therapie
- Sozialstunden

### Vorteile

- Keine Verurteilung
- Kein Strafregister-Eintrag (bei § 153 StPO; bei 153a teils ja)
- Schnelle Verfahrens-Beendigung

## 4) Beweis-Anträge § 244 StPO

### Pflicht-Beweisantrag

- Konkretes Beweisthema
- Bestimmtes Beweismittel
- Prüfungs-Pflicht Gericht

### Ablehnungs-Gründe § 244 III StPO

- Bewiesen / widerlegt
- Unerheblich
- Beweismittel unerreichbar
- Verschleppungs-Absicht

## 5) Hauptverhandlungs-Vorbereitung

### Sachverständigen-Prüfung

- Bei medizinischen / technischen Fragen
- Eigen-Sachverständiger
- Antrag auf gerichtlichen SV

### Zeugen-Prüfung

- Glaubwürdigkeits-Analyse
- Aussage-Konstanz
- Indirekte Beweise

### Plaedoyer-Strategie

- Pro Tatzeitpunkt
- Pro Beweismittel
- Strafmilderungs-Argumente

## 6) Workflow

### Phase 1 — Anklage-Auswertung

- Vollständige Akteneinsicht
- Beweis-Sichtung
- Schwachstellen-Identifikation

### Phase 2 — Vorab-Anträge

- Beweisanträge
- Einstellungs-Anträge
- Befangenheits-Anträge

### Phase 3 — Hauptverhandlung

- Tatsachen-Vortrag
- Beweis-Konstatierung
- Plaedoyer

### Phase 4 — Urteil

- Begründung erfassen
- Berufungs-Strategie

## 7) Strafmass-Reduzierung

### Strafzumessungs-Gründe § 46 StGB

- Schwere der Tat
- Vorleben
- Geschaedigten-Beziehung
- Bewährung-Aussicht

### Praktische Aspekte

- Schadens-Wiedergutmachung
- Gestaendnis (zeitlich, glaubhaft)
- Therapie-Bereitschaft
- Sozial-Verhalten

## 8) Berufung § 312 StPO

### Voraussetzungen

- Frist 1 Woche
- Schriftform
- Begründung beim Berufungsgericht (LG)

### Strategie

- Vollumfaengliche Anfechtung oder beschraenkt auf Strafmass
- Neue Beweise / Zeugen

## 9) Revision § 333 StPO

- Frist 1 Woche
- Rechtsfehler-Prüfung (nicht Tatsachen!)
- BGH oder OLG

## 10) Typische Fehler

1. **Beweisanträge zu pauschal** -> Ablehnung
2. **Einstellungs-Antrag versäumt** zur richtigen Zeit
3. **Schadens-Wiedergutmachung erst in HV**
4. **Berufungs-Frist 1 Woche versäumt**
5. **Revision auf Tatsachen-Fragen** falsch begrenzt

## Anschluss

- `fachanwalt-strafrecht-wahlverteidiger-mandat` — bei Mandats-Beginn
- `fachanwalt-strafrecht-untersuchungshaft-haftpruefung` — bei U-Haft
- `aktenaufbereiter-strafrecht` — Akten-Auswertung

## Aktuelle Rechtsprechung Anklage-Reaktion (Stand Mai 2026)

- BVerfG 23.09.2025 — 2 BvR 625/25 (ANOM-Kommunikation): Verwertbarkeit von Informationen aus der Überwachung einer ANOM-Kommunikation im Strafverfahren — relevant für die Frage des hinreichenden Tatverdachts (§ 203 StPO) bei Anklagen, die auf ANOM-Datensaetze gestuetzt sind. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=23.09.2025&Aktenzeichen=2+BvR+625/25
- BGH (GSSt) 03.02.2025 — GSSt 1/24: KCanG — Verfolgungsausschluss bei sanktionsfreien Eigenkonsummengen; bei Cannabisanklage zu pruefen, ob nicht schon die Eroeffnung (§ 203 StPO) am fehlenden Tatverdacht scheitert. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- Hinweis: Eine BGH-Leitentscheidung 2025/2026 speziell zur Pruefungsdichte des Eroeffnungsbeschlusses ist Stand Mai 2026 nicht im Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche in dejure.org / openjur.de unter "§ 203 StPO hinreichender Tatverdacht" durchführen.

## Normen Eroffnungsverfahren

- § 199 StPO — Vorlage der Anklageschrift an das Gericht
- § 200 StPO — Inhalt der Anklageschrift (Pflichtangaben)
- § 203 StPO — Eroffnung bei hinreichendem Tatverdacht
- § 204 StPO — Ablehnung der Eroffnung (sofortige Beschwerde § 210 II StPO)
- § 207 StPO — Eroffnungsbeschluss mit Aenderungen
- § 153 StPO — Einstellung Geringfuegigkeit
- § 153a StPO — Einstellung gegen Auflage

---

## Skill: `chatcontrol-csam-anwaltsgeheimnis-53-stpo`

_Chat-Control CSAM Anwaltsgeheimnis und § 53 StPO Zeugnisverweigerungsrecht: Anwendungsfall Kanzlei prüft ob Chat-Control-Massnahmen Anwaltsgeheimnis verletzen oder Mandatskommunikation abhoeren koennten: Chat-Control CSAM Anwaltsgeheimnis und § 53 StPO Zeug..._

# Chat-Control CSAM Anwaltsgeheimnis und § 53 StPO Zeugnisverweigerungsrecht: Anwendungsfall Kanzlei prüft ob Chat-Control-Massnahmen Anwaltsgeheimnis verletzen oder Mandatskommunikation abhoeren koennten


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Chat-Control CSAM Anwaltsgeheimnis und § 53 StPO Zeugnisverweigerungsrecht: Anwendungsfall Kanzlei prüft ob Chat-Control-Massnahmen Anwaltsgeheimnis verletzen oder Mandatskommunikation abhoeren koennten. § 53 StPO Zeugnisverweigerungsrecht, § 97 StPO Beschlagnahmeverbot, BRAO Anwaltsgeheimnis, EU-Chat-Control-VO-Entwurf. Prüfraster Anwaltsgeheimnis-Schutz, Beschlagnahmeschutz, EU-Regulierungsrisiken, Mandatskommunikation-Sicherheit. Output Rechtsgutachten zu Chat-Control-Risiken für Anwaltsgeheimnis. Abgrenzung zu KI-Governance-Berufsrecht und zu Akteneinsicht.

### ChatControl / EU-CSAM und Anwaltsgeheimnis § 53 StPO

## Zweck

Spezial-Mandat: Mandant ist Anwalt oder Anwalt-Mitarbeiter, der Sorge hat, dass ChatControl 2.0 (EU-Verordnungsvorschlag zur Bekämpfung von CSAM — Child Sexual Abuse Material) seine Mandantenkommunikation kompromittiert. Konflikt mit Anwaltsgeheimnis (§ 43a Abs. 2 BRAO), Zeugnisverweigerungsrecht (§ 53 StPO), Beschlagnahmeverboten (§ 97 StPO).

## Eingaben

- Kommunikationskanal (E-Mail, Messenger Signal/WhatsApp/Threema, beA)
- Verschlüsselungs-Status (E2E, Transport, keine)
- Mandantenfälle (insbes. Strafverteidigung, Familienrecht mit Kindeswohl)
- Bestehende IT-Compliance der Kanzlei
- Cloud-Anbieter (USA / EU / Hybrid)

## Rechtlicher Rahmen

### EU-Ebene

- **Vorschlag COM(2022) 209** "ChatControl 2.0" — Pflicht-Scanning aller Kommunikationsdienste auf CSAM-Material und Grooming
- **EU-Datenschutzbeauftragter EDPS-Stellungnahme** (2022) — sieht Verstoß gegen Grundrechte
- Stand Mai 2026 zum EU-Verfahren: Der Verordnungsvorschlag (CSA-VO/COM(2022)209) ist weiterhin im Rat blockiert; Verlaengerung der Interimsverordnung (EU) 2021/1232 in Diskussion. Aktualisierungen vor Ausgabe direkt unter https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:52022PC0209 pruefen.

### Nationales Anwaltsrecht

- **§ 43a Abs. 2 BRAO** — Verschwiegenheitspflicht Anwalt
- **§ 53 Abs. 1 Nr. 3 StPO** — Zeugnisverweigerungsrecht Anwalt
- **§ 53a StPO** — Personen, die Anwalt unterstützen
- **§ 97 StPO** — Beschlagnahmeverbot Verteidigungs-Unterlagen
- **§ 160a Abs. 1 StPO** — **Absolutes Erhebungsverbot** für Anwalts-Verteidiger-Kommunikation
- **§ 203 StGB** — Verletzung von Privatgeheimnissen
- **§ 33 BORA** — Datenverarbeitung in Kanzlei

### Leitentscheidungen (Stand Mai 2026)

- BVerfG 23.09.2025 — 2 BvR 625/25 (ANOM-Verwertbarkeit): Grundrechtliche Maßstäbe an die Verwertung verdeckt erhobener Kommunikationsdaten — Übertragbarkeit auf ChatControl-Szenarien diskussionswürdig. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=23.09.2025&Aktenzeichen=2+BvR+625/25
- BVerfG-Linie zum Anwaltsgeheimnis und § 160a StPO (z. B. BVerfG 12.10.2011 — 2 BvR 236/08 zu § 100a StPO und Verteidigerkommunikation): vor Verwendung in dejure.org / bverfg.de live verifizieren.
- Hinweis: Eine BGH- oder BVerfG-Leitentscheidung 2025/2026 speziell zu Client-Side-Scanning ist Stand Mai 2026 nicht im Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche durchführen.

## Konflikt mit ChatControl 2.0

| ChatControl 2.0 Pflicht | Konflikt |
|---|---|
| Client-Side-Scanning aller Inhalte | Bricht Anwaltsgeheimnis vor Versand |
| Hash-Datenbank-Abgleich auf Endgerät | E2E-Verschlüsselung wird umgangen |
| Meldung an EU Centre | Mandatsdaten an Behörde |
| Verpflichtende Implementierung durch Provider | Anwalt kann nicht ausweichen |

## Strategie für Anwalts-Mandant

### Phase 1 — Status-Analyse

- Welche Kommunikationswege werden für Mandantengespräche genutzt?
- E2E-verschlüsselte vs. Server-side-Klartext
- Provider-Auswahl: EU-basiert vs. US (DPF-zertifiziert)

### Phase 2 — Verschlüsselungs-Konzept

- beA für Anwalts-Gerichts-Kommunikation (zwingend nach § 31a BRAO i.V.m. § 130d ZPO)
- Threema Work / Wire / Element für Mandantengespräche (Schweiz/EU, kein US-Server)
- PGP/S-MIME E-Mail-Verschlüsselung
- Vermeidung WhatsApp/Telegram (US-Server, ChatControl-Risiko)

### Phase 3 — Mandanten-Information

- Mandanten informieren: Verschlüsselte Kanäle bevorzugt
- Beratung Hochrisiko-Mandanten (politisch verfolgt, journalistische Quellen)
- Notizen physisch sichern

### Phase 4 — Politisches Engagement

- DAV-Stellungnahmen zu ChatControl
- BfDI-Konsultation
- Verfassungsbeschwerde-Beteiligung möglich (Verein Digitalcourage e.V., DAV)

### Phase 5 — Bei Vollziehung ChatControl (post-Verabschiedung)

- Verfassungsbeschwerde gegen Implementierung in Deutschland
- Beweisverwertungsverbot in Strafverfahren bei Anwalt-Mandanten-Material § 97 StPO
- BVerfG-Antrag auf einstweilige Anordnung

## Kanzlei-IT-Compliance

### Pflichten

- **§ 19 BORA / § 50 BRAO** — Datenträger-Verwendung sicher
- **BORA-Pflicht zu sicheren Kommunikationswegen** seit DSGVO
- **§ 43e BRAO** — Berufshaftpflichtversicherung mit IT-Sicherheits-Komponente
- **TLS Mindest-Standard** für E-Mail
- **Kanzlei-Server EU-Standort** empfohlen

### Konkrete Tools

- beA (anwaltliche Kommunikation Gericht)
- Threema Work / Wire (Mandanten-Chat)
- Tresorit / Boxcryptor / Strato HiDrive für Cloud-Speicherung
- Hardware-Token für Auth (YubiKey)

## Risiken und Red Flags

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| WhatsApp / iMessage für Mandantengespräche | ChatControl-Risiko + § 203 StGB | Migration läuft | Threema/Signal mit EU-Server |
| Cloud-Anbieter USA ohne DPF | DSGVO-Verstoß + ChatControl-Risiko | DPF-Prüfung | EU-Cloud mit BSI C5 |
| Klare CSAM-Falschtreffer in eigener Kanzlei | Strafverfolgung trotz Verteidiger-Privilegs | Klärung läuft | § 160a StPO greift |
| Verzicht auf Verschlüsselung | § 43a BRAO-Verstoß | Konzept in Arbeit | E2E-konsistent |

## Quellen und Updates (Stand Mai 2026)

- BVerfG 23.09.2025 — 2 BvR 625/25 (ANOM-Verwertbarkeit): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=23.09.2025&Aktenzeichen=2+BvR+625/25
- CSA-VO-Vorschlag COM(2022)209 — Stand des EU-Gesetzgebungsverfahrens unter: https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:52022PC0209
- Interimsverordnung (EU) 2021/1232 (befristete Ausnahme von ePrivacy für freiwilliges CSAM-Scanning): vor Verwendung Geltungsdauer unter https://eur-lex.europa.eu pruefen.
- §§ 43a BRAO, 53, 53a, 97, 100a, 160a StPO sowie § 203 StGB als Maßstabskette.
- Weitere Rechtsprechung vor Ausgabe in dejure.org / bverfg.de / openjur.de mit Gericht, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `hauptverhandlung-vorbereiten`

_Hauptverhandlung im Strafverfahren vorbereiten: Anwendungsfall Strafverteidiger muss Hauptverhandlung strukturiert vorbereiten mit Einlassung Beweisanträgen und Verfahrenstaktik: Hauptverhandlung im Strafverfahren vorbereiten: Anwendungsfall Strafverteidige..._

# Hauptverhandlung im Strafverfahren vorbereiten: Anwendungsfall Strafverteidiger muss Hauptverhandlung strukturiert vorbereiten mit Einlassung Beweisanträgen und Verfahrenstaktik


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Hauptverhandlung im Strafverfahren vorbereiten: Anwendungsfall Strafverteidiger muss Hauptverhandlung strukturiert vorbereiten mit Einlassung Beweisanträgen und Verfahrenstaktik. § 136 StPO Schweigerecht, § 244 StPO Beweisanträge, § 258 StPO Schlusspledoyer, § 261 StPO freie Beweiswürdigung. Prüfraster Einlassung erarbeiten, Beweisantrag-Liste erstellen, Zeugenliste prüfen, Sachverständigen-Einwendungen vorbereiten, Plaedoyer-Gliederung. Output Vorbereitungschecklist für Hauptverhandlung mit Skript und Reaktionsplan. Abgrenzung zu Plaedoyer-Vorbereitung für spezifisches Schlusspledoyer und zu Einlassung-Vorbereiten.

### Hauptverhandlung vorbereiten

## Kaltstart-Rückfragen

1. Welche Anklage und welches Gericht — Amtsgericht Strafrichter, Schöffengericht, Landgericht große Strafkammer, Schwurgericht (§§ 24 ff. GVG)?
2. Welche Beweise sollen geführt werden — Zeugen, Sachverständige, Urkunden, Augenscheinsobjekte, Bildmaterial?
3. Soll Verständigung § 257c StPO angestrebt werden — bei welchem Strafrahmen wäre das verteidigungsstrategisch sinnvoll?
4. Bestehen Anhaltspunkte für Befangenheit eines Richters oder Schöffen (§§ 24, 31 StPO)?
5. Welche Beweisanträge sind zur Verteidigung erforderlich — Entlastungszeugen, Sachverständige, Beiziehung weiterer Akten?

## Anspruchsgrundlagen und Verfahrensregeln

- Beweisantragsrecht § 244 Abs. 3 StPO — Gericht darf nur unter engen Voraussetzungen ablehnen (Unzulässigkeit, Wahrunterstellung, Aufklärungsverpflichtung).
- Präklusion § 244 Abs. 6 Satz 2 StPO — verspätete Anträge können zurückgewiesen werden wenn Vorbringen ohne erkennbaren Grund verspätet erfolgt.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Befangenheit § 24 StPO — Ablehnung gegen Richter wegen Besorgnis der Befangenheit; Vortrag der Ablehnungsgründe § 26 StPO.
- Beweisaufnahme nach § 244 Abs. 2 StPO Aufklärungspflicht des Gerichts.
- Schlussvorträge § 258 StPO — Reihenfolge StA, Nebenkläger, Angeklagter mit Verteidiger; letztes Wort dem Angeklagten § 258 Abs. 2 StPO.
- Strafzumessung §§ 46 ff. StGB — Schuld als Grundlage, Wirkungen auf das künftige Leben, Strafmilderung §§ 49 StGB.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Beweisanträge — Anforderungen

- Konkrete Tatsachenbehauptung (Beweisthema).
- Konkretes Beweismittel (Zeuge mit Name und Anschrift, Sachverständiger, Urkunde, Augenschein).
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Ablehnungsgründe abschließend § 244 Abs. 3 Satz 2 StPO — Unzulässigkeit, Offenkundigkeit, Aufklärung bedeutungslos, Wahrunterstellung, bereits erwiesen, Beweismittel völlig ungeeignet, Beweismittel unerreichbar, Beweisermittlungsantrag.

## Schreibvorlage Beweisantrag

```
An das Amtsgericht [Ort]
Strafrichter / Schoeffengericht
[Az]

In der Strafsache gegen [Angeklagter]
wegen [Tatvorwurf]

Beweisantrag § 244 Abs. 3 StPO

Es wird beantragt zum Beweis der Tatsache dass
[konkrete Tatsachenbehauptung]
die Zeugin / den Zeugen [Name geboren Datum wohnhaft Anschrift]
zu vernehmen.

Begruendung
1. Konnexitaet — der Zeuge / die Zeugin hat unmittelbare
 Wahrnehmungen ueber [Beweisthema] gemacht da [Begruendung].
2. Bedeutung — Die Beweistatsache ist erheblich weil
 [Verbindung mit Tatbestand / Strafzumessung].
3. Geeignetheit — Der Zeuge ist nicht voellig ungeeignet im
 Sinne § 244 Abs. 3 Satz 3 Nr. 4 StPO da [Begruendung].

Mit kollegialen Gruessen
```

## Strategie-Checkliste vor Hauptverhandlung

- Akten vollständig studiert, Aktenspiegel erstellt
- Beweisaufnahmeantrag schriftlich vorbereitet
- Hauptbeweisthemen identifiziert (Entlastung Tatbestand, Schuldfähigkeit, Strafmilderung)
- Plädoyer-Skizze mit Strafzumessungsargumenten § 46 StGB
- Befangenheitsfragen vorab geprüft
- Mit Mandant Probelauf wegen Schweigen oder Einlassung
- Bei Verständigung: Belehrungspflicht § 257c Abs. 4 StPO im Hinterkopf
- Vorbereitung Schlussvortrag mit klarer Antragstellung

## Operativer Sitzungsplan

Dieses Fachmodul nicht nur für die große Strategie, sondern auch für die Tagesarbeit vor und während der Hauptverhandlung.

1. **Tagesmappe bauen:** Ladung, Besetzung, Sitzungsbeginn, Anreise, Mandantenbriefing, Zeugenreihenfolge, Beweisthemen, Aktenstellen, Notfallnummern.
2. **Einlassungsfenster markieren:** Schweigen, Teileinlassung, schriftliche Erklärung oder spontane Reaktion nur nach Akten- und Beweislage.
3. **Antragslog führen:** Jeder Beweisantrag, Widerspruch, § 257-StPO-Erklärung, Ablehnungsbeschluss und Wiederholungsbedarf bekommt Datum, Uhrzeit, Beweisthema, Entscheidung und Revisionsnotiz.
4. **Protokoll sichern:** Bei wichtigen Vorgängen sofort prüfen, ob ein Antrag auf vollständige Protokollierung nach § 273 Abs. 3 StPO sinnvoll ist.
5. **Nach dem Sitzungstag:** Mandantenkurzbrief, Fristen-/Wiedervorlagenupdate, offene Anträge, nächste Zeugen, mögliche Rechtsmittel- oder Verständigungsrisiken.

**Anschluss-Skills:** `strafprozess-hv-tagesmappe-und-sitzungsplan`, `strafprozess-antragslog-beweisantraege-und-widerspruch`, `strafprozess-sitzungsprotokoll-und-revisionssicherung`, `strafprozess-verhandlungslog-sta-gericht-nebenklage`.

## Übergabe

- Bei Verurteilung Berufungs- oder Revisionsfrist § 314 § 341 StPO — eine Woche ab Verkündung.
- Bei Verfahrensverstößen Revisionsgründe § 338 StPO (absolute) und § 337 StPO (relative) sichern durch Sitzungsprotokoll-Beobachtung, rechtzeitige Anträge/Widersprüche und bei Bedarf Protokollierungsantrag nach § 273 Abs. 3 StPO.
- Bei Verständigungsversuch ergebnisoffen — Dokumentation der Belehrung.
- Anschluss: Skill `fachanwalt-strafrecht-akteneinsicht-beantragen` ggf. nochmals für ergänzende Aktenbestandteile.

## Zentrale Rechtsprechung Hauptverhandlung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage-Fragen vor Hauptverhandlung

1. Gericht und Besetzung: Strafrichter (§ 25 GVG), Schoeffengericht (§ 28 GVG) oder Strafkammer (§ 74 GVG)?
2. Liegt Verstaendigung in Betracht? Falls ja: Vorgespraech nach § 257b StPO und Protokollierung sicherstellen.
3. Beweisantraege: Welche Entlastungszeugen, Sachverstaendige, Urkunden — Konnexitaet geprueft?
4. Befangenheitsantrag noetig? Vorgehensweise: Ablehnungsgesuch schriftlich vor Beginn der Vernehmung.
5. Einlassung oder Schweigen: Letzte Entscheidung mit Mandant vor HV-Beginn abklaeren.

---

## Skill: `insolvenzantrag-staatsanwaltschaft`

_Insolvenzantrag-Massnahmen durch Staatsanwaltschaft im Wirtschaftsstrafrecht: Anwendungsfall Staatsanwaltschaft hat Insolvenzantrag gestellt oder Vermögenswerte beschlagnahmt und Verteidiger muss reagieren: Insolvenzantrag-Massnahmen durch Staatsanwaltschaf..._

# Insolvenzantrag-Massnahmen durch Staatsanwaltschaft im Wirtschaftsstrafrecht: Anwendungsfall Staatsanwaltschaft hat Insolvenzantrag gestellt oder Vermögenswerte beschlagnahmt und Verteidiger muss reagieren


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Insolvenzantrag-Massnahmen durch Staatsanwaltschaft im Wirtschaftsstrafrecht: Anwendungsfall Staatsanwaltschaft hat Insolvenzantrag gestellt oder Vermögenswerte beschlagnahmt und Verteidiger muss reagieren. § 283 StGB Bankrott, § 15a InsO Antragspflicht, §§ 111b ff. StPO Beschlagnahme. Prüfraster Insolvenzantrag-Berechtigung prüfen, Beschlagnahme anfechten, Insolvenzantragspflichtverletzung als Strafbarkeitsrisiko einordnen. Output Verteidigungs-Strategie-Memo mit Massnahmenliste gegen Staatsanwaltschafts-Insolvenzantrag. Abgrenzung zu Distressed-MA und zu Wirtschaftsstrafrecht.

### Insolvenzantrag der Staatsanwaltschaft gegen Angeklagte/n

## Kernsachverhalt & Mandantenfragen

Die Konstellation ist strafverteidigungspraktisch gefährlich: Gleichzeitig laufen ein Strafverfahren (Schweigerecht nach § 136 StPO) und ein Insolvenzverfahren (Mitwirkungspflicht nach § 97 InsO). Mandantschaft versteht die Doppelgleisigkeit oft nicht. Fehler in einem Verfahren können das andere ruinieren.

**8 Kaltstart-Rückfragen:**

1. Liegt Ihnen der Insolvenzantrag im Wortlaut vor? Wer ist Antragsteller (Finanzamt, Staatsanwaltschaft, Sozialversicherungsträger, privater Gläubiger)?
2. Gegen wen richtet sich der Antrag – gegen Sie persönlich oder gegen eine von Ihnen geführte Gesellschaft (GmbH, AG, Einzelkaufmann)?
3. Welches Strafverfahren läuft parallel und welche Tatvorwürfe enthält es (Steuerhinterziehung, Untreue, Betrug, Beitragsvorenthaltung)?
4. Bestehen bereits Sicherungsmaßnahmen im Strafverfahren – Vermögensarrest nach § 111e StPO oder Beschlagnahme nach § 111b StPO?
5. Hat das Insolvenzgericht bereits einen vorläufigen Insolvenzverwalter eingesetzt?
6. Haben Sie gegenüber dem Insolvenzverwalter oder dem Gericht bereits Angaben gemacht?
7. Gibt es realistische Möglichkeiten zur Zahlung – Ratenzahlung, Vergleich mit dem Antragsteller, Darlehen Dritter?
8. Haben Sie anwaltliche Vertretung im Insolvenzverfahren getrennt von der strafrechtlichen Vertretung?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 14 InsO | Gläubigerantrag auf Insolvenz; rechtlich titulierte Forderung oder Glaubhaftmachung notwendig |
| § 17 InsO | Zahlungsunfähigkeit als Eröffnungsgrund |
| § 19 InsO | Überschuldung juristischer Personen als Eröffnungsgrund |
| § 21 InsO | Sicherungsmaßnahmen des Insolvenzgerichts; vorläufiger Insolvenzverwalter |
| § 35 InsO | Insolvenzmasse; gesamtes pfändbares Vermögen |
| § 36 InsO | Pfändungsfreie Gegenstände; unterhaltsrelevante Freigrenzen |
| § 97 InsO | Mitwirkungspflicht des Schuldners; Selbstbelastungsverbot § 97 Abs. 1 S. 3 InsO |
| § 129 ff. InsO | Insolvenzanfechtung; Rückgewähr anfechtbarer Zahlungen |
| § 15b InsO | Zahlungsverbot nach Insolvenzreife (früher § 64 GmbHG a.F.) |
| § 174 ff. InsO | Forderungsanmeldung zur Tabelle |
| § 270 InsO | Eigenverwaltung; Schuldner bleibt verfügungsberechtigt |
| § 270b InsO | Schutzschirmverfahren (Sanierungsoption) |
| § 302 InsO | Ausnahmen von der Restschuldbefreiung bei vorsätzlichen unerlaubten Handlungen |
| §§ 73, 73c StGB | Einziehung von Taterträgen und Wertersatz |
| §§ 111b–111p StPO | Vermögenssicherung im Strafverfahren; Beschlagnahme und Vermögensarrest |
| § 111i StPO | Verhältnis Vermögensarrest zur Insolvenzeröffnung |
| § 370 AO | Steuerhinterziehung; häufigste Grundlage des Insolvenzantrags durch Finanzamt |
| § 266a StGB | Beitragsvorenthaltung gegenüber Sozialversicherungsträgern |
| § 15a InsO | Insolvenzantragspflicht (Insolvenzverschleppung) |

---

## Leitentscheidungen

| Aktenzeichen | Gericht / Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

---

## Prüfschema

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Antrag prüfen: Antragsteller, Forderungsgrundlage, Titulierung oder Glaubhaftmachung ausreichend? | § 14 InsO |
| 2 | Insolvenzgrund prüfen: Zahlungsunfähigkeit (§ 17 InsO) oder Überschuldung (§ 19 InsO) tatsächlich gegeben? | § 17, § 19 InsO |
| 3 | Sicherungsmaßnahmen im Insolvenzverfahren prüfen: vorläufiger Insolvenzverwalter eingesetzt? Kontensperrung? | § 21 InsO |
| 4 | Parallele Beschlagnahme/Vermögensarrest prüfen: § 111b/111e StPO; Verhältnis zur Insolvenzmasse klären | § 111i StPO |
| 5 | Schweigerecht vs. Mitwirkungspflicht: Aufklärung der Mandantschaft über Doppelgleisigkeit; Aussagen schriftlich vorbereiten | § 97 InsO, § 136 StPO |
| 6 | Anhörung Insolvenzgericht vorbereiten: Liquiditätsplan erstellen, BWA/SuSa beibringen, Insolvenzgrund bestreiten oder einräumen | § 14 Abs. 2 InsO |
| 7 | Vergleich mit Antragsteller prüfen: Ratenzahlung, Stundung, Einmalzahlung; parallel Schadenswiedergutmachung nach § 46a StGB | § 46a StGB |
| 8 | Sofortige Beschwerde gegen Anordnungen prüfen: Frist 2 Wochen | § 6 InsO, §§ 567 ff. ZPO |
| 9 | Eigenantrag mit Eigenverwaltung/Schutzschirm erwägen: Mandantschaft behält Verfügungsgewalt; Vermögensarrest wird abgelöst | § 270, § 270b InsO |
| 10 | Insolvenzanfechtungsrisiken prüfen: Zahlungen an Nahestehende, Beraterhonorare, Schenkungen in anfechtbaren Zeiträumen | §§ 129–135 InsO |
| 11 | Restschuldbefreiung prüfen: § 302 InsO ausschließen wenn Steuerhinterziehung, Betrug oder andere vorsätzliche Delikte vorliegen | § 302 InsO |
| 12 | Koordination mit Insolvenzverwaltung: frühzeitiger Kontakt, Unterlagenzulieferung mit Selbstbelastungsfilter | § 97 InsO |
| 13 | Schadenswiedergutmachung als Strafmilderung dokumentieren: § 46a StGB; Verständigung § 257c StPO einbeziehen | § 46a, § 257c StPO |
| 14 | Geschäftsführerhaftung nach § 15b InsO prüfen: Zahlungen nach Eintritt der Insolvenzreife; Haftungsumfang ermitteln | § 15b InsO |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Insolvenzantrag Staatsanwaltschaft abwehren | Stellungnahme; Template unten |
| Variante A — Mandant stellt selbst Insolvenzantrag | Eigenantrag § 15 InsO; Haftungsminimierung |
| Variante B — Verfahren einzustellen | § 153a StPO-Angebot annehmen; Busse zahlen |
| Variante C — Glaeubigerbenachteiligung im Fokus | § 283 StGB-Varianten pruefen; InsO-Anfchtung parallel |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 – Anhörung Insolvenzgericht (Widerspruch gegen Antrag)

```
An das Amtsgericht [...]
– Insolvenzgericht –
Aktenzeichen: [...]

Stellungnahme zur Anhörung gemäß § 14 Abs. 2 InsO

In dem Insolvenzantragsverfahren gegen
[Name/Firma der Schuldnerin / des Schuldners]

zeige ich die anwaltliche Vertretung an.

Der Insolvenzantrag vom [Datum] ist zurückzuweisen.

I. Kein Insolvenzgrund vorhanden

Die Antragstellerin hat keine wirksam titulierte Forderung
glaubhaft gemacht. Der Steuerbescheid vom [Datum] ist nicht
rechtskräftig; gegen ihn ist Einspruch eingelegt (Anlage 1).
Ein auf bestrittene Forderungen gestützter Gläubigerantrag
ist mangels Forderungslegitimation unzulässig (vgl. BGH
IX ZB 37/12).

II. Zahlungsunfähigkeit liegt nicht vor

Zum Stichtag [Datum] verfügt die Schuldnerin über folgende
liquide Mittel: [Kontostand EUR, offene Kreditlinie EUR,
zugesagtes Darlehen EUR (Nachweis Anlage 2)]. Die fälligen
Verbindlichkeiten betragen [Summe EUR]. Die Liquiditätslücke
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

III. Hilfsweise: Vergleichsbereitschaft

Hilfsweise erklärt die Schuldnerin Bereitschaft zur sofortigen
Zahlung von [Betrag EUR] sowie Ratenzahlung der verbleibenden
Schuld in monatlichen Raten von [Betrag EUR] ab [Datum].

[Ort, Datum]
[Unterschrift, Kanzlei]
```

### Baustein 2 – Memo an Mandantschaft: Schweigerecht vs. Mitwirkungspflicht

```
Mandanteninfo: Ihre Rechte in Strafverfahren und Insolvenzverfahren

1. Im Strafverfahren:
 Sie haben das Recht zu schweigen (§ 136 StPO).
 Keine Aussage ohne Absprache mit mir.

2. Im Insolvenzverfahren:
 Sie sind zur Auskunft verpflichtet (§ 97 InsO).
 Unrichtige Angaben können als Bankrott (§ 283 StGB) geahndet werden.

3. Schutz vor Selbstbelastung:
 § 97 Abs. 1 S. 3 InsO enthält ein beschränktes Verwertungsverbot:
 Zwangsweise erlangte Auskünfte dürfen im Strafverfahren nicht
 verwertet werden. Freiwillige Angaben genießen diesen Schutz
 jedoch NICHT.

4. Praxisregel:
 Alle Auskünfte im Insolvenzverfahren schriftlich, nach Rücksprache
 mit mir. Keine mündlichen Spontanangaben gegenüber dem Insolvenz-
 verwalter.

5. Koordination:
 Ich stimme Ihre Angaben im Insolvenzverfahren mit Ihrer
 Strafverteidigungsstrategie ab.
```

### Baustein 3 – Antrag auf Eigenantrag mit Eigenverwaltung § 270 InsO

```
An das Amtsgericht [...]
– Insolvenzgericht –

Antrag auf Eröffnung des Insolvenzverfahrens in Eigenverwaltung
gemäß §§ 270 ff. InsO

Die Schuldnerin beantragt die Eröffnung des Insolvenzverfahrens
über ihr Vermögen verbunden mit der Anordnung der Eigenverwaltung
gemäß § 270 InsO.

Begründung:
[1. Insolvenzgrund: Zahlungsunfähigkeit nach § 17 InsO liegt vor.]
[2. Kein Schaden für Gläubiger durch Eigenverwaltung: Mandantschaft
hat Sanierungskonzept vorgelegt (Anlage 1).]
[3. Eigenverwaltung hat Vorrang vor Fremdverwaltung, wenn keine
Nachteile für Gläubiger ersichtlich, § 270 Abs. 1 InsO.]
[4. Strategischer Vorteil im Strafverfahren: Mit Eigenverwaltung
entfällt faktisch das durch Fremdverwaltung entstehende Risiko
unkontrollierter Aktenweitergabe an die Staatsanwaltschaft.]

Dem Antrag liegt ein Sanierungsplan gemäß § 270 Abs. 2 Nr. 3 InsO bei.

[Ort, Datum]
[Unterschrift]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Insolvenzgrund (Gläubigerantrag) | Antragsteller muss Forderung und Insolvenzgrund glaubhaft machen (§ 14 InsO); Schuldner muss widerlegen |
| Zahlungsunfähigkeit (§ 17 InsO) | Vermutet ab Insolvenzantrag; Schuldner muss Liquidität substantiiert nachweisen |
| Überschuldung (§ 19 InsO) | Antragsteller oder Sachverständiger muss Überschuldungsstatus erstellen; Schuldner kann bestreiten |
| § 97 InsO Selbstbelastungsschutz | Schuldner muss darlegen, dass Auskunft zu Strafverfolgung führen könnte; enger Maßstab |
| Insolvenzanfechtung (§ 129 InsO) | Insolvenzverwalter trägt objektiven Tatbestand; bei Vorsatzanfechtung (§ 133 InsO) auch Benachteiligungsvorsatz |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Sofort | Akteneinsicht im Insolvenzgericht beantragen; Anhörungsfrist im Blick | § 14 Abs. 2 InsO |
| 2 Wochen | Sofortige Beschwerde gegen Anordnungen des Insolvenzgerichts | § 6 InsO |
| 3 Wochen ab Bestellung | Vorläufiger Insolvenzverwalter ist im Amt; Koordination dringend | § 21 InsO |
| 6 Wochen ab Eröffnung | Forderungsanmeldung zur Tabelle (Gläubigerseite) | § 174 InsO |
| 3 Jahre | Verjährung strafrechtlicher Ansprüche nach § 370 AO (leichte Steuerhinterziehung) | § 78 StGB, § 376 AO |
| 10 Jahre | Strafverfolgungsverjährung bei schwerer Steuerhinterziehung (§ 376 AO Abs. 1) | § 376 AO |
| 3 Jahre | Insolvenzanfechtung § 133 Abs. 1 InsO (Vorsatzanfechtung); ab Kenntnis des Verwalters | § 146 InsO |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Schweigerecht gilt auch im Insolvenzverfahren" | Nein; § 97 InsO normiert ausdrücklich Mitwirkungspflicht; Schweigerecht aus § 136 StPO gilt nur im Strafverfahren |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Insolvenz stoppt den Vermögensarrest automatisch" | Grundsätzlich ja (§ 111i StPO), aber Einziehungsanspruch des Staates bleibt bestehen; er wird zum Insolvenzgläubiger |
| "Restschuldbefreiung befreit auch von Steuerschulden" | Nein; § 302 Nr. 1 InsO schließt vorsätzlich begangene unerlaubte Handlungen aus; Steuerhinterziehung ist § 370 AO = unerlaubte Handlung |
| "Eigenverwaltung schadet den Gläubigern" | § 270 InsO sieht vor, dass Eigenverwaltung angeordnet wird wenn kein Nachteil für Gläubiger; Beweislast liegt beim Widersprechenden |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Strafverteidigung | VV-RVG Teil 4 (Nrn. 4100 ff.); Mittelgebühr nach Umfang; Verständigung erhöht Gebührensatz |
| Insolvenzrechtliches Mandat | VV-RVG Teil 3 (Nrn. 3300 ff.) nach Gegenstandswert = Insolvenzforderung oder Streitwert im Anfechtungsstreit |
| Separat Honorarvereinbarung § 3a RVG | Für Straf- und Insolvenzmandat getrennt sinnvoll; vermeidet Streit über Gegenstandswerte |
| Kosten vorläufiger Insolvenzverwalter | Feste Vergütungssätze nach InsVV; gehen aus der Masse; kein Anwaltseinfluss |
| Kosten des Steuerstrafverfahrens | Bei Einstellung § 153a StPO: Auflage (Geldbetrag) als Strafe; Anrechnung auf Steuerschulden möglich |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Insolvenzantrag des Finanzamts + Strafverfahren | Zwei getrennte Mandatsverträge (Strafrecht + Insolvenzrecht); Koordination zwischen beiden Vertretern |
| Vermögensarrest nach § 111e StPO läuft bereits | Eigenantrag erwägen; Insolvenzeröffnung löst Arrest ab (§ 111i StPO) und verschafft Gestaltungsraum |
| Vergleich mit Finanzamt möglich | Stundungs-/Ratenvergleich anstreben; Schadenswiedergutmachung nach § 46a StGB ins Strafverfahren einbringen |
| Insolvenzantrag rechtlich angreifbar | Kein Insolvenzgrund trotz Rückständen? Sofortige Beschwerde + einstweilige Verfügung |
| Mandantschaft ist GmbH-Geschäftsführer | § 15b InsO-Haftung prüfen; rechtzeitiger Eigenantrag schützt vor persönlicher Haftung |
| Restschuldbefreiung angestrebt | Prüfen ob Straftatbestand § 302 InsO greift; ggf. Strafverfahrensabschluss ohne Vorsatzurteil anstreben |

---

## Anschluss-Skills

- `fachanwalt-strafrecht-zeugenbeistand` – bei Zeugenvernehmung im Strafverfahren mit Insolvenzberührung
- `fachanwalt-strafrecht-adhaesionsverfahren` – Verletztenentschädigung im Strafverfahren als Insolvenzforderung
- `plaedoyer-vorbereitung-strafverteidigung` – Strafzumessung mit Schadenswiedergutmachung (§ 46a StGB)
- `fachanwalt-strafrecht-nebenklage-opfervertretung` – Verletzte als Insolvenzgläubiger

---

## Quellen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

---

## Skill: `nebenklage-opfervertretung`

_Nebenklage und Opfervertretung im Strafverfahren: Anwendungsfall Opfer einer Straftat moechte als Nebenklaeger am Verfahren teilnehmen und anwaltliche Vertretung benoetigen: Nebenklage und Opfervertretung im Strafverfahren: Anwendungsfall Opfer einer Straft..._

# Nebenklage und Opfervertretung im Strafverfahren: Anwendungsfall Opfer einer Straftat moechte als Nebenklaeger am Verfahren teilnehmen und anwaltliche Vertretung benoetigen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Nebenklage und Opfervertretung im Strafverfahren: Anwendungsfall Opfer einer Straftat moechte als Nebenklaeger am Verfahren teilnehmen und anwaltliche Vertretung benoetigen. §§ 395-406h StPO Nebenklage, § 403 StPO Adhaesionsantrag, OEG Opferentschaedigungsgesetz. Prüfraster Nebenklageberechtigung prüfen, Beitrittserklärung formulieren, Akteneinsicht beantragen, taktische Interessen Opfer vs. Strafverfolgung abwaegen. Output Nebenklagebeitrittserklärung mit Antragsliste und Strategie-Memo. Abgrenzung zu Adhaesionsverfahren und zu Erstgespraeach-Mandatsannahme.

### Nebenklage und Opfervertretung im Strafverfahren

## Kernsachverhalt & Mandantenfragen

Die Nebenklage gibt der verletzten Person eine eigenständige Rolle im Strafverfahren – mit Rechten, die über bloße Zeugenaussagen weit hinausgehen. Gleichzeitig ist sie keine vollwertige Parteistellung. Die Kunst liegt darin, die Mandantschaft zu schützen, ohne den Prozess zu blockieren.

**8 Kaltstart-Rückfragen:**

1. Welche konkrete Tat wurde begangen und wann? Liegt eine schriftliche Anzeige oder Strafanzeige vor?
2. Ist die Staatsanwaltschaft bereits tätig? Liegt ein Aktenzeichen vor?
3. Wie ist die Beziehung zum/zur Beschuldigten (Fremd, Bekannt, Familie, Arbeitsbeziehung)?
4. Welche körperlichen, seelischen oder finanziellen Schäden sind entstanden? Ärztliche Dokumentation vorhanden?
5. Wurde die Mandantschaft bereits als Zeugin/Zeuge vernommen? Protokoll vorhanden?
6. Besteht akute Gefährdung durch den Täter (Drohungen, Stalking, Wiederholungsgefahr)?
7. Sind zivilrechtliche Ansprüche geplant (Schmerzensgeld, Schadensersatz, Verdienstausfall)?
8. Wünscht die Mandantschaft Anonymität oder befürchtet sie Repressalien durch Anschluss als Nebenklägerin?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 395 StPO | Nebenklagebefugnis; Katalog der berechtigenden Straftaten (Abs. 1–3) |
| § 396 StPO | Anschlussverfahren; Erklärung beim Gericht; Form und Frist |
| § 397 StPO | Befugnisse der Nebenklage: Anwesenheit, Fragerecht, Beweisantragsrecht, Schlussvortragsrecht |
| § 397a StPO | Beiordnung des Opferanwalts; von Amts wegen (Abs. 1) oder nach PKH-Maßstab (Abs. 2) |
| § 400 StPO | Rechtsmittelbefugnis der Nebenklage (eingeschränkt auf Strafzumessung) |
| § 401 StPO | Revision der Nebenklage |
| § 403 StPO | Adhäsionsantrag: Geltendmachung zivilrechtlicher Ansprüche im Strafverfahren |
| § 406e StPO | Akteneinsicht der verletzten Person durch anwaltliche Vertretung |
| § 406g StPO | Psychosoziale Prozessbegleitung; Beiordnung durch das Gericht |
| § 68 Abs. 2/3 StPO | Adressanonymisierung für gefährdete Zeugen und Nebenklägerinnen |
| § 172 StPO | Klageerzwingungsverfahren bei Einstellungsentscheidung der StA |
| § 238 StGB | Stalking; häufige Grundlage der Nebenklage |
| §§ 174–184k StGB | Sexualstraftaten; Katalog für Nebenklagebefugnis § 395 Abs. 1 Nr. 1 |
| §§ 223–226a StGB | Körperverletzungsdelikte; Katalog § 395 Abs. 1 Nr. 3 |
| §§ 211, 212 StGB | Tötungsdelikte; Hinterbliebene sind nebenklageberechtigt |

---

## Leitentscheidungen

| Aktenzeichen | Gericht / Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

---

## Prüfschema Nebenklage

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Tatbestand der Anklage/Eröffnungsbeschluss: Fällt er in den Katalog § 395 StPO? | § 395 Abs. 1–3 StPO |
| 2 | Verletzteneigenschaft: Ist Mandantschaft persönlich und unmittelbar durch die Tat verletzt? Sachenrechtliche oder rein wirtschaftliche Beeinträchtigung reicht nicht | § 395 StPO |
| 3 | Hinterbliebenenstellung bei Tötungsdelikt: Verwandtschaftsbeziehung prüfen (§ 395 Abs. 2 Nr. 1 StPO) | § 395 Abs. 2 StPO |
| 4 | Akteneinsichtsantrag gemäß § 406e StPO: Berechtigtes Interesse darlegen; Ablehnung anfechten | § 406e StPO |
| 5 | Beiordnungsantrag § 397a StPO: Voraussetzungen von Amts wegen (Abs. 1) oder nach PKH-Maßstab (Abs. 2) prüfen | § 397a StPO |
| 6 | Anschlusserkärung formulieren und einreichen: schriftlich beim Gericht, mit Vollmacht | § 396 StPO |
| 7 | Psychosoziale Prozessbegleitung § 406g StPO prüfen: Schutzbedürftigkeit bei Sexualdelikten, Minderjährigkeit, schwerer Gewalt | § 406g StPO |
| 8 | Adhäsionsantrag erwägen: Schmerzensgeld, Schadensersatz, Feststellungsantrag für Zukunftsschäden | §§ 403–406c StPO |
| 9 | Adressanonymisierung beantragen wenn Gefährdung: § 68 Abs. 2/3 StPO | § 68 StPO |
| 10 | Hauptverhandlungsvorbereitung: Fragerecht, Beweisantragsrecht, Erklärungsrecht nach § 257 StPO | § 397 StPO |
| 11 | Schlussplädoyer vorbereiten: Schuldspruchantrag, Strafzumessungsargumente, Adhäsionsantrag | § 397 Abs. 1 StPO |
| 12 | Rechtsmittelprüfung nach Urteil: Berufung/Revision nach § 400/§ 401 StPO – nur zu Lasten Angeklagter | §§ 400, 401 StPO |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Nebenklage Opfervertretung | Nebenklage-Anschlussschrift; Template unten |
| Variante A — Opfer will nur Schmerzensgeld | Adhaesionsantrag statt Nebenklage |
| Variante B — Taeterseitiges Gestaendnis vorhanden | Nebenklage trotzdem sinnvoll für Strafhoehe und Entschaedigung |
| Variante C — Verjährungsrisiko | Nebenklagebefugnis fristen-unabhaengig; Verjaahrung des Hauptvorwurfs beachten |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 – Anschlusserkärung als Nebenklage

```
An das [Gericht]
Aktenzeichen: [...]

Anschlusserklärung als Nebenklage gemäß §§ 395, 396 StPO

In der Strafsache gegen [Name Beschuldigte/r]
wegen [Tatvorwurf, z.B. schwere Körperverletzung gemäß § 226 StGB]

zeige ich die anwaltliche Vertretung der Verletzten
[Name, Geburtsdatum, Anschrift]
an.

Ich erkläre hiermit den Anschluss als Nebenklage gemäß
§§ 395 Abs. 1 Nr. 3, 396 Abs. 1 StPO.

Begründung der Nebenklagebefugnis:
Die Verletzte hat durch die Tat vom [Datum] schwere
Körperverletzung im Sinne des § 226 StGB erlitten
[konkrete Verletzungen benennen]. Die Verletzteneigenschaft
ist damit gegeben; der Tatbestand fällt unter den Katalog
des § 395 Abs. 1 Nr. 3 StPO.

Eine schriftliche Vollmacht liegt in Kopie bei.

[Ort, Datum]
[Unterschrift, Kanzlei]
```

### Baustein 2 – Beiordnungsantrag § 397a Abs. 1 StPO (von Amts wegen)

```
An das [Gericht]
Aktenzeichen: [...]

Antrag auf Beiordnung als Opferanwalt gemäß § 397a Abs. 1 StPO

Die Nebenklägerin [Name] beantragt durch ihre Vertretung,
mich als anwaltlichen Beistand gemäß § 397a Abs. 1 Nr. [...]
StPO beizuordnen.

Voraussetzungen:
[Nr. 1: Die Nebenklägerin ist Opfer eines Sexualdelikts
nach §§ 174 bis 184k StGB / versuchten Tötungsdelikts /
schwerer Körperverletzung § 226 StGB / minderjährig.]

Eine Prüfung der wirtschaftlichen Verhältnisse findet
gemäß § 397a Abs. 1 StPO nicht statt; die Beiordnung
ist kostenlos.

Die Hauptverhandlung ist für [Datum] angesetzt.
Die sachgerechte Wahrnehmung der Interessen der Neben-
klägerin – insbesondere Fragerecht, Beweisantragsrecht,
Schlussplädoyer und Adhäsion – erfordert anwaltliche
Vertretung.

[Ort, Datum]
[Unterschrift]
```

### Baustein 3 – Akteneinsichtsantrag § 406e StPO

```
An die Staatsanwaltschaft [...]
Aktenzeichen: [...]

Antrag auf Akteneinsicht gemäß § 406e Abs. 1 StPO

Ich zeige die anwaltliche Vertretung der Verletzten
[Name] an.

Ich beantrage vollständige Akteneinsicht, insbesondere:
– Einstellungs- oder Anklageentscheidung
– Vernehmungsprotokolle (Beschuldigte/r und Zeugen)
– Sachverständigengutachten
– Lichtbilder und Spurenauswertung
– Telekommunikationsauswertungen

Das berechtigte Interesse der Verletzten ergibt sich aus
der Anschlussabsicht gemäß §§ 395, 396 StPO sowie aus
der Prüfung von Adhäsionsansprüchen nach §§ 403 ff. StPO.

Sollte die Akteneinsicht ganz oder teilweise versagt werden,
beantrage ich ausdrücklich gerichtliche Entscheidung gemäß
§ 406e Abs. 4 StPO.

[Ort, Datum]
[Unterschrift]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Nebenklagebefugnis § 395 StPO | Verletztenvertretung trägt Verletzteneigenschaft und Katalogtat vor; Gericht prüft von Amts wegen |
| Beiordnung § 397a Abs. 1 StPO | Keine Bedürftigkeitsprüfung; Antragstellerin muss nur Katalogvoraussetzungen belegen |
| Beiordnung § 397a Abs. 2 StPO | Verletztenvertretung muss Bedürftigkeit + eigene Unfähigkeit zur Interessenwahrnehmung glaubhaft machen |
| Akteneinsicht § 406e StPO | Berechtigtes Interesse wird bei Nebenklage vermutet; StA trägt überwiegende Gegeninteressen |
| Adhäsion § 403 StPO | Verletzte trägt Anspruchsgrundlage und Schadenshöhe; Beweisaufnahme im Strafverfahren |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Bis Schluss der Beweisaufnahme | Anschlusserklärung muss vor Schlussvorträgen vorliegen | § 396 Abs. 1 StPO |
| Sofort nach Ladung | Akteneinsicht beantragen; Vorlaufzeit der Behörde einplanen | § 406e StPO |
| Bis Beginn der Schlussvorträge | Adhäsionsantrag stellen (§ 404 StPO) | § 404 StPO |
| 1 Woche nach Urteilszustellung | Frist zur Einlegung von Berufung / Revision (§§ 316, 341 StPO) | §§ 400, 401 StPO |
| 3 Jahre | Zivilrechtliche Verjährung der Deliktsansprüche (§ 195 BGB); ab Kenntnis von Schaden und Schädiger | § 199 BGB |
| 30 Jahre | Verjährung bei vorsätzlichen Verletzungen (§ 199 Abs. 2 BGB) wenn keine Kenntnis des Schädigers | § 199 Abs. 2 BGB |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Nebenklage ist unnötig; StA verfolgt schon" | Nebenklage gibt eigene Verfahrensrechte: Fragerecht, Beweisantragsrecht, Schlussplädoyer, Rechtsmittel – StA hat andere Interessenlage |
| "Anschluss ist zu spät" | § 396 Abs. 1 StPO lässt Anschluss bis Beginn der Schlussvorträge zu; keine Ausschlussfrist davor |
| "Beiordnung nach § 397a StPO abgelehnt weil kein Katalogdelikt" | Beschluss anfechten; hilfsweise Antrag nach § 397a Abs. 2 StPO mit PKH-Bewilligung |
| "Akteneinsicht gefährdet Persönlichkeitsrechte des Beschuldigten" | § 406e Abs. 2 StPO: Versagung nur bei überwiegenden schutzwürdigen Interessen; Katalogtatbegehung begründet regelmäßig Vorrang der Verletzten |
| "Nebenklage kann das Strafmaß nicht beeinflussen" | Unrichtig; § 400 Abs. 1 StPO erlaubt Anfechtung, wenn ein schwerer wiegender Schuldspruch erstrebt wird; Strafzumessungsargumente im Plädoyer möglich |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Beiordnung § 397a StPO | Pflichtverteidigergebühren VV-RVG Teil 4 (Nrn. 4124 ff.); Staatskasse trägt Kosten |
| Wahlmandat Nebenklage | Mittelgebühr nach VV-RVG 4124–4125 zuzüglich Terminsgebühren; Honorarvereinbarung nach § 3a RVG möglich |
| Adhäsion | VV-RVG Teil 4 Abschnitt 6 (Nrn. 4143–4147); Wertgebühr nach Adhäsionsanspruch; Adhäsion selbst ist für Verletzten kostenfrei (§ 472a StPO) |
| Hauptverhandlung je Sitzungstag | VV-RVG 4125 (Terminsgebühr); erhöht bei besonderen Schwierigkeiten oder besonderem Umfang |
| Rechtsmittelverfahren | Eigene Verfahrens- und Terminsgebühr nach VV-RVG 4130/4131 (Berufung) bzw. 4134 (Revision) |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Verletzter will Strafmaß beeinflussen | Aktive Nebenklage: Schlussvortrag mit Strafzumessungsargumenten; ggf. Revision nach § 401 StPO |
| Verletzter will primär Schadensersatz | Adhäsionsantrag kombinieren mit Nebenklage; spart Zivilklage |
| Verletzter will Anonymität | Adressanonymisierung § 68 Abs. 3 StPO beantragen; Anschluss über Anwaltskanzleianschrift |
| Verletzter ist minderjährig | § 397a Abs. 1 StPO + § 406g StPO (psychosoziale Prozessbegleitung) kombinieren |
| StA stellt ein (§ 170 Abs. 2 StPO) | Klageerzwingungsantrag § 172 StPO prüfen; Frist 1 Monat nach Bescheidung |
| Täter ist insolvent | Adhäsionsforderung zur Insolvenztabelle anmelden; § 302 InsO bei Vorsatztaten prüfen |

---

## Anschluss-Skills

- `fachanwalt-strafrecht-adhaesionsverfahren` – zivilrechtliche Ansprüche im Strafverfahren
- `fachanwalt-strafrecht-zeugenbeistand` – wenn Verletzte/r zugleich Zeuge/in ist
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` – Adhäsionsforderung in der Insolvenz
- `plaedoyer-vorbereitung-strafverteidigung` – Schlussvortrag aus Nebenklage-Perspektive

---

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `plaedoyer-vorbereitung-strafverteidigung`

_Plaedoyer für Strafverteidigung vorbereiten und strukturieren: Anwendungsfall nach Abschluss der Beweisaufnahme muss Strafverteidiger Schlusspledoyer mit Schuldfrage Strafzumessung und Verfahrenshindernissen vorbereiten: Plaedoyer für Strafverteidigung vorb..._

# Plaedoyer für Strafverteidigung vorbereiten und strukturieren: Anwendungsfall nach Abschluss der Beweisaufnahme muss Strafverteidiger Schlusspledoyer mit Schuldfrage Strafzumessung und Verfahrenshindernissen vorbereiten


## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Plaedoyer Vorbereitung** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Strafrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Plaedoyer für Strafverteidigung vorbereiten und strukturieren: Anwendungsfall nach Abschluss der Beweisaufnahme muss Strafverteidiger Schlusspledoyer mit Schuldfrage Strafzumessung und Verfahrenshindernissen vorbereiten. § 258 StPO Schlusspledoyer, § 46 StGB Strafzumessung, § 261 StPO freie Beweiswürdigung. Prüfraster Schuldfrage anhand Beweisaufnahme, Beweiswürdigungs-Angriff, Strafzumessung Milderungsgründe, Verfahrenshindernisse. Output Plaedoyer-Gliederung mit Kernargumentation und Antragsformulierungen. Abgrenzung zu Hauptverhandlung-Vorbereiten für Gesamtvorbereitung und zu Schriftsatzkern.

### Plädoyer-Vorbereitung Strafverteidigung

## Kernsachverhalt & Mandantenfragen

Das Plädoyer ist der letzte große Auftritt der Verteidigung in der Hauptverhandlung. Es fasst Beweiswürdigung und Rechtslage zusammen – und muss klar, strukturiert und überzeugend sein. Verteidigerinnen und Verteidiger, die das Plädoyer nicht vorbereiten, verschenken wesentliches Strafminderungspotenzial.

**8 Kaltstart-Rückfragen:**

1. Was ist der genaue Tatvorwurf und welcher Straftatbestand liegt der Anklage zugrunde?
2. Welches Verteidigungsziel ist vereinbart: Freispruch (Tatbestand verneinend oder Rechtfertigung), milderer Schuldspruch, Bewährungsstrafe oder Mindeststrafe?
3. Welche Beweise hat die Staatsanwaltschaft in der Hauptverhandlung eingeführt (Zeugen, Sachverständige, Urkunden, Geständnis)?
4. Liegen Verwertungsverbote vor (Durchsuchung ohne richterliche Anordnung, Belehrungsmangel, verbotene Vernehmungsmethoden)?
5. Hat der/die Angeklagte ein Geständnis abgelegt oder bestreitet er/sie den Tatvorwurf vollständig?
6. Sind Hilfsbeweisanträge noch offen oder müssen sie vor dem Plädoyer gestellt werden?
7. Welche Strafzumessungsargumente stehen zur Verfügung (Geständnis, Schadenswiedergutmachung, Erstmaligkeit, Familie)?
8. Besteht die Möglichkeit einer Verständigung nach § 257c StPO oder ist das Plädoyer ohne Absprache zu halten?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 258 StPO | Schlussvorträge; Reihenfolge: StA – Nebenklage – Verteidigung; letztes Wort des Angeklagten Abs. 3 |
| § 244 StPO | Beweisaufnahme; Ablehnungsgründe für Beweisanträge (Abs. 3–6) |
| § 257 StPO | Erklärungsrecht nach Beweisaufnahme |
| § 257c StPO | Verständigung im Strafverfahren |
| § 136a StPO | Verbotene Vernehmungsmethoden; absolutes Verwertungsverbot |
| § 344 StPO | Revisionsbegründung; Verfahrensrüge und Sachrüge |
| § 20 StGB | Schuldunfähigkeit; Voraussetzungen und Folgen |
| § 21 StGB | Verminderte Schuldfähigkeit; Strafrahmenverschiebung nach § 49 StGB |
| § 22 StGB | Versuch; Definition |
| § 23 StGB | Strafbarkeit und Strafrahmenmilderung beim Versuch (Abs. 2) |
| § 24 StGB | Rücktritt vom Versuch; Straflosigkeit |
| § 32 StGB | Notwehr |
| § 34 StGB | Rechtfertigender Notstand |
| § 35 StGB | Entschuldigender Notstand |
| § 46 StGB | Strafzumessung: Grundsätze und Gesichtspunkte |
| § 46a StGB | Täter-Opfer-Ausgleich als Strafmilderungsgrund |
| § 49 StGB | Mildernde Umstände; Strafrahmenverschiebung (Abs. 1 und Abs. 2) |
| § 52 StGB | Tateinheit (Idealkonkurrenz) |
| § 53 StGB | Tatmehrheit (Realkonkurrenz) |
| § 56 StGB | Strafaussetzung zur Bewährung |

---

## Leitentscheidungen

| Aktenzeichen | Gericht / Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

---

## Prüfschema Plädoyervorbereitung

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Hilfsbeweisanträge prüfen: Noch offene Beweisfragen vor Schluss der Beweisaufnahme sichern; ggf. Ablehnung als Revisionsstoff | § 244 StPO |
| 2 | Verfahrensrügen dokumentieren: Verstöße gegen StPO während HV notieren; Formalvoraussetzungen prüfen | § 344 StPO |
| 3 | Beweisaufnahme-Protokoll auswerten: Widersprüche in Zeugenaussagen, Inkonsistenzen zwischen Polizeiprotokoll und HV-Aussage | § 261 StPO |
| 4 | Verwertungsverbote prüfen: § 136a StPO (verbotene Methoden), § 100a StPO (TKÜ ohne Voraussetzungen), § 105 StPO (Durchsuchung ohne richterliche Anordnung) | §§ 136a, 100a, 105 StPO |
| 5 | Tatbestand subsumieren: Objektiver Tatbestand (Handlung, Erfolg, Kausalität, objektive Zurechnung); Subjektiver Tatbestand (Vorsatz, Fahrlässigkeit) | Einschlägige §§ StGB |
| 6 | Rechtfertigung/Entschuldigung prüfen: Notwehr § 32, Notstand §§ 34/35, Einwilligung, Erlaubnisirrtum | §§ 32, 34, 35 StGB |
| 7 | Schuldfähigkeit prüfen: § 20 StGB (Ausschluss), § 21 StGB (Verminderung); psychiatrisches Gutachten auswerten | §§ 20, 21 StGB |
| 8 | Versuch/Vollendung prüfen: Versuch nach § 22 StGB; Strafrahmenverschiebung § 23 Abs. 2 i.V.m. § 49 Abs. 1 StGB; Rücktritt § 24 StGB | §§ 22–24, 49 StGB |
| 9 | Konkurrenzen prüfen: Tateinheit § 52 oder Tatmehrheit § 53 StGB; Gesetzeskonkurrenz (Spezialität, Subsidiarität, Konsumtion) | §§ 52, 53 StGB |
| 10 | Strafzumessung vorbereiten: Strafrahmen feststellen; Verschiebung nach § 49 StGB einbeziehen; Zumessungsgesichtspunkte nach § 46 Abs. 2 StGB sammeln | §§ 46, 49 StGB |
| 11 | Bewährungsvoraussetzungen prüfen: § 56 StGB – Straferwartung unter 2 Jahre; positive Sozialprognose; ggf. besondere Umstände § 56 Abs. 2 StGB | § 56 StGB |
| 12 | Plädoyerstruktur erstellen: Eröffnung (Sachverhalt aus Verteidigersicht), Beweiswürdigung (Zeugenkritik), Rechtliche Würdigung (Subsumtion), Strafzumessung | § 258 StPO |
| 13 | Letztes Wort vorbereiten: Mandant über Inhalt und Wirkung aufklären; Reue, Entschuldigung, Sachverhalt – auf Plädoyer abstimmen | § 258 Abs. 3 StPO |
| 14 | Revisions-Rügeliste finalisieren: Verfahrensrügen geordnet nach Schluss der HV; Fristenkontrolle Revisionsbegründung (1 Monat) | § 344 StPO, § 345 StPO |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Plaedoyer Strafverteidigung vorbereiten | Plaedoyerstruktur; Template unten |
| Variante A — Verstaendigung nach § 257c StPO | Absprachen-Plaedoyer; andere Argumentation |
| Variante B — Freispruch angestrebt | Beweis-Plaedoyer; jede Anklage-Schwaeche herausarbeiten |
| Variante C — Strafmass streitig | Strafzumessungs-Plaedoyer; § 46 StGB-Aspekte |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1 – Plädoyerstruktur (Muster-Gliederung)

```
PLÄDOYER
Strafsache gegen [Name]
Aktenzeichen: [...]
Hauptverhandlung am [Datum]

I. ERÖFFNUNG
 Zusammenfassung des Sachverhalts aus Verteidigersicht.
 "Was ist in dieser Sache tatsächlich passiert?"

II. BEWEISWÜRDIGUNG – TATSÄCHLICHES
 A. Zeugenaussagen
 - Zeuge X: Widerspruch zwischen polizeilicher Vernehmung
 vom [Datum] (Protokoll Bl. [X]) und HV-Aussage am
 [Datum]; Aussage daher nicht glaubwürdig.
 - Zeuge Y: Eigeninteresse; Vorwurf von [Datum].
 B. Sachverständigengutachten
 - Methode anerkannt? Anknüpfungstatsachen vollständig?
 - Gegen-Auslegung möglich?
 C. Verwertungsverbote
 - Beschlagnahme vom [Datum]: ohne richterliche Anordnung
 (§ 105 StPO); Beweisverwertungsverbot geltend machen.

III. RECHTLICHE WÜRDIGUNG
 A. Tatbestand
 - Objektiver Tatbestand: [Handlung X] führte nicht zu
 [Erfolg Y]; Kausalität fehlt / obj. Zurechnung ausgeschlossen.
 - Subjektiver Tatbestand: Vorsatz nicht nachgewiesen.
 B. Schuldfähigkeit / Versuch / Konkurrenzen
 - [Ggf. § 21 StGB; § 23 Abs. 2 StGB; § 52 StGB.]

IV. STRAFZUMESSUNG (hilfsweise)
 Strafrahmen: § [X] StGB: [Mindeststrafe] bis [Höchststrafe].
 Strafmilderung:
 - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 - Erstmals straffällig
 - Schadenswiedergutmachung: [Betrag EUR] bereits geleistet
 - Familie: [X] Kinder, Alleinverdiener
 - Lange Verfahrensdauer: [X] Jahre; Belastung für Mandanten

V. BEWÄHRUNG (§ 56 StGB)
 Sozialprognose positiv: keine Vorstrafen, stabiles Umfeld,
 Arbeitsstelle gesichert, Wohnverhältnisse geordnet.

VI. ANTRAG
 Ich beantrage, [Name] vom Vorwurf der [Straftat]
 freizusprechen / zu einer Freiheitsstrafe von [X] Monaten
 auf Bewährung zu verurteilen.
```

### Baustein 2 – Hilfsbeweisantrag (vor Schluss der Beweisaufnahme)

```
An den Vorsitzenden
Aktenzeichen: [...]

Hilfsbeweisantrag gemäß § 244 Abs. 3 StPO

In der Hauptverhandlung gegen [Name] beantrage ich
hilfsweise für den Fall, dass das Gericht von einer
Verurteilung wegen [Tatbestand] ausgeht:

Beweis darüber, dass [Beweisbehauptung], durch Einvernahme
des Zeugen [Name, Anschrift] / Einholung eines Sachverstän-
digengutachtens des [Institut/Sachverstand].

Das Beweismittel ist erheblich, weil [Begründung].

Eine Ablehnung wäre rechtsmittelrelevant (§ 344 StPO).

[Ort, Datum]
[Unterschrift]
```

### Baustein 3 – Memo letztes Wort des Angeklagten

```
VORBEREITUNG LETZTES WORT
(Vertraulich – Anwalt-Mandant-Gespräch)

Empfehlung für Inhalt des letzten Wortes:

1. Reue / Entschuldigung:
 Falls Geständnis oder Teilgeständnis: Kurze ehrliche
 Entschuldigung gegenüber dem Gericht und ggf. der Verletzten.
 Nicht ausschweifend – Glaubwürdigkeit durch Kürze.

2. Sachverhaltshinweise:
 Nur wenn Plädoyer und letztes Wort koordiniert:
 "Ich möchte noch einmal betonen, dass ich nie die Absicht
 hatte, [Person X] zu schädigen."

3. Persönliche Situation:
 Kurz: Familie, Arbeit, Therapie, Wiedergutmachung.

4. Was NICHT sagen:
 – Schuldzuweisung an Zeugen oder Opfer
 – Rechtsmittelankündigung
 – Lange Stellungnahmen zur Rechtslage (das ist Sache der Verteidigung)

Timing: Kurz (1–3 Minuten). Wirkung: Menschlichkeit zeigen.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Tatnachweis | Staatsanwaltschaft trägt volle Beweislast; in dubio pro reo bei Zweifeln |
| Schuldunfähigkeit § 20 StGB | Im Strafverfahren: Gericht prüft von Amts wegen; Gutachten erforderlich; Zweifel gehen zu Lasten der Anklage |
| Notwehr § 32 StGB | Angeklagte/r muss Notwehrlage behaupten; StA muss Überschreitung beweisen |
| Rücktritt § 24 StGB | Angeklagte/r trägt Freiwilligkeit des Rücktritts; Zweifelssatz gilt |
| Verwertungsverbot | Verteidigung muss Verfahrensverstoß konkret rügen; Gericht prüft dann von Amts wegen |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Vor Schluss der Beweisaufnahme | Hilfsbeweisanträge stellen | § 244 StPO |
| 1 Woche nach Urteilsverkündung | Revision einlegen (Einlegungsfrist) | § 341 StPO |
| 1 Monat nach Urteilszustellung | Revisionsbegründungsfrist; Verfahrensrügen müssen vollständig sein | § 345 StPO |
| Laufend | Verfahrensrügen in der HV protokollieren lassen | § 344 StPO |
| Je nach Delikt | Strafverfolgungsverjährung (§ 78 StGB): 3 Jahre (leichte Delikte) bis 30 Jahre (Mord) | § 78 StGB |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Geständnis wurde freiwillig abgelegt" | § 136a StPO prüfen; Geständnis nach langer Vernehmung ohne Pause, unter psychischem Druck oder nach falscher Versprechung kann Verwertungsverbot begründen |
| "Zeuge ist glaubwürdig, kein Grund zur Zweifel" | Methodische Glaubwürdigkeitsprüfung: Konstanz (Aussage-Polizei vs. HV), Detailreichtum, Eigeninteresse; BGH-Maßstäbe (BGH NStZ 2007, 112) |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Keine Revision möglich, da Berufungsurteil" | § 333 StPO erlaubt Revision auch gegen Berufungsurteile; Verfahrensrügen aus der Berufungsverhandlung sind rügefähig |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Hauptverhandlungsgebühr | VV-RVG Nr. 4112 (Verfahrensgebühr) + Nr. 4114/4115 (Terminsgebühr je Sitzungstag) |
| Mehrtägige HV | Erhöhung ab 2. Sitzungstag; Pauschbetrag nach VV-RVG Nr. 4116 |
| Verständigung § 257c StPO | Keine gesonderte Gebühr; im Rahmen HV-Mandat |
| Revisionsmandat | Eigenständige Verfahrensgebühr VV-RVG Nr. 4130 (Sprungrevision) oder 4134 (Revision nach Berufung) |
| Kostenentscheidung bei Freispruch | Kosten trägt Staatskasse; notwendige Auslagen des/der Freigesprochenen nach § 467 StPO |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Freispruch realistisch | Plädoyer fokussiert auf Beweiswürdigung und in dubio pro reo; keine Strafzumessungsargumente in Hilfsplädoyer rein, solange kein Geständnis |
| Verurteilung sicher, Strafmaß offen | Vollständige Strafzumessungsargumentation: Erstmaligkeit, Familie, Geständnis, § 46a StGB, Verfahrensdauer |
| Bewährung das Ziel | Sozialprognose aufbereiten: Arbeitsplatznachweis, Wohnanschrift, Familiensituation, ggf. Therapiebereitschaft |
| Verständigung § 257c StPO gescheitert | Plädoyer ohne Absprache hält; eigene Beweiswürdigung betonen; Verständigungsablauf für Revision dokumentieren |
| § 21 StGB und § 49 StGB relevant | Strafrahmenverschiebung ausdrücklich beantragen; Gutachten auswerten; psychiatrische Befunde zitieren |
| Revision vorbereiten | Verfahrensrügen während HV notieren; vollständige Rügedokumentation; Einlegungsfrist 1 Woche nach Urteil |

---

## Anschluss-Skills

- `fachanwalt-strafrecht-adhaesionsverfahren` – Schadenswiedergutmachung im Plädoyer als § 46a StGB-Argument
- `fachanwalt-strafrecht-nebenklage-opfervertretung` – Gegenstrategie zur Nebenklage-Schlussvortrag
- `fachanwalt-strafrecht-zeugenbeistand` – Verwertbarkeit von Zeugenaussagen im Plädoyer
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` – Strafzumessung bei Wirtschaftsstrafsachen

---

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

---

## Skill: `schriftsatzkern-substantiierung`

_Substantiierter Schriftsatzkern für Strafverfahren Einspruch und Revision: Anwendungsfall Strafverteidiger muss Einspruch gegen Strafbefehl Revisionsbegründung oder Klageerzwingungsantrag verfassen: Substantiierter Schriftsatzkern für Strafverfahren Einspru..._

# Substantiierter Schriftsatzkern für Strafverfahren Einspruch und Revision: Anwendungsfall Strafverteidiger muss Einspruch gegen Strafbefehl Revisionsbegründung oder Klageerzwingungsantrag verfassen


## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Plaedoyer Vorbereitung** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Strafrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; StPO; StGB — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Substantiierter Schriftsatzkern für Strafverfahren Einspruch und Revision: Anwendungsfall Strafverteidiger muss Einspruch gegen Strafbefehl Revisionsbegründung oder Klageerzwingungsantrag verfassen. §§ 410 ff. StPO Einspruch Strafbefehl, § 344 StPO Revisionsbegründung, § 172 Abs. 2 bis 3 StPO Klageerzwingungsantrag, § 147 StPO Akteneinsicht. Prüfraster Tatsachenvortrag-Geruest, Beweisantrag-Liste, Verfahrenshindernisse, Sachrügen und Verfahrensrügen, Strafmass-Hilfsantrag. Output vollständiger Verteidigungs-Schriftsatz mit Antrag Begründung und Beweisangebot. Abgrenzung zu Plaedoyer-Vorbereitung und zu Hauptverhandlung.

### Schriftsatzkern und Substantiierung im Allgemeines und Wirtschaftsstrafrecht

## Wann dieser Arbeitsgang greift

- Es soll ein vollwertiger Verteidigungs- oder Antragsschriftsatz im Strafverfahren erstellt werden, typischerweise: Einspruch gegen Strafbefehl (§§ 410 ff. StPO), Revisionsbegruendung (§ 344 StPO), Klageerzwingungsantrag (§ 172 Abs. 2-3 StPO), Beschwerde, Antrag auf gerichtliche Entscheidung (§ 23 EGGVG), Adhaesionsantrag-Erwiderung (§§ 403 ff. StPO).
- Mandatsannahme und ggf. Verstaendigung sind abgeschlossen oder gescheitert.
- Einspruchs-, Revisions-, Beschwerde- oder Klageerzwingungsfrist ist bekannt und im Kalender eingetragen.

## Aufbauschema

### A. Rubrum

- Beschuldigte/Angeklagte/Verurteilte (Name, Geburtsdatum, ladungsfaehige Anschrift) - exakte Schreibweise wie in Strafbefehl/Anklage/Urteil.
- Verteidigerin/Verteidiger mit Beiordnung-/Wahlvermerk (Pflicht-/Wahlverteidigung).
- Gericht/Staatsanwaltschaft (Zuständigkeit pruefen; bei Revision zuständiges Revisionsgericht).
- Aktenzeichen (Bezugs-Az., neues Az. nach Eingang).
- Bezeichnung der angefochtenen Entscheidung mit Datum.

### B. Antraege

Strafprozessual passende Antraege je nach Verfahrenstyp:

- **Einspruch gegen Strafbefehl:** Antrag auf Aufhebung des Strafbefehls und Freispruch, hilfsweise Einstellung (§§ 153, 153a, 154, 170 Abs. 2 StPO entsprechend), hilfsweise milderes Strafmass.
- **Revisionsbegruendung:** Antrag auf Aufhebung des Urteils und Zurueckverweisung, hilfsweise eigene Sachentscheidung (§ 354 StPO), bei reinem Strafausspruch ggf. nur Aufhebung des Rechtsfolgenausspruchs.
- **Klageerzwingung:** Antrag auf Anordnung der Anklageerhebung gegen Beschuldigte/n (§ 175 StPO).
- **Beschwerde gegen Haftbefehl:** Aufhebung des Haftbefehls, hilfsweise Aussetzung des Vollzugs gegen Auflagen (§ 116 StPO).
- **Beweisantraege** gem. § 244 Abs. 3-6 StPO als gesonderter Block; Connexitaet, Konnex zum Tatvorwurf und konkrete Beweistatsache.

### C. Tatsachenvortrag (Verteidigungs-Sachverhalt)

Der Substantiierungs-Kern; pro Tatvorwurf bzw. Tatbestand eine eigene Tatsachen-Sequenz:

1. **Sachverhalts-Chronologie** mit konkreten Daten (Tag, Uhrzeit, Ort, Personen) - eigene Version der Verteidigung.
2. **Bestrittene Tatsachen der Anklage** explizit benennen; pauschales Bestreiten reicht in der Revision nicht.
3. **Entlastende Tatsachen** mit Beweismitteln (Zeugen, Urkunden, Sachverstaendige, Augenschein).
4. **Verfahrensgeschichte** (Beschuldigtenvernehmung, Akteneinsicht, Haftgrund, Belehrungen § 136 StPO).

### D. Rechtliche Wuerdigung

Strafrechtlicher Pruefungsaufbau:

1. **Tatbestand** des StGB/Nebenstrafrechts (BtMG, AO §§ 369 ff., StVG, WaffG) nennen.
2. **Tatbestandsmerkmale** durchgehen; jedes Merkmal gegen den eigenen Tatsachenvortrag spiegeln (objektive und subjektive Seite; Vorsatz/Fahrlaessigkeit).
3. **Rechtfertigungsgruende** (§§ 32, 34 StGB) und **Entschuldigungsgruende** (§§ 33, 35 StGB) pruefen.
4. **Verfahrenshindernisse:** Verjährung (§ 78 StGB), Strafklageverbrauch (Art. 103 III GG, ne bis in idem), fehlender Strafantrag (§ 77 StGB), Immunitaet, Verfolgungsverjaehrung im Steuerstrafrecht (§ 376 AO).
5. **Beweiswuerdigung-Kritik:** Indizienkette, Aussage-gegen-Aussage-Konstellation, Glaubwuerdigkeitsanalyse.
6. **Rechtsprechungs-Verweise:** BGH-Strafsenate, BVerfG (Art. 103 GG, Schuldprinzip), EGMR (Art. 6 EMRK).
7. **Subsumtions-Ergebnis** klar formulieren (Freispruch, Einstellung, Strafmilderung).

### E. Beweisantraege (§ 244 StPO)

Pflichtbestandteil, ohne den Substantiierung nicht ausreicht:

- **Zeugenbeweis:** Name, ladungsfaehige Anschrift, Beweistatsache in einem Satz, Konnexitaet (Wieso kennt Zeugin die Tatsache?).
- **Sachverstaendigenbeweis:** Beweistatsache, vorgeschlagene Sachgebietsbezeichnung; bei DNA, Blutalkohol, IT-Forensik, Brandursache, Schussspurenanalyse.
- **Urkundenbeweis:** konkrete Aktenfundstelle, Inhalt mit Bezug zur Beweistatsache (Verlesung gem. § 249 StPO).
- **Augenscheinsbeweis:** Tatort, Tatwaffe, Lichtbild, Videoaufnahme.
- **Praesente Beweismittel** in der Hauptverhandlung (§ 245 StPO).
- Abgrenzung Beweisantrag / Beweisermittlungsantrag - Beweisantrag braucht bestimmte Tatsache + bestimmtes Beweismittel.

### F. Anlagenverzeichnis

- Anlagen mit Datum, Aussteller, Inhaltsbeschreibung in einem Satz.
- Erwaehnung im Tatsachenvortrag mit Aktenfundstelle (Bl. ... d.A.).
- Bei Revision: keine neuen Tatsachen, sondern Verweis auf Aktenstellen.

## Substantiierungs-Fallen im Strafverfahren

- **Pauschales Bestreiten** in der Revision (§ 344 Abs. 2 StPO verlangt bei Verfahrensruege bestimmte Tatsachen, die den Verfahrensmangel ergeben).
- **Verfahrensruege ohne Tatsachenvortrag** zum Verfahrensgeschehen (Schweigegrund § 261 StPO, abgelehnter Beweisantrag, Verletzung § 244 StPO).
- **Sachruege** zu allgemein ("Beweiswuerdigung sei luckenhaft") - notwendig: konkret welche Lueke und warum sie ergebnisrelevant ist.
- **Beweisantrag zur falschen Tatsache** - Beweistatsache deckt nur Teilaussage ab; Gericht lehnt mit § 244 Abs. 3 StPO ab.
- **Konkurrenzen** (Tateinheit/Tatmehrheit, §§ 52, 53 StGB) nicht ausgearbeitet.

## Pruefkette vor Versand

1. Antragsformulierung strafprozessual passend (Freispruch, Einstellung, Aufhebung, Zurueckverweisung)?
2. Jede Tatbestandsmerkmals-Subsumtion mit eigener Tatsache + Beweis hinterlegt?
3. Frist eingehalten (Einspruchsfrist 2 Wochen § 410 StPO; Revisionseinlegung 1 Woche § 341 StPO, Revisionsbegruendung 1 Monat § 345 StPO; Klageerzwingung 1 Monat § 172 Abs. 2 StPO)?
4. Verfahrenshindernisse von Amts wegen geprueft (Verjährung, Strafantrag)?
5. Beweisantraege bestimmt formuliert (Tatsache + Mittel + Konnexitaet)?
6. Anlagenverzeichnis vollstaendig?
7. beA-Konformitaet (PDF/A, ERVV, qeS bzw. sicherer Uebermittlungsweg)?
8. Vier-Augen-Pruefung durch Sozius oder Senior-Verteidigerin?

## Rechtsprechungs-Werkzeugkasten

- BVerfG (Art. 103 GG, Schuldprinzip, faires Verfahren), BGH-Strafsenate, OLG-Linien, EGMR (Art. 6 EMRK).
- StGB, StPO, BtMG, AO (§§ 369 ff.), OWiG, JGG sowie Nebenstrafrecht (StVG, WaffG, KCanG, AWG).
- Aktuelle Reform- und Gesetzgebungslage einbeziehen (z.B. KCanG-Folgeanpassungen, RAusBeitrG).

## Pflicht-Output

1. **Schriftsatz** mit Rubrum, Antraegen, Tatsachenvortrag, Rechtsausfuehrung, Beweisantraegen, Anlagenverzeichnis.
2. **Anlagen-Konvolut** numerisch geordnet, jede Anlage einzeln benannt.
3. **Frist-Doku** mit Eingangsbestaetigung (beA-Eingangsnachricht).
4. **Mandanten-Erinnerung** mit Naechster-Schritt-Aufgaben (Zeuginnen vorbereiten, Sachverstaendiger, Aktenstudium).

## Beispiel-Tatbestaende im Wirtschaftsstrafrecht

Drei haeufige Tatbestaende und ihre Substantiierungs-Anforderungen:

### Tatbestand 1: Steuerhinterziehung (§ 370 AO)

- Steueranspruch nach Steuergesetz: konkrete Steuerart, Veranlagungszeitraum, Bemessungsgrundlage.
- Unrichtige/unvollstaendige Angabe oder pflichtwidriges Unterlassen: konkrete Erklaerung, konkretes Feld.
- Steuerverkuerzung in bestimmter Hoehe: Differenz aus Steueranspruch und Festsetzung.
- Vorsatz: Wissen und Wollen, bedingter Vorsatz reicht (BGH-Linie).
- Strafzumessung: § 370 Abs. 3 AO (besonders schwerer Fall), Selbstanzeige § 371 AO.

### Tatbestand 2: Betrug (§ 263 StGB)

- Taeuschung ueber Tatsachen: konkrete Aeusserung oder konkludentes Verhalten.
- Irrtum: Vorstellung des Getaeuschten; Indizien.
- Vermoegensverfuegung: konkrete Verfuegung mit Schadensrelevanz.
- Vermoegensschaden: Saldo; bei Eingehungsbetrug auch Gefaehrdungsschaden (BVerfG-Konkretisierungsgebot).
- Bereicherungsabsicht und Stoffgleichheit.

### Tatbestand 3: Untreue (§ 266 StGB)

- Vermoegensbetreuungspflicht: Rechtsgrund (Anstellungsvertrag, gesetzliche Pflicht, Geschaeftsfuehrer).
- Pflichtverletzung: konkrete Handlung gegen das Innenverhaeltnis.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Vorsatz auch hinsichtlich Pflichtwidrigkeit.

## Antrags-Muster nach Verfahrenstyp

### Einspruch gegen Strafbefehl

- "Es wird beantragt, den Strafbefehl des AG ... vom ... (Az. ...) aufzuheben und die Angeklagte/den Angeklagten freizusprechen."
- Hilfsweise: "... das Verfahren gemaess § 153 Abs. 2 StPO (alternativ § 153a StPO mit konkreter Auflage) einzustellen."
- Hilfsweise: "... auf eine Geldstrafe von hoechstens X Tagessaetzen zu erkennen."

### Revisionsbegruendung

- "Es wird beantragt, das Urteil des LG ... vom ... mit den ihm zugrundeliegenden Feststellungen aufzuheben und die Sache zur erneuten Verhandlung und Entscheidung an eine andere Strafkammer des LG ... zurueckzuverweisen."
- Bei reinem Rechtsfolgenangriff: "... das Urteil im Rechtsfolgenausspruch aufzuheben."

### Klageerzwingung

- "Es wird beantragt, die Staatsanwaltschaft ... anzuweisen, öffentliche Klage gegen die Beschuldigte/n ... wegen ... zu erheben."

### Annex-Antraege

- Pflichtverteidigerbestellung (§ 140 StPO).
- Akteneinsicht (§ 147 StPO).
- Haftaussetzung (§ 116 StPO) oder -aufhebung.
- Wiedereinsetzung in den vorigen Stand (§§ 44 ff. StPO).

## Beweisaufnahme - was das Gericht sehen will

### Zeugenbeweis

- Form: "Beweis: Vernehmung der Zeugin Name, ladungsfaehige Anschrift, zum Beweis der Tatsache, dass ...; Konnexitaet: Die Zeugin war anwesend / hat das Gespraech selber gefuehrt / hat den Vorgang dokumentiert."
- Keine Beweisermittlung ueber Zeugnis - Beweistatsache muss bestimmt sein.

### Sachverstaendigenbeweis

- Beweistatsache: konkret (z.B. Blutalkoholwert zum Tatzeitpunkt, Programmierfehler im Buchungssystem, Brandursache).
- Sachgebiet benennen, Notwendigkeit gegenueber anderen Beweismitteln darlegen.
- Bei Gegengutachten: Privatgutachten beilegen und gerichtlich neues Sachverstaendigengutachten beantragen.

### Urkundenbeweis

- Aktenstelle: Bl. ... d.A. mit konkretem Inhalt.
- Verlesung gem. § 249 StPO oder Selbstleseverfahren gem. § 249 Abs. 2 StPO beantragen.

### Augenschein

- Tatort, Tatwaffe, Aufnahme - Antrag auf Inaugenscheinnahme in der Hauptverhandlung.

## Verfahrens- und Sachruege in der Revision

Schon im Schriftsatz die Trennung sauber durchziehen:

- **Verfahrensruegen:** § 244 StPO (Ablehnung Beweisantrag), § 261 StPO (Wuerdigungs-Lueke aus Inbegriff der Hauptverhandlung), § 338 StPO (absolute Revisionsgruende), § 136 StPO (Belehrungsverstoss); jede Ruege braucht Tatsachenvortrag, der den Mangel ergibt (§ 344 Abs. 2 S. 2 StPO).
- **Sachruegen:** Subsumtions-, Konkurrenz-, Strafzumessungs-, Schuldfahigkeits-Fehler; Bezug auf die Urteilsgruende, nicht auf das Akteninhalt.

## Elektronische Einreichung (beA, EGVP, EBO)

- PDF/A-2 oder PDF/A-3, mit eingebetteten Schriften.
- Strukturdatensatz nach ERVV pflicht-konform (Sender, Empfaenger, Az., Versanddatum).
- Qualifizierte elektronische Signatur (qeS) der einreichenden RA-Person oder einfacher elektronischer Versand ueber beA (sicherer Uebermittlungsweg).
- Eingangsbestaetigung aufbewahren - Datum der Einreichung ist Fristwahrungs-Beweis.
- Spezifika im Strafverfahren: Strafverteidiger reichen Schriftsaetze regelmaessig ueber beA an Strafkammer/Staatsanwaltschaft ein; Postausgang nach § 32a StPO.

## Schriftsatz-Stil

- Aktiv, kurze Saetze, klare Subsumtion.
- Keine Floskeln; Beweismittel-Zitate woertlich mit Aktenfundstelle.
- Sachlich auch bei provokanter Anklage.
- Bei Revision: keine Tatsachenwertung jenseits der Urteilsgruende.

## Vier-Augen-Check

Vor Versand:

- [ ] Antrag strafprozessual passend (Freispruch/Einstellung/Aufhebung/Zurueckverweisung)
- [ ] Frist gewahrt mit Reserve (Einspruch 2 Wochen, Revisionseinlegung 1 Woche, Revisionsbegruendung 1 Monat)
- [ ] Jede Tatsache hat Beweisantrag oder Aktenfundstelle
- [ ] Verfahrenshindernisse von Amts wegen geprueft
- [ ] Sachruege/Verfahrensruege sauber getrennt
- [ ] Rechtsprechungs-Zitat aktuell (BGH/BVerfG/EGMR)
- [ ] beA-konform mit qeS oder sicherem Uebermittlungsweg
- [ ] Senior-/Sozius-Freigabe

## Cross-Refs

- `erstgespraech-mandatsannahme` (im selben Plugin) für Mandatsannahme und Erstprognose.
- `vergleichsverhandlung-strategie` (im selben Plugin) für Verstaendigung § 257c StPO, Einstellung § 153a StPO und Adhaesion.
- `fachanwalt-strafrecht-hauptverhandlung-vorbereiten` für Beweisantraege in der Hauptverhandlung.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

