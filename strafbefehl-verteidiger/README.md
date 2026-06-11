# Strafbefehl-Verteidiger

<!-- BEGIN plugin-sofort-download-section (autogen) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`strafbefehl-verteidiger.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/strafbefehl-verteidiger.md) (115 KB)
- Im Repo: [`testakten/megaprompts/strafbefehl-verteidiger.md`](../testakten/megaprompts/strafbefehl-verteidiger.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strafbefehl-verteidiger`) | [`strafbefehl-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafbefehl-verteidiger.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **LUMEN Studios GmbH — Insolvenz- und Wirtschaftsstrafverfahren** (`lumen-studios-insolvenz-strafverfahren`) | [Gesamt-PDF lesen](../testakten/lumen-studios-insolvenz-strafverfahren/gesamt-pdf/lumen-studios-insolvenz-strafverfahren_gesamt.pdf) | [`testakte-lumen-studios-insolvenz-strafverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) |
| **Strafbefehl – Ladendiebstahl und Fahrerflucht** (`strafbefehl-ladendiebstahl-fahrerflucht`) | [Gesamt-PDF lesen](../testakten/strafbefehl-ladendiebstahl-fahrerflucht/gesamt-pdf/strafbefehl-ladendiebstahl-fahrerflucht_gesamt.pdf) | [`testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafbefehl-ladendiebstahl-fahrerflucht.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein freistehender Strafbefehls-Assistent für Kanzleien: vom Fristnotruf über Akteneinsicht und Einspruch bis zur beschränkten Rechtsfolgenstrategie oder Hauptverhandlung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn Register, Kanzleisoftware, beA, E-Mail, Datenraum oder Aktenexport fehlen, arbeitet es mit manuellen Uploads oder mit einem klar gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `strafbefehl-kommandocenter` starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nicht raten lassen, sondern mit der passenden Vorlage nachfordern oder Simulation ausdrücklich aktivieren.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `strafbefehl-kommandocenter` - Strafbefehl-Kommandocenter
- `strafbefehl-aktenanlage` - Aktenanlage Strafbefehl
- `strafbefehl-fristen-einspruch` - Frist und Einspruch nach § 410 StPO
- `strafbefehl-akteneinsicht-147` - Akteneinsicht
- `strafbefehl-zulaessigkeit-407` - Zulässigkeit des Strafbefehls
- `strafbefehl-inhalt-409-pruefung` - Inhaltsprüfung nach § 409 StPO
- `strafbefehl-einspruch-beschraenkung` - Einspruch beschränken oder nicht
- `strafbefehl-wiedereinsetzung` - Wiedereinsetzung
- `strafbefehl-pflichtverteidiger` - Pflichtverteidigung
- `strafbefehl-polizeifilmerei-201-kug` - Film-, Foto- und Tonaufnahmen von Polizeieinsätzen
- `strafbefehl-tagessaetze-geldstrafe` - Tagessätze und Geldstrafe
- `strafbefehl-nebenfolgen-fahrerlaubnis` - Nebenfolgen
- `strafbefehl-beweis-und-einlassung` - Beweis und Einlassung
- `strafbefehl-zeugen-befragungsstrategie` - Zeugenbefragung
- `strafbefehl-hauptverhandlung-vorbereitung` - Hauptverhandlung vorbereiten
- `strafbefehl-abwesenheit-vertretung` - Abwesenheit und Vertretung
- `strafbefehl-einstellung-153-153a-170` - Einstellung und Verständigung
- `strafbefehl-deal-verstaendigung` - Gesprächsstrategie mit Gericht und Staatsanwaltschaft
- `strafbefehl-rechtsmittel-nach-urteil` - Rechtsmittel nach Urteil
- `strafbefehl-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `strafbefehl-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/strafbefehl-mandatskarte.md` - Strafbefehl-Mandatskarte
- `assets/templates/frist-einspruch-410.md` - Frist und Einspruch nach § 410 StPO
- `assets/templates/akteneinsicht-147.md` - Akteneinsicht nach § 147 StPO
- `assets/templates/strafbefehl-inhaltspruefung.md` - Inhaltsprüfung Strafbefehl
- `assets/templates/einspruch-unbeschraenkt.md` - Unbeschränkter Einspruch
- `assets/templates/einspruch-beschraenkt.md` - Beschränkter Einspruch
- `assets/templates/wiedereinsetzung.md` - Wiedereinsetzung
- `assets/templates/pflichtverteidiger-check.md` - Pflichtverteidiger-Check
- `assets/templates/tagessaetze.md` - Tagessatzprüfung
- `assets/templates/einlassungsstrategie.md` - Einlassungsstrategie
- `assets/templates/zeugen-fragenkatalog.md` - Zeugenfragen
- `assets/templates/hauptverhandlung-plan.md` - Hauptverhandlung
- `assets/templates/einstellung-153-153a.md` - Einstellung nach §§ 153, 153a StPO
- `assets/templates/nebenfolgen-fahrerlaubnis.md` - Nebenfolgen
- `assets/templates/rechtsmittel-nach-urteil.md` - Rechtsmittel nach Urteil
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 55 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenanlage-fehlerkatalog` | Aktenanlage Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `akteneinsicht-behoerden-gericht-und-registerweg` | Akteneinsicht: Behörden-, Gerichts- oder Registerweg. |
| `anschluss-routing` | Anschluss-Routing für Strafbefehl-Verteidigung: wählt den nächsten Spezial-Skill nach Engpass (§ 410 StPO Einspruch 2 Wochen, Strafbefehl, Ermittlungsakte, Einspruchsschrift), dokumentiert Router-Entscheidung mit Begründung. |
| `deal-beweislast-einspruch` | Deal: Beweislast, Darlegungslast und Substantiierung. |
| `dokumente-intake` | Dokumentenintake für Strafbefehl-Verteidigung: sortiert Strafbefehl, Ermittlungsakte, Einspruchsschrift, prüft Datum, Absender, Frist und Beweiswert (Vernehmungen, Zeugen); markiert Lücken; berücksichtigt Mandatsgeheimnis § 43a BRAO. |
| `einspruch-risikoampel-und-gegenargumente` | Einspruch: Risikoampel, Gegenargumente und Verteidigungslinien. |
| `einspruchsentscheidung-und-folgen` | Einspruchsentscheidung, Beschränkung und Nebenfolgen beim Strafbefehl: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output im Strafbefehl Verteidiger. |
| `einstellung-153a-hauptverhandlung` | Einstellung im Strafbefehlsverfahren: § 153 StPO (Geringfuegigkeit ohne Auflage) § 153a StPO (mit Auflage) § 170 Abs. 2 StPO (Einstellung mangels hinreichenden Tatverdachts). Opportunitaetsprinzip. Zustimmungserfordernisse. BZR-Eintrag b... |
| `einstellung-fahrerlaubnis` | Einstellung: Compliance-Dokumentation und Aktenvermerk. |
| `einstieg-routing` | Einstieg, Triage und Routing für Strafbefehl-Verteidigung: ordnet Rolle (Beschuldigter, Staatsanwaltschaft, Amtsrichter), markiert Frist (§ 410 StPO Einspruch 2 Wochen), wählt Norm (§§ 407 ff. StPO, § 410 StPO Einspruch 2 Wochen) und Zus... |
| `fahrerlaubnis-mandantenentscheidung` | Fahrerlaubnis: Mandantenkommunikation und Entscheidungsvorlage. |
| `hauptverhandlung-international-schnittstellen` | Hauptverhandlung: Internationaler Bezug und Schnittstellen. |
| `mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten im Strafbefehl Verteidiger. |
| `nebenfolgen-fahrerlaubnis-strafbefehl` | Fahrerlaubnisentzug § 69 StGB und Fahrverbot § 44 StGB im Strafbefehl. Regelentziehung § 69 Abs. 2 StGB bei §§ 315c 316 142 StGB. Sperrfrist § 69a StGB. Vorzeitige Aufhebung § 69a Abs. 7 StGB. Abgrenzung § 25 StVG (OWi-Fahrverbot). MPU-A... |
| `nebenfolgen-strafbefehl-strafbefehls` | Nebenfolgen: Verhandlung, Vergleich und Eskalation. |
| `output-waehlen` | Output-Wahl für Strafbefehl-Verteidigung: stimmt Adressat (Beschuldigter, Staatsanwaltschaft, Amtsrichter), Frist (§ 410 StPO Einspruch 2 Wochen) und Form auf den Zweck ab — typische Outputs: Einspruch, Akteneinsicht-Antrag, Verteidigung... |
| `pflichtverteidigung-quellenkarte` | Pflichtverteidigung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `quellen-livecheck` | Quellen-Live-Check für Strafbefehl-Verteidigung: prüft Normen (§§ 407 ff. StPO, § 410 StPO Einspruch 2 Wochen) gegen amtliche Datenbank, Rechtsprechung mit Gericht-Datum-Az-Rn; nutzt Amtsgericht und Quellenhygiene nach references/quellen... |
| `rechtsmittel-tagessaetze-geldstrafe` | Rechtsmittel nach Urteil in der Hauptverhandlung nach Strafbefehl-Einspruch. Berufung § 312 StPO (Frist 1 Woche schriftlich). Revision § 333 StPO (Frist 1 Woche Rechtsfehler). Revisionsbegründung § 345 StPO 1 Monat. Absolute Revisionsgrü... |
| `start-chronologie-fristen` | Einstieg, Schnelltriage und Fallrouting im Strafbefehl Verteidiger-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei... |
| `stbv-einspruch-strafbefehl-fahrerlaubnis` | Leitfaden Einspruch gegen Strafbefehl: Form, Frist, Beschraenkung auf Rechtsfolge, taktische Erwaegungen. Pruefraster für Verteidiger im Strafbefehl Verteidiger. |
| `stbv-fahrerlaubnis-bei-strafbefehl-spezial` | Spezialfall Fahrerlaubnis bei Strafbefehl § 111a StPO und § 69 StGB: vorläufige Entziehung, Sperrfrist, Wiedererteilung. Pruefraster für Verteidiger und Fahrerlaubnisbehoerde im Strafbefehl Verteidiger. |
| `stbv-strafbefehl-abwesenheit-vertretung` | Bauleiter Prüfung Strafbefehl § 407 StPO: Tatvorwurf, Strafhoehe, Folgen, Einspruchsfrist. Pruefraster für Verteidiger Erstgespraech im Strafbefehl Verteidiger. |
| `stbv-strafbefehl-auslaendischer-mandant-spezial` | Spezialfall Strafbefehl gegen auslaendischen Mandanten: Uebersetzungspflicht, Auslieferung, Eintrag im Bundeszentralregister, Einreise. Pruefraster für Verteidiger im Strafbefehl Verteidiger. |
| `strafbefehl-abwesenheit-vertretung` | Mandant kann oder will zur Hauptverhandlung nach Strafbefehl-Einspruch nicht erscheinen und Verteidiger soll ihn vertreten. Prüfraster Entbindung von Erscheinungspflicht § 411 Abs. 2 StPO Voraussetzungen und Antrag. Verwerfung des Einspr... |
| `strafbefehl-aktenanlage` | Neues Strafbefehl-Mandat anlegen und Mandatsakte strukturieren damit Fristen und Beweismittel sicher verwaltet werden. Prüfraster Aktenstruktur Vollmacht Fristenkalender Beweismittelverzeichnis. Normen § 410 StPO Einspruchsfrist § 147 St... |
| `strafbefehl-akteneinsicht-147` | Akteneinsicht im Strafbefehlsverfahren nach § 147 StPO. Antrag bei Staatsanwaltschaft oder Amtsgericht. Versagungsgründe § 147 Abs. 2 StPO. Akte im Strafbefehlsverfahren: Ermittlungsakte Messakte Bußgeldheft. Beschwerderecht § 147 Abs. 5... |
| `strafbefehl-deal-verstaendigung` | Verständigung nach § 257c StPO im Strafbefehlsverfahren. Voraussetzungen Inhalt Bindungswirkung Belehrung nach § 257c Abs. 4 und 5 StPO. Grenzen: kein Freispruch kein Schuldspruchverzicht. Abgrenzung informelle Absprache. Ablaufprotokoll... |
| `strafbefehl-dokumentenmatrix-und-lueckenliste` | Strafbefehl: Dokumentenmatrix, Lückenliste und Nachforderung. |
| `strafbefehl-einlassung-deal-verstaendigung` | Beweisprüfung und Einlassungsstrategie im Strafbefehlsverfahren. Schweigen nach § 136 StPO darf nicht nachteilig gewertet werden (BGH st. Rspr.). Gestaendnis vs. Bestreiten Strategie. Beweisanträge § 244 StPO. Einlassung schriftlich oder... |
| `strafbefehl-einspruch-aktenanlage` | Gegen: Fristen, Form, Zuständigkeit und Rechtsweg. |
| `strafbefehl-einspruch-beschraenkung` | Beschraenkter Einspruch nach § 410 Abs. 2 StPO auf Rechtsfolgen. Schuldspruch wird rechtskraeftig. Taktisches Kalkuel. Geldstrafe Tagessatz Fahrverbot Einziehung angreifbar. Vollstreckungsverzug § 456a StPO. Abgrenzung unbeschraenkter Ei... |
| `strafbefehl-fristen-einspruch` | Sichert die Einspruchsfrist nach § 410 StPO (2 Wochen ab Zustellung) und erstellt Einspruchsentwuerfe. Berechnung Zustellungsfiktion § 418 ZPO i.V.m. § 37 StPO. Unbeschraenkter oder beschraenkter Einspruch § 410 Abs. 2 StPO. Wiedereinset... |
| `strafbefehl-hauptverhandlung-vorbereitung` | Hauptverhandlung nach § 411 StPO bei Einspruch. Termin Vorbereitungspflichten. Beweisanträge § 244 StPO. Einlassung oder Schweigen. Strafzumessung § 46 StGB. Befangenheitsantrag § 24 StPO. Entbindung von Erscheinungspflicht § 411 Abs. 2... |
| `strafbefehl-inhalt-409-pruefung` | Prüft Strafbefehl auf Pflichtinhalt nach § 409 StPO (7 Mindestangaben) und identifiziert Nichtigkeitsgründe. Tatbeschreibung Bestimmtheitsgrundsatz Art. 103 Abs. 2 GG. Fehlerhafte Rechtsfolgen Geldstrafe Tagessatz Fahrverbot. Strafbefehl... |
| `strafbefehl-pflichtverteidiger` | Pflichtverteidigerbestellung im Strafbefehlsverfahren nach § 140 StPO. Notwendige Verteidigung. Antrag auf Beiordnung § 141 StPO. Bestellung durch Gericht. Auswechslung des Pflichtverteidigers § 143a StPO. Gebühren Nr. 4100 ff. VV-RVG im... |
| `strafbefehl-polizeifilmerei-201-kug` | Strafbefehl wegen Filmens oder Fotografierens von Polizeieinsätzen, Versammlungen oder Kontrollen: prüft § 201 StGB, § 201a StGB, KunstUrhG/KUG §§ 22 bis 23 sowie § 33, Beweissicherung, Tonspur, Veröffentlichung, Beschlagnahme des Smartp... |
| `strafbefehl-quality-gate` | Vor dem Einspruch-Versand vor der Hauptverhandlung oder nach dem Urteil eine Abschlussprüfung durchführen. Prüfraster Fristen Vollmacht Zulässigkeit Einlassung Beweisanträge Strafzumessung Protokoll. Normen § 410 StPO Einspruchsfrist § 4... |
| `strafbefehl-quality-gate-akteneinsicht` | Einstieg in das Strafbefehl-Mandat — Ampel-Schnelldiagnose zeigt kritische Fristen und offene Handlungsfelder auf einen Blick. Zentrales Steuerungsmodul routet auf Subskills: Frist § 410 StPO Akteneinsicht § 147 StPO Inhaltsprüfung § 409... |
| `strafbefehl-rechtsprechungsrecherche` | Rechtsprechung zum Strafbefehlsverfahren recherchieren für Schriftsaetze oder Argumentation in der Hauptverhandlung. Prüfraster BGH OLG-Rspr zu §§ 407-412 StPO Einspruch Wiedereinsetzung Strafzumessung. Normen §§ 407 408 410 412 StPO. Da... |
| `strafbefehl-tagessaetze-geldstrafe` | Berechnung Tagessaetze und Geldstrafe nach §§ 40 41 StGB. Tagessatzanzahl nach Schuld. Tagessatzhoehe nach Nettoeinkommen Dreissigstel. Mindest-Tagessatz 1 EUR. Schaetzungsrecht des Gerichts § 40 Abs. 3 StGB. Einkommensnachweise. Ratenza... |
| `strafbefehl-wiedereinsetzung` | Wiedereinsetzung in den vorigen Stand nach § 44 StPO bei versaeumter Einspruchsfrist. Voraussetzungen: kein Verschulden. Antragsfrist 1 Woche. Glaubhaftmachung § 45 StPO. Zustellungsfiktion entgegnen. Eidesstattliche Versicherung. Wieder... |
| `strafbefehl-zulaessigkeit-407` | Zulässigkeit des Strafbefehls nach § 407 StPO. Nur Vergehen. Sanktionskatalog § 407 Abs. 2 StPO. Sachliche Zuständigkeit Amtsgericht. Keine U-Haft. Keine Beweisprobleme die Hauptverhandlung erfordern. Ablehnung durch Richter § 408 Abs. 3... |
| `strafbefehls-erstpruefung-und-mandatsziel` | Strafbefehls: Erstprüfung, Rollenklärung und Mandatsziel. |
| `tagessaetze-verstaendigung-sonderfall` | Tagessaetze: Schriftsatz-, Brief- und Memo-Bausteine. |
| `unterlagen-luecken` | Lücken- und Beschaffungsliste für Strafbefehl-Verteidigung: trennt fehlende Tatsachen von fehlenden Belegen (Strafbefehl, Ermittlungsakte, Einspruchsschrift), nennt pro Lücke Beweisthema, Beschaffungsweg (Amtsgericht), Frist und Ersatzna... |
| `verstaendigung-sonderfall-und-edge-case` | Verstaendigung: Sonderfall und Edge-Case-Prüfung. |
| `verteidiger-formular-portal-und-einreichung` | Verteidiger: Formular, Portal und Einreichungslogik. |
| `verteidigung-wiedereinsetzung-zeugenstrategie` | Verteidigung: Tatbestandsmerkmale, Beweisfragen und Beleglage. |
| `wiedereinsetzung-zahlen-schwellen-und-berechnung` | Wiedereinsetzung: Zahlen, Schwellenwerte und Berechnung. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen im Strafbefehl Verteidiger. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen im Strafbefehl Verteidiger. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton im Strafbefehl Verteidiger. |
| `zeugen-befragungsstrategie-strafbefehl` | Hauptverhandlung nach Strafbefehl-Einspruch — Zeugen erschuettern oder Entlastungszeugen foerdern. Prüfraster Glaubwürdigkeitsanalyse Aussage-Konstanz Vorhalt fruehere Aussage Fragerecht § 240 StPO. Normen § 68 StPO Zeugenpflichten § 52... |
| `zeugenstrategie-mehrparteien-konflikt-und-interessen` | Zeugenstrategie: Mehrparteienkonflikt und Interessenmatrix. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
