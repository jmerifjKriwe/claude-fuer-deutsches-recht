# Berufsrecht Anwälte

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`berufsrecht-anwaelte`) | [`berufsrecht-anwaelte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-anwaelte.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Falkenried & Partner mbB — Managementakte Q2/2026** (`kanzlei-management-falkenried-partnerkreis-q2-2026`) | [Gesamt-PDF lesen](../testakten/kanzlei-management-falkenried-partnerkreis-q2-2026/gesamt-pdf/kanzlei-management-falkenried-partnerkreis-q2-2026_gesamt.pdf) | [`testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzlei-management-falkenried-partnerkreis-q2-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für anwaltliches Berufsrecht: BRAO, BORA, FAO, beA, Kanzleisitz, Werbung, Interessenkollision, Verschwiegenheit, KI-/Cloud-Outsourcing, Fremdbesitz, Berufsausübungsgesellschaft, Gebühren, Kammeraufsicht und anwaltsgerichtliche Risiken.

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
- KI-/Outsourcing-Freigabevermerk nach § 43e BRAO mit Consumer-Tool-Abgrenzung, No-Training, Drittstaat, Schatten-KI-Policy, KI-VO-Transparenz und anwaltlicher Endkontrolle

## Installation

ZIP aus dem aktuellen Release laden und in Claude Code oder Cowork über Customize Plugins installieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 51 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ai-act-aktenherausgabe-zurueckbehaltung` | AI ACT Aktenherausgabe Zurueckbehaltung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-aktenherausgabe-zurueckbehaltung-fak` | Anwälte: aktenherausgabe und zurueckbehaltung - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `anwaelte-anwaltliche-nebentaetigkeit` | Anwälte: anwaltliche nebentaetigkeit - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `anwaelte-anwaltsgerichtliche-anschuldigung` | Anwälte: anwaltsgerichtliche anschuldigung - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `anwaelte-bea-passive-nutzung` | Anwälte: bea passive nutzung und empfangsbekenntnis - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `anwaelte-berufsausuebungsgesellschaft` | Anwälte: berufsausuebungsgesellschaft und fremdbesitz - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `anwaelte-berufsrechtliche` | Anwälte: berufsrechtliche notfallkommunikation - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `anwaelte-beschwerde-rechtsanwaltskammer-fakte` | Anwälte: beschwerde bei rechtsanwaltskammer - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `anwaelte-datenschutzpanne-kanzlei` | Datenschutzpanne Kanzlei: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-fristversaeumnis-wiedereinsetzung` | Fristversaeumnis Wiedereinsetzung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-geldwaesche-risikoanalyse` | Geldwaesche Risikoanalyse: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-honorarvereinbarung-rvg` | Honorarvereinbarung RVG: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-internationales-geheimnisschutz` | Internationales Geheimnisschutz: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-kammeraufsicht-kammerantwort` | Kammeraufsicht Kammerantwort: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-ki-tool-legal-tech-mandatsgeheimnis` | KI Tool Legal Tech Mandatsgeheimnis: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-legal-tech-mandatskuendigung-unzeit` | Legal Tech Mandatskuendigung Unzeit: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-qualitaetsmanagement-vier-robe` | Qualitaetsmanagement Vier Robe: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-ruege-gegenvorstellung-sanktionen` | Ruege Gegenvorstellung Sanktionen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-ruege-gegenvorstellung-schatten-ki` | Ruege Gegenvorstellung Schatten KI: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-syndikusrechtsanwalt-abgrenzung` | Syndikusrechtsanwalt Abgrenzung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-umgehung-berufsgericht` | Umgehung Berufsgericht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-verschwiegenheit-cloud-outsourcing` | Verschwiegenheit Cloud Outsourcing: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaelte-werbung-google-aktenherausgabe` | Werbung Google Aktenherausgabe: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anwaltsgerichtliche-anschuldigung` | Anwaltsgerichtliche Anschuldigung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `bea-passive-berufsausuebungsgesellschaft` | BEA Passive Berufsausuebungsgesellschaft: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `berufsrecht-anwaelte-kaltstart-routing` | Allgemeiner Kaltstart und Routing: vertiefter Berufsrechts-Skill für Anwälte; führt vom ersten Satz oder Dokument in den richtigen Arbeitsmodus, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und nä... |
| `berufsrecht-bag-zulassung-haftung` | BAG Zulassung Haftung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `berufsrechtliche-notfallkommunikation` | Berufsrechtliche Notfallkommunikation: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `beweisfuehrung-berufsverfahren` | Beweisfuehrung Berufsverfahren: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `beweisfuehrung-berufsverfahren-fremdgeld` | Beweisfuehrung Berufsverfahren Fremdgeld: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `datenraum-dokumentenintake-aktenlog` | Datenraum Dokumentenintake Aktenlog: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fachanwaltstitel-fortbildung-fremdgeld` | Fachanwaltstitel Fortbildung Fremdgeld: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fortbildung-geldwaesche-kyc-homeoffice` | Fortbildung Geldwaesche KYC Homeoffice: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fremdgeld-anderkonto-gebuehrenunterschreitung` | Fremdgeld Anderkonto Gebuehrenunterschreitung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `geldwaesche-risikoanalyse` | Geldwaesche Risikoanalyse: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `interessenkollision-mehrfachvertretung` | Interessenkollision Mehrfachvertretung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `it-cloud-kammeraufsicht-ruege` | IT Cloud Kammeraufsicht Ruege: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kammeraufsicht-rechtsprechungscheck` | Kammeraufsicht Rechtsprechungscheck: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ki-tool-legal-tech-mandatsgeheimnis` | KI Tool Legal Tech Mandatsgeheimnis: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ki-tool-legal-tech-mandatskuendigung-unzeit` | KI Tool Legal Tech Mandatskuendigung Unzeit: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mandanten-beteiligtenkommunikation` | Mandanten Beteiligtenkommunikation: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notfallkommunikation-rak-beschwerde-berufsverfahren` | Notfallkommunikation RAK Beschwerde Berufsverfahren: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `protokoll-nachbereitung-rechnungseinzug-red` | Protokoll Nachbereitung Rechnungseinzug RED: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `qualitaetsmanagement-vier` | Qualitaetsmanagement Vier: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `sanktionen-mandatsannahme-steuerliche` | Sanktionen Mandatsannahme Steuerliche: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `sozietaetswechsel-mandantenmitnahme` | Sozietaetswechsel Mandantenmitnahme: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `sozietaetswechsel-syndikus-terminsvertretung` | Sozietaetswechsel Syndikus Terminsvertretung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `terminsvertreter-untervollmacht-umgehung` | Terminsvertreter Untervollmacht Umgehung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `umgehung-gegenanwalts-unsachlichkeit` | Umgehung Gegenanwalts Unsachlichkeit: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vermerk-mustertext-sitzungs` | Vermerk Mustertext Sitzungs: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verschwiegenheit-geheimnisschutz-werbung` | Verschwiegenheit Geheimnisschutz Werbung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
