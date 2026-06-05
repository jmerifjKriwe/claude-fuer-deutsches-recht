---
name: freiwillige-registrierung-fremdmandat
description: "Freiwillige Registrierung, Fremdmandat Agenturfall: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Freiwillige Registrierung, Fremdmandat Agenturfall

## Arbeitsbereich

In diesem Skill wird **Freiwillige Registrierung, Fremdmandat Agenturfall** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `freiwillige-registrierung` | Berät zu freiwilliger Eintragung nach § 2 Abs. 5 LobbyRG: Rechte, volle Pflichten, Aktualisierung, Verhaltenskodex und Bußgeldrisiko bei falschen Angaben. Output Entscheidungsvermerk. |
| `fremdmandat-agenturfall` | Spezialfür Public-Affairs-Agenturen, Kanzleien, Beratungen und Dienstleister mit mehreren Mandanten. Output Mandanten-Trennblatt. |

## Arbeitsweg

Für **Freiwillige Registrierung, Fremdmandat Agenturfall** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `lobbyregister-bundestag` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `freiwillige-registrierung`

**Fokus:** Berät zu freiwilliger Eintragung nach § 2 Abs. 5 LobbyRG: Rechte, volle Pflichten, Aktualisierung, Verhaltenskodex und Bußgeldrisiko bei falschen Angaben. Output Entscheidungsvermerk.

# Freiwillige Registrierung

## Einsatz

Entscheiden, ob freiwillige Registrierung strategisch und organisatorisch tragfaehig ist.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Warum soll freiwillig registriert werden?
2. Kann die Organisation alle Angaben dauerhaft richtig und aktuell halten?
3. Gibt es Reputations-, Zugangsausweis- oder Transparenzgruende?

## Trade-off freiwillige Registrierung — was sich wirklich ändert

- **Pro:** Zugang zu BT-Anhörungen (Verbändeanhörung, § 70 Abs. 1 GO-BT i. V. m. Verhaltensrichtlinien), Sichtbarkeit bei Ministerien, Pressewahrnehmbarkeit, "transparency by default".
- **Contra:** Volle Pflichten aus § 3 LobbyRG: Stammdaten, Auftraggeber/Mitglieder, Schwerpunktthemen, jährlicher Tätigkeitsbericht und Finanzdaten — auch wenn nicht eintragungspflichtig.
- **Aktualisierungspflicht (§ 3 Abs. 3 LobbyRG) und Jahresbestätigung (§ 4 Abs. 2 LobbyRG):** Änderungen innerhalb von 30 Tagen; jährliche Bestätigung und Finanzdaten nach aktueller Portal-/Gesetzeslage prüfen.
- **Verhaltenskodex (§ 5 LobbyRG):** Unterwerfung als Voraussetzung; Verstoß führt zur Veröffentlichung und ggf. Sanktion (§ 7 LobbyRG bis 50.000 Euro).
- **Praxis-Hinweis:** Freiwillige Registrierung ist organisationspolitisch oft sinnvoll, aber Compliance-Aufwand realistisch kalkulieren (mind. 20–40 Std/Jahr je nach Größe); Verantwortlichkeit benennen (interne Lobbyregister-Beauftragte).
- **Frist-Trigger:** Beitragsjahr und Stichtage in den Compliance-Kalender; Kommunikation mit Auftraggebern und Spitzenpersonen vor jedem Update.

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Entscheidungsvorlage mit Vorteilen, Pflichten, Aufwand, Risiken und Go/No-Go.

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

## 2. `fremdmandat-agenturfall`

**Fokus:** Spezialfür Public-Affairs-Agenturen, Kanzleien, Beratungen und Dienstleister mit mehreren Mandanten. Output Mandanten-Trennblatt.

# Fremdmandat und Agenturfall

## Einsatz

Auftraggeberdaten und eigene Interessenvertretung getrennt halten.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche Mandate laufen parallel?
2. Welche Kontakte sind welchem Auftraggeber zuzuordnen?
3. Welche Kosten, Personen und Dokumente gehoeren zu welchem Mandat?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Mandanten-Trennblatt mit Konfliktcheck, Auftraggeberbezug, Kostenzuordnung und Updateausloesern.

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
