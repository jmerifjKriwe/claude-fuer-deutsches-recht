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
| **Grossbankrott und Zeugenstreit — Mehrere Deliktszweige, Pellbach Logistik & Spedition GmbH, LG Koeln** (`grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln`) | [Gesamt-PDF lesen](../testakten/grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln/gesamt-pdf/grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln_gesamt.pdf) | [`testakte-grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-grossbankrott-und-zeugenstreit-mehrere-deliktszweige-vellbruck-koeln.zip) |
| **Vertriebsbonus und staatsanwaltschaftlicher Honeypot** (`internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot`) | [Gesamt-PDF lesen](../testakten/internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot/gesamt-pdf/internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot_gesamt.pdf) | [`testakte-internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-internal-investigation-vertriebsbonus-staatsanwaltschaft-honeypot.zip) |
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

Automatisch generierte Komplett-Liste aller 37 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `adhaesionsverfahren-ermittlungsverfahren` | Adhaesionsverfahren Ermittlungsverfahren: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `aussagepsychologie-staatsanwaltschaft` | Aussagepsychologie Staatsanwaltschaft: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `chatcontrol-csam-einlassung-vorbereiten` | Chatcontrol Csam Einlassung Vorbereiten: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ergaenzt-fachanwalt-insolvenzantrag-red` | Ergaenzt Fachanwalt Insolvenzantrag RED: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fa-strafrecht-quellen-frist-next` | Rechtsquellen: Quellenprüfung; Fristennotiz und nächster Schritt: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `fachanwalt-strafrecht-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `fachanwalt-strafrecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `fachanwalt-strafrecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `fachanwalt-strafrecht-orientierung` | Orientierung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fachanwalt-strafrecht-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `fachanwalt-strafrecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `fachanwalt-strafrecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `hauptverhandlung-quellenkarte` | Hauptverhandlung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `koerperverletzung-stgb-todesfolge` | Koerperverletzung Stgb Todesfolge: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mandat-triage-plaedoyer-vorbereitung` | Mandat Triage Plaedoyer Vorbereitung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `nebenklage-nebenstrafrecht-opfervertretung` | Nebenklage Nebenstrafrecht Opfervertretung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `spezial-raub-rechtsbeugung` | Spezial Raub Rechtsbeugung: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `steuerstrafrecht-ao-akteneinsicht-auswerten` | Steuerstrafrecht AO Akteneinsicht Auswerten: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `stpo-strafrecht-strafverteidigung` | Stpo Strafrecht Strafverteidigung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafprozess-antragslog-beweisantraege` | Strafprozess Antragslog Beweisantraege: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafprozess-instruktionen` | Strafprozess Instruktionen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafr-dysfunk-befangenheitsantrag` | Strafr Dysfunk Befangenheitsantrag: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafr-dysfunk-darlegungslast-empirie-nutzen` | Strafr Dysfunk Darlegungslast Empirie Nutzen: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafr-dysfunk-sitzungspolizei` | Strafr Dysfunk Sitzungspolizei: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafr-haftpruefung` | Strafr Haftpruefung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafr-vermoegensabschoepfung` | Strafr Vermoegensabschoepfung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafrecht-aussagepsy-suggestion-tuechtigkeit` | Aussagepsy Suggestion Tuechtigkeit: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafrecht-betrug-stgb-btmg-grundtatbestand` | Betrug Stgb Btmg Grundtatbestand: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafrecht-computerbetrug-263a-design-designg` | Computerbetrug 263a Design Designg: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafrecht-gmbh-verletzung-insiderhandel-wphg` | Gmbh Verletzung Insiderhandel Wphg: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafrecht-markenrecht-143a-marktmanipulation` | Markenrecht 143a Marktmanipulation: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafrecht-stgb-easy-social-media-amtsdelikte` | Stgb Easy Social Media Amtsdelikte: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafrecht-strafprozess-ermittlungsverfahren` | Strafprozess Ermittlungsverfahren: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafrecht-untreue-schaden` | Untreue Schaden: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafrecht-urheberrecht-urhg-108a-gewerblich` | Urheberrecht Urhg 108a Gewerblich: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `subventionsbetrug-stgb-toetung-verlangen` | Subventionsbetrug Stgb Toetung Verlangen: bündelt 10 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `versicherungsbetrug-stgb-vorenthalten` | Versicherungsbetrug Stgb Vorenthalten: bündelt 8 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
