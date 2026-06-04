# Strafanzeige-Vorbereiter

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strafanzeige-vorbereiter`) | [`strafanzeige-vorbereiter.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafanzeige-vorbereiter.zip) |

### Demonstrations-Akten

Dieses Plugin hat derzeit keine eigene Demonstrations-Akte. Es arbeitet mit Sachverhaltsnotizen, Chats, E-Mails, EML-Dateien, Screenshots, Fotos, Videos, Zeugenlisten, Belegen, ärztlichen Unterlagen, Verträgen und vorhandenen Anzeigeentwürfen.

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist ausdrücklich keine Strafanzeigenkanone. Es soll Gerichte und Staatsanwaltschaften nicht mit wütenden, unbelegten Anzeigen fluten und niemanden durch haltlose Vorwürfe unter Druck setzen. Wenn eine Strafanzeige aber nötig ist, führt es zu einem sauberen, nüchternen, beweisnahen Entwurf.

## Leitplanke

Wehe, es werden Dinge behauptet, die nicht stimmen. Das Plugin zwingt zur Trennung von eigener Wahrnehmung, Dokument, Zeuge, Vermutung und rechtlicher Bewertung. Bei eigener Beteiligung, Unternehmensfällen, schweren Gewalt-/Sexualdelikten, Wirtschaftsstrafsachen oder Berufsgeheimnissen: anwaltliche Hilfe einschalten.

## Was dieses Plugin gut kann

- Trennt Strafanzeige, Strafantrag, zivilrechtliche Alternativen und bloße Beschwerde.
- Prüft vorab § 164 StGB, §§ 186/187 StGB, § 824 BGB und Druckmittelrisiken.
- Baut Sachverhalt, Beweismatrix, Anlagenverzeichnis und Strafantragsfristen auf.
- Erzeugt erst am Ende einen Anzeigeentwurf, wenn die Tatsachenbasis trägt.

## Startlogik

Beginne mit dem allgemeinen Kaltstart-Skill. Er fragt Rolle, Ziel, Frist, Unterlagen, Risiken und gewünschten Output ab. Danach werden nur passende Spezial-Skills vorgeschlagen.

## Quellenhygiene

Normtexte werden aus amtlichen Quellen geprüft. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle verwendet. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anzeige-allgemeiner-kaltstart` | Geführter Einstieg für Strafanzeigen: Sachverhalt, Beweise, Straftatverdacht, Strafantrag, Risiken falscher Verdächtigung, Alternativen und anwaltliche Eskalationsschwelle. |
| `anzeige-nicht-anzeigen-redteam` | Red-Team prüft, ob eine Strafanzeige unnötig, riskant, zivilrechtlich kontraproduktiv oder straf-/haftungsrechtlich gefährlich wäre. |
| `kompendium-01-anzeige-antragsdelik-bis-anzeige-strafantrag` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 01; bündelt 2 frühere Spezialskills (anzeige-antragsdelikte-77b-frist, anzeige-strafantrag-form-frist) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-02-anzeige-steuerhinter-bis-anzeige-akteneinsich` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 02; bündelt 2 frühere Spezialskills (anzeige-steuerhinterziehung-370-ao, anzeige-akteneinsicht-verletzter-406e) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemu... |
| `kompendium-03-anzeige-anfangsverda-bis-anzeige-anlagenverze` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 03; bündelt 2 frühere Spezialskills (anzeige-anfangsverdacht-152-160-stpo, anzeige-anlagenverzeichnis-hashlog) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemus... |
| `kompendium-04-anzeige-anwalt-einsc-bis-anzeige-arbeitsplatz` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 04; bündelt 2 frühere Spezialskills (anzeige-anwalt-einschalten-schwelle, anzeige-arbeitsplatz-sexuelle-belaestigung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Aus... |
| `kompendium-05-anzeige-bankrott-283-bis-anzeige-bedrohung-24` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 05; bündelt 2 frühere Spezialskills (anzeige-bankrott-283, anzeige-bedrohung-241) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-06-anzeige-beleidigung-bis-anzeige-betrug-263` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 06; bündelt 2 frühere Spezialskills (anzeige-beleidigung-185-194, anzeige-betrug-263) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-07-anzeige-beweismatrix-bis-anzeige-chatverlaeuf` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 07; bündelt 2 frühere Spezialskills (anzeige-beweismatrix-tatsachen-meinungen, anzeige-chatverlaeufe-emails-header) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausga... |
| `kompendium-08-anzeige-compliance-w-bis-anzeige-computerbetr` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 08; bündelt 2 frühere Spezialskills (anzeige-compliance-whistleblower-hinschg, anzeige-computerbetrug-phishing) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemu... |
| `kompendium-09-anzeige-datenstrafta-bis-anzeige-diebstahl-un` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 09; bündelt 2 frühere Spezialskills (anzeige-datenstraftaten-202a-303a, anzeige-diebstahl-unterschlagung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-10-anzeige-druckmittel-bis-anzeige-falsche-verd` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 10; bündelt 2 frühere Spezialskills (anzeige-druckmittel-verbot-noetigung, anzeige-falsche-verdaechtigung-164) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemus... |
| `kompendium-11-anzeige-gegenanzeige-bis-anzeige-geldwaesche` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 11; bündelt 2 frühere Spezialskills (anzeige-gegenanzeige-risiko, anzeige-geldwaesche-261) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-12-anzeige-geschgehg-23-bis-anzeige-haeusliche-g` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 12; bündelt 2 frühere Spezialskills (anzeige-geschgehg-23-geheimnisverrat, anzeige-haeusliche-gewalt-gewschg) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-13-anzeige-hausfriedens-bis-anzeige-insolvenzver` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 13; bündelt 2 frühere Spezialskills (anzeige-hausfriedensbruch-123, anzeige-insolvenzverschleppung-15a) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-14-anzeige-internationa-bis-anzeige-klageerzwing` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 14; bündelt 2 frühere Spezialskills (anzeige-international-eu-158-3, anzeige-klageerzwingung-172-stpo) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-15-anzeige-koerperverle-bis-anzeige-korruption-2` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 15; bündelt 2 frühere Spezialskills (anzeige-koerperverletzung-223-230, anzeige-korruption-299-331ff) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-16-anzeige-kreditgefaeh-bis-anzeige-minderjaehri` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 16; bündelt 2 frühere Spezialskills (anzeige-kreditgefaehrdung-824-bgb, anzeige-minderjaehrige-schule) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-17-anzeige-muster-straf-bis-anzeige-noetigung-24` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 17; bündelt 2 frühere Spezialskills (anzeige-muster-strafanzeige-generator, anzeige-noetigung-240) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-18-anzeige-notruf-akut-bis-anzeige-online-platt` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (anzeige-notruf-akut-gefahr, anzeige-online-plattform-screenshots) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-19-anzeige-onlinewache-bis-anzeige-opferschutz` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 19; bündelt 2 frühere Spezialskills (anzeige-onlinewache-vs-staatsanwaltschaft, anzeige-opferschutz-nebenklage) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemu... |
| `kompendium-20-anzeige-rechtsfolgen-bis-anzeige-ruecknahme-e` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 20; bündelt 2 frühere Spezialskills (anzeige-rechtsfolgen-und-zivilstrategie, anzeige-ruecknahme-einstellung-170-153) und bewahrt deren Workflows, Normanker, Prüfprogramme und Aus... |
| `kompendium-21-anzeige-sachbeschaed-bis-anzeige-sachverhalt` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 21; bündelt 2 frühere Spezialskills (anzeige-sachbeschaedigung-303, anzeige-sachverhalt-ohne-adjektive) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-22-anzeige-stalking-238-bis-anzeige-strafanzeige` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (anzeige-stalking-238, anzeige-strafanzeige-vs-strafantrag-158) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-23-anzeige-tierschutz-1-bis-anzeige-ueblerede-ve` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 23; bündelt 2 frühere Spezialskills (anzeige-tierschutz-17, anzeige-ueblerede-verleumdung-186-187) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-24-anzeige-umweltstraft-bis-anzeige-unternehmen` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 24; bündelt 2 frühere Spezialskills (anzeige-umweltstraftaten-324ff, anzeige-unternehmen-internal-investigation) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabem... |
| `kompendium-25-anzeige-untreue-266-bis-anzeige-urheberrecht` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 25; bündelt 2 frühere Spezialskills (anzeige-untreue-266, anzeige-urheberrecht-markenrecht) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-26-anzeige-verkehrsunfa-bis-anzeige-video-audio` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 26; bündelt 2 frühere Spezialskills (anzeige-verkehrsunfall-flucht-142, anzeige-video-audio-kug-201) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `kompendium-27-anzeige-wer-was-wann-bis-anzeige-zeugenliste` | strafanzeige-vorbereiter: Konsolidiertes Skill-Kompendium 27; bündelt 2 frühere Spezialskills (anzeige-wer-was-wann-wo-wie, anzeige-zeugenliste-kontakt) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
