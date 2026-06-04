---
name: kompendium-22-stellungnahmen-gutac-bis-suche-open-data-moni
description: "lobbyregister-bundestag: Konsolidiertes Skill-Kompendium 22; bündelt 2 frühere Spezialskills (stellungnahmen-gutachten-upload, suche-open-data-monitor) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 22 - lobbyregister-bundestag

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `stellungnahmen-gutachten-upload` | Prüft Bereitstellungspflicht für grundlegende Stellungnahmen oder Gutachten zu Regelungsvorhaben und Quartalsfrist. Norm § 3 LobbyRG. Output Upload-Log. |
| `suche-open-data-monitor` | Nutzt Suche, Standardlisten, Open Data und API zur Markt-, Compliance- und Gegenparteienprüfung. Output Monitoring-Report. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `stellungnahmen-gutachten-upload`

**Frühere Beschreibung:** Prüft Bereitstellungspflicht für grundlegende Stellungnahmen oder Gutachten zu Regelungsvorhaben und Quartalsfrist. Norm § 3 LobbyRG. Output Upload-Log.

# Stellungnahmen und Gutachten Upload

## Einsatz

Entscheiden, welche Dokumente in den Bereich Inhalte der Interessenvertretung gehoeren.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Wurde ein Dokument an Bundestags- oder Regierungsadressaten gegeben?
2. Ist es grundlegend oder nur Begleitkommunikation?
3. In welchem Quartal wurde es versandt?
4. Wie wird nach dem Upload geprueft, dass Dokument, Regelungsvorhaben und Version oeffentlich richtig erscheinen?

## API-Nachweis nach Upload

Nach dem Portal-Upload soll der Skill eine Nachkontrolle anlegen: oeffentlichen Eintrag per API abrufen, `statements`, `regulatoryProjects`, Version, `sourceDate`, Detailseite und PDF sichern und gegen Versanddatum, Empfaengerkreis, Regelungsvorhaben und Schwärzungsvermerk pruefen. Die API prueft nur den veroeffentlichten Datenstand; sie ersetzt den Portal-Upload nicht.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Upload-Log mit Dokumenttitel, Regelungsvorhaben, Versanddatum, Quartalsfrist, Schwärzungsbedarf und API-Nachweis.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `suche-open-data-monitor`

**Frühere Beschreibung:** Nutzt Suche, Standardlisten, Open Data und API zur Markt-, Compliance- und Gegenparteienprüfung. Output Monitoring-Report.

# Suche und Open-Data-Monitor

## Einsatz

Oeffentliche Registerdaten fuer Due Diligence und Monitoring auswerten.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Organisation, Branche, Registernummer oder Vorhaben sollen beobachtet werden?
2. Welche Suchfilter und Datenfelder sind relevant?
3. Welche Aenderungen muessen intern gemeldet werden?
4. Geht es um eigene Portal-Nachkontrolle, Gegenparteienpruefung, Dublettenrisiko oder Marktmonitoring?
5. Soll die Abfrage einmalig, periodisch oder als Cursor-gestuetzte Trefferliste laufen?

## API-V2-Arbeitsweise

Nutze die offizielle API V2 nur als lesende Quelle fuer oeffentliche Registerdaten. Fuer jede Abfrage:

1. API-Key ueber `LOBBYREGISTER_API_KEY` verwenden, nicht in die Akte schreiben.
2. `GET /registerentries?q=...&format=json` fuer Suche nach Organisationen, Zweigniederlassungen, Auftraggebern, Unterauftragnehmern, Themen und Schreibvarianten.
3. `GET /registerentries/{registerNumber}?format=json` fuer den amtlichen Einzelabgleich.
4. `GET /registerentries/{registerNumber}/{version}?format=json` fuer Versionsvergleich.
5. `GET /statistics/registerentries?format=json` fuer Datenstand und Monitoring-Kontext.
6. Cursor-Regel beachten: Folgeanfragen wiederholen, bis sich der Cursor nicht mehr aendert.
7. `sourceDate`, Suchparameter, Cursor, Registernummer, Version, `detailsPageUrl`, `pdfUrl` und Hash der Antwort dokumentieren.

Bei Zweigniederlassungen ist zwingend ein Suchlauf auf Rechtstraegername, Niederlassungsname, Sitzstaat, deutsche Adresse und Marken-/Kurzname auszugeben. Ein zweiter Treffer ist nicht automatisch Pflicht oder Fehler, sondern ein Streitpunkt fuer den Doppelregistrierungs-Check.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Monitoring-Report mit Suchprofil, API-Abfrageplan, Trefferliste, Cursor-Protokoll, Datenstand, Feldauffaelligkeiten, rechtlicher Bewertung und Folgeaktion.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- API-Ausgaben werden nicht als Portal-Einreichung oder automatische Registeraenderung dargestellt.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
