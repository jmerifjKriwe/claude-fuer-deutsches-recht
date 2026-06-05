# Berufsgerichtliche Verfahren Freie Berufe

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`berufsgerichtliche-verfahren-freie-berufe`) | [`berufsgerichtliche-verfahren-freie-berufe.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsgerichtliche-verfahren-freie-berufe.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für anwaltsgerichtliche und berufsgerichtliche Verfahren gegen Anwälte, Patentanwälte, Steuerberater, Wirtschaftsprüfer und Notare: Kammeraufsicht, Rüge, Disziplinarverfahren, Zulassung, Vermögensverfall, beA, Werbung, Sachlichkeit und Rechtsmittel.

## Worum es geht

Dieses Plugin ist ein experimentelles Arbeits- und Lernwerkzeug. Es soll keine echten Amts-, Mandats-, Steuer-, Prüfungs- oder Berufsgeheimnisse aufnehmen, solange die technische und rechtliche Umgebung dafür nicht ausdrücklich freigegeben ist. Es arbeitet am besten mit anonymisierten, abstrahierten oder synthetischen Fällen und mit Dokumenten, die vor der Nutzung datenschutz- und geheimnisschutzrechtlich geprüft wurden.

## Arbeitsweise

Der Allgemein-Skill startet kurz, sortiert Rolle, Verfahrensstand, Frist, Unterlagen und gewünschtes Arbeitsprodukt und routet dann in die passenden Spezial-Skills. Jeder Skill verlangt Quellenhygiene: Normen, Behördenhinweise, Formulare und Rechtsprechung werden vor tragenden Aussagen live aus amtlichen oder frei zugänglichen Quellen geprüft; keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

## Typische Outputs

- Kurzvermerk und Risikoampel
- Checkliste für den nächsten Arbeitstag
- Fragenliste an Behörde, Gericht, Kammer, Mandant, Partei oder Zeugen
- Entwurf für Verfügung, Vermerk, Schriftsatz, Antrag, E-Mail oder Gesprächsleitfaden
- Red-Team-Check gegen Fristenfehler, Zuständigkeitsfehler und Scheingenauigkeit

## Installation

ZIP aus dem aktuellen Release laden und in Claude Code oder Cowork über Customize Plugins installieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `bea-nicht-berufsgericht` | BEA Nicht Berufsgericht: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bea-nutzungspflichten-kanzleisitz` | BEA Nutzungspflichten Kanzleisitz: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `berufsgericht-beweisaufnahme` | Berufsgericht Beweisaufnahme: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `berufsgericht-freie-berufe-dokumente-aktenlog` | Dokumentenintake und Aktenlog: prüft ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmit... |
| `berufsgericht-freie-berufe-kaltstart-routing` | Allgemeiner Kaltstart und Routing: führt vom ersten Satz oder Dokument in den richtigen Arbeitsmodus in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur. |
| `berufsgericht-freie-berufe-quellen-rspr-fristen` | Berufsgericht Freie Berufe Quellen Rspr Fristen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `berufsgerichtliche-verfahren-freie-berufe-red-team-qualitygate` | Red-Team-Qualitygate: prüft prüft Ergebnis auf Fristenfehler, Zuständigkeitsfehler, Scheinpräzision und Ton in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmitt... |
| `berufspflicht-verhaeltnismaessigkeit` | Berufspflicht Verhaeltnismaessigkeit: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `berufsverbot-sofortvollzug-verteidigung` | Berufsverbot Sofortvollzug Verteidigung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `dienstaufsicht-notar-beschwerde-verteidigung` | Dienstaufsicht Notar Beschwerde Verteidigung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `geldwaeschepflicht-kanzlei` | Geldwaeschepflicht Kanzlei: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `interessenkollision-mehrfachvertretung` | Interessenkollision Mehrfachvertretung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kammeranhoerung-fristverlaengerung` | Kammeranhoerung Fristverlaengerung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kollegenbeleidigung-strafbarkeit` | Kollegenbeleidigung Strafbarkeit: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mandanten-beteiligtenkommunikation-notar` | Mandanten Beteiligtenkommunikation Notar: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notar-anderkonto-auszahlungsreife` | Notar Anderkonto Auszahlungsreife: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notar-gesellschafterliste-fehler-verteidigung` | Notar Gesellschafterliste Fehler Verteidigung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `patentanwalt-erfinderkonflikt-praevention` | Patentanwalt Erfinderkonflikt Praevention: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `rak-ruege-unsachlichkeit-verteidigung` | RAK Ruege Unsachlichkeit Verteidigung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `robe-werbung-vermerk-mustertext-sitzungs` | Robe Werbung Vermerk Mustertext Sitzungs: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `sanktionen-mandatsannahme` | Sanktionen Mandatsannahme: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `social-media-berufsrecht-verteidigung` | Social Media Berufsrecht Verteidigung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `steuerberater-berufsgericht-stberg` | Steuerberater Berufsgericht Stberg: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `steuerberater-vorbehaltsaufgabe-kammer` | Steuerberater Vorbehaltsaufgabe Kammer: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vermoegensverfall-zulassungswiderruf` | Vermoegensverfall Zulassungswiderruf: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `werbung-robe-wirtschaftspruefer` | Werbung Robe Wirtschaftspruefer: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `wirtschaftspruefer-berufsaufsicht` | Wirtschaftspruefer Berufsaufsicht: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat. |
| `wirtschaftspruefer-testat-widerruf` | Wirtschaftspruefer Testat Widerruf: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
