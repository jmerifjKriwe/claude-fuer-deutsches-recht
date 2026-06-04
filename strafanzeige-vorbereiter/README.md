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

Automatisch generierte Komplett-Liste aller 56 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anzeige-akteneinsicht-verletzter-406e` | Akteneinsicht für Verletzte und ihre Anwälte: Voraussetzungen, Schutzinteressen, Datenschutz und Taktik. |
| `anzeige-allgemeiner-kaltstart` | Geführter Einstieg für Strafanzeigen: Sachverhalt, Beweise, Straftatverdacht, Strafantrag, Risiken falscher Verdächtigung, Alternativen und anwaltliche Eskalationsschwelle. |
| `anzeige-anfangsverdacht-152-160-stpo` | Anfangsverdacht strukturieren: zureichende tatsächliche Anhaltspunkte, Ermittlungsauftrag der StA, keine bloße Spekulation. |
| `anzeige-anlagenverzeichnis-hashlog` | Anlagen zu Strafanzeigen: Nummerierung, Hashwerte, Originale, Kopien, Versandnachweis und digitale Kette. |
| `anzeige-antragsdelikte-77b-frist` | Strafantragsfrist und Antragsberechtigung bei Beleidigung, Hausfriedensbruch, einfacher Körperverletzung und weiteren Antragsdelikten. |
| `anzeige-anwalt-einschalten-schwelle` | Schwellen für anwaltliche Hilfe: eigene Beteiligung, Wirtschaftsstrafrecht, Sexual-/Gewaltdelikte, Berufsgeheimnisse, Unternehmen, Presse. |
| `anzeige-arbeitsplatz-sexuelle-belaestigung` | Arbeitsplatzvorfälle: strafrechtliche Anzeige, AGG/Arbeitsrecht, Beweise, Schutz, interne Untersuchung und Betroffenenrechte. |
| `anzeige-bankrott-283` | Bankrott und Buchführungsdelikte: Vermögensverschiebung, Buchführung, Krise, Gläubigerbenachteiligung und Insolvenzakten. |
| `anzeige-bedrohung-241` | Bedrohung anzeigen: Inhalt, Ernstlichkeit, Adressat, Beweise, Schutzmaßnahmen. |
| `anzeige-beleidigung-185-194` | Beleidigung anzeigen: Kontext, Meinungsfreiheit, Strafantrag, Beweise, Plattform/Arbeitsplatz. |
| `anzeige-betrug-263` | Betrugsanzeige: Täuschung, Irrtum, Vermögensverfügung, Schaden, Vorsatz, Belege und zivilrechtliche Parallelspur. |
| `anzeige-beweismatrix-tatsachen-meinungen` | Ordnet jedes Element der Anzeige nach Tatsachenwissen, Beleg, Zeuge, Dokument, Meinung und Vermutung. |
| `anzeige-chatverlaeufe-emails-header` | Chatverläufe, EML-Dateien, E-Mail-Header, Messenger-Screenshots, Export und Kontext sichern. |
| `anzeige-compliance-whistleblower-hinschg` | Hinweisgebermeldung, interne Stelle, externe Meldung, Strafanzeige und Schutz vor Repressalien koordinieren. |
| `anzeige-computerbetrug-phishing` | Computerbetrug/Phishing anzeigen: Zahlungsdaten, TAN, Social Engineering, Bankkommunikation, Logs und Sofortmaßnahmen. |
| `anzeige-datenstraftaten-202a-303a` | Ausspähen, Abfangen, Datenveränderung, Computersabotage: technische Beweise, Logs, Forensik und ZAC. |
| `anzeige-diebstahl-unterschlagung` | Diebstahl/Unterschlagung anzeigen: Gewahrsam, Eigentum, Wegnahme, Zueignung, Beweise, Herausgabeverlangen. |
| `anzeige-druckmittel-verbot-noetigung` | Prüft, ob Drohung mit Strafanzeige oder Anzeige selbst als unzulässiges Druckmittel/Nötigung wirken kann. |
| `anzeige-falsche-verdaechtigung-164` | Warn- und Prüfskill zu § 164 StGB: niemanden sicher beschuldigen, wenn nur Verdachtsmomente oder Hörensagen vorliegen. |
| `anzeige-gegenanzeige-risiko` | Risiko der Gegenanzeige wegen falscher Verdächtigung, Verleumdung, Nötigung, Datenschutzverstoß oder Prozessbetrug. |
| `anzeige-geldwaesche-261` | Geldwäscheverdacht: Tatertrag, Verschleierung, Transaktionen, GwG-Verdachtsmeldung vs Strafanzeige. |
| `anzeige-geschgehg-23-geheimnisverrat` | Geschäftsgeheimnis-Strafanzeige: Geheimnisqualität, angemessene Geheimhaltungsmaßnahmen, Erlangen/Nutzen/Offenlegen, Strafantrag. |
| `anzeige-haeusliche-gewalt-gewschg` | Strafanzeige bei häuslicher Gewalt plus Schutzanordnung, Beweissicherung, medizinische Dokumentation und Sicherheitsplan. |
| `anzeige-hausfriedensbruch-123` | Hausfriedensbruch anzeigen: befriedetes Besitztum, Wohnung/Geschäft, Aufforderung zu gehen, Strafantrag. |
| `anzeige-insolvenzverschleppung-15a` | Insolvenzverschleppung anzeigen: Organstellung, Zahlungsunfähigkeit/Überschuldung, Fristen, Gläubigerschaden und Belege. |
| `anzeige-international-eu-158-3` | Internationale Sachverhalte: Tatort, Zuständigkeit, Europol/Interpol nicht direkt, ausländische Behörden, Übersetzungen und Beweise. |
| `anzeige-klageerzwingung-172-stpo` | Nach Einstellung: Beschwerde, Klageerzwingung, Fristen, Verletztenstellung und anwaltliche Schwelle. |
| `anzeige-koerperverletzung-223-230` | Körperverletzung: Verletzung, Arztbericht, Fotos, Zeugen, Strafantrag bei § 223 und besonderes öffentliches Interesse. |
| `anzeige-korruption-299-331ff` | Korruptionsanzeige: Bestechlichkeit/Bestechung im geschäftlichen Verkehr oder Amt, Vorteil, Unrechtsvereinbarung, Belege, Selbstbelastung. |
| `anzeige-kreditgefaehrdung-824-bgb` | Zivilrechtliches Haftungsrisiko bei Behauptungen über Insolvenz, Betrug, Zahlungsunfähigkeit oder Unzuverlässigkeit. |
| `anzeige-minderjaehrige-schule` | Strafanzeige bei Minderjährigen/Schule: Jugendstrafrecht, Schutz, Schulrecht, Eltern, Jugendamt und Deeskalation. |
| `anzeige-muster-strafanzeige-generator` | Erzeugt eine nüchterne Strafanzeige mit optionalem Strafantrag, Anlagen, Beweismatrix und Risikoformulierungen. |
| `anzeige-nicht-anzeigen-redteam` | Red-Team prüft, ob eine Strafanzeige unnötig, riskant, zivilrechtlich kontraproduktiv oder straf-/haftungsrechtlich gefährlich wäre. |
| `anzeige-noetigung-240` | Nötigung prüfen: Gewalt/Drohung, empfindliches Übel, Verwerflichkeit, legitime Anzeigeandrohung vs. Missbrauch. |
| `anzeige-notruf-akut-gefahr` | Akute Gefahr, laufende Tat, Selbst-/Fremdgefährdung: Sofort Polizei/112/110 statt Entwurf. |
| `anzeige-online-plattform-screenshots` | Screenshots, URLs, Zeitstempel, Accountdaten, Plattformmeldungen und Löschrisiko beweissicher sichern. |
| `anzeige-onlinewache-vs-staatsanwaltschaft` | Adressat und Form: Onlinewache, Polizeidienststelle, Staatsanwaltschaft, Spezialdienststelle Cybercrime, Zoll oder Finanzbehörde. |
| `anzeige-opferschutz-nebenklage` | Rechte Verletzter: Nebenklage, psychosoziale Prozessbegleitung, Adhäsion, Schutzanordnung, Akteneinsicht. |
| `anzeige-rechtsfolgen-und-zivilstrategie` | Strafanzeige mit Zivilrecht koordinieren: Schadensersatz, Unterlassung, einstweilige Verfügung, Kündigung, Versicherung, Adhäsion. |
| `anzeige-ruecknahme-einstellung-170-153` | Was nach Anzeige passiert: Einstellung, Rücknahme Strafantrag, Opportunität, Beschwerde, Kommunikation mit StA. |
| `anzeige-sachbeschaedigung-303` | Sachbeschädigung: Beschädigung/Zerstörung/Veränderung, Fotos, Kostenvoranschlag, Strafantrag, Zivilforderung. |
| `anzeige-sachverhalt-ohne-adjektive` | Entfernt Polemik und Rechtswertungen aus Anzeigen; schreibt nüchtern, präzise und beweisnah. |
| `anzeige-stalking-238` | Nachstellung anzeigen: wiederholtes Verhalten, Eignung zur Beeinträchtigung, Dokumentation, Kontaktverbote und Plattformbeweise. |
| `anzeige-steuerhinterziehung-370-ao` | Steuerstraftaten anzeigen oder Selbstbelastung vermeiden: Drittanzeige, Selbstanzeige-Abgrenzung, Belege, Finanzamt/Steufa. |
| `anzeige-strafantrag-form-frist` | Strafantrag richtig stellen, beweisen und Rücknahmefolgen prüfen. |
| `anzeige-strafanzeige-vs-strafantrag-158` | Unterscheidet Strafanzeige, Strafantrag, Dienstaufsichtsbeschwerde, Privatklage und zivilrechtliche Abmahnung. |
| `anzeige-tierschutz-17` | Tierschutzanzeige: erhebliche Schmerzen/Leiden, Rohheit, länger anhaltende Wiederholung, Veterinäramt und Beweise. |
| `anzeige-ueblerede-verleumdung-186-187` | Strafanzeige und Kommunikation so formulieren, dass keine unnötige ehrverletzende Drittverbreitung entsteht. |
| `anzeige-umweltstraftaten-324ff` | Umweltstraftaten anzeigen: Gewässer, Boden, Luft, Abfall, Genehmigungen, Beweise und Umweltbehörde. |
| `anzeige-unternehmen-internal-investigation` | Unternehmensanzeige nach interner Untersuchung: Legal Hold, Mitarbeiterinterviews, Datenschutz, Arbeitsrecht, Beschlagnahmerisiko und Bericht. |
| `anzeige-untreue-266` | Untreue anzeigen: Vermögensbetreuungspflicht, Pflichtverletzung, Vermögensnachteil, Organ-/Mitarbeiterfälle. |
| `anzeige-urheberrecht-markenrecht` | IP-Strafanzeigen bei Urheber-, Marken-, Design- und Patentrechtsverletzungen: Strafantrag, Testkauf, Originalitätsnachweis, Zoll. |
| `anzeige-verkehrsunfall-flucht-142` | Unerlaubtes Entfernen vom Unfallort: Schaden, Wartepflicht, Feststellungen, Dashcam/Zeugen, Selbstmeldung. |
| `anzeige-video-audio-kug-201` | Video-/Audioaufnahmen als Beweis: Recht am Bild, Vertraulichkeit des Wortes, öffentliche Situation, Polizei/Versammlung und Veröffentlichungsverbot. |
| `anzeige-wer-was-wann-wo-wie` | Sachverhaltskern einer Anzeige: chronologisch, nüchtern, belegbar, ohne Polemik. |
| `anzeige-zeugenliste-kontakt` | Zeugen benennen, aber nicht beeinflussen: Kontaktdaten, Wahrnehmung, Reihenfolge und Dokumentation. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
