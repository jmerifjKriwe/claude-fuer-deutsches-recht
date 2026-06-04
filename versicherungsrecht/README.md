# Versicherungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`versicherungsrecht`) | [`versicherungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versicherungsrecht.zip) |

### Demonstrations-Akten

Dieses Plugin hat derzeit keine eigene Demonstrations-Akte. Es arbeitet mit hochgeladenen Policen, Bescheiden, Verträgen, Messprotokollen, Behördenbriefen und Aktenauszügen.

<!-- END plugin-sofort-download-section (autogen) -->

Großes, praxisnahes Versicherungsrecht-Plugin für Deckung, Ablehnung, Vertragsgestaltung, Aufsicht und Prozess. Es ist bewusst nicht nur ein Fachanwalts-Lernplugin, sondern ein Arbeitswerkzeug für Kanzlei, Rechtsabteilung, Versicherungsnehmer, Vermittler und Versicherer.

## Was dieses Plugin gut kann

- Deckungsablehnungen und Leistungsprüfung nach VVG zerlegen.
- Lebensversicherung, BU, PKV, Unfall, Rechtsschutz, Kreditversicherung, D&O, Cyber und Sachversicherung mit eigenen Spezial-Skills prüfen.
- BaFin, Ombudsmann, Klage und Vergleich taktisch voneinander trennen.
- Europäische Aufsicht, IDD, Solvency II, DORA und grenzüberschreitenden Vertrieb einordnen.

## Startlogik

Beginne mit dem allgemeinen Skill. Er fragt Rolle, Ziel, Fristen, Unterlagen, Eskalationsniveau und gewünschten Output ab. Danach schlägt er nur die Spezial-Skills vor, die zum Fall passen.

## Quellenhygiene

Normtexte werden aus amtlichen Quellen geprüft. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle verwendet. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. Nicht das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-deckungsprozess-zust-bis-sachverstaendigenver` | versicherungsrecht: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (deckungsprozess-zustaendigkeit-215-vvg, rechtsabteilung-rechtsschutzversicherung-im-massenverfahren, sachverstaendigenverfahren-versicherung) und be... |
| `kompendium-02-unfallversicherung-i-bis-rechtsschutz-vorvert` | versicherungsrecht: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (unfallversicherung-invaliditaet-fristen-gliedertaxe, vers-fristen-verjaehrung-klagefrist-fallkalender, rechtsschutz-vorvertraglichkeit-schadenereign... |
| `kompendium-03-versicherungsprodukt-bis-betriebsunterbrechun` | versicherungsrecht: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (versicherungsprodukt-agb-klauselkontrolle, betriebshaftpflicht-versicherungsfall-serienschaden, betriebsunterbrechung-sachschaden-trigger) und bewah... |
| `kompendium-04-cyberversicherung-ra-bis-elementarschaden-sta` | versicherungsrecht: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (cyberversicherung-ransomware-sanktionsrecht, d-o-claims-made-innenhaftung-43-gmbhg, elementarschaden-starkregen-ueberschwemmung) und bewahrt deren W... |
| `kompendium-05-rechtsabteilung-d-o-bis-versicherungsmakler` | versicherungsrecht: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (rechtsabteilung-d-o-deckung-bei-organhaftung, umwelthaftpflicht-umweltschadenversicherung, versicherungsmakler-haftung-deckungsluecke) und bewahrt d... |
| `kompendium-06-dora-cyber-ikt-versi-bis-bu-abstrakte-konkret` | versicherungsrecht: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (dora-cyber-ikt-versicherer, vergleich-abfindung-entschaedigungsquittung, bu-abstrakte-konkrete-verweisung) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-07-bu-berufsbild-50-pro-bis-datenschutz-schweige` | versicherungsrecht: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (bu-berufsbild-50-prozent-substantiierung, bu-nachpruefung-anerkenntnis-leistungseinstellung, datenschutz-schweigepflicht-gesundheitsdaten) und bewah... |
| `kompendium-08-direktanspruch-pflic-bis-gewerbe-betriebsschl` | versicherungsrecht: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (direktanspruch-pflichtversicherung-115-vvg, eiopa-grenzueberschreitender-vertrieb, gewerbe-betriebsschliessung-infektionsschutz) und bewahrt deren W... |
| `kompendium-09-hausrat-einbruchdieb-bis-internationales-vers` | versicherungsrecht: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (hausrat-einbruchdiebstahl-entschaedigungsgrenze, idd-vertrieb-beratung-dokumentation, internationales-versicherungsprogramm-master-local-policy) und... |
| `kompendium-10-kfz-haftpflicht-regr-bis-krankentagegeld-beru` | versicherungsrecht: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (kfz-haftpflicht-regress-alkohol-flucht, kfz-kasko-grobe-fahrlaessigkeit-entwendung, krankentagegeld-berufsunfaehigkeit-abgrenzung) und bewahrt deren... |
| `kompendium-11-kreditausfallversich-bis-lebensversicherung-b` | versicherungsrecht: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (kreditausfallversicherung-warenkredit-forderungsausfall, kreditversicherung-obliegenheiten-limit-pruefung, lebensversicherung-bezugsrecht-widerruf-a... |
| `kompendium-12-lebensversicherung-r-bis-nachhaltigkeit-taxon` | versicherungsrecht: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (lebensversicherung-rueckkaufswert-abschlusskosten-widerspruch, lebensversicherung-ueberschussbeteiligung-bewertungsreserven, nachhaltigkeit-taxonomi... |
| `kompendium-13-pkv-kostenerstattung-bis-produkthaftpflicht-r` | versicherungsrecht: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (pkv-kostenerstattung-medizinische-notwendigkeit, private-krankenversicherung-beitragsanpassung-treuhaender, produkthaftpflicht-rueckrufkosten) und b... |
| `kompendium-14-rechtsabteilung-betr-bis-rechtsabteilung-idd` | versicherungsrecht: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (rechtsabteilung-betriebsunterbrechung-und-lieferkettenausfall, rechtsabteilung-cyberversicherung-nach-ransomware, rechtsabteilung-idd-vertrieb-und-p... |
| `kompendium-15-rechtsschutz-deckung-bis-reiseversicherung-ru` | versicherungsrecht: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (rechtsschutz-deckungszusage-stichentscheid, rechtsschutz-erfolgsaussicht-mutwilligkeit, reiseversicherung-ruecktritt-abbruch-krankheit) und bewahrt... |
| `kompendium-16-restschuldversicheru-bis-solvency-ii-scr-orsa` | versicherungsrecht: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (restschuldversicherung-widerruf-kopplung-verbraucherdarlehen, rueckversicherung-cut-through-und-fronting, solvency-ii-scr-orsa-aufsichtsrecht) und b... |
| `kompendium-17-subrogation-regress-bis-vag-bafin-aufsicht-b` | versicherungsrecht: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (subrogation-regress-86-vvg, transportversicherung-ware-lagerung, vag-bafin-aufsicht-beschwerde-missstand) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-18-vers-ombudsmann-bafi-bis-versicherungssumme-u` | versicherungsrecht: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (vers-ombudsmann-bafin-beschwerde-klageweg, versicherungsbetrug-verdachtsfall-kooperation-strafrecht, versicherungssumme-unterversicherung-taxwert) u... |
| `kompendium-19-vvg-anzeigepflicht-1-bis-vvg-falligkeit-14-ab` | versicherungsrecht: Konsolidiertes Skill-Kompendium 19; bündelt 3 frühere Spezialskills (vvg-anzeigepflicht-19-ruecktritt-kuendigung-anpassung, vvg-arglist-taeuschung-anfechtung, vvg-falligkeit-14-abschlagszahlung) und bewahrt deren Work... |
| `kompendium-20-vvg-gefahrerhoehung-bis-vvg-obliegenheit-28` | versicherungsrecht: Konsolidiertes Skill-Kompendium 20; bündelt 3 frühere Spezialskills (vvg-gefahrerhoehung-23-27, vvg-mehrfachversicherung-78, vvg-obliegenheit-28-quotelung-kausalitaet) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-21-vvg-versicherung-fue-bis-wohngebaeude-leitung` | versicherungsrecht: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (vvg-versicherung-fuer-fremde-43-48, wohngebaeude-leitungswasser-sturm-hagel-brand) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabe... |
| `vers-allgemeiner-kaltstart` | Allgemeiner Einstieg ins Versicherungsrecht: Police, Bedingungen, Schadenereignis, Ablehnung, Fristen, Aufsicht, Ombudsmann und Klageweg strukturiert erfassen und passende Spezial-Skills vorschlagen. |
| `vers-deckungsablehnung-redteam` | Deckungsablehnung des Versicherers zerlegen: Risikoausschluss, Obliegenheit, Kausalität, grobe Fahrlässigkeit, Arglist, Beweislast und Vergleichsfenster systematisch prüfen. |
| `vers-dokumentenintake-police-avb-nachtraege` | Dokumentenintake für Versicherungsakten: Versicherungsschein, AVB, Nachträge, Beratungsdokumentation, Schadenanzeige, Gutachten, Korrespondenz und Ablehnung in eine Aktenmatrix überführen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
