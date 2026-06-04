# Berichtspflichten-Erlediger

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`berichtspflichten-erlediger`) | [`berichtspflichten-erlediger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/berichtspflichten-erlediger.zip) |

### Demonstrations-Akten

Dieses Plugin hat derzeit keine eigene Demonstrations-Akte. Es arbeitet mit hochgeladenen Statistikschreiben, Portalbelegen, ELSTER-/IDEV-/LUCID-Ausdrucken, Fristenlisten, E-Mails, ERP-/Lohnbuchhaltungsdaten, Umwelt- und Produktnachweisen.

<!-- END plugin-sofort-download-section (autogen) -->

Praxisplugin für mittelständische Betriebe, die ihre Berichtspflichten nicht lieben müssen, sie aber elegant, fristgerecht und belegbar erledigen wollen. Es sammelt Pflichten aus Statistik, Steuer, Sozialversicherung, Umwelt, Produktrecht, Lieferkette, Datenschutz, Arbeitsschutz und Aufsicht in einem operativen Workflow.

## Leitplanke

Das Plugin ist kein Bürokratie-Jubelchor. Es hilft, Berichtspflichten zu vermeiden, wenn sie nicht bestehen, und sie sauber zu erledigen, wenn sie bestehen. Keine freiwillige Übererfüllung, keine Fantasiezahlen, keine Portalabgabe ohne menschliche Freigabe.

## Was dieses Plugin gut kann

- Pflichten schnell identifizieren: Muss ich wirklich melden, an wen, bis wann, mit welchen Daten?
- Fristen, Portale, Rollen, Datenquellen und Versandnachweise in ein Board bringen.
- Meldungen vorbereiten, plausibilisieren, freigeben und dokumentieren.
- Überzogene oder freiwillige Datenanforderungen höflich, aber bestimmt begrenzen.

## Startlogik

Beginne mit dem allgemeinen Kaltstart-Skill. Er fragt Rolle, Ziel, Frist, Unterlagen, Risiken und gewünschten Output ab. Danach werden nur passende Spezial-Skills vorgeschlagen.

## Quellenhygiene

Normtexte werden aus amtlichen Quellen geprüft. Rechtsprechung wird nur mit Gericht, Datum, Aktenzeichen und frei zugänglicher Quelle verwendet. Keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 21 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `bericht-allgemeiner-kaltstart` | Einstieg für mittelständische Betriebe: Berichtspflichten, Statistikmeldungen, Portale, Fristen, Zuständigkeiten, Datenquellen und Vermeidungs-/Vereinfachungsoptionen schnell sortieren. |
| `bericht-statistik-anfrage-redteam` | Amtliche oder quasi-amtliche Datenanforderung kritisch prüfen: Rechtsgrundlage, Umfang, Geheimnisse, Datenschutz, Frist und Antwortstrategie. |
| `kompendium-01-bericht-behoerdenkom-bis-bericht-bussgeld-ver` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (bericht-behoerdenkommunikation-fristverlaengerung, berichtspflichten-register-und-fristenboard, bericht-bussgeld-vermeidung-heilung) und be... |
| `kompendium-02-bericht-ausland-toch-bis-bericht-fuhrpark-tel` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (bericht-ausland-tochter-de-pflichten, bericht-emissionshandel-tehg-dehst, bericht-fuhrpark-telemetrie-datenschutz) und bewahrt deren Workfl... |
| `kompendium-03-bericht-ki-einsatz-a-bis-bericht-nachweisordn` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (bericht-ki-einsatz-ausfuellen-validieren, bericht-lohnsteuer-sozialversicherung-meldungen, bericht-nachweisordner-dokumentenmatrix) und bew... |
| `kompendium-04-bericht-schwerbehind-bis-bericht-wp-stb-koord` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (bericht-schwerbehindertenanzeige-sgb-ix, bericht-verpackg-vollstaendigkeitserklaerung, bericht-wp-stb-koordination) und bewahrt deren Workf... |
| `kompendium-05-bericht-abfallnachwe-bis-bericht-arbeitsschut` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (bericht-abfallnachweis-nachwv-krwg, bericht-api-portal-zugang-rollen, bericht-arbeitsschutz-unterweisung-nachweise) und bewahrt deren Workf... |
| `kompendium-06-bericht-arbeitsunfal-bis-bericht-auskunftspfl` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (bericht-arbeitsunfall-dguv, bericht-audit-trail-freigabe, bericht-auskunftspflicht-bstatg-15) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-07-bericht-aussenhandel-bis-bericht-baugenehmigu` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (bericht-aussenhandel-intrastat-ahstatg, bericht-battg-batterieregister-mengen, bericht-baugenehmigung-baustatistik) und bewahrt deren Workf... |
| `kompendium-08-bericht-bauwirtschaf-bis-bericht-bundesbank-a` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (bericht-bauwirtschaft-soka-bau, bericht-behg-brennstoffemissionen, bericht-bundesbank-awv-z4-z5) und bewahrt deren Workflows, Normanker, Pr... |
| `kompendium-09-bericht-chemikalien-bis-bericht-csrd-esrs-la` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (bericht-chemikalien-reach-clp, bericht-csddd-vorschau-lieferkette, bericht-csrd-esrs-lagebericht) und bewahrt deren Workflows, Normanker, P... |
| `kompendium-10-bericht-datenminimie-bis-bericht-elektrog-ear` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (bericht-datenminimierung-geheimnisschutz, bericht-dsgvo-datenpanne-33-34, bericht-elektrog-ear-mengenmeldung) und bewahrt deren Workflows,... |
| `kompendium-11-bericht-energieaudit-bis-bericht-eudr-entwald` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (bericht-energieaudit-edl-g, bericht-entsendungen-a1-mindestlohn, bericht-eudr-entwaldung-due-diligence) und bewahrt deren Workflows, Norman... |
| `kompendium-12-bericht-gefahrstoffv-bis-bericht-handwerk-gef` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (bericht-gefahrstoffverzeichnis-gefstoffv, bericht-geschaeftsfuehrer-dashboard, bericht-handwerk-gefahrstoffe-asbest) und bewahrt deren Work... |
| `kompendium-13-bericht-hinweisgeber-bis-bericht-immobilien-g` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (bericht-hinweisgeberschutz-jahresreport, bericht-idev-estatistik-core, bericht-immobilien-gebaeudeenergie-geg) und bewahrt deren Workflows,... |
| `kompendium-14-bericht-jahresabschl-bis-bericht-konjunktur-u` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (bericht-jahresabschluss-bundesanzeiger, bericht-keine-pflicht-begruendet-ablehnen, bericht-konjunktur-und-produktionsstatistik) und bewahrt... |
| `kompendium-15-bericht-konzern-mutt-bis-bericht-lksg-bafa-be` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (bericht-konzern-mutter-tochter-matrix, bericht-lebensmittel-haccp-rueckverfolgung, bericht-lksg-bafa-bericht) und bewahrt deren Workflows,... |
| `kompendium-16-bericht-lucid-verpac-bis-bericht-mindestlohnd` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 16; bündelt 3 frühere Spezialskills (bericht-lucid-verpackg-9-10, bericht-maschinen-ce-konformitaetsakte, bericht-mindestlohndokumentation-arbeitszeit) und bewahrt deren Workfl... |
| `kompendium-17-bericht-mutterschutz-bis-bericht-produktsiche` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 17; bündelt 3 frühere Spezialskills (bericht-mutterschutz-gefaehrdungsbeurteilung, bericht-nis2-bsi-incident, bericht-produktsicherheit-rueckruf-market) und bewahrt deren Workf... |
| `kompendium-18-bericht-saisonkalend-bis-bericht-transparenzr` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 18; bündelt 3 frühere Spezialskills (bericht-saisonkalender-mittelstand, bericht-stichprobe-und-befreiung-kleine-unternehmen, bericht-transparenzregister-gwg-ubo) und bewahrt d... |
| `kompendium-19-bericht-trinkwasser-bis-bericht-verdienststa` | berichtspflichten-erlediger: Konsolidiertes Skill-Kompendium 19; bündelt 3 frühere Spezialskills (bericht-trinkwasser-legionellen-meldung, bericht-umsatzsteuer-voranmeldung-elster, bericht-verdienststatistik-verdstatg) und bewahrt deren... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
