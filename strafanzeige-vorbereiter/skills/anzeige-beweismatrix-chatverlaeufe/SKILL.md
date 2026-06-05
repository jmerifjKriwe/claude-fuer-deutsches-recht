---
name: anzeige-beweismatrix-chatverlaeufe
description: "Anzeige Beweismatrix Chatverlaeufe im Strafanzeigen-Vorbereitung: prüft konkret Ordnet jedes Element der Anzeige nach Tatsachenwissen, Beleg, Zeuge, Dokument. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Anzeige Beweismatrix Chatverlaeufe

## Arbeitsbereich

Dieser Skill behandelt **Anzeige Beweismatrix Chatverlaeufe** als zusammenhängenden Arbeitsgang im Strafanzeigen-Vorbereitung. Im Mittelpunkt steht die Prüfung von Ordnet jedes Element der Anzeige nach Tatsachenwissen, Beleg, Zeuge. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `anzeige-beweismatrix-tatsachen-meinungen` | Ordnet jedes Element der Anzeige nach Tatsachenwissen, Beleg, Zeuge, Dokument, Meinung und Vermutung. |
| `anzeige-chatverlaeufe-emails-header` | Chatverläufe, EML-Dateien, E-Mail-Header, Messenger-Screenshots, Export und Kontext sichern. |

## Arbeitsweg

- Rolle und Ziel im Strafanzeige Vorbereiter klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `anzeige-beweismatrix-tatsachen-meinungen`

**Fokus:** Ordnet jedes Element der Anzeige nach Tatsachenwissen, Beleg, Zeuge, Dokument, Meinung und Vermutung.

# Beweismatrix: Tatsache, Meinung, Vermutung

## Einsatz

Für saubere Anzeigen ohne Überbehauptung.

## Norm- und Quellenanker

StPO § 158; StGB § 164; ZPO Beweisgrundsätze.

## Arbeitsfragen

1. Welche Aussage ist Tatsache?
2. Welcher Beleg?
3. Welche Vermutung muss als solche markiert werden?

## Output

Beweismatrix und Anlagenliste.

## Red Flags

- Adjektive ersetzen Beweise
- Screenshots ohne Kontext
- Zeuge unklar

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.

## 2. `anzeige-chatverlaeufe-emails-header`

**Fokus:** Chatverläufe, EML-Dateien, E-Mail-Header, Messenger-Screenshots, Export und Kontext sichern.

# Chats, E-Mails und Header sichern

## Einsatz

Für digitale Kommunikation als Hauptbeweis.

## Norm- und Quellenanker

StPO; ZPO; DSGVO; Fernmeldegeheimnis je Kontext.

## Arbeitsfragen

1. Welcher Kommunikationskanal?
2. Sind vollständige Verläufe vorhanden?
3. Wer ist Absender?

## Output

Kommunikationsbeweis-Paket.

## Red Flags

- einzelne Chatfetzen
- Header fehlen
- Weiterleitung verändert Beweis

## Arbeitsstil

Erst bremsen, dann prüfen, dann schreiben: nur Tatsachen behaupten, Vermutungen als Vermutung kennzeichnen, entlastende Umstände nicht unterschlagen, Strafantragsfristen prüfen und Strafrecht nicht als unlauteres Druckmittel benutzen.

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren. Normen und Behördenportale vor Abgabe live prüfen.
