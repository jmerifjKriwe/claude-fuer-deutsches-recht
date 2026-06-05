---
name: vers-ombudsmann-versicherungsbetrug
description: "Vers Ombudsmann Bafin Beschwerde Klageweg, Versicherungsbetrug Verdachtsfall Kooperation Strafrecht, Versicherungssumme Unterversicherung Taxwert: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Vers Ombudsmann Bafin Beschwerde Klageweg, Versicherungsbetrug Verdachtsfall Kooperation Strafrecht, Versicherungssumme Unterversicherung Taxwert

## Arbeitsbereich

In diesem Skill wird **Vers Ombudsmann Bafin Beschwerde Klageweg, Versicherungsbetrug Verdachtsfall Kooperation Strafrecht, Versicherungssumme Unterversicherung Taxwert** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `vers-ombudsmann-bafin-beschwerde-klageweg` | Eskalationsrouting im Versicherungsrecht: Versicherungsombudsmann, PKV-Ombudsmann, BaFin-Beschwerde, Deckungsklage, einstweiliger Rechtsschutz und Vergleichsdruck sauber unterscheiden. |
| `versicherungsbetrug-verdachtsfall-kooperation-strafrecht` | Versicherungsrechtlicher Umgang mit Betrugsverdacht: Auskunft, Leistungsprüfung, Strafanzeige, Datenschutz, Zivilprozess und Verteidigungsrisiken. |
| `versicherungssumme-unterversicherung-taxwert` | Versicherungssumme, Unterversicherung, gleitender Neuwert, Taxe, Summenausgleich und Vorsorgeversicherung prüfen. |

## Arbeitsweg

Für **Vers Ombudsmann Bafin Beschwerde Klageweg, Versicherungsbetrug Verdachtsfall Kooperation Strafrecht, Versicherungssumme Unterversicherung Taxwert** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `versicherungsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `vers-ombudsmann-bafin-beschwerde-klageweg`

**Fokus:** Eskalationsrouting im Versicherungsrecht: Versicherungsombudsmann, PKV-Ombudsmann, BaFin-Beschwerde, Deckungsklage, einstweiliger Rechtsschutz und Vergleichsdruck sauber unterscheiden.

# Ombudsmann, BaFin-Beschwerde oder Klage?

## Einsatz

Nicht jede Ablehnung gehört sofort in die Klage. Der Skill wählt das Verfahren nach Streitwert, Eilbedürftigkeit, Beweisbedarf, Bindungswirkung und taktischem Druck.

## Norm- und Quellenanker

VVG §§ 214 ff., § 215; VAG Aufsicht; ZPO; Ombudsmann-Verfahrensordnungen live prüfen; BaFin-Verbraucherbeschwerde.

## Arbeitsfragen

1. Geht es um Verbrauchermandat, Unternehmer, PKV, Rechtsschutz oder Großschaden?
2. Ist eine schnelle Zahlung, eine Grundsatzentscheidung oder Aktenoffenlegung wichtiger?
3. Welche Hemmung und Bindung hat der gewählte Weg?
4. Welche Unterlagen muss die Beschwerde enthalten?

## Output

Entscheidungsbaum mit Musterschreiben für Ombudsmann/BaFin, Klageweg-Notiz und Fristenhinweis.

## Red Flags

- BaFin als Leistungsgericht missverstanden
- Ombudsmann bei hohem Streitwert ungeeignet
- Klagefrist/Verjährung läuft parallel
- PKV-Ombudsmann und Versicherungsombudsmann verwechselt

## Anschluss-Skills

- deckungsprozess-zustaendigkeit-215-vvg
- rechtsschutz-deckungszusage-stichentscheid

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `versicherungsbetrug-verdachtsfall-kooperation-strafrecht`

**Fokus:** Versicherungsrechtlicher Umgang mit Betrugsverdacht: Auskunft, Leistungsprüfung, Strafanzeige, Datenschutz, Zivilprozess und Verteidigungsrisiken.

# Verdacht Versicherungsbetrug und Kooperation mit Strafrecht

## Einsatz

Für Fälle, in denen Versicherer Betrug wittern oder Mandanten mit Strafanzeige konfrontiert sind.

## Norm- und Quellenanker

VVG §§ 28, 31; StGB § 263; StPO; DSGVO; BGB.

## Arbeitsfragen

1. Welche Tatsachen tragen den Verdacht?
2. Was darf/muss der Versicherungsnehmer noch erklären?
3. Wie beeinflusst ein Strafverfahren den Deckungsprozess?

## Output

Risikomemo, Aussage-/Mitwirkungsplan und Zivil-/Strafschnittstelle.

## Red Flags

- vorschnelle Einlassung
- Strafakte nicht beigezogen
- Mitwirkung und Selbstbelastung nicht getrennt

## Anschluss-Skills

- Nutze den allgemeinen Skill des Plugins, wenn Rolle, Police/Vertrag, Frist oder Ziel noch nicht klar sind.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `versicherungssumme-unterversicherung-taxwert`

**Fokus:** Versicherungssumme, Unterversicherung, gleitender Neuwert, Taxe, Summenausgleich und Vorsorgeversicherung prüfen.

# Versicherungssumme, Unterversicherung und Taxwert

## Einsatz

Für Sachschäden, bei denen die Höhe nicht am Schaden, sondern an Summenmechanik und Bewertungslogik hängt.

## Norm- und Quellenanker

VVG §§ 74, 75, 76; AVB Sachversicherung; BGB.

## Arbeitsfragen

1. Welche Summe und Bewertungsbasis gilt?
2. Liegt Unterversicherung vor?
3. Ist Taxe vereinbart oder widerlegbar?

## Output

Berechnungsmatrix und Deckungsargumente.

## Red Flags

- gleitender Neuwert falsch gerechnet
- Taxe mit Zeitwert verwechselt
- Vorsorgeversicherung übersehen

## Anschluss-Skills

- Nutze den allgemeinen Skill des Plugins, wenn Rolle, Police/Vertrag, Frist oder Ziel noch nicht klar sind.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
