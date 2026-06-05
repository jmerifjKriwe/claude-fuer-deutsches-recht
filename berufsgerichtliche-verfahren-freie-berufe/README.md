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
| `bea-nicht-berufsgericht` | BEA Nicht Berufsgericht im Berufsgerichtliche Verfahren freier Berufe: prüft konkret beA nicht in Betrieb (Präventions- und Organisationspaket), beA nicht in Betrieb (Verteidigungs- und Kammerantwort), Berufsgericht Anschuldigungsschrift... |
| `bea-nutzungspflichten-kanzleisitz` | BEA Nutzungspflichten Kanzleisitz im Berufsgerichtliche Verfahren freier Berufe: prüft konkret beA und elektronische Kommunikation, Entscheidungsvorlage, Kanzleisitz und Zustellbarkeit, Kollegenbeleidigung und Unsachlichkeit. Liefert pri... |
| `berufsgericht-beweisaufnahme` | Berufsgericht Beweisaufnahme im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Berufsgericht Beweisaufnahme (Präventions- und, Berufsgericht Beweisaufnahme (Verteidigungs- und, Berufsgesellschaft Compliance (Präventions- und,... |
| `berufsgericht-freie-berufe-dokumente-aktenlog` | Dokumentenintake und Aktenlog: prüft ordnet Uploads, Eingangspost, Aktenbestandteile und fehlende Unterlagen in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmit... |
| `berufsgericht-freie-berufe-kaltstart-routing` | Allgemeiner Kaltstart und Routing: führt vom ersten Satz oder Dokument in den richtigen Arbeitsmodus in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmittelspur. |
| `berufsgericht-freie-berufe-quellen-rspr-fristen` | Berufsgericht Freie Berufe Quellen Rspr Fristen im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Quellen- und Rechtsprechungscheck, Fristen- und Zuständigkeitscockpit, Haftpflichtdeckung im Berufsverfahren (Präventions- und,... |
| `berufsgerichtliche-verfahren-freie-berufe-red-team-qualitygate` | Red-Team-Qualitygate: prüft prüft Ergebnis auf Fristenfehler, Zuständigkeitsfehler, Scheinpräzision und Ton in berufsgerichtlichen Verfahren freier Berufe; mit Normencheck, Aktenlog, Verteidigungslinie, Verhältnismäßigkeit und Rechtsmitt... |
| `berufspflicht-verhaeltnismaessigkeit` | Berufspflicht Verhaeltnismaessigkeit im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Berufspflicht und Verhältnismäßigkeit (Präventions- und, Berufspflicht und Verhältnismäßigkeit (Verteidigungs- und, Berufsrecht KI-Nutzung... |
| `berufsverbot-sofortvollzug-verteidigung` | Berufsverbot Sofortvollzug Verteidigung im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Berufsverbot und Sofortvollzug (Präventions- und, Berufsverbot und Sofortvollzug (Verteidigungs- und, Datenpanne beim Berufsträger (Präv... |
| `dienstaufsicht-notar-beschwerde-verteidigung` | Dienstaufsicht Notar Beschwerde Verteidigung im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Dienstaufsicht Notar Beschwerde (Präventions- und, Dienstaufsicht Notar Beschwerde (Verteidigungs- und, Fremdgeld und Anderkonto (P... |
| `geldwaeschepflicht-kanzlei` | Geldwaeschepflicht Kanzlei im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Geldwäschepflichten der Kanzlei (Präventions- und, Geldwäschepflichten der Kanzlei (Verteidigungs- und, Honorarvereinbarung und Erfolgshonorar (Präve... |
| `interessenkollision-mehrfachvertretung` | Interessenkollision Mehrfachvertretung im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Interessenkollision Mehrfachvertretung (Präventions- und, Interessenkollision Mehrfachvertretung (Verteidigungs- und, Kanzleisitz und Err... |
| `kammeranhoerung-fristverlaengerung` | Kammeranhoerung Fristverlaengerung im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Kammeranhörung Fristverlängerung (Präventions- und, Kammeranhörung Fristverlängerung (Verteidigungs- und, Patentanwalt Fristenversäumnis DPMA... |
| `kollegenbeleidigung-strafbarkeit` | Kollegenbeleidigung Strafbarkeit im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Kollegenbeleidigung und Strafbarkeit (Präventions- und, Kollegenbeleidigung und Strafbarkeit (Verteidigungs- und, Mandatskündigung zur Unzeit (... |
| `mandanten-beteiligtenkommunikation-notar` | Mandanten Beteiligtenkommunikation Notar im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Beteiligtenkommunikation, Notar Disziplinarverfahren BNotO, Patentanwalt Berufsgericht PAO, Protokoll und Nachbereitung. Liefert priori... |
| `notar-anderkonto-auszahlungsreife` | Notar Anderkonto Auszahlungsreife im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Notaranderkonto Auszahlungsreife (Präventions- und, Notaranderkonto Auszahlungsreife (Verteidigungs- und, Notar Geldwäsche Immobilie (Präventi... |
| `notar-gesellschafterliste-fehler-verteidigung` | Notar Gesellschafterliste Fehler Verteidigung im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Notar Gesellschafterliste Fehler (Präventions- und, Notar Gesellschafterliste Fehler (Verteidigungs- und, Notar Unparteilichkeit F... |
| `patentanwalt-erfinderkonflikt-praevention` | Patentanwalt Erfinderkonflikt Praevention im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Patentanwalt Erfinderkonflikt (Präventions- und, Patentanwalt Erfinderkonflikt (Verteidigungs- und, Patentanwalt Vertretungsbefugnis G... |
| `rak-ruege-unsachlichkeit-verteidigung` | RAK Ruege Unsachlichkeit Verteidigung im Berufsgerichtliche Verfahren freier Berufe: prüft konkret RAK-Rüge wegen Unsachlichkeit (Präventions- und, RAK-Rüge wegen Unsachlichkeit (Verteidigungs- und, Rechtsmittel im Berufsgericht (Prävent... |
| `robe-werbung-vermerk-mustertext-sitzungs` | Robe Werbung Vermerk Mustertext Sitzungs im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Robe, Werbung und Sachlichkeit, Schriftsatz, Vermerk und Mustertext. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und n... |
| `sanktionen-mandatsannahme` | Sanktionen Mandatsannahme im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Sanktionen und Mandatsannahme (Präventions- und, Sanktionen und Mandatsannahme (Verteidigungs- und, Aktenherausgabe und Zurückbehaltungsrecht (Prävent... |
| `social-media-berufsrecht-verteidigung` | Social Media Berufsrecht Verteidigung im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Social Media Berufsrecht (Präventions- und, Social Media Berufsrecht (Verteidigungs- und Kammerantwort), Steuerberater § 153 AO Berichtigu... |
| `steuerberater-berufsgericht-stberg` | Steuerberater Berufsgericht Stberg im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Steuerberater Berufsgericht StBerG, Steuerberater Unterlagenherausgabe (Präventions- und, Steuerberater Unterlagenherausgabe (Verteidigungs-... |
| `steuerberater-vorbehaltsaufgabe-kammer` | Steuerberater Vorbehaltsaufgabe Kammer im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Steuerberater Vorbehaltsaufgabe (Verteidigungs- und, Vergleich mit Kammer oder Aufsicht (Präventions- und, Vergleich mit Kammer oder Aufs... |
| `vermoegensverfall-zulassungswiderruf` | Vermoegensverfall Zulassungswiderruf im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Vermögensverfall und Zulassungswiderruf (Verteidigungs- und, Verschwiegenheit und Cloud-Dienstleister (Präventions- und, Verschwiegenheit u... |
| `werbung-robe-wirtschaftspruefer` | Werbung Robe Wirtschaftspruefer im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Werbung, Robe und Kanzleimarketing (Verteidigungs- und Kammerantwort), Wirtschaftsprüfer Qualitätskontrolle (Präventions- und, Wirtschaftsprüfer... |
| `wirtschaftspruefer-berufsaufsicht` | Wirtschaftspruefer Berufsaufsicht im Berufsgerichtliche Verfahren freier Berufe: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |
| `wirtschaftspruefer-testat-widerruf` | Wirtschaftspruefer Testat Widerruf im Berufsgerichtliche Verfahren freier Berufe: prüft konkret Wirtschaftsprüfer Testat Widerruf (Verteidigungs- und, Wirtschaftsprüfer Unabhängigkeit (Präventions- und, Wirtschaftsprüfer Unabhängigkeit (... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
