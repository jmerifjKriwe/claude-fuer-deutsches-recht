# Erbbaurecht Praxis

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`erbbaurecht-praxis`) | [`erbbaurecht-praxis.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/erbbaurecht-praxis.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Lindenwerder Erbbaurecht - Erbbauzins, Heimfall und Kita-Finanzierung** (`erbbaurecht-erbbauzins-heimfall-lindenwerder-2026`) | [Gesamt-PDF lesen](../testakten/erbbaurecht-erbbauzins-heimfall-lindenwerder-2026/gesamt-pdf/erbbaurecht-erbbauzins-heimfall-lindenwerder-2026_gesamt.pdf) | [`testakte-erbbaurecht-erbbauzins-heimfall-lindenwerder-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-erbbaurecht-erbbauzins-heimfall-lindenwerder-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein Spezialplugin für das Recht des Erbbaurechts: vom ersten Vertragsentwurf über Erbbauzins und Heimfall bis zu Finanzierung, Zustimmung, Versteigerung und Erbbaugrundbuch. Es erklärt die Sache auch für Menschen, die sonst nur Eigentum oder Miete kennen.

## Wofür dieses Plugin da ist

Dieses Plugin ist ein Praxiswerkzeug. Es fragt zuerst die Lage ab, baut dann eine Dokumenten- und Vollzugsmatrix und erzeugt schließlich das konkrete Arbeitsprodukt: Nachreichung, Beanstandungsantwort, Beschwerdegerüst, Mandantenbrief, Checkliste, Fristenlog oder Vertrags-/Urkundenreview. Es ersetzt keine Berufsträgerentscheidung, aber es verhindert, dass ein formeller Nachweis, ein Rang, eine Abteilung-II-Belastung oder eine Registerfolge in der Hektik untergeht.

## Kaltstart

Starte mit dem allgemeinen Skill `erbbaurecht-allgemeiner-kaltstart`. Lade danach möglichst den aktuellen Register- oder Grundbuchauszug, das Gerichtsschreiben, die Anmeldung/Bewilligung, den Vertragsentwurf und vorhandene Anlagen hoch. Das Plugin sortiert erst, dann prüft es.

## Quellen- und Halluzinationsschutz

- Normen werden als Prüfanker verwendet, nicht als Schmuck.
- Rechtsprechung wird nur ausgegeben, wenn Gericht, Datum, Aktenzeichen und ein frei zugänglicher Fundlink geprüft sind.
- Unsichere Register-/Grundbuchstände werden nicht geraten; das Plugin fordert aktuelle Auszüge oder Nachweise an.

## Amtliche Startquellen

- [ErbbauRG](https://www.gesetze-im-internet.de/erbbauv/)
- [GBO](https://www.gesetze-im-internet.de/gbo/)
- [GBV](https://www.gesetze-im-internet.de/gbvfg/)
- [BGB Sachenrecht](https://www.gesetze-im-internet.de/bgb/)
- [FamFG](https://www.gesetze-im-internet.de/famfg/)

## Typische Ergebnisse

- Prüfmatrix und Vollzugsfahrplan
- Entwurf für Nachreichung oder Antwort an das Gericht/Amt
- Mandantenbrief in normalem Deutsch
- Fristen- und Ranglog
- Beschwerde- oder Eilrechtsschutz-Skizze
- Liste fehlender Originale, Nachweise und Formmängel

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 26 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ablauf-laufzeitende-erbbaurecht-aktenstruktur` | Ablauf Laufzeitende Erbbaurecht Aktenstruktur: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `altlasten-rueckbau-erbbaurecht` | Altlasten Rueckbau Erbbaurecht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `change-control-dingliche-vorkaufsrechte` | Change Control Dingliche Vorkaufsrechte: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `erbbau-beschwerde-erbbaugrundbuch-lesen` | Erbbau Beschwerde Erbbaugrundbuch Lesen: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `erbbaurecht-kaltstart-routing` | Führt durch Grundstück, Erbbauberechtigte, Eigentümer, Laufzeit, Bauwerk, Erbbauzins, Heimfall, Finanzierung, Zustimmung und Grundbuchvollzug. |
| `erbbaurecht-photovoltaik-untererbbaurecht` | Photovoltaik Untererbbaurecht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `erbbaurecht-qualitygate-vertrag` | Checkt, ob ein Entwurf investierbar, vollziehbar, finanzierbar und konfliktfest ist. |
| `erbbauzins-struktur-erbbauzinsanpassung` | Erbbauzins Struktur Erbbauzinsanpassung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `erbbauzinsrang-finanzierungsbank-erbbaurecht` | Erbbauzinsrang Finanzierungsbank Erbbaurecht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `finanzierung-bankfaehigkeit-gemeinde-kirche` | Finanzierung Bankfaehigkeit Gemeinde Kirche: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `heimfall-gruende-indexklausel-inflation` | Heimfall Gruende Indexklausel Inflation: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `heimfall-verteidigung-insolvenz` | Heimfall Verteidigung Insolvenz: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `instandhaltung-versicherung-investoren-q` | Instandhaltung Versicherung Investoren Q: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kauf-due-kita-sozialimmobilie` | Kauf DUE Kita Sozialimmobilie: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kommunale-beschlussvorlage-erbbaurecht` | Kommunale Beschlussvorlage Erbbaurecht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `laufzeit-verlaengerung-wohnungs-weg` | Laufzeit Verlaengerung Wohnungs WEG: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `nachhaltigkeit-baupflicht-notar` | Nachhaltigkeit Baupflicht Notar: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `nutzungszweckwechsel-wohnen-rangruecktritt` | Nutzungszweckwechsel Wohnen Rangruecktritt: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `rechtsprechung-live-erbbaurecht-reminder` | Rechtsprechung Live Erbbaurecht Reminder: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `rueckbau-am-schieds-gerichtsstand` | Rueckbau AM Schieds Gerichtsstand: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `sicherheiten-buergschaft-teilerbbaurecht` | Sicherheiten Buergschaft Teilerbbaurecht: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `steuern-grunderwerbsteuer-entschaedigung` | Steuern Grunderwerbsteuer Entschaedigung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verjaehrung-verwirkung-vorlage` | Verjaehrung Verwirkung Vorlage: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkauf-spa-erbbaurechtsvertrag-pflichtinhalt` | Verkauf SPA Erbbaurechtsvertrag Pflichtinhalt: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vs-eigentum-erbbauzins-rueckstand` | VS Eigentum Erbbauzins Rueckstand: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `zustimmung-veraeusserung-zwangsversteigerung` | Zustimmung Veraeusserung Zwangsversteigerung: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
