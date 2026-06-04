# Telekommunikationsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`telekommunikationsrecht`) | [`telekommunikationsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/telekommunikationsrecht.zip) |

### Demonstrations-Akten

Dieses Plugin hat derzeit keine eigene Demonstrations-Akte. Es arbeitet mit Verträgen, Rechnungen, Messprotokollen, Anbieterwechselakten, Bescheiden der Bundesnetzagentur, Verwaltungsakten und technischen Unterlagen.

<!-- END plugin-sofort-download-section (autogen) -->

Großes Arbeitsplugin für Telekommunikationsrecht: vom defekten Internetanschluss bis zur Beschlusskammer der Bundesnetzagentur, vom Glasfaserausbau bis zu Frequenzen, Nummerierung, Netzneutralität, Sicherheitsvorfall und Sonderkartellrecht.

## Was dieses Plugin gut kann

- Verbraucher- und Geschäftskundenfälle zu Anschluss, Störung, Anbieterwechsel, Rufnummer und SLA sauber dokumentieren.
- BNetzA-Verfahren mit Akteneinsicht, Anhörung, Geschäftsgeheimnissen, Stellungnahmen und Eilrechtsschutz führen.
- Marktanalyse, Zugang, Entgelt, Frequenzen, Nummerierung, Open Access und Missbrauchsaufsicht fachlich trennen.
- Datenschutz, Standort-/Verkehrsdaten, IT-Sicherheit, NIS2/BSI und Notfallkommunikation integrieren.

## Startlogik

Beginne mit `tk-allgemeiner-kaltstart`. Der Skill trennt Verbraucherstreit, Geschäftskunden-SLA, Netzbetrieb, Frequenz, Nummerierung, Marktmacht, Infrastruktur, Datenschutz/Sicherheit und BNetzA-Verfahren. Danach wird nur gezielt in Spezial-Skills verzweigt.

## Rechtsweg-Kompass

Telekommunikationsrecht ist gemischt: Vertragliche Ansprüche laufen regelmäßig zivilrechtlich; regulierungsrechtliche Maßnahmen der Bundesnetzagentur sind öffentlich-rechtlich; Missbrauchs- und Wettbewerbsfragen können zivil-, verwaltungs- oder kartellrechtliche Schnittstellen haben. Deshalb prüft jeder streitige Skill zuerst Bescheid, Anspruch, Norm und Rechtsbehelfsbelehrung.

## Quellenhygiene

TKG, Nebengesetze, EU Electronic Communications Code, BNetzA-Verfügungen und Verwaltungspraxis werden live geprüft. Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 57 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `tk-abhoerschnittstellen-sicherheitsbehoerden` | TK-Überwachung, Schnittstellen, Auskunftsersuchen, Bestandsdaten, Verkehrsdaten, Strafverfolgung und Geheimnisschutz. |
| `tk-abmahnung-uwg-tkg` | Abmahnungen bei TK-Marketing, Preiswerbung, Rufnummernmissbrauch, Vergleichsportalen und Informationspflichten. |
| `tk-allgemeiner-kaltstart` | Allgemeiner Einstieg ins Telekommunikationsrecht: Anschluss, Internet, Mobilfunk, Anbieterwechsel, BNetzA-Bescheid, Frequenz, Nummerierung, Marktmacht, Datenschutz und Sicherheitsvorfall sortieren. |
| `tk-anbieterwechsel-rufnummernmitnahme` | Anbieterwechsel, Versorgungslücke, Rufnummernportierung, Entschädigung, Weiterversorgungspflicht und BNetzA-Beschwerde. |
| `tk-anschlussbereitstellung-verzug` | Bereitstellung von Festnetz-, Glasfaser-, Mobilfunk- oder Business-Anschluss: Terminversäumnis, Verzug, Entschädigung, Rücktritt, Ersatzlösung und Beweis. |
| `tk-bauarbeiten-kabelschaden` | Kabelschäden: Leitungsauskunft, Verkehrssicherung, Tiefbau, Schadensersatz, Betriebsunterbrechung und Beweissicherung. |
| `tk-behoerdenkommunikation-kooperationsstrategie` | Kommunikationsstrategie gegenüber der Bundesnetzagentur: kooperativ, präzise, aktenfest, geheimnisschonend und entscheidungsorientiert. |
| `tk-beschwerde-dashboard-bnetza` | Dashboard für Massenbeschwerden: Anbieterwechsel, Störung, Rufnummer, Werbeanruf, Rechnung, Missbrauch und Fristen. |
| `tk-beweisplan-messung-stoerung-protokoll` | Technischer Beweisplan für TK-Streit: Breitbandmessung, Ausfallprotokoll, Routerlogs, Technikertermine, Fotos, Tickets, SLA und Zeugen. |
| `tk-bundesnetzagentur-verfahren-akteneinsicht-fristen` | Verfahren vor der Bundesnetzagentur: Anhörung, Akteneinsicht, Geschäftsgeheimnisse, Beiladung, Fristen, Beschlusskammerlogik und gerichtliche Anschlussstrategie. |
| `tk-callcenter-einwilligung-werbeanrufe` | Telefonwerbung, Einwilligung, Rufnummernanzeige, Dokumentation, Bußgeldrisiko und Callcenter-Verträge. |
| `tk-campusnetze-private-5g` | Campusnetze/private 5G: lokale Frequenzen, Betreiberrolle, Sicherheit, SLA, Industrieanwendung und Drittzugang. |
| `tk-cloud-telefonie-voip-compliance` | Cloud-PBX/VoIP: Notruf, Standort, Datenschutz, Aufzeichnung, Ausfallsicherheit, Rufnummern und internationale Nutzer. |
| `tk-cookies-telemedien-ttdsg-tdddg` | Telemedien-/TK-Schnittstelle: Cookies, Einwilligung, Endgerätezugriff, Consent-Banner und Telekommunikationsdienste. |
| `tk-datacenter-connectivity` | Rechenzentrumskonnektivität: Carrier Meet-Me, Cross-Connects, SLA, Wegerecht im Gebäude, Datenschutz/Sicherheit und Ausfallhaftung. |
| `tk-eilrechtsschutz-bnetza-beschluss` | Eilrechtsschutz bei Frequenz-, Entgelt-, Zugang-, Nummerierungs- oder Missbrauchsmaßnahmen. |
| `tk-entgeltgenehmigung-kostenorientierung` | Entgeltregulierung, Kostenunterlagen, Effizienzmaßstab, Genehmigung, Margin Squeeze und Eilrechtsschutz. |
| `tk-eu-eecc-router` | EU-Router für TK-Recht: Richtlinie (EU) 2018/1972, Verbraucherrechte, Marktregulierung, Nummerierung, Universaldienst, Netzneutralität und nationale Umsetzung im TKG. |
| `tk-frequenznutzung-stoerungen` | Funkstörungen, EMV, Störungsmeldung, Messung, Unterlassung und BNetzA-Eingriff. |
| `tk-frequenzzuteilung-auktionsdesign` | Frequenzzuteilung, Vergabeverfahren, Auktionsdesign, Versorgungsauflagen, Nebenbestimmungen und Rechtsschutz. |
| `tk-glasfaser-hausanschluss-wegerecht` | Glasfaser- und Hausanschlussprojekte: Grundstückszugang, Gebäudenetz, Wegerecht, Gestattung, Wohnungseigentum, Open Access und Baukoordination. |
| `tk-infrastruktursharing-open-access` | Open-Access-Modelle, Infrastruktursharing, Wholesale-Only, Kooperationsverträge, Nichtdiskriminierung und Beihilfe-/Förderschnittstelle. |
| `tk-iot-m2m-sim-karten` | IoT-/M2M-Konnektivität: SIM-Karten, Roaming, Nummerierung, Sicherheit, Datenzugriff, Produkthaftung und Vertragsketten. |
| `tk-kartellrecht-schnittstelle-gwb-eu` | TK-Verträge und Kooperationen mit Kartellrechtsbezug: Open Access, Ausbaukooperation, Exklusivität, Wholesale, Joint Venture. |
| `tk-marktanalyse-betraechtliche-marktmacht` | Marktanalyse, Marktdefinition, SMP/beträchtliche Marktmacht, Konsultation, EU-Abstimmung und Regulierungsverfügung. |
| `tk-meldepflicht-it-sicherheitsvorfall` | Sicherheitsvorfälle bei TK-Anbietern: BNetzA/BSI/DSGVO-Meldungen, Kundenkommunikation, Ursachenanalyse und Abhilfe. |
| `tk-mindestvertragslaufzeit-kuendigung` | TK-Verträge: Mindestlaufzeit, automatische Verlängerung, monatliche Kündbarkeit, Kündigungsbutton/Onlinekündigung, AGB und Nachweis. |
| `tk-missbrauchsaufsicht-sonderkartellrecht` | Missbrauchsaufsicht im TK-Recht: Marktmacht, Diskriminierung, Behinderung, Margin Squeeze, Zugang und Verhältnis zu GWB/AEUV. |
| `tk-mitnutzung-gebaeude-netze` | Mitnutzung von Gebäudenetzen, Leerrohren, Masten, Schächten und passiver Infrastruktur. |
| `tk-netzneutralitaet-zero-rating-throttling` | Netzneutralität: Zero-Rating, Priorisierung, Drosselung, Spezialdienste, Traffic Management und Beschwerde-/Abmahnrisiken. |
| `tk-nis2-kritis-bsi-schnittstelle` | NIS2/KRITIS/BSI-Anforderungen für TK-Unternehmen, Rechenzentren, Managed Services und kritische Kommunikation. |
| `tk-notfall-und-katastrophenkommunikation` | Notfallkommunikation, Resilienz, Priorisierung, Cell Broadcast, Behördenkommunikation und Business Continuity. |
| `tk-notrufpflicht-112` | Notruf 112/110, Standortdaten, Ausfallsicherheit, VoIP, Alarmierung, Unternehmensanschlüsse und Haftungsrisiko. |
| `tk-nummerierung-rufnummernzuteilung` | Rufnummernzuteilung, Nutzung, Entzug, Mehrwertdienste, geografische Nummern, 0800/0900, M2M und Nummernportierung. |
| `tk-open-ran-lieferketten` | Open-RAN-/Netzkomponenten: Lieferkette, Sicherheit, Interoperabilität, Ausfall, Exportkontrolle und kritische Komponenten. |
| `tk-output-beschwerde-antrag-klage` | Formate im Telekommunikationsrecht: BNetzA-Beschwerde, Verbraucher-Schlichtung, verwaltungsrechtlicher Antrag, Widerspruch/Anfechtung, zivilrechtliche Klage und Stellungnahme. |
| `tk-redteam-regulierungsrisiko` | Red-Team für TK-Projekte: Marktmacht, Zugangs-/Entgeltregulierung, Wegerecht, Sicherheit, Datenschutz, BNetzA, Kartellrecht und politische Sichtbarkeit. |
| `tk-routerfreiheit-endgeraete` | Routerfreiheit, Netzabschlusspunkt, Endgerätefreiheit, Providerrouter, Konfigurationsdaten, Glasfaser-ONT und Gewährleistung/Sicherheit. |
| `tk-rufnummernmissbrauch-abschaltung` | Rufnummernmissbrauch, Ping-Anrufe, Spam, Mehrwertdienste, Abschaltung, Rechnungslegungs-/Inkassoverbot und Beschwerde. |
| `tk-satellite-starlink-ntn` | Satelliteninternet/NTN: Frequenzen, Genehmigung, Endgeräte, Verbrauchervertrag, Resilienz und nationale Sicherheitsaspekte. |
| `tk-schlichtung-verbraucher` | Verbraucherschlichtung bei TK-Streit: Voraussetzungen, Antrag, Unterlagen, Hemmung/Fristen, Verhältnis zu Klage und BNetzA-Beschwerde. |
| `tk-sla-business-kunden-ausfall` | Geschäftskunden-SLA: Verfügbarkeit, Reaktions-/Entstörzeiten, Credits, Schadensersatz, Haftungsbegrenzung und Force Majeure. |
| `tk-standardangebot-reference-offer` | Standardangebotspflichten, Prüfung von Klauseln, Änderungsanordnung, Zugangsnachfrage und Nichtdiskriminierung. |
| `tk-stoerung-minderung-ausfallentschaedigung` | Internet-/Telefonstörung: Minderung, Ausfallentschädigung, Entstörungspflichten, Messprotokolle, SLA und Schadensersatz. |
| `tk-streitbeilegung-bnetza` | Streitbeilegung bei Zugang, Mitnutzung, Entgelt, Nummerierung oder Anbieterwechsel mit BNetzA-Beteiligung. |
| `tk-towerco-standortmiete` | Mobilfunkstandorte: Miet-/Gestattungsvertrag, Baurecht, Immissionsschutz, Standortsharing, Rückbau und Eigentümerkonflikt. |
| `tk-traffic-location-data-privacy` | Verkehrsdaten, Standortdaten, Einzelverbindungsnachweis, Abrechnung, Einwilligung, Sicherheit und Löschung. |
| `tk-umzug-vertragsanpassung` | Umzug bei TK-Vertrag: Fortführung, Sonderkündigung, Leistungsfähigkeit am neuen Standort, Glasfaser-/Kabelanschluss und Kosten. |
| `tk-universalservice-mindestversorgung` | Universaldienst/Mindestversorgung mit Telekommunikationsdiensten: Unterversorgung, Anspruch, BNetzA-Verfahren, technische Zumutbarkeit und Alternativen. |
| `tk-verwaltungsrecht-anfechtung-bnetza` | Anfechtung, Verpflichtung oder Eilrechtsschutz gegen BNetzA-Beschlüsse und Nebenbestimmungen. |
| `tk-vorratsdaten-speicherung-eugh-bverfg` | Vorratsdatenspeicherung, Quick Freeze, Sicherheitsbehördenanfragen und EuGH/BVerfG-Linie live prüfen. |
| `tk-wegerecht-oeffentliche-wege` | Wegerecht, Mitverlegung, Baustellenkoordination, Zustimmung, Wiederherstellung und Streit mit Straßenbaulastträgern. |
| `tk-wholesale-reseller-mvno-vertrag` | Wholesale-, Reseller- und MVNO-Verträge: Zugang, SLA, Entgelt, Nummerierung, Kundenschutz, Datenschutz und Exit. |
| `tk-zivilklage-lg-entgelt-schadensersatz` | Zivilrechtliche TK-Klagen: Entgeltforderungen, Rückzahlung, Schadensersatz, SLA, AGB, Minderung und Verbraucher-/Businessstreit. |
| `tk-zugangsregulierung-vorleistung` | Zugang zu Netzen, Vorleistungsprodukten, TAL/Bitstrom, Glasfaser, Nichtdiskriminierung und technische Schnittstellen. |
| `tk-zusammenschaltung-interconnection` | Zusammenschaltung, Terminierung, IP-Interconnection, Qualität, Entgelte und Streitbeilegung. |
| `tk-zustaendigkeits-router-bnetza-vg-lg` | Rechtsweg- und Zuständigkeitsrouter für TK-Streitigkeiten: Verbraucheranspruch, BNetzA-Regulierungsverfahren, zivilrechtlicher Vertrag, verwaltungsgerichtlicher Eilrechtsschutz und Kartell-/Missbrauchsschnittstelle. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
