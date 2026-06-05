---
name: registereintrag-finalcheck-registerfuehrende
description: "Registereintrag Finalcheck, Registerfuehrende Stelle Kontakt: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Registereintrag Finalcheck, Registerfuehrende Stelle Kontakt

## Arbeitsbereich

In diesem Skill wird **Registereintrag Finalcheck, Registerfuehrende Stelle Kontakt** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `registereintrag-finalcheck` | Prüft vor Freigabe Vollständigkeit, Richtigkeit, Aktualitaet, Irreführungsfreiheit, Quellenstand und Plausibilitaet aller Pflichtangaben. Output Finalcheck-Protokoll. |
| `registerfuehrende-stelle-kontakt` | Bereitet Anfragen an die registerführende Stelle, Nachweisantworten, Korrekturen und Telefonnotizen vor. Output RfS-Kommunikationsakte. |

## Arbeitsweg

Für **Registereintrag Finalcheck, Registerfuehrende Stelle Kontakt** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `lobbyregister-bundestag` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `registereintrag-finalcheck`

**Fokus:** Prüft vor Freigabe Vollständigkeit, Richtigkeit, Aktualitaet, Irreführungsfreiheit, Quellenstand und Plausibilitaet aller Pflichtangaben. Output Finalcheck-Protokoll.

# Registereintrag Finalcheck

## Einsatz

Den Eintrag vor Absendung wie eine Compliance-Akte gegenlesen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Sind alle Pflichtfelder belegt?
2. Passen Personen, VZAE, Kosten, Auftraggeber und Vorhaben zusammen?
3. Sind Risiken, Annahmen und Nachreichpflichten markiert?

## Quellenanker

## Doppelregistrierungs-Check

Vor Freigabe muss geprueft werden, ob mehrere Registerentwuerfe dieselbe juristische Person, dieselben betrauten Personen, dieselben Finanzaufwendungen oder dieselben Regelungsvorhaben doppelt abbilden. Bei Doppelungen: einen Streitvermerk erstellen, Primaerentwurf markieren und eine Anfrage an die registerfuehrende Stelle vorbereiten.

## API- und Export-Nachkontrolle

Der Finalcheck hat zwei Zeitpunkte:

1. **Vor Portalabgabe:** Interne Daten mit `assets/templates/registerdaten-json-mapping.md` JSON-nah auf das oeffentliche Schema mappen. Das Mapping ist nur QA, keine Einreichung.
2. **Nach Veroeffentlichung:** Oeffentlichen Registereintrag per API V2 oder JSON-Download abrufen und mit `assets/templates/registerexport-diff.md` gegen die Freigabeakte pruefen.

Im Nachcheck mindestens pruefen: Registernummer, Version, Gesetzeslage, Aktivstatus, Name/Rechtstraeger, Adresse, Niederlassungen, betraute Personen, VZAE, Taetigkeitsbeschreibung, Interessenbereiche, Regelungsvorhaben, Stellungnahmen, Auftraggeber, Unterauftragnehmer, Finanzaufwendungen, Zuwendungen, Schenkungen, Berichte, Verhaltenskodex, verweigerte Angaben, verspaetete Aktualisierung und Kodexverstoesse.

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md
- Open Data/API: ../../references/open-data-api-v2.md

## Output

Finalcheck-Protokoll mit Gruen/Orange/Rot, Korrekturliste, Freigabeempfehlung, API-Nachkontrollplan und Registerexport-Diff.

## Qualitaetsgate

- Pflichtgrund, Ausnahme und freiwillige Registrierung werden getrennt.
- Jede Frist bekommt Triggerdatum, Verantwortliche und Wiedervorlage.
- Jede Portalangabe bekommt Quelle, Freigabe und offenen Pruefpunkt.
- Unsichere Rechts- oder Tatsachenfragen werden nicht geglaettet, sondern sichtbar markiert.
- Jede API-Abweichung wird als rechtlich relevant, technisch relevant oder Anzeige-/Schemaeffekt klassifiziert.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `registerfuehrende-stelle-kontakt`

**Fokus:** Bereitet Anfragen an die registerführende Stelle, Nachweisantworten, Korrekturen und Telefonnotizen vor. Output RfS-Kommunikationsakte.

# Registerfuehrende Stelle Kontakt

## Einsatz

Kommunikation mit der Bundestagsverwaltung knapp, sachlich und belegfest fuehren.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Was ist die konkrete Frage oder Beanstandung?
2. Welche Registernummer, Portalstelle und Belege gehoeren dazu?
3. Welche Frist wurde gesetzt?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

RfS-Kommunikationsakte mit Entwurf, Anlagenliste, Telefonnotiz und Wiedervorlage.

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
