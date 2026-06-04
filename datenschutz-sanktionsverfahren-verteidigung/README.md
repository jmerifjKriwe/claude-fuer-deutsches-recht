# Datenschutz-Sanktionsverfahren und Verteidigung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`datenschutz-sanktionsverfahren-verteidigung`) | [`datenschutz-sanktionsverfahren-verteidigung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/datenschutz-sanktionsverfahren-verteidigung.zip) |

Dieses Plugin hat (bewusst) keine eigene Demonstrations-Akte.

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist die Spezialwerkstatt für Mandate, in denen Datenschutzaufsicht nicht mehr nur Beratung ist, sondern Druck macht: Anhörung, Auskunftsverlangen, Art.-58-Anordnung, Bußgeldbescheid, Einspruch, Hauptverhandlung, Rechtsbeschwerde, Verwaltungsgericht und EuGH-Frage. Es ergänzt `datenschutzrecht`, ist aber bewusst eigenständig, weil solche Verfahren prozessual anders funktionieren als AVV, DSFA oder Datenschutzerklärung.

## Wofür es gedacht ist

- Verteidigung gegen DSGVO-Geldbußen nach Art. 83 DSGVO.
- Vertretung im OWiG-Verfahren nach § 41 BDSG, einschließlich Akteneinsicht, Einspruch, Zwischenverfahren, gerichtlicher Hauptverhandlung, Beschlussverfahren und Rechtsbeschwerde.
- Abwehr oder Verhandlung von Aufsichtsmaßnahmen nach Art. 58 Abs. 2 DSGVO: Verwarnung, Anordnung, Löschung, Verarbeitungsstopp, Drittlandtransfer-Stopp, Zwangsmittel und Veröffentlichungsrisiken.
- Verwaltungsgerichtlicher Rechtsschutz nach Art. 78 DSGVO und § 20 BDSG, wenn es nicht um die Geldbuße selbst geht.
- Koordination mit Datenpanne, Art.-82-Schadensersatz, Strafrecht, Geschäftsführung, D&O, Presse und internationalem One-Stop-Shop.

## Der wichtigste erste Satz im Mandat

Nicht sofort "kooperativ" alles erzählen. Erst verstehen, welche Spur läuft. Datenschutzrechtliche Mitwirkung, OWiG-Verteidigung und verwaltungsgerichtlicher Rechtsschutz haben unterschiedliche Regeln. Das Plugin fragt deshalb zuerst:

1. Liegt nur ein Auskunftsverlangen, eine Anhörung, ein Bußgeldbescheid oder eine Art.-58-Anordnung vor?
2. Wer ist Adressat und welche Behörde ist zuständig: Landesaufsicht, BfDI, kirchliche Datenschutzaufsicht oder federführende EU-Aufsicht?
3. Welche Frist läuft und wie wurde zugestellt?
4. Geht es um Geldbuße, Maßnahme, beides oder Folgerisiken?
5. Was ist belegt und was behauptet die Behörde nur?

## Zwei Hauptspuren

| Spur | Typischer Rechtsweg | Typische Arbeit |
| --- | --- | --- |
| **Bußgeld** | Art. 83 DSGVO, § 41 BDSG, OWiG/StPO sinngemäß; Einspruch nach § 67 OWiG; Zuständigkeit nach § 68 OWiG, modifiziert durch § 41 BDSG | Anhörung, Akteneinsicht, Bußgeldbescheid, Einspruch, Zwischenverfahren, Hauptverhandlung, Beschlussverfahren, Rechtsbeschwerde |
| **Aufsichtsmaßnahme** | Art. 58/78 DSGVO, § 20 BDSG, VwGO | Anordnung prüfen, Bestimmtheit/Ermessen/Verhältnismäßigkeit, Anfechtungsklage, Eilrechtsschutz, Umsetzung/Verhandlung |

## Leitentscheidungen und Stand

Stand: Juni 2026. Besonders wichtig sind EuGH, Urteil vom 05.12.2023, C-807/21 (Deutsche Wohnen), und EuGH, Urteil vom 05.12.2023, C-683/21 (Nacionalinis visuomenės sveikatos centras). Die Linie ist: Ein Unternehmen kann unmittelbar Adressat einer DSGVO-Geldbuße sein; die Aufsicht muss nicht zuerst eine natürliche Person identifizieren. Zugleich bleibt Vorsatz oder Fahrlässigkeit erforderlich. Das Plugin behandelt diese Linie als Prüfprogramm, nicht als Freibrief für schematische Unternehmenshaftung.

## Quellenhygiene

Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate. Normen und Rechtsprechung werden vor Ausgabe mit amtlichen oder frei zugänglichen Quellen geprüft, insbesondere:

- DSGVO über EUR-Lex.
- BDSG und OWiG über gesetze-im-internet.de.
- EuGH über CURIA/EUR-Lex.
- EDPB Guidelines 04/2022 über edpb.europa.eu.
- Deutsche Gerichtsentscheidungen nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freier/amtlicher Quelle.

## Typische Outputs

- Behördenpost-Analyse: Was ist das, was droht, welche Frist läuft?
- Akteneinsichtsantrag und fristwahrender Einspruch.
- Stellungnahme vor Bußgeldbescheid.
- Art.-83-Bemessungsgegenrechnung nach EDPB 04/2022.
- Verschuldens- und Organisationsmemo nach EuGH C-807/21/C-683/21.
- Klage-/Eilantragsgerüst gegen Art.-58-Anordnung.
- Terminsmappe für Hauptverhandlung im Bußgeldverfahren.
- Management-Briefing für Vorstand/Geschäftsführung.
- Schlussmemo mit Remediation, Wiedervorlagen und Lessons Learned.

## Gute Startbefehle

```text
/datenschutz-sanktionsverfahren-verteidigung:kaltstart-verfahrensstand-und-mandatsziel
/datenschutz-sanktionsverfahren-verteidigung:bescheid-oder-anhoerung-richtig-lesen
/datenschutz-sanktionsverfahren-verteidigung:akteneinsicht-49-owig-147-stpo
/datenschutz-sanktionsverfahren-verteidigung:zustaendigkeit-amtsgericht-landgericht-41-bdsg
/datenschutz-sanktionsverfahren-verteidigung:art-58-anordnung-verwaltungsakt
/datenschutz-sanktionsverfahren-verteidigung:edpb-04-2022-bemessungsmethodik
```

## Skill-Logik

Die 100 Skills sind nicht als lose Liste gedacht, sondern als Verteidigungsmaschine: Kaltstart, Behördenvorfeld, Bußgeld/OWiG, Art.-83-Bemessung, Verwaltungsgericht, EU-One-Stop-Shop, Beweise/Forensik und Output. Jeder Skill soll die Mandantin handlungsfähiger machen und nicht bloß Normen aufsagen.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kaltstart-verfahrensstand-und-mandatsziel` | Kaltstart Verfahrensstand und Mandatsziel: Anhörung, Bußgeldbescheid, Art.-58-Anordnung, Verwaltungsstreit und Gerichtsphase in zehn Minuten trennen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über §... |
| `kompendium-01-arbeitnehmerdaten-un-bis-einspruch-67-owig-fr` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (arbeitnehmerdaten-und-betriebsrat-im-sanktionsverfahren, beschlussverfahren-72-owig, beschwerde-betroffener-behoerdenverfah... |
| `kompendium-02-fristenzentrale-zust-bis-ki-tools-im-sanktion` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (fristenzentrale-zustellung-und-wiedervorlage, fristverlaengerung-behoerde-ohne-nachteile, grch-verfahrensgrundrechte, ki-to... |
| `kompendium-03-parallelverfahren-ar-bis-sachverstaendige-it` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (parallelverfahren-art-82-massenklagen, parallelverfahren-strafrecht-42-bdsg, rechtsweg-router-bussgeld-verwaltungsgericht-z... |
| `kompendium-04-wiedereinsetzung-nac-bis-aufsichtliche-anordn` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (wiedereinsetzung-nach-fristversaeumnis, zustaendigkeit-amtsgericht-landgericht-41-bdsg, zwischenverfahren-69-owig, aufsicht... |
| `kompendium-05-bussgeldbescheid-65-bis-fruehstellungnahme-v` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (bussgeldbescheid-65-owig-analyse, bussgeldreduzierung-verhandlungspaket, datenpanne-vor-bussgeld-selbstmeldung, fruehstellu... |
| `kompendium-06-kirchliche-datenschu-bis-sanktionsmandat-schl` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (kirchliche-datenschutzaufsicht-sanktionen, massnahmenplan-als-sanktionsminderung, oeffentliche-stellen-bussgeldprivilegien,... |
| `kompendium-07-veroeffentlichung-vo-bis-akteneinsicht-49-owi` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (veroeffentlichung-von-bussgeldentscheidungen, anwesenheit-73-owig-vertretung, one-stop-shop-art-56-60, akteneinsicht-49-owi... |
| `kompendium-08-anhoerung-55-owig-bis-art-83-abs-2-kriteri` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (anhoerung-55-owig, art-58-anordnung-verwaltungsakt, art-78-rechtsschutz-und-betroffenenbeschwerde, art-83-abs-2-kriterien-e... |
| `kompendium-09-aufsicht-in-regulier-bis-auslaendische-mutter` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (aufsicht-in-regulierten-branchen, aufsichtsbehoerden-antwortschreiben, aufsichtsbehoerden-auskunftsverlangen-art-58-1, ausl... |
| `kompendium-10-behoerdenkommunikati-bis-behoerdenvergleich-e` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (behoerdenkommunikation-reputationsschutz, behoerdenstrategie-kooperation-oder-schweigen, behoerdenuntaetigkeit-und-beschwer... |
| `kompendium-11-bescheid-oder-anhoer-bis-beweisrecht-stpo-im` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (bescheid-oder-anhoerung-richtig-lesen, besondere-datenkategorien-art-9, bestimmtheit-und-ermessen-art-58, beweisrecht-stpo-... |
| `kompendium-12-bfdi-vs-landesaufsic-bis-durchsuchung-beschla` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (bfdi-vs-landesaufsicht, datenloeschung-vs-beweissicherung, dokumentenmatrix-akteneinsicht-vorlage-und-luecken, durchsuchung... |
| `kompendium-13-edpb-04-2022-bemessu-bis-einstellung-anregen` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (edpb-04-2022-bemessungsmethodik, edpb-art-65-streitbeilegung, edsa-und-dsk-praxis-livecheck, einstellung-anregen-vor-besche... |
| `kompendium-14-einstweilige-anordnu-bis-gewinnabschoepfung-u` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (einstweilige-anordnung-123-vwgo-datenschutz, eugh-vorlage-art-267, gerichtstermin-sprechzettel, gewinnabschoepfung-und-fina... |
| `kompendium-15-hauptverhandlung-71-bis-irische-dpc-und-deut` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (hauptverhandlung-71-owig, internationale-datenpanne-und-multi-notification, interne-untersuchung-legal-hold, irische-dpc-un... |
| `kompendium-16-kinder-und-schutzbed-bis-loeschkonzept-und-au` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (kinder-und-schutzbeduerftige-betroffene, kosten-auslagen-und-d-und-o-risiko, lieferanten-und-auftragsverarbeiter-regress, l... |
| `kompendium-17-loeschungsanordnung-bis-mandantenreport-regu` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (loeschungsanordnung-und-datenbestand, logfiles-und-technische-beweise, mandanteninterview-ohne-selbstbelastung, mandantenre... |
| `kompendium-18-mehrere-verstoesse-u-bis-normenkollision-gehe` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 18; bündelt 4 frühere Spezialskills (mehrere-verstoesse-und-art-83-3, milderung-durch-compliance-vor-dem-vorfall, milderung-durch-remediation-nach-dem-vorfall,... |
| `kompendium-19-organisationsverschu-bis-public-sector-und-ve` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 19; bündelt 4 frühere Spezialskills (organisationsverschulden-ersteinschaetzung, privilege-und-mandatsgeheimnis, profiling-und-automatisierte-entscheidungen, pu... |
| `kompendium-20-rechtsbeschwerde-79-bis-selbstbelastungsfrei` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 20; bündelt 4 frühere Spezialskills (rechtsbeschwerde-79-owig, schlussmemo-und-lessons-learned, scope-cut-behoerdenfragen-einhegen, selbstbelastungsfreiheit-und... |
| `kompendium-21-staatsanwaltschaft-i-bis-umsatz-und-wirtschaf` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 21; bündelt 4 frühere Spezialskills (staatsanwaltschaft-im-dsgvo-owig, tracking-cookies-und-ttddg-schnittstelle, transferstopp-drittland-art-58, umsatz-und-wirt... |
| `kompendium-22-unternehmensgruppe-u-bis-verhaeltnismaessigke` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 22; bündelt 4 frühere Spezialskills (unternehmensgruppe-und-federfuehrende-aufsicht, untersagung-und-verarbeitungsstopp, unverhaeltnismaessigkeit-und-existenzge... |
| `kompendium-23-verteidigerrolle-dsb-bis-vg-eilrechtsschutz-8` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (verteidigerrolle-dsb-gf-und-externe-berater, verwarnung-art-58-2-b, vg-anfechtungsklage-20-bdsg, vg-eilrechtsschutz-80-5-vw... |
| `kompendium-24-videoueberwachung-un-bis-vorstands-und-gf-bri` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 24; bündelt 4 frühere Spezialskills (videoueberwachung-und-biometrie, vorbelastungen-und-wiederholungstaeter, vorsatz-fahrlaessigkeit-unternehmen, vorstands-und... |
| `kompendium-25-zeugeninterviews-mit-bis-zwangsgeld-und-volls` | datenschutz-sanktionsverfahren-verteidigung: Konsolidiertes Skill-Kompendium 25; bündelt 2 frühere Spezialskills (zeugeninterviews-mitarbeiter, zwangsgeld-und-vollstreckung-aufsicht) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `red-team-vor-jeder-einreichung` | Red Team vor jeder Einreichung: Stellungnahme, Klage und Einspruchsbegründung auf Selbstwidersprüche, Blindzitate und Beweisrisiken prüfen. Normanker: DSGVO Art. 58 und 77-84; BDSG § 41; OWiG §§ 46 und 55 und 66-72; StPO über § 46 OWiG;... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
