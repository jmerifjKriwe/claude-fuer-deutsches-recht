---
name: unfallversicherung-invaliditaet-vers
description: "Unfallversicherung Invaliditaet Fristen Gliedertaxe, Vers Fristen Verjaehrung Klagefrist Fallkalender, Rechtsschutz Vorvertraglichkeit Schadenereignis: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Unfallversicherung Invaliditaet Fristen Gliedertaxe, Vers Fristen Verjaehrung Klagefrist Fallkalender, Rechtsschutz Vorvertraglichkeit Schadenereignis

## Arbeitsbereich

In diesem Skill wird **Unfallversicherung Invaliditaet Fristen Gliedertaxe, Vers Fristen Verjaehrung Klagefrist Fallkalender, Rechtsschutz Vorvertraglichkeit Schadenereignis** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `unfallversicherung-invaliditaet-fristen-gliedertaxe` | Private Unfallversicherung: Unfallbegriff, Invalidität, ärztliche Feststellung, Fristen, Gliedertaxe, Mitwirkung von Krankheiten und Progression. |
| `vers-fristen-verjaehrung-klagefrist-fallkalender` | Fristen und Ausschlussrisiken im Versicherungsrecht: Fälligkeit, Hemmung, Verjährung, Obliegenheitsfristen, Nachprüfungsfristen, Gutachtenfristen und prozessuale Termine sicher verwalten. |
| `rechtsschutz-vorvertraglichkeit-schadenereignis` | Rechtsschutzversicherung: zeitliche Einordnung des Rechtsschutzfalls, Dauerverstoß, Beratungsrechtsschutz, Wartezeit und Vorvertraglichkeit. |

## Arbeitsweg

Für **Unfallversicherung Invaliditaet Fristen Gliedertaxe, Vers Fristen Verjaehrung Klagefrist Fallkalender, Rechtsschutz Vorvertraglichkeit Schadenereignis** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `versicherungsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `unfallversicherung-invaliditaet-fristen-gliedertaxe`

**Fokus:** Private Unfallversicherung: Unfallbegriff, Invalidität, ärztliche Feststellung, Fristen, Gliedertaxe, Mitwirkung von Krankheiten und Progression.

# Private Unfallversicherung: Invalidität, Fristen, Gliedertaxe

## Einsatz

Dieser Skill rettet Unfallmandate vor Fristversäumnissen und falscher Gliedertaxenberechnung.

## Norm- und Quellenanker

VVG §§ 178–191; AUB/AVB; BGB; ZPO medizinischer Sachverständigenbeweis.

## Arbeitsfragen

1. Wann ereignete sich das Unfallereignis und wie ist es beweisbar?
2. Wann trat Invalidität ein und wann wurde sie ärztlich festgestellt?
3. Welche Fristen nennt die AUB-Fassung?
4. Welche Vorinvalidität oder Mitwirkung wird behauptet?

## Output

Unfallfristenplan, Invaliditätsmatrix, Gutachterfragen und Anspruchsberechnung.

## Red Flags

- Frist zur ärztlichen Feststellung versäumt
- Unfallbegriff bei Eigenbewegung unklar
- Mitwirkungsanteil pauschal gekürzt
- Progression falsch gerechnet

## Anschluss-Skills

- vers-fristen-verjaehrung-klagefrist-fallkalender
- vergleich-abfindung-entschaedigungsquittung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `vers-fristen-verjaehrung-klagefrist-fallkalender`

**Fokus:** Fristen und Ausschlussrisiken im Versicherungsrecht: Fälligkeit, Hemmung, Verjährung, Obliegenheitsfristen, Nachprüfungsfristen, Gutachtenfristen und prozessuale Termine sicher verwalten.

# Fristenkalender für Versicherungsfälle

## Einsatz

Versicherungsfälle sind oft Fristenfallen. Dieser Skill macht aus verstreuter Korrespondenz einen belastbaren Fristen- und Handlungskalender.

## Norm- und Quellenanker

VVG §§ 14, 15, 28, 31, 215; BGB §§ 195, 199, 203, 204; ZPO; spartenspezifische AVB-Fristen.

## Arbeitsfragen

1. Wann entstand der Anspruch, wann wurde er fällig, wann wurde abgelehnt?
2. Gab es Verhandlungen oder Ombudsmannverfahren mit Hemmungswirkung?
3. Welche AVB-Fristen laufen für Anzeige, Invaliditätsfeststellung, Nachweise oder Nachprüfung?
4. Welche Klage- oder Verfahrensfrist ist als nächstes kritisch?

## Output

Fristenkalender mit Rechtsgrund, Start, Ende, Hemmung, Verantwortlichem, nächster Handlung und Beleg.

## Red Flags

- Ablehnung liegt Monate zurück
- Verhandlungen nur telefonisch
- Invalidität oder Berufsunfähigkeit nicht fristgerecht substantiiert
- Ombudsmann als Hemmung überschätzt

## Anschluss-Skills

- deckungsprozess-zustaendigkeit-215-vvg
- unfallversicherung-invaliditaet-fristen-gliedertaxe

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `rechtsschutz-vorvertraglichkeit-schadenereignis`

**Fokus:** Rechtsschutzversicherung: zeitliche Einordnung des Rechtsschutzfalls, Dauerverstoß, Beratungsrechtsschutz, Wartezeit und Vorvertraglichkeit.

# Rechtsschutz: Vorvertraglichkeit und Schadenereignis

## Einsatz

Wenn die RSV sagt „der Streit begann vor Vertragsbeginn“, setzt dieser Skill die Chronologie richtig.

## Norm- und Quellenanker

VVG §§ 125 ff.; ARB; BGB; ZPO.

## Arbeitsfragen

1. Welches Ereignis löste den Rechtsverstoß aus?
2. Ist es ein Dauerverstoß, Folgeereignis oder neuer Streit?
3. Welche Wartezeit gilt?
4. Welche Korrespondenz belegt den ersten ernsthaften Konflikt?

## Output

Zeitstrahl Rechtsschutzfall, Argumentationsmemo und Deckungsnachforderung.

## Red Flags

- Kündigungsschutzfall falsch datiert
- Dauerverstoß pauschal angenommen
- Wartezeit übersehen
- Beratungs- und Prozessrechtsschutz verwechselt

## Anschluss-Skills

- rechtsschutz-deckungszusage-stichentscheid
- deckungsprozess-zustaendigkeit-215-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
