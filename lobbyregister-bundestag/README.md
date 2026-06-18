# Lobbyregister Bundestag

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`lobbyregister-bundestag`) | [`lobbyregister-bundestag.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lobbyregister-bundestag.zip) |
| **Alle Skills als Markdown** | [`lobbyregister-bundestag-skills-markdown.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lobbyregister-bundestag-skills-markdown.zip) |
| **Unified Mini Prompt** (Sparversion bis 7.500 Zeichen) | [`lobbyregister-bundestag-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lobbyregister-bundestag-unified-mini-prompt.md) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Akte Lobbyregister: Bürgerinitiative Waldmoor 2030** (`lobbyregister-buergerinitiative-waldmoor`) | [Gesamt-PDF lesen](../testakten/lobbyregister-buergerinitiative-waldmoor/gesamt-pdf/lobbyregister-buergerinitiative-waldmoor_gesamt.pdf) | [`testakte-lobbyregister-buergerinitiative-waldmoor.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lobbyregister-buergerinitiative-waldmoor.zip) |
| **Akte Lobbyregister: Emerald Liffey Bank plc / Zweigniederlassung Frankfurt** (`lobbyregister-dublin-bank-frankfurt-branch`) | [Gesamt-PDF lesen](../testakten/lobbyregister-dublin-bank-frankfurt-branch/gesamt-pdf/lobbyregister-dublin-bank-frankfurt-branch_gesamt.pdf) | [`testakte-lobbyregister-dublin-bank-frankfurt-branch.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lobbyregister-dublin-bank-frankfurt-branch.zip) |
| **Akte Lobbyregister: Spreebogen Regulatory GmbH / Wasserstoffpaket** (`lobbyregister-public-affairs-agentur-wasserstoff`) | [Gesamt-PDF lesen](../testakten/lobbyregister-public-affairs-agentur-wasserstoff/gesamt-pdf/lobbyregister-public-affairs-agentur-wasserstoff_gesamt.pdf) | [`testakte-lobbyregister-public-affairs-agentur-wasserstoff.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lobbyregister-public-affairs-agentur-wasserstoff.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Superplugin für Meldungen, Registrierung, Aktualisierung, oeffentliche API-Abfragen und laufende Compliance im Lobbyregister für die Interessenvertretung gegenueber dem Deutschen Bundestag und der Bundesregierung. Es fuehrt Nutzerinnen und Nutzer von der Frage "Muss ich ueberhaupt?" bis zur prueffaehigen Registrierungsmappe, zum Portal-Eingabeplan, zu Quartals-Uploads, Jahresaktualisierung, Verhaltenskodex, Open-Data-Monitoring und Meldung moeglicher Verstoesse.

Dieses Plugin ist **vollstaendig freistehend**. Es erwartet keine anderen Plugins, keine Portal-API und keine Kanzleisoftware. Wenn kein Zugang zum Lobbyregisterportal, DMS, CRM, Public-Affairs-Tool oder Finanzsystem vorhanden ist, arbeitet es mit manuellen Uploads oder einem ausdruecklich markierten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder ZIP aus dem Release installieren.
2. Neue Sache mit `lobbyregister-kommandocenter` oder `end-to-end-registrierungswizard` starten.
3. Organisation, geplante Kontakte, Auftraggeber, Regelungsvorhaben, Fristen, Portalstatus und vorhandene Unterlagen nennen.
4. Das Plugin routet zu Pflichtcheck, Ausnahmen, Portalangaben, Finanzdaten, Stellungnahmen, Updates, Verhaltenskodex oder Meldung.
5. Am Ende immer das Qualitaetsgate verlangen: Pflichtgrund, Ausnahmen, Datenfelder, Fristen, Freigaben, offene Annahmen und naechste Portalaktion.

## Enthaltene Skills

- `lobbyregister-kommandocenter` - Lobbyregister-Kommandocenter
- `lobbyregister-intake-mandat` - Mandats- und Projekt-Intake
- `interessenvertretung-begriff` - Begriff der Interessenvertretung
- `adressatenkreis-bundestag-bundesregierung` - Adressatenkreis Bundestag und Bundesregierung
- `registrierungspflicht-schwellen` - Registrierungspflicht und Schwellen
- `ausnahmen-bundestag` - Ausnahmen Bundestag
- `ausnahmen-bundesregierung` - Ausnahmen Bundesregierung
- `freiwillige-registrierung` - Freiwillige Registrierung
- `personen-organisationstyp` - Personen- und Organisationstyp
- `konzern-netzwerk-plattform` - Konzern, Netzwerk und Plattform
- `hauptstadtrepraesentanz` - Hauptstadtrepraesentanz
- `vertretungsberechtigte-personen` - Vertretungsberechtigte Personen
- `betraute-personen` - Betraute Personen
- `drehtuer-angaben` - Drehtuer-Angaben
- `taetigkeitsbeschreibung` - Taetigkeitsbeschreibung
- `interessen-und-vorhabenbereiche` - Interessen- und Vorhabenbereiche
- `regelungsvorhaben-erfassen` - Regelungsvorhaben erfassen
- `stellungnahmen-gutachten-upload` - Stellungnahmen und Gutachten Upload
- `auftraggeber-ermitteln` - Auftraggeber ermitteln
- `unterauftragnehmer-erfassen` - Unterauftragnehmer erfassen
- `fremdmandat-agenturfall` - Fremdmandat und Agenturfall
- `finanzaufwendungen-berechnen` - Finanzaufwendungen berechnen
- `hauptfinanzierungsquellen` - Hauptfinanzierungsquellen
- `oeffentliche-zuwendungen` - Oeffentliche Zuwendungen
- `schenkungen-sponsoring` - Schenkungen und Sponsoring
- `mitgliedschaften-mitgliederzahl` - Mitgliedschaften und Mitgliederzahl
- `jahresabschluss-rechenschaftsbericht` - Jahresabschluss und Rechenschaftsbericht
- `anonymisierung-schutzantrag` - Anonymisierung und Schutzantrag
- `datenschutz-nichtoeffentliche-angaben` - Datenschutz und nicht oeffentliche Angaben
- `portal-account-rollen` - Portal-Account und Rollen
- `erstregistrierung-ausfuellen` - Erstregistrierung ausfuellen
- `bestaetigungsdokument-freigabe` - Bestaetigungsdokument und Freigabe
- `registereintrag-finalcheck` - Registereintrag Finalcheck
- `aktualisierung-unverzueglich` - Unverzuegliche Aktualisierung
- `geschaeftsjahresaktualisierung` - Geschaeftsjahresaktualisierung
- `fristen-und-quartalsmonitor` - Fristen- und Quartalsmonitor
- `verhaltenskodex-integritaet` - Verhaltenskodex und Integritaet
- `erstkontakt-offenlegung` - Erstkontakt Offenlegung
- `visitenkarte-und-nachweise` - Visitenkarte und Nachweise
- `hausausweis-und-anhoerung` - Hausausweis und Anhoerung
- `registerfuehrende-stelle-kontakt` - Registerfuehrende Stelle Kontakt
- `verstoesse-melden` - Verstoesse melden
- `bussgeld-und-pruefverfahren` - Bussgeld und Pruefverfahren
- `nicht-aktualisiert-risiko` - Nicht-aktualisiert Risiko
- `fruehere-interessenvertretung-exit` - Exit und fruehere Interessenvertretung
- `suche-open-data-monitor` - Suche und Open-Data-Monitor
- `benachrichtigungskonto-monitor` - Benachrichtigungskonto Monitor
- `interne-lobbyregister-richtlinie` - Interne Lobbyregister-Richtlinie
- `dokumentationsakte-revisionsspur` - Dokumentationsakte und Revisionsspur
- `end-to-end-registrierungswizard` - End-to-End Registrierungswizard

## Vorlagen

- `assets/templates/registrierungspflicht-check.md` - Pflicht- und Ausnahmepruefung
- `assets/templates/registereintrag-datenraum.md` - Datenraum für Erstregistrierung und Update
- `assets/templates/regelungsvorhaben-matrix.md` - Regelungsvorhaben, Stellungnahmen und Uploadfristen
- `assets/templates/auftraggeber-und-unterauftrag.md` - Auftraggeber, Unterauftrag und eingesetzte Personen
- `assets/templates/finanzdaten-check.md` - Finanzaufwendungen, Zuwendungen, Schenkungen und Abschluss
- `assets/templates/aktualisierungskalender.md` - Fristen, Quartale und Geschaeftsjahresupdate
- `assets/templates/verhaltenskodex-kontaktkarte.md` - Offenlegung und Kodex-Check für Kontakte
- `assets/templates/qualitaetsgate.md` - Finaler Freigabe- und Risiko-Check
- `assets/templates/auslandsrechtstraeger-zweigniederlassung-check.md` - Spezialcheck auslaendischer Rechtstraeger mit deutscher Zweigniederlassung
- `assets/templates/streitvermerk-doppelregistrierung.md` - Variantenvermerk einmalige oder doppelte Registrierung
- `assets/templates/rfs-anfrage-zweigniederlassung.md` - Anfrageentwurf an die registerfuehrende Stelle
- `assets/templates/api-abfrageplan.md` - API-Such- und Abfrageplan für oeffentliche Registerdaten
- `assets/templates/registerdaten-json-mapping.md` - JSON-nahes Mapping interner Registerdaten auf den oeffentlichen Export
- `assets/templates/registerexport-diff.md` - Diff zwischen interner Freigabeakte und API/API-Export
- `assets/templates/open-data-monitoring-plan.md` - Watchlist, Alarmregeln und API-Cursor-Protokoll

## Offizielle Startquellen

- [Lobbyregister FAQ für Interessenvertreter](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572)
- [Lobbyregister A-Z](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/lobbyregister-a-z-863568)
- [Handbuch zur Eintragung Version 2.0](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch)
- [LobbyRG bei gesetze-im-internet](https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html)
- [Verhaltenskodex Anlage 6 BTGO](https://www.gesetze-im-internet.de/btgo2025anl_6/BJNR0FA0I0025BJNE000100000.html)
- [Sanktionen bei Verstoessen](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/sanktionen-bei-verstoessen-1014438)
- [Inhalte der Interessenvertretung](https://www.lobbyregister.bundestag.de/inhalte-der-interessenvertretung?lang=de)
- [Registerfuehrende Stelle](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/registerfuehrende-stelle-rfs--863578)
- [Open Data/API](https://www.lobbyregister.bundestag.de/informationen-und-hilfe/open-data-1049716)
- [API V2 YAML](https://api.lobbyregister.bundestag.de/rest/v2/R2.21-de.yaml)
- [API V2 Swagger UI](https://api.lobbyregister.bundestag.de/rest/v2/swagger-ui/)
- [JSON-Schema Registereintrag](https://www.lobbyregister.bundestag.de/json-schemas/current/Lobbyregister-Registereintrag-schema.json)

## Open Data und API V2

Das Plugin nutzt die offizielle API als **lesende Kontrollschicht**: Suche nach Organisationen, Abfrage veroeffentlichter Registereintraege, Versionen, Statistikdaten, Dublettenpruefung, Export-Diff und Monitoring. Registrierung, Aktualisierung, Bestaetigung, Stellungnahmen-Upload und sonstige Portalhandlungen bleiben Portalaktionen und dürfen nicht als API-Einreichung ausgegeben werden.

Technische Arbeitsregel:

1. Vor der Portalaktion: interne Daten mit `assets/templates/registerdaten-json-mapping.md` JSON-nah strukturieren.
2. Nach der Veroeffentlichung: oeffentlichen Eintrag mit API V2 abfragen und mit `assets/templates/registerexport-diff.md` gegen die Freigabeakte prüfen.
3. Für laufende Compliance: `assets/templates/api-abfrageplan.md` und `assets/templates/open-data-monitoring-plan.md` nutzen, Cursor und `sourceDate` archivieren.
4. Bei Zweigniederlassungen, Auftraggebern, Unterauftragnehmern und Namensvarianten immer eine Freitextsuche auf Dubletten dokumentieren.

Details stehen in [references/open-data-api-v2.md](references/open-data-api-v2.md).

## Freistehende Leitplanken

- Keine Aussage "nicht registrierungspflichtig" ohne dokumentierte Prüfung von Interessenvertretung, Adressat, Schwelle und Ausnahme.
- Keine Registrierung oder Aktualisierung ohne Verantwortliche, Freigabe und Bestaetigungsdokument.
- Keine Behauptung einer API-Einreichung ohne offizielle Dokumentation. Die bekannte API V2 ist für oeffentliche Registerdaten als lesender Zugriff zu behandeln.
- Keine Regelungsvorhaben- oder Stellungnahme-Bewertung ohne Datum der Kontaktaufnahme und Quartals-/Updatefrist.
- Keine Finanzangaben ohne Geschaeftsjahr, Berechnungsmethode, Belege und Plausibilitaetscheck.
- Keine Kontaktaufnahme ohne Offenlegung von Identitaet, Anliegen und gegebenenfalls Auftraggeber.
- Keine Meldung moeglicher Verstoesse ohne konkrete Registernummer, Sachverhalt, Belege und Unsicherheiten.
- Keine echten Mandats-, Lobbying- oder Personaldaten in ungepruefte Cloud- oder KI-Umgebungen.

## Verwendungsbeispiel

```
Wir sind ein mittelstaendisches Unternehmen und wollen in den naechsten Wochen
mit Bundestagsabgeordneten und einem Bundesministerium zu einem geplanten
Bundesgesetz sprechen. Bitte starte mit lobbyregister-kommandocenter, pruefe
Registrierungspflicht und Ausnahmen, lege die Datenanforderung an, formuliere
die Regelungsvorhaben und erstelle am Ende eine Registrierungsmappe mit
Fristenkalender und Offenlegungsbausteinen fuer Erstkontakte.
```

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 52 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `account-rollen-regelungsvorhaben-erfassen` | Plant Administrationskonto, Rollen, Zugriffsschutz, Zwei-Personen-Freigabe und Passwortmanager für das Lobbyregisterportal. Output Account-Konzept im Lobbyregister Bundestag. |
| `adressatenkreis-bundestag-bundesregierung` | Kartiert Adressatinnen und Adressaten nach § 1 LobbyRG: Bundestagsorgane, Mitglieder, Fraktionen, Gruppen, Mitarbeitende, Bundesregierung und Leitungsebenen bis Referatsleitung. Output Adressatenkarte im Lobbyregister Bundestag. |
| `aktualisierung-unverzueglich-adressatenkreis` | Steuert unverzuegliche Updates bei Stammdaten, Personen, Tätigkeitsbeschreibung, Vorhabenbereichen, Regelungsvorhaben, Auftraegen und Auftraggebern. Output Update-Ticket im Lobbyregister Bundestag. |
| `anonymisierung-schutzantrag-auftraggeber` | Prüft Beschraenkung der Veröffentlichung bei schutzwürdigen Interessen nach § 4 Abs. 6 LobbyRG und Altfall-Anonymisierung. Output Schutzantrag-Skizze im Lobbyregister Bundestag. |
| `auftraggeber-ermitteln` | Erfasst Auftraggeberinnen und Auftraggeber bei Interessenvertretung im Auftrag Dritter und die jeweils beauftragte Interessenvertretung. Output Auftraggebermatrix im Lobbyregister Bundestag. |
| `ausnahmen-bundesregierung-bundestag` | Prüft Ausnahmen bei Interessenvertretung gegenüber Bundesregierung und Ministerien nach § 2 Abs. 3 LobbyRG, einschließlich Buergeranfragen, Sachverständigengremien und Ersuchen. Output Ausnahmeprüfung im Lobbyregister Bundestag. |
| `ausnahmen-bundestag` | Prüft die Ausnahmen von der Registrierungspflicht bei Interessenvertretung gegenüber Bundestagsadressaten nach § 2 Abs. 2 LobbyRG. Output Ausnahmegutachten kurz mit Restpflichten im Lobbyregister Bundestag. |
| `benachrichtigungskonto-monitor` | Richtet Beobachtung von Registereintraegen, Aktualisierungen und Entwicklungen über das Benachrichtigungskonto ein. Output Watchlist im Lobbyregister Bundestag. |
| `bestaetigungsdokument-freigabe` | Bestimmt Unterzeichner, Leitungsperson, vertretungsberechtigte Person und interne Freigabe vor Eintragung oder Geschäftsjahresaktualisierung. Output Signaturmappe im Lobbyregister Bundestag. |
| `betraute-personen-datenschutz` | Ermittelt Personen, die mit Interessenvertretung nicht nur bei Gelegenheit betraut sind und unmittelbar auftreten. Abgrenzung zu Backoffice, gelegentlicher Hilfe und VZAE. Output Personenliste im Lobbyregister Bundestag. |
| `bussgeld-pruefverfahren-quartalsmonitor` | Reaktionsbei RfS-Prüfung, Anhörung, Bußgeldrisiko nach § 7 LobbyRG und Kodexverstoss. Output Verteidigungs- und Remediationplan im Lobbyregister Bundestag. |
| `datenschutz-nichtoeffentliche-angaben` | Ordnet öffentliche und nicht öffentliche Registerangaben, personenbezogene Daten, interne Nachweise und Portalveröffentlichung. Output Datenschutzkarte im Lobbyregister Bundestag. |
| `dokumentationsakte-revisionsspur-drehtuer` | Baut Aktenstruktur für Belege, Freigaben, Portal-Screenshots, Kontaktlogs, Kostenmethodik, RfS-Kommunikation und Jahresupdates. Output Aktenplan im Lobbyregister Bundestag. |
| `drehtuer-angaben` | Führt durch Angaben zu Mandat, Amt oder Funktion in Bundestag, Bundesregierung oder Bundesverwaltung aktuell oder in den letzten fuenf Jahren. Output Drehtuer-Prüfprotokoll im Lobbyregister Bundestag. |
| `end-to-erstkontakt-offenlegung` | Geführter Gesamtmit 50-Skill-Routing: Pflicht, Datenraum, Portal, Freigabe, Aktualisierung, Kodex und Monitoring. Output vollständige Registrierungsmappe im Lobbyregister Bundestag. |
| `erstkontakt-offenlegung` | Formuliert Offenlegung beim erstmaligen Kontakt: Identität, Anliegen, Auftraggeber, Registereintrag und Verhaltenskodizes. Output Kontaktbausteine im Lobbyregister Bundestag. |
| `erstregistrierung-ausfuellen` | Führt Schritt für Schritt durch den Portal-Ersteintrag: Stammdaten, Personen, Tätigkeit, Finanzen, Vorhaben, Auftraege und Uploads. Output Eingabeplan im Lobbyregister Bundestag. |
| `finanzaufwendungen-berechnen` | Berechnet finanzielle Aufwendungen im Bereich Interessenvertretung, Personal- und Sachkosten, Infrastruktur und Zuordnung. Output Kostenblatt im Lobbyregister Bundestag. |
| `freiwillige-registrierung-fremdmandat` | Berät zu freiwilliger Eintragung nach § 2 Abs. 5 LobbyRG: Rechte, volle Pflichten, Aktualisierung, Verhaltenskodex und Bußgeldrisiko bei falschen Angaben. Output Entscheidungsvermerk im Lobbyregister Bundestag. |
| `fremdmandat-agenturfall` | Spezialfür Public-Affairs-Agenturen, Kanzleien, Beratungen und Dienstleister mit mehreren Mandanten. Output Mandanten-Trennblatt im Lobbyregister Bundestag. |
| `fristen-und-quartalsmonitor` | Baut Fristenkalender für unverzuegliche Updates, Quartalsfrist für Stellungnahmen, sechs Monate Finanzdaten, jaehrliche Bestätigung und Nachholfristen. Output Fristenbuch im Lobbyregister Bundestag. |
| `fruehere-interessenvertretung` | Führt durch Anzeige, dass keine registrierungspflichtige Interessenvertretung mehr betrieben wird, sowie Archivierung und Monitoring der Liste frueherer Eintraege. Output Exit-Akte im Lobbyregister Bundestag. |
| `geschaeftsjahresaktualisierung` | Führt durch die mindestens jaehrliche vollständige Überprüfung und Bestätigung des Registereintrags nach § 3 und § 4 LobbyRG. Output Jahresupdate-Mappe im Lobbyregister Bundestag. |
| `hauptstadtrepraesentanz` | Prüft, ob eine Geschäftsstelle am Sitz von Bundestag und Bundesregierung als Hauptstadtrepraesentanz anzugeben ist. Output Berlin-Anschrift-Check im Lobbyregister Bundestag. |
| `hausausweis-anhoerung-interessen` | Prüft Auswirkungen des Registerstatus auf Tagesausweis, Gebaeudezutritt und Teilnahme an öffentlichen Anhörungen nach § 6 LobbyRG. Output Zutrittscheck im Lobbyregister Bundestag. |
| `hausausweis-und-anhoerung` | Prüft Auswirkungen des Registerstatus auf Tagesausweis, Gebaeudezutritt und Teilnahme an öffentlichen Anhoerungen nach § 6 LobbyRG. Output Zutrittscheck. |
| `intake-mandat-lobbyregister` | Erfasst Ausgangslage, Organisation, Kontaktplaene, Auftraggeber, Fristen und Portalstatus vor jeder Lobbyregister-Prüfung. Nutzt LobbyRG §§ 1 bis 5 und Bundestags-Handbuch. Output Intake-Protokoll und Dokumentenliste im Lobbyregister Bun... |
| `interessen-und-vorhabenbereiche` | Ordnet Interessen- und Vorhabenbereiche im Register zu und prüft, ob Themen breit genug und nicht verschleiernd beschrieben sind. Output Bereichsmatrix im Lobbyregister Bundestag. |
| `interessenvertretung-begriff-interne` | Prüft, ob eine Kontaktaufnahme unmittelbare oder mittelbare Einflussnahme auf Willensbildungs- oder Entscheidungsprozesse nach § 1 LobbyRG ist. Abgrenzung zu Information, Petition, Servicekontakt und rein lokalem Anliegen. Output Subsumt... |
| `interne-lobbyregister-richtlinie` | Erstellt interne Richtlinie für Rollen, Meldewege, Kontaktfreigabe, Registerdaten, Fristen, Verhaltenskodex und Schulung. Output Richtlinienentwurf im Lobbyregister Bundestag. |
| `jahresabschluss-rechenschaftsbericht-konzern` | Prüft Bereitstellung von Jahresabschluss oder Rechenschaftsbericht, Umgang mit noch nicht aufgestellten Unterlagen und Nachreichpflicht. Output Abschluss-Uploadplan im Lobbyregister Bundestag. |
| `kaltstart-triage` | Einstieg, Schnelltriage und Fallrouting im Lobbyregister Bundestag-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei... |
| `konzern-netzwerk-plattform` | Strukturiert Lobbyregisterfragen bei Konzernen, Verbaenden, losen Netzwerken, Plattformen und sonstigen kollektiven Tätigkeiten. Output Eintragungseinheiten-Map im Lobbyregister Bundestag. |
| `lobbyregister-hauptfinanzierungsquellen-angaben` | Strukturiert Hauptfinanzierungsquellen nach § 3 LobbyRG und grenzt Umsaetze, Beitraege, Zuwendungen, Schenkungen und sonstige Einnahmen ab. Output Finanzquellenmatrix im Lobbyregister Bundestag. |
| `lobbyregister-kommandocenter` | Master-Routing für Lobbyregister-Mandate: Pflichtcheck, Registrierung, Aktualisierung, Verhaltenskodex, Meldung, Sanktion, Unterlagen und naechster Skill. Normen LobbyRG §§ 1 bis 7. Output Mandatskarte, Routing und Qualitaetsgate im Lobb... |
| `mitgliedschaften-mitgliederzahl-nicht` | Erfasst Mitgliederzahl, mitgliedschaftliche Organisation und relevante Mitgliedschaften im Zusammenhang mit Interessenvertretung. Output Mitgliederkarte im Lobbyregister Bundestag. |
| `nicht-aktualisiert-risiko` | Prüft Kennzeichnung nicht aktualisiert, Nachholfristen, Übertragung in fruehere Interessenvertreter und Reputationsfolgen. Output Rettungsplan im Lobbyregister Bundestag. |
| `oeffentliche-zuwendungen-personen` | Prüft Zuwendungen und Zuschuesse der deutschen öffentlichen Hand, EU, Mitgliedstaaten oder Drittstaaten mit Schwelle je Geber. Output Zuwendungsliste im Lobbyregister Bundestag. |
| `personen-organisationstyp` | Bestimmt, ob natuerliche Person, juristische Person, Personengesellschaft, Einzelkaufmann, Netzwerk, Plattform oder sonstige Organisation einzutragen ist. Output Typenentscheidung im Lobbyregister Bundestag. |
| `regelungsvorhaben-erfassen` | Erfasst konkrete aktuelle, geplante oder angestrebte Regelungsvorhaben, auch ohne vorhandenen Referentenentwurf oder Drucksache. Output Regelungsvorhaben-Karte im Lobbyregister Bundestag. |
| `registereintrag-finalcheck-registerfuehrende` | Prüft vor Freigabe Vollständigkeit, Richtigkeit, Aktualitaet, Irreführungsfreiheit, Quellenstand und Plausibilitaet aller Pflichtangaben. Output Finalcheck-Protokoll im Lobbyregister Bundestag. |
| `registerfuehrende-stelle-kontakt` | Bereitet Anfragen an die registerführende Stelle, Nachweisantworten, Korrekturen und Telefonnotizen vor. Output RfS-Kommunikationsakte im Lobbyregister Bundestag. |
| `registrierungspflicht-schenkungen-sponsoring` | Prüft § 2 Abs. 1 LobbyRG: regelmäßig, auf Dauer, geschäftsmäßig für Dritte, mehr als 30 Kontakte in drei Monaten, Gegenleistung oder Auftrag. Output Pflichtampel im Lobbyregister Bundestag. |
| `schenkungen-sponsoring` | Prüft Schenkungen und sonstige lebzeitige Zuwendungen Dritter, Gesamtstufe, Einzelangaben, Zustimmung und Altfall-Anonymisierung. Output Sponsoring-Check im Lobbyregister Bundestag. |
| `stellungnahmen-gutachten-suche-open` | Prüft Bereitstellungspflicht für grundlegende Stellungnahmen oder Gutachten zu Regelungsvorhaben und Quartalsfrist. Norm § 3 LobbyRG. Output Upload-Log im Lobbyregister Bundestag. |
| `suche-open-data-monitor` | Nutzt Suche, Standardlisten, Open Data und API zur Markt-, Compliance- und Gegenparteienprüfung. Output Monitoring-Report im Lobbyregister Bundestag. |
| `taetigkeitsbeschreibung-unterauftragnehmer` | Formuliert die allgemeine Tätigkeit der Interessenvertretung klar, nicht irreführend und updatefähig. Normen § 3 und § 5 LobbyRG. Output Portaltext im Lobbyregister Bundestag. |
| `unterauftragnehmer-erfassen` | Prüft Unterauftragsverhältnisse, eingesetzte Organisationen und natuerliche Personen im Verantwortungsbereich. Output Unterauftragskette im Lobbyregister Bundestag. |
| `verhaltenskodex-integritaet-verstoesse-melden` | Operationalisiert Offenheit, Transparenz, Ehrlichkeit und Integritaet nach § 5 LobbyRG und Verhaltenskodex für Kontakte. Output Kodex-Check im Lobbyregister Bundestag. |
| `verstoesse-melden` | Führt durch Meldung möglicher Verstoesse gegen Verhaltenskodex oder Registerpflichten an lobbyregister-meldung@bundestag.de. Output Meldungsentwurf im Lobbyregister Bundestag. |
| `vertretungsberechtigte-personen-visitenkarte` | Ermittelt gesetzliche Vertretungen, Leitungspersonen und Zeichnungsberechtigte für Registerangaben und Bestätigungsdokument. Normen § 3 und § 4 LobbyRG. Output Vertretungsmatrix im Lobbyregister Bundestag. |
| `visitenkarte-und-nachweise` | Nutzt die Lobbyregister-Visitenkarte, Registerauszug und interne Nachweise für Kontaktaufnahme, Hausausweis, Anhörung und Compliance-Akte. Output Nachweispack im Lobbyregister Bundestag. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->

<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Unified Mini Prompt und Mega-Prompt

Für normale Chatbots ohne Plugin-Installation gibt es den **Unified Mini Prompt**: eine einzelne Markdown-Datei bis 7.500 Zeichen, die den Kern-Workflow dieses Plugins verdichtet und als Release-Asset direkt herunterladbar ist.

- **Sparversion herunterladen:** [`lobbyregister-bundestag-unified-mini-prompt.md`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/lobbyregister-bundestag-unified-mini-prompt.md)
- **Großer Mega-Prompt nur zur Anschauung im Repo:** [`testakten/megaprompts/lobbyregister-bundestag.md`](../testakten/megaprompts/lobbyregister-bundestag.md) (84 KB)

Der große Mega-Prompt wird nicht als installierbares Plugin und nicht als CoWork-Uploadmaterial ausgeliefert. Für echte Plugin-Nutzung bitte das Plugin-ZIP verwenden; für Ein-Datei-Nutzung den Unified Mini Prompt.

<!-- END megaprompt-und-vorlagen (autogen) -->
