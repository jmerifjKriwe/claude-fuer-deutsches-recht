# Fachanwalt Strafrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`fachanwalt-strafrecht`) | [`fachanwalt-strafrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/fachanwalt-strafrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BtM-Akte** (`betaeubungsmittelrecht-apotheke-substitution-festival`) | [Gesamt-PDF lesen](../testakten/betaeubungsmittelrecht-apotheke-substitution-festival/gesamt-pdf/betaeubungsmittelrecht-apotheke-substitution-festival_gesamt.pdf) | [`testakte-betaeubungsmittelrecht-apotheke-substitution-festival.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-betaeubungsmittelrecht-apotheke-substitution-festival.zip) |
| **Grossbankrott und Zeugenstreit — Mehrere Deliktszweige, Pellbach Logistik & Spedition GmbH, LG Koeln** (`grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln`) | [Gesamt-PDF lesen](../testakten/grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln/gesamt-pdf/grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln_gesamt.pdf) | [`testakte-grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln.zip) |
| **Wirtschaftsstrafsache Bankert — U-Haft, Betrug, Steuerhinterziehung, LG Frankfurt** (`wirtschaftsstrafsache-uhaft-bankert-frankfurt`) | [Gesamt-PDF lesen](../testakten/wirtschaftsstrafsache-uhaft-bankert-frankfurt/gesamt-pdf/wirtschaftsstrafsache-uhaft-bankert-frankfurt_gesamt.pdf) | [`testakte-wirtschaftsstrafsache-uhaft-bankert-frankfurt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-wirtschaftsstrafsache-uhaft-bankert-frankfurt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

## Was dieses Plugin im Strafprozess leistet

Dieses Plugin ist als Arbeitscockpit für Strafverteidigung gedacht: nicht nur für die große Strategie, sondern für die täglichen Schritte einer laufenden Strafakte. Es ordnet Eingänge, markiert Fristen, baut Aktenlog und Wiedervorlagen, steuert Akteneinsicht, U-Haft, Pflichtverteidigung, Hauptverhandlung, Antragslog, Mandanteninstruktionen, Rechtsmittel und Vollstreckungsnachlauf.

Der Kaltstart soll sofort praktisch werden: Was ist heute gefährlich, welche Frist läuft, welcher Schriftsatz oder Anruf muss raus, welche Aktenbestandteile fehlen, was darf der Mandant keinesfalls ohne Rücksprache tun? Danach schlägt das Plugin die passenden Strafprozess-Skills aus diesem Plugin vor und hält das Ergebnis als Checkliste, Matrix, Memo, Mandantenbrief oder Schriftsatzbaustein fest.

Neu aufgenommen ist ein vertiefter Prüfpfad für digitale Ermittlungsmaßnahmen: biometrischer Internetabgleich, KI-gestützte Trefferlisten, verfahrensübergreifende Analyseplattformen, Akteneinsicht in technische Protokolle, Löschung, Benachrichtigung, KI-VO-Konformität und Verwertungsangriffe. Der Skill behandelt solche Maßnahmen ausdrücklich als rechtsstandsabhängig: Entwurf, Inkrafttreten und aktueller Wortlaut sind vor jeder tragenden Aussage live zu prüfen.

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `strafprozess-cockpit-taegliche-kanzleifuehrung` | Laufendes Verteidigungs-Cockpit mit Verfahrensstand, Fristen, Haftlage, Akteneinsicht, offenen Anträgen, Terminen und nächstem Schritt. |
| `strafprozess-aktenlog-fristen-und-wiedervorlagen` | Macht aus beA-/EGVP-Eingängen, Beschlüssen, Ladungen, Strafbefehlen, Urteilen und Nachlieferungen ein belastbares Fristen- und Aufgabenlog. |
| `strafprozess-haft-und-besuchsmanagement` | Organisiert U-Haft, Haftprüfung, Haftbeschwerde, Haftverschonung, Akteneinsicht, Besuch, Telefon, Familie, Arbeitgeber und Beschleunigungskontrolle. |
| `strafprozess-hv-tagesmappe-und-sitzungsplan` | Baut für jeden Sitzungstag eine Hauptverhandlungs-Tagesmappe mit Zeugenprogramm, Fragelisten, Einlassungsfenster, Antragsentwürfen und Nachbereitung. |
| `strafprozess-sitzungsprotokoll-und-revisionssicherung` | Sichert Protokollierung, Anträge, Belehrungen, Verständigung, letztes Wort und mögliche Revisionsrügen während und nach der Hauptverhandlung. |
| `fachanwalt-strafrecht-orientierung` | Orientierung im Strafrecht — FAO-Voraussetzungen Normen typische Mandate Notfristen Quellenprüfung. Plugin für schnelle Verortung. Strafverteidigung im Ermittlungsverfahren (Akteneinsicht § 147 StPO) H… |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-strafprozess-aktenlo` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 01; bündelt 10 frühere Spezialskills (allgemein, strafr-haftpruefung-haftbeschwerde-workflow, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel, workflow-mandant... |
| `kompendium-02-strafprozess-ermittl-bis-strafrecht-spezial-s` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 02; bündelt 10 frühere Spezialskills (strafprozess-ermittlungsverfahren-sofortmassnahmen, strafprozess-rechtsmittel-und-notfristencockpit, strafrecht-spezial-btmg-strafverfahren-prax... |
| `kompendium-03-strafrecht-spezial-s-bis-fachanwalt-strafrech` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 03; bündelt 10 frühere Spezialskills (strafrecht-spezial-steuerstrafrecht-371-ao-selbstanzeige, akteneinsicht-strafrecht-auswerten, erstgespraech-mandatsannahme, fachanwalt-strafrech... |
| `kompendium-04-fachanwalt-strafrech-bis-spezial-aktenaufbere` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 04; bündelt 10 frühere Spezialskills (fachanwalt-strafrecht-orientierung, fachanwalt-strafrecht-untersuchungshaft-haftpruefung, fachanwalt-strafrecht-verstaendigung-257c-toa-46a, fac... |
| `kompendium-05-spezial-ergaenzt-man-bis-spezial-stgb-risikoa` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 05; bündelt 10 frühere Spezialskills (spezial-ergaenzt-mandantenkommunikation-entscheidungsvorlage, spezial-fachanwalt-erstpruefung-und-mandatsziel, spezial-insolvenzantrag-red-team-... |
| `kompendium-06-spezial-stpo-dokumen-bis-strafprozess-hv-tage` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 06; bündelt 10 frühere Spezialskills (spezial-stpo-dokumentenmatrix-und-lueckenliste, spezial-strafrecht-tatbestand-beweis-und-belege, spezial-strafverteidigung-schriftsatz-brief-und... |
| `kompendium-07-strafprozess-mandant-bis-strafr-dysfunk-conte` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 07; bündelt 10 frühere Spezialskills (strafprozess-mandantenkommunikation-und-instruktionen, strafprozess-pflichtverteidigung-beiordnung-und-wechsel, strafprozess-sitzungsprotokoll-u... |
| `kompendium-08-strafr-dysfunk-darle-bis-strafr-dysfunk-senat` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 08; bündelt 10 frühere Spezialskills (strafr-dysfunk-darlegungslast-umkehren, strafr-dysfunk-empirie-nutzen, strafr-dysfunk-erklaerungsrecht-257-stpo, strafr-dysfunk-hinweis-auf-heil... |
| `kompendium-09-strafr-dysfunk-sitzu-bis-strafrecht-spezial-1` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 09; bündelt 10 frühere Spezialskills (strafr-dysfunk-sitzungspolizei-ordnungsmittel, strafr-dysfunk-verschleppungsabsicht-abgrenzen, strafr-dysfunk-vorwurf-einordnen, strafr-dysfunk-... |
| `kompendium-10-strafrecht-spezial-1-bis-strafrecht-spezial-a` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 10; bündelt 10 frühere Spezialskills (strafrecht-spezial-188-stgb-easy-verteidigung, strafrecht-spezial-188-stgb-social-media-beweise, strafrecht-spezial-amtsdelikte-340-stgb-koerper... |
| `kompendium-11-strafrecht-spezial-a-bis-strafrecht-spezial-a` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 11; bündelt 10 frühere Spezialskills (strafrecht-spezial-aussagepsy-suggestion-falscherinnerung, strafrecht-spezial-aussagepsy-tuechtigkeit-bereitschaft, strafrecht-spezial-aussageps... |
| `kompendium-12-strafrecht-spezial-a-bis-strafrecht-spezial-b` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 12; bündelt 10 frühere Spezialskills (strafrecht-spezial-aussagepsychologie-staatsanwaltschaft-replik, strafrecht-spezial-aussagepsychologie-vernehmungslehre-praxis, strafrecht-spezi... |
| `kompendium-13-strafrecht-spezial-b-bis-strafrecht-spezial-c` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 13; bündelt 10 frühere Spezialskills (strafrecht-spezial-betrug-263-stgb-grundtatbestand, strafrecht-spezial-btmg-29-grundtatbestand, strafrecht-spezial-btmg-29a-nicht-geringe-menge,... |
| `kompendium-14-strafrecht-spezial-c-bis-strafrecht-spezial-g` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 14; bündelt 10 frühere Spezialskills (strafrecht-spezial-computerbetrug-263a-stgb, strafrecht-spezial-design-strafrecht-51-designg, strafrecht-spezial-erpresserischer-menschenraub-23... |
| `kompendium-15-strafrecht-spezial-g-bis-strafrecht-spezial-k` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 15; bündelt 10 frühere Spezialskills (strafrecht-spezial-gmbh-verletzung-anzeigepflicht-84-gmbhg, strafrecht-spezial-insiderhandel-119-wphg, strafrecht-spezial-insolvenzverschleppung... |
| `kompendium-16-strafrecht-spezial-k-bis-strafrecht-spezial-m` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 16; bündelt 10 frühere Spezialskills (strafrecht-spezial-koerperverletzung-223-stgb-grund, strafrecht-spezial-koerperverletzung-mit-todesfolge-227-stgb, strafrecht-spezial-konkursrec... |
| `kompendium-17-strafrecht-spezial-m-bis-strafrecht-spezial-r` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 17; bündelt 10 frühere Spezialskills (strafrecht-spezial-markenrecht-143a-markeng-bandenmaessig, strafrecht-spezial-marktmanipulation-120-wphg, strafrecht-spezial-mietwucher-5-wistg,... |
| `kompendium-18-strafrecht-spezial-r-bis-strafrecht-spezial-s` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 18; bündelt 10 frühere Spezialskills (strafrecht-spezial-raub-249-stgb, strafrecht-spezial-raub-mit-todesfolge-251-stgb, strafrecht-spezial-rechtsbeugung-339-stgb, strafrecht-spezial... |
| `kompendium-19-strafrecht-spezial-s-bis-strafrecht-spezial-u` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 19; bündelt 10 frühere Spezialskills (strafrecht-spezial-subventionsbetrug-264-stgb, strafrecht-spezial-toetung-auf-verlangen-216-stgb, strafrecht-spezial-totschlag-212-stgb, strafre... |
| `kompendium-20-strafrecht-spezial-u-bis-strafrecht-spezial-v` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 20; bündelt 10 frühere Spezialskills (strafrecht-spezial-urheberrecht-108-urhg-unerlaubte-eingriffe, strafrecht-spezial-urheberrecht-108a-urhg-gewerblich, strafrecht-spezial-urheberr... |
| `kompendium-21-strafrecht-spezial-v-bis-vergleichsverhandlun` | fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 21; bündelt 8 frühere Spezialskills (strafrecht-spezial-versicherungsbetrug-265-stgb, strafrecht-spezial-vorenthalten-arbeitgeberanteile-266a-stgb, strafrecht-spezial-vorteilsannahme... |
| `spezial-hauptverhandlung-livequellen-und-rechtsprechungscheck` | Hauptverhandlung: Livequellen- und Rechtsprechungscheck im Plugin fachanwalt strafrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-rechtsquellen-fristennotiz-und-naechster-schritt` | Rechtsquellen: Fristennotiz und nächster Schritt im Plugin fachanwalt strafrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin fachanwalt-strafrecht: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin fachanwalt-strafrecht: liest Uploads, sortiert Dokumentarten, markiert Fristen, erkennt U-Haft-, Akteneinsichts-, Rechtsmittel- und Hauptverhandlungsrisiken und baut eine knappe Arbeitsakte mit Anschluss-Skills. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin fachanwalt-strafrecht: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin fachanwalt-strafrecht: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin fachanwalt-strafrecht: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin fachanwalt-strafrecht: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
