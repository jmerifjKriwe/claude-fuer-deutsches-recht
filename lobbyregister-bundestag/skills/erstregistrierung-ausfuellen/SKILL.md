---
name: erstregistrierung-ausfuellen
description: "Erstregistrierung Ausfuellen im Lobbyregister Bundestag: prüft konkret Führt Schritt für Schritt durch den Portal-Ersteintrag, Berechnet finanzielle Aufwendungen im Bereich, Personal- un. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Erstregistrierung Ausfuellen

## Arbeitsbereich

Dieser Skill behandelt **Erstregistrierung Ausfuellen** als zusammenhängenden Arbeitsgang im Lobbyregister Bundestag. Im Mittelpunkt steht die Prüfung von Führt Schritt für Schritt durch den Portal-Ersteintrag, Berechnet finanzielle Aufwendungen im Bereich, Personal- un. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `erstregistrierung-ausfuellen` | Führt Schritt für Schritt durch den Portal-Ersteintrag: Stammdaten, Personen, Tätigkeit, Finanzen, Vorhaben, Auftraege und Uploads. Output Eingabeplan. |
| `finanzaufwendungen-berechnen` | Berechnet finanzielle Aufwendungen im Bereich Interessenvertretung, Personal- und Sachkosten, Infrastruktur und Zuordnung. Output Kostenblatt. |

## Arbeitsweg

- Rolle und Ziel im Lobbyregister beim Bundestag klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: § 3 LobbyRG Eintragung vor erster Interessenvertretung, § 5 LobbyRG jährliche Aktualisierung, Berichtspflicht ggf. innerhalb 3 Monaten nach Ende des Geschäftsjahres.
- Tragende Normen verifizieren: LobbyRG §§ 1, 2, 3, 5, 6, 7, 8 (i.d.F. Reform 2024), Verhaltenskodex Lobbyregister, GOBT, BGleiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Interessenvertreter, Bundestagsverwaltung (Lobbyregisterstelle), Geschäftsstelle, registrierte Verbände, Bundesregierung (zweiter Registerteil).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Lobbyregistereintrag, Verhaltenskodex-Bestätigung, Tätigkeitsbericht, Hausausweisantrag, Finanzangaben, Verbandsmitgliederliste — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `erstregistrierung-ausfuellen`

**Fokus:** Führt Schritt für Schritt durch den Portal-Ersteintrag: Stammdaten, Personen, Tätigkeit, Finanzen, Vorhaben, Auftraege und Uploads. Output Eingabeplan.

# Erstregistrierung ausfuellen

## Einsatz

Aus Datenraum und Checklisten einen konkreten Portal-Eingabeplan machen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Sind alle Pflichtfelder und Nachweise vorhanden?
2. Welche Angaben sind noch unsicher?
3. Welche Texte muessen vor Eintragung intern freigegeben werden?

## Quellenanker

## Stop-Regel bei Zweigniederlassungen

Wenn die Nutzerin eine unselbststaendige Zweigniederlassung als eigene Organisation registrieren will, muss der Skill stoppen und nachfragen: Ist die Zweigniederlassung eigener Rechtstraeger oder nur Handelsregisterzweigstelle? Liegt eine ausdrueckliche Auskunft der registerfuehrenden Stelle vor? Ohne diese Klaerung nur den ausländischen oder inlaendischen Rechtstraeger als Primaerentwurf ausgeben und die Niederlassung transparent im Eintrag abbilden.

## JSON-nahes Eingabemapping

Erzeuge neben dem Portal-Eingabeplan ein JSON-nahes Arbeitsmapping nach `assets/templates/registerdaten-json-mapping.md`. Das Mapping hilft, Pflichtfelder, Freigaben und den spaeteren API-Diff vorzubereiten. Es darf nicht als technische Einreichung, XML-Upload oder Portalersatz bezeichnet werden.

Fuer jedes Feld angeben:

- interne Quelle
- Portalabschnitt
- Freigabeperson
- Unsicherheiten
- erwartetes oeffentliches JSON-Feld nach Veroeffentlichung
- Nachkontrolle per API oder JSON-Download

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Eingabeplan mit Portalabschnitten, Copy-Texten, Anlagenliste, Freigaben, JSON-nahem Mapping, API-Nachkontrollplan und Stop-Punkten.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- Die API wird nur als spaetere Kontrollquelle beschrieben, nicht als Einreichungsweg.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `finanzaufwendungen-berechnen`

**Fokus:** Berechnet finanzielle Aufwendungen im Bereich Interessenvertretung, Personal- und Sachkosten, Infrastruktur und Zuordnung. Output Kostenblatt.

# Finanzaufwendungen berechnen

## Einsatz

Finanzangaben nachvollziehbar und prueffest vorbereiten.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Personen und Sachmittel dienen Interessenvertretung?
2. Welche Kosten sind anteilig zuzuordnen?
3. Welche Geschaeftsjahre und Rundungsstufen gelten im Portal?

## Aufwendungs- und Finanzangabe § 3 Abs. 1 Nr. 8 LobbyRG

**Anzugeben** für das jeweilige letzte abgeschlossene **Geschäftsjahr**:

- jährliche **finanzielle Aufwendungen** für Interessenvertretung gegenüber Bundestag und Bundesregierung,
- gestuft in den vorgegebenen **Korridoren** (siehe unten),
- inkl. **Personalkosten**, **Sachkosten**, **externe Dienstleistungen**, **Aufwendungen für Beauftragte**.

## Korridor-Stufen (Aufwendungsangabe)

Eintrag im Portal erfolgt in Stufen, nicht punktgenau:

| Stufe | Korridor |
|---|---|
| 1 | bis 10.000 Euro |
| 2 | 10.001 - 20.000 Euro |
| 3 | 20.001 - 30.000 Euro |
| ... | weiter in 10.000-Euro-Schritten bis ... |
| n | 90.001 - 100.000 Euro |
| n+1 | 100.001 - 200.000 Euro (ab 100.000 in 100.000er-Schritten) |
| ... | weiter in 100.000-Euro-Schritten |
| Höchststufe | über mehrere Millionen Euro (exakter Schritt nach aktueller Portal-Vorgabe; Handbuch live prüfen) |

(Stufenraster der amtlichen Vorgabe Bundestag entsprechen; vor Eintrag im Portal verifizieren.)

## Methodik der Aufwandsberechnung

1. **Personalkosten** anteilig: Vollzeit-Äquivalente, die für Interessenvertretung tätig sind; Bruttogehalt + Lohnnebenkosten + Sozialversicherung + ggf. variable Vergütung.
2. **Sachkosten** anteilig: Büroraum, IT, Telefon, Reise, Veranstaltungen.
3. **Externe Dienstleistungen**: Honorare für Berater, Agenturen, Anwälte, soweit sie Interessenvertretung tätigen (nicht: reine Rechtsberatung in Mandantenangelegenheit).
4. **Anteilssatz** bei gemischter Tätigkeit: nachvollziehbar herleiten (z. B. Zeiterfassungssysteme, Schätzung mit Begründung, Dokumentation).
5. **Geschäftsjahr** entsprechend Bilanzjahr; bei Vereinen / Stiftungen ggf. Kalenderjahr.

## Pflichten zur Auftraggeber-Angabe § 3 Abs. 1 Nr. 9 LobbyRG

- Bei **interessensvertretender Tätigkeit für Dritte** Auftraggeber namentlich angeben.
- Bei Schutzbedarf: Anonymisierung beantragen (§ 4 LobbyRG, vgl. Skill `anonymisierung-schutzantrag`).

## Praxisfallen

- **Unter Schwelle 10.000 Euro**: dennoch Stufe 1 anzugeben — kein „kein Aufwand", sondern „bis 10.000 Euro".
- **Beauftragte** zählen zum Aufwand des Auftraggebers — bei doppelter Eintragung Doppelzählung vermeiden.
- **Aktualisierung** unverzüglich bei wesentlicher Änderung (z. B. Stufenwechsel) — § 3 Abs. 3 LobbyRG (innerhalb 30 Tagen).
- **Anwaltliche Tätigkeit in Mandantenangelegenheit** ist regelmäßig nicht Interessenvertretung (§ 2 II Nr. 9 LobbyRG); jedoch politische Lobbyarbeit der Kanzlei für Wirtschaftsmandanten kann pflichtig sein.
- **Branchenverband** zählt seine Gesamt-Aufwendungen für Interessenvertretung; nicht aufzuteilen auf Mitglieder.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Kostenblatt mit Methodik, Annahmen, Belegen, Stufenwert und Freigabefragen.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
