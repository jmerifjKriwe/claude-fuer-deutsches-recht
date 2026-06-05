---
name: lebensversicherung-rueckkaufswert
description: "Lebensversicherung Rueckkaufswert im Plugin Versicherungsrecht: prüft konkret Rückkaufswert, Abschlusskosten, Kündigung, Beitragsfreistellung und Altvertrags-. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Lebensversicherung Rueckkaufswert

## Arbeitsbereich

Dieser Skill behandelt **Lebensversicherung Rueckkaufswert** als zusammenhängenden Arbeitsgang im Plugin Versicherungsrecht. Im Mittelpunkt steht die Prüfung von Rückkaufswert, Abschlusskosten, Kündigung. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `lebensversicherung-rueckkaufswert-abschlusskosten-widerspruch` | Rückkaufswert, Abschlusskosten, Kündigung, Beitragsfreistellung und Altvertrags-Widerspruch in Lebens- und Rentenversicherung prüfen. |
| `lebensversicherung-ueberschussbeteiligung-bewertungsreserven` | Überschussbeteiligung, Schlussüberschuss, Bewertungsreserven und Informationsrechte in Lebensversicherung und Rentenversicherung verständlich prüfen. |
| `nachhaltigkeit-taxonomie-sfdr-versicherungsprodukt` | Nachhaltigkeits- und ESG-Angaben bei Versicherungsanlageprodukten: Taxonomie, SFDR, Greenwashing, Produktfreigabe und Vertrieb. |

## Arbeitsweg

- Rolle und Ziel im Versicherungsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `lebensversicherung-rueckkaufswert-abschlusskosten-widerspruch`

**Fokus:** Rückkaufswert, Abschlusskosten, Kündigung, Beitragsfreistellung und Altvertrags-Widerspruch in Lebens- und Rentenversicherung prüfen.

# Lebensversicherung: Rückkaufswert, Abschlusskosten, Widerspruch

## Einsatz

Der Skill ist für Mandate, in denen Kunden alte Lebensversicherungen kündigten oder widersprechen wollen.

## Norm- und Quellenanker

VVG §§ 150 ff., 169; VVG a.F. bei Altverträgen live prüfen; BGB; BGH-Rechtsprechung nur verifiziert verwenden.

## Arbeitsfragen

1. Welche Vertragsgeneration und Belehrung gilt?
2. Wie wurde der Rückkaufswert berechnet?
3. Sind Abschlusskosten/Zillmerung transparent?
4. Ist Widerspruch, Kündigung oder Vergleich wirtschaftlich besser?

## Output

Rückkaufswert-Check, Belehrungsprüfung, Anspruchsberechnung und Mandantenentscheidung.

## Red Flags

- Altvertrag ohne vollständige Unterlagen
- Widerspruch wirtschaftlich überschätzt
- Steuerfolgen vergessen
- Vergleich ohne Berechnung

## Anschluss-Skills

- lebensversicherung-bezugsrecht-widerruf-aenderung
- vag-bafin-aufsicht-beschwerde-missstand

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `lebensversicherung-ueberschussbeteiligung-bewertungsreserven`

**Fokus:** Überschussbeteiligung, Schlussüberschuss, Bewertungsreserven und Informationsrechte in Lebensversicherung und Rentenversicherung verständlich prüfen.

# Überschussbeteiligung und Bewertungsreserven

## Einsatz

Der Skill übersetzt versicherungsmathematische Schreiben in rechtlich prüfbare Fragen.

## Norm- und Quellenanker

VVG §§ 153 ff., 169; VAG; Informationspflichten; BaFin-Hinweise live prüfen.

## Arbeitsfragen

1. Welche Überschusskomponenten sind zugesagt, deklariert oder nur erwartet?
2. Wie wird Beteiligung an Bewertungsreserven erklärt?
3. Welche Änderung beruht auf Zinsumfeld, Kollektiv oder Kosten?
4. Welche Auskunft kann verlangt werden?

## Output

Transparenzmemo, Auskunftsschreiben und Plausibilitätscheck.

## Red Flags

- Schlussüberschuss als garantiert verstanden
- Bewertungsreserven nicht nachvollziehbar
- Tarifgeneration verwechselt
- BaFin-Aufsicht mit Individualanspruch verwechselt

## Anschluss-Skills

- vag-bafin-aufsicht-beschwerde-missstand
- solvency-ii-scr-orsa-aufsichtsrecht

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `nachhaltigkeit-taxonomie-sfdr-versicherungsprodukt`

**Fokus:** Nachhaltigkeits- und ESG-Angaben bei Versicherungsanlageprodukten: Taxonomie, SFDR, Greenwashing, Produktfreigabe und Vertrieb.

# Nachhaltigkeit bei Versicherungsprodukten

## Einsatz

Für Lebens-/Rentenversicherungsprodukte mit Fonds/ESG-Versprechen und Vertriebsunterlagen.

## Norm- und Quellenanker

SFDR; Taxonomie-VO; IDD; VAG/VVG Informationspflichten; UWG; BaFin-Verlautbarungen live prüfen.

## Arbeitsfragen

1. Welche Nachhaltigkeitsaussage wird gemacht?
2. Ist das Produkt Versicherungsanlageprodukt?
3. Welche Offenlegungspflichten treffen Hersteller und Vertrieb?
4. Besteht Greenwashing- oder Haftungsrisiko?

## Output

ESG-Disclosure-Check, Vertriebsfreigabe, Risikomemo und Korrekturvorschläge.

## Red Flags

- Marketingversprechen stärker als Anlagepolitik
- SFDR-Kategorie falsch verstanden
- Taxonomiequote nicht belegbar
- Beratung dokumentiert ESG-Wunsch nicht

## Anschluss-Skills

- idd-vertrieb-beratung-dokumentation
- vag-bafin-aufsicht-beschwerde-missstand

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
