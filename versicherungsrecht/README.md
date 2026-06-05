# Versicherungsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`versicherungsrecht`) | [`versicherungsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/versicherungsrecht.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

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
| `bu-berufsbild-bu-nachpruefung-datenschutz` | BU Berufsbild BU Nachpruefung Datenschutz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `cyberversicherung-ransomware-d-o` | Cyberversicherung Ransomware D O: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `deckungsprozess-vvg-rechtsabteilung` | Deckungsprozess VVG Rechtsabteilung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `direktanspruch-pflichtversicherung-eiopa` | Direktanspruch Pflichtversicherung Eiopa: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `dora-cyber-abfindung-entschaedigungsquittung` | Dora Cyber Abfindung Entschaedigungsquittung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `hausrat-einbruchdiebstahl-idd-vertrieb` | Hausrat Einbruchdiebstahl IDD Vertrieb: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kfz-haftpflicht-kasko-grobe-krankentagegeld` | KFZ Haftpflicht Kasko Grobe Krankentagegeld: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kreditausfallversicherung-warenkredit` | Kreditausfallversicherung Warenkredit: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `lebensversicherung-rueckkaufswert` | Lebensversicherung Rueckkaufswert: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `pkv-kostenerstattung-private` | PKV Kostenerstattung Private: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `rechtsabteilung-betriebsunterbrechung` | Rechtsabteilung Betriebsunterbrechung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `rechtsabteilung-d-umwelthaftpflicht` | Rechtsabteilung D Umwelthaftpflicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `rechtsschutz-deckungszusage-erfolgsaussicht` | Rechtsschutz Deckungszusage Erfolgsaussicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `restschuldversicherung-widerruf` | Restschuldversicherung Widerruf: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `subrogation-regress-transportversicherung` | Subrogation Regress Transportversicherung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `unfallversicherung-invaliditaet-vers` | Unfallversicherung Invaliditaet Vers: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vers-deckungsablehnung-redteam` | Deckungsablehnung des Versicherers zerlegen: Risikoausschluss, Obliegenheit, Kausalität, grobe Fahrlässigkeit, Arglist, Beweislast und Vergleichsfenster systematisch prüfen. |
| `vers-dokumentenintake-police-avb-nachtraege` | Dokumentenintake für Versicherungsakten: Versicherungsschein, AVB, Nachträge, Beratungsdokumentation, Schadenanzeige, Gutachten, Korrespondenz und Ablehnung in eine Aktenmatrix überführen. |
| `vers-kaltstart-routing` | Allgemeiner Einstieg ins Versicherungsrecht: Police, Bedingungen, Schadenereignis, Ablehnung, Fristen, Aufsicht, Ombudsmann und Klageweg strukturiert erfassen und passende Fachmodule vorschlagen. |
| `vers-ombudsmann-versicherungsbetrug` | Vers Ombudsmann Versicherungsbetrug: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `versicherungsprodukt-agb-betriebshaftpflicht` | Versicherungsprodukt AGB Betriebshaftpflicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `versicherungsrecht-vvg-anzeigepflicht-ruecktritt-arglist` | VVG Anzeigepflicht Ruecktritt Arglist: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vvg-gefahrerhoehung-mehrfachversicherung` | VVG Gefahrerhoehung Mehrfachversicherung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vvg-versicherung-wohngebaeude-leitungswasser` | VVG Versicherung Wohngebaeude Leitungswasser: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
