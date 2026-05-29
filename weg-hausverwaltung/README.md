# WEG- und Hausverwaltung

Operatives Plugin für Wohnungseigentümergemeinschaften, Hausverwaltungen, Verwaltungsbeiräte und anwaltliche Begleitung. Der Schwerpunkt liegt nicht auf abstrakter Dogmatik, sondern auf den täglichen Vorgängen: Eigentümerversammlung vorbereiten, Beschlussvorlagen schreiben, Beschlüsse protokollieren, Beschlusssammlung pflegen, Wirtschaftsplan und Jahresabrechnung prüfen, Hausgeld und Sonderumlagen verfolgen, Betriebskosten/Nebenkosten kontrollieren, Handwerker beauftragen, Erhaltungsmaßnahmen steuern und rechtliche Eskalationen rechtzeitig erkennen.

Das Plugin arbeitet paralegal-praktisch: Es erstellt keine "Rechtsberatung aus dem Nichts", sondern strukturiert Akten, formuliert Beschluss- und Anschreibenentwürfe, baut Prüfmatrizen, markiert Fristen, trennt kaufmännische Verwaltung von Rechtsfragen und schlägt bei Risiko den passenden Anwalts- oder Gerichtspfad vor.

## Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| WEG- und Hausverwaltung (`weg-hausverwaltung`, dieses Plugin) | [weg-hausverwaltung.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/weg-hausverwaltung.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

## Zum Ausprobieren: Testakte

| Testakte | Direkt-Download |
| --- | --- |
| **Hohenzollernhof WEG/Hausverwaltung** | [testakte-weg-hausverwaltung-hohenzollernhof.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-weg-hausverwaltung-hohenzollernhof.zip) |

Die Testakte enthält eine fiktive, unordentliche WEG-Verwaltungsakte mit Eigentümerbeschwerden, drei Handwerkerangeboten, fehleranfälliger Jahresabrechnung, Entwurf einer Eigentümerversammlung, Steckersolar-/Wallbox-Anträgen, Sonderumlage und Beiratsnotizen.

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
| `eigentuemerversammlung-vorbereiten` | Versammlung vom Themenstapel bis zur Beschlussreife planen. |
| `einladung-tagesordnung-fristen` | Einladung, Tagesordnung, Ladungsfristen und Vollmachten prüfen. |
| `beschlussvorlagen-erstellen` | Rechtssichere und verständliche Beschlussvorlagen mit Alternativen formulieren. |
| `beschlusssammlung-protokoll` | Protokoll, Beschlusssammlung, Verkündung, Anlagen und Nachversand strukturieren. |
| `beschlussanfechtung-risiko` | Anfechtungs- und Nichtigkeitsrisiken nach §§ 44 und 45 WEG erkennen. |
| `wirtschaftsplan-jahresabrechnung-28-weg` | Wirtschaftsplan, Jahresabrechnung, Vermögensbericht, Nachschüsse und Vorschüsse prüfen. |
| `hausgeld-sonderumlage-liquiditaet` | Hausgeldrückstände, Sonderumlagen, Liquidität, Mahnung und Klagepfad ordnen. |
| `betriebskosten-nebenkostenabrechnung` | Betriebskosten/Nebenkosten nach BetrKV, Mietvertrag und WEG-Abrechnung kontrollieren. |
| `handwerker-beauftragung-vergabe` | Angebote einholen, vergleichen, beauftragen, Nachträge prüfen und Dokumentation sichern. |
| `erhaltung-modernisierung-baumaengel` | Erhaltung, Modernisierung, Mängel, Gewährleistung und Bauüberwachung verwalten. |
| `bauliche-veraenderungen-20-weg` | Bauliche Veränderungen nach §§ 20 und 21 WEG beschlussfähig vorbereiten. |
| `steckersolar-wallbox-barrierefreiheit` | Privilegierte Maßnahmen: Steckersolar, E-Mobilität, Einbruchsschutz, Glasfaser, Barrierefreiheit. |
| `verwalterpflichten-26-27-weg` | Bestellung, Abberufung, Vertretungsmacht, Maßnahmenkatalog, Verwaltervertrag. |
| `eigentuemerkommunikation-beschwerde` | Eigentümerkommunikation, Beschwerden, Eskalationsmails und transparente Antwortbausteine. |
| `stoerung-hausordnung-mieter-eigentuemer` | Lärm, Müll, Feuchtigkeit, Gemeinschaftsflächen, Mieter als Störer, Hausordnung. |
| `beirat-controlling-verwalter` | Verwaltungsbeirat: Rechnungsprüfung, Angebotskontrolle, Protokollcheck, Eskalationsnotiz. |
| `datenschutz-dokumentenfreigabe` | DSGVO, Eigentümerlisten, Belegeinsicht, Schwärzungen, Cloud-Freigaben. |
| `eskalation-anwalt-amtsgericht` | Wann Anwalt, Amtsgericht, Beschlussklage, Hausgeldklage oder einstweiliger Rechtsschutz nötig wird. |

## Typische Workflows

**Eigentümerversammlung:** `mandat-objekt-triage` -> `eigentuemerversammlung-vorbereiten` -> `einladung-tagesordnung-fristen` -> `beschlussvorlagen-erstellen` -> `beschlusssammlung-protokoll` -> `beschlussanfechtung-risiko`.

**Jahresabrechnung:** `wirtschaftsplan-jahresabrechnung-28-weg` -> `beirat-controlling-verwalter` -> `hausgeld-sonderumlage-liquiditaet` -> bei vermieteten Wohnungen zusätzlich `betriebskosten-nebenkostenabrechnung`.

**Handwerkermaßnahme:** `erhaltung-modernisierung-baumaengel` -> `handwerker-beauftragung-vergabe` -> `beschlussvorlagen-erstellen` -> `eigentuemerkommunikation-beschwerde` -> bei Streit `eskalation-anwalt-amtsgericht`.

## Grenzen

Das Plugin ersetzt keine anwaltliche Beratung, keine WEG-Spezialkanzlei, keine Steuerberatung und keine technische Bauleitung. Es hilft, die Verwaltung so zu dokumentieren, dass Anwälte, Beiräte, Verwalter und Eigentümer sauber weiterarbeiten können.
