# WEG- und Hausverwaltung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`weg-hausverwaltung`) | [`weg-hausverwaltung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/weg-hausverwaltung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **WEG Hohenzollernhof — Hausverwaltung unter Druck** (`weg-hausverwaltung-hohenzollernhof`) | [Gesamt-PDF lesen](../testakten/weg-hausverwaltung-hohenzollernhof/gesamt-pdf/weg-hausverwaltung-hohenzollernhof_gesamt.pdf) | [`testakte-weg-hausverwaltung-hohenzollernhof.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-weg-hausverwaltung-hohenzollernhof.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Operatives Plugin für Wohnungseigentümergemeinschaften, Hausverwaltungen, Verwaltungsbeiräte und anwaltliche Begleitung. Der Schwerpunkt liegt nicht auf abstrakter Dogmatik, sondern auf den täglichen Vorgängen: Eigentümerversammlung vorbereiten, Beschlussvorlagen schreiben, Beschlüsse protokollieren, Beschlusssammlung pflegen, Wirtschaftsplan und Jahresabrechnung prüfen, Hausgeld und Sonderumlagen verfolgen, Betriebskosten/Nebenkosten kontrollieren, Handwerker beauftragen, Erhaltungsmaßnahmen steuern, Restaurant- und Hausordnungskonflikte sortieren, E-Mobilität/Steckersolar/PV beschlussreif machen und rechtliche Eskalationen rechtzeitig erkennen.

Das Plugin arbeitet paralegal-praktisch: Es erstellt keine "Rechtsberatung aus dem Nichts", sondern strukturiert Akten, formuliert Beschluss- und Anschreibenentwürfe, baut Prüfmatrizen, markiert Fristen, trennt kaufmännische Verwaltung von Rechtsfragen und schlägt bei Risiko den passenden Anwalts- oder Gerichtspfad vor.

## Installation in Claude Code

1. ZIP herunterladen.
2. Claude Code -> **Customize Plugins** -> **Install from .zip** -> Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code -> Download ZIP" verwenden.

## Quellen- und Rollenregel

- Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbarer Quelle.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- Bei streitigen Beschlüssen, Verjährung, Anfechtung, Schadensersatz, Verwalterhaftung oder gerichtlichen Schritten immer anwaltliche Eskalation markieren.
- Verwaltungspraxis, kaufmännische Kontrolle und juristische Bewertung werden sichtbar getrennt.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Triage, Upload-Erkennung und Workflow-Routing im WEG-/Hausverwaltungsalltag. |
| `rechtsstand-mai-2026-faktenbank` | Quellen-Gate mit WEG/BGB/BetrKV-Ankern und frei verifizierten BGH-Linien. |
| `mandat-objekt-triage` | Objekt, Gemeinschaft, Rollen, Verwaltervertrag, Teilungserklärung, Fristen und Aktenlage erfassen. |
| `grossakte-konfliktlandkarte` | Große unübersichtliche Verwaltungsakten clustern, priorisieren und in passende Spezial-Skills routen. |
| `eigentuemerversammlung-vorbereiten` | Versammlung vom Themenstapel bis zur Beschlussreife planen. |
| `einladung-tagesordnung-fristen` | Einladung, Tagesordnung, Ladungsfristen und Vollmachten prüfen. |
| `beschlussvorlagen-erstellen` | Rechtssichere und verständliche Beschlussvorlagen mit Alternativen formulieren. |
| `protokollwerkstatt-top-marathon` | Lange Eigentümerversammlungen mit vielen TOPs protokollfähig strukturieren. |
| `beschlusssammlung-protokoll` | Protokoll, Beschlusssammlung, Verkündung, Anlagen und Nachversand strukturieren. |
| `beschlussanfechtung-risiko` | Anfechtungs- und Nichtigkeitsrisiken nach §§ 44 und 45 WEG erkennen. |
| `wirtschaftsplan-jahresabrechnung-28-weg` | Wirtschaftsplan, Jahresabrechnung, Vermögensbericht, Nachschüsse und Vorschüsse prüfen. |
| `abrechnung-ist-plan-mieterschnittstelle` | Ist-/Plan-Kosten, Verteilerschlüssel, Betriebskosten und vermietende Eigentümer zusammenführen. |
| `hausgeld-sonderumlage-liquiditaet` | Hausgeldrückstände, Sonderumlagen, Liquidität, Mahnung und Klagepfad ordnen. |
| `betriebskosten-nebenkostenabrechnung` | Betriebskosten/Nebenkosten nach BetrKV, Mietvertrag und WEG-Abrechnung kontrollieren. |
| `handwerker-beauftragung-vergabe` | Angebote einholen, vergleichen, beauftragen, Nachträge prüfen und Dokumentation sichern. |
| `erhaltung-modernisierung-baumaengel` | Erhaltung, Modernisierung, Mängel, Gewährleistung und Bauüberwachung verwalten. |
| `heizung-schaden-versicherung-notmassnahme` | Heizungsstörung, Wasserschaden, Versicherung, Sofortmaßnahme und Beschlussnachlauf ordnen. |
| `bauliche-veraenderungen-20-weg` | Bauliche Veränderungen nach §§ 20 und 21 WEG beschlussfähig vorbereiten. |
| `steckersolar-wallbox-barrierefreiheit` | Privilegierte Maßnahmen: Steckersolar, E-Mobilität, Einbruchsschutz, Glasfaser, Barrierefreiheit. |
| `e-mobilitaet-steckersolar-kellerstrom` | Wallbox, Ladeinfrastruktur, Dach-PV, Steckersolar und riskante Kellerstrom-Provisorien prüfen. |
| `verwalterpflichten-26-27-weg` | Bestellung, Abberufung, Vertretungsmacht, Maßnahmenkatalog, Verwaltervertrag. |
| `eigentuemerkommunikation-beschwerde` | Eigentümerkommunikation, Beschwerden, Eskalationsmails und transparente Antwortbausteine. |
| `stoerung-hausordnung-mieter-eigentuemer` | Lärm, Müll, Feuchtigkeit, Gemeinschaftsflächen, Mieter als Störer, Hausordnung. |
| `gewerbe-restaurant-geruch-laerm-hof` | Restaurant-/Gewerbekonflikte mit Geruch, Lärm, Müll, Lieferverkehr, Hofnutzung und Betreiberrollen. |
| `hausordnung-tauben-fahrrad-kinder-weihnachtsbaum` | Alltagssachen sauber sortieren: Tauben, Fahrraddiebstahl, Kinder, Weihnachtsbaum, Fluchtwege. |
| `beirat-controlling-verwalter` | Verwaltungsbeirat: Rechnungsprüfung, Angebotskontrolle, Protokollcheck, Eskalationsnotiz. |
| `datenschutz-dokumentenfreigabe` | DSGVO, Eigentümerlisten, Belegeinsicht, Schwärzungen, Cloud-Freigaben. |
| `eskalation-anwalt-amtsgericht` | Wann Anwalt, Amtsgericht, Beschlussklage, Hausgeldklage oder einstweiliger Rechtsschutz nötig wird. |

## Typische Workflows

**Eigentümerversammlung:** `grossakte-konfliktlandkarte` -> `eigentuemerversammlung-vorbereiten` -> `einladung-tagesordnung-fristen` -> `beschlussvorlagen-erstellen` -> `protokollwerkstatt-top-marathon` -> `beschlussanfechtung-risiko`.

**Jahresabrechnung:** `wirtschaftsplan-jahresabrechnung-28-weg` -> `abrechnung-ist-plan-mieterschnittstelle` -> `beirat-controlling-verwalter` -> `hausgeld-sonderumlage-liquiditaet` -> bei vermieteten Wohnungen zusätzlich `betriebskosten-nebenkostenabrechnung`.

**Handwerkermaßnahme:** `erhaltung-modernisierung-baumaengel` -> `handwerker-beauftragung-vergabe` -> `beschlussvorlagen-erstellen` -> `eigentuemerkommunikation-beschwerde` -> bei Streit `eskalation-anwalt-amtsgericht`.

**Alltagskonflikt:** `grossakte-konfliktlandkarte` -> `hausordnung-tauben-fahrrad-kinder-weihnachtsbaum` oder `gewerbe-restaurant-geruch-laerm-hof` -> `eigentuemerkommunikation-beschwerde` -> bei hartem Konflikt `eskalation-anwalt-amtsgericht`.

## Grenzen

Das Plugin ersetzt keine anwaltliche Beratung, keine WEG-Spezialkanzlei, keine Steuerberatung und keine technische Bauleitung. Es hilft, die Verwaltung so zu dokumentieren, dass Anwälte, Beiräte, Verwalter und Eigentümer sauber weiterarbeiten können.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 67 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abrechnung-ist-plan-mieterschnittstelle` | Jahresabrechnung, Wirtschaftsplan und Mieterschnittstelle: trennt § 28 WEG-Nachschüsse/Vorschussanpassung von mietrechtlicher Betriebskostenabrechnung, prüft Ist-/Plan-Abweichungen, Umlagefähigkeit, Gewerbeanteile, Belege, Heizkosten/CO2... |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im WEG- und Hausverwaltungs-Plugin (Stand 05/2026). Ordnet Uploads, erkennt Fristen und Risiken, fragt Rolle und Objekt ab und schlägt passende Skills für Beschlüsse, Eigentümerversammlung, Ab... |
| `bad-umbau-bodengleiche-dusche-sondereigentum-gemeinschaft` | Bodengleiche Dusche, Haltegriffe und unterfahrbares Waschbecken im Sondereigentum (Stand 06/2026): SE/GE-Abgrenzung, Beschluss nach § 20 Abs. 2 Nr. 2 WEG, DIN 18534 Abdichtung, Pflegekasse § 40 SGB XI bis 4180 Euro. BGH V ZR 57/12. |
| `barrierefreie-einladung-protokoll-versammlung` | Versammlungsdokumente barrierefrei gestalten (Stand 06/2026): PDF/UA (ISO 14289), Word-Formatvorlagen, Leichte Sprache nach DIN SPEC 33429, Grossdruck, TTS-Kompatibilitaet. Praktischer Umgang mit Casavi/Vermieter-Cloud-PDFs. |
| `bauliche-veraenderung-aufzug-treppenlift-20-abs-2-weg` | Aufzug-Nachrüstung und Treppenlift als privilegierte bauliche Veränderung nach § 20 Abs. 2 Nr. 2 WEG (Stand 06/2026): Anspruch ohne Ermessen, DIN 18040-2, Kostentragung § 21 WEG, KfW 159 bis 50000 Euro, BGH V ZR 244/22. |
| `bauliche-veraenderungen-20-weg` | Prüft bauliche Veränderungen nach §§ 20 und 21 WEG (Stand 05/2026): Anspruch, Gestattung, Grenzen, Kostenfolge, Gebrauch, Auflagen, Rückbau, Beschlussvorschlag und Anfechtungsrisiko, einschließlich der BGH-Linie 2024-2025 zu Klimasplitge... |
| `beirat-controlling-verwalter` | Unterstützt Verwaltungsbeiräte bei Rechnungsprüfung, Angebotskontrolle, Beschlussvorbereitung, Protokollcheck, Verwalterkommunikation und Eskalationsnotizen (Stand 05/2026); berücksichtigt BGH V ZR 34/24 (Schadensersatzweg über GdWE) und... |
| `beschlussanfechtung-risiko` | Prüft Beschlüsse auf Anfechtungs- und Nichtigkeitsrisiken nach §§ 44 und 45 WEG (Stand 05/2026): Frist, Beschlusskompetenz, Einladung, Tagesordnung, Mehrheit, Kostenfolge, Bestimmtheit, ordnungsmäßige Verwaltung sowie BGH-Linie zu Schlüs... |
| `beschlusssammlung-protokoll` | Erstellt und prüft Protokoll, Beschlussverkündung, Beschlusssammlung (§ 24 Abs. 7 WEG), Anlagenverweise, Abstimmungsergebnis, Nachversand und Dokumentationsstand (Stand 05/2026). Sorgt dafür, dass Auslegungsfragen späterer Beschlussklage... |
| `beschlussvorlagen-erstellen` | Erstellt WEG-Beschlussvorlagen mit Beschlusskompetenz, Kostenfolge, Ausführungsdetails, Alternativen, Begründung, Anlagenverweis und Anfechtungsrisiko (Stand 05/2026). Liefert Mustertexte für Abrechnungsspitzen, Sonderumlage, Schlüsselän... |
| `betriebskosten-nebenkostenabrechnung` | WEG- und Hausverwaltungs-Schnittstelle Betriebskosten: erstellt und kontrolliert mietrechtliche Betriebskostenabrechnungen aus WEG-Jahresabrechnung, Wirtschaftsplan, Heizkostenabrechnung und Belegen; mit BetrKV, HeizkostenV, CO2KostAufG,... |
| `bfsg-hausverwalter-website-portal-2025` | Barrierefreiheitsstärkungsgesetz (BFSG) ab 28.06.2025 fuer Verwalter-Websites und Eigentuemer-Portale (Stand 06/2026): Anwendungsbereich, Kleinstunternehmen-Ausnahme, WCAG 2.1 AA, Bussgeld bis 100000 Euro, Pflicht-Erklaerung. |
| `datenschutz-betroffenenrechte-auskunft-loeschung-weg` | Betroffenenrechte nach DSGVO Art. 15-21 im WEG-Alltag (Stand 06/2026): Auskunft, Loeschung, Einschraenkung, Widerspruch. Fristen, Abgrenzung Anspruchsberechtigte, zulaessige Verweigerungsgruende, EuGH C-307/22. |
| `datenschutz-datenpanne-meldung-72h` | Datenschutzverletzungen nach Art. 33/34 DSGVO melden (Stand 06/2026): 72-Stunden-Frist, Risikobewertung, Meldung an Aufsichtsbehoerde, Betroffenenbenachrichtigung. Typische Pannen in der Hausverwaltung mit Sofortmassnahmen. |
| `datenschutz-dokumentenfreigabe` | Prüft Datenschutz und Dokumentenfreigaben in der Hausverwaltung (Stand 05/2026): Eigentümerlisten, Belegeinsicht, Handwerkerdaten, Mieterbeschwerden, Cloud-Ordner, Schwärzungen und Versandkreis. Schnittstelle zum Datenschutzrecht-Plugin... |
| `datenschutz-vvt-tom-avv-hausverwaltung` | VVT nach Art. 30 DSGVO, TOM nach Art. 32 und AVV nach Art. 28 DSGVO fuer die typische Hausverwaltung (Stand 06/2026): Verarbeitungsverzeichnis-Muster, TOM-Mindeststandards, AVV-Pflichten gegenueber Buchhaltungssoftware und Cloud-Diensten. |
| `digitale-versammlung-screenreader-untertitel` | Hybride und rein digitale Eigentuemerversammlung nach § 23 Abs. 1 WEG barrierefrei durchfuehren (Stand 06/2026): Live-Untertitel Zoom/Teams, Screenreader-kompatible Abstimmung, Tonqualitaet, Vollmacht in Textform. BGH V ZR 33/24. |
| `e-mobilitaet-steckersolar-kellerstrom` | Prüft E-Mobilität, Wallboxen, Ladeinfrastruktur, Steckersolar, Dach-PV und unzulässige Kellerstrom-Lösungen in WEG-Anlagen. Ordnet § 20 WEG, Brandschutz, Messkonzept, Kosten, Netzanschluss und Beschlussvarianten. Output: Beschluss- und R... |
| `eigentuemerkommunikation-beschwerde` | Formuliert klare, deeskalierende und dokumentationssichere Kommunikation an Eigentümer, Beirat, Mieter und Handwerker bei Beschwerden, Rückfragen, Fristen und Beschlussumsetzung (Stand 05/2026). Berücksichtigt aktuelle BGH-Linien (Abrech... |
| `eigentuemerversammlung-vorbereiten` | Plant eine Eigentümerversammlung (Stand 05/2026) von Themenstapel, Beschlussbedarf, Unterlagen, Beiratsabstimmung, Einladungszeitplan, Raum/virtueller Teilnahme bis zur Nachbereitung. Berücksichtigt § 23 Abs. 1a WEG, BGH-Linie zu Vorbefa... |
| `einladung-tagesordnung-fristen` | Prüft und erstellt Einladungen zur Eigentümerversammlung mit Tagesordnung, Ladungsfrist, Zugang, Vollmacht, Beschlussgegenständen, Anlagen und Fristenkontrolle (Stand 05/2026). Berücksichtigt § 24 Abs. 4 WEG (Ladungsfrist 3 Wochen), § 23... |
| `erhaltung-modernisierung-baumaengel` | Steuert Erhaltungsmaßnahmen, Modernisierung, Baumängel, Gewährleistungsfristen, Gutachten, Sofortmaßnahmen, Beschlussbedarf und Kommunikation mit Eigentümern (Stand 05/2026). Berücksichtigt GEG § 71 (65 % erneuerbare Energien beim Heizun... |
| `eskalation-anwalt-amtsgericht` | Erkennt, wann ein WEG-/Hausverwaltungsvorgang nicht mehr nur Verwaltung ist (Stand 05/2026): Anwalt, Beschlussklage, Hausgeldklage, einstweiliger Rechtsschutz, Beweissicherung, Verwalterhaftung über GdWE oder Vergleich; berücksichtigt Fr... |
| `gewerbe-restaurant-geruch-laerm-hof` | Bearbeitet Restaurant- und Gewerbekonflikte in WEG-Anlagen: Geruch, Lüftung, Lärm, Müll, Lieferverkehr, Fettabscheider, Sondernutzung, Brandschutz und Mieter-/Eigentümerrollen. Output: Eskalations- und Beschlussplan. |
| `grossakte-konfliktlandkarte` | Ordnet unübersichtliche WEG- und Hausverwaltungsakten mit vielen Konflikten: Heizung, Dach, Gewerbe, Geruch, Tauben, Fahrrad, Kinder, Wallbox, Steckersolar, Nebenkosten, Protokolle und Beschlüsse. Output: Konfliktlandkarte, Prioritätenpl... |
| `handwerker-beauftragung-vergabe` | Begleitet Handwerkerbeauftragung in der WEG (Stand 05/2026): Leistungsbeschreibung, Vergleichsangebote, Beschlussbedarf, Budget, Nachträge, Abnahme, Rechnungskontrolle, Gewährleistung, Dokumentation; berücksichtigt § 27 WEG (Verwalterkom... |
| `hausgeld-sonderumlage-liquiditaet` | Prüft Hausgeld, Vorschüsse, Rückstände, Sonderumlagen, Liquidität, Mahnungen, Ratenzahlung, Beschlussgrundlage und Klagepfad der GdWE (Stand 05/2026). Berücksichtigt BGH V ZR 190/24 zum Zurückbehaltungsrecht und V ZR 139/23 zur Verteilun... |
| `hausordnung-tauben-fahrrad-kinder-weihnachtsbaum` | Ordnet Alltagskonflikte in WEG-Anlagen: Tauben auf Balkonen, Fahrradkeller, Diebstahl, Kinderlärm, Spielhof, Weihnachtsbaum, Brandschutz, Hausordnung und Kommunikation. Output: Maßnahmenmatrix und deeskalierende Schreiben. |
| `heizung-schaden-versicherung-notmassnahme` | Bearbeitet Heizungsstörungen, Wasserschäden, Feuchtigkeit, Frost, Versicherung und Notmaßnahmen in WEG-Anlagen. Prüft Zuständigkeit, Sofortmaßnahmen, Beweise, Handwerker, Beschlussbedarf, Umlage und Mieterkommunikation. Output: Maßnahmen... |
| `kfw-foerderung-pflegekasse-bafa-barriere-koordination` | Foerderungs-Koordination fuer Barrierefreiheits-Massnahmen (Stand 06/2026): KfW 159 bis 50000 Euro, Pflegekasse § 40 SGB XI bis 4180 Euro, BAFA, Steuern § 33b EStG. Antrags-Reihenfolge und Kumulationsregeln. |
| `mandat-objekt-triage` | Erfasst eine WEG-/Hausverwaltungsakte (Stand 05/2026): Objekt, Rollen, Teilungserklärung, Gemeinschaftsordnung, Verwaltervertrag, Beschlusssammlung, Abrechnungen, Vermögensbericht, Angebote, Fristen, Risiken und nächsten Workflow. Identi... |
| `marketing-akquise-neue-weg-mandate` | Akquise neuer WEG-Verwaltungsmandate (Stand 06/2026): Pitch-Bestandteile, Honorarmatrix, Verwaltervertrag nach § 26 WEG, Uebernahme-Uebergabe-Checkliste und Wettbewerbsgrenzen. BGH V ZR 251/21 zur Sondervergütung. |
| `marketing-newsletter-eigentuemerkommunikation` | Eigentuemerinfo vs. E-Mail-Werbung klar trennen (Stand 06/2026): § 7 UWG Double-Opt-In, Einwilligungspflicht, Versicherungswerbung nach § 34d GewO, DSGVO Art. 6. BGH VI ZR 225/17 zu unerlaubter E-Mail-Werbung. |
| `marketing-website-impressum-tmg-und-bewertungen` | Verwalter-Website rechtssicher gestalten (Stand 06/2026): Impressum nach § 5 DDG, Datenschutz nach TDDDG, § 34c GewO, Umgang mit falschen und negativen Bewertungen auf Google und Co. BGH VI ZR 1244/20. |
| `protokollwerkstatt-top-marathon` | Erstellt und prüft Protokolle für lange Eigentümerversammlungen mit vielen Tagesordnungspunkten. Trennt Aussprache, Antrag, Beschlusswortlaut, Abstimmung, Verkündung, Anlagen und Nacharbeit. Output: protokollfähige TOP-Struktur. |
| `rampe-handlauf-tuerverbreiterung-gemeinschaftsbereich` | Rampe, beidseitige Handläufe, Tuerverbreiterung und Beleuchtungsoptimierung im Gemeinschaftseigentum (Stand 06/2026): DIN 18040 Masszahlen, Kostentragung § 21 WEG, Genehmigungspflicht Landesbauordnung, Beschlussvorlagen. |
| `rechtsstand-mai-2026-faktenbank` | Quellen-Gate für WEG und Hausverwaltung mit Stand 05/2026. Enthält Normanker zu WEG, BGB, BetrKV, HeizkostenV, GEG und CO2KostAufG sowie frei verifizierte BGH-Rechtsprechung des V. Zivilsenats 2024 bis 2026 zu Kostenverteilung, baulichen... |
| `spezial-bauliche-formular-portal-und-einreichung` | Bauliche: Formular, Portal und Einreichungslogik im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-beschluesse-dokumentenmatrix-und-lueckenliste` | Beschluesse: Dokumentenmatrix, Lückenliste und Nachforderung im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-beschlusssammlung-schriftsatz-brief-und-memo-bausteine` | Beschlusssammlung: Schriftsatz-, Brief- und Memo-Bausteine im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-betriebskosten-mehrparteien-konflikt-und-interessen` | Betriebskosten: Mehrparteienkonflikt und Interessenmatrix im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-eigentuemerversammlung-risikoampel-und-gegenargumente` | Eigentuemerversammlung: Risikoampel, Gegenargumente und Verteidigungslinien im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-handwerker-internationaler-bezug-und-schnittstellen` | Handwerker: Internationaler Bezug und Schnittstellen im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-hausgeld-zahlen-schwellen-und-berechnung` | Hausgeld: Zahlen, Schwellenwerte und Berechnung im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-hausverwaltungs-fristen-form-und-zustaendigkeit` | Hausverwaltungs: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-jahresabrechnung-livequellen-und-rechtsprechungscheck` | Jahresabrechnung: Livequellen- und Rechtsprechungscheck im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-operatives-erstpruefung-und-mandatsziel` | Operatives: Erstprüfung, Rollenklärung und Mandatsziel im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-protokoll-behoerden-gericht-und-registerweg` | Protokoll: Behörden-, Gerichts- oder Registerweg im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-sonderumlage-compliance-dokumentation-und-akte` | Sonderumlage: Compliance-Dokumentation und Aktenvermerk im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-weg-tatbestand-beweis-und-belege` | WEG: Tatbestandsmerkmale, Beweisfragen und Beleglage im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-wirtschaftsplan-verhandlung-vergleich-und-eskalation` | Wirtschaftsplan: Verhandlung, Vergleich und Eskalation im Plugin weg hausverwaltung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `steckersolar-wallbox-barrierefreiheit` | Spezialworkflow für privilegierte Maßnahmen nach § 20 Abs. 2 WEG (Stand 05/2026): Steckersolargerät, Wallbox/E-Mobilität, barrierefreier Umbau, Einbruchsschutz, Glasfaseranschluss. Prüft Anspruch, technische Unterlagen, Auflagen, Beschlu... |
| `stoerung-hausordnung-mieter-eigentuemer` | Bearbeitet Störungen in der WEG (Stand 05/2026): Lärm, Müll, Feuchtigkeit, Geruch, Kamera, Gemeinschaftsflächen, Mieter als Störer, vermietender Eigentümer, Hausordnung, Abmahnung, Beweissicherung. Berücksichtigt BGH V ZR 1/24 (mittelbar... |
| `top-generator-emotion-zu-beschluss` | Verwandelt ungeordnete Beschwerden, WhatsApp-Nachrichten, Eigentuemermails und Verwaltervermerke in sachliche Tagesordnungspunkte, Beschlussvorschlaege, Informations-TOPs und Protokollbausteine. |
| `verwalterpflichten-26-27-weg` | Prüft Verwalterbestellung, Abberufung, Verwaltervertrag, Aufgaben und Befugnisse nach §§ 26 und 27 WEG (Stand 05/2026), laufende Verwaltung, Eilmaßnahmen, Vertretung der GdWE und Haftung; berücksichtigt BGH V ZR 34/24 (keine Schutzwirkun... |
| `wegh-bauliche-veraenderung-beschluss-spezial` | Spezialfall bauliche Veraenderung Beschluss WEG nach Reform: privilegierte Massnahmen, Kostenverteilung. Pruefraster fuer Verwalter und Eigentuemergemeinschaft. |
| `wegh-eigentuemerversammlung-bauleiter` | Bauleiter Eigentuemerversammlung WEG: Einberufung, Tagesordnung, Beschlusskompetenz, Protokoll. Pruefraster fuer Verwalter. |
| `wegh-verwalterhaftung-spezial` | Spezialfall Verwalterhaftung WEG §§ 26 ff. WEG nach Reform 2020: Innen- und Aussenhaftung, D-and-O fuer Verwalter, Haftung fuer Beschlussumsetzung. Pruefraster fuer Verwalter. |
| `wegh-wirtschaftsplan-jahresabrechnung-leitfaden` | WEG-Leitfaden Wirtschaftsplan und Jahresabrechnung nach § 28 WEG: Vorschüsse, Nachschüsse, Abrechnungsspitzen, Einzelabrechnungen, Vermögensbericht, Beschlussformulierung, Anfechtungsrisiko und Mieterschnittstelle. |
| `wirtschaftsplan-jahresabrechnung-28-weg` | Prüft Wirtschaftsplan, Jahresabrechnung, Vermögensbericht, Nachschüsse, Vorschussanpassungen, Rücklagen, Verteilerschlüssel, Beleglage und Beschlussformulierung nach § 28 WEG (Stand 05/2026). Berücksichtigt BGH V ZR 102/23 (Auslegung des... |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin weg-hausverwaltung: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin weg-hausverwaltung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin weg-hausverwaltung: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin weg-hausverwaltung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin weg-hausverwaltung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin weg-hausverwaltung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin weg-hausverwaltung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
