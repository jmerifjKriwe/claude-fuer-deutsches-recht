# Berufsrecht Notare

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`berufsrecht-notare`) | [`berufsrecht-notare.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berufsrecht-notare.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Waldwinkel: GmbH-Anteile, Hofgrundstück, Erbfolge und drei Registerrückfragen** (`notariat-alltag-waldwinkel-gmbh-immobilien-erbfall`) | [Gesamt-PDF lesen](../testakten/notariat-alltag-waldwinkel-gmbh-immobilien-erbfall/gesamt-pdf/notariat-alltag-waldwinkel-gmbh-immobilien-erbfall_gesamt.pdf) | [`testakte-notariat-alltag-waldwinkel-gmbh-immobilien-erbfall.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-notariat-alltag-waldwinkel-gmbh-immobilien-erbfall.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für Notarrecht: BNotO, BeurkG, DONot, Dienstaufsicht, Urkundspflichten, Neutralität, Verwahrung, Amtspflichten, Vertreter/Verwalter, Disziplinarverfahren und notarielle Berufspraxis.

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

Automatisch generierte Komplett-Liste aller 50 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `amtsenthebung-vermoegensverfall` | Amtsenthebung Vermoegensverfall: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `belehrungspflicht-verbraucher-beurkundung` | Belehrungspflicht Verbraucher Beurkundung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `berufshaftpflicht-berufspflichtverletzung` | Berufshaftpflicht Berufspflichtverletzung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `berufsrecht-notare-kaltstart-routing` | Allgemeiner Kaltstart und Routing: vertiefter Berufsrechts-Skill für Notare; führt vom ersten Satz oder Dokument in den richtigen Arbeitsmodus, typische Rechtsprechungslinien nur nach Live-Verifikation, Kammerpraxis, Verteidigung und näc... |
| `beurkundung-ausland-beurkundungsabbruch` | Beurkundung Ausland Beurkundungsabbruch: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `datenraum-dokumentenintake-aktenlog` | Datenraum Dokumentenintake Aktenlog: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `datenschutzpanne-notariat` | Datenschutzpanne Notariat: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `datenschutzpanne-notariat-dienstaufsicht` | Datenschutzpanne Notariat Dienstaufsicht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fernbeglaubigung-videoverfahren` | Fernbeglaubigung Videoverfahren: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fernbeglaubigung-videoverfahren-02` | Fernbeglaubigung Videoverfahren 02: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `geldwaesche-kyc-homeoffice-honorar-gebuehren` | Geldwaesche KYC Homeoffice Honorar Gebuehren: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `geldwaesche-sanktionslisten-haftpflicht` | Geldwaesche Sanktionslisten Haftpflicht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `grundschuld-sicherungszweck-haftpflicht` | Grundschuld Sicherungszweck Haftpflicht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `it-cloud-kammeraufsicht-ruege` | IT Cloud Kammeraufsicht Ruege: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ki-notariat-kollegialitaet-kammerantwort` | KI Notariat Kollegialitaet Kammerantwort: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kostenrechnung-gnotkg-nebentaetigkeit` | Kostenrechnung Gnotkg Nebentaetigkeit: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `mandatsannahme-mandatsbeendigung-mitarbeiter` | Mandatsannahme Mandatsbeendigung Mitarbeiter: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notar-gesellschafterliste-register` | Notar Gesellschafterliste Register: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notaranderkonto-auszahlungsreife` | Notaranderkonto Auszahlungsreife: bündelt 9 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-amtsenthebung-vermoegensverfall` | Notare: amtsenthebung vermögensverfall - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-anderkonto-verwahrung-faktenmatrix` | Notare: anderkonto und verwahrung - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-auszahlungsanweisung-faktenmatrix` | Notare: auszahlungsanweisung konflikt - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-belehrungspflicht-verbraucher` | Belehrungspflicht Verbraucher: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-belehrungspflicht-verbraucher-faktenma` | Notare: belehrungspflicht und verbraucher - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-beurkundung-ausland-faktenmatrix` | Notare: beurkundung im ausland bezug - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-beurkundungsabbruch-faktenmatrix` | Notare: beurkundungsabbruch - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-beurkundungsverfahren-vollmacht` | Notare: beurkundungsverfahren vollmacht - Kaltstart mit Faktenmatrix, Risikoampel und fehlenden Unterlagen; mit Live-Normencheck, Kammerlogik, Verhältnismäßigkeit, Belegplan und nächstem Schritt. |
| `notare-datenschutzpanne-notariat` | Datenschutzpanne Notariat: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-dienstaufsicht-beschwerde` | Dienstaufsicht Beschwerde: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-fernbeglaubigung-videoverfahren` | Fernbeglaubigung Videoverfahren: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-grundschuld-sicherungszweck` | Grundschuld Sicherungszweck: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-handelsregisteranmeldung-fehler` | Handelsregisteranmeldung Fehler: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-kollegialitaet-faktenma-kostenrechnung` | Kollegialitaet Faktenma Kostenrechnung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-kostenrechnung-gnotkg-beschwerde` | Kostenrechnung Gnotkg Beschwerde: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-notarvertretung-notariatsverwalter` | Notarvertretung Notariatsverwalter: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-rechtsmittel-dienstaufsicht` | Rechtsmittel Dienstaufsicht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-umwandlung-registersperre` | Umwandlung Registersperre: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-urkundensammlung-verwahrung` | Urkundensammlung Verwahrung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notare-werbung-protokoll-nachbereitung` | Werbung Protokoll Nachbereitung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `notarielle-verwahrung-notarkammer-anfrage` | Notarielle Verwahrung Notarkammer Anfrage: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `quellen-rechtsprechungscheck-berufsgericht` | Quellen Rechtsprechungscheck Berufsgericht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `share-deal-umwandlung-registersperre` | Share Deal Umwandlung Registersperre: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `unparteilichkeit-familiengesellschaft` | Unparteilichkeit Familiengesellschaft: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `urkundenrolle-fehler-werbung-amtsbezeichnung` | Urkundenrolle Fehler Werbung Amtsbezeichnung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `urkundensammlung-verwahrung` | Urkundensammlung Verwahrung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vermerk-mustertext-sitzungs` | Vermerk Mustertext Sitzungs: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verschwiegenheit-datenraum-verwahrungsanzeige` | Verschwiegenheit Datenraum Verwahrungsanzeige: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verschwiegenheit-geheimnisschutz-werbung` | Verschwiegenheit Geheimnisschutz Werbung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verwahrungsanzeige-gnotkg` | Verwahrungsanzeige Gnotkg: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `werbung-amtsbezeichnung-amtsenthebung` | Werbung Amtsbezeichnung Amtsenthebung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
