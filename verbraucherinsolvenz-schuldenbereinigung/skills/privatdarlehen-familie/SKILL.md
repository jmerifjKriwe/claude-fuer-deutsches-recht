---
name: privatdarlehen-familie
description: "Privatdarlehen Familie im Plugin Verbraucherinsolvenz Schuldenbereinigung: prüft konkret Privatdarlehen in Familie und Freundeskreis, Restschuldbefreiungsantrag, SCHUFA/Auskunfteien nach Insolvenz. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Privatdarlehen Familie

## Arbeitsbereich

Dieser Skill behandelt **Privatdarlehen Familie** als zusammenhängenden Arbeitsgang im Plugin Verbraucherinsolvenz Schuldenbereinigung. Im Mittelpunkt steht die Prüfung von Privatdarlehen in Familie und Freundeskreis, Restschuldbefreiungsantrag, SCHUFA/Auskunfteien nach Insolvenz. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `privatdarlehen-familie` | Privatdarlehen in Familie und Freundeskreis: Beweis, Gleichbehandlung, Scham, Unterlagen und Planquote.; Normanker: InsO Forderungsanmeldung; BGB Darlehen; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |
| `restschuldbefreiungsantrag` | Restschuldbefreiungsantrag: Frist, Wirkung, Laufzeit, Obliegenheiten und gefährliche Altfehler.; Normanker: InsO §§ 286-303 und 287 und 300; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |
| `schufa-und-auskunfteien` | SCHUFA/Auskunfteien nach Insolvenz: Löschung, Restschuldbefreiung, falsche Einträge und Datenschutzbeschwerde.; Normanker: DSGVO Art. 5 und 6 und 16 und 17; BDSG; InsO RSB; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung. |

## Arbeitsweg

- Rolle und Ziel im Verbraucherinsolvenz Schuldenbereinigung klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `privatdarlehen-familie`

**Fokus:** Privatdarlehen in Familie und Freundeskreis: Beweis, Gleichbehandlung, Scham, Unterlagen und Planquote.; Normanker: InsO Forderungsanmeldung; BGB Darlehen; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Privatdarlehen in Familie und Freundeskreis: Beweis, Gleichbehandlung, Scham, Unterlagen und Planquote.

## Fachkern: Privatdarlehen in Familie und Freundeskreis: Beweis, Gleichbehandlung, Scham, Unterlagen und Planquote.
- **Spezialgegenstand:** Privatdarlehen in Familie und Freundeskreis: Beweis, Gleichbehandlung, Scham, Unterlagen und Planquote.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO Forderungsanmeldung; BGB Darlehen. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

## Arbeitsfragen

1. Geht es um Verbraucherinsolvenz, ehemalige Selbstständigkeit oder Regelinsolvenz?
2. Welche Gläubiger, Titel, Pfändungen, Inkassoschreiben, Steuern, Unterhalts- oder Deliktforderungen existieren?
3. Gibt es laufende Vollstreckung, Kontosperre, Mietrückstand, Stromsperre oder Arbeitsplatzrisiko?
4. Liegt ein außergerichtlicher Einigungsversuch vor oder muss er vorbereitet werden?
5. Welche Unterlagen fehlen für Antrag, Plan, Bescheinigung, Stundung und Restschuldbefreiung?

## Vorgehen

- Zuerst Existenz sichern: Konto, Miete, Energie, Krankenversicherung, Unterhalt, Arbeit.
- Danach Gläubigerliste, Forderungsgrund, Titel, Sicherheiten und § 302-Risiken erfassen.
- Dann Plan bauen: Nullplan, Quote, Drittmittel, Einmalzahlung oder dynamische Rate.
- Bei Antragstellung Formulare, Anlagen, RSB-Antrag und Stundung getrennt abhaken.
- In der Wohlverhaltensphase Obliegenheiten als Kalender und nicht als abstrakte Belehrung führen.

## Ergebnisformate

- Unterlagenliste, Gläubigertabelle, Planentwurf, Anschreiben, Gerichtsantrag-Check, P-Konto-Notfallplan, Red-Team-Vermerk oder Laienerklärung.

## 2. `restschuldbefreiungsantrag`

**Fokus:** Restschuldbefreiungsantrag: Frist, Wirkung, Laufzeit, Obliegenheiten und gefährliche Altfehler.; Normanker: InsO §§ 286-303 und 287 und 300; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# Restschuldbefreiungsantrag: Frist, Wirkung, Laufzeit, Obliegenheiten und gefährliche Altfehler.

## Fachkern: Restschuldbefreiungsantrag: Frist, Wirkung, Laufzeit, Obliegenheiten und gefährliche Altfehler.
- **Spezialgegenstand:** Restschuldbefreiungsantrag: Frist, Wirkung, Laufzeit, Obliegenheiten und gefährliche Altfehler.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO §§ 286-303, 287, 300. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

## Arbeitsfragen

1. Geht es um Verbraucherinsolvenz, ehemalige Selbstständigkeit oder Regelinsolvenz?
2. Welche Gläubiger, Titel, Pfändungen, Inkassoschreiben, Steuern, Unterhalts- oder Deliktforderungen existieren?
3. Gibt es laufende Vollstreckung, Kontosperre, Mietrückstand, Stromsperre oder Arbeitsplatzrisiko?
4. Liegt ein außergerichtlicher Einigungsversuch vor oder muss er vorbereitet werden?
5. Welche Unterlagen fehlen für Antrag, Plan, Bescheinigung, Stundung und Restschuldbefreiung?

## Vorgehen

- Zuerst Existenz sichern: Konto, Miete, Energie, Krankenversicherung, Unterhalt, Arbeit.
- Danach Gläubigerliste, Forderungsgrund, Titel, Sicherheiten und § 302-Risiken erfassen.
- Dann Plan bauen: Nullplan, Quote, Drittmittel, Einmalzahlung oder dynamische Rate.
- Bei Antragstellung Formulare, Anlagen, RSB-Antrag und Stundung getrennt abhaken.
- In der Wohlverhaltensphase Obliegenheiten als Kalender und nicht als abstrakte Belehrung führen.

## Ergebnisformate

- Unterlagenliste, Gläubigertabelle, Planentwurf, Anschreiben, Gerichtsantrag-Check, P-Konto-Notfallplan, Red-Team-Vermerk oder Laienerklärung.

## 3. `schufa-und-auskunfteien`

**Fokus:** SCHUFA/Auskunfteien nach Insolvenz: Löschung, Restschuldbefreiung, falsche Einträge und Datenschutzbeschwerde.; Normanker: DSGVO Art. 5 und 6 und 16 und 17; BDSG; InsO RSB; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine fuer Verbraucherinsolvenz und Schuldenbereinigung.

# SCHUFA/Auskunfteien nach Insolvenz: Löschung, Restschuldbefreiung, falsche Einträge und Datenschutzbeschwerde.

## Fachkern: SCHUFA/Auskunfteien nach Insolvenz: Löschung, Restschuldbefreiung, falsche Einträge und Datenschutzbeschwerde.
- **Spezialgegenstand:** SCHUFA/Auskunfteien nach Insolvenz: Löschung, Restschuldbefreiung, falsche Einträge und Datenschutzbeschwerde.. Die Prüfung setzt bei der konkreten Sachfrage an und endet mit einem verwertbaren Arbeitsergebnis.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.


## Auftrag

Dieser Skill arbeitet im Plugin **Verbraucherinsolvenz und Schuldenbereinigung**. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

DSGVO Art. 5, 6, 16, 17; BDSG; InsO RSB. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

## Arbeitsfragen

1. Geht es um Verbraucherinsolvenz, ehemalige Selbstständigkeit oder Regelinsolvenz?
2. Welche Gläubiger, Titel, Pfändungen, Inkassoschreiben, Steuern, Unterhalts- oder Deliktforderungen existieren?
3. Gibt es laufende Vollstreckung, Kontosperre, Mietrückstand, Stromsperre oder Arbeitsplatzrisiko?
4. Liegt ein außergerichtlicher Einigungsversuch vor oder muss er vorbereitet werden?
5. Welche Unterlagen fehlen für Antrag, Plan, Bescheinigung, Stundung und Restschuldbefreiung?

## Vorgehen

- Zuerst Existenz sichern: Konto, Miete, Energie, Krankenversicherung, Unterhalt, Arbeit.
- Danach Gläubigerliste, Forderungsgrund, Titel, Sicherheiten und § 302-Risiken erfassen.
- Dann Plan bauen: Nullplan, Quote, Drittmittel, Einmalzahlung oder dynamische Rate.
- Bei Antragstellung Formulare, Anlagen, RSB-Antrag und Stundung getrennt abhaken.
- In der Wohlverhaltensphase Obliegenheiten als Kalender und nicht als abstrakte Belehrung führen.

## Ergebnisformate

- Unterlagenliste, Gläubigertabelle, Planentwurf, Anschreiben, Gerichtsantrag-Check, P-Konto-Notfallplan, Red-Team-Vermerk oder Laienerklärung.
