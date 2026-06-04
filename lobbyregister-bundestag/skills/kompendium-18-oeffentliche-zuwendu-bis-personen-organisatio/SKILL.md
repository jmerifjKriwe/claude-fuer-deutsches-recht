---
name: kompendium-18-oeffentliche-zuwendu-bis-personen-organisatio
description: "lobbyregister-bundestag: Konsolidiertes Skill-Kompendium 18; bündelt 2 frühere Spezialskills (oeffentliche-zuwendungen, personen-organisationstyp) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 18 - lobbyregister-bundestag

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `oeffentliche-zuwendungen` | Prüft Zuwendungen und Zuschuesse der deutschen öffentlichen Hand, EU, Mitgliedstaaten oder Drittstaaten mit Schwelle je Geber. Output Zuwendungsliste. |
| `personen-organisationstyp` | Bestimmt, ob natuerliche Person, juristische Person, Personengesellschaft, Einzelkaufmann, Netzwerk, Plattform oder sonstige Organisation einzutragen ist. Output Typenentscheidung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `oeffentliche-zuwendungen`

**Frühere Beschreibung:** Prüft Zuwendungen und Zuschuesse der deutschen öffentlichen Hand, EU, Mitgliedstaaten oder Drittstaaten mit Schwelle je Geber. Output Zuwendungsliste.

# Oeffentliche Zuwendungen

## Einsatz

Oeffentliche Finanzierungen richtig einzeln oder gesammelt erfassen.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Welche oeffentlichen Stellen haben gezahlt?
2. Ueberschreiten Zahlungen je Geber den relevanten Schwellenwert?
3. Wie ist die Leistung kurz zu beschreiben?

## Quellenanker

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Zuwendungsliste mit Geber, Betrag, Zweck, Beschreibung, Beleg und Portaltext.

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

## 2. `personen-organisationstyp`

**Frühere Beschreibung:** Bestimmt, ob natuerliche Person, juristische Person, Personengesellschaft, Einzelkaufmann, Netzwerk, Plattform oder sonstige Organisation einzutragen ist. Output Typenentscheidung.

# Personen- und Organisationstyp

## Einsatz

Den richtigen Registertraeger auswaehlen, damit nicht Einzelpersonen falsch registriert werden.

## Gefuehrter Ablauf

1. Sachverhalt in einem Satz zusammenfassen: Wer will mit wem worueber sprechen oder hat bereits gehandelt?
2. Offizielle Quelle und Rechtsstand nennen: LobbyRG, Lobbyregister-FAQ, Handbuch oder Verhaltenskodex.
3. Die folgenden Leitfragen nacheinander stellen und fehlende Angaben als offene Punkte markieren.
4. Ergebnis nicht als Rechtsrat ausgeben, sondern als prueffaehige Arbeitsunterlage mit Annahmen, Belegen und naechster Portalaktion.

## Leitfragen

1. Wer tritt nach aussen auf?
2. Handelt eine Person im eigenen Namen oder fuer eine Organisation?
3. Gibt es mehrere Traeger, Netzwerkpartner oder Plattformstrukturen?

## Quellenanker

## Spezialfall Auslandsrechtstraeger mit deutscher Zweigniederlassung

Bei einer unselbststaendigen Zweigniederlassung ist zuerst der Rechtstraeger zu bestimmen. Die Handelsregistereintragung der Zweigniederlassung macht sie nicht automatisch zu einer eigenen juristischen Person. Der Skill soll deshalb die Eintragungseinheit, die Frankfurter oder Berliner Anschrift, die betrauten Personen und die Kosten-/Taetigkeitszuordnung auseinanderhalten. Eine zweite Registrierung der Zweigniederlassung darf nur als Pruefoption vorbereitet werden, nicht als selbstverstaendlicher Portal-Schritt.

- LobbyRG: https://www.gesetze-im-internet.de/lobbyrg/BJNR081800021.html
- Lobbyregister FAQ: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/informationen-fuer-interessenvertreter-863572
- Handbuch: https://www.lobbyregister.bundestag.de/informationen-und-hilfe/handbuch
- Leitplanken: ../../references/lobbyregister-leitplanken.md

## Output

Typenentscheidung mit Portal-Kategorie, Nachweisen und Abgrenzung zu betreuten Personen.

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
