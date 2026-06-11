# Megaprompt: verbraucherinsolvenz-schuldenbereinigung

> *Achtung: Dies ist ein experimentelles Mega-Prompt-Markdown, das einen kompletten Klotzkette-Plugin in eine einzige Datei zusammenfuehrt. Keine Haftung, keine Gewaehr. Nur zum Ausprobieren der Skills auch ohne Claude Code; keine Rechtsberatung. Vor Verwendung im Mandat anwaltlich pruefen.*
>
> *Caution: This is an experimental Mega-Prompt Markdown that consolidates a full Klotzkette plugin into a single file. No warranty, no liability. For exploration with chat tools that do not run Claude Code only; not legal advice.*

**Verwendung:** Diesen gesamten Text in einen Chat ohne Claude-Code-Integration einfuegen (oder als Datei hochladen). Der Chat-Agent erhaelt damit die gebuendelten Skills dieses Plugins als Kontext. Eine Replikation des vollen Plugin-Verhaltens ist nicht garantiert — der Megaprompt ist eine Best-Effort-Kompression.


## Zusammensetzung

Dieser Megaprompt enthaelt top-15 von 68 Skills des Plugins `verbraucherinsolvenz-schuldenbereinigung`.

## Inhaltsverzeichnis

1. **unterlagen-und-schuldeninventar** — Unterlagen- und Schuldeninventar: Gläubiger, Forderungsgrund, Titel, Inkasso, Vollstreckung, Sicherheiten und bestritten…
2. **kaltstart-schuldenbild-glaeubiger-sofortschutz** — Kaltstart Verbraucherinsolvenz: Schuldenbild, Einkommen, Unterhalt, Wohnung, Selbstständigkeit, Gläubigerliste, Beratung…
3. **red-team-antrag** — Red-Team des Verbraucherinsolvenzantrags: Lücken, falsche Gläubigeradresse, § 302-Risiko, fehlender RSB-Antrag.; Normank…
4. **red-team-obliegenheiten** — Red-Team der Wohlverhaltensphase: Umzug, Job, Erbschaft, Sonderzahlung, neue Schulden und Informationspflicht.; Normanke…
5. **red-team-plan** — Red-Team des Schuldenbereinigungsplans: unrealistische Quote, vergessene Forderung, falsche Mehrheit, Formfehler.; Norma…
6. **verbraucher-oder-regelinsolvenz** — Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz: ehemalige Selbstständige, überschaubare Vermögensverhältnisse, Arbe…
7. **verbraucherinsolvenz-versagungsgruende** — Verbraucherinsolvenz: Versagungsgruende: Skill behandelt § 290 InsO Versagung der Restschuldbefreiung Tatbestaende Straf…
8. **verbraucherinsolvenz-treuhaender-rolle** — Verbraucherinsolvenz: Rolle des Treuhaenders: Skill behandelt die Aufgaben des Treuhaenders in der Wohlverhaltensphase V…
9. **verbraucherinsolvenz-3-jahres-restschuldbefreiung** — Verbraucherinsolvenz: 3-Jahres-Restschuldbefreiung: Skill behandelt die seit 01.10.2020 geltende verkuerzte Frist auf dr…
10. **verbraucherinsolvenz-pfaendungsschutzkonto** — Verbraucherinsolvenz: Pfaendungsschutzkonto P-Konto: Skill klaert die rechtliche Konstruktion des Pfaendungsschutzkontos…
11. **verbraucherinsolvenz-unterhalt-und-insolvenz** — Verbraucherinsolvenz und eheliche Unterhaltspflicht: Skill behandelt das Verhaeltnis von laufender Unterhaltspflicht zum…
12. **verbraucherinsolvenz-belegchaos-strukturieren** — Schuldnerberatungsstelle: Strukturierung des Belegchaos: Skill liefert die Methodik wie Schuldnerberater die ungeordnete…
13. **verbraucherinsolvenz-aussergerichtl-schuldenbereinigung** — Aussergerichtlicher Schuldenbereinigungsplan nach §§ 305 InsO: Skill leitet durch die Erstellung des ersten Vergleichsvo…
14. **verbraucherinsolvenz-nachtraegliche-glaeubiger** — Verbraucherinsolvenz: Nachtraegliche Glaeubiger nach Restschuldbefreiung: Skill klaert ob nicht angemeldete Glaeubiger n…
15. **vorzeitige-restschuldbefreiung** — Vorzeitige Restschuldbefreiung: Kosten, Gläubigerbefriedigung, Anträge und Timing: Normanker: InsO § 300; liefert konkre…

---

## Skill: `unterlagen-und-schuldeninventar`

_Unterlagen- und Schuldeninventar: Gläubiger, Forderungsgrund, Titel, Inkasso, Vollstreckung, Sicherheiten und bestrittene Forderungen beweisfest erfassen.; Normanker: InsO § 305 Abs. 1; InsO §§ 174 ff.; ZPO Vollstreckungstitel; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textb..._

# Unterlagen- und Schuldeninventar: Gläubiger, Forderungsgrund, Titel, Inkasso, Vollstreckung, Sicherheiten und bestrittene Forderungen beweisfest erfassen.

## Fachkern: Unterlagen- und Schuldeninventar: Gläubiger, Forderungsgrund, Titel, Inkasso, Vollstreckung, Sicherheiten und bestrittene Forderungen beweisfest erfassen.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO § 305 Abs. 1; InsO §§ 174 ff.; ZPO Vollstreckungstitel. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

---

## Skill: `kaltstart-schuldenbild-glaeubiger-sofortschutz`

_Kaltstart Verbraucherinsolvenz: Schuldenbild, Einkommen, Unterhalt, Wohnung, Selbstständigkeit, Gläubigerliste, Beratungsstelle und Sofortschutz sortieren.; Normanker: InsO §§ 304-314 und 286-303; ZPO §§ 850 ff.; SGB-Schnittstellen; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und..._

# Kaltstart Verbraucherinsolvenz: Schuldenbild, Einkommen, Unterhalt, Wohnung, Selbstständigkeit, Gläubigerliste, Beratungsstelle und Sofortschutz sortieren.

## Fachkern: Kaltstart Verbraucherinsolvenz: Schuldenbild, Einkommen, Unterhalt, Wohnung, Selbstständigkeit, Gläubigerliste, Beratungsstelle und Sofortschutz sortieren.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO §§ 304-314, 286-303; ZPO §§ 850 ff.; SGB-Schnittstellen. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

---

## Skill: `red-team-antrag`

_Red-Team des Verbraucherinsolvenzantrags: Lücken, falsche Gläubigeradresse, § 302-Risiko, fehlender RSB-Antrag.; Normanker: InsO §§ 305 und 287 und 290 und 302; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung._

# Red-Team des Verbraucherinsolvenzantrags: Lücken, falsche Gläubigeradresse, § 302-Risiko, fehlender RSB-Antrag.

## Fachkern: Red-Team des Verbraucherinsolvenzantrags: Lücken, falsche Gläubigeradresse, § 302-Risiko, fehlender RSB-Antrag.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO §§ 305, 287, 290, 302. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

---

## Skill: `red-team-obliegenheiten`

_Red-Team der Wohlverhaltensphase: Umzug, Job, Erbschaft, Sonderzahlung, neue Schulden und Informationspflicht.; Normanker: InsO §§ 295 und 296 und 297a; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung._

# Red-Team der Wohlverhaltensphase: Umzug, Job, Erbschaft, Sonderzahlung, neue Schulden und Informationspflicht.

## Fachkern: Red-Team der Wohlverhaltensphase: Umzug, Job, Erbschaft, Sonderzahlung, neue Schulden und Informationspflicht.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO §§ 295, 296, 297a. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

---

## Skill: `red-team-plan`

_Red-Team des Schuldenbereinigungsplans: unrealistische Quote, vergessene Forderung, falsche Mehrheit, Formfehler.; Normanker: InsO §§ 305 und 307-309; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung._

# Red-Team des Schuldenbereinigungsplans: unrealistische Quote, vergessene Forderung, falsche Mehrheit, Formfehler.

## Fachkern: Red-Team des Schuldenbereinigungsplans: unrealistische Quote, vergessene Forderung, falsche Mehrheit, Formfehler.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO §§ 305, 307-309. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

---

## Skill: `verbraucher-oder-regelinsolvenz`

_Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz: ehemalige Selbstständige, überschaubare Vermögensverhältnisse, Arbeitnehmerforderungen und Geschäftsführer-Vergangenheit: Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz: ehemalige Selbstständige, üb..._

# Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz: ehemalige Selbstständige, überschaubare Vermögensverhältnisse, Arbeitnehmerforderungen und Geschäftsführer-Vergangenheit.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz: ehemalige Selbstständige, überschaubare Vermögensverhältnisse, Arbeitnehmerforderungen und Geschäftsführer-Vergangenheit.; Normanker: InsO § 304; § 15a InsO als Altlast; Forderungsstruktur; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung.

## Fachkern: Abgrenzung Verbraucherinsolvenz oder Regelinsolvenz: ehemalige Selbstständige, überschaubare Vermögensverhältnisse, Arbeitnehmerforderungen und Geschäftsführer-Vergangenheit.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO § 304; § 15a InsO als Altlast; Forderungsstruktur. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

---

## Skill: `verbraucherinsolvenz-versagungsgruende`

_Verbraucherinsolvenz: Versagungsgruende: Skill behandelt § 290 InsO Versagung der Restschuldbefreiung Tatbestaende Strafurteile Vermoegensverlagerung Verletzung Aufklaerungspflicht und Erwerbsobliegenheit. Verteidigu..._

# Verbraucherinsolvenz: Versagungsgruende


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Verbraucherinsolvenz: Versagungsgruende. Skill behandelt § 290 InsO Versagung der Restschuldbefreiung Tatbestaende Strafurteile Vermoegensverlagerung Verletzung Aufklaerungspflicht und Erwerbsobliegenheit. Verteidigungsstrategien. Liefert Pruefraster.

### Verbraucherinsolvenz Versagungsgruende

## Fachkern: Verbraucherinsolvenz Versagungsgruende
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Norm

- § 290 InsO.

## Tatbestaende

### § 290 Abs. 1 Nr. 1 InsO
- Strafurteil wegen § 283 ff. StGB Bankrott.

### § 290 Abs. 1 Nr. 2 InsO
- Verletzung Aufklaerungspflicht im Antrag.

### § 290 Abs. 1 Nr. 3 InsO
- Vermoegensverschiebung in 10 Jahren vor Antrag.

### § 290 Abs. 1 Nr. 4 InsO
- Letzte 10 Jahre eine Restschuldbefreiung erteilt.

### § 290 Abs. 1 Nr. 5 InsO
- Verletzung Erwerbsobliegenheit.

### § 290 Abs. 1 Nr. 6 InsO
- Unrichtige oder unvollstaendige Vermoegensaufstellung.

## Verteidigungsstrategien

- Pruefen des Tatbestands.
- Verschulden des Schuldners?
- Geringfuegigkeit (Bagatellgrenze in einzelnen Faellen).
- Glaeubiger-Stellungnahme einholen.

## Pruefraster

1. Welcher Tatbestand?
2. Verschulden?
3. Bagatelle?
4. Verfahrensgang?

---

## Skill: `verbraucherinsolvenz-treuhaender-rolle`

_Verbraucherinsolvenz: Rolle des Treuhaenders: Skill behandelt die Aufgaben des Treuhaenders in der Wohlverhaltensphase Vermoegensaufsicht Verteilung Forderungspruefung Glaeubigerinformation. Verguetung und Koste..._

# Verbraucherinsolvenz: Rolle des Treuhaenders


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Verbraucherinsolvenz: Rolle des Treuhaenders. Skill behandelt die Aufgaben des Treuhaenders in der Wohlverhaltensphase Vermoegensaufsicht Verteilung Forderungspruefung Glaeubigerinformation. Verguetung und Kostenfragen. Liefert Pruefraster.

### Verbraucherinsolvenz Treuhaender Rolle

## Fachkern: Verbraucherinsolvenz Treuhaender Rolle
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Norm

- §§ 292 ff. InsO Treuhaender.
- § 293 InsO Bestellung.
- § 295 InsO Aufgaben.

## Aufgaben

### Vermoegensaufsicht
- Empfang der monatlichen Abfuehrungen.
- Pruefung auf Erfuellung der Mitwirkungspflichten.

### Forderungspruefung
- Anmeldung Pruefung.
- Bestreitung bei zweifelhaften Forderungen.

### Glaeubigerinformation
- Jahresberichte.
- Schlussbericht.

### Verteilung
- Quotale Verteilung der Massen.

## Verguetung

- § 14 InsVV Insolvenzrechtsverguetungsverordnung.
- Mindestverguetung 100 Euro/Jahr für Treuhaender in Verbraucherinsolvenz.

## Pruefraster

1. Treuhaenderaufgaben sauber abgegrenzt?
2. Pflichtverletzungen?
3. Verguetung angemessen?

---

## Skill: `verbraucherinsolvenz-3-jahres-restschuldbefreiung`

_Verbraucherinsolvenz: 3-Jahres-Restschuldbefreiung: Skill behandelt die seit 01.10.2020 geltende verkuerzte Frist auf drei Jahre Voraussetzungen Versagungsgruende Mitwirkungspflichten Verfahrensgang. Aktue..._

# Verbraucherinsolvenz: 3-Jahres-Restschuldbefreiung


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Verbraucherinsolvenz: 3-Jahres-Restschuldbefreiung. Skill behandelt die seit 01.10.2020 geltende verkuerzte Frist auf drei Jahre Voraussetzungen Versagungsgruende Mitwirkungspflichten Verfahrensgang. Aktuelle Diskussion zur Folgen bei nachtraeglich auftauchenden Glaeubigern. Liefert Pruefraster.

### Verbraucherinsolvenz 3 Jahres Restschuldbefreiung

## Fachkern: Verbraucherinsolvenz 3 Jahres Restschuldbefreiung
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Norm

- § 287 Abs. 2 InsO (Frist 3 Jahre seit 01.10.2020).
- Insolvenzrechtsreform-Gesetz vom 22.12.2020.

## Voraussetzungen

- Verbraucher- oder Regelinsolvenz.
- Wohlverhaltensphase: Mitwirkungspflichten.
- Keine Versagungsgruende (§ 290 InsO).

## Wohlverhaltensphase

### Pflichten
- Erwerbsobliegenheit.
- Abfuehrungspflicht (Pfaendungsbetrag).
- Meldepflicht bei Wohnsitz-/Berufswechsel.
- Auskunftspflicht.
- Erbschaftspflicht (50 Prozent der Erbschaft).
- Treuhaender informieren.

### Verstoss
- Versagungsgrund § 290 InsO.
- Treuhaender beantragt Aufhebung.

## Versagungsgruende § 290 InsO

- Verurteilung wegen § 283 ff. StGB Bankrottdelikte.
- Schaedigende Vermoegensverlagerung.
- Verletzung von Aufklaerungspflichten.
- Verletzung der Erwerbsobliegenheit.

## Nachtraeglich auftauchende Glaeubiger

- § 301 InsO: Restschuldbefreiung wirkt auch für nicht angemeldete Glaeubiger.
- Ausnahme: arglistig verschwiegene Forderungen (§ 302 InsO).

## Pruefraster

1. Verfahrensgang korrekt?
2. Mitwirkungspflichten erfuellt?
3. Versagungsgruende ausgeschlossen?
4. Nachtraegliche Glaeubiger ueberraschen?

---

## Skill: `verbraucherinsolvenz-pfaendungsschutzkonto`

_Verbraucherinsolvenz: Pfaendungsschutzkonto P-Konto: Skill klaert die rechtliche Konstruktion des Pfaendungsschutzkontos nach §§ 850k 850l ZPO Grundfreibetraege Erhoehungsbetraege Antrag und Beweisfuehrun..._

# Verbraucherinsolvenz: Pfaendungsschutzkonto P-Konto


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Verbraucherinsolvenz: Pfaendungsschutzkonto P-Konto. Skill klaert die rechtliche Konstruktion des Pfaendungsschutzkontos nach §§ 850k 850l ZPO Grundfreibetraege Erhoehungsbetraege Antrag und Beweisfuehrung sowie Wechselwirkung mit Insolvenzverfahren. Liefert Pruefraster.

### Verbraucherinsolvenz Pfaendungsschutzkonto

## Fachkern: Verbraucherinsolvenz Pfaendungsschutzkonto
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Norm

- §§ 850k, 850l ZPO.
- Pfaendungsfreigrenzen-Bekanntmachung jaehrlich neu.

## Grundfreibetrag

- Aktueller Grundfreibetrag 2024: 1.499,99 Euro/Monat (live im Mandat verifizieren).
- Erhoehungsbetraege für Unterhaltsverpflichtungen.

## Erhoehungsbetraege

- Pro unterhaltsberechtigte Person ca. 560 Euro/Monat (live verifizieren).
- Sozialleistungsbezug komplett geschuetzt.
- Kindergeld vollstaendig geschuetzt.

## Antrag

- Bei der Bank: Umwandlung in P-Konto.
- Bescheinigung der Beratungsstelle ueber Unterhaltslast.
- Vollstreckungsgericht bei besonderem Bedarf.

## Wechselwirkung Insolvenzverfahren

- P-Konto-Schutz neben Insolvenzverfahren.
- Nicht Schuldnerkonto wechseln, sondern bestehendes Konto umwandeln.

## Pruefraster

1. P-Konto eingerichtet?
2. Grundfreibetrag korrekt?
3. Erhoehungsbetraege beantragt?
4. Bankkommunikation?

---

## Skill: `verbraucherinsolvenz-unterhalt-und-insolvenz`

_Verbraucherinsolvenz und eheliche Unterhaltspflicht: Skill behandelt das Verhaeltnis von laufender Unterhaltspflicht zum Insolvenzverfahren Pflichten in der Wohlverhaltensphase Anrechnung und Rangordnung...._

# Verbraucherinsolvenz und eheliche Unterhaltspflicht


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Verbraucherinsolvenz und eheliche Unterhaltspflicht. Skill behandelt das Verhaeltnis von laufender Unterhaltspflicht zum Insolvenzverfahren Pflichten in der Wohlverhaltensphase Anrechnung und Rangordnung. Liefert Pruefraster.

### Verbraucherinsolvenz Unterhalt Und Insolvenz

## Fachkern: Verbraucherinsolvenz Unterhalt Und Insolvenz
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Norm

- §§ 1601 ff. BGB Familienunterhalt.
- §§ 287, 295 InsO Mitwirkung in Wohlverhaltensphase.

## Laufende Unterhaltspflicht

- Unterhalt aus Erwerbseinkommen ist nicht der Insolvenzmasse zugeordnet.
- § 850d ZPO: privilegierte Pfaendbarkeit für Unterhalt; bevorrechtigter Anspruch.

## Unterhaltsrueckstaende vor Insolvenzantrag

- Werden als Insolvenzforderung behandelt.
- § 302 Nr. 3 InsO: Unterhaltsrueckstaende vor Insolvenzverfahren nehmen nicht an der Restschuldbefreiung teil.

## Erwerbsobliegenheit

- Pflicht zur vollen Erwerbstaetigkeit auch zur Unterhaltsleistung.

## Pruefraster

1. Laufender oder rueckstaendiger Unterhalt?
2. Rangordnung?
3. Erwerbsobliegenheit erfuellt?
4. § 850d ZPO-Pfaendung?

---

## Skill: `verbraucherinsolvenz-belegchaos-strukturieren`

_Schuldnerberatungsstelle: Strukturierung des Belegchaos: Skill liefert die Methodik wie Schuldnerberater die ungeordneten Belege Mahnungen Vollstreckungsbescheide Inkassobriefe und Bankauszuege des Sc..._

# Schuldnerberatungsstelle: Strukturierung des Belegchaos


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Schuldnerberatungsstelle: Strukturierung des Belegchaos. Skill liefert die Methodik wie Schuldnerberater die ungeordneten Belege Mahnungen Vollstreckungsbescheide Inkassobriefe und Bankauszuege des Schuldners in eine geordnete Glaeubiger- und Forderungsliste ueberfuehren. Liefert Checkliste und Vorlagenstruktur.

### Verbraucherinsolvenz Belegchaos Strukturieren

## Fachkern: Verbraucherinsolvenz Belegchaos Strukturieren
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Ausgangslage

- Schuldner bringt Plastiktueten / Schuhkartons mit ungeordneten Unterlagen.
- Belege oft jahrealt, teils nicht mehr lesbar.
- Glaeubiger zum Teil unbekannt oder Mehrfacheintraege durch Inkasso-Kette.

## Workflow

### Schritt 1: Sortieren in Kategorien
- Forderungen (Mahnungen, Rechnungen, Vollstreckungsbescheide).
- Vertraege (Mietvertrag, Kreditvertrag, Telefonvertrag).
- Behörden (Finanzamt, Krankenkasse, Sozialamt).
- Konten (Bankauszuege, Sparbuecher).
- Einkommen (Gehaltsabrechnungen, Sozialleistungen).
- Sonstiges (Schriftverkehr, Notizen).

### Schritt 2: Glaeubigerliste anlegen
- Pro Glaeubiger eine Zeile.
- Spalten: Name, Adresse, Hauptforderung, Zinsen, Kosten, Aktenzeichen, Datum letzter Vollstreckungsakt.
- Inkasso-Ketten zusammenfuehren (Originalglaeubiger -> Inkasso 1 -> Inkasso 2).

### Schritt 3: Auskunft einholen
- Schufa-Selbstauskunft (kostenfrei).
- Schuldnerverzeichnis bei Vollstreckungsgerichten.
- Bankkonten-Abfrage.
- Anfrage an bekannte Glaeubiger nach aktuellem Forderungsstand.

### Schritt 4: Forderungen pruefen
- Verjährung (§§ 195, 199 BGB; vollstreckbare Titel 30 Jahre § 197 BGB).
- Bestreitbare Forderungen.
- Doppelte Forderungen.

### Schritt 5: Vermoegen erfassen
- Bankkonten, Sparbuecher, Lebensversicherungen, Bausparvertraege.
- Hausrat, Pkw, ggf. Immobilien.
- Pfaendungsfreies Einkommen.

## Werkzeuge

- Excel-Tabelle "Glaeubigerliste".
- Excel-Tabelle "Vermoegensaufstellung".
- Excel-Tabelle "Einkommensberechnung".
- Standardformbriefe an Glaeubiger.
- Verschluesselte Datenablage.

## Aktenfuehrung

- Eigene Mandatsakte mit Originalen / Kopien.
- Versionierung der Vermoegens- und Schuldenliste.
- Datenschutz: DSGVO Art. 30 Verzeichnis von Verarbeitungstaetigkeiten.

## Pruefraster

1. Belege vollstaendig?
2. Glaeubigerliste sauber?
3. Verjährungspruefung erfolgt?
4. Vermoegensaufstellung erstellt?
5. Einkommensberechnung erstellt?

---

## Skill: `verbraucherinsolvenz-aussergerichtl-schuldenbereinigung`

_Aussergerichtlicher Schuldenbereinigungsplan nach §§ 305 InsO: Skill leitet durch die Erstellung des ersten Vergleichsvorschlags von der Vermoegens- und Schuldenliste ueber die Quotenberechnung..._

# Aussergerichtlicher Schuldenbereinigungsplan nach §§ 305 InsO


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Aussergerichtlicher Schuldenbereinigungsplan nach §§ 305 InsO. Skill leitet durch die Erstellung des ersten Vergleichsvorschlags von der Vermoegens- und Schuldenliste ueber die Quotenberechnung bis zur formalen Vorlage an die Glaeubiger. Behandelt Pflicht zur Beilage Bescheinigung der geeigneten Stelle / des geeigneten Beraters. Liefert Vorlagenstruktur und Pruefraster.

### Verbraucherinsolvenz Aussergerichtl Schuldenbereinigung

## Fachkern: Verbraucherinsolvenz Aussergerichtl Schuldenbereinigung
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Norm

- § 305 InsO (Insolvenzverordnung).
- Schuldnerberatungsstellen-Recht der Länder.

## Voraussetzungen

- Schuldner ist Verbraucher (kein selbststaendiges Wirtschaftsleben).
- Erfolglose aussergerichtliche Einigung nach § 305 Abs. 1 Nr. 1 InsO.

## Erstellung des Vergleichsvorschlags

### Schritt 1: Vermoegens- und Schuldenliste
- Gesamtschuldenstand mit Glaeubigern, Hauptforderung, Kosten, Zinsen.
- Verfuegbares Einkommen unter Beruecksichtigung der Pfaendungsfreigrenzen (§ 850c ZPO i.V.m. Pfaendungstabelle).
- Verfuegbare Aktiva (Bankkonten, Pkw, Hausrat, ggf. Wohnung).

### Schritt 2: Quotenberechnung
- Realistisch erfuellbare Quote.
- Typische Spanne 0-30 Prozent.
- Sondervorschriften für einzelne Glaeubigertypen (z. B. Finanzamt nach AO).

### Schritt 3: Vergleichsvorschlag
- Form: Schriftlich.
- Inhalt: Hoehe der Quote, Zahlungsmodalitaet (Einmalzahlung, Monatsraten), Laufzeit (max. 6-Monate Plan), Restschuldbefreiung.

### Schritt 4: Beilagen
- Bescheinigung der geeigneten Stelle (anerkannte Schuldnerberatungsstelle, Rechtsanwalt, Steuerberater).
- Vermoegens- und Schuldenliste.
- Einkommensnachweise.

## Vorgehen bei Glaeubigerantworten

- Annahme aller Glaeubiger: aussergerichtliche Einigung erfolgreich.
- Ablehnung durch einzelnen Glaeubiger: gerichtliches Verfahren nach § 306 InsO.

## Pruefraster

1. Vermoegens- und Schuldenliste vollstaendig?
2. Quote realistisch?
3. Bescheinigung vorhanden?
4. Glaeubigerantworten dokumentiert?

---

## Skill: `verbraucherinsolvenz-nachtraegliche-glaeubiger`

_Verbraucherinsolvenz: Nachtraegliche Glaeubiger nach Restschuldbefreiung: Skill klaert ob nicht angemeldete Glaeubiger nach Erteilung der Restschuldbefreiung noch Anspruch geltend mac..._

# Verbraucherinsolvenz: Nachtraegliche Glaeubiger nach Restschuldbefreiung


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Verbraucherinsolvenz: Nachtraegliche Glaeubiger nach Restschuldbefreiung. Skill klaert ob nicht angemeldete Glaeubiger nach Erteilung der Restschuldbefreiung noch Anspruch geltend machen koennen § 301 InsO und Ausnahmen § 302 InsO. Liefert Pruefraster.

### Verbraucherinsolvenz Nachtraegliche Glaeubiger

## Fachkern: Verbraucherinsolvenz Nachtraegliche Glaeubiger
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Norm

- § 301 InsO: Wirkung der Restschuldbefreiung gegenueber allen Glaeubigern.
- § 302 InsO: Ausnahmen.

## Wirkung

- Restschuldbefreiung wirkt auch für Glaeubiger, die ihre Forderung nicht angemeldet haben.

## Ausnahmen § 302 InsO

### Nr. 1: Arglistig verschwiegen
- Schuldner hat die Forderung in der Vermoegensaufstellung arglistig nicht angegeben.

### Nr. 2: Vorsaetzliche unerlaubte Handlung
- Forderung aus vorsaetzlicher unerlaubter Handlung (§§ 823 ff. BGB).

### Nr. 3: Unterhaltsforderungen
- Unterhalt für Zeitraum vor Insolvenzverfahren.

### Nr. 4: Geldstrafen Geldbussen
- Geldstrafen und Geldbussen.

## Pruefraster

1. Forderung angemeldet?
2. Wenn nicht: Aussnahme nach § 302 InsO?
3. Vorsatz / Arglist?
4. Verjährung?

---

## Skill: `vorzeitige-restschuldbefreiung`

_Vorzeitige Restschuldbefreiung: Kosten, Gläubigerbefriedigung, Anträge und Timing: Normanker: InsO § 300; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Te..._

# Vorzeitige Restschuldbefreiung: Kosten, Gläubigerbefriedigung, Anträge und Timing.


## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: InsO — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.

**Fokus:** Vorzeitige Restschuldbefreiung: Kosten, Gläubigerbefriedigung, Anträge und Timing.; Normanker: InsO § 300; liefert konkrete Fragen, Dokumentenliste, Entscheidungsbaum und Textbausteine für Verbraucherinsolvenz und Schuldenbereinigung.

## Fachkern: Vorzeitige Restschuldbefreiung: Kosten, Gläubigerbefriedigung, Anträge und Timing.
- **Normen-/Quellenanker:** InsO Verbraucherinsolvenz, außergerichtlicher Einigungsversuch, Schuldenbereinigungsplan, P-Konto, Restschuldbefreiung, Forderungsanmeldung und Pfändungsschutz.
- **Entscheidende Weiche:** Schuldnerstatus, Gläubigerliste, Forderungstyp, pfändbares Einkommen, Vergleichsquote, Obliegenheiten und Antragsreife trennen.
- **Arbeitsprodukt:** Erzeuge eine konkrete Prüf- oder Entscheidungsmatrix mit Norm, Tatbestand, Beleg, Einwand, Risikoampel und nächstem Schritt; Anschluss-Skills nur bei echter Vertiefung nennen.

## Auftrag

Dieser Skill arbeitet. Er soll Laien, Schuldnerberatung, Anwältinnen und Angehörigen helfen, eine echte Akte sauber zu ordnen, ohne falsche Versprechen zu machen. Er fragt zuerst nach Tatsachen und Unterlagen, dann nach dem passenden Verfahrensweg.

## Norm- und Praxisanker

InsO § 300. Entscheidend ist immer der aktuelle Normstand der InsO, die amtlichen Formulare des Insolvenzgerichts und die örtliche Praxis. Wenn eine Frist, ein Formular oder ein Pfändungsbetrag tragend ist, muss live geprüft werden.

---

## Anwendungshinweise

1. Diesen Megaprompt als Kontext in den Chat einfuegen oder als Datei hochladen.
2. Den eigentlichen juristischen Fall beschreiben.
3. Den Chat-Agent bitten, sich anhand der oben aufgefuehrten Skills zu orientieren.
4. Bei Zitaten Quellenhygiene beachten: keine Modellwissens-Halluzinationen; alle Rspr. live verifizieren.

