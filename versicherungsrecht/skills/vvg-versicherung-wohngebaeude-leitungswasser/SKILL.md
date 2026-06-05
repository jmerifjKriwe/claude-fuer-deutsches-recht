---
name: vvg-versicherung-wohngebaeude-leitungswasser
description: "VVG Versicherung Wohngebaeude Leitungswasser im Plugin Versicherungsrecht: prüft konkret Versicherung für fremde Rechnung, Wohngebäudeversicherung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# VVG Versicherung Wohngebaeude Leitungswasser

## Arbeitsbereich

**VVG Versicherung Wohngebaeude Leitungswasser** ordnet den Fall über die tragenden Prüffelder: Versicherung für fremde Rechnung, Wohngebäudeversicherung. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vvg-versicherung-fuer-fremde-43-48` | Versicherung für fremde Rechnung: wer darf Leistung verlangen, wem stehen Einwendungen entgegen, welche Rolle haben Sicherungsnehmer, Leasinggeber, Mieter, Subunternehmer und Konzernunternehmen? |
| `wohngebaeude-leitungswasser-sturm-hagel-brand` | Wohngebäudeversicherung: Leitungswasser, Sturm/Hagel, Brand, Elementarschaden, grobe Fahrlässigkeit, Obliegenheiten und Sanierungskosten. |

## Arbeitsweg

- Rolle und Ziel im Versicherungsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `vvg-versicherung-fuer-fremde-43-48`

**Fokus:** Versicherung für fremde Rechnung: wer darf Leistung verlangen, wem stehen Einwendungen entgegen, welche Rolle haben Sicherungsnehmer, Leasinggeber, Mieter, Subunternehmer und Konzernunternehmen?

# Versicherung für fremde Rechnung §§ 43–48 VVG

## Einsatz

Dieser Skill klärt Dreiecksverhältnisse, in denen Versicherungsnehmer und wirtschaftlich Betroffener auseinanderfallen.

## Norm- und Quellenanker

VVG §§ 43–48, 44, 45; BGB Abtretung/Einziehung; ZPO Prozessführungsbefugnis.

## Arbeitsfragen

1. Wer ist Versicherungsnehmer, versicherte Person, Bezugsberechtigter, Sicherungsnehmer?
2. Wer besitzt Police und kann Zahlung verlangen?
3. Welche Einwendungen gegen wen sind möglich?
4. Ist gewillkürte Prozessstandschaft oder Abtretung nötig?

## Output

Beteiligtenmatrix, Anspruchsinhaber-Prüfung, Prozessführungsnotiz und Zahlungsempfänger-Check.

## Red Flags

- Leasingobjekt beschädigt
- Bank als Sicherungsnehmer
- Konzernpolice mit Tochtergesellschaft
- versicherte Person will direkt klagen

## Anschluss-Skills

- transportversicherung-ware-lagerung
- direktanspruch-pflichtversicherung-115-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `wohngebaeude-leitungswasser-sturm-hagel-brand`

**Fokus:** Wohngebäudeversicherung: Leitungswasser, Sturm/Hagel, Brand, Elementarschaden, grobe Fahrlässigkeit, Obliegenheiten und Sanierungskosten.

# Wohngebäudeversicherung: Leitungswasser, Sturm, Brand

## Einsatz

Der Skill führt durch typische Gebäudeschäden mit Gutachten, Handwerkerangeboten und Streit um Ursache oder Höhe.

## Norm- und Quellenanker

VVG §§ 1, 28, 81, 82; BGB; VGB/AVB; Sachverständigenverfahren.

## Arbeitsfragen

1. Welche Gefahr ist versichert und welche ausgeschlossen?
2. Was ist Ursache, Folgeschaden, Sanierung und Sowieso-Kosten?
3. Wurde Schadenminderung erfüllt?
4. Ist grobe Fahrlässigkeit quotenrelevant?

## Output

Deckungsmemo, Schadenpositionsliste, Gutachterfragen und Zahlungsaufforderung.

## Red Flags

- Leitungswasser vs. Grundwasser verwechselt
- Sanierung vor Besichtigung ohne Fotobeweise
- Schimmel als Folgeschaden unklar
- Neuwertspitze nicht beachtet

## Anschluss-Skills

- sachverstaendigenverfahren-versicherung
- elementarschaden-starkregen-ueberschwemmung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
