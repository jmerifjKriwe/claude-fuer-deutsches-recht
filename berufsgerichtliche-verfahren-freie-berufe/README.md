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
| `bea-nicht-berufsgericht` | Bea Nicht In Betrieb Praevention, Bea Nicht In Betrieb Verteidigung, Berufsgericht Anschuldigungsschrift Praevention, Berufsgericht Anschuldigungsschrift Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `bea-nutzungspflichten-kanzleisitz` | Bea Nutzungspflichten, Entscheidungsvorlage, Kanzleisitz Und Zustellbarkeit, Kollegenbeleidigung Unsachlichkeit: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren O... |
| `berufsgericht-beweisaufnahme` | Berufsgericht Beweisaufnahme Praevention, Berufsgericht Beweisaufnahme Verteidigung, Berufsgesellschaft Compliance Praevention, Berufsgesellschaft Compliance Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `berufsgericht-freie-berufe-dokumente-aktenlog` | Dokumentenintake und Aktenlog: prüft ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmit... |
| `berufsgericht-freie-berufe-kaltstart-routing` | Allgemeiner Kaltstart und Routing: führt vom ersten Satz oder Dokument in den richtigen Arbeitsmodus in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur. |
| `berufsgericht-freie-berufe-quellen-rspr-fristen` | Quellen Und Rechtsprechungscheck, Frist Und Zustaendigkeit Cockpit, Haftpflichtdeckung Berufsverfahren Praevention, Haftpflichtdeckung Berufsverfahren Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Re... |
| `berufsgerichtliche-verfahren-freie-berufe-red-team-qualitygate` | Red-Team-Qualitygate: prüft prüft Ergebnis auf Fristenfehler, Zuständigkeitsfehler, Scheinpräzision und Ton in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmitt... |
| `berufspflicht-verhaeltnismaessigkeit` | Berufspflicht Und Verhaeltnismaessigkeit Praevention, Berufspflicht Und Verhaeltnismaessigkeit Verteidigung, Berufsrecht Ki Nutzung Praevention, Berufsrecht Ki Nutzung Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigke... |
| `berufsverbot-sofortvollzug-verteidigung` | Berufsverbot Und Sofortvollzug Praevention, Berufsverbot Und Sofortvollzug Verteidigung, Datenpanne Berufstraeger Praevention, Datenpanne Berufstraeger Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und R... |
| `dienstaufsicht-notar-beschwerde-verteidigung` | Dienstaufsicht Notar Beschwerde Praevention, Dienstaufsicht Notar Beschwerde Verteidigung, Fremdgeld Anderkonto Pflicht Praevention, Fremdgeld Anderkonto Pflicht Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Be... |
| `geldwaeschepflicht-kanzlei` | Geldwaeschepflicht Kanzlei Praevention, Geldwaeschepflicht Kanzlei Verteidigung, Honorarvereinbarung Erfolgshonorar Praevention, Honorarvereinbarung Erfolgshonorar Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `interessenkollision-mehrfachvertretung` | Interessenkollision Mehrfachvertretung Praevention, Interessenkollision Mehrfachvertretung Verteidigung, Kanzleisitz Und Erreichbarkeit Praevention, Kanzleisitz Und Erreichbarkeit Verteidigung: wählt den konkreten Prüfpfad, trennt Frist,... |
| `kammeranhoerung-fristverlaengerung` | Kammeranhoerung Fristverlaengerung Praevention, Kammeranhoerung Fristverlaengerung Verteidigung, Patentanwalt Fristenversaeumnis Epo Dpma Praevention, Patentanwalt Fristenversaeumnis Epo Dpma Verteidigung: wählt den konkreten Prüfpfad, t... |
| `kollegenbeleidigung-strafbarkeit` | Kollegenbeleidigung Und Strafbarkeit Praevention, Kollegenbeleidigung Und Strafbarkeit Verteidigung, Mandatskuendigung Zur Unzeit Praevention, Mandatskuendigung Zur Unzeit Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständ... |
| `mandanten-beteiligtenkommunikation-notar` | Mandanten Oder Beteiligtenkommunikation, Notar Disziplinar Bnoto, Patentanwalt Berufsgericht Pao, Protokoll Und Nachbereitung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten... |
| `notar-anderkonto-auszahlungsreife` | Notar Anderkonto Auszahlungsreife Praevention, Notar Anderkonto Auszahlungsreife Verteidigung, Notar Geldwaesche Immobilie Praevention, Notar Geldwaesche Immobilie Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `notar-gesellschafterliste-fehler-verteidigung` | Notar Gesellschafterliste Fehler Praevention, Notar Gesellschafterliste Fehler Verteidigung, Notar Unparteilichkeit Familiengesellschaft Praevention, Notar Unparteilichkeit Familiengesellschaft Verteidigung: wählt den konkreten Prüfpfad,... |
| `patentanwalt-erfinderkonflikt-praevention` | Patentanwalt Erfinderkonflikt Praevention, Patentanwalt Erfinderkonflikt Verteidigung, Patentanwalt Vertretungsbefugnis Grenze Praevention, Patentanwalt Vertretungsbefugnis Grenze Verteidigung: wählt den konkreten Prüfpfad, trennt Frist,... |
| `rak-ruege-unsachlichkeit-verteidigung` | Rak Ruege Unsachlichkeit Praevention, Rak Ruege Unsachlichkeit Verteidigung, Rechtsmittel Berufsgericht Praevention, Rechtsmittel Berufsgericht Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgru... |
| `robe-werbung-vermerk-mustertext-sitzungs` | Robe Werbung Sachlichkeit, Schriftsatz Vermerk Und Mustertext, Sitzungs Und Terminvorbereitung, Vermoegensverfall Zulassungswiderruf: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den n... |
| `sanktionen-mandatsannahme` | Sanktionen Mandatsannahme Praevention, Sanktionen Mandatsannahme Verteidigung, Aktenherausgabe Zurueckbehaltungsrecht Praevention, Aktenherausgabe Zurueckbehaltungsrecht Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständig... |
| `social-media-berufsrecht-verteidigung` | Social Media Berufsrecht Praevention, Social Media Berufsrecht Verteidigung, Steuerberater 153 Ao Berichtigung Praevention, Steuerberater 153 Ao Berichtigung Verteidigung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `steuerberater-berufsgericht-stberg` | Steuerberater Berufsgericht Stberg, Steuerberater Unterlagenherausgabe Praevention, Steuerberater Unterlagenherausgabe Verteidigung, Steuerberater Vorbehaltsaufgabe Praevention: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `steuerberater-vorbehaltsaufgabe-kammer` | Steuerberater Vorbehaltsaufgabe Verteidigung, Vergleich Mit Kammer Praevention, Vergleich Mit Kammer Verteidigung, Vermoegensverfall Zulassungswiderruf Praevention: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Re... |
| `vermoegensverfall-zulassungswiderruf` | Vermoegensverfall Zulassungswiderruf Verteidigung, Verschwiegenheit Cloud Dienstleister Praevention, Verschwiegenheit Cloud Dienstleister Verteidigung, Werbung Robe Kanzleimarketing Praevention: wählt den konkreten Prüfpfad, trennt Frist... |
| `werbung-robe-wirtschaftspruefer` | Werbung Robe Kanzleimarketing Verteidigung, Wirtschaftspruefer Qualitaetskontrolle Praevention, Wirtschaftspruefer Qualitaetskontrolle Verteidigung, Wirtschaftspruefer Testat Widerruf Praevention: wählt den konkreten Prüfpfad, trennt Fri... |
| `wirtschaftspruefer-berufsaufsicht` | Wirtschaftspruefer Berufsaufsicht Wpo: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `wirtschaftspruefer-testat-widerruf` | Wirtschaftspruefer Testat Widerruf Verteidigung, Wirtschaftspruefer Unabhaengigkeit Praevention, Wirtschaftspruefer Unabhaengigkeit Verteidigung, Anwaltsgericht Brao Ueberblick: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
