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

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im WEG- und Hausverwaltungs-Plugin (Stand 05/2026). Ordnet Uploads, erkennt Fristen und Risiken, fragt Rolle und Objekt ab und schlägt passende Skills für Beschlüsse, Eigentümerversammlung, Ab... |
| `kompendium-01-workflow-chronologie-bis-einladung-tagesordnu` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel, einladung-tagesordnung-fristen) und bewahrt deren Workflows, Normanker, Prüf... |
| `kompendium-02-spezial-hausverwaltu-bis-wegh-verwalterhaftun` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (spezial-hausverwaltungs-fristen-form-und-zustaendigkeit, heizung-schaden-versicherung-notmassnahme, wegh-verwalterhaftung-spezial) und bewahrt deren... |
| `kompendium-03-erhaltung-modernisie-bis-abrechnung-ist-plan` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (erhaltung-modernisierung-baumaengel, kfw-foerderung-pflegekasse-bafa-barriere-koordination, abrechnung-ist-plan-mieterschnittstelle) und bewahrt der... |
| `kompendium-04-bad-umbau-bodengleic-bis-bauliche-veraenderun` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (bad-umbau-bodengleiche-dusche-sondereigentum-gemeinschaft, barrierefreie-einladung-protokoll-versammlung, bauliche-veraenderung-aufzug-treppenlift-2... |
| `kompendium-05-bauliche-veraenderun-bis-beschlussanfechtung` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (bauliche-veraenderungen-20-weg, beirat-controlling-verwalter, beschlussanfechtung-risiko) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `kompendium-06-beschlusssammlung-pr-bis-betriebskosten-neben` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (beschlusssammlung-protokoll, beschlussvorlagen-erstellen, betriebskosten-nebenkostenabrechnung) und bewahrt deren Workflows, Normanker, Prüfprogramm... |
| `kompendium-07-bfsg-hausverwalter-w-bis-datenschutz-datenpan` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (bfsg-hausverwalter-website-portal-2025, datenschutz-betroffenenrechte-auskunft-loeschung-weg, datenschutz-datenpanne-meldung-72h) und bewahrt deren... |
| `kompendium-08-datenschutz-dokument-bis-digitale-versammlung` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (datenschutz-dokumentenfreigabe, datenschutz-vvt-tom-avv-hausverwaltung, digitale-versammlung-screenreader-untertitel) und bewahrt deren Workflows, N... |
| `kompendium-09-e-mobilitaet-stecker-bis-eigentuemerversammlu` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (e-mobilitaet-steckersolar-kellerstrom, eigentuemerkommunikation-beschwerde, eigentuemerversammlung-vorbereiten) und bewahrt deren Workflows, Normank... |
| `kompendium-10-eskalation-anwalt-am-bis-grossakte-konfliktla` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (eskalation-anwalt-amtsgericht, gewerbe-restaurant-geruch-laerm-hof, grossakte-konfliktlandkarte) und bewahrt deren Workflows, Normanker, Prüfprogram... |
| `kompendium-11-handwerker-beauftrag-bis-hausordnung-tauben-f` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (handwerker-beauftragung-vergabe, hausgeld-sonderumlage-liquiditaet, hausordnung-tauben-fahrrad-kinder-weihnachtsbaum) und bewahrt deren Workflows, N... |
| `kompendium-12-mandat-objekt-triage-bis-marketing-newsletter` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (mandat-objekt-triage, marketing-akquise-neue-weg-mandate, marketing-newsletter-eigentuemerkommunikation) und bewahrt deren Workflows, Normanker, Prü... |
| `kompendium-13-marketing-website-im-bis-rampe-handlauf-tuerv` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (marketing-website-impressum-tmg-und-bewertungen, protokollwerkstatt-top-marathon, rampe-handlauf-tuerverbreiterung-gemeinschaftsbereich) und bewahrt... |
| `kompendium-14-rechtsstand-mai-2026-bis-spezial-beschluesse` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (rechtsstand-mai-2026-faktenbank, spezial-bauliche-formular-portal-und-einreichung, spezial-beschluesse-dokumentenmatrix-und-lueckenliste) und bewahr... |
| `kompendium-15-spezial-beschlusssam-bis-spezial-eigentuemerv` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-beschlusssammlung-schriftsatz-brief-und-memo-bausteine, spezial-betriebskosten-mehrparteien-konflikt-und-interessen, spezial-eigentuemervers... |
| `kompendium-16-spezial-handwerker-i-bis-spezial-operatives-e` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (spezial-handwerker-internationaler-bezug-und-schnittstellen, spezial-hausgeld-zahlen-schwellen-und-berechnung, spezial-operatives-erstpruefung-und-m... |
| `kompendium-17-spezial-protokoll-be-bis-spezial-weg-tatbesta` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (spezial-protokoll-behoerden-gericht-und-registerweg, spezial-sonderumlage-compliance-dokumentation-und-akte, spezial-weg-tatbestand-beweis-und-beleg... |
| `kompendium-18-spezial-wirtschaftsp-bis-stoerung-hausordnung` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (spezial-wirtschaftsplan-verhandlung-vergleich-und-eskalation, steckersolar-wallbox-barrierefreiheit, stoerung-hausordnung-mieter-eigentuemer) und be... |
| `kompendium-19-top-generator-emotio-bis-wegh-bauliche-veraen` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 19; bündelt 3 frühere Spezialskills (top-generator-emotion-zu-beschluss, verwalterpflichten-26-27-weg, wegh-bauliche-veraenderung-beschluss-spezial) und bewahrt deren Workflows, Normank... |
| `kompendium-20-wegh-eigentuemervers-bis-wirtschaftsplan-jahr` | weg-hausverwaltung: Konsolidiertes Skill-Kompendium 20; bündelt 3 frühere Spezialskills (wegh-eigentuemerversammlung-bauleiter, wegh-wirtschaftsplan-jahresabrechnung-leitfaden, wirtschaftsplan-jahresabrechnung-28-weg) und bewahrt deren W... |
| `spezial-jahresabrechnung-livequellen-und-rechtsprechungscheck` | Jahresabrechnung: Livequellen- und Rechtsprechungscheck im WEG- und Hausverwaltungsrecht: fachlich vertiefter Spezialskill mit Normenradar (WEG/BGB/BetrKV), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbr... |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin weg-hausverwaltung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin weg-hausverwaltung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin weg-hausverwaltung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin weg-hausverwaltung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin weg-hausverwaltung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
