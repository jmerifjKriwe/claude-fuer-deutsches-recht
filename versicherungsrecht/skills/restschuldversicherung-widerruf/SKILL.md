---
name: restschuldversicherung-widerruf
description: "Restschuldversicherung Widerruf im Plugin Versicherungsrecht: prüft konkret Restschuldversicherung bei Verbraucherdarlehen, Rückversicherung, Fronting-Strukturen, Captives. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Restschuldversicherung Widerruf

## Arbeitsbereich

**Restschuldversicherung Widerruf** ordnet den Fall über die tragenden Prüffelder: Restschuldversicherung bei Verbraucherdarlehen, Rückversicherung, Fronting-Strukturen. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `restschuldversicherung-widerruf-kopplung-verbraucherdarlehen` | Restschuldversicherung bei Verbraucherdarlehen: Kopplung, Widerruf, Beratung, Kosten, Arbeitslosigkeit/Arbeitsunfähigkeit/Tod und Bankvertrieb prüfen. |
| `rueckversicherung-cut-through-und-fronting` | Rückversicherung, Fronting-Strukturen, Captives, Cut-through-Klauseln und Insolvenzrisiken rechtlich einordnen. |
| `solvency-ii-scr-orsa-aufsichtsrecht` | Solvency-II-Aufsichtsrahmen: Eigenmittel, SCR/MCR, ORSA, Governance, Ausgliederung und BaFin-Kommunikation für Versicherer und Gruppen. |

## Arbeitsweg

- Rolle und Ziel im Versicherungsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `restschuldversicherung-widerruf-kopplung-verbraucherdarlehen`

**Fokus:** Restschuldversicherung bei Verbraucherdarlehen: Kopplung, Widerruf, Beratung, Kosten, Arbeitslosigkeit/Arbeitsunfähigkeit/Tod und Bankvertrieb prüfen.

# Restschuldversicherung und Verbraucherdarlehen

## Einsatz

Für Verbraucher und Banken bei Streit um teure oder unpassende Restschuldversicherungen.

## Norm- und Quellenanker

VVG §§ 6, 7, 8; BGB Verbraucherdarlehen §§ 491 ff.; PAngV; IDD/Vermittlerrecht.

## Arbeitsfragen

1. Wie wurde die Versicherung mit dem Darlehen angeboten?
2. Wurden Kosten, Widerruf und Leistungsumfang transparent erklärt?
3. Welcher versicherte Fall ist eingetreten?
4. Ist Rückabwicklung, Leistung oder Beschwerde Ziel?

## Output

Kopplungsprüfung, Widerrufs-/Beratungsmemo, Leistungsantrag und Bankenbrief.

## Red Flags

- Versicherung im Effektivzins versteckt
- Gesundheits-/Arbeitslosigkeitsausschluss übersehen
- Widerrufsbelehrung lückenhaft
- Bank und Versicherer verweisen aufeinander

## Anschluss-Skills

- idd-vertrieb-beratung-dokumentation
- vag-bafin-aufsicht-beschwerde-missstand

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `rueckversicherung-cut-through-und-fronting`

**Fokus:** Rückversicherung, Fronting-Strukturen, Captives, Cut-through-Klauseln und Insolvenzrisiken rechtlich einordnen.

# Rückversicherung, Cut-through und Fronting

## Einsatz

Für Industrieprogramme, Captives und internationale Versicherungsstrukturen, in denen Erstversicherer und Rückversicherer auseinanderfallen.

## Norm- und Quellenanker

VVG/VAG Rückversicherung; BGB Vertragsauslegung; InsO; internationales Privatrecht.

## Arbeitsfragen

1. Wer ist Erstversicherer, Rückversicherer, Fronting Carrier, Captive?
2. Gibt es direkte Rechte des Versicherungsnehmers?
3. Welche Insolvenz- oder Sanktionsrisiken bestehen?

## Output

Strukturmemo, Anspruchslandkarte und Insolvenz-/Aufsichtsrisiko.

## Red Flags

- Cut-through nur behauptet
- Fronting Carrier insolvenzgefährdet
- anwendbares Recht fehlt

## Anschluss-Skills

- Nutze den allgemeinen Skill des Plugins, wenn Rolle, Police/Vertrag, Frist oder Ziel noch nicht klar sind.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `solvency-ii-scr-orsa-aufsichtsrecht`

**Fokus:** Solvency-II-Aufsichtsrahmen: Eigenmittel, SCR/MCR, ORSA, Governance, Ausgliederung und BaFin-Kommunikation für Versicherer und Gruppen.

# Solvency II, SCR und ORSA für Versicherer

## Einsatz

Für Rechtsabteilungen von Versicherern, Captives oder Investoren, die aufsichtsrechtliche Anforderungen verstehen und dokumentieren müssen.

## Norm- und Quellenanker

VAG; Delegierte Solvency-II-Regeln; EIOPA-Leitlinien; DORA bei IKT; HGB/IFRS nur als Schnittstelle.

## Arbeitsfragen

1. Welche Einheit: Versicherer, Rückversicherer, Gruppe, Vermittler, Ausgliederung?
2. Welche Kapital- und Governancepflicht ist betroffen?
3. Welche BaFin-/EIOPA-Vorgaben sind live zu prüfen?
4. Welche Dokumentation muss Vorstand/Aufsichtsrat sehen?

## Output

Aufsichtsmemo, ORSA-/Governance-Fragenliste, BaFin-Kommunikationsentwurf und Vorstandsvorlage.

## Red Flags

- SCR-Zahl ohne Governance-Kontext
- Ausgliederung nicht DORA-kompatibel
- Gruppe/Einzelunternehmen verwechselt
- Aufsichtsbrief zu langsam beantwortet

## Anschluss-Skills

- dora-cyber-ikt-versicherer
- eioPA-grenzueberschreitender-vertrieb

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
