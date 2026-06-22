# Coverage Testakten Gerichts- und Staatsanwaltschafts-Plugins

Stand des Testakten-Arbeitslaufs. Bewertet werden zehn Pflichtbestandteile je Akte: README mit Lernzielen, Rubrum, Eingangsschriftsatz, Erwiderung oder Einlassung, Pflicht-Anlagen, Verfuegungs- und Beweisstand, Entscheidungs- oder Verfuegungsentwurf, Streitstoff-Liste, Loesungspfad, Pflichtanker.

Es wurden keine neuen Skills angelegt. Saemtliche Personen, Anschriften und Aktenzeichen in den Akten sind frei erfunden.

## Stand je Plugin

| Plugin | Testakten | Aktenname | Pflichtstruktur | Pflicht-Anker | AZ-Pattern | Lernziele | Streitstoff-Liste | Loesungspfad | ZIP baut | Offene Punkte |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| richter-amtsgericht-zivil | 1 | AG Musterstadt 12 C 145/26 Verkehrsunfall Kreisverkehr | 100 Prozent | ja | ja | ja | ja | ja | ja | Referenz-Exemplar im vollen Pflichtformat |
| richter-landgericht-zivilkammer | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| relationstechnik-zivilrecht | 1 | bisherige Kurzakte | 30 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| richter-familiengericht | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| richter-amtsgericht-straf | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| richter-landgericht-strafkammer | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| richter-arbeitsgericht | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| richter-sozialgericht | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| richter-finanzgericht | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| richter-verwaltungsgericht | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| richter-amtsgericht-handelsregister | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| richter-amtsgericht-insolvenz-restrukturierung | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| richter-bverfg-verfassungsbeschwerden | 1 | bisherige Kurzakte | 20 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| staatsanwaltschaft-amtsanwaltschaft | 1 | bisherige Kurzakte | 25 Prozent | nein | teilweise | nein | nein | nein | ja | auf Pflichtformat auszubauen |
| staatsanwaltschaft-praxis-einstieg | 0 | keine | 0 Prozent | nein | nein | nein | nein | nein | nein | Testakte im Pflichtformat anzulegen |

## Methodik und Hinweise

Das Plugin richter-amtsgericht-zivil traegt die erste vollstaendige Testakte im Pflichtformat als verbindliches Referenz-Exemplar; sie umfasst Rubrum, Klageschrift, Klageerwiderung, vier Anlagen, Hinweis- und Beweisbeschluss, Urteilsentwurf, Streitstoff-Liste mit dreizehn Zeilen, Loesungspfad und Pflichtanker. Alle uebrigen Gerichts- und Staatsanwaltschafts-Plugins tragen bislang die fruehere Kurzakte (ein README mit Sachverhalt und Aufgabe) und sind nach demselben Muster auf das Pflichtformat auszubauen.

Die ZIP-Assets werden im Release-Workflow aus dem jeweiligen testakte-Ordner gebaut; der Lauf des Bundling-Skripts bestaetigt, dass die neue Aktenstruktur korrekt verpackt wird.

## Gesamtcoverage

Vollstaendiges Pflichtformat: ein von fuenfzehn Plugins (rund sieben Prozent). Das Referenz-Exemplar steht; der Ausbau der uebrigen vierzehn Akten auf das Pflichtformat ist der naechste Arbeitsschritt.
