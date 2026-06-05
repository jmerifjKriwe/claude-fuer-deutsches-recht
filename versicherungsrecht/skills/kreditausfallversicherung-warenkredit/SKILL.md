---
name: kreditausfallversicherung-warenkredit
description: "Kreditausfallversicherung Warenkredit im Plugin Versicherungsrecht: prüft konkret Kreditausfall-/Warenkreditversicherung, Kreditversicherung im laufenden Debitorenmanagement, Bezugsrechte in Lebens- und Rentenversicherung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Kreditausfallversicherung Warenkredit

## Arbeitsbereich

Dieser Skill behandelt **Kreditausfallversicherung Warenkredit** als zusammenhängenden Arbeitsgang im Plugin Versicherungsrecht. Im Mittelpunkt steht die Prüfung von Kreditausfall-/Warenkreditversicherung, Kreditversicherung im laufenden Debitorenmanagement, Bezugsrechte in Lebens- und Rentenversicherung. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kreditausfallversicherung-warenkredit-forderungsausfall` | Kreditausfall-/Warenkreditversicherung: Limit, Forderungsausfall, Insolvenztatbestand, Obliegenheiten, Selbstbehalt, Factoring-Schnittstelle und Regress. |
| `kreditversicherung-obliegenheiten-limit-pruefung` | Kreditversicherung im laufenden Debitorenmanagement: Limite, Überfälligkeiten, Risikoinformationen, Inkassostart, Meldungen und Streit um Leistungsfreiheit. |
| `lebensversicherung-bezugsrecht-widerruf-aenderung` | Bezugsrechte in Lebens- und Rentenversicherung: widerruflich/unwiderruflich, Scheidung, Erbfall, Sicherungsabtretung, Insolvenz, Änderungserklärung und Auszahlungsstreit. |

## Arbeitsweg

- Rolle und Ziel im Versicherungsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `kreditausfallversicherung-warenkredit-forderungsausfall`

**Fokus:** Kreditausfall-/Warenkreditversicherung: Limit, Forderungsausfall, Insolvenztatbestand, Obliegenheiten, Selbstbehalt, Factoring-Schnittstelle und Regress.

# Kreditausfallversicherung und Warenkreditversicherung

## Einsatz

Für Lieferanten, die Zahlungsausfälle über Kreditversicherung absichern und bei Insolvenz des Kunden Deckung brauchen.

## Norm- und Quellenanker

VVG Schadenversicherung; AVB Warenkredit; InsO; HGB; Factoringvertrag.

## Arbeitsfragen

1. Welches Kreditlimit galt wann und für welchen Schuldner?
2. Ist der versicherte Forderungsausfall eingetreten?
3. Wurden Melde-, Mahn- und Inkassoobliegenheiten eingehalten?
4. Wie wirken Factoring, Abtretung und Eigentumsvorbehalt?

## Output

Limit-/Forderungsmatrix, Obliegenheitscheck, Insolvenznachweis und Deckungsantrag.

## Red Flags

- Lieferung nach Limitstreichung
- Mahnobliegenheiten verletzt
- Forderung abgetreten
- Ausfalltatbestand nicht erreicht

## Anschluss-Skills

- kreditversicherung-obliegenheiten-limit-pruefung
- restschuldversicherung-widerruf-kopplung-verbraucherdarlehen

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `kreditversicherung-obliegenheiten-limit-pruefung`

**Fokus:** Kreditversicherung im laufenden Debitorenmanagement: Limite, Überfälligkeiten, Risikoinformationen, Inkassostart, Meldungen und Streit um Leistungsfreiheit.

# Kreditversicherung: Limitprüfung und Obliegenheiten

## Einsatz

Der Skill eignet sich für Unternehmen, die ihr Debitorenportfolio versichert führen und nicht durch Prozessfehler Deckung verlieren wollen.

## Norm- und Quellenanker

VVG §§ 28, 31; AVB Kreditversicherung; InsO; BGB/HGB.

## Arbeitsfragen

1. Welche Limite sind aktiv, reduziert, gestrichen oder still?
2. Welche Überfälligkeiten lösen Meldung oder Lieferstopp aus?
3. Welche Informationen über Bonität/Insolvenz lagen vor?
4. Welche Dokumentation braucht der Versicherer?

## Output

Debitoren-Ampel, Obliegenheitskalender, Lieferfreigabe-Check und Schadenanzeige.

## Red Flags

- Excel-Limitliste veraltet
- Bonitätswarnung nicht gemeldet
- Weiterlieferung trotz Ausfallanzeichen
- Inkasso ohne Versichererabstimmung

## Anschluss-Skills

- kreditausfallversicherung-warenkredit-forderungsausfall
- vvg-obliegenheit-28-quotelung-kausalitaet

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `lebensversicherung-bezugsrecht-widerruf-aenderung`

**Fokus:** Bezugsrechte in Lebens- und Rentenversicherung: widerruflich/unwiderruflich, Scheidung, Erbfall, Sicherungsabtretung, Insolvenz, Änderungserklärung und Auszahlungsstreit.

# Lebensversicherung: Bezugsrecht, Widerruf, Änderung

## Einsatz

Der Skill klärt, wer bei Tod oder Ablauf wirklich Geld bekommt und wie Änderungen sauber dokumentiert werden.

## Norm- und Quellenanker

VVG §§ 150–171, besonders §§ 159, 160; BGB Erbrecht/Abtretung; InsO; FamFG/Nachlass.

## Arbeitsfragen

1. Ist das Bezugsrecht widerruflich oder unwiderruflich?
2. Wann und in welcher Form wurde geändert?
3. Gibt es Scheidung, Erbfall, Pfändung, Abtretung oder Insolvenz?
4. Welche Auszahlungsunterlagen fordert der Versicherer?

## Output

Bezugsrechtsgutachten, Unterlagenliste, Auszahlungsschreiben und Streitrisiko.

## Red Flags

- alte Ehegattenbezeichnung
- Sicherungsabtretung an Bank
- Erben verwechseln Nachlass und Bezugsrecht
- unwirksame Änderung kurz vor Tod

## Anschluss-Skills

- lebensversicherung-rueckkaufswert-abschlusskosten-widerspruch
- subrogation-regress-86-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
