---
name: hausrat-einbruchdiebstahl-idd-vertrieb
description: "Hausrat Einbruchdiebstahl IDD Vertrieb im Plugin Versicherungsrecht: prüft konkret Hausratversicherung bei Einbruchdiebstahl, Raub, Trickdiebstahl, Wertsachen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Hausrat Einbruchdiebstahl IDD Vertrieb

## Arbeitsbereich

Dieser Skill behandelt **Hausrat Einbruchdiebstahl IDD Vertrieb** als zusammenhängenden Arbeitsgang im Plugin Versicherungsrecht. Im Mittelpunkt steht die Prüfung von Hausratversicherung bei Einbruchdiebstahl, Raub, Trickdiebstahl. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `hausrat-einbruchdiebstahl-entschaedigungsgrenze` | Hausratversicherung bei Einbruchdiebstahl, Raub, Trickdiebstahl, Wertsachen, Außenversicherung, Unterversicherung und Stehlgutliste. |
| `idd-vertrieb-beratung-dokumentation` | Versicherungsvertrieb: Beratungspflichten, Geeignetheit, Beratungsdokumentation, Provision, Makler/Vertreter, Onlineabschluss und Haftung. |
| `internationales-versicherungsprogramm-master-local-policy` | Master Policy, Local Policy, admitted/non-admitted insurance, Claims Handling und internationale Deckungskoordination prüfen. |

## Arbeitsweg

- Rolle und Ziel im Versicherungsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `hausrat-einbruchdiebstahl-entschaedigungsgrenze`

**Fokus:** Hausratversicherung bei Einbruchdiebstahl, Raub, Trickdiebstahl, Wertsachen, Außenversicherung, Unterversicherung und Stehlgutliste.

# Hausrat: Einbruchdiebstahl und Entschädigungsgrenzen

## Einsatz

Der Skill macht aus einer chaotischen Einbruchakte eine plausible, belegte Entschädigungsforderung.

## Norm- und Quellenanker

VVG §§ 1, 28, 81; VHB/AVB; StGB Indizien nur als Tatsachen; ZPO.

## Arbeitsfragen

1. Welche versicherte Gefahr liegt vor und welche Spuren/Anzeigen belegen sie?
2. Welche Sachen fehlen, welche Werte sind beweisbar?
3. Welche Grenzen gelten für Wertsachen, Bargeld, Außenversicherung?
4. Gibt es Unterversicherung oder Sicherungsobliegenheiten?

## Output

Stehlgutmatrix, Beleglückenliste, Polizeinachweis-Check und Regulierungsschreiben.

## Red Flags

- nur Erinnerungswerte ohne Belege
- Einbruchspuren fehlen
- Tresorklausel übersehen
- Sicherungsobliegenheit nachträglich behauptet

## Anschluss-Skills

- vvg-obliegenheit-28-quotelung-kausalitaet
- vergleich-abfindung-entschaedigungsquittung

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `idd-vertrieb-beratung-dokumentation`

**Fokus:** Versicherungsvertrieb: Beratungspflichten, Geeignetheit, Beratungsdokumentation, Provision, Makler/Vertreter, Onlineabschluss und Haftung.

# IDD/VVG-Vertrieb: Beratung und Dokumentation

## Einsatz

Der Skill prüft, ob ein Produkt richtig verkauft wurde und wer für Falschberatung haftet.

## Norm- und Quellenanker

VVG §§ 6, 7, 59–68; VersVermV; IDD/EU-Recht; BGB Maklerhaftung; GewO.

## Arbeitsfragen

1. Wer ist Vermittler und wem schuldet er was?
2. Welche Wünsche/Bedürfnisse wurden erhoben?
3. Ist Beratungsdokumentation vorhanden und passend?
4. Welche Produktkosten/Provisionen wurden offengelegt?

## Output

Beratungsfehler-Matrix, Haftungsadressat, Auskunftsverlangen und Anspruchsskizze.

## Red Flags

- Makler und Vertreter verwechselt
- Dokumentation nachträglich erstellt
- Onlineabschluss ohne Bedarfsermittlung
- Provision/Kosten intransparent

## Anschluss-Skills

- restschuldversicherung-widerruf-kopplung-verbraucherdarlehen
- vag-bafin-aufsicht-beschwerde-missstand

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `internationales-versicherungsprogramm-master-local-policy`

**Fokus:** Master Policy, Local Policy, admitted/non-admitted insurance, Claims Handling und internationale Deckungskoordination prüfen.

# Internationale Versicherungsprogramme: Master und Local Policy

## Einsatz

Für Konzernprogramme mit deutschen und ausländischen Risiken.

## Norm- und Quellenanker

- Rom-I-VO für Rechtswahl und zwingende Versicherungs-/Aufsichtsnormen; Brüssel-Ia-VO für Gerichtsstand und Konzern-/Versicherungsgerichtsstände.
- VVG für deutsche Versicherungsverträge, Obliegenheiten, Anzeige, Gefahrerhöhung, Leistungspflicht und Verjährung.
- VAG und BaFin-Praxis für Erlaubnis-/Aufsichtsfragen, wenn ein ausländischer Versicherer deutsche Risiken zeichnet.
- Lokales Aufsichtsrecht live prüfen: admitted/non-admitted, compulsory insurance, premium taxes, sanctions, claims payment, fronting.
- Programmklauseln: DIC/DIL, Financial Interest Clause, Claims Cooperation, Sanctions Clause, Cut-through, Loss Payee, Captive/Reinsurance.

## Arbeitsfragen

1. Welche Risiken liegen wo: Sach, Haftpflicht, D&O, Cyber, Transport, Kredit, Employee Benefits?
2. Welche Police deckt welchen Standort: Master, Local, Difference in Conditions, Difference in Limits, Fronting?
3. Ist non-admitted insurance im Risikoland zulässig oder braucht es lokale admitted cover?
4. Wer darf Prämien annehmen, Policen ausstellen und Claims bezahlen, ohne Versicherungsaufsicht oder Steuerrecht zu verletzen?
5. Wie laufen Notice, Loss Adjustment, Coverage Position, Zahlung, Regress und Recovery zwischen Local Policy, Master und Rückversicherer?
6. Gibt es Sanktionen, Devisenrecht, Versicherungssteuer, Pflichtversicherung oder lokale Sprache/Form?

## Output

Programm-Matrix mit Land, Risiko, Police, admitted-status, Steuer, Pflichtversicherung, Claim-Routing, Zahlungsweg, Rechtswahl, Gerichtsstand und Red Flags.

## Red Flags

- Local Policy übersehen
- Steuern/Prämienabgaben vergessen
- Claim Notice an falsche Stelle
- Master verspricht Deckung, aber Local Law verbietet Zahlung ins Land
- DIC/DIL wird als Vollversicherung missverstanden
- Konzern-Risk-Manager meldet Claim, aber lokale Police verlangt Notice durch lokale Einheit

## Anschluss-Skills

- Nutze den allgemeinen Skill des Plugins, wenn Rolle, Police/Vertrag, Frist oder Ziel noch nicht klar sind.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
