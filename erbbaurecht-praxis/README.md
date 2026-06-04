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
| `erbbaurecht-allgemeiner-kaltstart` | Führt durch Grundstück, Erbbauberechtigte, Eigentümer, Laufzeit, Bauwerk, Erbbauzins, Heimfall, Finanzierung, Zustimmung und Grundbuchvollzug. |
| `erbbaurecht-qualitygate-vertrag` | Checkt, ob ein Entwurf investierbar, vollziehbar, finanzierbar und konfliktfest ist. |
| `kompendium-01-rechtsprechung-erbba-bis-erbbaurecht-fristen` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 01; bündelt 2 frühere Spezialskills (rechtsprechung-erbbaurecht-live-verifizieren, erbbaurecht-fristen-und-reminder) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemus... |
| `kompendium-02-heimfall-gruende-und-bis-erbbaurecht-indexkla` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 02; bündelt 2 frühere Spezialskills (heimfall-gruende-und-verfahren, erbbaurecht-indexklausel-inflation) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-03-erbbaurecht-verkauf-bis-erbbaurechtsvertrag` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 03; bündelt 2 frühere Spezialskills (erbbaurecht-verkauf-spa-klauseln, erbbaurechtsvertrag-pflichtinhalt) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-04-erbbaurecht-steuern-bis-entschaedigung-bei-h` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 04; bündelt 2 frühere Spezialskills (erbbaurecht-steuern-und-grunderwerbsteuer, entschaedigung-bei-heimfall-und-ablauf) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabe... |
| `kompendium-05-erbbau-beschwerde-gr-bis-erbbaugrundbuch-lese` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 05; bündelt 2 frühere Spezialskills (erbbau-beschwerde-grundbuchamt, erbbaugrundbuch-lesen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-06-erbbaurecht-ablauf-l-bis-erbbaurecht-aktenstr` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 06; bündelt 2 frühere Spezialskills (erbbaurecht-ablauf-laufzeitende-exitplan, erbbaurecht-aktenstruktur) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-07-erbbaurecht-altlaste-bis-erbbaurecht-betreibe` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 07; bündelt 2 frühere Spezialskills (erbbaurecht-altlasten-und-rueckbau, erbbaurecht-betreiberwechsel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-08-erbbaurecht-change-o-bis-erbbaurecht-dinglich` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 08; bündelt 2 frühere Spezialskills (erbbaurecht-change-of-control-bei-erbbauberechtigtem, erbbaurecht-dingliche-vorkaufsrechte) und bewahrt deren Workflows, Normanker, Prüfprogramme un... |
| `kompendium-09-erbbaurecht-erbbauzi-bis-erbbaurecht-gewerbep` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 09; bündelt 2 frühere Spezialskills (erbbaurecht-erbbauzinsrang-vor-finanzierungsbank, erbbaurecht-gewerbepark) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-10-erbbaurecht-instandh-bis-erbbaurecht-investor` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 10; bündelt 2 frühere Spezialskills (erbbaurecht-instandhaltung-versicherung-betriebspflichten, erbbaurecht-investoren-q-and-a) und bewahrt deren Workflows, Normanker, Prüfprogramme und... |
| `kompendium-11-erbbaurecht-kauf-und-bis-erbbaurecht-kita-soz` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 11; bündelt 2 frühere Spezialskills (erbbaurecht-kauf-und-due-diligence, erbbaurecht-kita-sozialimmobilie) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-12-erbbaurecht-kommunal-bis-erbbaurecht-mandante` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 12; bündelt 2 frühere Spezialskills (erbbaurecht-kommunale-beschlussvorlage, erbbaurecht-mandantenbrief) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-13-erbbaurecht-nachhalt-bis-erbbaurecht-notar-un` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 13; bündelt 2 frühere Spezialskills (erbbaurecht-nachhaltigkeit-und-baupflicht, erbbaurecht-notar-und-grundbuchkosten) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabem... |
| `kompendium-14-erbbaurecht-nutzungs-bis-erbbaurecht-rangruec` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 14; bündelt 2 frühere Spezialskills (erbbaurecht-nutzungszweckwechsel-wohnen-gewerbe-sozial, erbbaurecht-rangruecktritt-bank) und bewahrt deren Workflows, Normanker, Prüfprogramme und A... |
| `kompendium-15-erbbaurecht-rueckbau-bis-erbbaurecht-schieds` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 15; bündelt 2 frühere Spezialskills (erbbaurecht-rueckbau-am-laufzeitende, erbbaurecht-schieds-und-gerichtsstand) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-16-erbbaurecht-sicherhe-bis-erbbaurecht-teilerbb` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 16; bündelt 2 frühere Spezialskills (erbbaurecht-sicherheiten-buergschaft-depot-lastschrift, erbbaurecht-teilerbbaurecht-und-aufteilung) und bewahrt deren Workflows, Normanker, Prüfprog... |
| `kompendium-17-erbbaurecht-und-phot-bis-erbbaurecht-untererb` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 17; bündelt 2 frühere Spezialskills (erbbaurecht-und-photovoltaik, erbbaurecht-untererbbaurecht-und-weitergabe) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-18-erbbaurecht-verjaehr-bis-erbbaurecht-vorlage` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (erbbaurecht-verjaehrung-verwirkung-duldung, erbbaurecht-vorlage-zustimmungsantrag) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabe... |
| `kompendium-19-erbbaurecht-vs-eigen-bis-erbbauzins-rueckstan` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 19; bündelt 2 frühere Spezialskills (erbbaurecht-vs-eigentum-vs-miete, erbbauzins-rueckstand-mahnung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-20-erbbauzins-struktur-bis-erbbauzinsanpassung` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 20; bündelt 2 frühere Spezialskills (erbbauzins-struktur-und-reallast, erbbauzinsanpassung-paragraph-9a) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-21-finanzierung-erbbaur-bis-gemeinde-kirche-stif` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (finanzierung-erbbaurecht-bankfaehigkeit, gemeinde-kirche-stiftung-als-eigentuemer) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabe... |
| `kompendium-22-heimfall-verteidigun-bis-insolvenz-erbbaubere` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (heimfall-verteidigung, insolvenz-erbbauberechtigter) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-23-laufzeit-verlaengeru-bis-wohnungs-erbbaurecht` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 23; bündelt 2 frühere Spezialskills (laufzeit-verlaengerung-und-neubestellung, wohnungs-erbbaurecht-und-weg) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-24-zustimmung-veraeusse-bis-zwangsversteigerung` | erbbaurecht-praxis: Konsolidiertes Skill-Kompendium 24; bündelt 2 frühere Spezialskills (zustimmung-veraeusserung-belastung, zwangsversteigerung-erbbaurecht) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
