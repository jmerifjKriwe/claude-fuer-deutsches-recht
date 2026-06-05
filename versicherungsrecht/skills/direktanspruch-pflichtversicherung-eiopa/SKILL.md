---
name: direktanspruch-pflichtversicherung-eiopa
description: "Direktanspruch Pflichtversicherung Eiopa im Plugin Versicherungsrecht: prüft konkret Direktanspruch gegen Haftpflichtversicherer, Grenzüberschreitender Versicherungsvertrieb, Betriebsschließungsversicherung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Direktanspruch Pflichtversicherung Eiopa

## Arbeitsbereich

Dieser Skill behandelt **Direktanspruch Pflichtversicherung Eiopa** als zusammenhängenden Arbeitsgang im Plugin Versicherungsrecht. Im Mittelpunkt steht die Prüfung von Direktanspruch gegen Haftpflichtversicherer, Grenzüberschreitender Versicherungsvertrieb, Betriebsschließungsversicherung. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `direktanspruch-pflichtversicherung-115-vvg` | Direktanspruch gegen Haftpflichtversicherer: Pflichtversicherung, Geschädigter, Insolvenz, Kfz, Berufshaftpflicht, Deckungsgrenzen und Einwendungen. |
| `eiopa-grenzueberschreitender-vertrieb` | Grenzüberschreitender Versicherungsvertrieb: Niederlassungs-/Dienstleistungsfreiheit, Host-/Home-Aufsicht, EIOPA, Passporting, Verbraucherbeschwerden und Sprach-/Informationspflichten. |
| `gewerbe-betriebsschliessung-infektionsschutz` | Betriebsschließungsversicherung: behördliche Verfügung, Krankheitserregerklauseln, dynamische/statische Verweisung, Teilschließung, Umsatzausfall und Vergleich. |

## Arbeitsweg

- Rolle und Ziel im Versicherungsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `direktanspruch-pflichtversicherung-115-vvg`

**Fokus:** Direktanspruch gegen Haftpflichtversicherer: Pflichtversicherung, Geschädigter, Insolvenz, Kfz, Berufshaftpflicht, Deckungsgrenzen und Einwendungen.

# Direktanspruch in Pflichtversicherung § 115 VVG

## Einsatz

Für Geschädigte, die nicht nur den Schädiger, sondern direkt den Versicherer in Anspruch nehmen wollen.

## Norm- und Quellenanker

VVG § 115; PflVG; Pflichtversicherungsnormen je Berufsgruppe; BGB Delikt/Vertrag; ZPO.

## Arbeitsfragen

1. Welche Pflichtversicherung eröffnet § 115 VVG?
2. Welche Einwendungen kann der Versicherer dem Geschädigten entgegenhalten?
3. Welche Deckungssumme und Selbstbehalt gelten?
4. Welche Parteien müssen verklagt oder beteiligt werden?

## Output

Direktanspruchsprüfung, Anspruchsschreiben, Klageparteienmatrix und Deckungssummencheck.

## Red Flags

- freiwillige Haftpflicht als Pflichtversicherung behandelt
- Selbstbehalt gegen Geschädigten falsch angewandt
- Schädiger insolvent
- Berufshaftpflichtnorm nicht identifiziert

## Anschluss-Skills

- betriebshaftpflicht-versicherungsfall-serienschaden
- subrogation-regress-86-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `eiopa-grenzueberschreitender-vertrieb`

**Fokus:** Grenzüberschreitender Versicherungsvertrieb: Niederlassungs-/Dienstleistungsfreiheit, Host-/Home-Aufsicht, EIOPA, Passporting, Verbraucherbeschwerden und Sprach-/Informationspflichten.

# EIOPA und grenzüberschreitender Versicherungsvertrieb

## Einsatz

Für internationale Policen, InsurTechs, EU-Vermittler und deutsche Kunden ausländischer Versicherer.

## Norm- und Quellenanker

VAG; IDD; Solvency II; EIOPA-Veröffentlichungen live prüfen; Rom-I/Brüssel-Ia bei Vertrag und Gerichtsstand.

## Arbeitsfragen

1. Wer ist Home-State-Aufsicht, wer Host-State?
2. Welche Vertriebsform und Kundengruppe?
3. Welche Pflichtinformationen in welcher Sprache?
4. Welches Gericht/Recht ist für Individualstreit zuständig?

## Output

EU-Vertriebscheck, Aufsichtslandkarte, Beschwerdeweg und Vertragsrechtsnotiz.

## Red Flags

- ausländische Aufsicht als BaFin-Ersatz missverstanden
- Gerichtsstandsklausel gegenüber Verbrauchern unwirksam
- Pflichtinformationen nur englisch
- Passporting nicht geprüft

## Anschluss-Skills

- vag-bafin-aufsicht-beschwerde-missstand
- deckungsprozess-zustaendigkeit-215-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `gewerbe-betriebsschliessung-infektionsschutz`

**Fokus:** Betriebsschließungsversicherung: behördliche Verfügung, Krankheitserregerklauseln, dynamische/statische Verweisung, Teilschließung, Umsatzausfall und Vergleich.

# Betriebsschließungsversicherung und Infektionsschutz

## Einsatz

Für Gewerbebetriebe nach behördlichen Eingriffen oder hygienerechtlichen Betriebsschließungen.

## Norm- und Quellenanker

VVG §§ 1, 14, 28; AVB Betriebsschließung; IfSG als Sachrecht; BGB AGB-Kontrolle.

## Arbeitsfragen

1. Welche Behörde ordnete was genau an?
2. Verweist die AVB statisch oder dynamisch auf IfSG-Listen?
3. Lag vollständige oder teilweise Betriebsschließung vor?
4. Wie berechnet sich der versicherte Schaden?

## Output

Deckungsmemo, AVB-Auslegung, Schadensberechnung und Vergleichsvorschlag.

## Red Flags

- Allgemeinverfügung und Einzelverfügung verwechselt
- Umsatzausfall ohne Kostenersparnis
- Klauseltransparenz nicht geprüft
- Vergleich ohne Nachberechnung

## Anschluss-Skills

- betriebsunterbrechung-sachschaden-trigger
- deckungsprozess-zustaendigkeit-215-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
