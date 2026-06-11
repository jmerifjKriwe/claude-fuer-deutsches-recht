# Megaprompt: fachanwalt-verwaltungsrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 65 Skills des Plugins `fachanwalt-verwaltungsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Fachanwalt Verwaltungsrecht: ordnet Rolle (Bürger/Antragsteller, Behörde, Verwaltungsge…
2. **mandat-triage-verwaltungsrecht** — Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofor…
3. **orientierung-mandat-fachanwaltschaft** — Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen ueberb…
4. **orientierung-sonderfall-edge-case** — Orientierung: Sonderfall und Edge-Case-Prüfung: Orientierung: Sonderfall und Edge-Case-Prüfung.
5. **erstgespraech-mandatsannahme** — Strukturierter Erstgespraechsleitfaden für Allgemeines Verwaltungs- und Bauplanungsrecht: Erfassung der Konstellation, K…
6. **erstpruefung-und-mandatsziel** — Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.
7. **drittanfechtung-umwelt** — Drittanfechtung umweltrechtlicher Genehmigungen (BImSchG, BauGB) durch Nachbarn oder Umweltverband: Klagebefugnis und ma…
8. **energieanlagen-bimschg-genehmigung-verfahren** — BImSchG-Genehmigung für Energieanlagen (Wind, Biogas, Biomasse, Wasserstoff-Elektrolyseur) begleiten: Vorhabentraeger be…
9. **energietrassen-planfeststellung-rechtsschutz** — Rechtsschutz gegen Planfeststellungsbeschluss für Strom- und Gastrassen klagen: Anlieger oder Umweltverband klagt gegen …
10. **normenkontrolle-47-vwgo** — Normenkontrollantrag nach § 47 VwGO gegen Bauleitplaene, Rechtsverordnungen oder Satzungen: Betroffener will Bebauungspl…
11. **schriftsatzkern-substantiierung** — Substantiierten Schriftsatzkern für verwaltungsrechtliche Klagen und Anträge erstellen: Widerspruch, Anfechtungsklage, V…
12. **vergleich-106-vwgo-behoerde** — Verwaltungsrechts-Vergleich nach § 106 VwGO und öffentlich-rechtlicher Vertrag nach § 55 VwVfG: Mandant will Streit mit …
13. **vergleichsverhandlung-strategie** — Vergleichsverhandlungs-Strategie für Verwaltungsrechtsstreitigkeiten: Partei oder Anwalt will außergerichtlichen Verglei…
14. **beamten-disziplinarverfahren** — Beamten-Disziplinarverfahren führen oder verteidigen: Beamter hat Dienstvergehen begangen oder ist Dienstherr bei Einlei…
15. **fa-vwgo-widerspruchsbescheid-abschleppen-oepnv** — Fa VwGO Widerspruchsbescheid Abschleppen Oepnv: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtspre…

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Fachanwalt Verwaltungsrecht: ordnet Rolle (Bürger/Antragsteller, Behörde, Verwaltungsgericht), markiert Frist (§ 74 VwGO Klagefrist 1 Mon.), wählt Norm (VwGO, VwVfG, AO (steuerlich)) und Zuständigkeit (VG, OVG/VGH, BVerwG), leitet zum passenden Spezial-Skill._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Fachanwalt Verwaltungsrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `amtshaftung-paragraf-839-bgb-art-34-gg` — Amtshaftung Paragraf 839 BGB ART 34 GG
- `anfechtungs-risikoampel-und-gegenargumente` — Anfechtungs Eilrechtsschutz ABS
- `anhoerung-paragraf-28-vwvfg` — Anhoerung Paragraf 28 Vwvfg
- `anordnung-quellenkarte` — Anordnung Quellenkarte
- `drittanfechtung-umwelt` — Drittanfechtung
- `eilrechtsschutz-paragraf-80-vwgo` — Eilrechtsschutz Paragraf 80 Vwgo
- `einstweilige-verhandlung-vergleich-und-eskalation` — Einstweilige Fachanwalt Kanzlei
- `ermessen-paragraf-40-vwvfg` — Ermessen Paragraf 40 Vwvfg
- `erstgespraech-mandatsannahme` — Erstgespraech Mandatsannahme FA Vwgo
- `workflow-mandantenkommunikation` — FA Verwaltungsrecht Mandant Redteam Gate
- `einstieg-schnelltriage-fallrouting` — FA Verwaltungsrecht Start Chronologie Fristen
- `klagefrist-paragraf-58-vwgo-bverwg-4-c-1-19` — Klagefrist Paragraf 58 Vwgo Bverwg 4 C 1 19
- `kommunalrecht-paragraf-2-go` — Kommunalrecht Paragraf 2 GO
- `anschluss-routing` — Anschluss Routing
- `dokumente-intake` — Dokumente Intake

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Fachanwalt Verwaltungsrecht sind VwGO, VwVfG, § 80 Abs 5 VwGO einstweilige Anordnung Normenkontrolle Polizei. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-verwaltungsrecht`

_Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Checks: Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Check..._

# Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Checks


## Aktenstart statt Formularstart

Wenn zu **Widerspruchsschrift Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Verwaltungsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Eingangs-Triage für verwaltungsrechtliche Mandate: Erst-Qualifizierung des Sachgebiets, Verfahrensstands und Frist-Sofort-Checks. Normen: § 70 VwGO (Widerspruch 1 Monat), § 74 VwGO (Klage 1 Monat), § 75 VwGO (Untätigkeitsklage 3 Monate). Prüfraster: Sachgebiet (Bau, Gewerbe, Polizei, Beamtenrecht, Schule, Subventionen, Auslaender), Behördenebene, Verfahrensstand, Frist-Sofort-Check, Eskalation bei drohendem Vollzug. Output Triage-Protokoll mit Fristen-Ampel, Routing-Empfehlung. Abgrenzung: Detailprüfung siehe widerspruch-oder-klage-erstprüfung; Schriftsatz siehe schriftsatzkern-substantiierung.

### Mandat-Triage Verwaltungsrecht

## Ablauf — sieben Fragen

### Frage 1 — Wer und für wen?

- Bürger gegen Behörde
- Unternehmen gegen Behörde
- Behörde (selten — vertretbar nur unter strikter Trennung)
- Verband-Klagebefugnis

### Frage 2 — Sachgebiet?

- **Bau- und Planungsrecht** Baugenehmigung Nachbarklage Bebauungsplan
- **Gewerberecht** Gewerbeerlaubnis Untersagung Gaststätte Spielhalle
- **Polizei- und Ordnungsrecht** polizeiliche Maßnahme Versammlungsrecht
- **Beamten- und Soldatenrecht** Disziplinar Beurteilung Konkurrentenklage
- **Schule und Hochschule** Versetzung Abitur Zulassung
- **Subventionsrecht** Förderbescheid Rückforderung
- **Asyl- und Ausländerrecht** (an `fachanwalt-migrationsrecht` weiter)
- **Sozialrecht** (an `fachanwalt-sozialrecht` weiter)
- **Steuerrecht** (an `steuerrecht-anwalt-und-berater` weiter)
- **Vergaberecht** (an `fachanwalt-vergaberecht` weiter)
- **Umweltrecht**
- **Versammlungsrecht**
- **Kommunalrecht**

### Frage 3 — Akute Eilbedürftigkeit?

- Sofortige Vollziehung angeordnet
- Vollzug innerhalb Tage angekündigt
- Demonstrationsverbot ein-Tages-Vorlauf
- Räumung droht
- Untersagung erteilt — Geschäftsstillstand
- Bauleitplan-Aufstellung in der Beschlussphase

### Frage 4 — Stand?

- Vor Antragstellung (Beratung)
- Antrag eingereicht — wartet auf Bescheid
- Anhörung läuft § 28 VwVfG
- Bescheid liegt vor (Datum)
- Widerspruchsverfahren läuft
- Klage erhoben (Az VG)
- Berufung / Revision (OVG BVerwG)
- Verfassungsbeschwerde

### Frage 5 — Behörde?

- Bundesbehörde (z.B. BAMF Bundespolizei BfArM)
- Landesbehörde (z.B. Bezirksregierung Landratsamt)
- Kommunalbehörde
- Sondereinrichtung Anstalt öffentlichen Rechts

### Frage 6 — Frist?

- **Widerspruch** ein Monat § 70 VwGO; Bekanntgabe-Fiktion § 41 Abs. 2 VwVfG vier Tage seit 01.01.2025 (PostModG)
- **Klage** ein Monat § 74 VwGO ab Bekanntgabe Widerspruchsbescheid
- **Untätigkeitsklage** § 75 VwGO nach drei Monaten ohne Bescheid
- **Verfassungsbeschwerde** ein Monat § 93 BVerfGG
- **Bei fehlender Rechtsbehelfsbelehrung** ein Jahr § 58 Abs. 2 VwGO

### Frage 7 — Wirtschaftliche Verhältnisse PKH?

- Prozesskostenhilfe § 166 VwGO iVm §§ 114 ff. ZPO
- Beratungshilfe für außergerichtlich

## Routing-Matrix

| Sachgebiet | Folge-Skill |
|---|---|
| Baugenehmigung Nachbarklage | (Skill bau-nachbarklage — perspektivisch) |
| Bauliche Untersagung | `widerspruch-oder-klage-erstpruefung` |
| Gewerbe-Erlaubnis-Streit | `widerspruch-oder-klage-erstpruefung` |
| Beamten-Konkurrentenklage | (Skill konkurrentenklage — perspektivisch) |
| Beurteilung Beamter | (Skill beurteilungsanfechtung — perspektivisch) |
| Schule Versetzung Zulassung | `widerspruch-oder-klage-erstpruefung` |
| Asyl Ausländerrecht | weiter an `mandat-triage-migrationsrecht` |
| Sozialleistung | weiter an `mandat-triage-sozialrecht` |
| Steuerrecht | weiter an `anw-mandat-triage-steuerrecht` |
| Polizei-Maßnahme | (Skill polizei-feststellungs-klage — perspektivisch) |
| Versammlungs-Verbot | `widerspruch-oder-klage-erstpruefung` plus § 80 Abs. 5 VwGO |

## Eilmodus

Bei sofortiger Vollziehung oder akutem Vollzug:

1. Mandantengespräch — Sachverhalt zwanzig Minuten
2. Bescheid einlesen — fünfzehn Minuten
3. Widerspruch einlegen (formloser Schriftsatz) — gleichzeitig
4. Eilantrag § 80 Abs. 5 VwGO oder § 123 VwGO formulieren
5. Bei VG einreichen — Eingang sicherstellen Empfangsbestätigung

## Eskalation

- **Telefon-Sofort** drohender Vollzug binnen Stunden
- **Binnen einer Stunde** Bescheid mit sofortiger Vollziehung
- **Heute** Widerspruchsschrift Eilantrag-Erstentwurf
- **Diese Woche** Klage-Erstentwurf Begründung

## Ausgabe

- `triage-protokoll-verwaltungsrecht.md`
- Frist im Fristenbuch
- Bei Eilmodus: Eilantrag-Entwurf im Anhang
- Mandatsvereinbarung mit Streitwertabschätzung § 52 GKG
- Empfehlung Folge-Skill

## Leitentscheidungen Mandat-Triage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- VwGO §§ 42 58 68 70 74 75 80 80a 123
- VwVfG §§ 28 35 41
- GKG § 52
- BVerwGE Std.Spruch
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

---

## Skill: `orientierung-mandat-fachanwaltschaft`

_Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen ueberblicken: N..._

# Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen ueberblicken


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung im Fachanwaltsrecht Verwaltungsrecht: FAO-Voraussetzungen, Kerngebiete, typische Mandate und Fristen ueberblicken. Normen: VwGO (Anfechtungs-, Verpflichtungs-, Leistungs-, Feststellungsklage, Eilrechtsschutz §§ 80 und 123 VwGO), VwVfG, Polizei- und Ordnungsrecht, Baurecht. Prüfraster: Sachgebiet (Bau, Gewerbe, Polizei, Beamtenrecht), Verfahrensarten, Fristen-Überblick. Output Orientierungs-Memo, Routing zu Fachmodule. Abgrenzung: Detailarbeit in Fachmodule; Mandats-Triage siehe mandat-triage-verwaltungsrecht.

### Fachanwalt für Verwaltungsrecht — Orientierung

## FAO-Voraussetzungen

- Lehrgang 120 Stunden + drei Klausuren.
- 80 Fälle in den letzten drei Jahren, davon mindestens 30 gerichtliche Verfahren.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| Verwaltungsverfahren | VwVfG (Bund) Landes-VwVfG |
| Verwaltungsprozess | VwGO §§ 40 ff. 80 86b 123 |
| Allgemeines Verwaltungsrecht | Quellenprüfung Hartmann Grundbegriffe |
| Polizei- und Ordnungsrecht | Polizei- und Ordnungsgesetze der Länder (PolG NRW BayPAG) |
| Baurecht | BauGB BauNVO Landesbauordnungen |
| Beamtenrecht | BeamtStG BBG Landesbeamtengesetze |
| Versammlungsrecht | VersG / Landesversammlungsgesetze |
| Datenschutz öffentlich | BDSG Landesdatenschutzgesetze |

## Typische Mandate

- Bauantrag Widerspruch und Klage
- Polizei- und Ordnungsverfügung
- Beamtenrechtliche Streitigkeiten (Beurteilung Versetzung Disziplinarverfahren)
- Sozialhilfe vs Eingliederung (Abgrenzung zu Sozialrecht)
- Versammlungsverbot
- Ausländer- und Asylrechtsstreit (siehe fachanwalt-migrationsrecht)
- Verwaltungsvollstreckung

## Fristen

- **Widerspruchsfrist** § 70 VwGO — ein Monat.
- **Klagefrist** § 74 VwGO — ein Monat ab Bekanntgabe.
- **Berufungsantrag (Zulassung)** § 124a VwGO — ein Monat.
- **Eilrechtsschutz** § 80 Abs. 5 VwGO und § 123 VwGO — keine Frist; aber Eilbedürfnis erforderlich.
- **Normenkontrolle** § 47 VwGO — ein Jahr ab Bekanntmachung der Norm.

## Hauptgerichte

- Verwaltungsgericht erste Instanz (§ 45 VwGO).
- OVG / VGH Berufung und Normenkontrolle.
- BVerwG Leipzig Revision.

## Berufsverband

- ARGE Verwaltungsrecht DAV.

## Aktuelle Rechtsprechung (Leitsaetze)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Fristen im Ueberblick

| Verfahrensschritt | Frist | Grundlage |
|---|---|---|
| Widerspruch | 1 Monat | § 70 VwGO |
| Klage | 1 Monat | § 74 VwGO |
| Normenkontrolle | 1 Jahr | § 47 Abs. 2 VwGO |
| Untaetigkeitsklage | 3 Monate | § 75 VwGO |
| Berufungsantrag | 1 Monat | § 124a VwGO |
| Verfassungsbeschwerde | 1 Monat | § 93 BVerfGG |
| Revisionsantrag | 1 Monat | § 139 VwGO |

## Schnittstellen

- **kanzlei-allgemein** für Fristen Versand.
- **fachanwalt-migrationsrecht** bei Auslaenderrecht.
- **fachanwalt-sozialrecht** bei Abgrenzung Sozialgericht vs. Verwaltungsgericht.

---

## Skill: `orientierung-sonderfall-edge-case`

_Orientierung: Sonderfall und Edge-Case-Prüfung: Orientierung: Sonderfall und Edge-Case-Prüfung._

# Orientierung: Sonderfall und Edge-Case-Prüfung


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 28 Abs. 1 VwVfG` — Anhörung vor belastender Verwaltungsentscheidung.
- `§ 37 Abs. 1 VwVfG` — Bestimmtheit des Verwaltungsakts.
- `§ 39 Abs. 1 VwVfG` — Begruendungspflicht.
- `§ 40 VwVfG` — Ermessensausübung und Ermessensfehler.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist, soweit Widerspruchsverfahren vorgesehen.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz gegen Vollziehung.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Orientierung: Sonderfall und Edge-Case-Prüfung.

## Spezialwissen: Orientierung: Sonderfall und Edge-Case-Prüfung
- **Normen-/Quellenanker:** VwGO, VwVfG.

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

---

## Skill: `erstgespraech-mandatsannahme`

_Strukturierter Erstgespraechsleitfaden für Allgemeines Verwaltungs- und Bauplanungsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen: Strukturierter Erstgespra..._

# Strukturierter Erstgespraechsleitfaden für Allgemeines Verwaltungs- und Bauplanungsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Strukturierter Erstgespraechsleitfaden für Allgemeines Verwaltungs- und Bauplanungsrecht: Erfassung der Konstellation, Konflikt- und GwG-Check, Vollmacht, Streitwert/Gebührenvereinbarung, Fristen-Erstprognose und Handlungsweichen.

### Erstgespraech und Mandatsannahme im Allgemeines Verwaltungs- und Bauplanungsrecht

## Wann dieser Arbeitsgang greift

- Neue Anfrage aus dem Bereich Allgemeines Verwaltungs- und Bauplanungsrecht (Telefon, Mail, Empfehlung, Walk-in).
- Mandantin oder Mandant beschreibt Sachverhalt unstrukturiert; viele Anlagen ohne System.
- Vor jeder weiteren fachlichen Bearbeitung: erst Annahme klaeren, Konflikt- und GwG-Pruefung, Vollmacht, Streitwert/Vereinbarung, Fristen.

## Phasen des Erstgespraechs

### 1. Aufnahme der Konstellation (10-15 Min.)

Standard-Fragenraster für Allgemeines Verwaltungs- und Bauplanungsrecht:

- Beteiligte (Vor-/Nachname, Geburtsdatum, Anschrift, Rolle: Klaegerin/Beklagter, Antragsteller, Beschuldigter)
- Konflikt-Kern in einem Satz ("Was ist Ihr Ziel?")
- Konkrete fachliche Stossrichtung: VA, Widerspruch, Klage VG, Bauplanung, Gewerberecht, Beamtenrecht
- Bisherige Korrespondenz (Bescheide, Schreiben der Gegenseite, anwaltliche Vertretung der Gegenseite?)
- **Fristenscreening sofort:** anstehende Klage-/Widerspruchs-/Einspruchsfristen aus den vorgelegten Schreiben (z.B. Widerspruch, Anfechtungsklage VG, Verpflichtungsklage, Eilantrag § 80 Abs. 5 VwGO). Frist-Alarm an die Vorbereitung weitergeben.

### 2. Konflikt-Pruefung und GwG-Check (5 Min.)

- Konflikt-Check ueber Mandantsystem: Gegnerin, Streitgegenstand, frueherer Mandant?
- GwG-Identifizierung: amtlicher Lichtbildausweis (Ausweisscan), bei juristischer Person Handelsregister-/Transparenzregister-Auszug, ggf. wirtschaftlich Berechtigte/n.
- Risikobewertung (niedrig/mittel/hoch) abhaengig von Mandatscharakter, Bargeld, Auslandsbezug.
- Doku im Mandatsbogen (Pflicht nach §§ 10 ff. GwG i.V.m. § 2 Abs. 1 Nr. 10 GwG für RA-Mandate).

### 3. Vollmacht und Schweigepflichtentbindung

- Allgemeine Prozess-/Aussenvollmacht (BORA, ZPO, FamFG, je nach Fachgebiet).
- Spezielle Vollmachten: ggf. Akteneinsicht Strafakte, KV-Abrechnungsdaten, Sozialdaten (Schweigepflichtentbindung gegenueber Krankenkasse, Arzt, Behörde).
- Bei Eheleuten/GbR/GmbH: einzelvollmachtgebende Person und Vertretungsmacht klaeren.

### 4. Streitwert und Gebührenvereinbarung

Standard-Streitwerte im Bereich Allgemeines Verwaltungs- und Bauplanungsrecht:

- Skizze: Streitwert grob abschaetzen (z.B. Hauptforderung, ggf. + Zinsen, Nebenforderungen).
- RVG-Pauschalrechnung (Berechnungstool im Plugin) oder Stundenhonorarvereinbarung.
- Beratungshilfe-/Prozesskostenhilfe-Antrag pruefen, wenn wirtschaftlich angezeigt.
- Vorschussanforderung nach § 9 RVG.

### 5. Strategie-Erstskizze

Drei Weichen am Ende des Erstgespraechs:

- **Mandat annehmen:** vollstaendig (Pruefung + Schriftsatz) oder begrenzt (nur Pruefung/Gutachten).
- **Verweisen:** wenn Spezialgebiet ausserhalb der Fachanwaltschaft, oertlich unzuständig oder Konflikt.
- **Ablehnen:** offensichtlich aussichtslos, GwG-Hit, Bauchgefuehl-Vorsicht.

## Pflicht-Output am Ende

1. **Mandatsbogen** mit Beteiligten, Konflikt-Check, GwG-Status, Streitwert.
2. **Frist-Liste** (Sofortfristen, Verjährung, Ausschlussfristen, Beweisanforderungs-Fristen).
3. **Anlagenverzeichnis** des uebergebenen Datenraums (Stand erstes Sortieren).
4. **Naechster-Schritt-Plan:** binnen 24/48/72 h, Owner, Output.
5. **Honorarvereinbarung** unterschrieben oder Vorbehalt notiert.

## Relevante Rechtsgrundlagen und Standards

- BORA, BRAO, FAO für Fachanwaltschaft Allgemeines Verwaltungs- und Bauplanungsrecht.
- GwG, GwGMeldV, Identifizierungsleitfaden BRAK.
- VwVfG, VwGO, BauGB, BauNVO, GewO, BBG/BeamtStG (für fachliche Erstpruefung).
- DSGVO und BDSG für den Umgang mit Mandantendaten (Art. 6 DSGVO als Rechtsgrundlage, Art. 9 ggf. Gesundheitsdaten).

## Typische Fehler im Erstgespraech

- Frist uebersehen, weil Mandantin sie nicht selber genannt hat (immer aus jedem Schreiben Frist herausziehen).
- Konflikt-Check nur nach Personennamen, nicht nach Sachzusammenhang (gleiche Liegenschaft, gleicher Sachverhalt).
- Vollmachtsumfang unklar -> spaeter Streit mit Mandantin ueber Befugnisse.
- Honorarvereinbarung muendlich -> Beweisnot bei Streitwert-/Honorar-Streit.
- GwG: kein Lichtbildausweis erfasst, kein Aktenvermerk ueber Risikobewertung.

## Praxis-Checkliste

- [ ] Personalien und Rolle aller Beteiligten erfasst
- [ ] Konflikt-Check durchgefuehrt
- [ ] GwG: Identifizierung + Risikobewertung notiert
- [ ] Allgemeine Vollmacht unterschrieben
- [ ] Speziale Vollmacht / Entbindungserklaerung (wo noetig) unterschrieben
- [ ] Streitwert geschaetzt
- [ ] Honorarvereinbarung unterschrieben oder ausdruecklich auf RVG verwiesen
- [ ] Fristenliste angelegt und in Kalender eingetragen
- [ ] Mandatsbogen vollstaendig
- [ ] Naechster-Schritt-Plan dem Mandanten kommuniziert (E-Mail-Zusammenfassung)

## Konkrete Praxis-Konstellationen

### Konstellation A: Eilbeduerftigkeit

Mandantin kommt am Donnerstag, Frist laeuft am Montag (Klage- oder Widerspruchsfrist im Bereich Allgemeines Verwaltungs- und Bauplanungsrecht). Handlungs-Sequenz:

1. Sofort-Vollmacht und Sofort-Akteneinsicht (per beA, ELSTER, Behördenportal).
2. Antrag auf Wiedereinsetzung (§ 233 ZPO, § 60 VwGO, § 110 AO) als Reserve dokumentieren.
3. Spaeteste-Stunde-Versand-Plan: beA bevorzugt, mit qualifizierter Signatur und Empfangsbekenntnis.
4. Honorarvereinbarung NICHT auf Eilzuschlag verzichten - aber transparent kommunizieren.

### Konstellation B: Komplexer Sachverhalt, Datenraum unsortiert

Mandant uebergibt 200+ Dateien (PDF-Scans, E-Mails, Excel-Listen). Vor jeder fachlichen Bewertung:

1. Datenraum-Index in Excel: Datum, Absender, Empfaenger, Aktenzeichen, kurze Inhaltszeile.
2. Chronologischer Verlauf als Zeitstrahl - Spielraum für Verjährungs- und Ausschlussfristen identifizieren.
3. Loecher im Datenraum gezielt anfordern (Mandantenfragen-Katalog).

### Konstellation C: Interessenkonflikt-Naehe

Frueheres Mandat mit derselben Gegnerin oder gleichem Sachzusammenhang. Pruefung:

1. § 43a Abs. 4 BRAO und § 3 BORA - Sachzusammenhang, nicht nur Personenidentitaet.
2. Einwilligung beider Mandanten in Textform (mit konkreter Beschreibung).
3. Bei Zweifel: Mandat ablehnen und an Kanzleikollegium ueberweisen.

## Mandanten-Erwartungsmanagement

- Realistische Erfolgs- und Kostenprognose (nicht "Wir gewinnen sicher").
- Verfahrensdauer im Bereich Allgemeines Verwaltungs- und Bauplanungsrecht: Erfahrungswerte nach Instanz.
- Vergleichschance vs. streitiges Urteil als Option offen halten.
- Schriftliche Zusammenfassung des Erstgespraechs binnen 48 h.

## Honorarvereinbarung - Best Practices

- RVG-Basis als Default, Stundenhonorar nur mit gesondertem Hinweis nach § 3a RVG.
- Erfolgshonorar nur in den engen Grenzen § 4a RVG.
- Vorschuss in Hoehe der voraussichtlichen 1. Instanz.
- Klarstellung: Auslagen-Pauschale, USt, Reisekosten, Sachverstaendigenkosten gesondert.
- Bei PKH/Beratungshilfe-Mandant: schriftliche Belehrung, dass eigene Beitraege moeglich sind.

## Mandatsbogen-Muster (Mindestinhalt)

- Mandant (Name, Geburtsdatum, Anschrift, Telefon, E-Mail)
- Gegner (Name, Anschrift, ggf. anwaltliche Vertretung)
- Kurzbeschreibung Sachverhalt (5-10 Saetze)
- Ziel des Mandats (eine Zeile)
- Strittige Fragen (bullet)
- Geprueft: Konflikt - GwG - Vollmacht
- Streitwert (Schaetzung)
- Honorarvereinbarung (RVG/Stunde/Pauschale)
- Frist-Liste
- Aktenanlage Datum
- Naechster-Schritt

## Leitentscheidungen Mandatsannahme / Erstkontakt

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Cross-Refs

- `vergleichsverhandlung-strategie` (im selben Plugin) für den Fall, dass aussergerichtliche Loesung angestrebt wird.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Schriftsatzaufbau, wenn Klage/Widerspruch eingereicht wird.
- Kanzlei-Allgemein-Plugin `kanzlei-allgemein` für Konflikt-, GwG- und PEP-Pruefroutinen.

---

## Skill: `erstpruefung-und-mandatsziel`

_Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel._

# Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 28 Abs. 1 VwVfG` — Anhörung vor belastender Verwaltungsentscheidung.
- `§ 37 Abs. 1 VwVfG` — Bestimmtheit des Verwaltungsakts.
- `§ 39 Abs. 1 VwVfG` — Begruendungspflicht.
- `§ 40 VwVfG` — Ermessensausübung und Ermessensfehler.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist, soweit Widerspruchsverfahren vorgesehen.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz gegen Vollziehung.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel.

## Spezialwissen: Fachanwalt: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** VwGO, VwVfG.

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

---

## Skill: `drittanfechtung-umwelt`

_Drittanfechtung umweltrechtlicher Genehmigungen (BImSchG, BauGB) durch Nachbarn oder Umweltverband: Klagebefugnis und materielle Gründe prüfen: Drittanfechtung umweltrechtlicher Genehmigungen (BImSchG, BauGB) durch Nachbarn oder Umweltverband: Klagebefugnis..._

# Drittanfechtung umweltrechtlicher Genehmigungen (BImSchG, BauGB) durch Nachbarn oder Umweltverband: Klagebefugnis und materielle Gründe prüfen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Drittanfechtung umweltrechtlicher Genehmigungen (BImSchG, BauGB) durch Nachbarn oder Umweltverband: Klagebefugnis und materielle Gründe prüfen. Normen: § 42 Abs. 2 VwGO (Schutznorm-Theorie), § 5 BImSchG (Nachbarschutz), UmwRG (Verbandsklage), UVP-Pflicht. Prüfraster: Klagebefugnis Dritter, drittschützende Normen, UVP-Fehler, Verbandsklage. Output Klageschrift-Entwurf, Klagebefugungs-Gutachten. Abgrenzung: BImSchG-Genehmigung Betreiber siehe energieanlagen-bimschg-genehmigung-verfahren; Bauleitplanung Normenkontrolle siehe fachanwalt-verwaltungsrecht-normenkontrolle-47-vwgo.

### Drittanfechtung Umwelt-Genehmigung

## 1) Klagebefugnis § 42 II VwGO

### Schutznorm-Theorie

- Norm muss auch Dritten schuetzen
- BImSchG § 5 schuetzt Nachbarn
- Bei reinen Allgemeinwohl-Normen: keine Klagebefugnis

### Bei Verbänden

- Umwelt-Verbands-Klage UmwRG
- Anerkennung BfN

### Praxis-Konstellationen

- Tierhaltungs-Anlage
- Windkraft-Anlage
- Straßen-/Schienen-Planfeststellung
- Industriebetrieb

## 2) Prüfungs-Punkte

### Materiell

- Genehmigungs-Voraussetzungen § 6 BImSchG
- Immissions-Schutz § 5 BImSchG
- UVP-Pflicht
- Naturschutz

### Verfahrens

- Beteiligungs-Verfahren
- Anhörung
- Sachverständigen-Prüfung

### Verfahrensvorschriften

- Vorabbescheid-Aufhebung
- Wesentliche Änderung
- Teil-Genehmigung

## 3) Verfahrens-Vorschriften

### Förmliches Verfahren § 10 BImSchG

- Bekanntmachung
- Auslegung 1 Monat
- Erörterungs-Termin
- Bescheid mit Begründung

### Vereinfachtes Verfahren § 19 BImSchG

- Bei kleineren Anlagen
- Keine Bürgerbeteiligung
- Schneller

## 4) UVP-Prüfung

### Pflicht / Vor-Prüfung

- UVPG Anlage 1
- Schwellenwerte
- Allgemeine UVP / Standortbezogene UVP / Vor-UVP

### Bei Versäumnis

- Genehmigung anfechtbar
- Auflagen-Defizit

## 5) Workflow

### Phase 1 — Bescheid-Prüfung

- Vollständigkeit
- Auflagen
- Begründung

### Phase 2 — Klage-Strategie

- Widerspruchs-Verfahren (Landes-AusfG)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Eilantrag § 80 V VwGO bei Sofortvollzug

### Phase 3 — Beweisaufnahme

- Sachverständigen-Gutachten
- Eigenstudien (Geruch, Larm, Bioaerosole)
- Vergleichs-Anlagen

### Phase 4 — Urteil

- Aufhebung Genehmigung
- Auflagen-Änderung
- Klage abgewiesen

## 6) Aufschiebende Wirkung

### Sofortvollzug § 80 II VwGO

- Bei wirtschaftlicher Bedeutung typisch
- Eilantrag § 80 V VwGO

### Erfolgsaussichten Eil

- Wahrscheinlichkeit Hauptsache-Erfolg
- Eigene Schädigung vs. AG-Interesse

## 7) Verbands-Klage UmwRG

### Voraussetzungen

- BfN-anerkannt
- Klage-Frist 1 Monat
- Beteiligungs-Verfahren genutzt

### Reichweite

- Nicht nur eigene Rechte
- Auch Umweltbelange
- Klimaschutz im aktuellen Fokus

## 8) Typische Fehler

1. **Klagebefugnis nicht ausreichend dargetan**
2. **Eilantrag versäumt** — Anlage geht in Betrieb
3. **Sachverständiger zu spaet**
4. **UVP-Pflicht übersehen**

## 9) BVerwG-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## 10) Honorar

- Streitwert nach wirtschaftlichem Interesse
- Bei Vereinen oft NGO-Finanzierung
- VKH-Antrag möglich

## Aktuelle BVerwG-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `testakten/umweltrecht-industrieanlage-genehmigung` — bei vertiefter Verteidigung
- `fachanwalt-agrarrecht-tierhaltung-genehmigung` — bei Stallneubau-Bezug
- `fachanwalt-verwaltungsrecht-orientierung` — Triage

---

## Skill: `energieanlagen-bimschg-genehmigung-verfahren`

_BImSchG-Genehmigung für Energieanlagen (Wind, Biogas, Biomasse, Wasserstoff-Elektrolyseur) begleiten: Vorhabentraeger beantragt Genehmigung oder Drittbetroffener klagt dagegen: BImSchG-Genehmigung für Energieanlagen (Wind, Biogas, Biomasse, Wasserstoff-Elek..._

# BImSchG-Genehmigung für Energieanlagen (Wind, Biogas, Biomasse, Wasserstoff-Elektrolyseur) begleiten: Vorhabentraeger beantragt Genehmigung oder Drittbetroffener klagt dagegen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** BImSchG-Genehmigung für Energieanlagen (Wind, Biogas, Biomasse, Wasserstoff-Elektrolyseur) begleiten: Vorhabentraeger beantragt Genehmigung oder Drittbetroffener klagt dagegen. Normen: §§ 4 und 10 und 19 BImSchG (foermliches/vereinfachtes Verfahren), 4. BImSchV, TA Laerm, UmwRG (Verbandsklage). Prüfraster: Antragsunterlagen (Schallgutachten, Schattenwurf, saP), Drittanfechtung, UVP-Pflicht EuGH-Linie, Eilantrag § 80 Abs. 5 VwGO. Output Antragsunterlagen-Prüfung, Klageschrift-Entwurf oder Widerspruch. Abgrenzung: Planfeststellung Energietrassen siehe energietrassen-planfeststellung-rechtsschutz; Vergabe siehe fachanwalt-vergaberecht-Plugin.

### Energieanlagen-BImSchG-Genehmigung-Verfahren

## Kernsachverhalt

Energieanlagen (Wind, Biogas, Wasserstoff, größere Solarthermie, KWK, Geothermie) bedürfen in der Regel einer BImSchG-Genehmigung nach §§ 4 ff. BImSchG, wenn sie eine bestimmte Schwelle nach der 4. BImSchV überschreiten. Das Skill bedient die Mandanten-Vertretung im förmlichen oder vereinfachten Verfahren — sowohl auf Vorhabenträger- als auch auf Nachbar-/Verbandsseite.

## Kaltstart-Rückfragen

1. Welcher Anlagen-Typ und welche installierte Leistung — Windkraftanlage, Biogas, KWK, Elektrolyseur, Geothermie, Freiflächen-PV?
2. Wo befindet sich der Standort, welche Behörde ist zuständig — untere Immissionsschutzbehörde, Regierungspräsidium, Bergamt?
3. Welcher Verfahrensstand — Voranfrage, laufender Antrag, Bescheid, Klage, Eilantrag?
4. In welcher Rolle ist der Mandant — Vorhabenträger, Drittbetroffener (Nachbar, Grundeigentümer), anerkannter Umweltverband?
5. Liegt UVP-Pflicht oder UVP-Vorprüfungspflicht nach UVPG vor?
6. Welche Gutachten existieren bereits — Schallgutachten, saP, Schattenwurf, UVP-Bericht?
7. Wurde Sofortvollzug angeordnet — Eilantrag nach § 80 Abs. 5 VwGO erforderlich?
8. Sind Verbandseinwendungen oder eine UmwRG-Klage bereits eingeleitet?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Auszüge)

**§ 4 Abs. 1 BImSchG** — Genehmigungsbedürftige Anlagen dürfen nur errichtet und betrieben werden, wenn eine Genehmigung nach § 6 BImSchG erteilt worden ist.

**§ 5 Abs. 1 BImSchG** — Genehmigungsbedürftige Anlagen sind so zu errichten und zu betreiben, dass zur Gewährleistung eines hohen Schutzniveaus für die Umwelt insgesamt schädliche Umwelteinwirkungen und sonstige Gefahren, erhebliche Nachteile und erhebliche Belästigungen für die Allgemeinheit und die Nachbarschaft nicht hervorgerufen werden können (drittschützende Grundpflicht).

**§ 6 Abs. 1 BImSchG** — Die Genehmigung ist zu erteilen, wenn sichergestellt ist, dass die Grundpflichten des § 5 erfüllt werden und andere öffentlich-rechtliche Vorschriften und Belange des Arbeitsschutzes der Errichtung und dem Betrieb nicht entgegenstehen.

**§ 10 BImSchG** — Förmliches Genehmigungsverfahren mit Bekanntmachung, Auslegung, Erörterungstermin, Öffentlichkeitsbeteiligung bei Anlagen der Spalte 1 der 4. BImSchV.

**§ 19 BImSchG** — Vereinfachtes Verfahren ohne Öffentlichkeitsbeteiligung bei Anlagen der Spalte 2 der 4. BImSchV; Genehmigung durch Behörde von Amts wegen.

**§ 44 BNatSchG** — Schädigungs- und Störungsverbote für besonders und streng geschützte Arten; Fang, Tötung, Störung, Zerstörung von Fortpflanzungs- und Ruhestätten verboten (artenschutzrechtliche Verbote, Prüfpflicht in saP).

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema BImSchG-Genehmigungsverfahren

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Anlagen-Klassifizierung 4. BImSchV | Nr. 1.6 WEA, Nr. 1.4 Biogas, Nr. 8 Feuerungsanlage; Spalte 1 (förmlich) oder Spalte 2 (vereinfacht)? | Verfahrensart bestimmt |
| 2 | UVP-Pflicht UVPG | Anhang 1 UVPG: ab 20 WEA UVP-Pflicht; 6–19 allgemeine Vorprüfung; 3–5 standortbezogene Vorprüfung | UVP-Umfang festgelegt |
| 3 | Antragsunterlagen vollständig | Formular, Beschreibung, Schallgutachten, Schattenwurf, saP, Lageplan, UVP-Bericht | Vollständigkeitsprüfung durch Behörde |
| 4 | Schallgutachten TA Lärm | Beurteilungspegel je Immissionsort; Tag-/Nachtwerte; Vorbelastung; WR 55/40 dB(A), MI 60/45 dB(A) | Einhaltung Immissionsrichtwerte |
| 5 | Schattenwurf-Prognose | Max. 30 h/Jahr astronomisch, max. 8 h/Jahr meteorologisch (LAI-Hinweise); Abschaltautomatik als Auflage | Auflageninhalt Nebenbestimmung |
| 6 | saP § 44 BNatSchG | Erfassungszeitraum, Methoden, Arten (Rotmilan, Fledermäuse, Mauersegler); Vermeidungs- und CEF-Maßnahmen | Verbotstatbestand ausgeschlossen? |
| 7 | Öffentlichkeitsbeteiligung § 10 BImSchG | Bekanntmachung, Auslegung 1 Monat, Einwendungen 1 Monat, Erörterungstermin | Verfahrensfehler rügen |
| 8 | Genehmigungstatbestand § 6 BImSchG | Grundpflichten § 5; entgegenstehende öffentlich-rechtliche Vorschriften; Bauleitplan | Tatbestand erfüllt? |
| 9 | Nebenbestimmungen Auflagen | Lärm-Nachtabschaltung, Schattenwurf-Modul, Artenschutz-Bauzeit-Fenster, Rückbau-Bürgschaft | Verhältnismäßigkeit der Auflagen |
| 10 | Sofortvollzug § 80 Abs. 2 Nr. 4 VwGO | Klimaschutz-Argument; Begründungserfordernis § 80 Abs. 3 VwGO | Eilantrag prüfen |
| 11 | Klage-Befugnis Drittbetroffener § 42 Abs. 2 VwGO | Möglichkeitstheorie; Verletzung subjektiver Rechte aus § 5 BImSchG (drittschützend) | Klagebefugnis bejahen/verneinen |
| 12 | Klagefrist § 74 VwGO | 1 Monat ab Bekanntgabe; bei UVP-pflichtigen Vorhaben analog; Verband UmwRG | Frist dokumentieren |
| 13 | UmwRG Verbandsklage | § 2 UmwRG; Vorab-Mitwirkung Pflichtvoraussetzung; UVP-Defizite, saP-Fehler | Prozessuale Stellung |
| 14 | Ausschluss-Fristen Einwendungen | § 10 Abs. 3 BImSchG Einwendungsfrist; Präklusion bei späterer Klage | Einwendungen rechtzeitig |
| 15 | Eilantrag § 80 Abs. 5 VwGO | Interessenabwägung; formelle Mängel Vollziehungsanordnung § 80 Abs. 3; Hauptsacheerfolgsaussicht | Antrag stellen bei sofortigem Vollzug |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Einhaltung Schallimmissionsrichtwerte | Vorhabenträger (im Verfahren), Behörde (im Klageverfahren) | Schallgutachten, Gegengutachten, Messung |
| saP methodische Ordnungsgemäßheit | Vorhabenträger | Erfassungsberichte, Gutachten, Kartierdaten |
| Erhebliche Schattenwurf-Beeinträchtigung | Drittbetroffener (im Eilverfahren) | Schattenwurf-Simulation, eigene Ermittlung |
| UVP-Fehler | Verband / Drittbetroffener | UVP-Bericht, Verfahrensunterlagen |
| Klagebefugnis Drittbetroffener | Antragsteller | Entfernung, Grundstücksplan, Schallprognose |
| Verhältnismäßigkeit Auflagen | Vorhabenträger bei Anfechtung | Alternativnachweis, Sachverständigengutachten |

## Fristen und Verjährung

| Frist | Grundlage | Lauf | Hinweis |
|---|---|---|---|
| Einwendungsfrist Auslegung | § 10 Abs. 3 BImSchG | 1 Monat nach Auslegungsende | Präklusion bei späterer Klage wenn kein Einwand erhoben |
| Klagefrist | § 74 VwGO | 1 Monat ab Bekanntgabe | Gilt auch bei UmwRG-Verbandsklagen |
| Beschwerde Eilentscheidung | § 146 Abs. 4 VwGO | 2 Wochen ab Beschluss, Begründung 1 Monat | OVG als Beschwerdegericht |
| Genehmigungsfiktion § 42a VwVfG | § 16 Abs. 1 BImSchG | Bei förmlichem Verfahren keine Fiktion; nur bei vereinfachtem Verfahren | Auf Fristeinhaltung achten |
| Gültigkeitsfrist Genehmigung | — | Genehmigung unbefristet; Nebenbestimmungen befristet | Auflagenfristen im Blick behalten |
| Verjährung Nachbar-Ansprüche | § 195 BGB | 3 Jahre ab Kenntnis | Privatrechtliche Ausgleichsansprüche |

## Typische Gegenargumente

| Gegenargument | Gegenstrategie |
|---|---|
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "TA-Lärm-Werte eingehalten" | Vorbelastungs-Korrektur prüfen: wurden alle vorhandenen Windkraftanlagen in der Umgebung als Vorbelastung berücksichtigt? Kumulationseffekte? |
| "Klimaschutz rechtfertigt sofortige Vollziehung" | § 80 Abs. 3 VwGO: Begründung muss auf Einzelfall eingehen; abstrakter Klimaschutzverweis reicht nicht (OVG-Ständige Rspr.) |
| "Einwendungen präkludiert" | Präklusion greift nicht gegenüber UmwRG-Verbänden bei UVP-pflichtigen Vorhaben; UVP-Defizite jederzeit rügefähig |
| "Drittbetroffener nicht klagebefugt" | § 5 Abs. 1 Nr. 1 BImSchG ist drittschützend; Nachbar im Einwirkungsbereich hat subjektives Recht; Möglichkeitstheorie großzügig |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Einwendungen nicht substantiiert" | Im BImSchG-Verfahren genügt allgemeine Darlegung der Betroffenheit; detaillierte Rüge erst in Klage erforderlich |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — BImSchG-Genehmigungsverfahren begleiten | Verfahrensbegleitung nach Pruefschema; Schriftsatz unten |
| Variante A — Genehmigung für Drittbetroffene anfechten | Anfechtungsklage VwGO statt Verfahrensbegleitung |
| Variante B — Foermliches Genehmigungsverfahren nicht noetig | Anzeigeverfahren § 15 BImSchG als Alternative pruefen |
| Variante C — Behörde zoegert Untaetigkeit moegliche Alternative | Untaetigkeitsklage § 75 VwGO vorbereiten bei Verzoegerung |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Klagebegründung Drittbetroffener (Schallschutz)

```
Verwaltungsgericht [Ort]
Klagebegründung

In der Verwaltungsrechtssache
[Kläger]
gegen
[Beklagte: Immissionsschutzbehörde]
beigeladen: [Vorhabenträger]

Az. VG [Az]

I. Sachverhalt

Der Kläger ist Eigentümer des Grundstücks [Anschrift], das sich in
einer Entfernung von ca. [x] Metern zur nächsten geplanten
Windkraftanlage befindet. Das Grundstück liegt im
[Wohn-/Mischgebiet].

Die Beklagte erteilte mit Bescheid vom [Datum] eine BImSchG-
Genehmigung für [n] Windkraftanlagen des Typs [Typ] am
Standort [Standort].

II. Zulässigkeit

Die Anfechtungsklage ist zulässig. Der Kläger ist nach §§ 42 Abs. 2,
113 Abs. 1 VwGO klagebefugt, da die Verletzung des drittschützenden
§ 5 Abs. 1 Nr. 1 BImSchG möglich erscheint. Die Klagefrist von einem
Monat (§ 74 VwGO) ist gewahrt.

III. Begründetheit — Verletzung § 5 Abs. 1 Nr. 1 BImSchG

1. Methodische Fehler im Schallgutachten

Das dem Bescheid zugrundeliegende Schallgutachten des Büros [Name]
vom [Datum] weist folgende methodische Mängel auf:

a) Unterschätzung der Vorbelastung — das Gutachten berücksichtigt
 die bestehenden Windkraftanlagen [Bezeichnung] in der Umgebung
 nicht als Vorbelastung. Nach TA Lärm Nr. 2.4 ist die
 Vorbelastung am Immissionsort zu berücksichtigen. Ohne
 Korrektur dieser Lücke kann die Einhaltung des Immissions-
 richtwerts von [40/45] dB(A) nachts nicht festgestellt werden.

b) Unzureichende Messung Schallleistungspegel — der verwendete
 Schallleistungspegel des Anlagentyps basiert auf Messungen
 unter optimalen Bedingungen. Ein Zuschlag für Amplituden-
 modulation nach TA Lärm Nr. A.2.3.3 wurde nicht berücksichtigt.

2. Beweissicherungsantrag

Der Kläger beantragt die Einholung eines gerichtlichen
Sachverständigengutachtens zur Frage, ob die Schallimmissions-
richtwerte der TA Lärm am Grundstück des Klägers eingehalten
werden.

Anlagen: Privates Gegengutachten [Anlage K1], Lagepläne [K2]
```

### Baustein 2: Einwendung im BImSchG-Verfahren (Naturschutz)

```
An die [Immissionsschutzbehörde]
Verfahren: BImSchG-Genehmigung [Vorhaben]

Einwendungen nach § 10 Abs. 3 BImSchG

Einwender: [Name, Adresse]

Sehr geehrte Damen und Herren,

gegen das geplante Vorhaben erheben wir namens und in Vollmacht
des Einwenders folgende Einwendungen:

1. Artenschutzrechtliche Defizite der saP

Die ausgelegte saP des Büros [Name] vom [Datum] genügt den
methodischen Anforderungen nicht:

a) Unzureichender Erfassungszeitraum für Fledermäuse — die
 Transekt-Kartierung umfasste lediglich [n] Termine im
 Zeitraum [Monat – Monat]. Für eine ordnungsgemäße saP sind
 nach den LLUR-/LfU-Hinweisen der Länder mindestens [n]
 Detektorerhebungen über die gesamte Aktivitätssaison
 (April bis Oktober) erforderlich.

b) Rotmilan — im Radius von 1.500 m um den Standort wurden
 während des Erfassungszeitraums [n] Rotmilan-Individuen
 kartiert. Das Gutachten kommt zu dem Ergebnis, es bestehe
 kein signifikant erhöhtes Tötungsrisiko gem. § 44 Abs. 1
 Nr. 1 BNatSchG. Diese Bewertung ist angreifbar, da die
 Kartierung nicht in den Hauptaktivitätsstunden
 (08:00–12:00 Uhr) an mindestens 12 Termine erfolgte.

c) Fehlende CEF-Maßnahmen — für den nachgewiesenen Bestand
 der [Art] wurden keine vorgezogenen Ausgleichsmaßnahmen
 (CEF) benannt.

2. Schattenwurf

Die Schattenwurf-Simulation zeigt für das Grundstück des Einwenders
([Adresse]) eine theoretische Beschattungsdauer von [x] Stunden/Jahr.
Die angeordneten Auflagen genügen nicht, da eine Abschaltautomatik
fehlt.

Wir beantragen daher die Versagung der Genehmigung,
hilfsweise die Aufnahme konkreter Nebenbestimmungen.
```

### Baustein 3: Antrag auf Akteneinsicht und Vorbereitung Eilantrag

```
An die [Immissionsschutzbehörde]

Antrag auf Akteneinsicht § 29 VwVfG

Sehr geehrte Damen und Herren,

wir zeigen an, namens und in Vollmacht [des Mandanten]
tätig zu sein. Wir beantragen Einsicht in die gesamte
Genehmigungsakte des Verfahrens [Az.], einschließlich:

- aller eingereichten Gutachten und Stellungnahmen
- der Behördenkorrespondenz
- der Nebenbestimmungen und Prüfvermerke
- des UVP-Berichts und der Behördenentscheidung zur UVP-Pflicht

Sobald die Sofortvollziehung angeordnet wird, werden wir beim
Verwaltungsgericht [Ort] Eilantrag nach § 80 Abs. 5 VwGO stellen.
Die Akteneinsicht ist für die Begründung unabdingbar.

Wir bitten um Mitteilung des frühesten Termins für die Einsicht.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| Streitwert Drittbetroffener | § 52 Abs. 1 GKG; Orientierungswert nach Streitwertkatalog Verwaltungsgerichtsbarkeit: Nachbar-WEA typisch EUR 15.000–30.000 je nach Anlage | Konjunktur der Rspr. beachten; bei mehreren Klagepunkten Addierung |
| Streitwert Vorhabenträger (Genehmigungsklage) | Investitionsvolumen / Ertragserwartung; typisch EUR 50.000–200.000 | § 52 Abs. 1 GKG Abschätzung nach wirtschaftlichem Interesse |
| Gerichtskosten | GKG Anlage 1 Nr. 1210; bei EUR 20.000 Streitwert ca. EUR 1.888 | Bei VG-Verfahren drei Instanzen einkalkulieren |
| Sachverständigenkosten saP | EUR 5.000–20.000 je nach Artenspektrum und Erfassungsaufwand | Ggf. gerichtliches Gutachten auf Kosten der Gegenseite bei Obsiegen |
| Eilverfahren Streitwert | Halb des Hauptsache-Streitwerts | § 80 Abs. 5 VwGO-Beschluss = Bruchteil |

## Strategische Empfehlung

| Mandantenrolle | Situation | Empfehlung |
|---|---|---|
| Vorhabenträger | Antragsunterlagen unvollständig | Proaktive Abstimmung mit Behörde vor Einreichung; Gutachter-Auswahl nach behördlicher Praxis |
| Vorhabenträger | Klage Drittbetroffener | Sachverständige beiziehen; § 80 Abs. 3-Begründung präzise ausarbeiten; frühe Verhandlung anbieten |
| Drittbetroffener | Bescheid ergangen | Eigenes Schallgutachten in Auftrag geben; Einwendungs-Präklusion prüfen; Klagefrist sichern |
| Drittbetroffener | Sofortvollzug angeordnet | Eilantrag § 80 Abs. 5 VwGO; § 80 Abs. 3-Begründungsmangel angreifen; Hauptsache parallel einreichen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Anschluss-Skills

- `energietrassen-planfeststellung-rechtsschutz` — Planfeststellungsverfahren für Leitungen und Netzinfrastruktur
- `eilantrag-80-abs-5-vwgo` — Vertiefung Eilantragsstrategie und Schriftsatz
- `fachanwalt-verwaltungsrecht-einstweiliger-rechtsschutz` — Grundlagen einstweiliger Rechtsschutz
- `fachanwalt-verwaltungsrecht-widerspruchsschrift` — Widerspruch gegen Genehmigungsbescheid

## Aktuelle Leitentscheidungen (v14.2 Ergaenzung)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- BImSchG §§ 4, 5, 6, 10, 19
- 4. BImSchV Anhang 1 (Nrn. 1.4, 1.6, 8)
- TA Lärm (6. Allg. VwV BImSchG)
- TA Luft 2021
- UVPG Anhang 1
- BNatSchG §§ 13, 44
- VwGO §§ 42, 74, 80, 113
- UmwRG § 2
- EU-RED III (Beschleunigungsgebiete)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

<!-- AUDIT 27.05.2026 — Bundle 027 Halluzinations-Reparatur
-->

---

## Skill: `energietrassen-planfeststellung-rechtsschutz`

_Rechtsschutz gegen Planfeststellungsbeschluss für Strom- und Gastrassen klagen: Anlieger oder Umweltverband klagt gegen Netzausbau: Rechtsschutz gegen Planfeststellungsbeschluss für Strom- und Gastrassen klagen: Anlieger oder Umweltverband klagt gegen Netza..._

# Rechtsschutz gegen Planfeststellungsbeschluss für Strom- und Gastrassen klagen: Anlieger oder Umweltverband klagt gegen Netzausbau


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Rechtsschutz gegen Planfeststellungsbeschluss für Strom- und Gastrassen klagen: Anlieger oder Umweltverband klagt gegen Netzausbau. Normen: § 43 EnWG, BBPlG, NABEG, EnLAG, LNG-Beschleunigungsgesetz; BVerwG als Erstinstanz. Prüfraster: Klagebefugnis, verkuerzte Klagefrist 1 Monat, UmwRG-Verbandsklage, Aarhus-Konvention, Erdkabel-Vorrang. Output Klageschrift-Entwurf, Klagebefugungs-Memo. Abgrenzung: BImSchG-Anlagen siehe energieanlagen-bimschg-genehmigung-verfahren; Planfeststellung allgemein VwVfG siehe schriftsatzkern-substantiierung.

### Energietrassen — Planfeststellung und Rechtsschutz

## Kernsachverhalt

Bei Stromtrassen, Erdgas-Pipelines, LNG-Terminals, Wasserstoff-Stammnetz und Offshore-Anbindungsleitungen gibt es verkürzte, beschleunigte Verfahren mit eingeschränktem Rechtsschutz. Die Klagefrist beträgt regelmäßig nur einen Monat. Mandanten auf Drittbetroffenen- und Verbandsseite haben dennoch erhebliche prozessuale Möglichkeiten, insbesondere über UVP-Fehler, Alternativenprüfung, Artenschutz und Entschädigungsansprüche.

## Kaltstart-Rückfragen

1. Welches Vorhabens-Typ — Stromtrasse (380 kV, HGÜ), Erdgas-Pipeline, LNG-Terminal, H2-Stammnetz, Offshore-Anbindungsleitung?
2. Welches Genehmigungsregime — NABEG, EnLAG, BBPlG, WindSeeG, LNG-Beschleunigungsgesetz?
3. Mandantenrolle — Grundeigentümer/Anlieger, anerkannter Umweltverband, Gemeinde?
4. Verfahrensstand — Bundesfachplanung, laufende Planfeststellung, Beschluss ergangen, Klagefrist läuft?
5. Wurde sofortige Vollziehung des Planfeststellungsbeschlusses angeordnet — Eilantrag nach § 80 Abs. 5 VwGO erforderlich?
6. Liegt Enteignung oder Entschädigungsanspruch des Grundeigentümers vor?
7. Hat der Verband im Planfeststellungsverfahren ordnungsgemäß mitgewirkt (Pflichtvoraussetzung UmwRG)?
8. Welche konkreten Fehler bestehen — Alternativenprüfung, UVP-Defizit, Artenschutz-saP, Lärmschutz, Erdkabel-Abwägung?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

### Normtexte (Auszüge)

**§ 18 NABEG (Planfeststellungsbeschluss)** — Die zuständige Behörde stellt den Plan auf Antrag des Vorhabenträgers durch Planfeststellungsbeschluss fest. Der Beschluss ist für alle öffentlich-rechtlichen Beziehungen verbindlich.

**§ 1 EnLAG** — Zur Beschleunigung des Ausbaus der Höchstspannungsnetze sind die im Bedarfsplan zu EnLAG aufgeführten Vorhaben vordringlich zu realisieren. Klagefrist 1 Monat, erste Instanz BVerwG.

**§ 50 Abs. 1 Nr. 6 VwGO** — Das Bundesverwaltungsgericht entscheidet im ersten und letzten Rechtszug über Streitigkeiten aus den in NABEG und EnLAG genannten Vorhaben.

**§ 4 Abs. 1 EnLAG (Erdkabel-Vorrang)** — Auf Verlangen des Vorhabenträgers oder auf Antrag der betroffenen Gemeinde oder Einwohner ist bei bestimmten Leitungsabschnitten Erdkabel zu prüfen und bevorzugt einzusetzen.

**§ 2 UmwRG** — Anerkannte Umweltverbände können Klage gegen Entscheidungen erheben, die dem Anwendungsbereich des UmwRG unterliegen, ohne Verletzung eigener Rechte geltend machen zu müssen (altruistische Verbandsklage).

**Art. 9 Aarhus-Konvention** — Zugang zu Gerichten in Umweltangelegenheiten muss effektiv sein; Kostenbarrieren dürfen Klagerecht nicht aushöhlen.

### Leitentscheidungen

| Gericht | Aktenzeichen | Datum | Leitsatz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema Planfeststellungs-Rechtsschutz

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Vorhabens-Regime bestimmen | NABEG / EnLAG / BBPlG / WindSeeG / LNG-G → Klagegericht und Klagefrist | BVerwG erste Instanz oder VG? |
| 2 | Klagefrist 1 Monat | Ab Zustellung des Planfeststellungsbeschlusses; keine Wiedereinsetzung außer bei unverschuldetem Fristversäumnis | Frist dokumentieren |
| 3 | Klagebefugnis Anlieger | Art. 14 GG Eigentumsgarantie; Enteignungs-Duldungspflicht; eigene Rechtsbetroffenheit aus Immissionsschutz | § 42 Abs. 2 VwGO analog |
| 4 | Klagebefugnis Verband | § 2 UmwRG; Beteiligung im Planfeststellungsverfahren erfolgt; keine Verletzung eigener Rechte nötig | Beteiligung dokumentieren |
| 5 | Sofortvollzug / Eilantrag | Anordnung sofortiger Vollziehung? Begründung § 80 Abs. 3 VwGO? | Eilantrag § 80 Abs. 5 VwGO |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 8 | saP / Artenschutz | Artenschutzrechtliche Prüfung nach § 44 BNatSchG; Erfassungsmethodik; Vermeidungsmaßnahmen | Methodenfehler geltend machen |
| 9 | Lärmschutz / TA Lärm | Bei Konverteranlagen, Umspannwerken; TA Lärm-Richtwerte; Schallgutachten korrekt? | Gegengutachten einsetzen |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 12 | Entschädigungsanspruch | Enteignungs-Entschädigung nach § 18 EnWG; Wertgutachten Grundstück vor und nach | Eigene Verhandlungsführung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| 14 | Aarhus-Kostenbarriere | Gerichtskosten dürfen effektiven Zugang nicht aushöhlen; Art. 9 Aarhus; EU-Recht | Kostenantrag bei Verband |
| 15 | Beschwerde bei Eilabweisung | § 146 VwGO 2 Wochen; OVG/BVerwG; neue Tatsachen zulässig | Beschwerdebegründung 1 Monat |

## Beweislast

| Beweisthema | Beweislastträger | Beweismittel |
|---|---|---|
| Vollständigkeit UVP-Bericht | Kläger (Rüge) / Behörde (Verteidigung) | UVP-Bericht, Planfeststellungsunterlagen |
| Methodische Fehler saP | Kläger | Eigene Artenschutz-Expertise, Gegenattest |
| Alternativenprüfung unvollständig | Kläger | Planfeststellungsbeschluss, Planunterlagen |
| Grundstückswertminderung | Anlieger (Entschädigung) | Wertgutachten vor/nach, Vergleichspreise |
| Härtung Klimaargument bei LNG | Verband (Kläger) | Emissionsberechnung, IPCC-Berichte, BVerfG |
| Kein effektiver Rechtsschutz Aarhus | Verband | Kostenaufstellung, Vergleich Streitwert vs. Verbandsbudget |

## Fristen und Verjährung

| Frist | Grundlage | Lauf | Hinweis |
|---|---|---|---|
| Klagefrist NABEG/EnLAG | § 74 VwGO i.V.m. NABEG/EnLAG | 1 Monat ab Zustellung Beschluss | Sehr kurz; sofort nach Erhalt des Beschlusses handeln |
| Eilantrag § 80 Abs. 5 VwGO | — | Innerhalb der Klagefrist; keine eigene Ausschlussfrist | Früh stellen, da Bau sofort beginnen kann |
| Beschwerde gegen Eilentscheidung | § 146 Abs. 4 VwGO | 2 Wochen; Begründung 1 Monat | BVerwG bei NABEG/EnLAG-Vorhaben |
| Beteiligung im Planfeststellungsverfahren | — | Auslegungszeitraum + Einwendungsfrist | Versäumnis → eingeschränkte Klagemöglichkeit |
| Entschädigungsklage | § 195 BGB | 3 Jahre ab Kenntnis des Eingriffs | Zivilgericht bei Entschädigungsstreit |
| Bundesfachplanung-Einwendung | NABEG § 9 | Innerhalb der Konsultationsfrist | Frühe Einbindung sichert spätere Klageposition |

## Typische Gegenargumente

| Gegenargument | Gegenstrategie |
|---|---|
| "Beschleunigungsgesetz schränkt Prüfung ein" | Grundrechtliche Mindestanforderungen bleiben; UVP-Richtlinie EU-Recht geht vor; Aarhus-Konvention Art. 9 |
| "Klimaschutz rechtfertigt sofortigen Bau" | § 80 Abs. 3 VwGO Begründung muss auf Einzelfall eingehen; fossiles Vorhaben: Klimaschluss wirkt gegen Sofortvollzug |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Verband nicht klagebefugt — zu spät beteiligt" | Beteiligung muss nur im Planfeststellungsverfahren erfolgt sein, nicht bereits in Bundesfachplanung; Beteiligung dokumentieren |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Enteignungsentschädigung angemessen" | Unabhängiges Wertgutachten beauftragen; Folgeschäden (Wertminderung, Nutzungseinschränkung) erfassen |
| "LNG-Terminal klimaneutral nutzbar" | Ohne verbindliche Wasserstoff-Umrüstungsklausel ist Klimaargument nicht tragfähig; BVerfG-Maßstab anlegen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Rechtsschutz gegen Planfeststellungsbeschluss Energietrasse | Anfechtungsklage nach Pruefschema; Schriftsatz unten |
| Variante A — Einwendung im Planfeststellungsverfahren noch moeglich | Einwendung im Verfahren zuerst; Klage nur nach Bestandskraft |
| Variante B — Mandant als Betroffener will nur Auflagen aendern | Teilanfechtung nur der belastenden Nebenbestimmungen |
| Variante C — Oeffentlichkeit will Gesamtprojekt verhindern | Normenkontrolle oder UVP-Ruege als staerkere Angriffspunkte |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Klage-Antrag BVerwG erste Instanz

```
Bundesverwaltungsgericht Leipzig
Simsonplatz 1
04107 Leipzig

Klage nach § 50 Abs. 1 Nr. 6 VwGO

In dem verwaltungsgerichtlichen Verfahren

[Kläger / Umweltverband]
— Kläger —

gegen

Bundesnetzagentur, Tulpenfeld 4, 53113 Bonn
— Beklagte —

beigeladen: [Vorhabenträger]

Klageziel

1. Der Planfeststellungsbeschluss der Bundesnetzagentur vom [Datum]
 Az. [Az.] für das Vorhaben [Bezeichnung] wird aufgehoben,
 hilfsweise für rechtswidrig und nicht vollziehbar erklärt.

2. Die Beklagte trägt die Kosten des Verfahrens.

Klagefrist: Der Planfeststellungsbeschluss wurde dem Kläger am
[Datum] zugestellt. Die Klagefrist von einem Monat ist gewahrt.

Begründung (vorläufig — wird vertieft nach Akteneinsicht)

A. Zulässigkeit
Der Kläger ist als anerkannter Umweltverband nach §§ 2, 3 UmwRG
klagebefugt. Er hat sich mit Einwendungsschreiben vom [Datum]
am Planfeststellungsverfahren beteiligt. Die Klagefrist ist gewahrt.

B. Begründetheit (vorläufig)

I. UVP-Defizite
Der UVP-Bericht weist folgende materielle Lücken auf:
— Alternativenprüfung unvollständig: Die Erdkabel-Variante
 entlang der Bestandsautobahn A[x] wurde nicht ernsthaft
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
— Artenschutzrechtliche Prüfung (saP) fehlerhaft: Rotmilan-
 Kartierung nur an [n] Terminen außerhalb der Hauptaktivitäts-
 zeiten.

II. Klimaschluss
Das Vorhaben [LNG-Terminal / Erdgas-Pipeline] erhöht die
Treibhausgasemissionen um [x] t CO2-Äquivalente p.a. und
konterkariert die Pflicht des Staates zum Schutz künftiger
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Wir beantragen die Gewährung von Akteneinsicht in die vollständige
Planfeststellungsakte sowie angemessene Verlängerung der
Begründungsfrist nach § 87b Abs. 1 VwGO.
```

### Baustein 2: Eilantrag gegen sofortige Vollziehung Planfeststellungsbeschluss

```
Bundesverwaltungsgericht Leipzig

Antrag nach § 80 Abs. 5 VwGO

In dem o.g. Verfahren [Az. Klage]

Antrag

Die aufschiebende Wirkung der Klage des Antragstellers vom [Datum]
gegen den Planfeststellungsbeschluss der Bundesnetzagentur vom
[Datum] wird wiederhergestellt.

Begründung

I. Formeller Mangel Vollziehungsanordnung § 80 Abs. 3 VwGO
Die Bundesnetzagentur hat die sofortige Vollziehung mit der
Begründung angeordnet, es bestehe ein dringendes öffentliches
Interesse an der zeitnahen Realisierung des Vorhabens. Diese
Begründung ist formell unzureichend, da sie keine
Auseinandersetzung mit den konkreten Umständen des Einzelfalls —
insbesondere den gerügten UVP-Fehlern und den Risiken
irreversibler Natureingriffe — enthält.

II. Erfolgsaussicht der Hauptsache
Die Klage hat wegen der oben dargelegten UVP-Defizite und der
mangelhaften saP erhebliche Erfolgsaussichten. Eine vollständige
Aufhebung des Planfeststellungsbeschlusses erscheint möglich.

III. Interessenabwägung
Beginnen die Bauarbeiten sofort, drohen irreversible Eingriffe in
FFH-Gebiete und in das Grundeigentum des Antragstellers. Diese
Schäden sind durch einen späteren Klageerfolg nicht mehr
rückgängig zu machen. Demgegenüber kann der Baubeginn um die
Dauer des Eilverfahrens (typisch 4–8 Wochen) verschoben werden,
ohne den Vorhabenerfolg dauerhaft zu gefährden.
```

### Baustein 3: Einwendung im Planfeststellungsverfahren (Anlieger)

```
An die [Planfeststellungsbehörde / Bundesnetzagentur]

Einwendungen im Planfeststellungsverfahren [Bezeichnung]

Einwender: [Name, Anschrift, Grundstück Flurstück]

Sehr geehrte Damen und Herren,

gegen das geplante Vorhaben erheben wir folgende Einwendungen:

1. Eigentumsbetroffenheit
Das Grundstück des Einwenders (Flurstück [x], Gemarkung [y])
liegt innerhalb des geplanten Schutzstreifens. Es wird durch
Dienstbarkeiten belastet, die die landwirtschaftliche Nutzung
erheblich einschränken. Eine angemessene Entschädigung nach
§ 18 EnWG ist sicherzustellen.

2. Erdkabel-Vorrang § 4 EnLAG
Im Bereich der Ortschaft [X] liegt Wohnbebauung in Sichtweite
der geplanten Freileitung. Der Einwender beantragt gemäß
§ 4 Abs. 1 EnLAG die Prüfung und bevorzugte Realisierung
als Erdkabel.

3. Lärm und elektromagnetische Felder
Die Schallstudie im UVP-Bericht berücksichtigt die Summenwirkung
mehrerer geplanter Umspannwerke und Schaltanlagen nicht.
Grenzwerte der 26. BImSchV (elektromagnetische Felder) sind
nachzuweisen.

Wir bitten um Berücksichtigung dieser Einwendungen und
vorherige Unterrichtung über den Erörterungstermin.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Streitwert und Kosten

| Position | Berechnung | Hinweis |
|---|---|---|
| Streitwert Verbandsklage | § 52 Abs. 1 GKG; Auffangwert EUR 5.000 oder Orientierungswert Streitwertkatalog Verwaltungsgerichtsbarkeit; BVerwG-Streitwerte bei Großvorhaben bis EUR 100.000 | Keine wirtschaftlichen Eigeninteressen des Verbands |
| Streitwert Anlieger | Wert der Eigentumsbeeinträchtigung; Entschädigungsforderung; typisch EUR 10.000–50.000 | § 52 Abs. 1 GKG nach wirtschaftlichem Interesse |
| Eilantrag Streitwert | Hälfte des Hauptsache-Streitwerts | Beschlussmäßige Entscheidung |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |
| Kostenprivileg Verbände | Art. 9 Abs. 4 Aarhus: Kosten dürfen nicht prohibitiv sein | Ermäßigung nach § 162 Abs. 3 VwGO beigeladener Verband |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Klagefrist 1 Monat läuft | Sofortige Klage mit vorläufiger Begründung; Akteneinsicht parallel beantragen; Frist unbedingt wahren |
| Sofortvollzug angeordnet | Eilantrag § 80 Abs. 5 VwGO; § 80 Abs. 3-Mangel als eigenständigen Aufhebungsgrund geltend machen |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Anlieger Grundstück betroffen | Entschädigungsanspruch frühzeitig beziffern; Wertgutachten vor Baubeginn; ggf. zivilrechtliche Entschädigungsklage |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |

## Anschluss-Skills

- `energieanlagen-bimschg-genehmigung-verfahren` — BImSchG-Genehmigung angrenzender Anlagen
- `eilantrag-80-abs-5-vwgo` — Vertiefung Eilantrag-Schriftsatz
- `fachanwalt-verwaltungsrecht-einstweiliger-rechtsschutz` — Grundlagen einstweiliger Rechtsschutz

## Aktuelle Leitentscheidungen (v14.2 Ergaenzung)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen

- EnLAG §§ 1, 4
- BBPlG, NABEG §§ 18, 50
- WindSeeG, LNG-Beschleunigungsgesetz
- EnWG § 28r (H2-Stammnetz), § 18 (Entschädigung)
- VwGO §§ 50, 74, 80, 80a, 113, 146
- UmwRG §§ 2, 3
- BNatSchG §§ 13, 44
- UVPG
- Aarhus-Konvention Art. 9 / EU-RL 2003/35
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

---

## Skill: `normenkontrolle-47-vwgo`

_Normenkontrollantrag nach § 47 VwGO gegen Bauleitplaene, Rechtsverordnungen oder Satzungen: Betroffener will Bebauungsplan oder kommunale Satzung zu Fall bringen: Normenkontrollantrag nach § 47 VwGO gegen Bauleitplaene, Rechtsverordnungen oder Satzungen: Be..._

# Normenkontrollantrag nach § 47 VwGO gegen Bauleitplaene, Rechtsverordnungen oder Satzungen: Betroffener will Bebauungsplan oder kommunale Satzung zu Fall bringen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Normenkontrollantrag nach § 47 VwGO gegen Bauleitplaene, Rechtsverordnungen oder Satzungen: Betroffener will Bebauungsplan oder kommunale Satzung zu Fall bringen. Normen: § 47 VwGO (Normenkontrolle OVG), Art. 14 GG (Eigentumsschutz), § 1 Abs. 7 BauGB (Abwaegungsgebot). Prüfraster: Antragsfrist 1 Jahr ab Inkrafttreten, Antragsbefugnis, OVG-Zuständigkeit, Abwaegungsfehler. Output Normenkontrollantrag-Entwurf. Abgrenzung: Anfechtungsklage gegen einzelnen VA siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Planfeststellung siehe energietrassen-planfeststellung-rechtsschutz.

### Normenkontrolle § 47 VwGO

## 1) Anwendungs-Bereich

### Pruefbare Normen § 47 I VwGO

- Bauleitpläne (Flächennutzungsplan, Bebauungsplan)
- Rechtsverordnungen Land / Kreis / Gemeinde
- Satzungen Gemeinden

### Nicht prüfbare

- Bundesgesetze (BVerfG-Verfahren)
- Verwaltungsvorschriften (im Wirkungsfeld)

## 2) Antragsbefugnis § 47 II VwGO

### Voraussetzung

- Rechts-Beeintraechtigung erkennbar
- Persönliche Betroffenheit
- Nicht jede Beteiligung

### Beispiele

- Grundeigentuemer im B-Plan-Gebiet
- Nachbar bei B-Plan
- Gewerbe bei Sondernutzungs-Satzung

## 3) Frist § 47 II VwGO

- **1 Jahr** nach Bekanntmachung
- Bei Versäumnis: Antrag unzulaessig
- Änderungs-Anträge erneut Frist

## 4) Zuständigkeit OVG

- Oberverwaltungsgericht / Verwaltungsgerichtshof
- Spezialisierte Senate
- Bei Verfahrens-Mangel: Verweisung an VG

## 5) Verfahren

### Schritt 1 — Antrag

- Schriftlich beim OVG
- Bezug auf konkrete Norm
- Antragsbegründung

### Schritt 2 — Anhörung

- Antragsgegner (Plan-Geber)
- Beteiligte

### Schritt 3 — Beweisaufnahme

- Akten-Einsicht
- ggf. Sachverständige

### Schritt 4 — Urteil

- Normenverwerfungs-Urteil
- Bei Erfolg: Norm tritt rueckwirkend außer Kraft
- Allgemein-Verbindlichkeit

## 6) Bauplanungs-Recht Schwerpunkt

### Prüfungsmaßstab

- Pflicht-Inhalte BauGB
- Abwaegungs-Gebot § 1 VII BauGB
- Verhältnismaessigkeit

### Mangel-Quellen

- Abwaegungs-Defizite
- Verfahrens-Mangel (Beteiligungs-Verletzung)
- Materiell rechtswidrige Inhalte

### Heilung § 215 BauGB

- Bestimmte Mangel sind heilbar
- Bei Mangel-Vortrag im Verfahren: keine Heilung
- Detaillierte Prüfung erforderlich

## 7) Workflow

### Phase 1 — Plan-Prüfung

- Plan-Begründung
- Abwaegungs-Vorgang
- Beteiligungs-Verfahren

### Phase 2 — Antragsbegründung

- Konkrete Mängel
- Eigene Betroffenheit
- Beweisanbote

### Phase 3 — OVG-Verfahren

- Schriftsatz-Wechsel
- Anhörungs-Termin
- Urteil

### Phase 4 — Bei Erfolg

- Norm verworfen
- Plan-Geber muss neu planen
- Folge: Bauverbot

## 8) Einstweiliger Rechtsschutz § 47 VI VwGO

### Voraussetzungen

- Eilbedürftigkeit
- Erfolgsaussicht Hauptverfahren

### Beispiel

- Bei beantragter Baugenehmigung im B-Plan
- Einstweilige Anordnung gegen Plan-Vollzug

## 9) Verfahrensdauer und Kosten

- 1-3 Jahre typisch
- Streitwert nach wirtschaftlichem Interesse
- Bei Verlust: Gerichts- + Anwaltskosten

## 10) Typische Fehler

1. **1-Jahres-Frist verpasst**
2. **Antragsbefugnis nicht ausreichend dargetan**
3. **Mängel pauschal vorgetragen**
4. **Heilungs-Pflicht nach § 215 BauGB ignoriert**

## 11) Aktuelle BVerwG-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `normenkontrolle-bauleitplanung` (Vollplugin) — Vertieftes Verfahren
- `fachanwalt-verwaltungsrecht-orientierung` — Triage
- `widerspruch-oder-klage-erstpruefung` — bei anderer VG-Sache

---

## Skill: `schriftsatzkern-substantiierung`

_Substantiierten Schriftsatzkern für verwaltungsrechtliche Klagen und Anträge erstellen: Widerspruch, Anfechtungsklage, Verpflichtungsklage, Eilantrag § 80 Abs: Substantiierten Schriftsatzkern für verwaltungsrechtliche Klagen und Anträge erstellen: Widerspru..._

# Substantiierten Schriftsatzkern für verwaltungsrechtliche Klagen und Anträge erstellen: Widerspruch, Anfechtungsklage, Verpflichtungsklage, Eilantrag § 80 Abs


## Aktenstart statt Formularstart

Wenn zu **Widerspruchsschrift Mandat Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Fachanwalt Verwaltungsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Substantiierten Schriftsatzkern für verwaltungsrechtliche Klagen und Anträge erstellen: Widerspruch, Anfechtungsklage, Verpflichtungsklage, Eilantrag § 80 Abs. 5 VwGO. Normen: §§ 42 und 80 VwGO sowie §§ 28 und 48 VwVfG. Prüfraster: Tatsachenvortrag-Geruest, Anspruchsgrundlagen-Kette, Beweisangebote, Hilfsanträge, Replik-/Duplik-Vorausschau. Output Schriftsatz-Geruest mit Klagepunkten und Begründungs-Bausteine. Abgrenzung: Fertige Klageschrift siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Vergabe-Schriftsatz siehe fachanwalt-vergaberecht-Plugin.

### Schriftsatzkern und Substantiierung im Allgemeines Verwaltungs- und Bauplanungsrecht

## Wann dieser Arbeitsgang greift

- Es soll ein vollwertiger Schriftsatz im Bereich Allgemeines Verwaltungs- und Bauplanungsrecht erstellt werden, typischerweise: Widerspruch, Anfechtungsklage VG, Verpflichtungsklage, Eilantrag § 80 Abs. 5 VwGO.
- Die Mandatsannahme und ggf. Vergleichsverhandlung sind abgeschlossen oder gescheitert.
- Klage-, Widerspruchs-, Einspruchs-, Rechtsmittel-Frist ist bekannt und im Kalender eingetragen.

## Aufbauschema

### A. Rubrum

- Parteien (Bezeichnung wie im Vorprozess oder Bescheid, exakte Schreibweise!).
- Zustellungsanschrift Bevollmaechtigte.
- Gericht/Behörde (Zuständigkeit pruefen und im Schriftsatz darstellen, wenn streitig).
- Aktenzeichen (Bezugs-Az., neues Az. nach Eingang).
- Streitwert/Gegenstandswert.

### B. Antraege

Klassischer Antrag-Block; je nach Verfahrenstyp:

- Leistungsantrag (zu zahlen, zu unterlassen, zu beseitigen, herauszugeben).
- Feststellungsantrag (Feststellungsinteresse darlegen).
- Gestaltungsantrag (Aufhebung, Anfechtung, Scheidung).
- Hilfsantraege staffeln (von eng nach weit oder von hoch nach niedrig).

### C. Tatsachenvortrag

Der Substantiierungs-Kern; pro Anspruchsgrundlage in VwVfG, VwGO, BauGB, BauNVO, GewO, BBG/BeamtStG eine eigene Tatsachen-Sequenz:

1. **Sachverhalts-Chronologie** mit konkreten Daten (Tag, Uhrzeit, Ort, Personen).
2. **Mandantenseitige Tatsachenbehauptungen** mit Beweisangeboten.
3. **Gegnerisches Verhalten** mit Belegen (Schreiben, Aussage, Verhalten).
4. **Schaden/Folgen** bezifferbar (Hauptforderung, Nebenforderung, Zinsen, Folgekosten).

### D. Rechtliche Wuerdigung

Anspruchsaufbau klassisch:

1. **Anspruchsgrundlage** nennen (z.B. § X iVm § Y).
2. **Tatbestandsmerkmale** durchgehen; jedes Merkmal wird gegen den Tatsachenvortrag gespiegelt.
3. **Einwendungen** der Gegenseite vorwegnehmen und entkraeften.
4. **Rechtsprechungs-Verweise:** BAG/BGH/BVerfG/EuGH/BFH je nach Fachgebiet; bei Allgemeines Verwaltungs- und Bauplanungsrecht typischerweise die letzte hoechstrichterliche Linie zitieren.
5. **Subsumtion-Ergebnis** klar formulieren.

### E. Beweisangebote

Pflichtbestandteil, ohne den Substantiierung nicht ausreicht:

- Urkundenbeweis: konkrete Anlage Kxx benennen, Inhalt nicht nur "Vertrag" sondern "Vertrag vom TT.MM.JJJJ, dort § X Abs. Y, Anlage K1".
- Zeugenbeweis: Name, ladungsfaehige Anschrift, Beweisthema in einem Satz.
- Sachverstaendigenbeweis: ggf. Privatgutachten mit anfuegen, gerichtliches Gutachten beantragen.
- Parteivernehmung als letzte Stufe, mit Antrag § 448 ZPO und Indiziengeruest.
- Inaugenscheinnahme: bei Sache vor Ort (Mietraum, Baustelle, Fahrzeug, Hardware).

### F. Anlagenverzeichnis

- K1, K2 ... durchnummeriert (Antragstellerin/Klaegerin).
- Bei Beklagten B1, B2 ...
- Jede Anlage mit Datum, Absender, Empfaenger, Inhaltsbeschreibung in einem Satz.
- Pflicht-Erwaehnung im Tatsachenvortrag.

## Substantiierungs-Fallen im Allgemeines Verwaltungs- und Bauplanungsrecht

- **Pauschaltatsachen** ohne konkrete Daten ("seit Jahren", "regelmaessig", "in mehreren Faellen") werden vom Gericht uebergangen.
- **Beweisangebot zur falschen Tatsache:** Beweisthema deckt nur Teilaussage ab.
- **Selbst-widersprueche** zwischen Schriftsatz und Anlage ("Im Vertrag steht doch was anderes").
- **Verspaeteter Vortrag** § 296 ZPO/§ 87b VwGO: Rueglich-Fristen beachten, Verschulden vermeiden.
- **Anspruchskonkurrenz** zwischen mehreren Grundlagen: nicht eine wegfallen lassen.

## Pruefkette vor Versand

1. Antragsformulierung tenoriert (urteilstauglich, vollstreckbar)?
2. Jede Tatbestandsmerkmal-Subsumtion mit eigener Tatsache + Beweis hinterlegt?
3. Frist eingehalten (Eingangsstempel/elektronische Uebermittlung)?
4. Zuständigkeit positiv festgestellt?
5. Streitwert plausibel, ggf. mit Anlage Streitwert-Berechnung?
6. Anlagenverzeichnis vollstaendig und nummerisch konsistent?
7. beA-/EGVP-/EBO-Konformitaet (PDF/A, ERVV-Signatur)?
8. Vier-Augen-Pruefung durch Sozius oder Senior-Anwaeltin?

## Rechtsprechungs-Werkzeugkasten

- BVerfG, BGH, BAG, BFH, BVerwG, EuGH und die jeweils massgeblichen Fachsenate für Allgemeines Verwaltungs- und Bauplanungsrecht.
- VwVfG, VwGO, BauGB, BauNVO, GewO, BBG/BeamtStG sowie Verordnungen/Richtlinien dazu.
- Aktuelle Reform- und Gesetzgebungslage einbeziehen.

## Pflicht-Output

1. **Schriftsatz** mit Rubrum, Antraegen, Tatsachenvortrag, Rechtsausfuehrung, Beweisangeboten, Anlagenverzeichnis.
2. **Anlagen-Konvolut** numerisch geordnet, jede Anlage einzeln benannt.
3. **Frist-Doku** mit Eingangsbestaetigung (beA-Eingangsnachricht, EB).
4. **Streitwertskizze** (eigenes Memo, falls > 1 Anspruch).
5. **Mandanten-Erinnerung** mit Naechster-Schritt-Aufgaben (Zeuginnen vorbereiten, Sachverstaendiger?).

## Beispiel-Anspruchsgrundlagen im Allgemeines Verwaltungs- und Bauplanungsrecht

Drei haeufig gebrauchte Anspruchsgrundlagen aus VwVfG, VwGO, BauGB, BauNVO, GewO, BBG/BeamtStG und ihre Substantiierungs-Anforderungen:

### Grundlage 1

- Tatbestandsmerkmal 1: konkrete Tatsache + Beweis.
- Tatbestandsmerkmal 2: konkrete Tatsache + Beweis.
- Tatbestandsmerkmal 3: konkrete Tatsache + Beweis.
- Rechtsfolge: konkreter Antrag.

### Grundlage 2

Analog - jede Tatsache braucht ein Beweisangebot.

### Grundlage 3 (Auffanggrundlage / Sekundaeranspruch)

Hilfsweise vortragen, klar als Hilfsantrag/Hilfsvortrag kennzeichnen.

## Antrags-Muster nach Verfahrenstyp

Typische Antraege in Allgemeines Verwaltungs- und Bauplanungsrecht (Widerspruch, Anfechtungsklage VG, Verpflichtungsklage, Eilantrag § 80 Abs. 5 VwGO):

- Hauptantrag (Leistung/Feststellung/Gestaltung).
- Hilfsantrag (z.B. für den Fall, dass Hauptforderung verjaehrt ist).
- Annex-Antraege (Zinsen, Nebenforderungen, Kosten).
- Streitwert-Antrag (falls Streitwert streitig).

## Beweisaufnahme - was das Gericht sehen will

### Urkundenbeweis

- Anlage K1: Bezeichnung, Datum, kurze Inhaltsbeschreibung.
- Im Tatsachenvortrag: "Diese Behauptung beruht auf dem als Anlage K1 vorgelegten Schreiben der Beklagten vom TT.MM.JJJJ, dort Seite Y, Absatz Z."

### Zeugenbeweis

- Form: "Beweis: Aussage der Zeugin Name, ladungsfaehige Anschrift, zum Beweisthema (konkret in einem Satz)."
- Mehrere Zeuginnen zum gleichen Thema: Indiziengeruest staerken.
- Keine Beweisermittlung ueber Zeugnis - das Beweisthema muss konkret sein.

### Sachverstaendigenbeweis

- Bei Allgemeines Verwaltungs- und Bauplanungsrecht-typischen Streitfaellen oft notwendig (Bauwerk, IT-System, Anlagebewertung, medizinische Frage).
- Privatgutachten als Anlage K vorlegen + zugleich gerichtliches Gutachten beantragen.
- Verfahrensoekonomie: Sachverstaendigen-Kosten frueh mit Mandantin besprechen.

### Parteivernehmung (§ 448 ZPO)

- Letzte Stufe, nur wenn andere Beweismittel ausgeschoepft.
- Indiziengeruest vortragen, das eine gewisse Wahrscheinlichkeit der Behauptung tragt.

## Replik-/Duplik-Vorausschau

Schon im Klageschriftsatz die wahrscheinlichen Einwaende der Gegenseite vorwegnehmen:

- Verjährung -> Hemmungstatbestand vortragen.
- Erfuellung/Aufrechnung -> rechtzeitige Tatsachenbasis schaffen.
- Formmangel -> Heilung/Schutz-Argument bereit halten.
- Treuwidrigkeit -> Indiziengeruest gegen Treuwidrigkeits-Vorwurf.

## Elektronische Einreichung (beA, EGVP, EBO, ELSTER)

- PDF/A-2 oder PDF/A-3, mit eingebetteten Schriften.
- Strukturdatensatz nach ERVV pflicht-konform (Sender, Empfaenger, Az., Versanddatum).
- Qualifizierte elektronische Signatur (qeS) der einreichenden RA-Person oder einfacher elektronischer Versand ueber beA (sicherer Uebermittlungsweg).
- Eingangsbestaetigung aufbewahren - Datum der Einreichung ist Fristwahrungs-Beweis.
- 1.10.2026 / 1.10.2027 - ZVollstrDigitG-Aenderungen im Vollstreckungsbereich; in Allgemeines Verwaltungs- und Bauplanungsrecht ggf. spezifische ERV-Pflichten beachten.

## Schriftsatz-Stil

- Aktiv, kurze Saetze, klare Subsumtion.
- Keine Floskeln ("Die Klage ist zulaessig und begruendet" als Ueberschrift, aber dann substantiieren).
- Mandanten- und Beweismittel-Zitate woertlich, in Anfuehrungszeichen, mit Anlage-Verweis.
- Keine Gefuehlsausbrueche - sachlich auch bei provokanter Gegenseite.

## Vier-Augen-Check

Vor Versand:

- [ ] Antrag tenorierungsfaehig
- [ ] Frist gewahrt mit Reserve
- [ ] Jede Tatsache hat Beweis
- [ ] Anlagen vollstaendig und nummeriert
- [ ] Rechtsprechungs-Zitat aktuell
- [ ] Streitwert plausibel
- [ ] beA/EGVP-konform
- [ ] Senior-/Sozius-Freigabe

## Leitentscheidungen Schriftsatz-Substantiierung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Cross-Refs

- `erstgespraech-mandatsannahme` (im selben Plugin) für die Tatsachen-Grundlage und Streitwertskizze.
- `vergleichsverhandlung-strategie` (im selben Plugin) für parallelen Vergleichsversuch (Gueteverhandlung, Mediation).

---

## Skill: `vergleich-106-vwgo-behoerde`

_Verwaltungsrechts-Vergleich nach § 106 VwGO und öffentlich-rechtlicher Vertrag nach § 55 VwVfG: Mandant will Streit mit Behörde außergerichtlich beilegen: Verwaltungsrechts-Vergleich nach § 106 VwGO und öffentlich-rechtlicher Vertrag nach § 55 VwVfG: Mandan..._

# Verwaltungsrechts-Vergleich nach § 106 VwGO und öffentlich-rechtlicher Vertrag nach § 55 VwVfG: Mandant will Streit mit Behörde außergerichtlich beilegen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Verwaltungsrechts-Vergleich nach § 106 VwGO und öffentlich-rechtlicher Vertrag nach § 55 VwVfG: Mandant will Streit mit Behörde außergerichtlich beilegen. Normen: § 106 VwGO (Prozessvergleich), § 55 VwVfG (Vergleichsvertrag), § 28 VwVfG (Anhörung). Prüfraster: Vergleichsfähigkeit, Mediation VwG, Eroerrterungstermin, Petitionsweg, Protokoll-Anforderungen. Output Vergleichs-Entwurf, Strategie-Memo. Abgrenzung: Klage-Strategie siehe fachanwalt-verwaltungsrecht-anfechtungsklage; Vergleich Vergabe siehe fachanwalt-vergaberecht-Plugin.

### Verwaltungsrechts-Vergleich / Behördenkommunikation

## Zweck

Verwaltungsstreit kann an mehreren Stellen vergleichsweise beendet werden: **vor Bescheid** durch konsensorientierte Anhörung § 28 VwVfG, **nach Bescheid** durch Vergleichsvertrag § 55 VwVfG, **im Klageverfahren** durch Vergleich § 106 VwGO, **im Erörterungstermin** durch gerichtliche Mitteilung. Behördenkommunikation hat eigene Strategie- und Höflichkeits-Anforderungen.

## Eingaben

- Verwaltungsakt-Typ (begünstigend, belastend, Drittwirkung)
- Behörden-Ebene (Bund, Land, Kommune)
- Verfahrensphase (Anhörung, Widerspruch, Klage)
- Mandant (Bürger, Unternehmen, Konkurrent)
- Streitgegenstand (Genehmigung, Bauantrag, Subvention, Polizei-Verfügung)

## Rechtlicher Rahmen

- **§ 28 VwVfG** — Anhörung vor Verwaltungsakt
- **§ 55 VwVfG** — Vergleichsvertrag öffentlich-rechtlich
- **§§ 54-62 VwVfG** — Öffentlich-rechtlicher Vertrag
- **§ 106 VwGO** — Vergleich im Verwaltungsprozess
- **§ 87 VwGO** — Erörterungstermin
- **§§ 68 ff. VwGO** — Widerspruchsverfahren (Vorverfahren)
- **Art. 17 GG** — Petitionsrecht
- **MediationsG** — Mediation im Verwaltungsverfahren möglich

### Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## ADR-Pfade

### Pfad 1 — Anhörung § 28 VwVfG strategisch nutzen

- Vor Erlass des belastenden VA
- Anwalts-Stellungnahme mit Lösungs-Vorschlägen
- Behörde kann Modifikation erwägen
- Effektiv bei Ermessens-VAs

### Pfad 2 — Widerspruchs-Vergleich

- Im Widerspruchsverfahren (sofern noch zulässig)
- Verwaltungsbehörde zur Modifikation bewegen
- Schriftliche Verständigung

### Pfad 3 — Öffentlich-rechtlicher Vergleichsvertrag § 55 VwVfG

- Schriftform § 57 VwVfG zwingend
- Verzicht auf Anfechtungsklage gegen Modifikation
- Nur bei Ungewissheit über Sach-/Rechtslage
- Genehmigung Aufsichtsbehörde ggf. erforderlich

### Pfad 4 — Vergleich § 106 VwGO im Klageverfahren

- Im Verwaltungsprozess
- Erörterungstermin § 87 VwGO
- Gerichtlicher Vergleich vollstreckbar (§ 168 I Nr. 3 VwGO)
- Kostenregelung im Vergleich

### Pfad 5 — Mediation (selten, aber möglich)

- Bei Großvorhaben (Infrastruktur, UVP)
- Stuttgart 21-Modell
- Ungebundene Mediatoren
- Konsens als Ziel, nicht Vergleich

## Workflow

### Phase 1 — Verfahrens-Eintritt

- Akteneinsicht § 29 VwVfG
- Behörden-Position erkunden
- Anhörungs-Stellungnahme entwerfen

### Phase 2 — Anhörungs-Stellungnahme

- Sachverhalts-Korrektur
- Rechtsgründe
- Lösungs-Vorschläge (Auflagen, Modifikation)

### Phase 3 — Widerspruch (sofern Vorverfahren noch vorhanden)

- Beachtung: § 80 VwGO Anordnung aufschiebende Wirkung
- Bei Kommunen: häufig kein Vorverfahren (Landesrecht)
- Vergleichs-Ansatz im Widerspruch

### Phase 4 — Klage VG / OVG

- Anfechtungs-/Verpflichtungs-/Feststellungs-Klage
- Erörterungstermin nutzen
- Vergleich § 106 VwGO

### Phase 5 — Vollstreckung

- Bei Verpflichtungs-Klage: § 167 VwGO Vollstreckung
- Zwangsgeld gegen Behörde

## Strategie und Taktik

- **Anhörung ist Schlüsselphase**: hier ist Behörden-Ermessen am offensten
- **Behörden-Sprache**: nüchtern, sachlich, faktisch — keine Polemik
- **§ 55 VwVfG Vergleichsvertrag**: schriftliche Form zwingend, Aufsichts-Genehmigung beachten
- **Erörterungstermin**: VG ist meist vergleichsfreundlich, insb. bei tatsächlichen Streit
- **Petitionsweg parallel**: ergänzend, nicht statt Rechtsbehelf
- **Bei Ermessens-Reduzierung-Argumenten**: vorsichtig — Behörde behält Ermessen häufig

## Aktuelle Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellen und Updates

Stand: 05/2026. VwVfG/VwGO im Kern stabil. Für die Verifikation öffentlich-rechtlicher Vergleiche und Erörterungstermine vor Ausgabe Rechtsprechungsdatenbank des BVerwG (bverwg.de) konsultieren — keine Aktenzeichen aus Modellwissen.

- VwGO — [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vwgo/)
- VwVfG — [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vwvfg/)
- BVerwG-Entscheidungsdatenbank — [bverwg.de](https://www.bverwg.de/entscheidungen)

---

## Skill: `vergleichsverhandlung-strategie`

_Vergleichsverhandlungs-Strategie für Verwaltungsrechtsstreitigkeiten: Partei oder Anwalt will außergerichtlichen Vergleich mit Behörde oder am VG erzielen: Vergleichsverhandlungs-Strategie für Verwaltungsrechtsstreitigkeiten: Partei oder Anwalt will außerge..._

# Vergleichsverhandlungs-Strategie für Verwaltungsrechtsstreitigkeiten: Partei oder Anwalt will außergerichtlichen Vergleich mit Behörde oder am VG erzielen


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Vergleichsverhandlungs-Strategie für Verwaltungsrechtsstreitigkeiten: Partei oder Anwalt will außergerichtlichen Vergleich mit Behörde oder am VG erzielen. Normen: § 106 VwGO, § 55 VwVfG. Prüfraster: ZOPA (Zone of Possible Agreement), BATNA, Verhandlungsfenster, Druckmittel (Klagehaeufung, UmwRG), Settlement-Skript, Vergleichsentwurf. Output Verhandlungsstrategie-Memo, Vergleichsentwurf. Abgrenzung: Prozessvergleich VG siehe fachanwalt-verwaltungsrecht-vergleich-106-vwgo-behoerde; Anfechtungsklage (wenn kein Vergleich) siehe fachanwalt-verwaltungsrecht-anfechtungsklage.

### Vergleichsverhandlung und Einigung im Allgemeines Verwaltungs- und Bauplanungsrecht

## Wann dieser Arbeitsgang greift

- Sachverhalte aus dem Bereich Allgemeines Verwaltungs- und Bauplanungsrecht, in denen eine aussergerichtliche oder prozessbegleitende Einigung sinnvoll erscheint.
- Typische Konstellationen: Abhilfe, Tausch-/Anpassungslosung, Mediation Behörde-Buerger.
- Sowohl in der aussergerichtlichen Phase (vor Klage) als auch im laufenden Prozess (Gueteverhandlung, Hauptverhandlung).

## Vorbereitung der Verhandlung

### 1. BATNA und ZOPA bestimmen

- **BATNA** (Best Alternative to Negotiated Agreement): Was passiert, wenn wir uns nicht einigen? Kosten- und Zeit-Prognose Prozess, Erfolgsaussichten-Quote, Vollstreckungsrisiko.
- **WATNA** (Worst Alternative): schlimmster denkbarer Verlauf bei Klage/Klageabweisung.
- **Reservation Price** auf eigener Seite: untere Grenze der Akzeptanz.
- **ZOPA** (Zone of Possible Agreement): geschaetzte Schnittmenge zwischen eigener Reservation und der vermuteten Reservation der Gegenseite.

### 2. Interessen vs. Positionen

Klassisches Harvard-Konzept: nicht nur Positionen ("Ich will 100.000 Euro") sondern Interessen ("Ich brauche bis Jahresende Liquiditaet"). In Allgemeines Verwaltungs- und Bauplanungsrecht typische Interessen-Cluster:

- Liquiditaet (Sofort-Zahlung vs. Ratenzahlung)
- Reputation (Gegnerin will keinen Prozess mit Pressewirkung)
- Zukunfts-Beziehung (Mieter und Vermieter, Arbeitgeberin und ehem. Arbeitnehmer, Geschaeftspartner)
- Steuerliche Optimierung (Vergleich vs. Klage: ertragsteuerliche Behandlung, USt-Frage)
- Vertraulichkeit (NDA im Vergleich)

### 3. Druckmittel und Hebel

- Frist (Klage-/Verjährungsfrist als Druckmittel der Gegenseite kennen und eigene Frist gezielt einsetzen).
- Eskalationsstufen ankuendigen ohne sie zu uebertreiben.
- Hinweis auf Beweismittel, ohne diese vollstaendig offen zu legen.
- Reputationsdruck (Presse, Branche, Berufsregeln) sehr massvoll, nur wenn ethisch vertretbar.

## Ablauf der Verhandlung

### Eroeffnung

- Anker setzen: erste Zahl/Position deutlich hoeher als Reservation, aber begruendbar.
- Begruendung mit konkreten Positionen aus VwVfG, VwGO, BauGB, BauNVO, GewO, BBG/BeamtStG verknuepfen.

### Konzessionsphase

- In kleinen, begruendeten Schritten nachgeben.
- Jede Konzession an Gegenleistung knuepfen ("Wenn Sie X, dann koennen wir Y").
- Konzessionsmuster nicht linear (sonst extrapolierbar) sondern abnehmend.

### Endspiel

- Abschluss aktiv herbeifuehren ("Sind wir bei 47.500 dann durch?").
- Schweige-Pausen aushalten.
- Nachverhandlungs-Versuche der Gegenseite ("ein letztes Detail noch") freundlich, aber bestimmt zurueckweisen, wenn Substanz steht.

## Vergleichsentwurf - Pflichtbestandteile

### Bei aussergerichtlichem Vergleich

1. **Praeambel** mit kurzem Sachstand und Streitthema.
2. **Hauptregelung** (Zahlung, Leistung, Unterlassung, Rueckabwicklung).
3. **Faelligkeit** und Verzinsung.
4. **Sicherheiten** (Buergschaft, Hinterlegung, Sicherungsabtretung).
5. **Erfuellung gegen Erledigung:** keine Aufrechnung, Ratenausfall = Sofortfaelligkeit.
6. **Abgeltungs-/Vorbehaltsklausel:** "Mit diesem Vergleich sind alle wechselseitigen Anspruche aus dem zugrundeliegenden Sachverhalt abgegolten."
7. **Verschwiegenheit** (wenn von einer Partei gewuenscht).
8. **Steuerliche Behandlung** ggf. ausdruecklich, sonst Hinweis auf Steuerberatung.
9. **Salvatorische Klausel und Schriftform.**
10. **Vollstreckungstitel-Ersatz:** notarielle Beurkundung, Anwaltsvergleich nach § 796a ZPO, oder Schiedsvergleich.

### Bei Prozessvergleich

- Protokollvergleich nach § 794 Abs. 1 Nr. 1 ZPO (Vollstreckungstitel kraft Protokollierung).
- Widerrufsvorbehalt mit klarer Frist.
- Kostenregelung: ueblich Kostenaufhebung, ggf. Quote.
- Beteiligung der Streithelfer/Nebenintervenienten beachten.

## Risiken und Stolpersteine im Allgemeines Verwaltungs- und Bauplanungsrecht

- Steuerliche Fehlbehandlung: Vergleichszahlung als Schadensersatz vs. Lohn vs. USt-pflichtige Leistung -> VwVfG und ESt-/USt-Regeln pruefen.
- Vollmacht: Mandantin muss zustimmen, anwaltliche Vergleichsbefugnis muss in Vollmacht expliziert sein.
- Vollstreckbarkeit: aussergerichtlicher Vergleich ohne notarielle Form/Anwaltsvergleich ist kein Vollstreckungstitel.
- Verzicht zu weit gefasst: pauschale Abgeltungsklausel kann eigene Ansprueche unbeabsichtigt mit erfassen.
- Mandanten-Erwartung: Vergleich ist oft Kompromiss - Erwartungsmanagement vor Verhandlung.

## Pflicht-Output

1. **Verhandlungs-Memo** mit BATNA/WATNA, ZOPA-Schaetzung, Strategie.
2. **Vergleichsentwurf** (anwaltsvertraglich oder Protokollvergleich-Skript).
3. **Mandantenfreigabe** vor Unterzeichnung schriftlich.
4. **Steuer- und Vollstreckungs-Memo** zum Vergleich.
5. **Abschluss-Schreiben** an Gegenseite mit Kopien und Erfuellungsplan.

## Verhandlungs-Skripte

### Skript 1: Eroeffnung mit Ankerwert

> "Wir haben die Sache durchgerechnet. Auf Basis von VwVfG und der aktuellen Rechtsprechung kommen wir auf eine Hauptforderung von X Euro plus Y Euro Nebenforderungen. Wir sind bereit, ueber eine Pauschalsumme zu sprechen, die die Sache abschliesst."

### Skript 2: Begruendete Konzession

> "Wir koennen Z Euro nachgeben, wenn Sie im Gegenzug die Klausel A streichen und einer Vertraulichkeitsvereinbarung zustimmen. Andernfalls bleiben wir bei der urspruenglichen Position."

### Skript 3: Abschluss-Frage

> "Wenn wir uns auf 47.500 Euro einigen und das Geld bis zum 30. dieses Monats fliesst, ist die Sache für Sie dann erledigt?"

### Skript 4: Walk-Away-Signal

> "Wir haben hier eine klare Linie. Wenn Sie nicht ueber die 35.000 Euro hinauskommen, werden wir Klage einreichen und sehen, wie das Gericht entscheidet."

## Stoerfeuer und Antwort-Bausteine

- **"Wir haben rechtsschutzversichert, uns ist der Prozess egal":** "Die Versicherung pruft Erfolgsaussichten. Wir koennen Ihnen gerne unser BVerfG-/BGH-Zitat zur Klage-Quote in diesen Faellen schicken."
- **"Wir warten erstmal das Urteil im Verfahren XY ab":** "Verjährung laeuft uns weg. Wir lassen den Schiedsspruch im Hintergrund mitlaufen."
- **"Ihre Mandantin hat sich rechtsmissbraeuchlich verhalten":** "Bitte praezisieren Sie - dann nehmen wir das ggf. in den Vergleich auf."

## Steuerliche Behandlung des Vergleichs

Im Bereich Allgemeines Verwaltungs- und Bauplanungsrecht oft uebersehen:

- Vergleichszahlung als Schadensersatz (in der Regel keine USt, EStG je nach Art).
- Vergleich ueber Lohn-/Gehaltsanspruch -> Lohnsteuer- und SV-Abzug pruefen.
- Vergleichszahlung als Anwaltshonorar -> ggf. USt.
- Erbrechtliche Abfindung -> ggf. ErbStG.
- Hinweis im Vergleich: "Die steuerliche Behandlung ist nicht Gegenstand dieser Vereinbarung und obliegt der eigenen Steuerberatung der Parteien."

## Mediation als Alternative

- Wenn Beziehung erhalten bleiben soll (Familie, Geschaeftspartner, Mieter und Vermieter).
- Mediator unparteiisch, kein Entscheidungstraeger - braucht Vertraulichkeitsvereinbarung.
- Mediations-Vergleich kann durch Notar oder Anwaltsvergleich vollstreckbar gemacht werden.
- Förderung MediationsG; in einigen Bundeslaendern Kostenuebernahme bei Familiensachen.

## Vollstreckbarkeit

- **Anwaltsvergleich nach § 796a ZPO:** anwaltlich beurkundeter Vergleich, mit Vollstreckungsklausel des Gerichts = Vollstreckungstitel.
- **Notarieller Vergleich:** als Schuldanerkenntnis mit Vollstreckungsunterwerfung.
- **Prozessvergleich:** § 794 Abs. 1 Nr. 1 ZPO, sofort vollstreckbar.
- **Schiedsvergleich:** Vollstreckbarerklaerung nach §§ 1054, 1060 ZPO.

## Vergleichs-Reichweite und Abgeltungsklausel

Klassische Stolperfalle in Allgemeines Verwaltungs- und Bauplanungsrecht:

- **Eng:** "Mit Zahlung sind alle Anspruche aus diesem Verfahren erledigt."
- **Mittel:** "Mit Zahlung sind alle Anspruche aus dem zugrundeliegenden Sachverhalt erledigt."
- **Weit:** "Mit Zahlung sind saemtliche bekannten und unbekannten Anspruche zwischen den Parteien erledigt." -> Vorsicht: Schadensersatz für noch nicht erkannte Schaeden ggf. weg.

## Leitentscheidungen Vergleichsstrategie

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Cross-Refs

- `erstgespraech-mandatsannahme` (im selben Plugin) für die Erstaufnahme und Streitwertgrundlage.
- `schriftsatzkern-substantiierung` (im selben Plugin) für den Fall, dass Vergleichsverhandlungen scheitern und Klage erforderlich wird.
<!-- AUDIT 27.05.2026
Aktion: Eintrag gelöscht.
-->

---

## Skill: `beamten-disziplinarverfahren`

_Beamten-Disziplinarverfahren führen oder verteidigen: Beamter hat Dienstvergehen begangen oder ist Dienstherr bei Einleitung Disziplinarverfahren: Beamten-Disziplinarverfahren führen oder verteidigen: Beamter hat Dienstvergehen begangen oder ist Dienstherr..._

# Beamten-Disziplinarverfahren führen oder verteidigen: Beamter hat Dienstvergehen begangen oder ist Dienstherr bei Einleitung Disziplinarverfahren


## Normenanker

Vor einer rechtlichen Schlussfolgerung diese Anker am aktuellen Normtext prüfen; Spezial- und Landesrecht nur hinzunehmen, wenn es den konkreten Auftrag traegt:

- `§ 28 Abs. 1 VwVfG` — Anhörung vor belastender Verwaltungsentscheidung.
- `§ 37 Abs. 1 VwVfG` — Bestimmtheit des Verwaltungsakts.
- `§ 39 Abs. 1 VwVfG` — Begruendungspflicht.
- `§ 40 VwVfG` — Ermessensausübung und Ermessensfehler.
- `§ 70 Abs. 1 VwGO` — Widerspruchsfrist, soweit Widerspruchsverfahren vorgesehen.
- `§ 74 Abs. 1 VwGO` — Klagefrist.
- `§ 80 Abs. 5 VwGO` — Eilrechtsschutz gegen Vollziehung.
- `§ 123 Abs. 1 VwGO` — einstweilige Anordnung.

Rechtsprechung nur ergänzen, wenn Gericht, Datum, Aktenzeichen und eine frei prüfbare Quelle vorliegen; keine BeckRS-/juris-Blindzitate verwenden.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Beamten-Disziplinarverfahren führen oder verteidigen: Beamter hat Dienstvergehen begangen oder ist Dienstherr bei Einleitung Disziplinarverfahren. Normen: BBG/BeamtStG, Bundesdisziplinargesetz BDG, Landesdisziplinargesetze. Prüfraster: Dienstvergehen-Tatbestand, Disziplinarmassnahmen (Verweis bis Entfernung aus Beamtenverhältnis), Anhörung, VG-Klage. Output Anhörungsschrift, Klageschrift, Verteidigungskonzept. Abgrenzung: Beamtenrecht materiell (Befoerderung, Besoldung) siehe mandat-triage-verwaltungsrecht; Anfechtungsklage allgemein siehe fachanwalt-verwaltungsrecht-anfechtungsklage.

### Beamten-Disziplinarverfahren

## 1) Rechtsgrundlagen

- BBG (Bundesbeamten-Gesetz)
- BeamtStG (Beamtenstatusgesetz)
- Bundes-DG / Landes-DG (Disziplinargesetze)

## 2) Dienstpflicht-Verletzungen

### Beispiele

- Verletzung Verschwiegenheits-Pflicht
- Verspaetete Diensterscheinung
- Drogen-Konsum
- Privat-Strafraten mit Bezug
- Beleidigungen
- Unerlaubte Nebentaetigkeit

### Schwere

- Leichter Verstoß: Verweis
- Mittel: Geldbuße / Kürzung Bezüge
- Schwer: Aberkennung Ruhegehalt
- Sehr schwer: Entfernung aus Dienst

## 3) Disziplinar-Maßnahmen

| Maßnahme | Pflicht-Voraussetzung |
|---|---|
| Verweis | leichter Verstoß |
| Geldbuße | bis 1 Monatsbezüge |
| Kürzung Bezüge | befristet bis 5 Jahre |
| Zurueckstufung | dauerhafte Demotion |
| Entfernung Dienst | schwere Verstöße |
| Aberkennung Ruhegehalt | bei Ruhe-Beamten |

## 4) Verfahren

### Schritt 1 — Voruntersuchung

- Dienstvorgesetzter prüft Vorwurf
- Anhörung Beamter

### Schritt 2 — Förmliches Disziplinarverfahren

- Eröffnung durch Dienstherr
- Ermittlungsfuhrer
- Beweisaufnahme

### Schritt 3 — Disziplinarmaßnahme

- Bescheid mit Begründung
- Bei schwerer Maßnahme: Klage VG Pflicht

### Schritt 4 — Klage VG

- Disziplinargericht (im VG-Gefuege)
- Disziplinarklage Dienstherr
- Vollumfaengliche Prüfung

## 5) Beamten-Strategie

### Sofort-Maßnahmen

- Schweige-Recht (in Disziplinar-Verfahren begrenzt)
- Anwalt einschalten
- Pflicht-Aussage nur zu Sachen, die nicht selbst-belasten

### Vorbereitung

- Akten-Einsicht
- Gegen-Beweise
- Milderungs-Faktoren (Krankheit, Belastung)

### Vergleichs-Möglichkeit

- Einstellung gegen Auflage
- Anwendung Mildere-Maßnahme

## 6) Schwerwiegende Folgen

### Bei Aberkennung Ruhegehalt

- Verlust Pensionsanspruch
- Sozialer Sturz

### Bei Entfernung aus Dienst

- Wegfall Versorgung
- Verlust Status
- Schwere persönliche Folge

## 7) Strafverfahren parallel

### Bei Straf-Tat

- Strafverteidigung im Vorder-Grund
- Disziplinar typisch erst nach Strafurteil
- Bindung Disziplinar-Verfahren an Strafurteil § 22 BDG

### Praxis

- Strafmilderung -> Disziplinar-Erleichterung
- Bei Freispruch: Disziplinar oft eingestellt

## 8) Workflow

### Phase 1 — Erstgespräch

- Vorwurfs-Aufnahme
- Verteidigungs-Strategie

### Phase 2 — Anhörung

- Schriftliche Stellungnahme
- Beweise

### Phase 3 — Bei Bescheid

- Klage Disziplinar-VG
- Frist meist 1 Monat

### Phase 4 — Verhandlung

- Vor Disziplinarkammer
- Beweisaufnahme
- Urteil

## 9) Honorar

- Anwaltsgebuehren nach RVG
- Bei Erfolg: Erstattung durch Dienstherr (begrenzt)
- Beamtenbund-Mitgliedschaft typisch hilfreich

## 10) Typische Fehler

1. **Unüberlegte Aussage** in Voruntersuchung
2. **Klage-Frist 1 Monat verpasst**
3. **Milderungs-Faktoren nicht dargelegt**
4. **Strafverfahren ohne Disziplinar-Beratung**

## 11) BVerwG-Linien

- BVerwG laufende Disziplinar-Rspr.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aktuelle BVerwG-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `fachanwalt-verwaltungsrecht-orientierung` — Triage
- `fachanwalt-strafrecht-orientierung` — bei parallelem Strafverfahren
- `widerspruch-oder-klage-erstpruefung` — bei VG-Triage

---

## Skill: `fa-vwgo-widerspruchsbescheid-abschleppen-oepnv`

_Fa VwGO Widerspruchsbescheid Abschleppen Oepnv: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung: Fa VwGO Widerspruchsbescheid Abschleppen Oepnv: ordnet Normen, Nutzerangaben, Fristen, Belege und ve..._

# Fa VwGO Widerspruchsbescheid Abschleppen Oepnv: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Fa VwGO Widerspruchsbescheid Abschleppen Oepnv: ordnet Normen, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung zu einer belastbaren Prüfung.

### Widerspruchsbescheid Abschleppkosten ÖPNV-Verkehrsbetrieb

## Kernsachverhalt

Ein Verkehrsbetrieb in der Rechtsform einer Anstalt des öffentlichen Rechts (z.B. die Berliner Verkehrsbetriebe AöR — BVG) ist durch Landesgesetz ermächtigt, Fahrzeuge eigenständig von Flächen des öffentlichen Personennahverkehrs umzusetzen und die Kosten dafür durch Gebührenbescheid gegenüber Halter oder Fahrer festzusetzen. Gegen den Gebührenbescheid kann der Adressat Widerspruch einlegen. Die Widerspruchsstelle des Verkehrsbetriebs (typischerweise die Rechtsabteilung) prüft Rechtmäßigkeit und Zweckmäßigkeit der Umsetzungsanordnung sowie der Gebührenfestsetzung und erlässt einen Widerspruchsbescheid. Dieser Skill begleitet die Widerspruchsstelle beim Entwurf des Bescheids — von der Aktenanalyse über die rechtliche Würdigung bis zur Tenorierung und Rechtsbehelfsbelehrung.

## Kaltstart-Rückfragen

1. Welcher Verkehrsbetrieb und welche Anstaltsform — BVG AöR Berlin, HHA Hamburger Hochbahn AG, MVG München (Tochter SWM), KVB Köln AöR, RNV Rhein-Neckar — und welche landesrechtliche Ermächtigungsgrundlage greift?
2. Welchen Bereich betraf die Umsetzung — Bushaltestellenkap mit Haltverbotszeichen, Sonderfahrstreifen Bus/Tram nach Zeichen 245 StVO, Straßenbahngleis im Mischverkehr, Wendeschleife, ÖPNV-Vorrangfläche, Behindertenparkplatz an einer Haltestelle?
3. Welche Beweismittel liegen vor — Lichtbilder mit Zeitstempel, Übersichtsfoto Beschilderung, Detailfoto Fahrzeugposition, Halterabfrage Kraftfahrt-Bundesamt, Umsetzungsprotokoll mit Uhrzeiten Anforderung/Eintreffen/Verladung/Verbringung, Quittung Abschleppunternehmer?
4. Wer ist Adressat des Gebührenbescheids — Halter oder Fahrer nach § 23 Abs. 5 MobG BE, Fahrer ermittelt oder unbekannt, Schuldnerauswahl im Bescheid begründet?
5. Welche Stadien der Umsetzung sind aktenkundig — vollzogene Umsetzung, begonnene Umsetzung (Verladung läuft), Leerfahrt (Abschleppwagen unterwegs, Fahrzeug aber nicht mehr vor Ort), vermiedene Umsetzung (Fahrer erscheint vor Verladebeginn)?
6. Welche Einwände bringt der Widerspruchsführer — keine konkrete Behinderung, falsche Beschilderung, Notstand, Fremdverschulden, Halter nicht Fahrer, fehlende Wartezeit, unverhältnismäßig hohe Gebühr, Anhörungsmangel, fehlende Begründung?
7. Liegt ein Antrag nach § 80 Abs. 4 VwGO auf Aussetzung der sofortigen Vollziehung vor — oder hat der Widerspruchsführer bereits gezahlt und begehrt Erstattung?
8. Gibt es Indizien für eine Mitverursachung durch den Verkehrsbetrieb selbst — Bus drängt sich an stehendes Fahrzeug heran, Verkehrsleiter wartet trotz erkennbar zurückkehrendem Fahrer nicht zu, Anforderung des Abschleppwagens vor Ablauf einer angemessenen Beobachtungszeit?
- **Was will der Bürger wirklich erreichen?** Manchmal geht es um eine Stundung, eine Ratenzahlung, eine Kulanzregelung oder die schlichte Anerkennung der Sondersituation — nicht jeder Widerspruch zielt auf vollständige Aufhebung. Eine teilabhelfende Entscheidung mit erläuternder Begründung kann nachhaltiger befrieden als eine formal korrekte Zurückweisung.

## Rechtsgrundlagen

### Ermächtigungsgrundlage Berlin

**§ 23 Abs. 2 Satz 1 Mobilitätsgesetz Berlin (MobG BE)** — Die Berliner Verkehrsbetriebe sind berechtigt, Fahrzeuge von Flächen des öffentlichen Personennahverkehrs einschließlich der dort befindlichen Gehwege und Radwege zu entfernen, soweit diese Flächen durch die den Verkehrsregeln oder Verkehrszeichen widersprechende Nutzung von Fahrzeugen blockiert werden.

**§ 23 Abs. 5 MobG BE** — Für die Umsetzung werden Gebühren erhoben. Schuldner ist der Halter oder der Fahrer des umgesetzten Fahrzeugs. Die Höhe der Gebühren bestimmt sich nach der Gebührenordnung des Senats.

**§ 6 Abs. 1 Gesetz über Gebühren und Beiträge Berlin (GebBtrG BE) vom 22.05.1957** — Gebühren werden für die Inanspruchnahme öffentlicher Einrichtungen und Anlagen erhoben. Die Höhe bemisst sich nach dem Kostendeckungsprinzip.

**Berliner Verkehrsbetriebe-Benutzungsgebührenordnung (BVGBenGebO)** — Rechtsverordnung des Senats. Aktueller Tarif (Stand 2024/2025) bei Fahrzeugen bis 3,5 t zulässiger Gesamtmasse:
- Vollzogene Umsetzung: 274,17 Euro
- Begonnene Umsetzung: 215,30 Euro
- Leerfahrt: 158,74 Euro
- Vermiedene Umsetzung: 76,45 Euro

Bei Fahrzeugen über 3,5 t zulässiger Gesamtmasse:
- Vollzogene Umsetzung: 650,32 Euro
- Begonnene Umsetzung: 409,96 Euro
- Leerfahrt: 195,45 Euro
- Vermiedene Umsetzung: 76,45 Euro

### Verfahrensrecht

**§ 68 Abs. 1 Satz 1 VwGO** — Vor Erhebung der Anfechtungsklage sind Rechtmäßigkeit und Zweckmäßigkeit des Verwaltungsakts in einem Vorverfahren nachzuprüfen.

**§ 73 Abs. 1 Satz 2 Nr. 1 VwGO** — Den Widerspruchsbescheid erlässt die nächsthöhere Behörde, soweit nicht durch Gesetz eine andere höhere Behörde bestimmt ist; bei Selbstverwaltungsangelegenheiten gilt § 73 Abs. 1 Satz 2 Nr. 3 VwGO — die Selbstverwaltungskörperschaft (hier: die AöR selbst) erlässt den Widerspruchsbescheid durch ihre dafür zuständige Stelle.

**§ 80 Abs. 2 Satz 1 Nr. 1 VwGO** — Die aufschiebende Wirkung entfällt bei der Anforderung von öffentlichen Abgaben und Kosten. Der Widerspruch gegen den Gebührenbescheid hemmt die Vollstreckung also nicht; § 80 Abs. 4 VwGO ermöglicht der Ausgangsbehörde die Aussetzung.

**§§ 28, 39 VwVfG** — Anhörung vor belastendem Verwaltungsakt und Begründungspflicht. Bei Abschleppfällen wird die Anhörung typischerweise erst im Widerspruchsverfahren nachgeholt — was nach § 45 Abs. 1 Nr. 3 VwVfG zulässig ist.

### Materiellrechtliche Verhältnismäßigkeit

**BVerwG, Urteil vom 09.04.2014 — 3 C 5.13** — Die Einleitung einer kostenpflichtigen Abschleppmaßnahme wegen eines verbotswidrig an einem Taxenstand abgestellten Fahrzeugs ist regelmäßig auch ohne Einhaltung einer bestimmten Wartezeit mit dem bundesverfassungsrechtlichen Verhältnismäßigkeitsgrundsatz vereinbar. Nach Maßgabe der konkreten Umstände kann es allerdings geboten sein, von Abschleppmaßnahmen abzusehen — etwa wenn eine Beeinträchtigung des reibungslosen Taxen- oder ÖPNV-Verkehrs ausgeschlossen ist — oder mit der Abschleppanordnung zu warten, wenn konkrete Anhaltspunkte dafür vorliegen, dass der Verantwortliche kurzfristig wieder am Fahrzeug erscheinen und es unverzüglich selbst entfernen wird.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Gebührenschuldner Halter oder Fahrer** — § 23 Abs. 5 MobG BE benennt Halter und Fahrer als mögliche Schuldner der Umsetzungsgebühren. Die Widerspruchsstelle muss deshalb sauber festhalten, wen der Ausgangsbescheid in Anspruch nimmt, ob der Fahrer bekannt und kurzfristig greifbar war und ob besondere Umstände gegen die Heranziehung des Halters sprechen. Allgemeines Polizei- und Ordnungsrecht bleibt für Verantwortlichkeit, Verhältnismäßigkeit und Ermessensausübung wichtig; § 7 StVG ist dafür keine eigenständige Analogiegrundlage.

## Prüfraster für den Widerspruchsbescheid

### 1. Formelle Rechtmäßigkeit des Ausgangsbescheids

- Zuständigkeit der BVG bzw. des Verkehrsbetriebs sachlich und örtlich gegeben?
- Schriftform und Begründung nach § 39 VwVfG vorhanden?
- Rechtsbehelfsbelehrung im Gebührenbescheid korrekt — Verweis auf Widerspruchsfrist und Adresse der Widerspruchsstelle?
- Anhörung nach § 28 VwVfG erfolgt oder nach § 28 Abs. 2 Nr. 1 VwVfG entbehrlich (Gefahr im Verzug)?
- Bekanntgabe und Zustellungsdatum dokumentiert?

### 2. Materielle Rechtmäßigkeit der Umsetzungsanordnung

- Verkehrsfläche tatsächlich eine ÖPNV-Fläche im Sinne von § 23 MobG BE — Bushaltestelle mit Zeichen 224, Sonderfahrstreifen Zeichen 245, Gleiskörper Tram?
- Beschilderung ordnungsgemäß sichtbar zum Zeitpunkt des Abstellens — keine Verdeckung durch Begrünung, kein verdrehtes Schild, keine zwischenzeitliche Aufstellung als mobiles Haltverbot ohne ausreichende Vorlaufzeit?
- Verstoß gegen Verkehrsregeln oder Verkehrszeichen tatsächlich gegeben?
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Auswahl des Gebührenschuldners ermessensfehlerfrei — Fahrer, wenn anwesend, bekannt und kurzfristig handlungsbereit; sonst regelmäßig Halter, soweit keine aktenkundigen Sonderumstände gegen die Heranziehung sprechen.

### 3. Rechtmäßigkeit der Gebührenfestsetzung

- Korrekter Tarif nach BVGBenGebO — Differenzierung nach zulässiger Gesamtmasse und nach Stadium (vollzogen/begonnen/Leerfahrt/vermieden)?
- Bei Leerfahrt mit mehreren Fahrzeugen in unmittelbarer Nähe: Kostenteilung beachtet?
- Bei vermiedener Umsetzung: Gebühr nur einmal angesetzt, nicht zusätzlich zur Leerfahrtpauschale?
- Adressat des Bescheids — Halter oder Fahrer — zutreffend ausgewählt und im Bescheid bezeichnet?

### 4. Sonderkonstellationen

- **Notstand oder atypische Notlage** — Akut lebensbedrohliche Lage, Geburtswehen, medizinischer Notfall: nicht schematisch über eine OWiG-Analogie lösen, sondern als Rechtfertigungs-, Verhältnismäßigkeits- und Ermessensfrage prüfen. Entscheidend ist, was der Verkehrsbetrieb vor Ort wusste oder bei ordentlicher Aktenlage hätte erkennen können.
- **Fremdverschulden Dritter** — Vorderfahrzeug fährt nicht weg, Mandant kann nicht aus dem Haltestellenbereich ausparken: in der Regel keine Entlastung, da der Halter das Fahrzeug überhaupt nicht im Haltestellenbereich hätte abstellen dürfen.
- **Mitverursachung des Verkehrsbetriebs** — Bus oder Einsatzleitung schaffen die konkrete Konfliktlage erst nachträglich oder dokumentieren widersprüchlich: dann nicht zivilrechtlich abkürzen, sondern Verhältnismäßigkeit, Ermessen, Aktenklarheit und Kostengerechtigkeit prüfen. Je nach Stadium kann eine Teilabhilfe oder ein Absehen von der Gebühr tragfähig sein.
- **Halter ≠ Fahrer** — Halter trägt die Beweislast für die Identität des Fahrers; benennt er den Fahrer substantiiert, prüft die Widerspruchsstelle, ob der Bescheid umgestellt oder aufgehoben wird.
- **Zugeparkter Bewohner** — Verkehrsbetrieb hat keinen Anlass, Anwohner bevorzugt zu behandeln; relevant nur, wenn das Fahrzeug schon vor Anbringung mobiler Beschilderung legal stand und die Vorlauffrist (regelmäßig 72 Stunden, Rspr. der OVG) nicht eingehalten wurde.

## Aufbau des Widerspruchsbescheids

### Kopf und Tenor

- Briefkopf der Widerspruchsstelle (z.B. Berliner Verkehrsbetriebe — Anstalt des öffentlichen Rechts, Rechtsabteilung Widerspruchsstelle, Holzmarktstraße 15-17, 10179 Berlin).
- Aktenzeichen Widerspruchsverfahren und Aktenzeichen Ausgangsbescheid.
- Bezeichnung als Widerspruchsbescheid.
- Anrede und Bezugnahme auf Widerspruch des Adressaten vom Datum.
- Tenor:
 - **Zurückweisung:** "Der Widerspruch wird zurückgewiesen. Die Kosten des Widerspruchsverfahrens trägt der Widerspruchsführer. Eine Gebühr für das Widerspruchsverfahren wird nicht erhoben."
 - **Teilabhilfe:** "Der Gebührenbescheid vom Datum wird in Höhe von Betrag aufgehoben. Im Übrigen wird der Widerspruch zurückgewiesen. Kosten Verhältnis."
 - **Vollabhilfe:** "Der Gebührenbescheid vom Datum wird aufgehoben. Die Berliner Verkehrsbetriebe tragen die notwendigen Aufwendungen des Widerspruchsführers. Eine Kostenfestsetzung erfolgt auf Antrag."

### Sachverhalt

Chronologische Schilderung in nüchternem Verwaltungsstil — Tatzeit, Tatort, Beschilderung, Anforderung des Abschleppwagens, Eintreffen, Stadium der Umsetzung, Erlass des Gebührenbescheids, Eingang des Widerspruchs, Vorbringen des Widerspruchsführers.

### Gründe

- **Zulässigkeit** des Widerspruchs: Statthaftigkeit, Form, Frist, Beschwer.
- **Begründetheit:**
 - Ermächtigungsgrundlage benennen (§ 23 Abs. 2, 5 MobG BE iVm § 6 GebBtrG BE iVm BVGBenGebO).
 - Subsumtion: ÖPNV-Fläche, verkehrswidrige Nutzung, Verhältnismäßigkeit.
 - Auseinandersetzung mit jedem Einwand des Widerspruchsführers — auch wenn der Einwand am Ende verworfen wird.
 - Bei (Teil-)Abhilfe: tragende Erwägungen für das Absehen oder die Reduzierung.
- **Kostenentscheidung** nach § 80 VwVfG oder landesrechtlichem Pendant.

### Rechtsbehelfsbelehrung

- Klage zum Verwaltungsgericht Berlin, Kirchstraße 7, 10557 Berlin.
- Klagefrist ein Monat ab Zustellung dieses Widerspruchsbescheids (§ 74 Abs. 1 VwGO).
- Form: schriftlich, zur Niederschrift des Urkundsbeamten oder elektronisch über das besondere elektronische Anwaltspostfach bzw. das elektronische Bürger- und Organisationenpostfach.
- Hinweis auf § 80 Abs. 2 Satz 1 Nr. 1 VwGO — Klage entfaltet keine aufschiebende Wirkung; Antrag auf Anordnung nach § 80 Abs. 5 VwGO bleibt möglich.

### Unterschrift und Schlussformel

- Name, Funktion, Datum.
- Hinweis: Der Bescheid ist auf elektronischem Weg nicht angreifbar, soweit landesrechtlich entsprechend geregelt.

## Output-Vorlage

```
BERLINER VERKEHRSBETRIEBE — Anstalt des öffentlichen Rechts
Rechtsabteilung — Widerspruchsstelle
Holzmarktstraße 15-17, 10179 Berlin

[Name und Anschrift Widerspruchsführer]

 Aktenzeichen Widerspruch: V-R 25/[...]
 Aktenzeichen Ausgangsbescheid: [...]
 Bearbeitung: [Name]
 Datum: [...]

WIDERSPRUCHSBESCHEID

In dem Widerspruchsverfahren des [...] gegen den Gebührenbescheid
der Berliner Verkehrsbetriebe vom [Datum] ergeht folgender Bescheid:

Tenor:
[je nach Ergebnis]

Sachverhalt:
[chronologisch]

Gründe:
I. Zulässigkeit
II. Begründetheit
 1. Ermächtigungsgrundlage
 2. Formelle Rechtmäßigkeit
 3. Materielle Rechtmäßigkeit
 4. Auseinandersetzung mit den Einwänden
III. Kosten

Rechtsbehelfsbelehrung:
[siehe oben]

[Unterschrift]
Widerspruchsstelle Rechtsabteilung
```

## Parallele Rechtsgrundlagen in anderen Ländern

- **Hamburg** — Hamburger Hochbahn AG arbeitet auf Grundlage des HmbSOG iVm Anordnung der Polizei bzw. Wegerecht; eine eigene Umsetzungsbefugnis vergleichbar zum Berliner MobG BE besteht in dieser Form nicht. Gebührenbescheide erlässt regelmäßig die Polizei oder das Bezirksamt.
- **München** — MVG arbeitet als Tochter der SWM GmbH zivilrechtlich; Abschleppmaßnahmen erfolgen durch Polizei oder Kommunalreferat.
- **Köln** — KVB AöR; Umsetzungen erfolgen durch die Verwaltung der Stadt Köln auf Grundlage des PolG NRW und der Sondernutzungssatzung.
- **Bundesweit** — Abschlepp- und Umsetzungskosten folgen außerhalb Berlins regelmäßig den jeweiligen landesrechtlichen Polizei-, Ordnungs- und Verwaltungsvollstreckungsregeln sowie kommunalen Zuständigkeitsmodellen. § 23 MobG BE ist eine Berliner Sonderregel für ÖPNV-Flächen und darf nicht ungeprüft auf Hamburg, München, Köln oder andere Länder übertragen werden.

## Beispieltestakte

Eine vollständige Arbeitsakte mit sechs Fallvarianten und allen Ausgangsdokumenten liegt unter `testakten/bvg-widerspruchsstelle-abschleppen-mobg/`. Die Akte enthält keine Erwartungshorizonten — sie soll mit diesem Skill erst zum Widerspruchsbescheid verarbeitet werden.

## Hinweise zur praktischen Bescheidung

- **Tonalität** — Verwaltungsdeutsch, nüchtern, keine Belehrung des Bürgers. Bei Sondersituationen (Notstand, Trauerfall, Krankenhausnotfall) sachlich anerkennen, auch wenn die Entscheidung im Ergebnis zurückweisend ist.
- **Substantiierung** — Jeden Einwand des Widerspruchsführers ausdrücklich aufgreifen und mit einem Satz erwidern. Pauschale Floskeln ("nicht substantiiert") sind anfechtungsgerichtsfest nur, wenn die Begründung tatsächlich pauschal war.
- **Beweiswürdigung** — Lichtbilder mit Zeitstempel sind das stärkste Beweismittel; Aussagen des Verkehrsleiters sind protokollarisch zu untermauern; Einlassungen des Halters sind ernst zu nehmen, aber daran zu messen, was die Akte hergibt.
- **Verhältnismäßigkeit als Stellschraube** — Wenn ein vollständiges Absehen rechtlich nicht tragfähig ist, kann eine Reduzierung von vollzogener auf begonnene Umsetzung oder von begonnener auf vermiedene Umsetzung in atypischen Fällen angemessen sein.
- **Kostendeckungsprinzip** — Die Höhe der Gebühr ist durch die Rechtsverordnung gebunden; eine Reduzierung "nach Billigkeit" außerhalb der Verordnung ist nur über die Aufhebung des Bescheids und ein Absehen von der Festsetzung möglich, nicht durch freie Festsetzung eines geringeren Betrags.

## Quellen

- § 23 Mobilitätsgesetz Berlin — [gesetze.berlin.de](https://gesetze.berlin.de/bsbe/document/jlr-MobGBEpP23)
- Gesetz über Gebühren und Beiträge Berlin (GebBtrG BE) vom 22.05.1957
- Berliner Verkehrsbetriebe-Benutzungsgebührenordnung (BVGBenGebO) — [gesetze.berlin.de](https://gesetze.berlin.de/bsbe/document/jlr-BVGBenGebOBEV1Anlage)
- BVG Busspurberäumung — [bvg.de](https://www.bvg.de/de/service-und-kontakt/busspurbetreuung)
- BVerwG, Urteil vom 09.04.2014 — 3 C 5.13 — [bverwg.de](https://www.bverwg.de/090414U3C5.13.0)
- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- VwGO §§ 68 bis 80 — [gesetze-im-internet.de](https://www.gesetze-im-internet.de/vwgo/__73.html)

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

