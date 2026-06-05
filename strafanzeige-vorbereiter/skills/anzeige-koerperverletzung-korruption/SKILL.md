---
name: anzeige-koerperverletzung-korruption
description: "Anzeige Koerperverletzung Korruption im Strafanzeigen-Vorbereitung: prüft konkret Körperverletzung, Korruptionsanzeige. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Anzeige Koerperverletzung Korruption

## Arbeitsbereich

**Anzeige Koerperverletzung Korruption** ordnet den Fall über die tragenden Prüffelder: Körperverletzung, Korruptionsanzeige. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-koerperverletzung-223-230` | Körperverletzung: Verletzung, Arztbericht, Fotos, Zeugen, Strafantrag bei § 223 und besonderes öffentliches Interesse. |
| `anzeige-korruption-299-331ff` | Korruptionsanzeige: Bestechlichkeit/Bestechung im geschäftlichen Verkehr oder Amt, Vorteil, Unrechtsvereinbarung, Belege, Selbstbelastung. |

## Arbeitsweg

- Rolle und Ziel im Strafanzeige Vorbereiter klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `anzeige-koerperverletzung-223-230`

**Fokus:** Körperverletzung: Verletzung, Arztbericht, Fotos, Zeugen, Strafantrag bei § 223 und besonderes öffentliches Interesse.

# Körperverletzung §§ 223, 230 StGB

## Einsatz

Für einfache und gefährliche Körperverletzung.

## Norm- und Quellenanker

StGB §§ 223, 224, 230; StPO § 158.

## Arbeitsfragen

1. Welche Verletzung?
2. Welche ärztlichen Belege?
3. Welche Tatmittel/Zeugen?

## Output

Anzeige mit Beweis- und Strafantragscheck.

## Red Flags

- § 223 als immer Offizialdelikt
- Fotos ohne Datum
- Notwehrlage ungeprüft

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-korruption-299-331ff`

**Fokus:** Korruptionsanzeige: Bestechlichkeit/Bestechung im geschäftlichen Verkehr oder Amt, Vorteil, Unrechtsvereinbarung, Belege, Selbstbelastung.

# Korruption §§ 299, 331 ff. StGB

## Einsatz

Für Unternehmen und Betroffene bei Kickbacks/Geschenken.

## Norm- und Quellenanker

StGB §§ 299, 331–335; OWiG § 30; Compliance.

## Arbeitsfragen

1. Wer gab/nahm welchen Vorteil?
2. Welche Gegenleistung?
3. Welche Dokumente/Chats?

## Output

Korruptions-Anzeigepaket und Compliance-Schnittstelle.

## Red Flags

- eigene Beteiligung ungeklärt
- Geschenke policy-konform?
- Beweise nur Hörensagen

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
