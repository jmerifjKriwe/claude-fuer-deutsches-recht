---
name: vertretungsberechtigte-personen-visitenkarte
description: "Vertretungsberechtigte Personen Visitenkarte im Lobbyregister Bundestag: prüft konkret Ermittelt gesetzliche Vertretungen, Leitungspersonen und Zeichnungsberechtigte f, Nutzt die Lobbyregister-Visitenkarte, Registerauszug und interne Nachweise für K. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Vertretungsberechtigte Personen Visitenkarte

## Arbeitsbereich

Dieser Skill behandelt **Vertretungsberechtigte Personen Visitenkarte** als zusammenhängenden Arbeitsgang im Lobbyregister Bundestag. Im Mittelpunkt steht die Prüfung von Ermittelt gesetzliche Vertretungen, Leitungspersonen und Zeichnungsberechtigte f, Nutzt die Lobbyregister-Visitenkarte. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vertretungsberechtigte-personen` | Ermittelt gesetzliche Vertretungen, Leitungspersonen und Zeichnungsberechtigte für Registerangaben und Bestätigungsdokument. Normen § 3 und § 4 LobbyRG. Output Vertretungsmatrix. |
| `visitenkarte-und-nachweise` | Nutzt die Lobbyregister-Visitenkarte, Registerauszug und interne Nachweise für Kontaktaufnahme, Hausausweis, Anhoerung und Compliance-Akte. Output Nachweispack. |

## Arbeitsweg

- Rolle und Ziel im Lobbyregister beim Bundestag klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: § 3 LobbyRG Eintragung vor erster Interessenvertretung, § 5 LobbyRG jährliche Aktualisierung, Berichtspflicht ggf. innerhalb 3 Monaten nach Ende des Geschäftsjahres.
- Tragende Normen verifizieren: LobbyRG §§ 1, 2, 3, 5, 6, 7, 8 (i.d.F. Reform 2024), Verhaltenskodex Lobbyregister, GOBT, BGleiG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Interessenvertreter, Bundestagsverwaltung (Lobbyregisterstelle), Geschäftsstelle, registrierte Verbände, Bundesregierung (zweiter Registerteil).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Lobbyregistereintrag, Verhaltenskodex-Bestätigung, Tätigkeitsbericht, Hausausweisantrag, Finanzangaben, Verbandsmitgliederliste — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `vertretungsberechtigte-personen`

**Fokus:** Ermittelt gesetzliche Vertretungen, Leitungspersonen und Zeichnungsberechtigte für Registerangaben und Bestätigungsdokument. Normen § 3 und § 4 LobbyRG. Output Vertretungsmatrix.

# Vertretungsberechtigte Personen

## Einsatz

Alle gesetzlichen Vertretungen und Freigabepersonen belastbar erfassen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Organe oder Gesellschafter vertreten die Einheit?
2. Wer darf das Bestaetigungsdokument unterschreiben?
3. Gibt es Prokura, Generalvollmacht oder sonstige Organisation?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Vertretungsmatrix mit Namen, Funktion, Kontaktdatenstatus, Nachweis und Drehtuerfrage.

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

## 2. `visitenkarte-und-nachweise`

**Fokus:** Nutzt die Lobbyregister-Visitenkarte, Registerauszug und interne Nachweise für Kontaktaufnahme, Hausausweis, Anhoerung und Compliance-Akte. Output Nachweispack.

# Visitenkarte und Nachweise

## Einsatz

Den aktuellen Registerstatus gegenueber Adressaten nachweisbar machen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Ist der Eintrag aktuell und ohne Negativkennzeichnung?
2. Welche Personen benoetigen die Visitenkarte?
3. Welche Nachweise gehoeren in die Handakte?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Nachweispack mit Visitenkarte-Check, Ablageort, Gueltigkeitsnotiz und Aktualisierungshinweis.

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
