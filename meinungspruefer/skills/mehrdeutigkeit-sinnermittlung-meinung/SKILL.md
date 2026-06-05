---
name: mehrdeutigkeit-sinnermittlung-meinung
description: "Mehrdeutigkeit Sinnermittlung Meinung im Plugin Meinungspruefer: prüft konkret Ermittelt den objektiven Sinn einer mehrdeutigen Äußerung, Kontext, Prüft, ob eine Äußerung Meinung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Mehrdeutigkeit Sinnermittlung Meinung

## Arbeitsbereich

**Mehrdeutigkeit Sinnermittlung Meinung** ordnet den Fall über die tragenden Prüffelder: Ermittelt den objektiven Sinn einer mehrdeutigen Äußerung, Kontext, Prüft. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `mehrdeutigkeit-sinnermittlung` | Ermittelt den objektiven Sinn einer mehrdeutigen Äußerung nach Wortlaut, Kontext, Begleitumständen und Durchschnittspublikum. Prüft, ob nicht ehrverletzende Deutungen tragfähig ausgeschlossen werden können. |
| `meinung-tatsache-abgrenzung` | Prüft, ob eine Äußerung Meinung, Tatsachenbehauptung, gemischte Äußerung, Verdachtsäußerung, Frage oder Satire ist. Schützt die Meinungsfreiheit vor falscher Tatsachenschublade und verlangt Belege nur dort, wo Tatsachen behauptet werden. |

## Arbeitsweg

- Rolle und Ziel im Meinungsprüfer für Äußerungsrecht: Meinung oder Tatsache, Beleidigung, üble Nachrede, Verleumdung, § 188 StGB, Art klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: StGB §§ 13, 22, 23, 25, 32, 35, 46, 47, 56, 57, StPO §§ 100a, 102, 105, 112, 136, 137, 140, 147, 152, 153a, 244, 257c, 261, 264, 265, 267, 304, 341, 344, 349; § 188 StGB, Art. 5 GG, Art. 10 EMRK, Art. 11 GRCh, EGMR — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `mehrdeutigkeit-sinnermittlung`

**Fokus:** Ermittelt den objektiven Sinn einer mehrdeutigen Äußerung nach Wortlaut, Kontext, Begleitumständen und Durchschnittspublikum. Prüft, ob nicht ehrverletzende Deutungen tragfähig ausgeschlossen werden können.

# Mehrdeutigkeit und Sinnermittlung

## Warum dieser Skill wichtig ist

Das Bundesverfassungsgericht beanstandet regelmäßig, wenn Gerichte eine Äußerung isoliert oder zu streng verstehen. Eine Verurteilung oder zivilrechtliche Untersagung darf nicht auf eine belastende Deutung gestützt werden, wenn eine naheliegende weniger belastende Deutung nicht tragfähig ausgeschlossen wurde.

## Arbeitsweise

1. **Wortlaut isoliert erfassen.**
2. **Gesamtbeitrag lesen.**
3. **Erkennbaren Anlass einbeziehen.**
4. **Publikum bestimmen:** unvoreingenommen und verständig, nicht überempfindlich, nicht böswillig.
5. **Deutungen bilden:** belastend, neutral, entlastend.
6. **Deutungen ausscheiden:** nur mit Gründen aus Wortlaut und Umständen.
7. **Risiko ableiten:** je mehr realistische Deutungen, desto vorsichtiger mit strafrechtlicher oder zivilrechtlicher Härte.

## Deutungsprotokoll

| Deutung | Tragende Anhaltspunkte | Gegenargumente | Ergebnis |
|---|---|---|---|
| belastend | | | |
| wertend | | | |
| nicht ehrverletzend | | | |

## Fehlerquellen

- Juristische Fachsprache wird einem laienhaften Post untergeschoben.
- Ein Begriff wird aus einem längeren Satz herausgeschnitten.
- Der Betroffene versteht die Äußerung subjektiv schlimmer als das Publikum.
- Ironie wird wörtlich genommen.
- Ein früherer Streit wird ignoriert, obwohl er für alle Rezipienten erkennbar war.

## Output

Formuliere am Ende:

"Nach dem derzeit bekannten Kontext ist die naheliegendste Deutung ... Eine straf-/zivilrechtlich belastende Deutung wäre ... Sie kann derzeit [ausgeschlossen / nicht ausgeschlossen / nur mit Zusatzbelegen gestützt] werden, weil ..."


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `meinung-tatsache-abgrenzung`

**Fokus:** Prüft, ob eine Äußerung Meinung, Tatsachenbehauptung, gemischte Äußerung, Verdachtsäußerung, Frage oder Satire ist. Schützt die Meinungsfreiheit vor falscher Tatsachenschublade und verlangt Belege nur dort, wo Tatsachen behauptet werden.

# Meinung oder Tatsachenbehauptung

## Grundidee

Meinungen sind durch Stellungnahme, Wertung und Dafürhalten geprägt. Tatsachen sind dem Beweis zugänglich. Viele gefährliche Fälle sind gemischt: Der Satz klingt wertend, trägt aber einen tatsächlichen Vorwurf; oder er klingt tatsächlich, ist im Kontext aber erkennbar rhetorisch, satirisch oder wertend.

## Prüfraster

1. **Beweiszugänglichkeit:** Kann der Kern mit Beweismitteln als wahr oder falsch festgestellt werden?
2. **Wertungsschwerpunkt:** Geht es vor allem um Bewertung, Schlussfolgerung, Empörung oder Meinung?
3. **Tatsachensubstrat:** Auf welche konkreten Vorgänge stützt sich die Wertung?
4. **Gesamtsinn:** Würde eine Trennung von Tatsache und Wertung den Sinn verfälschen?
5. **Publikum:** Versteht das Publikum den Begriff fachlich oder umgangssprachlich?
6. **Mehrdeutigkeit:** Gibt es eine nicht ehrverletzende oder weniger belastende Deutung?

## Typische Grenzfälle

- "Lügner" kann Tatsachenvorwurf, moralische Bewertung oder politische/soziale Zuspitzung sein.
- "Pinocchio" kann ironischer Hinweis auf gebrochene Zusagen sein; der Tatsachenkern sind dann konkrete Zusagen und Abweichungen.
- "Korrupt" kann strafrechtlicher Bestechungsvorwurf oder harte Bewertung eines intransparenten Vorgangs sein.
- "Betrug" kann juristisch-technisch gemeint sein, im Alltag aber auch "ich fühle mich übers Ohr gehauen" bedeuten.

## Output

Gib aus:

- **Äußerungstyp:** Meinung / Tatsache / gemischt / Verdacht / Satire / Frage.
- **Tatsachenkern:** konkret benennen.
- **Wertungsanteil:** konkret benennen.
- **Beweisbedarf:** nur für Tatsachen.
- **Grundrechtlicher Effekt:** welche Teile in Art. 5 GG fallen und wo bewusste oder erwiesen unwahre Tatsachen herausfallen können.

## Weiterleitung

Bei Tatsachenkern: `beleglage-tatsachenbehauptung`.

Bei Werturteil mit Herabsetzung: `strafrecht-185-beleidigung` und `abwaegung-art-5-gg`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.
