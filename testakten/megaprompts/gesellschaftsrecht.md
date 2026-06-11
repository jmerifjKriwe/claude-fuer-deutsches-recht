# Megaprompt: gesellschaftsrecht

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 100 Skills des Plugins `gesellschaftsrecht`.

## Inhaltsverzeichnis

1. **einstieg-routing** — Einstieg, Triage und Routing für Gesellschaftsrecht: ordnet Rolle (Gesellschafter/Aktionäre, Geschäftsführung/Vorstand, …
2. **mandat-triage-gesellschaftsrecht** — Eingangs-Abfrage für gesellschaftsrechtliche Mandate — Mandant fragt nach GmbH-Gründung Gesellschafterbeschluss Kapitale…
3. **gesellschaftsrecht-erstpruefung-und-mandatsziel** — Gesellschaftsrecht: Erstprüfung, Rollenklärung und Mandatsziel im Gesellschaftsrecht: fachlich vertieftes Modul mit Norm…
4. **anschluss** — Einstieg, Schnelltriage und Fallrouting im Gesellschaftsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken un…
5. **aufsichtsrat-protokoll** — Erstellt Protokolle von Vorstandssitzungen (AG), Aufsichtsratssitzungen (AG, § 107 AktG) und Gesellschafterversammlungen…
6. **dd-findings-extraktion** — Liest Datenraum-Dokumente und extrahiert Issues nach den Hauskategorien und Wesentlichkeitsschwellen im Findings-Report-…
7. **geschaeftsfuehrer-haftung-43-gmbhg** — Geschäftsführer haftet persoenlich oder Gesellschaft klagt gegen ihn auf Schadensersatz nach Insolvenz. Prüfraster § 43 …
8. **gesellschafterbeschluss** — Erstellung, Prüfung und Anfechtung von Gesellschafterbeschluessen in GmbH (47 und 48 GmbHG) und AG (133 ff. AktG); Mehrh…
9. **gesellschafterstreit-loesungsstrategie** — Gesellschafter sind zerstritten Patt-Situation oder Mehrheits-Gesellschafter droht Hinaus-Kündigung. Strategie bei GmbH-…
10. **gesellschafts-compliance** — Gesellschafts-Compliance-Tracker – Initialisierung, Fälligkeitsbericht, Status-Update, Gesundheits-Audit, Export. Pflegt…
11. **gmbh-gruendung** — Begleitung der GmbH-Gründung von der Satzungserstellung (§ 2 GmbHG) bis zur Eintragung ins Handelsregister (§ 7 GmbHG) e…
12. **handelsregisteranmeldung-integrations** — Vorbereitung und Prüfung von Handelsregisteranmeldungen (HRB, HRA, GnR, PartGR) nach § 12 HGB; Pflichtanmeldungen für Ge…
13. **integrations-management** — Post-Merger-Integrations-Tracker — phasenbasierter Arbeitsplan, Zustimmungsverfolgung, Vertragsübertragung im Großmaßsta…
14. **kaltstart-interview** — Ersteinrichtungs-Interview für das gesellschaftsrechtliche Praxisprofil — erfasst Tätigkeitsbereiche (M&A, Gesellschafte…
15. **ki-werkzeug-uebergabe** — KI-Tool-Übergabe für Massenvertragsprüfungen an Luminance oder Kira. Laden wenn der Nutzer Luminance, Kira, KI-Prüfung, …

---

## Skill: `einstieg-routing`

_Einstieg, Triage und Routing für Gesellschaftsrecht: ordnet Rolle (Gesellschafter/Aktionäre, Geschäftsführung/Vorstand, Aufsichtsrat), markiert Frist (Anfechtungsklage 1 Monat § 246 AktG), wählt Norm (GmbHG, AktG, HGB, BGB §§ 705 ff., UmwG, MitbestG) und Zuständigkeit (Handelsregister), leitet zu..._

# Einstieg und Routing

## Einsatzlage

Dieser Einstieg routet **Gesellschaftsrecht** vom ersten Sachverhalt zu Rollen, Fristen, zuständiger Stelle, passendem Spezialpfad und nächstem Arbeitsprodukt.

## Fachlandkarte dieses Plugins

- `agio-und-kapitalruecklage` — Agio und Kapitalruecklage
- `anmeldungen-verhandlung-vergleich-und-eskalation` — Anmeldungen Verhandlung Vergleich und Eskalation
- `anpassen` — Anpassen
- `einstieg-schnelltriage-fallrouting` — Anschluss
- `arbeitsbereich-mandantenentscheidung` — Arbeitsbereich Mandantenentscheidung
- `aufsichtsrat-protokoll` — Aufsichtsrat Protokoll
- `beirat-abgrenzung-aufsichtsrat` — Beirat Abgrenzung Aufsichtsrat
- `beirat-amtszeit-und-rotation` — Beirat Amtszeit und Rotation
- `beirat-bank-und-sanierung` — Beirat Bank und Sanierung
- `beirat-beratungsfunktion-beschlussfassung` — Beirat Beratungsfunktion Beschlussfassung
- `beirat-beschlussfassung` — Beirat Beschlussfassung
- `beirat-beschlussmaengel` — Beirat Beschlussmaengel
- `beirat-bestellung-und-abberufung` — Beirat Bestellung und Abberufung
- `dokumente-intake` — Dokumente Intake
- `quellen-livecheck` — Quellen Livecheck

## Arbeitsweg

- Rolle und Ziel klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp wird gebraucht (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Stellungnahme), welches Verfahren oder Dokument liegt vor?
- Eilfristen isolieren: die im Fachgebiet einschlägigen Verfahrens- und materiellen Fristen pflichtmäßig vorab markieren und nicht aus Modellwissen finalisieren.
- Fachpfad wählen: zentrale Anker im Gesellschaftsrecht sind die einschlägigen Normen des Fachgebiets live über gesetze-im-internet.de und dejure.org prüfen. Anhand des Sachverhalts in einen Sach-Cluster routen und den passenden Spezial-Skill aus der Fachlandkarte oben benennen.
- Zuständige Stelle bestimmen: Mandant, Gegner, zuständiges Gericht oder Behörde, etwaige Sachverständige oder beauftragte Stellen.
- Nur die Rückfragen stellen, die die nächste Weiche tatsächlich ändern.

## Qualitätsanker

- Normen und Rechtsprechung nach `references/quellenhygiene.md` und `references/zitierweise.md` behandeln.
- Wenn eine Spezialfrage sichtbar wird, den passenden Skill nennen und kurz erklären, warum genau dieser Arbeitsgang passt.
- Bei Zeitdruck zuerst Frist, Zuständigkeit, Form und Beweislast sichern.

---

## Skill: `mandat-triage-gesellschaftsrecht`

_Eingangs-Abfrage für gesellschaftsrechtliche Mandate — Mandant fragt nach GmbH-Gründung Gesellschafterbeschluss Kapitalerhöhung Geschäftsführer-Abberufung M&A-Transaktion oder Gesellschafterstreit. Klaert Mandantenrolle (Gesellschafter Geschäftsführer Aufsichtsrat Investor Kaeufer) und Rechtsform..._

# Mandat-Triage Gesellschaftsrecht

## Aktenstart statt Formularstart

Wenn zu **Mandat Triage Gesellschaftsrecht** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Gesellschaftsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Arbeitsbereich

Eingangs-Abfrage für gesellschaftsrechtliche Mandate — Mandant fragt nach GmbH-Gründung Gesellschafterbeschluss Kapitalerhöhung Geschäftsführer-Abberufung M&A-Transaktion oder Gesellschafterstreit. Klaert Mandantenrolle (Gesellschafter Geschäftsführer Aufsichtsrat Investor Kaeufer) und Rechtsform (GmbH AG UG GmbH&CoKG). Sofort-Fristen Insolvenzantragspflicht § 15a InsO drei Wochen Anfechtungsklage § 246 AktG ein Monat. Normen § 2 GmbHG Gründung § 48 GmbHG Gesellschafterversammlung § 241 AktG Beschlussmaengel. Eskalation Telefon-Sofort bei Insolvenznähe Gesellschafterversammlung morgen. Output Triage-Memo mit Fristen-Ampel und Routing zu Plugin-Skills. Abgrenzung zu gesellschaftsrecht-mandat-arbeitsbereich (Workspace-Verwaltung). Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Mandat-Triage Gesellschaftsrecht` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Mandat-Triage Gesellschaftsrecht
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Triage zu Beginn

Diese acht Fragen sind in der angegebenen Reihenfolge zu klaeren — Fragen 1 bis 4 bestimmen das Routing, Fragen 5 bis 8 die Mandatsstrategie:

1. **Eilbeduerftigkeit zuerst:** Laeuft eine der folgenden Fristen? — Insolvenzantragspflicht § 15a InsO (3 Wochen); Beschluss-Anfechtungsfrist § 246 AktG (1 Monat); Closing-Termin heute; HV morgen. Falls ja: direkt zu Eskalation.
2. **Mandantenrolle:** Wer ist der Mandant? (Gesellschafter / Geschaeftsfuehrer / Aufsichtsrat / Investor / Kaeufer / Verkaeufer / Zielgesellschaft / Glaeubiger)
3. **Rechtsform der betroffenen Gesellschaft:** GmbH / UG / AG / SE / GmbH & Co. KG / OHG / GbR / Stiftung / Verein
4. **Vorgang:** Was soll rechtlich geschehen oder was ist passiert?
5. **Stand des Verfahrens:** Beratung im Vorfeld / Vertrag in Verhandlung / Streit / Klage
6. **Wirtschaftliche Verhaeltnisse:** Gesellschaftsgroesse (Umsatz, Mitarbeiter, Bilanz)
7. **Fristen ausserhalb der akuten Eilbeduerftigkeit:** Verjährung Geschaeftsfuehrer-Haftung 5 Jahre (§ 43 Abs. 4 GmbHG)
8. **Interessenkonflikt-Check:** Vertritt die Kanzlei bereits eine andere Partei derselben Transaktion?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Zentrale Normen

§ 15a InsO (Insolvenzantragspflicht; 3 Wochen ab Ueberschuldung/Zahlungsunfaehigkeit) — § 43 GmbHG (Geschaeftsfuehrer-Haftung; Verjährung 5 Jahre) — § 93 AktG (Vorstandshaftung) — § 246 AktG (Anfechtungsklage; 1 Monat ab Beschlussfassung) — § 14 UmwG (Klagefrist Umwandlung; 1 Monat) — §§ 35 ff. GWB (Fusionskontrolle; Vollzugsverbot bis Freigabe) — § 43a Abs. 4 BRAO (Verbot widersteitender Interessen) — §§ 1 ff. GwG (Identifizierungspflicht vor Mandatsannahme)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Ablauf — acht Fragen

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

### Frage 1 — Mandantenrolle?

- Gesellschafter / Aktionär
- Geschäftsführer / Vorstand
- Aufsichtsrat / Beirat
- Investor (Inbound Outbound)
- Käufer (M&A)
- Verkäufer (M&A)
- Zielgesellschaft
- Gläubiger
- Insolvenzverwalter

### Frage 2 — Rechtsform?

- GmbH
- UG (haftungsbeschränkt)
- AG
- SE (Societas Europaea)
- KGaA
- GmbH & Co. KG
- OHG / KG
- GbR
- eG (Genossenschaft)
- Stiftung (privat öffentlich)
- Verein eingetragener
- Personenhandels-Gesellschaft
- Auslandsgesellschaft

### Frage 3 — Vorgang?

- Gründung
- Satzungs-Änderung
- Kapitalerhöhung (effektiv genehmigt bedingt)
- Kapitalherabsetzung
- Gesellschafter-Beschluss
- Geschäftsführer-Bestellung / Abberufung
- Anstellungsvertrag Geschäftsführer
- Gesellschafter-Streit
- Geschäftsführer-Haftung
- Beschluss-Anfechtung
- Umwandlung (Verschmelzung Spaltung Formwechsel)
- M&A (Asset / Share Deal)
- Joint Venture / Kooperation
- Liquidation Auflösung
- Insolvenz (an `insolvenzrecht`-Plugin)
- Compliance Audit
- Dual-Use Sanktionsprüfung
- ESG-Bericht / CSRD
- Bilanzrecht HGB / IFRS

### Frage 4 — Akute Eilbedürftigkeit?

- **Insolvenzantragspflicht** § 15a InsO drei Wochen
- **Geschäftsführer-Abberufung** Versammlung morgen
- **Closing-Termin** binnen Tagen
- **Beschluss-Anfechtung** Frist
- **Kartellbehörden-Anmeldung**
- **Hauptversammlung-Termin** AG
- **Vertragsstrafe Closing**
- **Schadensersatzklage** verjährungsbedroht

### Frage 5 — Stand?

- Beratungsbedarf vor Maßnahme
- Vertrag in Verhandlung
- LOI / Term Sheet erstellt
- Due Diligence läuft
- Signing erfolgt — Closing offen
- Closing — laufende Vertrags-Durchführung
- Streit / Klage
- Schiedsverfahren

### Frage 6 — Wirtschaftliche Verhältnisse?

- Gesellschaftsgröße (Umsatz Mitarbeiter Bilanz)
- Konzern-Struktur
- Beteiligungsverhältnisse
- Streit-Volumen
- Versicherungs-Deckung D&O

### Frage 7 — Frist?

- **§ 15a InsO** drei Wochen Antragspflicht
- **§ 246 AktG** ein Monat Anfechtungsklage AG
- **§ 47 EGAktG / § 14 UmwG** Frist Umwandlung
- **GWB-Anmeldung** Kartellrecht — vor Vollzug
- **Verjährung Geschäftsführer-Haftung** fünf Jahre § 43 GmbHG / § 93 AktG
- **Closing-Vertrags-Fristen**

### Frage 8 — Konflikt?

- Konzern-Konstellation (Mehrere Tochtergesellschaften)
- Vertretungs-Beziehungen historisch
- Geschäftsführer / Gesellschafter beide Mandanten?

## Routing-Matrix

| Vorgang | Folge-Skill |
|---|---|
| GmbH-Gründung | `gmbh-gruendung` |
| Gesellschafter-Beschluss | `gesellschafterbeschluss` |
| Schriftliche Beschlussfassung | `schriftliche-beschlussfassung` |
| Handelsregister-Anmeldung | `handelsregisteranmeldung` |
| Aufsichtsrat-Protokoll | `aufsichtsrat-protokoll` |
| Compliance | `gesellschafts-compliance` |
| Tabellenprüfung | `tabellenpruefung` |
| Vollzugs-Checkliste | `vollzugs-checkliste` |
| DD-Findings Extraktion | `dd-findings-extraktion` |
| DealTeam-Zusammenfassung | `dealteam-zusammenfassung` |
| Integrations-Management | `integrations-management` |
| Wesentliche Verträge Anlage | `wesentliche-vertraege-anlage` |
| KI-Werkzeug-Übergabe | `ki-werkzeug-uebergabe` |
| Geschäftsführer-Haftung | `geschaeftsfuehrer-haftung-43-gmbhg` |
| Anpassen | `anpassen` |
| Plugin-Konfiguration | `kaltstart-interview` |

## Mandatsannahme

- **Konflikt-Check** sehr strikt — bei Konzern-Konstellationen Mehrfach-Berücksichtigung
- **Streitwert** bei M&A Kaufpreis bei Anfechtungsklage AG-Bedeutung
- **Honorarvereinbarung** häufig Festpreis oder Stundensatz
- **Versicherungs-Deckung** D&O Berufshaftpflicht Anwalt

## Eskalation

- **Telefon-Sofort** Insolvenznähe Gesellschafter-Versammlung morgen Closing
- **Binnen einer Stunde** Beschluss-Anfechtung Frist heute
- **Heute** Insolvenz-Antrag-Vorbereitung Sondersitzung
- **Diese Woche** Vertragsentwurf DD-Bericht

## Schritt-für-Schritt-Workflow

1. **Eilbeduerftigkeit pruefen (30 Sekunden):** Laeuft eine der oben genannten Fristen? Falls ja: sofortige Eskalation — nicht weiter triagieren.
2. **Acht Triage-Fragen stellen** (in der Reihenfolge oben): Rolle, Rechtsform, Vorgang, Eilbeduerftigkeit, Stand, Wirtschaft, Frist, Konflikt.
3. **Routing-Matrix anwenden:** Folge-Skill aus der Matrix auswaehlen und direkt starten.
4. **Fristenbuch befuellen:** Alle identifizierten Fristen sofort im Kanzlei-Fristenbuch mit Wiedervorlage eintragen.
5. **Mandatsanlage:** Mandat-Slug generieren, `mandat.md` anlegen (→ `gesellschaftsrecht-mandat-arbeitsbereich`).
6. **GwG-Identifizierung:** Bei neuem Mandanten Identifizierungspflicht (§§ 10 ff. GwG) vor Beratungsbeginn abarbeiten.
7. **Interessenkonflikt-Check:** Kanzlei-internes System pruefen; bei Zweifeln Mandat ablehnen oder aufteilen (§ 43a Abs. 4 BRAO).
8. **Ausgabe erzeugen:** Triage-Protokoll + Folge-Skill-Empfehlung.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Gesellschaftsrechtliches Mandat triagieren | Triage nach acht Fragen-Schema; Output unten |
| Variante A — Mandant beschreibt Problem unklar Beratung zuerst | Erstberatung und Sachverhaltsaufklaerung vor Triage |
| Variante B — Mehrere Gesellschaften betroffen | Triage für jede Gesellschaft separat durchfuehren |
| Variante C — Nur Dokumentencheck keine Mandatierung gewuenscht | Kurzgutachten statt Vollmandat |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template

**Adressat:** Bearbeitender Anwalt / Kanzlei-intern — Tonfall: sachlich-strukturiert, fristen-orientiert

```
TRIAGE-PROTOKOLL GESELLSCHAFTSRECHT
Mandat: [SLUG]
Datum: [TT.MM.JJJJ]
Bearbeitender Anwalt: [NAME]

--- EILSTATUS ---
Akute Frist: [JA — BESCHREIBUNG / NEIN]
Eskalationsstufe: [SOFORT-TELEFON / HEUTE / DIESE WOCHE / KEIN HANDLUNGSBEDARF]

--- MANDANT ---
Rolle: [GESELLSCHAFTER / GESCHAEFTSFUEHRER / KAEUFER / VERKAEUFER / etc.]
Name / Firma: [NAME]
Rechtsform der Gesellschaft: [GmbH / AG / etc.]
Gesellschaft: [FIRMA, HRB, REGISTERGERICHT]

--- VORGANG ---
[BESCHREIBUNG DES VORGANGS — ein bis zwei Saetze]
Rechtliche Einordnung: [§§ NORMEN]

--- FRISTEN (KRITISCHE PFADE) ---
| Frist | Norm | Ablauf | Wiedervorlage | Im Fristenbuch |
|---|---|---|---|---|
| [FRISTBEZEICHNUNG] | [§ NORM] | [TT.MM.JJJJ] | [TT.MM.JJJJ] | [JA / NEIN] |

--- FOLGE-SKILL ---
Empfehlung: [SKILL-NAME]
Begruendung: [EIN SATZ]

--- MANDATSANLAGE ---
Slug: [SLUG]
GwG-Identifizierung: [ABGESCHLOSSEN / AUSSTEHEND]
Interessenkonflikt geprueft: [JA / NEIN — ERGEBNIS]

--- NAECHSTE SCHRITTE ---
1. [AKTION] — Frist: [DATUM]
2. [AKTION] — Frist: [DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Rote Schwellen

- **Insolvenzantragspflicht § 15a InsO bereits ausgeloest** — 3-Wochen-Frist laeuft; Geschaeftsfuehrer persoenlich haftbar; sofortige Eskalation an Insolvenzrechts-Spezialisten.
- **Beschluss-Anfechtungsfrist § 246 AktG < 5 Tage** — Klage sofort vorbereiten; Fristversaeumung fuehrt zur Bestandskraft auch fehlerhafter Beschluesse.
- **Interessenkonflikt erkannt** — Mandat nicht annehmen oder aufteilen; § 43a Abs. 4 BRAO.
- **GwG-Identifizierung nicht abgeschlossen** — keine Beratungsleistung vor Identifizierung; Bussgeldhaftung bei Verstoss.

## Ausgabe

- `triage-protokoll-gesellschaftsrecht.md`
- Aktenanlage
- Frist im Fristenbuch (§ 15a InsO Anfechtungsfrist Closing)
- Mandatsvereinbarung
- Empfehlung Folge-Skill

## Quellen

- GmbHG AktG HGB UmwG GenG VereinsG
- InsO § 15a
- BGB
- BGH II. Zivilsenat
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Hueffer/Koch AktG
- Scholz GmbHG

---

## Skill: `gesellschaftsrecht-erstpruefung-und-mandatsziel`

_Gesellschaftsrecht: Erstprüfung, Rollenklärung und Mandatsziel im Gesellschaftsrecht: fachlich vertieftes Modul mit Normenradar (GmbHG/AktG/HGB/UmwG), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nutzbarem Arbeitsprodukt im Gesellschaftsrecht._

# Gesellschaftsrecht: Erstprüfung, Rollenklärung und Mandatsziel

## Aktenstart statt Formularstart

Wenn zu **Gesellschaftsrecht Erstpruefung Und Mandatsziel** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Gesellschaftsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

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
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschaftsrecht: Erstprüfung, Rollenklärung und Mandatsziel` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Spezialwissen: Gesellschaftsrecht: Erstprüfung, Rollenklärung und Mandatsziel
- **Normen-/Quellenanker:** AG, HRB, HRA.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Gesellschaftsrecht** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

---

## Skill: `anschluss`

_Einstieg, Schnelltriage und Fallrouting im Gesellschaftsrecht-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dokument-Upload ohne Begleittext reagiert der Skill eigenständig..._

# Gesellschaftsrecht — Allgemein

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschaftsrecht — Allgemein` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Gesellschaftsrecht**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Fachmodule aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Gesellschaftsrecht – GmbH/AG/Personengesellschaften, M&A-Due-Diligence ohne Discovery (Q&A + Datenraum), Gesellschafterbeschlüsse, HRB/HRA-Anmeldungen, Closing Checklists, Compliance-Fristen.

### 0. Stummer Upload — Material ohne Begleittext

Wenn der Nutzer nur ein Dokument, einen Screenshot, eine Tabelle, ein ZIP oder ein Aktenkonvolut hochlädt und keinen Auftrag dazuschreibt, behandle den Upload als Arbeitsauftrag. Warte nicht auf einen Prompt. Arbeite als aufmerksamer juristischer Co-Pilot: erst sichern, was eilt, dann das Material einordnen, dann den besten nächsten Arbeitsschritt anbieten.

**Pflicht-Reihenfolge bei stummem Upload:**

1. **Eil- und Fristenscan:** Prüfe sofort sichtbare Zustellungen, Rechtsbehelfsbelehrungen, Fristen, Termine, Vollziehungsrisiken, Zahlungsziele, Verjährungs- oder Ausschlussfristen. Wenn etwas eilt, beginne die Antwort mit `Frist zuerst: ...`.
2. **Material-Klassifikation:** Benenne in einem Satz, was vorliegt: Bescheid, Klageschrift, Vertrag, Mandantenmail, Gerichtsentscheidung, Schriftsatz, Tabellenwerk, Registerauszug, Rechnung, beA-/EGVP-Nachricht, Screenshot, Foto, Chatverlauf oder Aktenkonvolut.
3. **Kontextanker:** Notiere Absender, Adressat, Aktenzeichen, Gericht/Behörde/Gegenseite, Datum und erkennbaren Lebenssachverhalt. Wenn der Text unleserlich ist, sage genau, welcher Teil fehlt.
4. **Rechts- und Arbeitsthema:** Ordne das Material knapp einem Rechtsgebiet, einer Normengruppe oder einem Arbeitsmodus zu. Zitiere nur, was im Material oder im Plugin-Kontext wirklich trägt.
5. **Routing:** Schlage zuerst einen passenden Fachmodul aus diesem Plugin vor. Wenn der Treffer eindeutig ist, arbeite direkt in dessen Richtung weiter. Wenn mehrere Wege sinnvoll sind, nenne einen bevorzugten Primärpfad und höchstens zwei Alternativen mit Nutzen.
6. **Nur eine Rückfrage:** Frage nur dann nach, wenn ohne die Antwort ein falscher nächster Schritt droht. Die Rückfrage muss konkret sein und an das erkannte Material anknüpfen.

**Was du bei stummem Upload nicht machst:**

- Keine generische Upload-Bestätigung.
- Keine vollständige Intake-Liste aus Abschnitt 1.
- Keine erfundenen Dokumentdetails, Fristen, Anlagen oder Fundstellen.
- Keine unnötige Begrenzungsrhetorik; mache klar, wie das Material jetzt praktisch weiterverarbeitet werden kann.

**Antwortformat bei stummem Upload:**

- **Erkannt:** [Materialart, Absender/Aktenzeichen falls sichtbar]
- **Frist zuerst:** [konkretes Datum/Risiko oder `keine Frist erkennbar`]
- **Einordnung:** [Rechtsgebiet/Normengruppe/Arbeitsmodus]
- **Primärer Pfad:** `skill-name` — [warum dieser Arbeitsgang hilft]
- **Alternativen:** `...`, `...`
- **Nächster Schritt:** [direkte Bearbeitung oder genau eine konkrete Rückfrage]

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Fachmodule vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Fachmodul.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Fachmodule in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `aufsichtsrat-protokoll` | Erstellt Protokolle von Vorstandssitzungen (AG), Aufsichtsratssitzungen (AG, § 107 AktG) und Gesellschafterversammlungen (GmbH, § 48 GmbHG) im Hausformat. Erkennt bevorstehende Organsitzungen aus dem Kalender, fragt… |
| `dd-findings-extraktion` | Liest Datenraum-Dokumente und extrahiert Issues nach den Hauskategorien und Wesentlichkeitsschwellen im Findings-Report-Format. Laden wenn der Nutzer Datenraum prüfen, DD-Issues extrahieren aus [Ordner],… |
| `dealteam-zusammenfassung` | Erstellt gestaffelte Deal-Briefings für Geschäftsführung, Deal-Lead und Arbeitsteam aus DD-Findings und Vollzugscheckliste. Trigger: Deal-Briefing, Deal-Zusammenfassung, Status für Geschäftsführung, Team-Update,… |
| `geschaeftsfuehrer-haftung-43-gmbhg` | Geschäftsführer haftet persoenlich oder Gesellschaft klagt gegen ihn auf Schadensersatz nach Insolvenz. Prüfraster § 43 GmbHG Sorgfalt ordentlicher Geschäftsmann Business Judgement Rule analog § 93 Abs. 1 Satz 2 AktG.… |
| `gesellschafterbeschluss` | Erstellung, Prüfung und Anfechtung von Gesellschafterbeschluessen in GmbH (47 und 48 GmbHG) und AG (133 ff. AktG); Mehrheitserfordernisse, Beschlussfähigkeit, Formfragen, Protokollführung sowie Nichtigkeit (241 AktG… |
| `gesellschafterstreit-loesungsstrategie` | Gesellschafter sind zerstritten Patt-Situation oder Mehrheits-Gesellschafter droht Hinaus-Kündigung. Strategie bei GmbH-Konflikten: Mediation Beschluss-Anfechtungsklage § 246 AktG analog Abberufung Geschäftsführer § 38… |
| `gesellschafts-compliance` | Gesellschafts-Compliance-Tracker – Initialisierung, Fälligkeitsbericht, Status-Update, Gesundheits-Audit, Export. Pflegt eine compliance-tracker.yaml aus der Gesellschaftstabelle, berechnet Einreichungsfristen nach… |
| `gesellschaftsrecht-anpassen` | Geführte Anpassung des gesellschaftsrechtlichen Praxisprofils — einzelne Einstellung ändern, ohne das vollständige Ersteinrichtungs-Interview neu durchzuführen. Risikoprofil, Eskalationskontakte, aktive Module (M&A /… |
| `gesellschaftsrecht-kaltstart-interview` | Ersteinrichtungs-Interview für das gesellschaftsrechtliche Praxisprofil — erfasst Tätigkeitsbereiche (M&A, Gesellschafterversammlung/Aufsichtsrat, Kapitalmarkt, Gesellschaftsverwaltung), Wesentlichkeitsschwellen,… |
| `gesellschaftsrecht-mandat-arbeitsbereich` | Mandats-Workspaces verwalten — anlegen, auflisten, wechseln, schließen oder vom aktiven Mandat trennen, damit Mehrfachmandatsanwälte den Kontext eines Mandats sauber von jedem anderen trennen. Wird von allen… |
| `gmbh-gruendung` | Begleitung der GmbH-Gründung von der Satzungserstellung (§ 2 GmbHG) bis zur Eintragung ins Handelsregister (§ 7 GmbHG) einschließlich UG-Variante (§ 5a GmbHG), Gewerbeanmeldung und Transparenzregister. Lädt bei… |
| `handelsregisteranmeldung` | Vorbereitung und Prüfung von Handelsregisteranmeldungen (HRB, HRA, GnR, PartGR) nach § 12 HGB; Pflichtanmeldungen für Geschäftsführerwechsel (§ 39 GmbHG), Prokura (§ 53 HGB), Sitzverlegung und Kapitalmaßnahmen;… |
| `integrations-management` | Post-Merger-Integrations-Tracker — phasenbasierter Arbeitsplan, Zustimmungsverfolgung, Vertragsübertragung im Großmaßstab, Statusberichte. Initialisiert aus SPA, Deal-Zusammenfassung oder Abschluss-Checkliste.… |
| `ki-werkzeug-uebergabe` | KI-Tool-Übergabe für Massenvertragsprüfungen an Luminance oder Kira. Laden wenn der Nutzer "Luminance\", "Kira\", "KI-Prüfung\", "automatische Extraktion\" oder "Massenprüfung\" erwähnt oder der Datenraum mehr als ~50… |
| `mandat-triage-gesellschaftsrecht` | Eingangs-Abfrage für gesellschaftsrechtliche Mandate — Mandant fragt nach GmbH-Gründung Gesellschafterbeschluss Kapitalerhöhung Geschäftsführer-Abberufung M&A-Transaktion oder Gesellschafterstreit. Klaert… |
| `schriftliche-beschlussfassung` | Entwirft Beschlüsse im schriftlichen Verfahren (§ 48 Abs. 2 GmbHG) oder Umlaufbeschlüsse im Hausstil mit Präzedenzsuche im Beschlussarchiv. Bei der AG: Hinweis, dass HV-Beschlüsse Präsenz oder virtuelle HV (§ 118a… |
| `tabellenpruefung` | Tabellarisches Vertragsreview als Prompt-Matrix — pro Spalte ein Extraktionsprompt (was wird gefragt), pro Zeile ein dokumentspezifischer Prompt (wie wird dieses Dokument behandelt). Eine Zeile pro Dokument, eine… |
| `vollzugs-checkliste` | Vollzugscheckliste für M&A-Transaktionen nach deutschem Recht – was blockiert den Vollzug (Closing), kritischer Pfad, Tage bis Vollzug. Selbstaktualisierend: nimmt neue Einträge aus DD-Findings und Anlage-Erstellung… |
| `wesentliche-vertraege-anlage` | Erstellt das Verzeichnis wesentlicher Verträge (Material Contracts Schedule) aus Due-Diligence-Erkenntnissen auf Grundlage der SPA-Definition und des Anhangformats. Berücksichtigt Change-of-Control-Klauseln… |

## Worum geht es?

Dieses Plugin unterstuetzt Anwaelte und Wirtschaftsjuristen bei laufenden gesellschaftsrechtlichen Mandaten: GmbH- und AG-Governance, Personengesellschaften, M&A-Due-Diligence ohne Discovery, Gesellschafterbeschluesse, Handelsregisteranmeldungen, Closing-Checklisten und Compliance-Fristen. Es deckt sowohl die laufende Gesellschaftsverwaltung als auch transaktionsbezogene Mandate ab.

Das Plugin ist auf eine pruefende und beratende Kanzleipraxis ausgerichtet. Es enthaelt einen Kaltstart-für die Einrichtung des Praxisprofils sowie Mandats-Workspaces für Mehrfachmandatsbetrieb.

## Wann brauchen Sie diese Skill?

- Sie beraten eine GmbH bei Beschlussfassung, Geschaeftsfuehrer-Haftung oder Gesellschafterstreit.
- Sie begleiten eine M&A-Transaktion auf der Rechtspruefungsseite (Due Diligence, Q&A, Datenraum, Closing Checklist).
- Sie muessen Handelsregisteranmeldungen vorbereiten (Geschaeftsfuehrerwechsel, Prokura, Sitzverlegung, Kapitalmanahmen).
- Sie verwalten gesellschaftsrechtliche Compliance-Fristen (Jahresabschluss, Transparenzregister, Bilanzpublizitaet).
- Ein Gesellschafterstreit droht oder eine Patt-Situation ist eingetreten und Sie benoetigen eine Konfliktstrategie.

## Fachbegriffe (kurz erklaert)

- **Business Judgment Rule** — Haftungsprivileg für Geschaeftsfuehrer und Vorstande bei unternehmerischen Entscheidungen (analog § 93 Abs. 1 S. 2 AktG, § 43 GmbHG).
- **Drag-Along** — Mitnahmerecht: Mehrheitsgesellschafter kann Minderheitsgesellschafter zum Verkauf zwingen.
- **Tag-Along** — Mitveraeuserungsrecht: Minderheitsgesellschafter kann beim Verkauf mitziehen.
- **Closing Checklist** — Checkliste aller bis zum Vollzug einer Transaktion zu erfuellenden Bedingungen und Handlungen.
- **Umlaufbeschluss** — Gesellschafterbeschluss ohne Versammlung; bei GmbH nach § 48 Abs. 2 GmbHG zulaessig mit Zustimmung aller Gesellschafter.
- **Prokura** — Umfassende Handlungsvollmacht nach §§ 48 ff. HGB; bedarf der Handelsregistereintragung.
- **Change of Control** — Klausel in Vertraegen, die bei Wechsel der Gesellschafterstruktur besondere Rechte (z.B. Kuendigung) ausloest.

## Rechtsgrundlagen

- §§ 35-43 GmbHG — Geschaeftsfuehrung und Haftung
- §§ 46-49 GmbHG — Gesellschafterversammlung und Beschluesse
- §§ 93 ff. AktG — Vorstandshaftung, Business Judgment Rule
- §§ 107 ff. AktG — Aufsichtsrat (Protokoll, Beschluesse)
- §§ 241, 246 AktG — Nichtigkeits- und Anfechtungsklage (analog GmbH)
- §§ 12 ff. HGB — Handelsregister und Registeranmeldung
- §§ 48 ff. HGB — Prokura
- §§ 15 HGB — Wirkung der Handelsregistereintragung
- § 613a BGB — Betriebsuebergang bei Post-Merger-Integration
- §§ 18 ff. GwG — Transparenzregister

## Schritt-für-Schritt: Einstieg ins Plugin

1. Mandantenkonstellation klaeren: Gesellschaftsform, Mandantenrolle (Gesellschafter, GF, Aufsichtsrat, Kaeufer, Investor), Sachgebiet.
2. Phase des Mandats bestimmen: Governance, Transaktion (DD, Closing), Streit oder Compliance.
3. Passenden Skill auswaehlen (siehe Skill-Tour).
4. Eilfristen pruefen: Insolvenzantragspflicht § 15a InsO, Anfechtungsklagefrist § 246 AktG analog (ein Monat), WEG-Klagefrist.
5. Anschluss-Skill bestimmen: nach Due-Diligence-Extraktion folgt Deal-Team-Briefing und Closing Checklist.

## Skill-Tour (was gibt es hier?)

**Konfiguration und Einstieg**

- `gesellschaftsrecht-kaltstart-interview` — Ersteinrichtung des Praxisprofils: Taetigkeitsbereiche, Wesentlichkeitsschwellen, Hausstil, Eskalationsmatrix.
- `gesellschaftsrecht-anpassen` — Praxisprofil aktualisieren: Risikoprofil, Module, Schwellenwerte, Workspace-Pfade.
- `gesellschaftsrecht-mandat-arbeitsbereich` — Mandats-Workspaces verwalten für Mehrfachmandatsbetrieb.
- `mandat-triage-gesellschaftsrecht` — Eingangs-Abfrage für gesellschaftsrechtliche Mandate mit Fristen-Ampel und Routing.

**Gesellschafterbeschluesse und Governance**

- `gesellschafterbeschluss` — Erstellung, Pruefung und Anfechtung von Gesellschafterbeschluessen in GmbH und AG.
- `schriftliche-beschlussfassung` — Umlaufbeschluesse im Hausstil mit Stimmverboten und Mehrheitserfordernissen.
- `aufsichtsrat-protokoll` — Protokolle von Vorstandssitzungen, Aufsichtsratssitzungen und GV im Hausformat.

**Haftung und Konflikt**

- `geschaeftsfuehrer-haftung-43-gmbhg` — Prueft persönliche Haftung des GF nach § 43 GmbHG mit Business Judgment Rule und D&O-Versicherung.
- `gesellschafterstreit-loesungsstrategie` — Konflikt- und Mediationsstrategie bei Gesellschafterstreit, Patt-Situation und Einziehungsverfahren.

**Due Diligence und M&A**

- `dd-findings-extraktion` — Extraktion von DD-Issues aus Datenraum-Dokumenten nach Hauskategorien und Wesentlichkeitsschwellen.
- `dealteam-zusammenfassung` — Gestaffelte Deal-Briefings für GF, Deal-Lead und Arbeitsteam aus DD-Findings.
- `vollzugs-checkliste` — Vollzugscheckliste für M&A-Transaktionen: kritischer Pfad, CPs, Tage bis Closing.
- `wesentliche-vertraege-anlage` — Verzeichnis wesentlicher Vertraege (Material Contracts Schedule) aus DD-Erkenntnissen.
- `ki-werkzeug-uebergabe` — KI-Tool-Uebergabe für Massenvertragsprüfungen an Luminance oder Kira.
- `tabellenpruefung` — Tabellarisches Vertragsreview als Prompt-Matrix pro Dokument und Datenpunkt.

**Register und Compliance**

- `handelsregisteranmeldung` — Vorbereitung von HRB/HRA/GnR/PartGR-Anmeldungen mit Pflichtanmeldungen und Wirkung nach § 15 HGB.
- `gmbh-gruendung` — GmbH-Gruendung von der Satzung bis zur Handelsregistereintragung mit UG-Variante.
- `gesellschafts-compliance` — Compliance-Tracker für Einreichungsfristen, Bilanzpublizitaet und Transparenzregister.

**Post-Merger-Integration**

- `integrations-management` — PMI-Tracker: Phasenplan, Zustimmungsverfolgung, § 613a BGB und BetrVG-Mitbestimmung.

## Worauf besonders achten

- **Anfechtungsfrist beachten.** Die Analogie zu § 246 AktG für GmbH-Beschluesse setzt typischerweise eine einmonatige Klagefrist; nach laengerer Zeit droht Verwirkung.
- **Insolvenzantragspflicht parallel pruefen.** Sobald der GF Insolvenzanzeichen erkennt, laeuft die Antragspflicht nach § 15a InsO; sofort an `fortbestehensprognose`-Plugin verweisen.
- **Change-of-Control-Klauseln in DD.** Bei M&A-Due-Diligence muessen alle wesentlichen Vertraege auf Change-of-Control-Klauseln durchleuchtet werden; Closing kann sonst scheitern.
- **Umlaufbeschluss erfordert Einstimmigkeit.** Bei GmbH muss jeder Gesellschafter zustimmen (§ 48 Abs. 2 GmbHG); fehlende Stimmen machen Beschluss unwirksam.
- **Transparenzregister und Gesellschafterliste aktuell halten.** Jede Aenderung der Gesellschafterstruktur loest eine Meldepflicht aus (§ 20 GwG).

## Typische Fehler

- GF-Haftung wird nur nach § 43 GmbHG geprueft ohne § 15b InsO Zahlungsverbot bei Insolvenzreife.
- Protokolle von Gesellschafterversammlungen sind unvollstaendig; Abstimmungsergebnisse fehlen oder Stimmverbote werden nicht beachtet.
- Closing-Checklist wird zu spaet aufgebaut; Regulatory-Fristen wurden verpasst.
- Betriebsuebertragung nach § 613a BGB wird in Post-Merger-Integration nicht fristgemaess kommuniziert.
- DD-Findings werden nicht in die SPA-Garantien und Disclosure Schedules uebersetzt.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum (GmbHG, AktG, HGB, BGB, InsO, GwG, BetrVG)

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 48 GmbHG
- § 40 GmbHG
- § 246 AktG
- § 43 GmbHG
- § 47 GmbHG
- § 108 AktG
- § 20 GwG
- § 53 GmbHG
- § 15 GmbHG
- § 130 AktG
- § 5 GmbHG
- § 107 AktG

### Leitentscheidungen

- BGH II ZR 25/82
- BFH I R 53/08

---

## Skill: `aufsichtsrat-protokoll`

_Erstellt Protokolle von Vorstandssitzungen (AG), Aufsichtsratssitzungen (AG, § 107 AktG) und Gesellschafterversammlungen (GmbH, § 48 GmbHG) im Hausformat. Erkennt bevorstehende Organsitzungen aus dem Kalender, fragt nach Tagesordnung und Materialien und erstellt einen vollständigen Entwurf. Trigg..._

# Vorstands- und Aufsichtsratsprotokoll (AG: § 107 AktG; GmbH: § 48 GmbHG)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Vorstands- und Aufsichtsratsprotokoll (AG: § 107 AktG; GmbH: § 48 GmbHG)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Vorstands- und Aufsichtsratsprotokoll (AG: § 107 AktG; GmbH: § 48 GmbHG)
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Kernsachverhalt

Sitzungsprotokolle sind Rechtsurkunden. Sie dokumentieren Beschlussfassungen, legitimieren Organhandeln und sind das primäre Beweismittel für Ermächtigungen, Zustimmungen und Willensbildungsprozesse. Fehlerhafte, unvollständige oder verspätete Protokolle gefährden die Rechtssicherheit von Unternehmensentscheidungen — von Unternehmenskäufen über Kapitalmaßnahmen bis hin zur Entlastung von Vorstand und Aufsichtsrat.

Unterstützt bei der Erstellung von Protokollen für:
- **Aufsichtsratssitzungen** (AG, § 107 Abs. 2 AktG — gesetzliche Niederschriftspflicht)
- **Vorstandssitzungen** (AG, keine gesetzliche Pflicht, aber beweisrechtlich zwingend empfohlen)
- **Gesellschafterversammlungen** (GmbH, § 48 GmbHG — keine gesetzliche Protokollpflicht, aber gesellschaftsvertraglich und nach h.M. unverzichtbar)
- **Hauptversammlungen** (AG, § 130 AktG — notarielle Beurkundung bei börsennotierten AG)
- **Beiratssitzungen** (wenn Beirat organschaftliche Funktion hat)

## Kaltstart-Rückfragen

Bevor das Protokoll erstellt wird, sind folgende Punkte zu klären:

1. **Welches Organ, welche Gesellschaft?** AG-Aufsichtsrat / AG-Vorstand / GmbH-Gesellschafterversammlung / HV / Beirat — und Name der Gesellschaft?
2. **Datum, Uhrzeit, Ort?** Physische Sitzung (Adresse), Videokonferenz (Plattform), Telefonsitzung oder hybride Sitzung?
3. **Einladung erfolgt?** Wann, durch wen, auf welchem Weg? Wurde die Einladungsfrist (AR: § 110 Abs. 2 AktG mind. 14 Tage) eingehalten oder wurde auf sie verzichtet?
4. **Anwesenheit?** Wer war anwesend (Mitglieder, Gäste, externe Berater), wer entschuldigt? Beschlussfähigkeit gegeben (§ 108 Abs. 2 AktG)?
5. **Stimmverbote?** Lagen Interessenkonflikte vor (§ 47 Abs. 4 GmbHG, § 136 AktG)? Welche Mitglieder waren von welchen Abstimmungen ausgeschlossen?
6. **Tagesordnung und Materialien?** Bitte Tagesordnung, Beschlussvorlagen, Präsentationen und Berichte bereitstellen (auch als grober Entwurf oder Stichpunkte).
7. **Beschlüsse?** Welche Beschlüsse wurden gefasst, mit welchem Abstimmungsergebnis (Ja/Nein/Enthaltungen)?
8. **Anlagen?** Welche Dokumente wurden beigefügt oder in der Sitzung verteilt?
9. **Protokollform?** Vollprotokoll (wortnahe Wiedergabe der Diskussion), Beschlussprotokoll (nur Beschlüsse) oder Hybridform (Hausformat)?
10. **Unterzeichnung?** Wer unterzeichnet (AR-Vorsitzender allein nach § 107 Abs. 2 S. 3 AktG; GmbH-GV: Versammlungsleiter; Gegenpräsentation / Nichtjurist-Rolle beachten)?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Normtexte mit Auszügen

**§ 107 Abs. 2 AktG — Niederschriftspflicht Aufsichtsrat**
> "Über jede Sitzung des Aufsichtsrats ist eine Niederschrift anzufertigen, die Ort und Tag der Sitzung, die Teilnehmer, die Gegenstände der Tagesordnung, den wesentlichen Inhalt der Verhandlungen und die Beschlüsse des Aufsichtsrats enthält. [...] Die Niederschrift ist vom Vorsitzenden zu unterzeichnen."

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

**§ 48 GmbHG — Gesellschafterversammlung**
> "Die Beschlüsse der Gesellschafter werden in Versammlungen gefasst. [...] Die Gesellschafterversammlung wird durch die Geschäftsführer berufen."

Protokollpflicht: § 48 GmbHG enthält keine gesetzliche Protokollpflicht. Sie ergibt sich aus dem Gesellschaftsvertrag (übliche Klausel) oder aus Beweiszwecken. Bei § 48 Abs. 2 GmbHG (schriftliches Abstimmungsverfahren) empfiehlt sich ein schriftliches Protokoll, das die Einvernehmlichkeit aller Gesellschafter dokumentiert.

**§ 130 AktG — Beurkundung der Hauptversammlungsbeschlüsse**
> "(1) Jeder Beschluß der Hauptversammlung ist durch eine über die Verhandlung notariell aufgenommene Niederschrift zu beurkunden."

Gilt für börsennotierte AG. Für nicht börsennotierte AG reicht nach § 130 Abs. 4 AktG eine vom Vorsitzenden und vom Hauptaktionär unterzeichnete Niederschrift.

**§§ 241 ff. AktG — Beschlussmängel**

| Norm | Mängelart | Rechtsfolge |
|---|---|---|
| § 241 AktG | Nichtigkeitsgründe (abschließend): fehlende notarielle Form, Verstoß gegen Gläubigerschutz/öffentliche Ordnung, Satzungsverstoß bei Kapitalmaßnahmen | Beschluss ist nichtig von Anfang an; jedermann kann sich darauf berufen |
| § 243 AktG | Anfechtbarkeit: Gesetzes-/Satzungsverstoß | Beschluss wirksam bis zur Anfechtung; Klage innerhalb 1 Monat (§ 246 Abs. 1 AktG) |
| § 244 AktG | Heilung des anfechtbaren Beschlusses | Durch Genehmigung der HV oder Ablauf der Anfechtungsfrist |
| § 246 Abs. 1 AktG | Anfechtungsfrist | 1 Monat ab Beschlussfassung |

**§ 47 Abs. 4 GmbHG — Stimmverbot GmbH**
> "Ein Gesellschafter, welcher durch die Beschlußfassung entlastet oder von einer Verbindlichkeit befreit werden soll, hat hierbei kein Stimmrecht und darf ein solches auch nicht für andere ausüben."

Das Stimmverbot gilt auch für Beschlüsse über die Einleitung von Rechtsstreitigkeiten gegen den betreffenden Gesellschafter. Verstoß führt zur Anfechtbarkeit des Beschlusses.

**§ 136 AktG — Stimmverbotsregelungen bei der AG**
> "(1) Niemand kann für sich oder für einen anderen das Stimmrecht ausüben, wenn darüber Beschluß gefaßt wird, ob er zu entlasten oder von einer Verbindlichkeit zu befreien ist oder ob die Gesellschaft gegen ihn einen Anspruch geltend machen soll."

**§ 108 Abs. 2 AktG — Beschlussfähigkeit des Aufsichtsrats**
> "Der Aufsichtsrat ist beschlußfähig, wenn mindestens drei Mitglieder an der Beschlußfassung teilnehmen."

Zusätzlich: Mindestens die Hälfte der Gesamtzahl der Mitglieder muss anwesend sein (§ 108 Abs. 2 S. 1 AktG).

**§ 110 Abs. 2 AktG — Einladungsfrist Aufsichtsrat**
> Einberufung mind. 14 Tage vor der Sitzung. Verkürzung bei Dringlichkeit möglich; Verzicht bei Einvernehmen aller Mitglieder.

### Leitentscheidungen

| Gericht | Aktenzeichen | Fundstelle | Leitsatz / Relevanz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema: Sitzungsprotokoll

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Organidentifikation | Welches Gremium? AG-AR, AG-Vorstand, GmbH-GV, HV, Beirat? | Festlegung des anwendbaren Rechtsrahmens |
| 2 | Einladungsprüfung | Frist eingehalten (AR: § 110 Abs. 2 AktG, 14 Tage)? Einladungsverzicht dokumentiert? | Beschlussfähigkeit gefährdet, wenn Frist verletzt und kein Verzicht |
| 3 | Beschlussfähigkeit | Anzahl anwesender Mitglieder / Quorum (§ 108 Abs. 2 AktG AR; GmbH: Gesellschaftsvertrag)? | Keine gültige Beschlussfassung bei fehlendem Quorum |
| 4 | Stimmverbote | § 47 Abs. 4 GmbHG / § 136 AktG: Hat stimmbefangenes Mitglied abgestimmt? | Anfechtbarkeit prüfen; Stimmverbot im Protokoll vermerken |
| 5 | Interessenkonflikte | § 34 BGB analog AR: Abstimmung über eigene Angelegenheit? | Stimmbefangenheit vermerken; ggf. Mitglied aus Abstimmung ausschließen |
| 6 | Tagesordnungspunkte | Alle TOP korrekt erfasst? Reihenfolge stimmt? Beschlussvorlagen vorhanden? | Unvollständige TOP-Liste führt zu Beweisnot |
| 7 | Beschlussdokumentation | Beschlüsse vollständig und klar formuliert? Abstimmungsergebnis (Ja/Nein/Enthaltung) angegeben? | Unklare Beschlussformulierung = Auslegungsstreit |
| 8 | Anlagenverweis | Alle referenzierten Anlagen nummeriert und beigefügt? | Anlage fehlt = Beschluss unvollständig dokumentiert |
| 9 | Notarielle Beurkundung | § 130 Abs. 1 AktG (börsennotierte AG); § 179 AktG (Satzungsänderung); § 293 AktG (Unternehmensvertrag): Notar erforderlich? | Formnichtigkeit bei fehlendem Notar (§ 241 Nr. 2 AktG) |
| 10 | Unterzeichnung | AR: Vorsitzender allein (§ 107 Abs. 2 S. 3 AktG); GmbH-GV: Versammlungsleiter; HV: Notar / Vorsitzender (§ 130 AktG) | Fehlende Unterzeichnung begründet Beweisnot; kein automatischer Nichtigkeitsgrund |
| 11 | Executive Sessions | Vertrauliche Sitzungsabschnitte (ohne Management) separat dokumentiert? | Mandats- und Beratungsgeheimnis beachten |
| 12 | Zustellung und Fristen | Protokoll den Mitgliedern zugeleitet? Genehmigung in der Folgesitzung vorgesehen? | Keine gesetzliche Frist, aber Best Practice: innerhalb von 2 Wochen |
| 13 | Anfechtungsfrist | § 246 Abs. 1 AktG: 1 Monat ab Beschlussfassung — GmbH analog? | Fristnotiz anlegen; für M&A-Transaktionen besondere Relevanz |
| 14 | Beschlussmängelanalyse | Lagen formelle oder materielle Beschlussmängel vor (§§ 241, 243 AktG)? | Sofern erkennbar: unverzüglich mit Mandant besprechen |
| 15 | Archivierung | Protokoll in mandatsspezifischem Archiv, verschlüsselt gespeichert? Aufbewahrungsfrist beachten? | Handelsrechtliche Aufbewahrung: 10 Jahre (§ 257 HGB) |

## Beweislast

| Frage | Beweislast | Erläuterung |
|---|---|---|
| Beschluss wurde gefasst | Derjenige, der sich auf den Beschluss beruft | Protokoll als Urkundsbeweis (§ 416 ZPO bei privatschriftlichem Protokoll); bei notariellem Protokoll: öffentliche Urkunde (§ 415 ZPO) |
| Beschluss ist nichtig (§ 241 AktG) | Kläger (bei Feststellungsklage); jedermann kann einwenden | Nichtigkeitsgründe sind von Amts wegen zu berücksichtigen |
| Beschluss anfechtbar (§ 243 AktG) | Anfechtender Gesellschafter / Aktionär | Klage binnen 1 Monat; materieller Nachweis des Gesetzes-/Satzungsverstoßes |
| Stimmverbot verletzt (§ 47 Abs. 4 GmbHG) | Anfechtender Gesellschafter | Nachweis, dass stimmbefangenes Mitglied abgestimmt und Beschluss damit kausal beeinflusst wurde |
| Ordnungsgemäße Einladung | Einladender (Vorsitzender, Geschäftsführer) | Nachweis durch Einladungsschreiben, Eingangsbestätigungen, Einladungsverzicht |
| Beschlussfähigkeit | Protokollführer / Vorsitzender | Anwesenheitsliste im Protokoll ist Beweismittel |

## Fristen und Verjährung

| Frist | Norm | Inhalt | Folge bei Versäumnis |
|---|---|---|---|
| Anfechtung HV-Beschluss | § 246 Abs. 1 AktG | 1 Monat ab Beschlussfassung | Beschluss wird unanfechtbar; Anfechtungsrecht erlischt |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Nichtigkeit (§ 241 AktG) | Keine Frist | Nichtigkeitsklage zu jederzeit möglich | Dauerhafter Schwebezustand; Heilungsmöglichkeit nach § 244 AktG prüfen |
| Einladungsfrist AR | § 110 Abs. 2 AktG | Mind. 14 Tage vor Sitzung | Anfechtbarkeit der gefassten Beschlüsse; Verzicht dokumentieren |
| Protokollierung AR | § 107 Abs. 2 AktG | Keine gesetzliche Frist; Best Practice: 2 Wochen | Beweisschwierigkeiten; ggf. Beschlussfassung unwirksam wenn Inhalt unrekonstruierbar |
| Aufbewahrung Protokoll | § 257 Abs. 1 Nr. 1 HGB | 10 Jahre (Handelsbücher und Jahresabschlüsse; Protokolle als Handelsbriefe: 6 Jahre) | Ordnungswidrigkeitenrisiko; Beweisschwierigkeiten in Haftungsfällen |
| Ansprüche gegen AR-Mitglieder | § 116 i.V.m. § 93 Abs. 6 AktG | Verjährung: 5 Jahre (börsennotierte AG: 10 Jahre); § 93 Abs. 6 AktG | Spätfolgen fehlerhafter Protokollierung (Beschlussmangel → Schaden) |

## Typische Gegenargumente

| Einwand | Begründung Gegenseite | Erwiderung |
|---|---|---|
| Beschluss gültig trotz fehlendem Protokoll | Protokoll ist nur Beweismittel, kein Wirksamkeitserfordernis | Beweislastrisiko liegt beim Beschlussführer; ohne Protokoll kein verlässlicher Nachweis gegenüber M&A-Käufern, Behörden, Gerichten |
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| Protokoll erst 3 Monate nach Sitzung erstellt | Gesetz sieht keine Frist vor | Beweiswert des Protokolls leidet erheblich; Erinnerungsprotokoll mit deutlichem Hinweis auf späte Erstellung versehen |
| Videokonferenz ohne ausdrückliche Satzungsermächtigung | § 108 Abs. 4 AktG erlaubt Videokonferenz des AR | GmbH: GmbHG sieht keine ausdrückliche Regelung vor; gesellschaftsvertragliche Ermächtigung prüfen oder Einvernehmen aller sicherstellen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Aufsichtsratssitzung protokollieren | Protokoll nach Schema; Template unten |
| Variante A — Geheimhaltungspflichtige Tagesordnungspunkte | Protokoll in vertraulichen Teil und öffentlichen Teil aufteilen |
| Variante B — Beschluesse sind formell angriffen | Beschlussprotokoll mit Abstimmungsergebnis erweiternd festhalten |
| Variante C — Fernsitzung keine Anwesenheit in Praeenz | Protokollvermerk Fernsitzung mit Zustimmungsnachweis |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Aufsichtsratssitzung AG — vollständiges Musterprotokoll

```
PROTOKOLL DER AUFSICHTSRATSSITZUNG
DER MUSTER AG, Frankfurt am Main
(HRB 12345 Amtsgericht Frankfurt am Main)

Datum: 15. März 2026, 10:00 Uhr bis 12:30 Uhr
Ort: Räumlichkeiten der Kanzlei XY, Taunusanlage 1, 60329 Frankfurt am Main
Protokollführerin: Rechtsanwältin Dr. Christine Weber, Kanzlei XY

VORSITZ: Dr. Anna Müller (Aufsichtsratsvorsitzende)

ANWESEND:
Aufsichtsratsmitglieder:
- Dr. Anna Müller (Vorsitzende)
- Prof. Dr. Karl Schmidt (Stellvertretender Vorsitzender)
- Ursula Braun (Arbeitnehmervertreterin)
- Thomas Berger (Arbeitnehmervertreter)
- [weitere Mitglieder]

Gäste (mit Einladung des AR-Vorsitzenden):
- Max Huber, Vorstandsvorsitzender
- Sandra Weiß, Vorstand Finanzen (CFO)
- Dr. Peter Klein, Wirtschaftsprüfer, KPMG AG (nur TOP 3)

ENTSCHULDIGT: [Name], [Grund]

---------------------------------------------------------------------------

EINBERUFUNG UND BESCHLUSSFÄHIGKEIT

Dr. Müller eröffnete die Sitzung um 10:00 Uhr. Sie stellte fest, dass die Einladung zur
Sitzung den Mitgliedern mit Schreiben vom 28. Februar 2026 und damit ordnungsgemäß mit
einer Frist von 15 Tagen zugegangen ist (§ 110 Abs. 2 AktG). Es haben [N] von [N]
Aufsichtsratsmitgliedern an der Beschlussfassung teilgenommen. Der Aufsichtsrat ist damit
gemäß § 108 Abs. 2 AktG beschlussfähig.

Das Protokoll der letzten Sitzung vom 10. Januar 2026 wurde genehmigt.

---------------------------------------------------------------------------

TOP 1: Bericht des Vorstands — Geschäftsentwicklung Q1 2026

Der Vorstandsvorsitzende Max Huber berichtete über die Geschäftsentwicklung im ersten
Quartal 2026 anhand der Vorstands-Präsentation (Anlage A). Umsatz und EBIT entwickelten
sich plangemäß. Wesentliche Abweichungen vom Budget wurden nicht festgestellt.

Der Aufsichtsrat nahm den Bericht zur Kenntnis. Es wurde keine Beschlussfassung
veranlasst.

---------------------------------------------------------------------------

TOP 2: Zustimmung zum Erwerb der Beta GmbH — § 111 Abs. 4 AktG i.V.m. § 3 GO-Vorstand

Der Vorstandsvorsitzende erläuterte die geplante Übernahme sämtlicher Geschäftsanteile
der Beta GmbH, München (HRB 98765 AG München), zum Kaufpreis von bis zu 5.000.000 EUR
(in Worten: fünf Millionen Euro) gemäß dem Entwurf des Share Purchase Agreement
(Anlage B). Die Maßnahme unterfällt § 3 Abs. 1 lit. (c) der Geschäftsordnung des
Vorstands (Zustimmungspflicht bei Erwerben ab 1.000.000 EUR).

Der CFO Sandra Weiß erläuterte die Finanzierungsstruktur und die Due-Diligence-Ergebnisse
(Anlage C).

[Diskussion, wesentliche Erwägungen des Aufsichtsrats:]
Der Aufsichtsrat erörterte insbesondere die kartellrechtliche Freistellung und die
Gewährleistungsregeln des SPA. Keine Mitglieder hatten einen Interessenkonflikt
anzuzeigen.

Nach eingehender Beratung fasste der Aufsichtsrat einstimmig folgenden

BESCHLUSS:
Der Aufsichtsrat stimmt dem Erwerb sämtlicher Geschäftsanteile an der Beta GmbH,
München, durch die Muster AG zum Kaufpreis von bis zu 5.000.000 EUR (fünf Millionen
Euro) gemäß dem Entwurf des Share Purchase Agreement in der Fassung vom 10. März 2026
(Anlage B) zu. Er ermächtigt den Vorstand, den Kaufvertrag mit den in der Sitzung
besprochenen Maßgaben zu unterzeichnen.

Abstimmung: [N] Ja / [N] Nein / [N] Enthaltungen

---------------------------------------------------------------------------

TOP 3: Jahresabschluss und Lagebericht 2025 — § 172 AktG

[Dr. Klein von KPMG war für diesen TOP anwesend.]

Der Wirtschaftsprüfer Dr. Klein erläuterte den Bestätigungsvermerk und die wesentlichen
Ergebnisse der Jahresabschlussprüfung 2025 (Anlage D: Prüfungsbericht KPMG).

[Diskussion. Dr. Klein verließ den Sitzungssaal nach Abschluss von TOP 3 um 11:45 Uhr.]

Der Aufsichtsrat fasste folgenden

BESCHLUSS:
Der Aufsichtsrat billigt den Jahresabschluss und den Lagebericht 2025 der Muster AG
gemäß § 172 AktG in der geprüften Fassung (Anlage D).

Abstimmung: [N] Ja / [N] Nein / [N] Enthaltungen

---------------------------------------------------------------------------

SCHLIESSUNGSPUNKT

Dr. Müller stellte fest, dass keine weiteren Tagesordnungspunkte vorlagen. Sie schloss
die Sitzung um 12:30 Uhr.

ANLAGEN:
Anlage A: Vorstandspräsentation Geschäftsentwicklung Q1 2026
Anlage B: Entwurf Share Purchase Agreement Beta GmbH, Stand 10.03.2026
Anlage C: Finanzierungsübersicht und DD-Zusammenfassung
Anlage D: Jahresabschluss und Prüfungsbericht KPMG 2025

Frankfurt am Main, den [Datum der Unterzeichnung]

_________________________________
Dr. Anna Müller
Aufsichtsratsvorsitzende
(§ 107 Abs. 2 S. 3 AktG)

[ENTWURF — nicht zur Verabschiedung freigegeben]
```

### Baustein 2: GmbH-Gesellschafterversammlung mit Stimmverbot

```
PROTOKOLL DER GESELLSCHAFTERVERSAMMLUNG
DER ALPHA GMBH, München
(HRB 12345 Amtsgericht München)

Datum: 20. März 2026, 14:00 Uhr bis 15:30 Uhr
Ort: Geschäftsräume der Alpha GmbH, Maximilianstraße 10, 80539 München
Versammlungsleiter: Rechtsanwalt Dr. Jörg Fischer
Protokollführer: Rechtsanwalt Dr. Jörg Fischer

ERSCHIENENE GESELLSCHAFTER:
1. Herr Thomas Maier, gesch. 50 % [anwesend / vertreten durch ___]
2. Frau Petra Schulz, gesch. 30 % [anwesend]
3. Muster Beteiligungs GmbH, gesch. 20 % [vertreten durch Max Baum]

Sämtliche Geschäftsanteile = 100 % sind vertreten. Einberufung in der Versammlung
einvernehmlich als ordnungsgemäß anerkannt.

BESCHLUSSFÄHIGKEIT: Alle Gesellschafter anwesend oder vertreten; alle Gesellschafter
haben auf Wahrung der Einberufungsfrist verzichtet. Die Versammlung ist beschlussfähig.

---------------------------------------------------------------------------

TOP 1: Feststellung des Jahresabschlusses 2025

Die Geschäftsführerin Petra Schulz erläuterte den Jahresabschluss 2025
(Anlage A: Jahresabschluss mit Anhang). Umsatz: [X] EUR; EBIT: [Y] EUR.

Die Gesellschafterversammlung fasste folgenden

BESCHLUSS:
Der Jahresabschluss der Alpha GmbH zum 31. Dezember 2025 wird in der vorgelegten Fassung
(Anlage A) festgestellt. Der Bilanzgewinn in Höhe von [Z] EUR wird auf neue Rechnung
vorgetragen.

Abstimmung: Ja: 100 % / Nein: 0 % / Enthaltungen: 0 %

---------------------------------------------------------------------------

TOP 2: Entlastung der Geschäftsführerin — § 46 Nr. 5 GmbHG

[STIMMVERBOT: Frau Petra Schulz (30 %) unterliegt gemäß § 47 Abs. 4 GmbHG dem
Stimmverbot, da über ihre eigene Entlastung als Geschäftsführerin abgestimmt wird.
Sie ist von der Abstimmung über TOP 2 ausgeschlossen. Stimmrechtsanteil für die
Abstimmung: Thomas Maier 50 %, Muster Beteiligungs GmbH 20 % = 70 % der Gesamtstimmen.
Dieser Anteil gilt als 100 % für die Abstimmung über TOP 2.]

Die Gesellschafterversammlung fasste folgenden

BESCHLUSS:
Der Geschäftsführerin Petra Schulz wird für das Geschäftsjahr 2025 Entlastung erteilt.

Abstimmung (unter Ausschluss des Stimmrechts von Frau Petra Schulz):
Ja: 70 % der Gesamtstimmen (= 100 % der abstimmungsberechtigten Stimmen) /
Nein: 0 % / Enthaltungen: 0 %

---------------------------------------------------------------------------

SCHLIESSUNGSPUNKT: Keine weiteren Tagesordnungspunkte. Die Versammlung wurde um
15:30 Uhr geschlossen.

München, den [Datum]

_________________________________
Dr. Jörg Fischer
Versammlungsleiter / Protokollführer

[ENTWURF]
```

### Baustein 3: Prüfcheckliste vor Verabschiedung

```
PRÜFCHECKLISTE — PROTOKOLL [ORGAN] VOM [DATUM]
Zu prüfen vor Unterzeichnung / Versand

[ ] 1. Organgremium korrekt bezeichnet?
[ ] 2. Datum, Uhrzeit, Ort vollständig?
[ ] 3. Einladung ordnungsgemäß oder Verzicht dokumentiert (§ 110 Abs. 2 AktG)?
[ ] 4. Alle anwesenden / entschuldigten Mitglieder erfasst?
[ ] 5. Beschlussfähigkeit korrekt festgestellt (§ 108 Abs. 2 AktG)?
[ ] 6. Stimmverbote geprüft und ggf. vermerkt (§ 47 Abs. 4 GmbHG / § 136 AktG)?
[ ] 7. Alle TOP in korrekter Reihenfolge erfasst?
[ ] 8. Beschlusstexte stimmen mit tatsächlich gefassten Beschlüssen überein?
[ ] 9. Abstimmungsergebnisse (Ja / Nein / Enthaltung) numerisch korrekt?
[ ] 10. Anlagen korrekt nummeriert und vollständig beigefügt?
[ ] 11. Gäste / externe Berater mit Funktion und Top-Anwesenheit vermerkt?
[ ] 12. Executive Sessions / vertrauliche TOP separat protokolliert?
[ ] 13. Notarielle Beurkundung erforderlich? (§ 130 Abs. 1 AktG, § 179 AktG)
[ ] 14. Unterzeichnungsblock korrekt (AR: Vorsitzender allein; GmbH: Versammlungsleiter)?
[ ] 15. ENTWURF-Vermerk bis Genehmigung in der Folgesitzung vorhanden?
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

| Streitgegenstand | Streitwertansatz | Kosten (RVG-Beispiel) |
|---|---|---|
| Anfechtungsklage HV-Beschluss | Wirtschaftliches Interesse des Klägers, mind. 50.000 EUR (§ 247 Abs. 1 AktG) | Bei 50.000 EUR: 3 Gebühren × 1.605 EUR = ca. 4.815 EUR RA-Kosten (zzgl. MwSt.) |
| Anfechtungsklage GmbH-Beschluss | Freies Ermessen Gericht; oft wirtschaftliches Interesse an der Beschlussaufhebung | Abhängig von Unternehmenswert / Beteiligungsquote |
| Nichtigkeitsklage (§ 241 AktG) | § 247 Abs. 1 AktG analog | Vergleichbar Anfechtungsklage |
| Schadensersatz gegen AR-Mitglied | Konkreter Schaden | Regelmäßig hohe Gegenstandswerte; D&O-Versicherung prüfen |
| Notar Hauptversammlungsprotokoll | Geschäftswert = Gesellschaftsvermögen (mind. 30.000 EUR, § 105 GNotKG) | Bei 5 Mio. EUR: ca. 1.870 EUR Notargebühr (§ 91 GNotKG) |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| M&A-Transaktion: Zielgesellschaft hat lückenhafte AR-Protokolle | Due-Diligence-Finding mit hohem Schweregrad; Verkäufer-Garantie für ordnungsgemäße Beschlussfassung; MAC-Klausel prüfen |
| GmbH-Beschluss ohne Stimmverbotsbeachtung (§ 47 Abs. 4 GmbHG) | Unverzügliche Wiederholung des Beschlusses unter korrekter Stimmrechtsprüfung; falls Frist läuft, Heilungsklage erwägen |
| AR-Protokoll nachträglich (> 3 Monate) erstellt | Deutlichen Hinweis auf Erstellungsdatum im Protokoll; Erinnerungscharakter kennzeichnen; Parallelbeweise sichern (E-Mails, Präsentationen) |
| Videokonferenz-Sitzung ohne GV-Ermächtigung (GmbH) | Einvernehmen aller Gesellschafter ausdrücklich dokumentieren; nachträgliche satzungsrechtliche Ermächtigung erwägen |
| Beschlussfähigkeit knapp | Quorum-Berechnung im Protokoll explizit ausweisen; bei mehreren Ergebnissen (z.B. wegen Stimmbefangenheit) getrennt ausweisen |
| Entlastungsbeschluss mit Stimmverbot | Abstimmungsergebnis getrennt nach abstimmungsberechtigten und gesamten Stimmen dokumentieren; Stimmverbot mit Norm benennen |

## Ablauf (Skill-Steuerung)

### Schritt 1: Sitzung identifizieren

**Kalendererkennung** (wenn Kalender-Connector autorisiert): Suche nach bevorstehenden Ereignissen mit:
- "Vorstandssitzung", "Aufsichtsratssitzung", "AR-Sitzung", "Gesellschafterversammlung", "GV", "Hauptversammlung", "HV", "Beiratssitzung"
- Zeitfenster: 30 Tage voraus; bei Nichtfund 14 Tage rückwärts (Protokolle häufig nachträglich erstellt).

Falls kein Connector: direkt fragen — welches Organ, welches Datum, welcher Typ?

**Sitzungsmetadaten bestätigen:**
- Organ und Gesellschaft
- Datum, Uhrzeit, Ort (physisch / Videokonferenz nach § 108 Abs. 4 AktG / telefonisch)
- Ordnungsgemäße Einladung? (AR: § 110 Abs. 2 AktG, mind. 14 Tage)
- Form der Sitzungsniederschrift: Vollprotokoll / Beschlussprotokoll / Hybrid

### Schritt 2: Anwesenheit und Beschlussfähigkeit

**Mitglieder anwesend:**
- Organ-Zusammensetzung aus Praxisprofil; wer war tatsächlich anwesend / entschuldigt?
- AR: § 108 Abs. 2 AktG — Beschlussfähigkeit: mind. die Hälfte der Mitglieder; mind. 3 Mitglieder müssen bei der Abstimmung mitwirken.
- GmbH-GV: Quorum nach Gesellschaftsvertrag; gesetzlicher Standard: § 47 GmbHG (Mehrheit der abgegebenen Stimmen).

Wenn Beschlussfähigkeit nicht gegeben: STOPP. Keine Protokollierung gültiger Beschlussfassung.

**Interessenkonflikte:**
- AR: § 34 BGB analog; § 136 AktG (Stimmverbot Entlastung)
- GmbH: § 47 Abs. 4 GmbHG (Stimmverbot bei Rechtsgeschäften mit dem Gesellschafter)

### Schritt 3: Materialien

Tagesordnung und Sitzungsmaterialien anfordern:
> Bitte Tagesordnung und alle Sitzungsmaterialien bereitstellen. Falls Präsentationen oder Berichte vorlagen, diese hochladen. Wenn keine Materialien vorlagen, Tagesordnungspunkte als Stichpunkte mitteilen.

### Schritt 4: Protokoll erstellen

Hausformat aus Praxisprofil verwenden. Standard-Struktur:
- Kopfblock: Organ, Gesellschaft, Datum, Uhrzeit, Ort, Vorsitz, Protokollführer
- Einberufung und Beschlussfähigkeit
- Anwesenheitsliste (Mitglieder, Gäste mit Funktion)
- TOP-Blöcke je Tagesordnungspunkt
- Schließung mit Uhrzeit
- Anlagenverzeichnis
- Unterschriftenblock

### Schritt 5: Folgenreiche-Handlung-Sperre

Vor Verabschiedung als endgültig: Falls Rolle **Nichtjurist**:
> Beschlossene Protokolle sind die offizielle Aufzeichnung der Organentscheidungen. Vor Unterzeichnung mit einem Rechtsanwalt prüfen, insbesondere auf: Beschlussmängel (§§ 243, 241 AktG), Interessenkonflikte (§ 47 Abs. 4 GmbHG, § 136 AktG), Einladungsfristen und Beschlussfähigkeit.

### Schritt 6: Ausgabe

1. **Protokollentwurf** (im Hausformat; ENTWURF-Vermerk bis Genehmigung)
2. **Prüfcheckliste** (für Rechtsanwalt)
3. **Genehmigungsversion** (nach Freigabe; ohne Entwurfsvermerk)

## Risiken und typische Fehler

| Fehler | Risiko | Abhilfe |
|---|---|---|
| Fehlendes Protokoll | Beschlussbeweisnot; Beschluss kann Dritten gegenüber nicht belegt werden | Protokoll unverzüglich nacherstellen; Erinnerungscharakter kennzeichnen |
| Stimmverbot übersehen | Beschluss anfechtbar; ggf. nichtig | Stimmverbot systematisch für jeden TOP prüfen; stimmbefangene Mitglieder ausdrücklich ausschließen |
| Einladungsfrist versäumt | Beschlüsse anfechtbar (§ 246 AktG analog) | Einladungsverzicht dokumentieren; Frist künftig im Kalender vormerken |
| Anfechtungsfrist verpasst | Beschluss unanfechtbar; Schaden unreparierbar | Fristnotiz sofort nach Beschlussfassung anlegen |
| Notarielles Protokoll vergessen | Formnichtigkeit (§ 241 Nr. 2 AktG) bei Satzungsänderungen, Kapitalmaßnahmen | Vor jeder HV-Sitzung notarielle Beurkundungspflicht prüfen |
| Unklare Beschlussformulierung | Auslegungsstreit; Vollzugsprobleme bei M&A | Beschlusstexte präzise, vollständig und widerspruchsfrei formulieren |

## Output-Template

**Adressat:** Aufsichtsratsvorsitzender / Protokollführer — Tonfall: sachlich-juristisch, präzise

```
PROTOKOLL
der [ordentlichen / außerordentlichen] Sitzung des Aufsichtsrats
der [GESELLSCHAFT AG / GmbH]
am [TT. Monat JJJJ], [Uhrzeit] Uhr
in [ORT / per Videokonferenz gem. § 108 Abs. 4 AktG]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.
> Dieses Protokoll ist bis zur Genehmigung als ENTWURF zu behandeln.

--- KOPFBLOCK ---
Ort und Zeit: [ORT], [DATUM], [VON] bis [BIS] Uhr
Vorsitz: [NAME], [FUNKTION]
Protokollfuehrender: [NAME]

--- ANWESENHEIT ---
Anwesende AR-Mitglieder: [NAME] (Vorsitz), [NAME], [NAME] — [N] von [GESAMT]
Entschuldigt: [NAME]
Gaeste: [NAME], [FUNKTION] (nur bei TOP [N])
Beschlussfaehigkeit: [BEJAHT / VERNEINT] (§ 108 Abs. 2 AktG: mind. 3 Mitglieder)

--- EINBERUFUNG ---
Einberufung durch [VORSITZENDEN] mit Schreiben vom [DATUM] (Frist § 110 Abs. 2 AktG: mind. [N] Tage).
Tagesordnung lag vor / wurde verteilt am [DATUM].

--- TAGESORDNUNG ---
TOP 1: [TITEL]
TOP 2: [TITEL]
TOP 3: Verschiedenes

--- TOP 1: [TITEL] ---
[VORSITZENDER] erlaeutert [SACHVERHALT]. Nach Aussprache beschliesst der Aufsichtsrat:

BESCHLUSS [1/JJJJ]:
[WORTLAUT DES BESCHLUSSES]

Abstimmung: [N] Ja-Stimmen / [N] Nein-Stimmen / [N] Enthaltungen
[MITGLIED] war wegen Interessenkonflikts (§ 34 BGB analog) nicht stimmberechtigt.
Ergebnis: ANGENOMMEN / ABGELEHNT

[Weitere TOPs analog]

--- SCHLUSS ---
Naechster Termin: [DATUM] (voraussichtlich)
Schluss der Sitzung: [UHRZEIT] Uhr

Anlagen:
1. [ANLAGE 1]
2. [ANLAGE 2]

________________________ ________________________
[VORSITZENDER] [PROTOKOLLFUEHRENDER]
AR-Vorsitzender [FUNKTION]
```

## Rote Schwellen

- **Beschlussfaehigkeit nach § 108 Abs. 2 AktG nicht erreicht** (weniger als 3 Mitglieder stimmen mit) — keine gueltigen Beschluesse; Sitzung vertagen.
- **Stimmverbot § 136 AktG / § 47 Abs. 4 GmbHG uebersehen** — Beschluss anfechtbar; betroffenes Mitglied ausdrücklich von Abstimmung ausschliessen und im Protokoll dokumentieren.
- **Einladungsfrist § 110 Abs. 2 AktG unterschritten** — Beschluesse anfechtbar; Einladungsverzicht aller Mitglieder dokumentieren.
- **Satzungsaenderung / Kapitalmaßnahme ohne Notarprotokoll** — Formnichtigkeit (§ 241 Nr. 2 AktG); Notar rechtzeitig bestellen.
- **Anfechtungsfrist (1 Monat) nach § 246 AktG versaeumt** — Beschluss unanfechtbar auch bei Fehlern; sofort Fristnotiz anlegen.

## Anschluss-Skills

- `gesellschaftsrecht:tabellenpruefung` — Prüfung von Beschlusstabellen und Stimmrechtslisten
- `gesellschaftsrecht:vollzugs-checkliste` — Vollzugsbedingungen nach AR-Zustimmungsbeschluss
- `gesellschaftsrecht:gesellschafts-compliance` — Einreichungsfristen nach Jahresabschlussbilligung
- `grosskanzlei-corporate-ma:ki-einsatz-bei-gutachten-mandatsseite` — Gutachten zu Beschlussmängelrisiken

## Quellen und Zitierweise

- § 107 Abs. 2 AktG (Niederschriftspflicht Aufsichtsrat)
- § 48 GmbHG (Gesellschafterversammlung)
- § 130 AktG (Hauptversammlungsprotokoll)
- §§ 241, 243, 246 AktG (Beschlussmängel und -anfechtung)
- § 47 Abs. 4 GmbHG (Stimmverbot GmbH)
- § 108 Abs. 2 AktG (Beschlussfähigkeit AR)
- § 110 Abs. 2 AktG (Einladungsfrist AR)
- § 136 AktG (Stimmverbot AG)

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Schmidt/Lutter, AktG, 4. Aufl. 2020, § 243 Rn. 5 ff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Scholz, GmbHG, 12. Aufl. 2018, § 47 Rn. 110 ff.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen und Rechtsprechung

### Kuratierte Normen-Bibliothek

- § 48 GmbHG
- § 40 GmbHG
- § 246 AktG
- § 43 GmbHG
- § 47 GmbHG
- § 108 AktG
- § 20 GwG
- § 53 GmbHG
- § 15 GmbHG
- § 130 AktG
- § 5 GmbHG
- § 107 AktG

### Leitentscheidungen

- BGH II ZR 25/82
- BFH I R 53/08

---

## Skill: `dd-findings-extraktion`

_Liest Datenraum-Dokumente und extrahiert Issues nach den Hauskategorien und Wesentlichkeitsschwellen im Findings-Report-Format. Laden wenn der Nutzer Datenraum prüfen, DD-Issues extrahieren aus [Ordner], Due-Diligence-Prüfung oder was ist im VDR sagt oder auf VDR-Dokumente hinweist im Gesellschaf..._

# DD-Issue-Extraktion (Findings-Report)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `DD-Issue-Extraktion (Findings-Report)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: DD-Issue-Extraktion (Findings-Report)
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Triage zu Beginn

Vor dem Start des DD-Reviews folgende Fragen klären:

1. **Transaktionsstruktur:** Share Deal oder Asset Deal? GmbH oder AG?
2. **Wesentlichkeitsschwelle:** Welcher Mindestvertragswert ist zu prüfen (aus Praxisprofil)?
3. **Prüfkategorien:** Welche Kategorien sind für diesen Deal relevant (Gesellschaftsrecht, IP, Arbeitsrecht, Umwelt)?
4. **VDR-Vollständigkeit:** Gibt es offensichtliche Lücken (fehlende Kategorien, Platzhalter-Dokumente)?
5. **DD-Tiefe:** Full Legal DD oder Red-Flag-Review?
6. **Zeitplan:** Wann muss der Findings-Report vorliegen (Signing-Druck)?

## Zentrale Normen

§§ 311 Abs. 2, 241 Abs. 2 BGB (vorvertragliche Aufklärungspflichten) — § 442 BGB (Kenntnis des Käufers) — § 443 BGB (Garantien) — § 15 GmbHG (Abtretung GmbH-Anteile) — § 40 GmbHG (Gesellschafterliste) — § 613a BGB (Betriebsübergang) — §§ 35 ff. GWB (Fusionskontrolle) — Art. 28 DSGVO (Auftragsverarbeitung) — §§ 142, 144 ZPO (Urkundenvorlegung)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Zweck

Der Datenraum hat 2.000 Dokumente. Irgendwo darin befinden sich die 30, die für den Deal entscheidend sind. Dieser Skill liest Dokumente gegen die DD-Kategorien und Wesentlichkeitsschwellen aus dem Praxisprofil, extrahiert Issues und schreibt sie im Hausformat.

**Vorprozessuale Beweiserhebung im deutschen Recht.** Die Due Diligence (Sorgfaltsprüfung) in deutschen M&A-Transaktionen läuft ausschließlich über den virtuellen Datenraum (VDR – Virtual Data Room), den Frage-Antwort-Prozess (Q&A) und den Disclosure Letter (Offenlegungserklärung). Was nicht offengelegt wurde, ist weder bekannt noch garantiert – das im SPA (Share Purchase Agreement, Unternehmenskaufvertrag) verankerte Garantieregime modifiziert insoweit den allgemeinen Grundsatz, dass der Käufer das Risiko nicht offenbarter Mängel trägt. Gesetzliche Auskunftsansprüche im Streitfall: §§ 142, 144 ZPO; § 810 BGB; §§ 242, 259, 666 BGB; Art. 15 DSGVO; § 254 ZPO (Stufenklage).

## Eingaben

- Praxisprofil: `## M&A → DD-Struktur` (Kategorien, Schwellen)
- Praxisprofil: `## M&A → Issues-Memo-Format`
- Mandats-Kontext: `mandate/[code]/deal-kontext.md`
- VDR-Inventar oder Dokumentenliste

## Schritt-für-Schritt-Workflow

### Schritt 1: VDR-Inventarisierung

Falls VDR-Connector (Box/Datasite/Intralinks) verbunden: Index abrufen. VDR-Ordner auf DD-Anforderungskategorien abbilden. Lücken notieren – Kategorien ohne VDR-Inhalt.

```markdown

## VDR-Inventar: [Deal-Code]

| Anforderungskategorie | VDR-Ordner | Dokumente | Status |
|---|---|---|---|
| Gesellschaftsrecht / Verfassung | /01-Gesellschaft | 45 | Geprüft |
| Wesentliche Verträge | /02-Verträge | 312 | In Bearbeitung |
| IP / Technologie | /03-IP | 89 | Nicht begonnen |
| Arbeitnehmer | /04-HR | 120 | Nicht begonnen |
| Rechtstreitigkeiten / Behörden | /05-Streitigkeiten | 23 | Geprüft |
```

**Lücken:** [Anforderungskategorien ohne VDR-Inhalt – Nachforderung erforderlich]

### Schritt 2: Wesentlichkeitsschwelle anwenden

Gemäß Praxisprofil und Mandats-Kontext-Schwellen. Nicht alles prüfen, wenn die Schwelle Verträge über einem bestimmten Betrag vorschreibt.

Bei Verträgen: nach angegebenem Wert oder nach Gegenparteirelevanz sortieren. Top-down prüfen bis Schwelle erreicht oder Kategorie erschöpft.

### Schritt 3: Issues extrahieren

Je gelesenes Dokument gegen den Standardkatalog für seine Kategorie prüfen:

**Gesellschaftsrecht / Verfassung:**
- Gesellschaftsvertrag / Satzung vollständig und aktuell?
- Kapitalaufbringung nachgewiesen (§§ 7, 19 GmbHG; §§ 36, 54 AktG)?
- Gesellschafterstruktur und Gesellschafterliste (§ 40 GmbHG) korrekt?
- Vinkulierungsklauseln, Vorkaufsrechte, Mitziehrechte?
- Beirat oder Gesellschafterausschuss mit eingeschränkten Rechten?
- Nachschuss-/Einziehungsklauseln (§§ 26, 34 GmbHG)?

**Wesentliche Verträge:**
- Change-of-Control-Klausel (ausgelöst durch diesen Deal? Zustimmung erforderlich?)
- Abtretungsbeschränkung (kann der Vertrag auf Käufer übergehen?)
- Exklusivität / Wettbewerbsverbot
- Kündigungsrechte wegen des Deals
- Ungewöhnliche Haftungsregelungen; AGB-Kontrolle §§ 305 ff. BGB

**IP / Technologie:**
- Eigentumsnachweis (Abtretungen von Gründern/Arbeitnehmern vorhanden? § 69b UrhG; § 4 ArbNErfG)
- Open Source im Produkt (Copyleft-Risiko? GPL/LGPL/AGPL)
- Datenschutz (Verarbeitungsverzeichnis Art. 30 DSGVO; technisch-organisatorische Maßnahmen Art. 32 DSGVO)

**Arbeitnehmer:**
- Change-of-Control-Abfindungsansprüche
- Risiko Betriebsübergang § 613a BGB (Unterrichtungspflicht; Widerspruchsrecht 1 Monat)
- Betriebsrat (§ 102 BetrVG Kündigung; § 111 BetrVG Betriebsänderung)
- Scheinselbstständigkeit (§ 611a BGB; Nachzahlungsrisiko Sozialversicherung)

**Rechtsstreitigkeiten / Behörden:**
- Anhängige Verfahren und Rückstellungen
- Behördliche Anfragen oder laufende Prüfungen
- Kartellrecht / BKartA-Verfahren

### Schritt 4: Finding formulieren

> **Quellenattribution.** Bei Verweis auf Normen, Rechtsprechung oder Behördenmaßnahmen mit entsprechendem Tag versehen: `[juris]`, `[beck-online]`, `[Westlaw DE]` bei Zitaten aus Recherchetool; `[Modellwissen — prüfen]` bei Zitaten aus Modellwissen; `[Nutzer bereitgestellt]` bei VDR- oder Deal-Team-Quellen.

Je Finding-Vorlage aus Praxisprofil:

```
Finding #N: [Titel]
Kategorie: [Anforderungskategorie]
Schweregrad: [Stufe nach Hausschema]
Dokumente: [VDR-Pfad + Dokumentenname]
Finding: [Was das Dokument aussagt und warum es relevant ist]
Empfehlung: [Preisanpassung / Einbehalt / Zustimmung erforderlich / Garantie / Vertragsabbruch]
Vollzugshandlung: [ja – Zustimmung erforderlich / nein]
```

**Schweregradeinstufung:**
- Rot **Blockierend:** Beeinflusst Deal-Wert oder -struktur.
- Orange **Hoch:** Erheblich, aber lösbar.
- Gelb **Mittel:** Klärungsbedarf; lösbar.
- Gruen **Niedrig:** Für die Akte vermerkt.

### Schritt 5: Bericht je Kategorie

Findings nach Anforderungskategorie gruppieren. Innerhalb der Kategorie nach Schweregrad sortieren.

### Schritt 6: Batch-Verarbeitung

Für große Kategorien (300 Verträge): in Chargen verarbeiten. Nach jeder Charge laufende Issues-Liste aktualisieren und blockierende Punkte sofort melden.

## Output-Template

**Adressat:** Deal-Team (Lead Counsel) — **Tonfall:** sachlich-juristisch, präzise

```
[VERTRAULICH — ANWALTLICHES ARBEITSERGEBNIS]

> Dieses Ergebnis entstammt VDR-Materialien, die vertraulich oder privilegiert
> oder beides sind. Verteilung außerhalb des Vertraulichkeitskreises kann den
> Schutz aufheben.

### DD-Issues: [DEAL-CODE] — [KATEGORIE]
Erstellt: [DATUM] | Bearbeiter: [NAME]

Geprüfte Dokumente: [N] von [M] in Kategorie
Abdeckung: [Alle | >X EUR-Schwelle | Top-N]
Findings: [N] blockierend [N] hoch [N] mittel [N] niedrig

---

## Zusammenfassung

[N] blockierend · [N] hoch · [N] mittel — [das Eine, was das Deal-Team wissen muss]

---

## Finding #1: [TITEL]

Kategorie: [KATEGORIE]
Schweregrad: [STUFE]
Dokument: [VDR-PFAD/DOKUMENTENNAME]

**Sachverhalt:**
[Was das Dokument konkret aussagt]

**Rechtliche Bewertung:**
[Norm + Folge]

**Empfehlung:**
[Preisanpassung / Einbehalt / Zustimmung einholen / Garantie verlangen]

**Vollzugshandlung:** [ja/nein]

---

## Lücken

- [Anforderungspunkt ohne responsive Dokumente]
- [Referenziertes Dokument nicht im VDR]
```

## Rote Schwellen

- Change-of-Control bei wesentlichen Verträgen (Umsatzanteil >10 %) → sofortige Eskalation an Deal-Lead
- IP-Eigentumsluecke bei Kerntechnologie → blockierendes Finding; Abtretungs-Chain prüfen
- Betriebsübergang § 613a BGB ohne Unterrichtungsplan → Vollzugsverzögerung droht
- Fehlende aktuelle Gesellschafterliste (§ 40 GmbHG) → gutgläubiger Erwerb Dritter möglich
- BKartA-Verfahren oder FDI-Prüfung offen → Vollzugsverbot beachten (§ 41 GWB)

## Übergaben

- **An ki-werkzeug-uebergabe:** Bei Nutzung von Luminance/Kira massenhafte Vertragsextraktion dorthin übergeben.
- **An dealteam-zusammenfassung:** Aggregierte Findings speisen das Deal-Team-Briefing.
- **An wesentliche-vertraege-anlage:** Vertragsextraktionen speisen die Disclosure Schedule.
- **An vollzugs-checkliste:** Jedes Finding, das eine diskrete Vollzugshandlung impliziert.

## Quellen und Zitierweise

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Was dieser Skill nicht tut

- Er trifft keine Wesentlichkeitsentscheidung bei Grenzfällen. Er wendet die Schwelle an; ein Mensch entscheidet über den Grenzfall.
- Er verhandelt keine Garantien. Er erstellt die Findings, die deren Inhalt informieren.
- Er ersetzt keine KI-Massenprüfung. Für hochvolumige Klauselextraktion an ki-werkzeug-uebergabe übergeben.

---

## Skill: `geschaeftsfuehrer-haftung-43-gmbhg`

_Geschäftsführer haftet persoenlich oder Gesellschaft klagt gegen ihn auf Schadensersatz nach Insolvenz. Prüfraster § 43 GmbHG Sorgfalt ordentlicher Geschäftsmann Business Judgement Rule analog § 93 Abs. 1 Satz 2 AktG. Insolvenzantragspflicht-Verletzung § 15a InsO Zahlungsverbot § 15b InsO Complia..._

# Geschäftsführer-Haftung § 43 GmbHG prüfen

## Arbeitsbereich

Geschäftsführer haftet persoenlich oder Gesellschaft klagt gegen ihn auf Schadensersatz nach Insolvenz. Prüfraster § 43 GmbHG Sorgfalt ordentlicher Geschäftsmann Business Judgement Rule analog § 93 Abs. 1 Satz 2 AktG. Insolvenzantragspflicht-Verletzung § 15a InsO Zahlungsverbot § 15b InsO Compliance-Pflichten Steuer-Haftung § 69 AO Sozialversicherung § 266a StGB. Entlastung Sperrwirkung Beweislast Verjährung fuenf Jahre § 43 Abs. 4 GmbHG. D&O-Versicherung Selbstbehalt. Output Haftungs-Prüf-Memo mit Risikoampel Verteidigungs-Argumenten oder Schadensersatz-Berechnung. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Geschäftsführer-Haftung § 43 GmbHG prüfen` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Geschäftsführer-Haftung § 43 GmbHG prüfen
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Triage zu Beginn

Vor Beginn des Haftungsprüfrasters folgende Fragen klären:

1. **Mandantenrolle:** Auf welcher Seite steht der Mandant — GF als Beklagter oder Gesellschaft/Insolvenzverwalter als Kläger?
2. **Konkrete Pflichtverletzung:** Welche Handlung oder Unterlassung wird vorgeworfen?
3. **Schaden bezifferbar:** Liegt ein konkreter bezifferter Schaden vor oder nur Schadensverdacht?
4. **Verjährung:** Wann ist die Pflichtverletzung eingetreten? (5 Jahre, § 43 Abs. 4 GmbHG)
5. **D&O-Deckung:** Besteht eine D&O-Versicherung? Wurden vorvertragliche Anzeigepflichten erfüllt?
6. **Entlastungsbeschluss:** Wurde der GF entlastet (§ 46 Nr. 5 GmbHG)? Sperrwirkung prüfen.
7. **Insolvenz:** Ist die Gesellschaft insolvent oder war sie es bei der Pflichtverletzung?

## Zentrale Normen

§ 43 GmbHG (Haftung des Geschäftsführers) — § 43 Abs. 4 GmbHG (Verjährung 5 Jahre) — § 93 AktG (Sorgfaltsmaßstab AG-Vorstand; analog für GmbH-GF) — § 46 Nr. 5 GmbHG (Entlastung durch GV) — § 15a InsO (Insolvenzantragspflicht; 3-Wochen-Frist) — § 15b InsO (Zahlungsverbot nach Insolvenzreife) — § 69 AO (Haftung für Steuerschulden) — § 266a StGB (Vorenthalten von Sozialversicherungsbeiträgen) — § 266 StGB (Untreue) — § 34 AO (steuerliche Pflichten des gesetzlichen Vertreters)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema: GF-Haftung § 43 GmbHG

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Pflichten-Maßstab § 43 Abs. 1 GmbHG | Sorgfalt eines ordentlichen Geschäftsmannes; konkreter Sorgfaltsmaßstab nach Unternehmensgröße, Branche, Krise | Maßstab festgelegt |
| 2 | Business Judgement Rule | Unternehmerische Entscheidung? Vernünftigerweise zum Wohl der Gesellschaft? Angemessene Informationsgrundlage? Gutgläubig? | BJR greift → keine Haftung / greift nicht → weiter |
| 3 | Pflichtverletzung | Konkrete Handlung oder Unterlassung, die Sorgfaltsmaßstab verletzt | Pflichtverletzung festgestellt |
| 4 | Schaden | Konkrete Schadensbezifferung; Kausalität Pflichtverletzung → Schaden | Schaden quantifiziert |
| 5 | Verschulden | Vorsatz oder Fahrlässigkeit; Beweislast beim GF (§ 93 AktG analog) | Verschulden nachgewiesen/ausgeschlossen |
| 6 | Insolvenzantragspflicht | § 15a InsO: Zahlungsunfähigkeit/Überschuldung festgestellt? 3-Wochen-Frist eingehalten? | Verletzung strafbar; Zivilhaftung §§ 823 Abs. 2 BGB iVm § 15a InsO |
| 7 | Zahlungsverbot § 15b InsO | Zahlungen nach Insolvenzreife? Privileg für bestimmte Zahlungen? | Erstattungspflicht gegenüber Gesellschaft |
| 8 | Steuerrecht § 69 AO | Steuern vorsätzlich oder grob fahrlässig nicht abgeführt? | Persönliche Haftung des GF |
| 9 | Sozialversicherung § 266a StGB | Arbeitnehmeranteile nicht abgeführt? | Strafbarkeit + Zivilhaftung |
| 10 | Entlastung § 46 Nr. 5 GmbHG | Entlastungsbeschluss gefasst? Sperrwirkung prüfen (nur bekannte Sachverhalte) | Klage gesperrt soweit Sperrwirkung reicht |
| 11 | Verjährung § 43 Abs. 4 GmbHG | 5 Jahre ab Pflichtverletzung; Hemmung nach BGB | Verjährt oder Fristnotiz anlegen |
| 12 | D&O-Versicherung | Deckungsumfang; Selbstbehalt; Vorsatz ausgeschlossen; Deckungsablehnung wegen grober Fahrlässigkeit | Deckungszusage oder -ablehnung prüfen |

## Schritt-für-Schritt-Workflow

1. **Sachverhalt chronologisch aufbereiten:** Zeitleiste der Ereignisse (Pflichtverletzung, Schaden, Entlastungsbeschluss, D&O-Anzeige).
2. **Mandantenrolle festlegen:** GF-Verteidigung oder Aktivseite Gesellschaft/Insolvenzverwalter.
3. **BJR prüfen:** Voraussetzungen nach ARAG/Garmenbeck systematisch durchgehen.
4. **Pflichtverletzung herausarbeiten:** Konkrete Handlung oder Unterlassung benennen, Sorgfaltsmaßstab anlegen.
5. **Schaden beziffern:** Konkreter Schaden vs. hypothetisch rechtmäßiges Alternativverhalten.
6. **Insolvenzrisiko screenen:** § 15a InsO-Zeitpunkt bestimmen; Zahlungen nach Insolvenzreife inventarisieren.
7. **Entlastung prüfen:** Beschlusstext und Aktenlage zum Zeitpunkt des Beschlusses analysieren.
8. **Verjährung berechnen:** 5-Jahres-Frist ab konkreter Pflichtverletzung; Hemmungstatbestände prüfen.
9. **D&O anzeigen:** Unverzügliche Anzeige bei Versicherer; Obliegenheitspflichten beachten.
10. **Strategie festlegen:** Verteidigung (BJR + Entlastung + Verjährung) oder Aktivseite (Pflichtverletzung + Schaden + Kausalität).

## Output-Template

**Adressat:** Mandant / Kanzlei intern — **Tonfall:** sachlich-juristisch

```
### Haftungsanalyse Geschäftsführer-Haftung § 43 GmbHG
Gesellschaft: [FIRMA / HRB-NUMMER]
Geschäftsführer: [NAME]
Bearbeitungsstand: [DATUM]

## Sachverhalt
[Chronologische Kurzdarstellung der Pflichtverletzung]

## Haftungsprüfung

| Prüfungspunkt | Bewertung | Norm |
|---|---|---|
| Sorgfaltsmaßstab § 43 Abs. 1 GmbHG | [Maßstab beschrieben] | § 43 Abs. 1 GmbHG |
| Business Judgement Rule | [greift / greift nicht] | § 93 Abs. 1 Satz 2 AktG analog |
| Pflichtverletzung | [bejaht/verneint] | § 43 GmbHG |
| Schaden | [X EUR / noch zu ermitteln] | § 249 BGB |
| Kausalität | [bejaht/verneint] | — |
| Entlastung § 46 Nr. 5 GmbHG | [Sperrwirkung ja/nein] | § 46 Nr. 5 GmbHG |
| Verjährung § 43 Abs. 4 GmbHG | [läuft bis DATUM] | § 43 Abs. 4 GmbHG |
| D&O-Deckung | [gedeckt/abgelehnt/offen] | D&O-Police |

## Insolvenzrechtliche Haftung
[§ 15a InsO: Zeitpunkt Insolvenzreife; Zahlungen nach Insolvenzreife]
[§ 15b InsO: Erstattungspflicht quantifiziert]

## Steuerliche und strafrechtliche Risiken
[§ 69 AO, § 266a StGB — sofern einschlägig]

## Empfehlung
[Aktivseite: Klagefähigkeit bewerten | Verteidigung: Risikobewertung + Strategie]

Fristnotiz: Verjährung läuft ab [DATUM DER PFLICHTVERLETZUNG] + 5 Jahre = [DATUM]
```

## Rote Schwellen

- Insolvenzreife bekannt + Zahlungen fortgesetzt → § 15b InsO-Haftung; sofortige Mandatsanlage Insolvenzrecht
- § 266 StGB (Untreue) im Raum → strafrechtliche Beratung vorab; Selbstbelastungsverbot beachten
- D&O-Anzeige nicht fristgerecht → Obliegenheitsverletzung; Deckungsverlust möglich
- Entlastung ohne Kenntnis der Pflichtverletzung → Sperrwirkung greift nicht; Klage zulässig

## Quellen und Vertiefung

- GmbHG §§ 43, 46, 50: https://www.gesetze-im-internet.de/gmbhg/__43.html
- AktG § 93: https://www.gesetze-im-internet.de/aktg/__93.html
- InsO § 15a (Insolvenzantragspflicht; Frist seit SanInsFoG mit Wirkung 01.01.2021: ohne Antrag 3 Wochen Zahlungsunfaehigkeit/6 Wochen Ueberschuldung — kein Automatismus, sondern Hoechstfrist): https://www.gesetze-im-internet.de/inso/__15a.html
- InsO § 15b (rechtsformneutrales Zahlungsverbot bei Insolvenzreife, in Kraft seit 01.01.2021 durch SanInsFoG, BGBl. I 2020, 3256; ersetzt § 64 GmbHG a.F. und § 92 II AktG a.F.): https://www.gesetze-im-internet.de/inso/__15b.html
- InsO §§ 17, 18, 19: https://www.gesetze-im-internet.de/inso/__17.html ; https://www.gesetze-im-internet.de/inso/__18.html ; https://www.gesetze-im-internet.de/inso/__19.html
- AO § 69: https://www.gesetze-im-internet.de/ao_1977/__69.html
- StGB §§ 14, 263, 266, 266a, 283 ff.: https://www.gesetze-im-internet.de/stgb/__14.html ; https://www.gesetze-im-internet.de/stgb/__266.html ; https://www.gesetze-im-internet.de/stgb/__266a.html
- BGH, Urt. v. 21.04.1997 — II ZR 175/95 (ARAG/Garmenbeck; BGHZ 135, 244): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=21.04.1997&Aktenzeichen=II+ZR+175/95
- Hinweis zur Anwendung: § 15a InsO i.d.F. SanInsFoG (BGBl. I 2020, 3256) — Antragspflicht aufgrund Pandemiefolgen wurde zeitweilig modifiziert (COVInsAG 2020/21), zwischenzeitlich ausgelaufen. Bei Altsachverhalten Stichtag pruefen.
- Rechtsprechung im Uebrigen: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber offizielle oder frei zugaengliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Uebergabe an andere Skills

- `gesellschaftsrecht:gesellschafterbeschluss` — Entlastungsbeschluss prüfen und anfechten
- `gesellschaftsrecht:gesellschafterstreit-loesungsstrategie` — wenn Haftungsvorwurf Teil eines Gesellschafterkonflikts ist
- `gesellschaftsrecht:mandat-triage-gesellschaftsrecht` — wenn Mandat neu aufgenommen wird

---

## Skill: `gesellschafterbeschluss`

_Erstellung, Prüfung und Anfechtung von Gesellschafterbeschluessen in GmbH (47 und 48 GmbHG) und AG (133 ff. AktG); Mehrheitserfordernisse, Beschlussfähigkeit, Formfragen, Protokollführung sowie Nichtigkeit (241 AktG analog) und Anfechtbarkeit (246 AktG analog). Laedt bei Mandaten zur Beschlussfas..._

# Gesellschafterbeschluss – GmbH und AG

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschafterbeschluss – GmbH und AG` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Gesellschafterbeschluss – GmbH und AG
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Triage zu Beginn

Vor der Bearbeitung folgende Fragen klären:

1. **Rechtsform:** GmbH (§§ 47, 48 GmbHG), AG (§§ 121 ff., 133 ff. AktG) oder GmbH & Co. KG?
2. **Beschlussgegenstand:** Was soll beschlossen werden (Satzungsänderung, Kapitalmaßnahme, GF-Bestellung, Gewinnverteilung)?
3. **Ziel des Mandats:** Beschlussvorbereitung, Wirksamkeitsprüfung eines gefassten Beschlusses oder Anfechtungsklage?
4. **Stimmrechte und Quorum:** Liegt der Gesellschaftsvertrag vor? Sonderregeln zu Mehrheiten?
5. **Stimmverbote:** § 47 Abs. 4 GmbHG oder § 136 AktG einschlägig?
6. **Anfechtungsfrist:** Wann wurde der Beschluss gefasst? (1-Monat-Frist analog § 246 Abs. 1 AktG läuft!)

## Zentrale Normen

§ 46 GmbHG (Zuständigkeitskatalog GV) — § 47 GmbHG (Abstimmung; Stimmrechtsausschluss Abs. 4) — § 48 GmbHG (Versammlung; Umlaufverfahren Abs. 2) — § 51 GmbHG (Einberufung; Frist 1 Woche) — § 53 GmbHG (Satzungsänderung; 3/4-Mehrheit; notarielle Beurkundung) — § 121 AktG (Einberufung HV) — § 133 AktG (Mehrheitsprinzip AG) — § 136 AktG (Stimmrechtsverbot AG) — § 241 AktG (Nichtigkeitsgründe; abschließend) — § 243 AktG (Anfechtbarkeit) — § 246 AktG (Anfechtungsklage; 1-Monat-Frist) — § 249 AktG (Nichtigkeitsklage)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema: Gesellschafterbeschluss

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Einberufung | Ladungsform (GmbH: eingeschriebener Brief § 51; AG: § 121 AktG); Ladungsfrist (GmbH: 1 Woche; AG: 30 Tage § 123); Tagesordnung vollständig? | Einberufungsmangel → anfechtbar; Heilung möglich |
| 2 | Beschlussfähigkeit | Quorum aus GV/Satzung; bei GmbH ohne Satzungsregelung: jede ordnungsgemäß einberufene GV beschlussfähig | Quorum-Mangel → Beschluss ungültig |
| 3 | Stimmrechte ermitteln | GmbH: je 1 EUR = 1 Stimme (§ 47 Abs. 2); AG: je Aktie (§ 134 Abs. 1) | Stimmrechtsverteilung festgestellt |
| 4 | Stimmrechtsausschluss | § 47 Abs. 4 GmbHG: Entlastung, Befreiung von Verbindlichkeit, Rechtsverfolgung; § 136 AktG analog | Stimmen stimmbefangener Gesellschafter nicht zählen |
| 5 | Mehrheit berechnen | Einfache Mehrheit (§ 47 Abs. 1 GmbHG; § 133 Abs. 1 AktG); qualifizierte 3/4-Mehrheit bei Satzungsänderung (§ 53 Abs. 2 GmbHG; § 179 Abs. 2 AktG) | Mehrheit erreicht? |
| 6 | Protokollierung | GmbH: Protokoll mit Abstimmungsergebnis; Satzungsänderung notariell beurkunden (§ 53 Abs. 2); AG: § 130 AktG notarielle Beurkundung | Formfehler → § 241 Nr. 2 AktG Nichtigkeit |
| 7 | Anfechtbarkeit | Kausalität des Mangels für Beschlussergebnis (Relevanztheorie Quellenprüfung § 243 Rn. 8)? | Anfechtbar aber nicht nichtig |
| 8 | Nichtigkeit | § 241 AktG analog: fehlende Form, Sittenwidrigkeit, zwingende Gesetzesvorschriften verletzt | Nichtig von Anfang an; jedermann kann einwenden |
| 9 | Anfechtungsklage | Frist: 1 Monat ab Beschlussfassung analog § 246 Abs. 1 AktG; Klage gegen Gesellschaft; LG am Sitz | Fristnotiz anlegen! |
| 10 | Heilung | § 242 AktG (Einberufungsmängel nach 3 Jahren); nicht bei § 241 Nr. 3 und 5 AktG | Heilung möglich → Abwarten sinnvoll? |

## Schritt-für-Schritt-Workflow

1. **Sachverhalt aufnehmen:** Gesellschaftsvertrag/Satzung lesen; Gesellschafterkreis und Stimmrechte ermitteln.
2. **Einberufung prüfen:** Ladungsform, Ladungsfrist, Tagesordnung auf Vollständigkeit.
3. **Beschlussfähigkeit feststellen:** Quorum aus GV/Satzung; alle Gesellschafter erschienen?
4. **Stimmverbote screenen:** § 47 Abs. 4 GmbHG systematisch für jeden TOP durchgehen.
5. **Mehrheit berechnen:** Gesamtstimmen (ohne stimmbefangene); Mehrheitserfordernis je Beschlussgegenstand.
6. **Beschlusstext formulieren:** Präzise, vollständig, widerspruchsfrei; Abstimmungsergebnis als Zahl.
7. **Protokoll vorbereiten:** TOP-Nummerierung, Beschlusstext, Abstimmungsergebnis, Unterschrift Versammlungsleiter; bei Satzungsänderung Notar beauftragen.
8. **Anfechtbarkeit screenen:** Bei vorhandenen Mängeln Kausalität prüfen (Relevanztheorie).
9. **Fristen notieren:** 1-Monat-Frist analog § 246 AktG sofort kalendarisch sichern.
10. **Ausgabe:** Beschlussvorlage oder Anfechtungs-Memo je nach Mandatsinhalt.

## Output-Template

**Adressat:** Gesellschaft / Gesellschafter / Gericht — **Tonfall:** sachlich-juristisch / präzise

### Beschlussvorlage

```
### Gesellschafterbeschluss
[GESELLSCHAFTSNAME], [HRB-NUMMER]
Gesellschafterversammlung vom [DATUM]

## TOP [N]: [BEZEICHNUNG DES TAGESORDNUNGSPUNKTS]

[Beschlusstext — präzise, vollständig]

Abstimmungsergebnis:
Ja-Stimmen: [N] ([PROZENT] %)
Nein-Stimmen: [N] ([PROZENT] %)
Enthaltungen: [N]
Stimmbefangen: [NAME(N)] gem. § 47 Abs. 4 GmbHG wegen [GRUND]

Der Beschluss ist [angenommen / abgelehnt].

[ORT], den [DATUM]

_________________________________
[VERSAMMLUNGSLEITER]
```

### Anfechtungs-Memo

```
### Anfechtungs-Memo: Beschluss [GESELLSCHAFT] v. [DATUM]

Beschlussgegenstand: [BESCHLUSSINHALT]

Mängel:
1. [MANGEL 1] — Norm: [§] — Kausalität: [ja/nein]
2. [MANGEL 2] — Norm: [§] — Kausalität: [ja/nein]

Anfechtungsklage:
Frist: 1 Monat ab [DATUM] = [ABLAUFDATUM]
Klage gegen: [GESELLSCHAFT] (§ 246 Abs. 2 AktG analog)
Zuständiges Gericht: LG [ORT AM SITZ]

Risikobewertung:
[Anfechtungserfolg: hoch/mittel/gering — Begründung]

Empfehlung:
[Klage unverzüglich einreichen / weitere Sachverhaltsaufklärung / Abstehen]
```

## Rote Schwellen

- Anfechtungsfrist 1 Monat analog § 246 Abs. 1 AktG — sofortige Fristnotiz nach Mandatsannahme
- Fehlende notarielle Beurkundung bei Satzungsänderung → Nichtigkeit nach § 241 Nr. 2 AktG analog
- Stimmrechtsausschluss übersehen → Anfechtbarkeit; Heilung nur möglich wenn kein Berechtigter klagt
- Beschlussfähigkeit nicht festgestellt → gesamter Beschluss ungültig; Sitzung zu wiederholen

## Quellen und Zitierweise

- GmbHG §§ 46, 47, 48, 51, 53, 54
- AktG §§ 121, 130, 133, 134, 136, 179, 241, 243, 246, 249

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Uebergabe an andere Skills

- `gesellschaftsrecht:aufsichtsrat-protokoll` — Protokollierung des Beschlusses
- `gesellschaftsrecht:geschaeftsfuehrer-haftung-43-gmbhg` — wenn Beschluss GF-Entlastung betrifft
- `gesellschaftsrecht:gesellschafterstreit-loesungsstrategie` — wenn Beschluss Teil eines Gesellschafterkonflikts ist

---

## Audit-Hinweis (27.05.2026)

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Status: NOT_FOUND — dejure.org findet zum Datum 10.02.2021 kein Urteil unter diesem Aktenzeichen; NZG 2021, 418 nicht verifizierbar.
Maßnahme: Zitat entfernt. Kein Ersatz eingefügt; die gesetzliche Regelung (§ 48 Abs. 2 GmbHG sowie seit 2022 § 48 Abs. 1 S. 2 GmbHG) ist im Skill durch Normtexte abgedeckt.

---

## Skill: `gesellschafterstreit-loesungsstrategie`

_Gesellschafter sind zerstritten Patt-Situation oder Mehrheits-Gesellschafter droht Hinaus-Kündigung. Strategie bei GmbH-Konflikten: Mediation Beschluss-Anfechtungsklage § 246 AktG analog Abberufung Geschäftsführer § 38 GmbHG. Normen § 34 GmbHG Einziehung § 140 HGB analog Ausschluss-Klage § 48 Gmb..._

# Gesellschafterstreit — Lösungsstrategie

## Arbeitsbereich

Gesellschafter sind zerstritten Patt-Situation oder Mehrheits-Gesellschafter droht Hinaus-Kündigung. Strategie bei GmbH-Konflikten: Mediation Beschluss-Anfechtungsklage § 246 AktG analog Abberufung Geschäftsführer § 38 GmbHG. Normen § 34 GmbHG Einziehung § 140 HGB analog Ausschluss-Klage § 48 GmbHG Gesellschafterversammlung. Prüfraster Wertbestimmungs-Verfahren Abfindungsberechnung BGH Verkehrswert Schiedsklausel DIS. Output Konflikt-Strategie-Memo mit Verhandlungskonzept Klageoption und Kostenfolge. Abgrenzung: gesellschafterbeschluss für Beschlussfassung mandat-triage für Erst-Abfrage. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschafterstreit — Lösungsstrategie` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Gesellschafterstreit — Lösungsstrategie
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Triage zu Beginn

Vor dem Start der strategischen Analyse folgende Fragen klären:

1. **Mandantenrolle:** Mehrheitsgesellschafter, Minderheitsgesellschafter, GF als Beklagter oder Erbe?
2. **Konflikttypus:** Two-Tier-50/50, Mehrheit gegen Minderheit, GF-Konflikt oder Familiengesellschaft?
3. **Eskalationsstufe:** Frühphase (persönlich, lösbar) oder fortgeschrittene Eskalation (Klage droht/läuft)?
4. **Existenzgefahr:** Ist die Gesellschaft durch den Streit in ihrer Existenz bedroht?
5. **Schiedsklausel:** Gibt es eine wirksame Schiedsklausel in der Satzung? (Ordentlicher Rechtsweg ggf. gesperrt)
6. **Anfechtungsfrist:** Falls Beschlussfehler relevant — läuft die 1-Monat-Frist analog § 246 AktG?
7. **Abfindungsrelevanz:** Gibt es bereits konkrete Wertvorstellungen oder Satzungsklauseln zur Abfindung?

## Zentrale Normen

§ 38 GmbHG (Abberufung GF; jederzeit möglich) — § 34 GmbHG (Einziehung von Geschäftsanteilen; Satzungserfordernis) — § 47 GmbHG (Abstimmung; Stimmrechtsausschluss) — § 46 Nr. 8 GmbHG (Gesellschafterbeschluss über Klage gegen GF) — § 140 HGB analog (Ausschlusskiage; auf GmbH analog angewendet) — § 626 BGB (außerordentliche Kündigung; auch GF-Anstellungsvertrag) — §§ 241, 243, 246 AktG analog für GmbH (Beschlussmängelrecht) — §§ 935, 940 ZPO (einstweilige Verfügung) — § 1029 ZPO (Schiedsvereinbarung) — § 313 BGB (Störung der Geschäftsgrundlage)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Prüfschema: Gesellschafterstreit-Strategie

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Konflikt-Diagnose | Konflikttypus und Eskalationsstufe bestimmen | Strategierahmen festgelegt |
| 2 | Schiedsklausel | Satzungs-Schiedsklausel vorhanden und wirksam? | Ordentlicher Rechtsweg gesperrt → Schiedsgericht |
| 3 | Fristenlage | Beschluss-Anfechtungsfrist (1 Monat analog § 246 AktG); Abberufungsfrist | Sofortige Fristnotiz |
| 4 | Mediation | Mittlere Eskalation oder Unternehmensexistenz bedroht → Mediation prüfen | Mediationsvorrang oder sofortige Eskalation |
| 5 | Beschluss-Anfechtung | Formfehler? Stimmrechtsausschluss verletzt? Treuepflicht-Verstoß? | Anfechtungsklage analog § 246 AktG |
| 6 | GF-Abberufung | § 38 GmbHG: jederzeit möglich; wichtiger Grund bei § 38 Abs. 2 GmbHG; Anstellungsvertrag separat kündigen | Beschluss GV + Kündigung |
| 7 | Einziehung § 34 GmbHG | Satzungsklausel vorhanden? Einziehungsgrund? Beschluss der GV; Abfindung Verkehrswert | Einziehungsklage vorbereiten |
| 8 | Ausschlussklage | § 140 HGB analog: wichtiger Grund unzumutbar; Klage der Gesellschaft; Abfindung | Klageentwurf |
| 9 | Abfindungsberechnung | Verkehrswert (IDW S 1 Ertragswert) vs. Buchwert-Klausel; Satzungsklausel prüfen auf Sittenwidrigkeit | Wertgutachten beauftragen |
| 10 | Einstweiliger Rechtsschutz | § 935 ZPO: Verfügungsanspruch (Beschlussfehler) und Verfügungsgrund (Eilbedürftigkeit) | Einstweilige Verfügung vorbereiten |
| 11 | BATNA / ZOPA | BATNA beider Seiten; ZOPA ermitteln; wirtschaftliche Folgen ohne Einigung | Verhandlungsrahmen abstecken |
| 12 | Buy-Sell-Klauseln | Russian Roulette / Texas Shootout vorhanden? Aktivierung sinnvoll? | Klausel analysieren und Ablauf simulieren |

## Schritt-für-Schritt-Workflow

1. **Sachverhalt aufnehmen:** Satzung, Gesellschafterliste, Beschlussprotokoll, Anstellungsvertrag GF, Wirtschaftsstatus.
2. **Schiedsklausel prüfen:** DIS/ICC/Ad-hoc; bei wirksamer Klausel Schiedsgericht statt ordentliches Gericht.
3. **Fristen sichern:** Anfechtungsfrist 1 Monat analog § 246 AktG sofort kalendarisch sichern.
4. **Mandantenrolle analysieren:** Welche Instrumente stehen dem Mandanten zur Verfügung?
5. **Mediation erwägen:** Bei mittlerer Eskalation und Unternehmensinteresse immer als Erstweg anbieten.
6. **Optionen-Matrix erstellen:** Alle rechtlichen Instrumente mit Vor-/Nachteilen, Zeitrahmen, Kosten gegenüberstellen.
7. **Strategie festlegen:** Welche Kombination von Instrumenten (Anfechtung + einstweilige Verfügung, Einziehung + Abberufung)?
8. **Abfindungsrahmen abstecken:** IDW S 1-Gutachten beauftragen; Buchwert-Klausel auf Sittenwidrigkeit prüfen.
9. **Verhandlungsposition aufbauen:** BATNA beider Seiten; Verhandlungsziele und Roten Linien festlegen.
10. **Klage oder Vergleich:** Wenn Mediation scheitert: Klageentwurf; Vergleichsangebot parallel vorbereiten.

## Output-Template

**Adressat:** Mandant / Kanzlei intern — **Tonfall:** sachlich-strategisch

```
### Gesellschafterstreit-Strategie
Gesellschaft: [FIRMA / HRB-NUMMER]
Mandant: [NAME + ROLLE]
Bearbeitungsstand: [DATUM]

## Konflikt-Diagnose
Konflikttypus: [Two-Tier / Mehrheit-Minderheit / GF-Konflikt / Familie]
Eskalationsstufe: [Früh / Mittel / Hoch / Existenzgefährdend]
Schiedsklausel: [ja/nein; wenn ja: Ordnung + Ort]

## Fristen (KRITISCH)
Anfechtungsfrist: Beschluss v. [DATUM] → Ablauf [DATUM + 1 Monat]
Weitere Fristen: [AUFLISTUNG]

## Optionen-Matrix

| Option | Instrument | Zeitrahmen | Kosten | Risiko |
|---|---|---|---|---|
| Mediation | Neutral | 4-8 Wochen | mittel | Ergebnisoffen |
| Beschluss-Anfechtung | § 246 AktG analog | 6-18 Monate | mittel-hoch | Kausalität |
| GF-Abberufung | § 38 GmbHG + § 626 BGB | 2-4 Wochen | mittel | Anstellungsvertrag |
| Einziehung | § 34 GmbHG | 3-6 Monate | hoch | Abfindungsstreit |
| Ausschlussklage | § 140 HGB analog | 12-24 Monate | hoch | Beweislast |
| Buy-Sell | Satzungsklausel | 30-90 Tage | abhängig | Liquidität |

## Empfohlene Strategie
[Primärempfehlung + Begründung + Zeitplan]

## Abfindungsrahmen
Buchwert (Satzungsklausel): [X EUR]
Verkehrswert (IDW S 1 Schätzung): [Y EUR]
Sittenwidrigkeitsprüfung: [ja/nein]

## Nächste Schritte
1. [MASSNAHME] bis [DATUM]
2. [MASSNAHME] bis [DATUM]
```

## Rote Schwellen

- Anfechtungsfrist 1 Monat analog § 246 AktG läuft → sofortige Klage oder bewusstes Abstehen dokumentieren
- Gesellschaft zahlungsunfähig während des Konflikts → § 15a InsO; sofort Insolvenzrecht einbeziehen
- Existenzgefährdung durch Pattsituation → einstweilige Verfügung § 935 ZPO prüfen
- Abfindungsklausel Buchwert und Differenz zum Verkehrswert mehr als 50 % → Sittenwidrigkeit § 138 BGB prüfen

## Quellen und Vertiefung

- GmbHG §§ 34, 38, 39, 46, 47
- HGB § 140
- BGB §§ 138, 626, 738
- AktG §§ 241, 246
- ZPO §§ 935, 1029
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Scholz/K. Schmidt, GmbHG, 12. Aufl. 2021, § 34 Rn. 1 ff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.

## Uebergabe an andere Skills

- `gesellschaftsrecht:gesellschafterbeschluss` — Beschlussanfechtung und Nichtigkeitsklage
- `gesellschaftsrecht:geschaeftsfuehrer-haftung-43-gmbhg` — wenn GF-Haftungsvorwürfe Teil des Konflikts
- `gesellschaftsrecht:aufsichtsrat-protokoll` — wenn AR-Gremium in Konflikt involviert
- `gesellschaftsrecht:mandat-triage-gesellschaftsrecht` — Mandatsaufnahme bei neuem Streit

---

## Audit-Hinweis (27.05.2026)

Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Status: WRONG_TOPIC — das Urteil betrifft die Zulaessigkeit von Hinauskuendigungsklauseln in Form einer Vesting-Regelung (Managermodell, BGHZ 164, 98), nicht den Ausschluss analog § 140 HGB. Die Fundstelle NJW 2005, 3569 ist nicht korrekt.
Maßnahme: Beide Nennungen entfernt. Kein Ersatz eingefuegt; der Ausschlussklagen-Stoff ist ueber BGH II ZR 25/82 (Abfindung/Sittenwidrigkeit) und den Normenhinweis § 140 HGB analog teilweise abgedeckt.

---

## Skill: `gesellschafts-compliance`

_Gesellschafts-Compliance-Tracker – Initialisierung, Fälligkeitsbericht, Status-Update, Gesundheits-Audit, Export. Pflegt eine compliance-tracker.yaml aus der Gesellschaftstabelle, berechnet Einreichungsfristen nach Rechtsträger und Rechtsordnung und zeigt auf, was in den nächsten 30/60/90 Tagen f..._

# Gesellschafts-Compliance (§ 325 HGB Bilanzpublizität; § 20 GwG Transparenzregister)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Gesellschafts-Compliance (§ 325 HGB Bilanzpublizität; § 20 GwG Transparenzregister)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Gesellschafts-Compliance (§ 325 HGB Bilanzpublizität; § 20 GwG Transparenzregister)
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Kernsachverhalt

Kapitalgesellschaften und Personengesellschaften unterliegen einer Vielzahl periodisch wiederkehrender gesellschaftsrechtlicher und handelsrechtlicher Pflichten: Jahresabschluss-Offenlegung beim Unternehmensregister (§ 325 HGB), Einreichung der aktuellen Gesellschafterliste beim Handelsregister (§ 40 GmbHG), Meldung wirtschaftlich Berechtigter beim Transparenzregister (§ 20 GwG) sowie — bei prüfungspflichtigen Gesellschaften — Jahresabschlussprüfung (§ 316 HGB). Verstöße gegen diese Pflichten haben unterschiedliche Konsequenzen: Ordnungsgeldverfahren (§ 335 HGB), Bußgelder (§§ 56 f. GwG), strafrechtliche Risiken (§ 331 HGB) und — bei veralteter Gesellschafterliste — Gefährdung des gutgläubigen Erwerbs (§ 16 Abs. 3 GmbHG).

Dieser Skill pflegt einen einzigen YAML-Tracker für alle Gesellschaften eines Mandanten und berechnet, was wann und für wen fällig ist.

## Kaltstart-Rückfragen

Vor der Tracker-Initialisierung sind folgende Angaben erforderlich:

1. **Gesellschaftstabelle:** Welche Gesellschaften sind zu erfassen (Name, Rechtsform, Handelsregisternummer, Registergericht, Gründungsdatum, Geschäftsjahresende)?
2. **Größenklassen:** Bilanzsumme, Umsatzerlöse, Arbeitnehmerzahl für jede GmbH/AG (§ 267 HGB) — um Prüfungspflicht und Offenlegungsumfang zu bestimmen?
3. **Letzter Einreichungsstand:** Wann wurde der Jahresabschluss zuletzt beim Bundesanzeiger eingereicht? Liegt die aktuelle Gesellschafterliste beim Handelsregister?
4. **Transparenzregister:** Sind wirtschaftlich Berechtigte (§ 3 GwG) im Transparenzregister eingetragen oder gilt eine Eintragungsausnahme nach § 20 Abs. 2 GwG (Eintragung im Handelsregister)?
5. **Konzernstruktur:** Gibt es Mutter-Tochter-Verhältnisse, die einen Konzernabschluss nach §§ 290 ff. HGB auslösen könnten?
6. **Ruhende oder aufzulösende Gesellschaften:** Sind Gesellschaften betrieblich inaktiv? Sollen sie aufgelöst werden (§ 65 GmbHG, §§ 264 ff. AktG)?
7. **Ausländische Tochtergesellschaften:** Gibt es § 325a HGB-Pflichten für ausländische Tochtergesellschaften?
8. **Berichtszeitraum:** 30, 60 oder 90 Tage für den Fälligkeitsbericht?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtlicher Rahmen

### Normtexte mit Auszügen

**§ 325 Abs. 1 HGB — Bilanzpublizität (Offenlegungspflicht)**
> "Die gesetzlichen Vertreter von Kapitalgesellschaften haben [...] den Jahresabschluss und den Lagebericht [...] beim Betreiber des Bundesanzeigers elektronisch einzureichen."

Frist: § 325 Abs. 1a HGB — spätestens 12 Monate nach Ende des Geschäftsjahres. Kleine Kapitalgesellschaften (§ 267 Abs. 1 HGB) können vereinfachte Unterlagen einreichen; nur Bilanz und Anhang, kein GuV-Ausweis.

**§ 335 HGB — Ordnungsgeldverfahren**
> Wer § 325 HGB verletzt, kann vom Bundesamt für Justiz (BfJ) zur Einreichung angehalten und mit Ordnungsgeld belegt werden. Mindestordnungsgeld: 2.500 EUR; Maximum: 25.000 EUR je Verstoß. Verfahren beginnt von Amts wegen, sobald fristgerecht keine Einreichung erfolgt.

**§ 40 GmbHG — Gesellschafterliste**
> "Notare, die in Angelegenheiten der Gesellschaft tätig werden, haben [...] eine von ihnen unterschriebene, aktualisierte Gesellschafterliste [...] zum Handelsregister einzureichen."

Frist: unverzüglich nach jeder Änderung (Abtretung, Kapitalerhöhung, Erbfolge). Pflicht des Notars bei notarieller Beurkundung; sonst Geschäftsführer (§ 40 Abs. 2 GmbHG). Konsequenz veralteter Liste: Gutgläubiger Erwerb nach § 16 Abs. 3 GmbHG kann zustande kommen, wenn Erwerber auf die unrichtige Liste vertraut.

**§ 16 Abs. 3 GmbHG — Gutgläubiger Erwerb**
> "Ist die im Handelsregister eingetragene Gesellschafterliste unrichtig, so kann ein Erwerber, der auf die Richtigkeit der Liste vertraut, gutgläubig Anteile erwerben."

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**§§ 18 ff., 20 GwG — Transparenzregister**
> § 20 GwG verpflichtet juristische Personen des Privatrechts und eingetragene Personengesellschaften, die wirtschaftlich Berechtigten (§ 3 GwG) beim Transparenzregister anzumelden.

Frist: 2 Wochen nach Änderung der Beteiligungsverhältnisse. Ausnahme: § 20 Abs. 2 GwG — Eintragungspflicht gilt nicht, wenn die wirtschaftlich Berechtigten bereits aus öffentlich zugänglichen Registern (Handelsregister, Genossenschaftsregister) erkennbar sind. Seit 01.08.2021 ist das Transparenzregister ein Vollregister (keine reine Auffangfunktion mehr); § 59 Abs. 1 GwG: Übergangsfrist bis 31.03.2022 für GmbH.

**§ 267 HGB — Größenklassen**

| Klasse | Bilanzsumme | Umsatzerlöse | Arbeitnehmer (Jahresdurchschnitt) |
|---|---|---|---|
| Klein (§ 267 Abs. 1 HGB) | ≤ 7.500.000 EUR | ≤ 15.000.000 EUR | ≤ 50 |
| Mittelgroß (§ 267 Abs. 2 HGB) | ≤ 25.000.000 EUR | ≤ 50.000.000 EUR | ≤ 250 |
| Groß (§ 267 Abs. 3 HGB) | > 25.000.000 EUR | > 50.000.000 EUR | > 250 |

Zwei von drei Merkmalen müssen an zwei aufeinanderfolgenden Abschlussstichtagen erfüllt sein (§ 267 Abs. 4 HGB). `[Modellwissen — Schwellenwerte beim BfJ/Unternehmensregister bestätigen]`

**§ 316 HGB — Prüfungspflicht**
> "Der Jahresabschluss und der Lagebericht von Kapitalgesellschaften, die nicht kleine Kapitalgesellschaften sind, sind durch einen Abschlussprüfer zu prüfen."

Gilt für alle AG (keine Größenklassenausnahme). GmbH: Prüfungspflicht ab mittelgroß. Ohne Testierung darf der Abschluss nicht festgestellt werden.

**§ 290 HGB — Konzernabschlusspflicht**
> "Die gesetzlichen Vertreter einer Kapitalgesellschaft haben einen Konzernabschluss und einen Konzernlagebericht aufzustellen, wenn diese Kapitalgesellschaft auf eine andere Gesellschaft einen beherrschenden Einfluss ausüben kann."

**§ 325a HGB — Zweigniederlassungen ausländischer Gesellschaften**
> Bestimmte ausländische Gesellschaften mit Zweigniederlassung in Deutschland müssen Jahresabschlüsse in Deutschland offenlegen.

### Leitentscheidungen

| Gericht | Aktenzeichen | Fundstelle | Relevanz |
|---|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | - | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

## Prüfschema: Compliance-Initialisierung und laufender Betrieb

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

| Schritt | Prüfungspunkt | Inhalt | Ergebnis |
|---|---|---|---|
| 1 | Gesellschaftserfassung | Alle Gesellschaften mit Rechtsform, HR-Nummer, Gründungsdatum, GJ-Ende erfasst? | Vollständige Gesellschaftsliste als Basis des Trackers |
| 2 | Größenklassenbestimmung | § 267 HGB: Bilanzsumme, Umsatz, Arbeitnehmer für jede GmbH/AG; zwei-Kriterien-Test an zwei aufeinanderfolgenden Stichtagen | Festlegung der Offenlegungspflicht und des Prüfungsumfangs |
| 3 | Prüfungspflicht | § 316 HGB: AG (immer); GmbH mittelgroß/groß; Stiftungen / Genossenschaften nach §§ 340, 341 HGB? | Bestellung Abschlussprüfer vor GJ-Ende; Listenmandant: Jahresplan |
| 4 | Offenlegungsfrist § 325 HGB | 12 Monate nach GJ-Ende; bei börsennotierter AG: 4 Monate (§ 325 Abs. 4 HGB)? | Fälligkeitsdaten in Tracker eintragen; Frühwarnung 90 Tage vor Frist |
| 5 | Gesellschafterliste § 40 GmbHG | Letzte Einreichung beim HR; Änderungen seit letzter Einreichung (Abtretungen, Kapitalerhöhungen, Erbfolgen)? | Unverzügliche Einreichung bei Änderung; Stichtag des aktuellen Standes notieren |
| 6 | Transparenzregister § 20 GwG | Wirtschaftlich Berechtigte eingetragen? Eintragungsausnahme § 20 Abs. 2 GwG geprüft? | Bei fehlender oder veralteter Eintragung: 2-Wochen-Frist nach Änderung beachten |
| 7 | Konzernabschluss § 290 HGB | Beherrschender Einfluss auf andere Gesellschaften? Befreiungsmöglichkeit §§ 291–293 HGB (Konzern-Muttergesellschaft im Ausland)? | Konzernabschluss-Pflicht oder Befreiungssachverhalt dokumentieren |
| 8 | Ruhende Gesellschaften | Gesellschaft operativ inaktiv? Auflösung geplant? Tragekosten berechnet (HR-Gebühren, Steuer, RA-Honorar)? | Auflösung bei wirtschaftlich sinnloser Fortführung empfehlen (§ 65 GmbHG) |
| 9 | Ordnungsgeldgefahr | Einreichungsfrist überschritten ohne Einreichung? BfJ-Verfahren bereits eingeleitet? | Sofortige Nachreichung + Stellungnahme zum Ordnungsgeldantrag |
| 10 | Status-Pflege | Alle erledigten Pflichten im Tracker mit Datum und Nachweis (Bundesanzeiger-Veröffentlichungsnummer, HR-Eintragungsdatum) aktualisiert? | Lückenloser Einreichungsnachweis für M&A-Due-Diligence und Behörden |
| 11 | 30/60/90-Tage-Vorschau | Welche Pflichten werden in den nächsten 30, 60 oder 90 Tagen fällig? | Fälligkeitsbericht für Mandant und Kanzleikalender |
| 12 | Jahresabschluss-Feststellung | Feststellung des Jahresabschlusses vor Offenlegung: bei GmbH durch Gesellschafterversammlung (§ 46 Nr. 1 GmbHG); bei AG durch Vorstand + AR oder HV (§§ 172 f. AktG)? | Organübergreifende Terminplanung: Prüfung → Feststellung → Offenlegung |
| 13 | Jahresabschluss-Feststellungsfrist | § 264 Abs. 1 HGB: Kaufmännischer Jahresabschluss muss innerhalb der einem ordnungsgemäßen Geschäftsgang entsprechenden Zeit aufgestellt werden | Bei GmbH: spätestens in 3 Monaten nach GJ-Ende (§ 264 Abs. 1 S. 3 HGB, i.d.F. BilMoG) |
| 14 | Export und Reporting | Tracker exportiert als CSV / Tabelle für Mandant, Steuerberater, WP? | Jahresplanung mit externen Beratern abgestimmt |
| 15 | Audit-Nachverfolgung | Letzte Audit-Überprüfung > 12 Monate zurück? Transparenzregister nicht geprüft? | Gesundheits-Audit durchführen (Modus 4) |

## Beweislast

| Frage | Beweislast | Erläuterung |
|---|---|---|
| Fristgerechte Offenlegung § 325 HGB | Gesellschaft / gesetzlicher Vertreter | Nachweis durch Bundesanzeiger-Veröffentlichungsnummer und Datum |
| Gutgläubiger Erwerb § 16 Abs. 3 GmbHG | Erwerber muss Gutgläubigkeit darlegen | Unrichtigkeit der Liste: objektiv; Kenntnis des Erwerbers: subjektiv (Erwerber muss fehlendes Wissen beweisen) |
| Ordnungsgemäße Transparenzregister-Eintragung | Gesellschaft (Transparenzregister-Auszug als Nachweis) | Bußgeldverfahren: Behörde trägt Beweislast für den Verstoß; Gesellschaft muss Eintragung nachweisen |
| Prüfungspflicht besteht nicht (§ 316 HGB) | Gesellschaft (Nachweis Kleinunternehmen nach § 267 HGB) | Nachweis durch Jahresabschluss der zwei vorangegangenen Geschäftsjahre |
| Gesellschafterliste aktuell (§ 40 GmbHG) | Notar / Geschäftsführer | Nachweis durch aktuellen HR-Auszug mit Datumsangabe der letzten Änderung |

## Fristen und Verjährung

| Pflicht | Frist | Norm | Konsequenz bei Versäumnis |
|---|---|---|---|
| Jahresabschluss-Offenlegung | 12 Monate nach GJ-Ende | § 325 Abs. 1a HGB | Ordnungsgeldverfahren BfJ (§ 335 HGB); mind. 2.500 EUR |
| Jahresabschluss-Offenlegung börsennotierte AG | 4 Monate nach GJ-Ende | § 325 Abs. 4 HGB | Zusätzlich WpHG-Sanktionen, MAR-Pflichten |
| Gesellschafterliste | Unverzüglich nach Änderung | § 40 GmbHG | Gutgläubiger Erwerb (§ 16 Abs. 3 GmbHG); Haftung Geschäftsführer |
| Transparenzregister-Eintragung | 2 Wochen nach Änderung | § 20 GwG | Bußgeld §§ 56 f. GwG bis 1.000.000 EUR (vorsätzlich) oder 500.000 EUR (fahrlässig) |
| Jahresabschluss-Aufstellung GmbH | 3 Monate nach GJ-Ende | § 264 Abs. 1 S. 3 HGB | Pflichtverletzung Geschäftsführer; Schadensersatz § 43 GmbHG |
| HV-Einberufung AG | Binnen 8 Monate nach GJ-Ende | § 175 AktG | Ordnungswidrigkeitenrisiko; Aktionärsrechte gefährdet |
| Konzernabschluss-Offenlegung | 12 Monate nach GJ-Ende | § 325 HGB i.V.m. § 290 HGB | Ordnungsgeldverfahren BfJ |
| Ordnungsgeld-Widerspruch | 1 Monat nach Zustellung | § 335 Abs. 3 HGB | Ordnungsgeld wird bestandskräftig |
| Verjährung Ordnungsgeldbescheid | 3 Jahre (Verjährungsfrist OWiG) | § 31 OWiG | Nach Ablauf kein Vollzug mehr |

## Typische Gegenargumente

| Einwand | Begründung Gegenseite | Erwiderung |
|---|---|---|
| Kleine GmbH muss keinen GuV offenlegen | § 326 HGB: kleine GmbH nur Bilanz + Anhang | Richtig — aber Bilanz + Anhang müssen trotzdem fristgerecht eingereicht werden; häufig wird auch die verkürzte Offenlegung versäumt |
| Gesellschafterliste ist aktuell — Notar hat nicht gehandelt | Pflicht liegt beim Notar (§ 40 Abs. 1 GmbHG) | Bei eigener Erkenntnis der Änderung trifft den Geschäftsführer Subsidiärpflicht (§ 40 Abs. 2 GmbHG); Haftungsrisiko des GF prüfen |
| Transparenzregister-Eintragung entbehrlich wegen HR-Eintragung | § 20 Abs. 2 GwG: Mitteilung entbehrlich, wenn Angaben aus anderen Registern erkennbar | Seit 01.08.2021 Vollregister; Ausnahme gilt nur noch für exakt übereinstimmende Angaben; im Zweifel aktiv eingetragen lassen |
| Offenlegung verspätet, aber Ordnungsgeldverfahren noch nicht eingeleitet | Kein Schaden eingetreten | BfJ leitet Verfahren von Amts wegen ein; nachträgliche Einreichung mindert das Ordnungsgeld, hebt es aber nicht auf; unverzügliche Nachreichung + Erklärung einreichen |
| GJ nicht zum 31.12 — Frist läuft anders | Richtig: 12 Monate nach individuellem GJ-Ende | Tracker muss GJ-Ende je Gesellschaft individuell erfassen; Standardannahme 31.12. kann falsch sein |
| Prüfungspflicht entfällt, weil Gesellschaft geschrumpft | § 267 Abs. 4 HGB: Größenklassenwechsel erst nach zwei aufeinanderfolgenden Abschlussstichtagen | Prüfungspflicht besteht noch ein weiteres Jahr nach Unterschreiten der Schwellen |

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Compliance-Programm initialisierten oder pruefen | Compliance-Schema nach Checkliste; Template unten |
| Variante A — Kleines Unternehmen kein Budget für umfangreiches Programm | Minimalanforderungen-Compliance-Set statt Vollprogramm |
| Variante B — Branchenspezifische Anforderungen GwG DSGVO | Branchen-spezifisches Compliance-Modul einsetzen |
| Variante C — Bereits Ermittlungsverfahren laeuft | Compliance-Untersuchung als Verteidigung; Kooperation mit Behörden |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Schriftsatzbausteine

### Baustein 1: Widerspruch gegen Ordnungsgeldbescheid (§ 335 HGB)

```
An das
Bundesamt für Justiz
Referat IV 4
53094 Bonn

[Mandant / Gesellschaft]
[Anschrift]

[Ort, Datum]

Az. [Ordnungsgeldaktenzeichen]

Widerspruch gegen den Ordnungsgeldbescheid vom [Datum]

Sehr geehrte Damen und Herren,

wir vertreten die [Gesellschaft], [HR-Nummer], [Anschrift], in der oben bezeichneten
Angelegenheit. Gegen den Ordnungsgeldbescheid vom [Datum], der unserer Mandantin am
[Datum] zugegangen ist, legen wir hiermit

 W i d e r s p r u c h

ein.

Begründung:

Der Jahresabschluss der [Gesellschaft] für das Geschäftsjahr [Jahr] wurde am [Datum] beim
Betreiber des Bundesanzeigers eingereicht. Der Bundesanzeiger-Veröffentlichungscode lautet:
[Code].

Die verspätete Einreichung ist auf [konkrete Begründung: Prüfungsverzögerung durch
Wirtschaftsprüfer / IT-Umstellung / externe Umstände] zurückzuführen, für die der
gesetzliche Vertreter keine Verantwortung trägt. Wir bitten, dies bei der
Ordnungsgeldbemessung zu berücksichtigen.

Wir bitten höflich, das Ordnungsgeldverfahren einzustellen und den Bescheid aufzuheben.

Mit freundlichen Grüßen
[Kanzlei / Name]
Rechtsanwalt / Rechtsanwältin

Anlage: Bundesanzeiger-Veröffentlichungsbestätigung vom [Datum]
```

### Baustein 2: Aufforderungsschreiben an Geschäftsführer zur Einreichung Gesellschafterliste

```
An den Geschäftsführer
[Name GmbH]
[Anschrift]

[Ort, Datum]

Handelsregister-Einreichung der Gesellschafterliste (§ 40 GmbHG) — dringende Fristsetzung

Sehr geehrter Herr/Frau [Name],

in Ihrer Eigenschaft als Geschäftsführer der [Name GmbH] sind Sie gemäß § 40 Abs. 2
GmbHG verpflichtet, nach jeder Änderung der Beteiligungsverhältnisse eine aktualisierte
Gesellschafterliste unverzüglich zum Handelsregister einzureichen.

Die Abtretung der Geschäftsanteile des Herrn [Name] an [Erwerber] wurde am [Datum]
notariell beurkundet und ist noch nicht in der beim Handelsregister hinterlegten
Gesellschafterliste (Stand: [Datum]) eingetragen.

Wir fordern Sie auf, spätestens bis zum [Datum = 10 Tage] die aktualisierte
Gesellschafterliste beim Amtsgericht [Registergericht] zur Aufnahme in das
Handelsregister einzureichen.

Wir weisen darauf hin, dass eine nicht ordnungsgemäß eingetragene Gesellschafterliste
das Risiko eines gutgläubigen Erwerbs gemäß § 16 Abs. 3 GmbHG begründet.

Mit freundlichen Grüßen
[Kanzlei / Name]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

### Baustein 3: Gesellschafts-Compliance-Tracker YAML (vollständig)

```yaml
### Gesellschafts-Compliance-Tracker
### Erstellt: [JJJJ-MM-TT]
### Zuletzt aktualisiert: [JJJJ-MM-TT]
### HINWEIS: Fristen sind nur Referenz — beim Bundesanzeiger/HR/TR bestätigen

metadaten:
 unternehmen: "[Konzern- / Mandantenname]"
 erstellt: "[Datum]"
 zuletzt_aktualisiert: "[Datum]"
 letztes_audit: null

gesellschaften:
 - name: "Alpha GmbH"
 typ: "GmbH"
 handelsregisternummer: "HRB 12345"
 registergericht: "Amtsgericht München"
 gruendungsdatum: "2015-01-10"
 status: "aktiv"
 groessenklasse: "mittelgroß § 267 Abs. 2 HGB"
 geschaeftsjahr_ende: "12-31"
 abschlusspruefung_pflicht: "ja"
 gesellschafter_liste_aktuell: "2025-11-15"
 notizen: "Abtretung März 2026 noch nicht eingetragen"

 pflichten:
 - typ: "Jahresabschluss § 325 HGB"
 faellig: "2026-12-31"
 faelligkeits_grundlage: "GJ-Ende 31.12.2025 + 12 Monate"
 zuletzt_eingereicht: "2025-10-15"
 status: "aktuell"
 notizen: "GJ 2025 bis 31.12.2026 einzureichen"

 - typ: "Gesellschafterliste § 40 GmbHG"
 faellig: "2026-04-05"
 faelligkeits_grundlage: "Unverzüglich nach Abtretung März 2026"
 zuletzt_eingereicht: "2025-11-15"
 status: "überfällig"
 notizen: "Abtretung v. 20.03.2026 noch nicht eingetragen; GF aufgefordert"

 - typ: "Transparenzregister § 20 GwG"
 faellig: "2026-04-03"
 faelligkeits_grundlage: "Änderung wirtschaftlich Berechtigter März 2026 + 2 Wochen"
 zuletzt_eingereicht: "2025-11-15"
 status: "überfällig"
 notizen: "Neuer wirtschaftlich Berechtigter nach Abtretung"

 - typ: "Jahresabschlussprüfung § 316 HGB"
 faellig: "2026-05-31"
 faelligkeits_grundlage: "Vor Feststellung und Offenlegung GJ 2025"
 zuletzt_eingereicht: null
 status: "bald_fällig"
 notizen: "Prüfungsauftrag an KPMG erteilt 01.02.2026"
```

## Tracker-Datei (technische Beschreibung)

Pfad: `~/.claude/plugins/config/claude-fuer-deutsches-recht/gesellschaftsrecht/gesellschaften/compliance-tracker.yaml`

**Status-Werte:**
- `aktuell` — eingereicht für laufende Periode; nichts fällig in 90 Tagen
- `bald_fällig` — fällig innerhalb von 90 Tagen
- `überfällig` — Fälligkeitsdatum überschritten ohne eingetragenes Einreichungsdatum
- `unbekannt` — keine Information; manuelle Bestätigung erforderlich

## Wichtiger Hinweis zu Fristen

> Die Einreichungsfristen spiegeln öffentlich verfügbare gesetzliche Anforderungen wider. Fristen und Anforderungen können sich ändern. **Fristen immer mit dem Bundesamt für Justiz (§ 335 HGB), dem Handelsregister oder dem Transparenzregister direkt bestätigen, bevor sie für Compliance-Zwecke verwendet werden.** `[Modellwissen — prüfen]`

## Modus 1: Initialisierung

Ohne Tracker oder mit `--rebuild`.

### Schritt 1: Gesellschaftstabelle laden

Aus Praxisprofil `## Gesellschafts-Compliance` → Gesellschaftstabelle. Falls vorhanden: direkt verwenden. Falls nicht: Kaltstart-Rückfragen stellen.

### Schritt 2: Für jede Gesellschaft Pflichten ermitteln

**GmbH — Standardpflichten:**

| Pflicht | Norm | Frist | Konsequenz bei Verstoß |
|---|---|---|---|
| Jahresabschluss Offenlegung | § 325 Abs. 1 HGB | 12 Monate nach GJ-Ende | Ordnungsgeld BfJ § 335 HGB (mind. 2.500 EUR) |
| Gesellschafterliste | § 40 GmbHG | Unverzüglich nach Änderung | Gutgläubiger Erwerb § 16 Abs. 3 GmbHG; Haftung GF § 43 GmbHG |
| Transparenzregister | § 20 GwG | 2 Wochen nach Änderung | Bußgeld §§ 56 f. GwG bis 1.000.000 EUR |
| Jahresabschlussprüfung | § 316 HGB | Vor Offenlegung (mittelgroß/groß) | Strafbarkeit § 331 HGB; keine Testierung |

**AG — Standardpflichten:**

| Pflicht | Norm | Frist |
|---|---|---|
| Jahresabschluss Offenlegung | § 325 HGB | 12 Monate; börsennotiert: 4 Monate |
| Prüfpflicht | § 316 HGB | Alle AG (keine Größenausnahme) |
| HV-Einberufung (Jahresabschluss) | § 175 AktG | Binnen 8 Monate nach GJ-Ende |
| Transparenzregister | § 20 GwG | 2 Wochen nach Änderung |

### Schritt 3: Tracker schreiben

Compliance-Tracker mit allen Gesellschaften und berechneten Pflichten generieren.

## Modus 2: Bericht

```
/gesellschaftsrecht:gesellschafts-compliance --bericht [--tage 30|60|90|180]
```

```
GESELLSCHAFTS-COMPLIANCE-BERICHT — [Datum]
[Unternehmensname]

ÜBERFÄLLIG ([N]):
 [Gesellschaft] / [Pflicht] — war fällig am [Datum]

FÄLLIG INNERHALB [N] TAGE ([N]):
 [Gesellschaft] / [Pflicht] — fällig [Datum]

KÜRZLICH EINGEREICHT ([N] in letzten 90 Tagen):
 [Gesellschaft] / [Pflicht] — eingereicht [Datum]

UNBEKANNTER STATUS ([N]):
 [Gesellschaft] / [Pflicht] — keine Information; direkt beim Registerführer bestätigen

TRANSPARENZREGISTER:
 Zuletzt geprüft: [Datum]
 Gesellschaften mit aktueller Eintragung: [N] von [N]
 Gesellschaften ohne Prüfung in letzten 12 Monaten: [Liste]
```

## Modus 3: Update

### Folgenreiche-Handlung-Sperre (Einreichung)

Falls Rolle **Nichtjurist**:
> Eine Jahresabschluss-Einreichung beim Bundesanzeiger oder eine Handelsregistereintragung hat rechtliche Konsequenzen. Vor Einreichung mit einem Rechtsanwalt oder Steuerberater besprechen. `[Prüfen]`

Manuelles Update:
> "Jahresabschluss der Alpha GmbH zum 31.12.2025 am 05.03.2026 beim Bundesanzeiger eingereicht."

Massen-Update: Wirtschaftsprüfer-Bericht oder HR-Auszug hochladen; Matching-Gesellschaften automatisch aktualisieren.

## Modus 4: Gesundheits-Audit

```
/gesellschaftsrecht:gesellschafts-compliance --audit
```

**Einreichungs-Compliance:** Überfällige und unbekannte Punkte.

**Gesellschaftsgesundheit:**
- Ruhende Gesellschaften: Auflösung (§ 65 GmbHG) sinnvoller als Weiterbetrieb?
- Fehlende Gründungsdaten: Fristberechnung unzuverlässig.
- Gesellschafterliste veraltet: Risiko gutgläubiger Erwerb (§ 16 Abs. 3 GmbHG).

**Transparenzregister-Lücken:** Gesellschaften ohne Eintragung oder ohne geprüfte Ausnahme.

**Bilanzpublizitäts-Lücken:** Offenlegung > 12 Monate zurück = Ordnungsgeldgefahr.

**Konzern-Pflichten:** § 290 HGB-Konzernabschluss-Pflicht; § 325a HGB für ausländische Töchter.

```
GESELLSCHAFTS-GESUNDHEITS-AUDIT — [Datum]

EINREICHUNGS-COMPLIANCE
 Überfällig: [N]
 Unbekannter Status: [N]

RUHENDE GESELLSCHAFTEN ([N])
 [Liste mit Alter und jährlichen Tragekosten]

TRANSPARENZREGISTER
 Nicht eingetragen / geprüft: [N] Gesellschaften

BILANZPUBLIZITÄT § 325 HGB
 Überfällig (>12 Monate): [N] Gesellschaften
 Ordnungsgeldgefahr BfJ: [Liste]

EMPFOHLENE MASSNAHMEN
 1. [Höchste Priorität]
 2. [etc.]
```

## Modus 5: Export

```
/gesellschaftsrecht:gesellschafts-compliance --export [--format csv|tabelle]
```

CSV-Spalten: `Gesellschaftsname, Typ, HR-Nummer, Registergericht, Gründungsdatum, Status, Größenklasse, GJ-Ende, Pflicht, Fällig, Zuletzt eingereicht, Notizen`

## Streitwert und Kosten

| Verstoß | Sanktionsrahmen | Rechtsgrundlage |
|---|---|---|
| Verspätete Offenlegung § 325 HGB | Ordnungsgeld 2.500 – 25.000 EUR je Verstoß; Wiederholung möglich | § 335 HGB |
| Verletzung Transparenzregisterpflicht (vorsätzlich) | Bußgeld bis 1.000.000 EUR | § 56 Abs. 1 GwG |
| Verletzung Transparenzregisterpflicht (fahrlässig) | Bußgeld bis 500.000 EUR | § 56 Abs. 1 GwG |
| Falsche Jahresabschlussunterlagen § 331 HGB | Freiheitsstrafe bis 3 Jahre oder Geldstrafe | § 331 HGB |
| Haftung GF für veraltete Gesellschafterliste | Schadensersatz nach § 43 GmbHG | § 43 GmbHG; § 16 Abs. 3 GmbHG |
| RA-Beratungshonorar Ordnungsgeldwiderspruch | Gegenstandswert = Ordnungsgeldbetrag; 2 Gebühren (§§ 13, 14 RVG) | RVG Nr. 2300 |

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Mandant hat 10+ Gesellschaften und keine strukturierte Fristübersicht | Compliance-Tracker initialisieren; jährlicher Audit-Termin im Kanzleikalender; automatische 90-Tage-Frühwarnung |
| BfJ-Ordnungsgeldverfahren läuft | Sofortige Nachreichung + Widerspruch mit Begründung der Verspätungsursache; Ordnungsgeld wird bei unverzüglicher Nachreichung häufig reduziert |
| Abtretung ohne Notar / ohne Gesellschafterlisten-Update | Notar beauftragen; Gesellschafterliste unverzüglich einreichen; Transparenzregister-Meldung binnen 2 Wochen |
| M&A-Due-Diligence: Gesellschafterliste veraltet | Verkäufer-Garantie für ordnungsgemäße Gesellschafterliste verlangen; gutgläubigen Erwerb durch Dritte ausschließen; Closing-Bedingung: aktuelle HR-Liste |
| Größenklassenwechsel in Sichtweite | § 267 Abs. 4 HGB-Zweijahresregel prüfen; wenn zweites Jahr unter Schwellen: Prüfungspflicht entfällt; Prüfungsvertrag ggf. nicht verlängern |
| Ruhende Gesellschaft seit > 3 Jahren | Formale Auflösung (§ 65 GmbHG) prüfen; Kostenersparnis (HR-Gebühren, Buchhaltung, Steuern) gegen Auflösungsaufwand abwägen |

## Output-Template

**Adressat:** Mandant / Geschaeftsfuehrer / Complianceverantwortlicher — Tonfall: sachlich-strukturiert, handlungsorientiert

```
GESELLSCHAFTS-COMPLIANCE-BERICHT
Mandat/Praxis: [MANDATSCODE / PRAXISNAME]
Erstellt von: [NAME], [KANZLEI]
Datum: [TT.MM.JJJJ]
Berichtszeitraum: [DATUM] bis [DATUM]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.

--- PORTFOLIOÜBERSICHT ---
Gesellschaften gesamt: [N]
Status aktiv: [N] | ruhend: [N] | unbekannt: [N]

--- BILANZPUBLIZITAET § 325 HGB ---
Frist 12 Monate nach Geschaeftsjahresende

| Gesellschaft | GJ-Ende | Offenlegungsfrist | Eingereicht | Status |
|---|---|---|---|---|
| [NAME GmbH] | [TT.MM.JJJJ] | [TT.MM.JJJJ] | [TT.MM.JJJJ / OFFEN] | [OK / UEBERFAELLIG / ORDNUNGSGELD] |

Ordnungsgeldgefahr (§ 335 HGB): [N] Gesellschaften
Hoechstes Risiko: [NAME], ueberfaellig seit [N] Tagen (drohendes Ordnungsgeld: bis [BETRAG] EUR)

--- GESELLSCHAFTERLISTE § 40 GmbHG ---
Zuletzt eingereicht: [DATUM] / noch nicht eingereicht
Aendering: [BESCHREIBUNG] am [DATUM]
Handlungsbedarf: [JA — Notar beauftragen bis TT.MM.JJJJ / NEIN]

--- TRANSPARENZREGISTER §§ 18 ff. GwG ---
Beguenstigter(wirtschaftlich Berechtigter): [NAME], [BETEILIGUNG] %
Letztes Update: [DATUM]
Status: [AKTUELL / AENDERUNG ERFORDERLICH bis TT.MM.JJJJ]

--- PRÜFUNGSPFLICHT § 316 HGB ---
| Gesellschaft | Groessenklasse | Pruefungspflichtig | Pruefungsauftrag erteilt |
|---|---|---|---|
| [NAME] | [Gross / Mittel / Klein] | [JA / NEIN] | [DATUM / OFFEN] |

--- EMPFOHLENE MASSNAHMEN (PRIORISIERT) ---
1. [HOECHSTE PRIORITAET] — Frist: [DATUM] — verantwortlich: [PERSON]
2. [MITTLERE PRIORITAET] — Frist: [DATUM] — verantwortlich: [PERSON]
3. [NIEDRIGE PRIORITAET] — keine akute Frist

--- NAECHSTER AUDIT-TERMIN ---
[DATUM] (Empfehlung: jaehrlich, 90 Tage vor GJ-Ende)
```

## Rote Schwellen

- **Bilanzpublizitaet § 325 HGB > 12 Monate ueberfaellig** — Ordnungsgeldverfahren BfJ laeuft oder droht (§ 335 HGB: bis 25.000 EUR je Verstoß); sofort Jahresabschluss erstellen und einreichen.
- **Gesellschafterliste § 40 GmbHG nach Abtretung > 3 Wochen nicht eingereicht** — gutglaeuber Erwerb durch Dritte moeglich (§ 16 Abs. 3 GmbHG); Notar sofort beauftragen.
- **Transparenzregister-Eintrag nach Beteiligungsaenderung > 2 Wochen nicht aktualisiert** — Bußgeld bis 1.000.000 EUR (§ 56 Abs. 1 GwG).
- **Groessenklassenwechsel zur grossen Kapitalgesellschaft nicht erkannt** — Prüfungspflicht § 316 HGB gilt ab zweitem Jahr in Folge (§ 267 Abs. 4 HGB); Prüfungsauftrag erteilen.

## Anschluss-Skills

- `gesellschaftsrecht:gesellschaftsrecht-mandat-arbeitsbereich` — Mandatsworkspace für die betroffene Gesellschaft
- `gesellschaftsrecht:vollzugs-checkliste` — Gesellschafterliste und Transparenzregister als Vollzugspflicht bei M&A
- `gesellschaftsrecht:aufsichtsrat-protokoll` — Jahresabschluss-Billigung nach § 172 AktG protokollieren
- `gesellschaftsrecht:tabellenpruefung` — Compliance-Tabelle aus Jahresabschlussdaten prüfen

## Quellen und Zitierweise

- § 325 HGB (Bilanzpublizität / Offenlegungspflicht)
- § 335 HGB (Ordnungsgeldverfahren Bundesamt für Justiz)
- § 40 GmbHG (Gesellschafterliste)
- §§ 18 ff., 20 GwG (Transparenzregister)
- § 267 HGB (Größenklassen)
- § 316 HGB (Prüfungspflicht)
- § 16 Abs. 3 GmbHG (Gutgläubiger Erwerb)
- § 290 HGB (Konzernabschlusspflicht)
- § 264 Abs. 1 HGB (Aufstellungsfrist)

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Scholz, GmbHG, 12. Aufl. 2018, § 40 Rn. 3 ff. (Gesellschafterliste).
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Was dieser Skill nicht tut

- Er reicht keine Dokumente ein. Ausgabe ist Tracker und Aufgabenliste; Einreichung erfolgt durch Anwalt/Steuerberater.
- Er ruft keine Registerauszüge ab; er verfolgt, wann sie zuletzt bestätigt wurden.
- Er bestimmt nicht, ob eine Konzernabschluss-Pflicht besteht — das erfordert eine Analyse der tatsächlichen Konzernverhältnisse.
- Er ersetzt keine Steuerberatung (§ 316 HGB-Prüfung = Steuerberater/Wirtschaftsprüfer).

---

## Skill: `gmbh-gruendung`

_Begleitung der GmbH-Gründung von der Satzungserstellung (§ 2 GmbHG) bis zur Eintragung ins Handelsregister (§ 7 GmbHG) einschließlich UG-Variante (§ 5a GmbHG), Gewerbeanmeldung und Transparenzregister. Lädt bei Mandaten zur Neugründung, Vorgesellschaft, Stammkapitalaufbringung oder Gesellschaftsv..._

# GmbH-Gründung – Von der Satzung bis zum Handelsregistereintrag

## Arbeitsbereich

Begleitung der GmbH-Gründung von der Satzungserstellung (§ 2 GmbHG) bis zur Eintragung ins Handelsregister (§ 7 GmbHG) einschließlich UG-Variante (§ 5a GmbHG), Gewerbeanmeldung und Transparenzregister. Lädt bei Mandaten zur Neugründung, Vorgesellschaft, Stammkapitalaufbringung oder Gesellschaftsvertrag. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `GmbH-Gründung – Von der Satzung bis zum Handelsregistereintrag` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: GmbH-Gründung – Von der Satzung bis zum Handelsregistereintrag
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Triage zu Beginn

Vor Beginn der Gruendungsbegleitung klaeren:

1. **Rechtsform sicher?** GmbH oder UG (haftungsbeschraenkt, § 5a GmbHG)? Bei Stammkapital < 25.000 EUR: UG; bei nur 1 Gesellschafter und 1 Geschaeftsfuehrer: Musterprotokoll (§ 2 Abs. 1a GmbHG) moeglich.
2. **Gesellschafterkreis vollstaendig?** Alle Gesellschafter identifiziert, Geschaeftsfaehigkeit geprueft? Minderjaehrige: familiengerichtliche Genehmigung erforderlich?
3. **Gegenstand erlaubnispflichtig?** Zahlungsdienste (§ 32 KWG), Finanzanlageberatung (§ 34f GewO), Immobilienmakler (§ 34c GewO), Gesundheit, Waffen? Genehmigung VOR Gruendung einholen.
4. **Sacheinlagen?** Wird Stammkapital durch Sacheinlagen aufgebracht? → Sachgruendungsbericht (§ 5 Abs. 4 GmbHG) erforderlich; Zeitaufwand und Werthaltigkeitspruefung einplanen.
5. **Geschaeftsfuehrer geprueft?** Bestellungshindernisse nach § 6 Abs. 2 GmbHG ausgeschlossen? (insb. Insolvenzstraftaten, Betrug, Untreue)
6. **Transparenzregister-Pflicht bekannt?** Wirtschaftlich Berechtigte (§ 3 GwG) identifiziert? Eintragungsfrist 2 Wochen nach Gruendung.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Eingaben

1. **Gesellschafterkreis** – Namen, Adressen, Nationalität, Geschäftsfähigkeit;
 bei Minderjährigen: familiengerichtliche Genehmigung.
2. **Firma** – Unterscheidungskraft (§ 18 HGB), Irreführungsverbot (§ 18 Abs. 2
 HGB), Namenszusatz "GmbH" (§ 4 GmbHG) oder "UG (haftungsbeschränkt)" (§ 5a
 Abs. 1 GmbHG).
3. **Stammkapital** – Mindestens 25.000 € bei GmbH (§ 5 Abs. 1 GmbHG); bei UG
 mindestens 1 € (§ 5a Abs. 1 GmbHG).
4. **Geschäftsführer** – Natürliche Person, Geschäftsfähigkeit, keine
 Vorstrafen nach § 6 Abs. 2 Satz 2 GmbHG (Bestellungshindernis).
5. **Unternehmensgegenstand** – Hinreichend bestimmt; Erlaubnispflichtige
 Tätigkeiten (z. B. § 32 KWG, § 34c GewO) vorab prüfen.
6. **Sacheinlagen** – § 5 Abs. 4 GmbHG: Sachgründungsbericht, Werthaltigkeitsprüfung.

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 2 GmbHG** – Notarielle Beurkundung des Gesellschaftsvertrags; Musterprotokoll
 für vereinfachte Gründung (§ 2 Abs. 1a GmbHG, max. 3 Gesellschafter,
 1 Geschäftsführer).
- **§ 5 GmbHG** – Stammkapital 25.000 €; Stammeinlage mind. 1 €; § 5 Abs. 4 GmbHG
 Sachgründungsbericht.
- **§ 5a GmbHG** – UG (haftungsbeschränkt): Mindestkapital 1 €; Rücklage 25 % des
 Jahresüberschusses bis Aufstockung auf 25.000 € (§ 5a Abs. 3 GmbHG).
- **§ 6 GmbHG** – Geschäftsführer; Bestellungshindernisse § 6 Abs. 2 GmbHG.
- **§ 7 GmbHG** – Anmeldung zum Handelsregister; Voraussetzung: Einzahlung
 von mindestens 12.500 € (Hälfte) auf Bareinlage (§ 7 Abs. 2 GmbHG).
- **§ 8 GmbHG** – Inhalt der Anmeldung; Versicherung des Geschäftsführers über
 Bestellungshindernisse (§ 8 Abs. 3 GmbHG).
- **§ 11 GmbHG** – Entstehung der GmbH mit Eintragung; Haftung in der Vorgesellschaft.
- **§ 39 GmbHG** – Anmeldung von Geschäftsführerwechseln.
- **§ 3 GwG** i. V. m. **§§ 19 ff. GwG** – Transparenzregistereintragung der
 wirtschaftlich Berechtigten.

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 "ARGE Weißes Ross": Grundsätze zur Haftung in der Vorgesellschaft;
 Handeln im Namen der noch nicht eingetragenen GmbH begründet persönliche
 Haftung der Handelnden nach § 11 Abs. 2 GmbHG, es sei denn, die Gesellschaft
 wird eingetragen und die Verbindlichkeit übernommen.

2. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Zur Verlustdeckungspflicht der Gründergesellschafter in der Vor-GmbH:
 Das Prinzip der realen Kapitalaufbringung gebietet, dass bei Eintragung
 das Gesellschaftsvermögen mindestens dem angemeldeten Stammkapital entspricht.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Vorbereitung** – Firmenrecherche beim zuständigen Handelsregister und DPMA
 (Namensähnlichkeit); Gegenstandsformulierung; Bestellungshindernis-Prüfung
 § 6 Abs. 2 GmbHG; ggf. behördliche Genehmigungen vorab einholen.

2. **Gesellschaftsvertrag beurkunden** (§ 2 GmbHG) – Notar erstellt oder
 beurkundet den Gesellschaftsvertrag mit Mindestinhalt (§ 3 GmbHG: Firma,
 Sitz, Gegenstand, Stammkapital, Stammeinlagen). Bei vereinfachter Gründung:
 Musterprotokoll (Anlage zu § 2 Abs. 1a GmbHG).

3. **Stammkapital einzahlen** – Bareinlage auf Geschäftskonto einzahlen; bei UG:
 vollständige Einzahlung vor Anmeldung erforderlich (§ 5a Abs. 2 GmbHG).
 Bei GmbH: mindestens 12.500 € (§ 7 Abs. 2 Satz 1 GmbHG) vor Anmeldung.

4. **Geschäftsführer bestellen und Versicherung abgeben** – Gesellschafterbeschluss
 (§ 46 Nr. 5 GmbHG); Anstellungsvertrag; Versicherung nach § 8 Abs. 3 GmbHG
 gegenüber dem Registergericht.

5. **Handelsregisteranmeldung** (§ 7 GmbHG) – Notarielle Beglaubigung der
 Unterschrift (§ 12 HGB); Einreichung beim zuständigen Amtsgericht (HRB);
 Anlage: Gesellschaftsvertrag, Liste der Gesellschafter, Geschäftsführernachweis.

6. **Eintragung und Veröffentlichung** – Nach Eintragung entsteht die GmbH
 (§ 11 Abs. 1 GmbHG); Bekanntmachung im Bundesanzeiger (§ 10 GmbHG).

7. **Nachgelagerte Pflichten:**
 - Gewerbeanmeldung § 14 GewO bei der Gemeinde (innerhalb von 1 Monat).
 - IHK-Mitgliedschaft kraft Gesetzes (§ 2 IHKG); Beitragsbescheid folgt.
 - Transparenzregister: Eintragung wirtschaftlich Berechtigter (§ 20 GwG)
 innerhalb von 2 Wochen nach Gründung; Bußgeld bei Verstößen (§ 56 GwG).
 - Finanzamt: steuerliche Erfassung (USt., KSt., GewSt.) mittels ELSTER-
 Fragebogen.
 - Bankverbindung: Geschäftskonto für Stammkapital und laufenden Zahlungsverkehr.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — GmbH gruenden nach Standardprogramm | Gruendungsprotokoll nach Ablauf; Template unten |
| Variante A — Gruendung eilt keine Zeit für Musterprotokoll | Musterprotokoll-GmbH § 2 Abs. 1a GmbHG als Schnelloption |
| Variante B — Gesellschafter aus verschiedenen Ländern | Notarielle Gruendung im Inland; Vollmacht aus dem Ausland pruefen |
| Variante C — Gruender will erst UG dann Hochstufung | UG-Gruendung zuerst; Hochstufung nach Kapitalaufbau |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template

**Adressat:** Gruender / Mandant — Tonfall: verstaendlich-erklaerend, fristen-orientiert

```
GRUENDUNGS-CHECKLISTE
Mandant: [NAME]
Gesellschaft (geplante Firma): [FIRMA GmbH / UG (haftungsbeschraenkt)]
Sitz (geplant): [ORT]
Erstellt von: [NAME], [KANZLEI]
Datum: [TT.MM.JJJJ]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.

--- VORBEREITUNGSPHASE ---
☐ Firmenrecherche Handelsregister / DPMA — Name verfuegbar: [JA / OFFEN]
☐ Gesellschafterkreis vollstaendig — alle GF geprueft (§ 6 Abs. 2 GmbHG)
☐ Erlaubnispflichtige Taetigkeit geprueft — Genehmigung: [NICHT ERFORDERLICH / BEANTRAGT]
☐ Sacheinlagen: [KEINE / SACHGRUENDUNGSBERICHT ERFORDERLICH]
☐ Stammkapital: [BETRAG EUR] (GmbH: mind. 25.000 EUR; UG: mind. 1 EUR)

--- BEURKUNDUNG (§ 2 GmbHG) ---
☐ Notar: [NAME], [ORT] — Termin: [TT.MM.JJJJ]
☐ Gesellschaftsvertrag beurkundet am: [DATUM / OFFEN]
☐ Musterprotokoll: [JA — § 2 Abs. 1a GmbHG / NEIN — individueller GV]
☐ Gesellschafterbeschluesse (GF-Bestellung § 46 Nr. 5 GmbHG) beurkundet

--- STAMMKAPITAL-EINZAHLUNG (§ 7 Abs. 2 GmbHG) ---
☐ Geschaftskonto eroeffnet bei: [BANK]
☐ Einzahlung: [BETRAG EUR] eingezahlt am: [DATUM] (mind. 12.500 EUR bei GmbH vor Anmeldung)
☐ Einzahlungsnachweis: [VORHANDEN / AUSSTEHEND]

--- HANDELSREGISTERANMELDUNG (§ 7 GmbHG) ---
☐ Versicherung GF (§ 8 Abs. 3 GmbHG) unterzeichnet: [TT.MM.JJJJ]
☐ Anmeldung durch Notar eingereicht am: [TT.MM.JJJJ]
☐ HRB-Nummer vergeben: [NUMMER / AUSSTEHEND]
☐ Eintragung erfolgt am: [TT.MM.JJJJ / AUSSTEHEND]

--- NACHGELAGERTE PFLICHTEN ---
☐ Gewerbeanmeldung § 14 GewO — Frist: [4 Wochen nach Betriebsaufnahme] — erledigt: [DATUM / OFFEN]
☐ Transparenzregister § 20 GwG — Frist: 2 Wochen nach Eintragung ([TT.MM.JJJJ]) — erledigt: [DATUM / OFFEN]
☐ Steuerliche Erfassung ELSTER — Fragebogen abgesandt: [DATUM / OFFEN]
☐ IHK-Mitgliedschaft — Beitragsbescheid abgewartet: [JA / OFFEN]

--- KOSTEN (SCHAETZUNG) ---
Notargebuehren (GnotKG): ca. [BETRAG EUR] (abhaengig vom Geschaeftswert)
Gerichtsgebuehren Handelsregister: ca. [BETRAG EUR]
Beratungshonorar: [BETRAG EUR / nach RVG / Pauschalhonorar]
Gesamtschaetzung: ca. [BETRAG EUR]

--- STATUS GESAMT ---
Phase: [VORBEREITUNG / BEURKUNDUNG / EINZAHLUNG / ANMELDUNG / ABGESCHLOSSEN]
Naechster Schritt: [AKTION] — Frist: [DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Rote Schwellen

- **Handeln vor HR-Eintragung ohne Hinweis auf Vorgesellschaftshaftung** — § 11 Abs. 2 GmbHG: persönliche Haftung der Handelnden; Mandant explizit warnen.
- **Stammkapital nicht oder zu wenig eingezahlt vor Anmeldung** — § 7 Abs. 2 GmbHG: mind. 12.500 EUR vor Anmeldung; Registergericht lehnt sonst Eintragung ab.
- **Bestellungshindernis § 6 Abs. 2 GmbHG uebersehen** — Vorstrafe des Geschaeftsfuehrers fuehrt zur Ablehnung der Eintragung; Strafregisterauszug vorab anfordern.
- **Transparenzregister-Frist versaeumt** — Bussgeld bis 1.000.000 EUR (§ 56 Abs. 1 GwG); 2-Wochen-Frist ab Eintragung sofort im Fristenbuch verankern.
- **Erlaubnispflichtige Taetigkeit ohne Genehmigung aufgenommen** — Ordnungswidrigkeitsrisiko, Betriebsuntersagung; Genehmigung VOR Aufnahme der Taetigkeit einholen.

## Beispiel

*Sachverhalt:* Zwei Gesellschafter (A, 60 %; B, 40 %) gründen eine GmbH im
IT-Dienstleistungsbereich mit einem Stammkapital von 25.000 €. A soll
alleinvertretungsberechtigter Geschäftsführer werden.

*Ablaufskizze (Urteilsstil):*

Der Gesellschaftsvertrag ist nach § 2 Abs. 1 Satz 1 GmbHG notariell zu beurkunden.
Das Stammkapital von 25.000 € ist gemäß § 5 Abs. 1 GmbHG zulässig. Vor der
Anmeldung muss A mindestens 15.000 € (60 % von 25.000 €) und B mindestens
10.000 € (40 %) eingezahlt haben, so dass insgesamt 25.000 € auf das
Geschäftskonto der Gesellschaft eingezahlt sind – § 7 Abs. 2 Satz 1 GmbHG
verlangt Einzahlung von mindestens der Hälfte, hier also 12.500 €; es empfiehlt
sich jedoch die volle Einzahlung zur Vermeidung der Vorbelastungshaftung
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
Versicherung nach § 8 Abs. 3 GmbHG gegenüber dem Registergericht abzugeben.
Die Transparenzregistereintragung ist innerhalb von 2 Wochen vorzunehmen
(§ 20 Abs. 1 GwG).

- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
in: Altmeppen, GmbHG, 11. Aufl. 2023, § 2 Rn. 3.)*

## Risiken und typische Fehler

- **Vorgesellschaftshaftung** – Handeln vor Eintragung begründet persönliche
 Haftung der Handelnden (§ 11 Abs. 2 GmbHG); Haftungsübernahme durch die
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Vorbelastungshaftung** – Minderung des Gesellschaftsvermögens zwischen
 Gründung und Eintragung geht zu Lasten der Gesellschafter.
- **Sacheinlagen unterschätzt** – Fehlender Sachgründungsbericht (§ 5 Abs. 4
 GmbHG) führt zur Ablehnung der Eintragung durch das Registergericht.
- **Bestellungshindernis** – Vorstrafen nach § 6 Abs. 2 Satz 2 Nr. 3 GmbHG
 schließen Geschäftsführeramt aus; Strafregisterauszug rechtzeitig einholen.
- **Transparenzregister-Frist** – 2-Wochen-Frist nach § 20 Abs. 1 GwG;
 Bußgelder bis zu 1 Mio. € (§ 56 GwG).
- **Datenschutz/Berufsrecht** – § 43a Abs. 2 BRAO, § 203 StGB: keine
 Mandantendaten in externe KI-Systeme ohne Einwilligung.

## Quellenpflicht

Alle Aussagen zu GmbH-Gründungsrecht nach `references/zitierweise.md`.
Rspr. vor Kommentar; neueste Entscheidungen zuerst. Bei UG-Variante und
Vorgesellschaftsfragen bestehende Meinungsunterschiede in der Literatur
ausdrücklich aufzeigen. Gesetzesstände (insb. GwG) auf Aktualität prüfen.

---

## Skill: `handelsregisteranmeldung-integrations`

_Vorbereitung und Prüfung von Handelsregisteranmeldungen (HRB, HRA, GnR, PartGR) nach § 12 HGB; Pflichtanmeldungen für Geschäftsführerwechsel (§ 39 GmbHG), Prokura (§ 53 HGB), Sitzverlegung und Kapitalmaßnahmen; Eintragungsgrundätze und Wirkung nach § 15 HGB. Lädt bei allen Registerpublizitätsfrag..._

# Handelsregisteranmeldung – HRB / HRA / GnR / PartGR

## Arbeitsbereich

Vorbereitung und Prüfung von Handelsregisteranmeldungen (HRB, HRA, GnR, PartGR) nach § 12 HGB; Pflichtanmeldungen für Geschäftsführerwechsel (§ 39 GmbHG), Prokura (§ 53 HGB), Sitzverlegung und Kapitalmaßnahmen; Eintragungsgrundätze und Wirkung nach § 15 HGB. Lädt bei allen Registerpublizitätsfragen und Anmeldungspflichten. Arbeite entlang dieser konkreten Prüfungslinie und trenne Rolle, Frist, Zuständigkeit, Beweislast und gewünschten Output.

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Handelsregisteranmeldung – HRB / HRA / GnR / PartGR` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Handelsregisteranmeldung – HRB / HRA / GnR / PartGR
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Triage zu Beginn

Vor der Anmeldungsvorbereitung klaeren:

1. **Anmeldungsgegenstand:** Was soll angemeldet werden? (Geschaeftsfuehrer-Wechsel, Prokura, Sitzverlegung, Kapitalerhoehung, Satzungsaenderung, Liquidation, Loeschung)
2. **Registerart:** HRB (GmbH/AG), HRA (OHG/KG), GnR (eG), PartGR (PartG)? Bei GmbH & Co. KG: sowohl HRB als auch HRA betroffen?
3. **Unterlagen vollstaendig?** Gesellschafterbeschluss (ggf. notariell beurkundet bei Satzungsaenderung § 53 GmbHG), Versicherung GF (§ 8 Abs. 3 GmbHG), Satzung aktuell?
4. **Notar beauftragt?** § 12 HGB: öffentliche Beglaubigung erforderlich; Notar uebermittelt elektronisch (§ 12 Abs. 2 HGB). Ist der Notar bereits beauftragt?
5. **Mehrfache Aenderungen gleichzeitig?** Mehrere Aenderungen koennen in einer Anmeldung zusammengefasst werden; Voraussetzungen für jede Aenderung separat pruefen.
6. **§ 15 HGB-Risiko waehrend Wartezeit?** Wer vertritt die Gesellschaft bis zur Eintragung des neuen GF? Uebergangsregelungen (Vollmachten) treffen.
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist für den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Eingaben

1. **Registerart** – HRB (GmbH, AG, KGaA, SE), HRA (OHG, KG, GmbH & Co. KG),
 GnR (eG), PartGR (PartG).
2. **Anmeldungsgegenstand** – Art der Änderung: Geschäftsführer, Prokura, Sitz,
 Firma, Stammkapital, Satzungsänderung, Liquidation, Löschung.
3. **Unterlagen** – Gesellschafterbeschluss, Satzungsänderung, Versicherungen,
 Anstellungsvertrag (bei GF), Ausweiskopien.
4. **Zuständiges Registergericht** – Amtsgericht am Sitz der Gesellschaft
 (§ 8 HGB, §§ 13, 14 GmbHG); elektronische Einreichung über das
 Gemeinsame Registerportal der Länder (www.handelsregister.de).
5. **Vollmachten** – Notarielle Beglaubigung der Unterschrift des Anmeldenden
 erforderlich (§ 12 Abs. 1 Satz 1 HGB); bei GmbH: Unterschrift aller
 Geschäftsführer (§ 78 GmbHG).

## Rechtlicher Rahmen

### Zentrale Normen

- **§ 8 HGB** – Inhalt und Führung des Handelsregisters; öffentliches Register.
- **§ 12 HGB** – Form der Anmeldungen: elektronisch in öffentlich beglaubigter
 Form (§ 12 Abs. 1 Satz 1 HGB); Notar übermittelt (§ 12 Abs. 2 HGB).
- **§ 13 HGB** – Örtliche Zuständigkeit: Gericht am Sitz der Niederlassung.
- **§ 15 HGB** – Wirkung der Eintragung und Bekanntmachung; negative Publizität
 (Abs. 1): nicht eingetragene und bekanntgemachte Tatsachen können Dritten
 nicht entgegengehalten werden; positive Publizität (Abs. 3): irrtümliche
 Eintragung kann gegenüber gutgläubigen Dritten wirken.
- **§ 39 GmbHG** – Anmeldung von Geschäftsführerwechseln; Muster-Versicherung;
 unverzügliche Anmeldung.
- **§ 53 HGB** – Erteilung, Änderung und Erlöschen der Prokura; Anmeldung zur
 Eintragung; keine konstitutive Wirkung, aber Publizitätswirkung § 15 HGB.
- **§§ 54–58 HGB** – Umfang der Prokura; Beschränkungen (Grundstücke § 49
 Abs. 2 HGB).
- **§ 78 GmbHG** – Zeichnung der Anmeldungen durch alle Geschäftsführer.
- **§§ 181 ff. AktG** – Satzungsänderung bei AG; Anmeldung durch Vorstand und
 Aufsichtsratsvorsitzenden.

### Leitentscheidungen

1. Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 Zum Eintragungserfordernis bei Prokura-Erteilung: Die Eintragung der Prokura
 hat keine konstitutive Wirkung; die Prokura entsteht durch Erteilung, nicht
 durch Eintragung. Aus § 15 Abs. 1 HGB folgt jedoch, dass der nicht eingetragene
 Widerruf der Prokura Dritten gegenüber unwirksam ist, wenn diese keine
 Kenntnis hatten.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
 Rn. 14 – Zur Zurückweisung einer Handelsregisteranmeldung wegen unzureichender
 Beglaubigung: § 12 HGB verlangt öffentliche Beglaubigung der Unterschrift;
 bloße notarielle Beglaubigung von Ablichtungen genügt nicht.

### Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Ablauf

**Vorab:** Der untenstehende ist die typische Standardlinie. Wenn die Mandantenlage abweicht (siehe "Strategische Optionen" oben), sind die Schritte entsprechend zu verkuerzen, umzustellen oder durch ein anderes Skill zu ersetzen — der ist Leitfaden, nicht Pflichtprogramm.

1. **Sachverhalt klären** – Welcher Anmeldungsgegenstand liegt vor? Liegt ein
 neuer Geschäftsführer vor (§ 39 GmbHG), eine Prokura-Änderung (§ 53 HGB),
 eine Satzungsänderung (§ 54 GmbHG i. V. m. § 181 GmbHG) oder eine
 Kapitalmaßnahme?

2. **Unterlagen zusammenstellen** – Gesellschafterbeschluss (notariell beurkundet
 bei Satzungsänderung, § 53 Abs. 2 GmbHG); Anstellungsvertrag und ggf.
 Selbstauskunft des neuen Geschäftsführers nach § 8 Abs. 3 GmbHG; Satzung in
 aktueller Fassung.

3. **Anmeldung vorbereiten** – Entwurf der Anmeldeformulierung; Vorlage beim
 Notar zur Beglaubigung der Unterschrift nach § 12 HGB; Notar übermittelt
 elektronisch (§ 12 Abs. 2 HGB).

4. **Einreichungsfrist beachten:**
 - Geschäftsführerwechsel § 39 GmbHG: unverzüglich (keine Ausschlussfrist,
 aber Haftungsrisiko bei Verzögerung).
 - Prokura § 53 Abs. 1 HGB: unverzüglich nach Erteilung oder Erlöschen.
 - Satzungsänderung § 54 GmbHG: nach Beschluss unverzüglich, vor Wirksamkeit
 zur Eintragung anmelden (§ 54 Abs. 3 GmbHG).
 - Kapitalerhöhung AG: § 184 AktG; Anmeldung durch Vorstand und
 Aufsichtsratsvorsitzenden innerhalb angemessener Frist.

5. **Eintragung abwarten / § 15 HGB beachten** – Bis zur Eintragung und
 Bekanntmachung kann der geänderte Sachverhalt Dritten nicht entgegengehalten
 werden (§ 15 Abs. 1 HGB); in der Zwischenzeit Übergangsregelungen treffen
 (z. B. Vollmachten).

6. **Registerauszug prüfen** – Nach Eintragung aktuellen Handelsregisterauszug
 abrufen (www.handelsregister.de); fehlerhafte Eintragungen unverzüglich
 korrigieren (§ 395 FamFG, Berichtigungsantrag).

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Handelsregisteranmeldung vorbereiten und einreichen | Anmeldung nach Checkliste; Template unten |
| Variante A — Eilbedarf Eintragung innerhalb Woche noetig | Vorlagenversion pruefen; Notarbeschleunigungs-Option |
| Variante B — Aenderungsanmeldung nicht Erstanmeldung | Aenderungsanmeldung-Subset des Templates verwenden |
| Variante C — Anmeldung wird vom Registergericht bemueckelt | Beschwerdeverfahren vorbereiten; Ergaenzung der Unterlagen zuerst |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Output-Template

**Adressat:** Amtsgericht — Handelsregister — Tonfall: sachlich-juristisch, formbewusst

```
ANMELDUNG ZUM HANDELSREGISTER

An das
Amtsgericht [ORT] — Handelsregister
[ADRESSE]

[ORT], [TT.MM.JJJJ]

Betreff: [FIRMA] — [HRB/HRA-NUMMER] — Anmeldung [GEGENSTAND]

Anmeldende Partei: [KANZLEI / NOTAR] für [GESELLSCHAFT]

Hiermit melden wir im Namen der [FIRMA] mit Sitz in [ORT], eingetragen im
Handelsregister des Amtsgerichts [ORT] unter [HRB/HRA-NUMMER], folgende
Aenderung zur Eintragung an:

I. ANMELDUNGSGEGENSTAND
[GENAUE BESCHREIBUNG DER AENDERUNG]
Rechtsgrundlage: [§ NORM]

II. ANMELDENDE PERSONEN (§ 78 GmbHG / § [NORM])
[NAME], [FUNKTION], wohnhaft [ADRESSE]
[Fuer alle anmeldepflichtigen Personen wiederholen]

III. ANLAGEN
1. Gesellschafterbeschluss vom [DATUM] [notariell beurkundet / oeffentlich beglaubigt]
2. [Anlage 2]
3. [Anlage 3 (z.B. Versicherung § 8 Abs. 3 GmbHG)]
4. Aktueller Gesellschaftsvertrag / Satzung [falls geaendert]

IV. ERKLAERUNGEN
[Falls GF-Wechsel: Versicherung des neuen Geschaeftsfuehrers nach § 8 Abs. 3 GmbHG
bei. Die antretenden Personen versichern, dass keine Bestellungshindernisse
gemaiß § 6 Abs. 2 GmbHG vorliegen.]

Die Unterschriften der Anmeldenden wurden notariell beglaubigt (§ 12 Abs. 1
HGB) und werden durch Notar [NAME] elektronisch uebermittelt (§ 12 Abs. 2 HGB).

Mit freundlichen Gruessen
[NOTAR / KANZLEI]
[NAME]
[ANSCHRIFT]

--- UNTERLAGEN-CHECKLISTE ---
| Dokument | Erfordernis | Erledigt |
|---|---|---|
| Gesellschafterbeschluss | § 46 GmbHG / [NORM] | [JA / OFFEN] |
| Versicherung GF | § 8 Abs. 3 GmbHG | [JA / ENTFAELLT] |
| Beglaubigung Unterschrift | § 12 Abs. 1 HGB | [JA / OFFEN] |
| Aktueller GV / Satzung | [§ 53 GmbHG] | [JA / ENTFAELLT] |
| Bekanntmachung vorbereitet | § 10 GmbHG | [JA / ENTFAELLT] |
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Durchsetzung des Anspruchs / Vergleich / Reputationsschutz / schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestforderung / Zeitrahmen / Formerfordernis]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgesprach / Einigung vor Fristablauf]

Schlussabsatz Variante A (kooperativ):
Wir regen eine guetliche Einigung an und stehen für ein klaerenden Gesprach zur Verfuegung. Eine einvernehmliche Loesung erspart beiden Seiten Zeit und Kosten.

Schlussabsatz Variante B (formal-streng):
Eine aussergerichtliche Einigung kommt nur in Betracht wenn die Gegenseite innerhalb von [X] Tagen einen akzeptablen Vorschlag unterbreitet. Anderenfalls werden wir alle rechtlichen Schritte einleiten.

## Rote Schwellen

- **Formfehler § 12 HGB (fehlende Beglaubigung)** — Registergericht weist Anmeldung zurueck; erneute Vorlage mit Zeitverlust; Notar vor Einreichung pruefen lassen.
- **Versicherungspflicht § 8 Abs. 3 GmbHG fehlt** — Anmeldung ohne GF-Versicherung wird abgelehnt; Versicherung vor Notartermin einholen.
- **§ 15 Abs. 1 HGB: Verzoegerung > 2 Wochen** — Ausscheidender GF haftet ggf. weiterhin gegenueber Dritten; neuer GF kann Vertretungsmacht nicht aus Register beweisen; Anmeldung unverzueglich einreichen.
- **Satzungsaenderung ohne notarielle Beurkundung** — § 53 Abs. 2 GmbHG: Formnichtigkeit; Notar muss beurkunden (nicht nur beglaubigen).

## Beispiel

*Sachverhalt:* Gesellschafter-GF A scheidet aus. B wird neuer alleiniger GF.
Gesellschafterbeschluss vom 01.03.2025 liegt notariell beurkundet vor.

*Ablaufskizze (Urteilsstil):*

Der Abgang von A und die Bestellung von B sind unverzüglich nach § 39 Abs. 1
GmbHG zum Handelsregister anzumelden. Die Anmeldung muss von dem verbleibenden
Geschäftsführer B persönlich unterzeichnet werden (§ 78 GmbHG); bei mehreren
neuen GF müssen alle unterschreiben. Der Notar beglaubigt die Unterschrift
(§ 12 Abs. 1 HGB) und übermittelt die Anmeldung elektronisch (§ 12 Abs. 2 HGB).
Bis zur Eintragung kann Dritten gegenüber weder das Ausscheiden des A noch die
Vertretungsmacht des B aus dem Register entgegengehalten werden (§ 15 Abs. 1 HGB;
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
zu vermeiden, sollte B A sofort eine Löschungsvollmacht für etwaige von A noch
einzugehende Verbindlichkeiten entziehen.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Risiken und typische Fehler

- **Formfehler § 12 HGB:** Bloße Kopienbeglaubigung oder fehlende Originalunterschrift
 Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
 - Literaturhinweis gesperrt: Kommentar-, Handbuch- und Aufsatzfundstellen nur verwenden, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- **Negative Publizität (§ 15 HGB):** Nicht eingetragene Änderungen können
 Dritten gegenüber nicht geltend gemacht werden; erhebliches Haftungsrisiko
 bei verspäteter Prokura-Widerrufseintragung.
- **Versicherungspflicht § 8 Abs. 3 GmbHG:** Fehlt die Versicherung des neuen GF
 über das Nichtvorliegen von Bestellungshindernissen, wird die Anmeldung
 zurückgewiesen.
- **Falsche Registerart:** Eintragung im falschen Register (z. B. HRB statt HRA)
 bei GmbH & Co. KG führt zu Verfahrensverzögerungen.
- **Berufsrecht:** § 43a Abs. 2 BRAO, § 203 StGB; Vertraulichkeit der
 Gesellschafterdaten und -beschlüsse.

## Quellenpflicht

Alle Aussagen zu Registerpublizität und Anmeldungsform nach `references/
zitierweise.md`. § 15 HGB-Wirkungen sind differenziert darzustellen (negative
vs. positive Publizität; Gutgläubigkeitsschutz). Bei Streitfragen zur
konstitutiven vs. deklaratorischen Wirkung von Eintragungen sind h. M. und
abweichende Literaturauffassungen kenntlich zu machen.

---

## Skill: `integrations-management`

_Post-Merger-Integrations-Tracker — phasenbasierter Arbeitsplan, Zustimmungsverfolgung, Vertragsübertragung im Großmaßstab, Statusberichte. Initialisiert aus SPA, Deal-Zusammenfassung oder Abschluss-Checkliste. Berücksichtigt § 613a BGB (Betriebsübergang), BetrVG-Mitbestimmung und gesellschaftsrec..._

# Post-Merger-Integrations-Management

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Post-Merger-Integrations-Management` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Post-Merger-Integrations-Management
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Triage zu Beginn

Vor dem Start des Integrations-Trackings klären:

1. **Closing-Datum:** Wann war das Closing? (Tag-1/Tag-30/Tag-90-Workstreams hängen davon ab)
2. **SPA-Dokument verfügbar?** Vollständiges SPA oder nur Deal-Zusammenfassung?
3. **Schwerpunkt Rechtliches vs. Operatives:** Ist der Skill für rechtlichen Workstream oder operative Integration?
4. **Betriebsübergang?** Ist § 613a BGB ausgelöst? Wurden Arbeitnehmer bereits informiert?
5. **CoC-Klauseln:** Sind Tier-3-Verträge mit CoC-Klauseln identifiziert?
6. **Gesellschaftsbereinigung:** Soll eine Zielgesellschaft aufgelöst, verschmolzen oder fortgeführt werden?

## Zentrale Normen

§ 613a BGB (Betriebsübergang; Informationspflicht Abs. 5; Widerspruchsrecht Abs. 6 — 1 Monat) — §§ 111 ff. BetrVG (Interessenausgleich und Sozialplan) — § 17 KSchG (Massenentlassung) — § 40 GmbHG (Gesellschafterliste aktualisieren) — §§ 17 ff. UmwG (Verschmelzung) — §§ 65 ff. GmbHG (Liquidation) — §§ 414 f. BGB (Schuldübernahme; Vertragsübernahme) — § 25 HGB (Firmenhaftung bei Betriebsübernahme) — Art. 28 DSGVO (Auftragsverarbeitungsvertrag bei Tool-Übergabe)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- Unternehmenskaufvertrag (SPA/Anteilskaufvertrag) oder Auszüge
- deal-context.md (Mandatscode, Zielgesellschaft, Closing-Datum, Transaktionsleiter)
- Bestehende Abschluss-Checkliste, Vertragsbestand der Zielgesellschaft
- Statusmitteilungen von externem Berater, HR, Corporate Development

## Rechtlicher Rahmen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

Aufruf über Flag: `--init` (Modus 1) | `--verträge` (Modus 2) | `--bericht` (Modus 3) | `--update` (Modus 4) | `--export` (Modus 5).

### Modus 1: Initialisierung (`--init`)

deal-context.md lesen; ggf. anlegen. Abschluss-Checkliste importieren (Post-Closing-Punkte → Tag-1/30-Arbeitsplan).

Transaktionsunterlagen anfordern (Vollständiger SPA > Deal-Zusammenfassung > nichts). Phasenbasierten Arbeitsplan generieren:

**Tag 1 — rechtlich federführend:** Firmenname Handelsregister; Bankkonten-Bevollmächtigte; Gesellschafterliste § 40 GmbHG; D&O-Nachhaftungsdeckung; IP-Abtretungen.

**Tag 1 — rechtlich begleitend:** Mitarbeiterinformation § 613a Abs. 5 BGB (Frist beachten); Betriebsrat informieren; Kundenanschreiben prüfen.

**Tag 30:** Erster Zustimmungsanlauf (alle Gegenparteien); IP-Umschreibung DPMA; CoC-Vertragsanalyse (Tier 3).

**Tag 90:** Pflicht-Zustimmungen-Frist (SPA); Gesellschaftsbereinigungsentscheidung; HR-Harmonisierung (BetrVG).

**Tag 180:** Verschmelzungsanmeldung §§ 17 ff. UmwG oder Liquidationsanmeldung §§ 65 ff. GmbHG; Garantiefrist-Tracking.

### Modus 2: Vertragsübertragung (`--verträge`)

Vertragsbestand aus Datenraum, hochgeladener Liste oder SPA-Disclosure-Schedule importieren. Übertragungsmechanismus für jeden Vertrag klassifizieren:

| Mechanismus | Tier |
|---|---|
| Zustimmungserforderlich (ausdrückliche Klausel) | 1 (SPA-Pflicht) oder 2 |
| Change-of-Control-Klausel (ausgelöst durch Closing) | 3 — sofort handeln ⚠️ |
| Automatisch übertragbar (keine Beschränkung) | 4 |
| Keine Regelung (§§ 398 ff. BGB prüfen; § 354a HGB bei Kaufleuten) | 2 |

Tier-3-Verträge prominent ausweisen: CoC-Recht kann bereits mit Closing-Datum ausgelöst sein.

### Modus 3: Statusbericht (`--bericht`)

```
INTEGRATIONSSTATUS — [Mandatscode] / [Zielgesellschaft]
[Datum] — Tag [N] nach Closing

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO. Weitergabe nur nach Freigabe.

PFLICHT-ZUSTIMMUNGEN [Frist: DATUM — N Tage]
 Erhalten: [N] von [gesamt] ████░░ [%]
 Verweigert: [N] ⚠️

VERTRAGSÜBERTRAGUNG
 Tier 1–3: Status je Kategorie
 CoC offen: [N] ⚠️

ARBEITSPLAN — ÜBERFÄLLIG / DIESE WOCHE / ABGESCHLOSSEN

BLOCKIERER & ENTSCHEIDUNGSBEDARF
```

### Modus 4: Aktualisierung (`--update`)

Freitext oder hochgeladenes Statusdokument einlesen. Tracker-Einträge aktualisieren und Zusammenfassung der Änderungen zeigen.

### Modus 5: Export (`--export`)

Flaches CSV (Spalten: id, phase, beschreibung, prioritaet, frist, status, blockierer) oder Markdown-Tabelle. Formel-Injektionsschutz: Zellen aus Fremdquellen mit vorangestelltem Apostroph.

## Output-Template

**Adressat:** Internes Transaktionsteam / Mandant — Tonfall: sachlich-strukturiert, handlungsorientiert

```
PMI-STATUSBERICHT
Mandat: [MANDATSCODE]
Zielgesellschaft: [ZIELGESELLSCHAFT GmbH]
Closing-Datum: [TT.MM.JJJJ]
Bericht-Datum: [TT.MM.JJJJ] — Tag [N] nach Closing
Erstellt von: [NAME], [KANZLEI]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.
> Weitergabe nur nach ausdrücklicher Freigabe durch Transaktionsleiter.

--- PFLICHT-ZUSTIMMUNGEN (SPA-Anhang [X]) ---
Frist gemäß SPA: [TT.MM.JJJJ] ([N] Tage verbleibend)
Erhalten: [N] von [GESAMT] ████░░░░ [%]
Offen: [N] (Gegenpartei: [NAME]; kontaktiert: [DATUM])
Verweigert: [N] ⚠️ → SPA-Klausel [§/Ziff.] gefährdet

--- VERTRAGSÜBERTRAGUNGEN ---
Tier 1 (SPA-Pflicht): [N] offen / [N] abgeschlossen
Tier 2 (kein Sperrvermerk): [N] offen / [N] abgeschlossen
Tier 3 (CoC-Klausel ausgelöst): [N] ⚠️ — sofortiger Handlungsbedarf
Tier 4 (automatisch übertragen): [N] erledigt

--- GESELLSCHAFTSRECHTLICHE POST-CLOSING-PFLICHTEN ---
☐ Gesellschafterliste § 40 GmbHG beim Notar eingereicht [DATUM / OFFEN]
☐ Handelsregisteranmeldung [HRA/HRB-Nr.] aktualisiert [DATUM / OFFEN]
☐ IP-Umschreibung DPMA [DATUM / OFFEN]
☐ D&O-Nachhaftung bestätigt [DATUM / OFFEN]
☐ Bankkonten-Bevollmächtigte geändert [DATUM / OFFEN]

--- § 613a BGB / BETRIEBSÜBERGANG ---
☐ Arbeitnehmerinformation § 613a Abs. 5 BGB versandt [DATUM / OFFEN]
☐ Widerspruchsfrist (1 Monat ab Information) läuft bis: [TT.MM.JJJJ]
☐ Betriebsrat informiert (§§ 111 ff. BetrVG) [DATUM / OFFEN]
☐ Massenentlassung § 17 KSchG: [RELEVANT / NICHT RELEVANT]

--- NÄCHSTE SCHRITTE (7-Tage-Fenster) ---
1. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]
2. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]
3. [AKTION] — verantwortlich: [PERSON] — Frist: [DATUM]

--- BLOCKIERER & ENTSCHEIDUNGSBEDARF ---
⚠️ [BESCHREIBUNG BLOCKIERER] — benötigt Entscheidung von: [PERSON/GREMIUM]

--- RISIKOAMPEL ---
Gesamt: [GRÜN / GELB / ROT]
Begründung: [KURZBESCHREIBUNG]
```

## Rote Schwellen

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Tier-3-CoC-Klausel ausgelöst, aber kein Kontakt** → Recht kann mit Closing-Datum zu laufen begonnen haben; Gegenseite sofort anschreiben.
- **SPA-Pflicht-Zustimmungen: Frist < 14 Tage, < 100 %** → Transaktionsleiter eskalieren; MAC-Klausel prüfen.
- **Gesellschafterliste § 40 GmbHG > 3 Wochen nach Closing nicht beim Notar** → Haftungsrisiko; sofort beauftragen.

## Beispiel

GmbH-Anteilskauf, Closing 01.03.2025, 15 Pflicht-Zustimmungen aus SPA-Anhang, 3 CoC-Verträge. Tag-30-Bericht: 8 von 15 Zustimmungen erhalten, 2 verweigert (SPA-Pflicht gefährdet), 3 CoC-Verträge zur sofortigen Kontaktaufnahme.

## Risiken und typische Fehler

- **§ 613a Abs. 5 BGB-Informationspflicht vergessen.** Widerspruchsfrist 1 Monat läuft ab ordnungsgemäßer Information.
- **CoC-Klauseln zu spät identifizieren.** Tier-3-Verträge prominent anzeigen — Recht kann ab Closing laufen.
- **Garantiefristen nicht differenzieren.** Allgemeine, fundamentale und Steuergarantien haben unterschiedliche Überlebensfristen — aus SPA einzeln extrahieren.
- **Earn-out nicht abgrenzen.** Nur Referenzdaten führen, Eigentümer = Finance.

## Quellenpflicht

- `§ 613a Abs. 5 BGB` (Information), `§ 613a Abs. 6 BGB` (Widerspruchsfrist)
- `§§ 17 ff. UmwG` (Verschmelzung), `§§ 65 ff. GmbHG` (Liquidation), `§ 40 GmbHG` (Gesellschafterliste)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

## Skill: `kaltstart-interview`

_Ersteinrichtungs-Interview für das gesellschaftsrechtliche Praxisprofil — erfasst Tätigkeitsbereiche (M&A, Gesellschafterversammlung/Aufsichtsrat, Kapitalmarkt, Gesellschaftsverwaltung), Wesentlichkeitsschwellen, Hausstil und Eskalationsmatrix. Lädt, wenn CLAUDE.md noch [PLATZHALTER]-Marker enthä..._

# Ersteinrichtungs-Interview

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Interview** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Gesellschaftsrecht** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `Ersteinrichtungs-Interview` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: Ersteinrichtungs-Interview
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Triage zu Beginn

Vor dem Kaltstart-Interview klaeren:

1. **Profil bereits vorhanden?** CLAUDE.md lesen: vollstaendig befuellt? Falls ja: `--redo` oder `--modul [name]` verwenden, kein Neustart.
2. **Aufruf-Flag?** `--neues-mandat` (nur Transaktionskontext), `--modul ma/aufsichtsrat/kapitalmarkt/gesellschaften` (nur ein Modul), `--integrationen-pruefen` (nur Integrationen), `--redo` (Vollneustart).
3. **Zeitbudget des Nutzers?** 2 Minuten (Kurzversion: nur Rolle + aktive Module) oder 15 Minuten (vollstaendige Einrichtung inkl. Schwellenwerte und Hausstil)?
4. **Welche Module werden benoetigt?** Nicht alle Module annehmen; Nutzer explizit fragen. Pro-Tipp: Die meisten Nutzer brauchen 1-2 Module, nicht alle vier.
5. **Seed-Dokumente verfuegbar?** Wenn Nutzer Due-Diligence-Anforderungsliste oder Musterbeschluesse hochgeladen hat: aus diesen extrahieren statt manuell fragen.

## Eingaben

- Angaben des Nutzers zu Tätigkeit, Kanzlei-/Unternehmensprofil und aktivem Modul
- Optional: Bestehende Zuständigkeits- und Vollmachtsmatrix, Organisationsstruktur, Gesellschafterliste
- Seed-Dokumente je Modul (Due-Diligence-Anforderungsliste, Muster-Problemvermerk, Muster-Beschlüsse)
- Integrationsstatus (Datenraum, Boardportal, Dokumentenablage)

## Rechtlicher Rahmen

Die nachfolgenden Vorschriften bilden den rechtlichen Rahmen der unterstützten Tätigkeitsbereiche:

**Gesellschaftsrecht allgemein:** §§ 1 ff. GmbHG; §§ 1 ff. AktG; §§ 105 ff. HGB (OHG), §§ 161 ff. HGB (KG); §§ 705 ff. BGB n.F. (GbR seit 01.01.2024, MoPeG); §§ 1 ff. UmwG (Verschmelzung, Spaltung, Formwechsel).

**M&A / Unternehmenskauf:** § 311 AktG (faktischer Konzern); § 15 GmbHG (Abtretung von Geschäftsanteilen, notarielle Form); § 17 GmbHG (Kaduzierung); §§ 29 ff. GmbHG (Jahresabschluss, Gewinnverwendung). Für Beteiligungserwerb an AGs: WpÜG (Pflichtangebot ab 30 % Stimmrechte, § 29 WpÜG); §§ 327a ff. AktG (Squeeze-out).

**Beschlussfassung / Governance:** § 48 GmbHG (Gesellschafterversammlung; Abs. 2: schriftliche Abstimmung ohne Versammlung); § 49 GmbHG (Einberufung); §§ 118 ff. AktG (Hauptversammlung; § 130 AktG: Niederschrift durch Notar bei AG); §§ 95 ff. AktG (Aufsichtsrat); § 23 Abs. 5 AktG (Satzungsstrenge).

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Ablauf

### Schritt 0: Bestandsaufnahme

CLAUDE.md lesen:
- **Nicht vorhanden** → Interview starten.
- **Enthält `<!-- EINRICHTUNG PAUSIERT BEI: -->`** → Nutzer begrüßen, Fortsetzung anbieten.
- **Enthält `[PLATZHALTER]`, aber keinen Pause-Kommentar** → Vorlage unvollständig; Neustart oder Fortsetzen anbieten.
- **Vollständig befüllt** → bereits konfiguriert; überspringen, außer bei `--redo` oder `--modul [name]`.

**Modul-Flags:**
- `--redo` — vollständiges Re-Interview, überschreibt alle Abschnitte
- `--modul [ma | aufsichtsrat | kapitalmarkt | gesellschaften]` — einzelnes Modul hinzufügen oder aktualisieren
- `--neues-mandat` — Haus-Einrichtung überspringen, direkt zum transaktionsspezifischen Kontext (nur M&A-Modul)

### Schritt 0.5: Vorspann und Modulauswahl (1–2 Min.)

Vor allen weiteren Fragen zeigen:

> **`gesellschaftsrecht` unterstützt M&A-Transaktionen, Beschlussfassung und gesellschaftsrechtliche Governance, Kapitalmarktrecht sowie Gesellschaftsverwaltung und Compliance.** Anderer Schwerpunkt? Wenden Sie sich an den Legal-Builder-Hub.
>
> **2 Minuten** für Rolle, Tätigkeitssetting, Zuständigkeitsbereich und Modulauswahl. **15 Minuten** für Wesentlichkeitsschwellen im Vertragsreview, Hausstil für Beschlüsse, Gesellschafterlisten und Eskalationsmatrix.
>
> Kurzversion oder vollständige Einrichtung?

Dann fragen, welche Module aktiv sind:

> 1. **M&A** — Unternehmenskäufe, -verkäufe, Beteiligungserwerb, Fusionen
> 2. **Governance / Beschlussfassung** — Vorbereitung von Gesellschafterversammlungen, Aufsichtsratssitzungen, Protokollen, Beschlüssen
> 3. **Kapitalmarkt** — BaFin-Meldepflichten, WpHG-Compliance, Hauptversammlung börsennotierter AG, Ad-hoc-Publizität
> 4. **Gesellschaftsverwaltung** — Tochtergesellschaften, Gesellschafterliste, Jahresabschluss, Handelsregisterpflichten

### Schritt 1: Unternehmensprofil (immer, 2 Min.)

- Name der Kanzlei / des Unternehmens (für Arbeitsergebnis-Kopfzeilen)
- Tätigkeitssetting: Sozietät (solo/klein/groß) | Syndikusrechtsanwalt in-house | Behörde/Rechtsamt
- Branche und Rechtsform des betreuten Unternehmens (GmbH / AG / KG / GbR / SE)
- Eingetragener Sitz und relevante Handelsregister (HRB/HRA-Nummer)
- Größe des Rechtsteams
- Eskalationsmatrix: Wer entscheidet bei wesentlichen Fragen — Geschäftsführung, Aufsichtsrat, externer Anwalt?

Falls kein Vollmachts- und Zuständigkeitsdokument hochgeladen: Angebot, eine kompakte Vollmachtsmatrix als Standalone-Dokument zu erstellen.

### Schritt 2M: M&A-Modul (4–6 Min., falls aktiv)

- Käufer- oder Verkäuferseite als Regelfall?
- Serienakquisiteur mit Standard-Playbook oder transaktionsspezifisch?
- Wer leitet Transaktionen: Corporate-Development-Abteilung, Rechtsabteilung, externe Kanzlei als Federführer?
- Wesentlichkeitsschwelle für Vertragsreview (alle Verträge? Ab X EUR? Top-N-Verträge nach Umsatz?)
- Genutzter VDR: Intralinks, Datasite, Datenraum-eigener Cloud-Speicher?
- Seed-Dokumente: Due-Diligence-Anforderungsliste und ein früherer Problemvermerk (abgeschlossenes Mandat)

Aus Seed-Dokumenten extrahieren: Kategorienstruktur, Schwellenwerte, Hausformat für Problemvermerke.

### Schritt 2G: Governance/Beschlussfassung-Modul (3–4 Min., falls aktiv)

- Funktion: Geschäftsführer, Prokurist, Syndikusrechtsanwalt, externer Berater?
- Größe und Zusammensetzung des Aufsichtsrats / Beirats (falls vorhanden)
- Welche Form von Beschlüssen überwiegt: Gesellschafterbeschlüsse (§ 48 GmbHG), Aufsichtsratsbeschlüsse, Vorstandsbeschlüsse?
- Routinemäßige Nutzung des schriftlichen Verfahrens (§ 48 Abs. 2 GmbHG)? Bei welchen Gegenständen?
- Muster-Protokolle und Musterbeschlüsse hochladen (abgeschlossene Verfahren)

Bei AG zusätzlich: Hauptversammlung (Präsenz, virtuelle HV nach § 118a AktG, hybride HV); Notarielle Niederschrift (§ 130 AktG) — wer beauftragt den Notar?

### Schritt 2K: Kapitalmarkt-Modul (3–4 Min., falls aktiv)

- Börsenplatz (XETRA/Frankfurt, m:access, SDAX/MDAX/DAX, Drittbörse)?
- Geschäftsjahresende und Berichtspflichten (HGB oder IFRS)?
- BaFin-Meldepflichten: Stimmrechtsmitteilungen (§§ 33 ff. WpHG), Insiderverzeichnis (Art. 18 MAR)?
- Offenlegungsausschuss: Zusammensetzung, Turnus?
- Zuständigkeit für Ad-hoc-Publizität (Art. 17 MAR) — Rechtsabteilung, IR, Vorstand?

### Schritt 2V: Gesellschaftsverwaltungs-Modul (2–3 Min., falls aktiv)

- Anzahl aktiv verwalteter Gesellschaften
- Wesentliche Sitzstaaten (Deutschland, EU, Drittstaaten)
- Registerführung: Elektronische Gesellschafterliste (§ 40 GmbHG), automatische Handelsregisterüberwachung?
- Nutzung eines Entity-Management-Systems oder Tabellenkalkulation?
- Jahresabschluss-Pflichten (§§ 242 ff. HGB; Offenlegung §§ 325 ff. HGB)?

### Nach dem Interview

Zusammenfassung zeigen, Praxisprofil erstellen, Pflege erläutern:

> Ihr Praxisprofil liegt in CLAUDE.md. Änderungen jederzeit direkt oder per `/gesellschaftsrecht:gesellschaftsrecht-kaltstart-interview --redo` möglich. Am häufigsten angepasst: Wesentlichkeitsschwellen, Hausstil für Beschlüsse, Eskalationsmatrix.

## Output-Template

**Adressat:** Praxis-Nutzer / Kanzlei-intern — Tonfall: sachlich-bestaedigend, handlungsanleitend

```

## Gesellschaftsrecht Praxisprofil
_Erstellt: [TT.MM.JJJJ] — Version 1.0_

### Unternehmen / Kanzlei
Name: [KANZLEI / UNTERNEHMEN]
Taetigkeitssetting: [Sozietaet / Syndikusrechtsanwalt in-house / Rechtsamt]
Branche: [BRANCHE]
Rechtsform betreuter Gesellschaften: [GmbH / AG / SE / KG / etc.]
Sitz: [ORT]
Registergericht: [AMTSGERICHT ORT] — HRB [NUMMER]
Rechtsteam-Groesse: [N] Personen

### Eskalationsmatrix
Wesentliche Entscheidungen: [PERSON / GREMIUM]
Externe Eskalation ab: [BETRAG EUR / BESCHREIBUNG]
Externe Kanzlei: [NAME]

### Aktive Module
| Modul | Aktiv | Konfiguriert |
|---|---|---|
| M&A | [JA / NEIN] | [JA / AUSSTEHEND] |
| Governance / Beschlussfassung | [JA / NEIN] | [JA / AUSSTEHEND] |
| Kapitalmarkt | [JA / NEIN] | [JA / AUSSTEHEND] |
| Gesellschaftsverwaltung | [JA / NEIN] | [JA / AUSSTEHEND] |

### M&A-Modul (falls aktiv)
Regelfall: [Kaeuferseite / Verkaeuferseite / variabel]
Wesentlichkeitsschwelle Vertragsreview: [BETRAG EUR]
VDR-Plattform: [INTRALINKS / DATASITE / ANDERES]
KI-Massenreview-Vertrauen: [ERGEBNIS UEBERNEHMEN / 10-PROZENT-STICHPROBE / VOLLPRUEFUNG]

### Governance-Modul (falls aktiv)
Hausbeschlussformat: [BESCHLOSSEN: / Beschluss Nr. / etc.]
Bevorzugte Unterzeichner: [LISTE]
Notarielle Beurkundung erforderlich bei: [SATZUNGSAENDERUNG / KAPITALMASNAHME / etc.]

### Gesellschaftsverwaltungs-Modul (falls aktiv)
Anzahl aktiv verwalteter Gesellschaften: [N]
Entity-Management-System: [NAME / TABELLE]
Jahresabschluss-Pflichten: [HGB / IFRS]

### Integrationen
| System | Status | Letzter Test |
|---|---|---|
| [VDR-NAME] | [VERBUNDEN / NICHT VERBUNDEN] | [DATUM] |
| Handelsregister | [VERBUNDEN / NICHT VERBUNDEN] | [DATUM] |

_Profil-Pflege: Einzelne Aenderungen per `/gesellschaftsrecht:gesellschaftsrecht-anpassen`.
Vollstaendige Neueinrichtung per `/gesellschaftsrecht:gesellschaftsrecht-kaltstart-interview --redo`._
```

## Rote Schwellen

- **Modul-Annahme ohne Nachfragen** — nicht alle Module als aktiv annehmen; Nutzer verliert Zeit mit irrelevanten Fragen; immer zuerst fragen.
- **Konkrete Schwellenwerte nicht erfasst** — 'uebliche Schwellen' ist kein Wert; nach Zahlen fragen.
- **Profil mit Platzhaltern abgeschlossen** — `[PLATZHALTER]` in CLAUDE.md fuehrt dazu, dass Skills falsche Defaultwerte verwenden; nur als `[AUSSTEHEND]` mit Erklaerung belassen.

## Beispiel

**Szenario:** Syndikusrechtsanwalt einer GmbH mit 200 Mitarbeitern, aktive Module M&A und Governance.

Nach dem Interview: Praxisprofil enthält Wesentlichkeitsschwelle 100.000 EUR für Vertragsreview, Hausstil "BESCHLOSSEN:" für schriftliche Gesellschafterbeschlüsse nach § 48 Abs. 2 GmbHG, Eskalation zu externem M&A-Berater ab Transaktionsvolumen > 5 Mio. EUR. Kapitalmarkt- und Gesellschaftsverwaltungsmodul: nicht aktiviert.

## Risiken und typische Fehler

- **Alle Module als aktiv annehmen.** Erst fragen, dann nur relevante Abschnitte aufbauen. Ein M&A-Anwalt braucht kein Kapitalmarkt-Modul.
- **Käuferseite als Regelfall annehmen.** Das Praxisprofil erfasst den Hausstandard; die spezifische Rolle je Transaktion wird mit `--neues-mandat` festgelegt.
- **Generische Platzhalter eintragen.** "Übliche Wesentlichkeitsschwellen" ist kein Schwellenwert. Nach konkreten Zahlen fragen.
- **Seed-Dokumente für inaktive Module anfordern.** Nur die Anforderungsliste und den Problemvermerk anfordern, wenn M&A aktiv ist.
- **Faktenprüfung unterlassen.** Wenn der Nutzer eine Norm oder Frist nennt (z.B. "Anmeldefrist 3 Wochen nach Beschluss"), plausibilisieren und bei Abweichung flaggen: "[Prämisse geprüft — bitte verifizieren]".

## Quellenpflicht

Jeder Verweis auf Vorschriften in CLAUDE.md und in Skill-Ausgaben muss zitieren:
- Gesetze mit Paragraphenzeichen: `§ 48 Abs. 2 GmbHG`, `§ 130 AktG`
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Keine bloßen Gesetzesnummern ohne Paragraphenzeichen

Hinweis: Dieser Skill ersetzt keine anwaltliche Beratung im konkreten Einzelfall.

---

## Skill: `ki-werkzeug-uebergabe`

_KI-Tool-Übergabe für Massenvertragsprüfungen an Luminance oder Kira. Laden wenn der Nutzer Luminance, Kira, KI-Prüfung, automatische Extraktion oder Massenprüfung erwähnt oder der Datenraum mehr als ~50 Verträge enthält, die ein einheitliches Klausel-Extraktionsprofil erfordern im Gesellschaftsre..._

# KI-Tool-Übergabe (Luminance / Kira)

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

## Fachlicher Kern — Gesellschaftsrecht und Corporate Law
- **Problemfokus dieses Skills:** Bleibe beim konkreten Titel `KI-Tool-Übergabe (Luminance / Kira)` und löse die dort angelegte Fachfrage; arbeite mit konkreten Tatbestandsmerkmalen, Beweisfragen und dem unmittelbar benötigten Arbeitsprodukt. Routingfragen bleiben Hilfsmittel, wenn Frist, Zuständigkeit oder Verfahrensart offen sind.
- **Normenradar:** GmbHG §§ 3, 5, 13, 15, 16, 30, 34, 35, 40, 43, 46, 47, 49 ff.; AktG §§ 76, 93, 111, 119, 130, 243 ff.; HGB §§ 105 ff., 161 ff.; MoPeG/GesRÄndG-Folgen; UmwG; FamFG/Registerrecht; GWB/Fusionskontrolle bei Transaktionen.
- **Verifizierte Anker:** BGH, Urteil vom 08.11.2022 - II ZR 91/21 (zutreffende Gesellschafterliste/Listenstreit); BGH, Beschluss vom 18.03.2025 - II ZB 11/24 (Registerordner/Gesellschafterliste, Prüfungsumfang); BGH, Urteil vom 11.12.2006 - II ZR 166/05 und Urteil vom 12.04.2016 - II ZR 275/14 (Treuepflicht, Zustimmungspflichten); BGH, Urteil vom 30.09.2025 - II ZR 154/23 (Drittvergleich/verdeckte Vermögenszuwendung, Organ-/Beschlusskontrolle).
- **Arbeitsmodus:** Erst Gesellschaftsform, Organ, Beschlussweg, Vertretung, Registerlage, wirtschaftliches Ziel und Minderheitenposition sortieren; dann Treuepflicht, Kapitalerhaltung, Haftung, Transaktions-Closing und Beweis-/Vollzugsrisiko prüfen.
- **Outputpflicht:** Beschluss-/Listenmatrix, Register-To-do, Board-/Beiratsvorlage, Closing-CP-Liste, Treuepflicht-Red-Team, Geschäftsführerhaftungsmemo oder Mandanten-Decision-Paper.
- **Fehlerbremse:** Tragende Normen/Entscheidungen live oder aus der Akte verifizieren; Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate aus Modellwissen.

## Fachkern: KI-Tool-Übergabe (Luminance / Kira)
- **Normen-/Quellenanker:** GmbHG, AktG, HGB, BGB, UmwG, MoPeG, FamFG/Registerrecht, Gesellschafterliste, Beschlussmängel, Treuepflicht und Organhaftung.
- **Entscheidende Weiche:** Gesellschaftsform, Organrolle, Beschluss/Vertrag, Registerwirkung, Minderheitenschutz, Haftung und Frist getrennt prüfen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Triage zu Beginn

Vor der Tool-Ubergabe klaeren:

1. **Volumen:** Wie viele Dokumente sind im Datenraum? (< 50: manuelle Prüfung effizienter; 50-200: bedingt sinnvoll; > 200: KI-Tool empfohlen)
2. **Tool vorhanden?** Ist Luminance, Kira oder ein vergleichbares Tool bereits im Praxisprofil konfiguriert? Welches Vertrauensniveau ist eingestellt?
3. **Kategorien:** Sind die Verträge bereits grob kategorisiert (Lieferanten, Kunden, IP, Miet-, Arbeitsverträge)?
4. **AVV geklaert?** Liegt ein Auftragsverarbeitungsvertrag (Art. 28 DSGVO) mit dem Tool-Anbieter vor? Hat der Mandant der Weitergabe zugestimmt?
5. **Rechtsordnung:** Werden auch Verträge nach auslaendischem Recht gepüft? (gesondertes Profil erforderlich)
6. **QA-Ressourcen:** Wer fuehrt die Stichproben-QA durch? Wie viel Zeit steht zur Verfuegung?

## Zentrale Normen

§ 398 BGB (Forderungsabtretung) — § 399 BGB (Abtretungsverbot) — § 354a HGB (Abtretungsverbot unter Kaufleuten; ggf. unwirksam) — §§ 305 ff. BGB (AGB-Kontrolle) — § 307 BGB (unangemessene Benachteiligung) — § 613a BGB (Betriebsubergang; Vertragsuebergang) — §§ 69b, 43 UrhG (Arbeitnehmererfindung) — Art. 28 DSGVO (Auftragsverarbeitungsvertrag bei Datenweitergabe) — § 130 OWiG (Aufsichtspflichtverletzung bei Compliance-Verstoss)

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Eingaben

- Praxisprofil: `## M&A → KI-gestützte Prüfung` (Tool-Name, Verwendungszweck, Vertrauensniveau, Übergabe-Ablauf)
- VDR-Inventar oder Ordnerliste mit Kategorien
- Klausel-Extraktionsprofil (Standardprofil unten oder Hausformat aus Praxisprofil)
- Anzahl Dokumente in der Übergabecharge
- Deal-Code und Datenraumstruktur

## Ablauf

### Schritt 1: Kategorie-Triage

Nicht jede Kategorie ist für KI-Massenprüfung geeignet. Einschätzen:

| Kategorie | Eignet sich für KI-Tool | Begründung |
|---|---|---|
| Wesentliche Verträge (>50 gleichartige) | ✓ | Standardklauseln, hohes Volumen |
| Rahmenverträge / MSA | ✓ | Strukturierte Klauseln |
| IP-Lizenzverträge | Bedingt | Komplexe Terminologie; Stichproben-QA |
| Arbeitsverträge | Bedingt | Länderspezifische Normen; § 307 BGB |
| Gesellschaftsverträge / Satzungen | ✗ | Besprechungs- und Kontextbedarf |
| Side Letters / Anpassungsvereinbarungen | ✗ | Zu nuanciert für Bulk-Extraktion |

### Schritt 2: Extraktionsprofil erstellen

Für jede Vertragsart ein Extraktionsprofil mit den zu extraktierenden Klauseln erstellen:

**Standardprofil M&A – deutsches Recht:**

```yaml
extraktionsprofil:
 change_of_control:
 frage: "Gibt es eine Change-of-Control-Klausel? Ist Zustimmung erforderlich?"
 rechtsgrundlage: "Kein gesetzliches Zustimmungserfordernis; rein vertragliche Regelung"
 relevanz: "Zustimmungserfordernis vor Vollzug"
 kuendigungsrecht_abtretung:
 frage: "Gibt es ein Kündigungsrecht oder Abtretungsverbot bei Eigentümerwechsel?"
 rechtsgrundlage: "§ 398 BGB (Abtretung), § 613a BGB (Betriebsübergang)"
 relevanz: "Hemmt Vollzug oder Vertragsübertragung"
 wettbewerbsverbot:
 frage: "Enthält der Vertrag ein Wettbewerbs- oder Exklusivitätsverbot?"
 rechtsgrundlage: "§ 138 BGB (Sittenwidrigkeit), Bindung nach UWG"
 relevanz: "Schränkt Käufer-Geschäft ein"
 haftungsbegrenzung:
 frage: "Gibt es eine Haftungsobergrenze? In welcher Höhe? AGB oder Individualvereinbarung?"
 rechtsgrundlage: "§§ 305 ff. BGB (AGB-Kontrolle); § 309 Nr. 7 BGB"
 relevanz: "Risikoquantifizierung; AGB-Unwirksamkeit prüfen"
 ip_eigentum:
 frage: "Wer ist Eigentümer der erzeugten IP? Enthält der Vertrag eine Abtretung?"
 rechtsgrundlage: "§§ 69b, 43 UrhG (Arbeitnehmererfindung); § 7 ArbNErfG"
 relevanz: "IP-Kette zum Zielunternehmen"
 kuendigungsfristen:
 frage: "Wie sind ordentliche und außerordentliche Kündigung geregelt?"
 rechtsgrundlage: "§§ 314, 615 BGB; vertraglich oder gesetzlich"
 relevanz: "Risiko vorzeitiger Beendigung nach Vollzug"
 agb_kontrolle:
 frage: "Wurden die AGB einbezogen? Welcher Partei? Gültige Einbeziehung gem. §§ 305 ff. BGB?"
 rechtsgrundlage: "§§ 305, 307, 309 BGB"
 relevanz: "Unwirksame Klauseln trotz Vertragstext"
 compliance:
 frage: "Gibt es Compliance-Zusicherungen (Korruptionsverbote, Sanktionen, Exportkontrolle)?"
 rechtsgrundlage: "§ 130 OWiG; AWG/AWV; GwG"
 relevanz: "Compliance-Risiko des Zielunternehmens"
```

### Schritt 3: Tool-Übergabe-Paket erstellen

Das Übergabe-Paket enthält:

1. **Extraktionsprofil** (YAML oben, ggf. im Tool-nativen Format)
2. **Dokument-Inventar** (Liste aller Dokumente mit VDR-Pfad, Kategorie, Dateiname)
3. **Priorisierung** (Top-N nach Wert oder Relevanz zuerst)
4. **QA-Stichprobenplan** (welche %-QA für diesen Auftrag)

```markdown

## Übergabe-Paket – [Deal-Code] – [Datum]

**Tool:** [Luminance / Kira / anderes]
**Volumen:** [N] Dokumente
**Kategorien:** [Liste]
**Extraktionsprofil:** [Anlage-Link]
**Priorisierung:** [nach Wert >X EUR / Top-50 / vollständig]
**QA-Plan:** Stichprobe 10 % oder [N] Dokumente, gleichmäßig über Kategorien verteilt
**Erwartete Lieferzeit:** [N] Stunden/Tage
**Rückgabeformat:** [XLSX / CSV / Tool-API]
**Übergabe an:** [Tool-Administrator / externes Dienstleister]
```

### Schritt 4: QA-Schicht

Nach Erhalt der Tool-Ausgabe:

1. **Stichproben-QA**: [N] Dokumente manuell gegenlesen
 - Vollständigkeit: Alle extraktierten Klauseln vorhanden?
 - Richtigkeit: Klausel korrekt klassifiziert?
 - Falsch-Negative: Übersehene wesentliche Klauseln?
 - Falsch-Positive: Irrelevante Klauseln einbezogen?

2. **Fehler-Typen dokumentieren**:

```markdown
QA-Bericht – [Deal-Code]
- Geprüfte Dokumente: [N] von [M] ([%])
- Fehlerrate: [N] Fehler in [N] geprüften Dokumenten
- Häufige Fehler: [Beschreibung]
- Anpassung Extraktionsprofil: [ja / nein; wenn ja: was]
- Gesamtbewertung Vertrauensniveau: [hoch / mittel / niedrig]
```

3. **Vertrauensniveau aus Praxisprofil anwenden:**
 - `Ergebnis übernehmen`: Direkt in DD-Issues übernehmen, QA-Ergebnis vermerken
 - `Stichproben`: Mittleres Vertrauensniveau; alle 🔴-Issues manuell nachprüfen
 - `Vollständige Neuprüfung`: Nur Screening verwenden; alle Issues selbst extrahieren

### Schritt 5: Rückübergabe an DD-Issue-Extraktion

Tool-Ergebnisse im Standardformat für den `dd-findings-extraktion`-Skill übergeben:

```yaml
ki_tool_ergebnisse:
 tool: "Luminance"
 version: "2024.3"
 datum: "[DATUM]"
 vertrauensniveau: "mittel"
 qa_stichprobe_prozent: 10
 dokumente_gesamt: 312
 findings:
 - dokument: "VDR/02-Verträge/Acme-MSA-2021.pdf"
 kategorie: "Wesentliche Verträge"
 klausel: "change_of_control"
 extrakt: "§ 12 Abs. 3: Bei Kontrollwechsel hat [Vertragspartner] das Recht, fristlos zu kündigen."
 schweregrad_vorschlag: "🔴"
 ki_konfidenz: 0.92
 qa_geprueft: true
 qa_korrekt: true
```

## Quellen und Zitierweise

Normen-Basis für Extraktionsprofil: §§ 305 ff. BGB (AGB-Kontrolle), § 398 BGB (Abtretung), § 613a BGB (Betriebsübergang), §§ 69b, 43 UrhG, § 7 ArbNErfG, § 130 OWiG.

Zitierweise nach `../../references/zitierweise.md`.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Output-Template

**Adressat:** Tool-Administrator / DD-Team-intern — Tonfall: strukturiert, technisch-praezise

```
KI-TOOL-ÜBERGABE-PAKET
Mandat: [MANDATSCODE]
Deal-Code: [DEAL-CODE]
Datum: [TT.MM.JJJJ]
Tool: [LUMINANCE / KIRA / ANDERES]
Erstellt von: [NAME], [KANZLEI]

> Vertraulich — Mandatsgeheimnis § 43a Abs. 2 BRAO.
> Weitergabe an Tool-Anbieter nur nach AVV gem. Art. 28 DSGVO und Mandantenzustimmung.

--- CHARGE-BESCHREIBUNG ---
Dokumente gesamt: [N]
Kategorien:
 - [KATEGORIE 1]: [N] Dokumente — Eignung: [HOCH / BEDINGT / NIEDRIG]
 - [KATEGORIE 2]: [N] Dokumente — Eignung: [HOCH / BEDINGT / NIEDRIG]
Ausgeschlossen (manuell zu prüfen): [N] Dokumente (Gesellschaftsvertraege, Side Letters)

--- EXTRAKTIONSPROFIL ---
Version: [v1.0]
Rechtsordnung: [Deutsches Recht / Englisches Recht / Gemischt]
Klauseln im Profil:
 1. change_of_control — [§ Vertrag; CoC-Recht]
 2. abtretungsverbot — [§ 399 BGB; § 354a HGB]
 3. haftungsbegrenzung — [§§ 305 ff. BGB]
 4. wettbewerbsverbot — [§ 138 BGB]
 5. kuendigungsfristen — [§§ 314, 615 BGB]
 [weitere nach Profil]

--- PRIORISIERUNG ---
Top-[N] nach [Vertragswert / Relevanz]: [LISTE]
Vollstaendige Prufung: [JA / NEIN]

--- QA-PLAN ---
Stichprobe: [N] % = [N] Dokumente
Vertrauensniveau Praxisprofil: [ERGEBNIS UEBERNEHMEN / 10-PROZENT-STICHPROBE / VOLLPRÜFUNG]
QA-Verantwortlich: [NAME]
QA-Frist: [TT.MM.JJJJ]

--- ERWARTETER ABLAUF ---
Uebergabe an Tool: [TT.MM.JJJJ]
Erwartete Lieferung: [TT.MM.JJJJ]
Rueckgabeformat: [XLSX / CSV / YAML]

--- QA-BERICHT (nach Lieferung auszufuellen) ---
Geprüfte Dokumente: [N] von [M] ([%])
Fehlerrate: [N] Fehler
Haeufige Fehlertypen: [BESCHREIBUNG]
Gesamtbewertung Vertrauensniveau: [HOCH / MITTEL / NIEDRIG]
Empfehlung: [ERGEBNIS DIREKT UEBERNEHMEN / NACHPRUEFUNG ERFORDERLICH FUER ROT-FINDINGS]
```

## Rote Schwellen

- **Kein AVV (Art. 28 DSGVO) vor Datenweitergabe** — Bussgeldhaftung; Weitergabe sofort stoppen bis AVV vorliegt.
- **KI-Vertrauensniveau "vollstaendige Neuprüfung" und kein QA-Budget** — KI-Tool liefert nur Screening; alle Findings sind manuell zu verifizieren bevor Garantien abgegeben werden.
- **Gesellschaftsvertraege / Side Letters in Batch** — ungeeignet für Bulk-Extraktion; sofort aus Charge herausnehmen und manuell prüfen.
- **Abtretungsverbote nicht klassifiziert** — Haftungsrisiko bei Garantien; § 354a HGB-Prüfung für Kaufleute-Vertraege immer separat durchfuehren.

## Beispiel

**Eingabe:** Datenraum enthält 280 Lieferantenverträge; Luminance konfiguriert.

**Ausgabe:** Übergabe-Paket mit Extraktionsprofil (8 Klauseln), Priorisierung Top-50 nach Vertragswert >100 TEUR, QA-Stichprobenplan 10 %. Nach QA: 15 🔴-Findings (davon 3 Change-of-Control mit Zustimmungserfordernis) → direkt an Vollzugscheckliste übergeben.

## Risiken / typische Fehler

- **Falsch-Negative bei AGB-Kontrolle:** KI-Tools übersehen oft die AGB-Einbeziehungs-Frage (§ 305 BGB). Immer manuell nachprüfen, ob AGB wirksam einbezogen wurden.
- **Change-of-Control ohne Zustimmungs-Prüfung:** Klausel extrahiert, aber nicht geprüft, ob bloßes Informationsrecht oder echtes Zustimmungserfordernis. Manuelle Klassifizierung erforderlich.
- **Jurisdiktion nicht erkannt:** Bei internationalen Verträgen (z. B. englisches Recht) falsche Klauselklassifizierung. Rechtsordnung im Profil explizit angeben.
- **Vertrauen ohne QA:** Kein Tool ist 100 % korrekt. QA-Stichproben sind nicht optional.
- **Mandantengeheimnis:** Dokumente an Drittanbieter weitergeben erfordert Auftragsverarbeitungsvertrag (AVV) gem. Art. 28 DSGVO und Zustimmung des Mandanten.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

