---
name: quellen-livecheck-regelaltersrente-vorzeitige
description: "Quellen Livecheck Regelaltersrente Vorzeitige im Plugin Rentenpruefer: prüft konkret Quellen-Livecheck im Rentenrecht, Prüfung von Regelaltersrente und vorzeitiger Altersrente. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Quellen Livecheck Regelaltersrente Vorzeitige

## Arbeitsbereich

**Quellen Livecheck Regelaltersrente Vorzeitige** ordnet den Fall über die tragenden Prüffelder: Quellen-Livecheck im Rentenrecht, Prüfung von Regelaltersrente und vorzeitiger Altersrente. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `quellen-livecheck-rentenrecht` | Quellen-Livecheck im Rentenrecht: Normtext, DRV-Praxis, Abkommen, Versorgungswerkssatzung und Rechtsprechung absichern. |
| `regelaltersrente-und-vorzeitige-rente` | Prüfung von Regelaltersrente und vorzeitiger Altersrente nach SGB VI: Altersgrenzen, Wartezeiten, Abschläge, Antragstiming und Übergang in den Ruhestand. |

## Arbeitsweg

- Rolle und Ziel im Rentenpruefer klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `quellen-livecheck-rentenrecht`

**Fokus:** Quellen-Livecheck im Rentenrecht: Normtext, DRV-Praxis, Abkommen, Versorgungswerkssatzung und Rechtsprechung absichern.

# quellen-livecheck-rentenrecht

## Aufgabe

Verhindert Scheinpräzision in einem stark dokumenten- und trägertypischen Feld.

## Pflichtfragen

- Welches Rentensystem oder welcher Träger ist betroffen: DRV, Knappschaft, Versorgungswerk, Zusatzversorgung, ausländischer Träger oder Mischfall?
- Gibt es einen Bescheid, eine Renteninformation, eine Rentenauskunft, einen Versicherungsverlauf oder nur Einzelunterlagen?
- Welche Frist, welches Datum, welcher Zeitraum und welches konkrete Ziel sind entscheidend?
- Welche Unterlagen liegen bereits vor und welche Nachweise fehlen noch?

## Spezifischer Intake

Thema, Norm, Staat, Träger, Satzung, gewünschte Aussage, vorhandene Quelle.

## Prüfprogramm

1. **Systemroute klären:** gesetzliche Rente, Versorgungswerk, Ausland, Nachversicherung oder Rechtsbehelf trennen.
2. **Tatsachen sichern:** Zeiträume monatsgenau, Träger, Bescheide, Nachweise, Übersetzungen und Zustellungen erfassen.
3. **Norm- und Quellencheck:** SGB VI, SGB X, SGG, FRG, DRV-Informationen, Sozialversicherungsabkommen oder konkrete Satzung live prüfen.
4. **Beweiswert bewerten:** Original, beglaubigte Kopie, ausländische Urkunde, Arbeitsbuch, Zeuge, Arbeitgeberarchiv, Behördenauskunft.
5. **Handlung ableiten:** Antrag, Kontenklärung, Nachreichung, Widerspruch, Klage, Vergleich, Nachfassschreiben oder Mandantenbrief.

## Output

Quellenliste mit geprüften und offenen Punkten.

## Qualitäts-Hardening

- Keine nicht überprüfbaren Fundstellen, keine privaten Datenbankzitate, keine Kommentar- oder Aufsatzblindzitate.
- Bei ausländischen Zeiten nie pauschal anerkennen: EU/EWR/Schweiz, Abkommensstaat, vertragsloser Drittstaat und FRG strikt trennen.
- Bei Versorgungswerken immer Beruf, Kammer, Bundesland und aktuelle Satzung verlangen.
- Zahlen, Fristen und Altersgrenzen nur mit aktueller Quelle oder als ausdrücklich zu prüfenden Punkt ausgeben.

## 2. `regelaltersrente-und-vorzeitige-rente`

**Fokus:** Prüfung von Regelaltersrente und vorzeitiger Altersrente nach SGB VI: Altersgrenzen, Wartezeiten, Abschläge, Antragstiming und Übergang in den Ruhestand.

# regelaltersrente-und-vorzeitige-rente

## Aufgabe

Findet den richtigen Rentenbeginn und verhindert teure Timingfehler.

## Pflichtfragen

- Welches Rentensystem oder welcher Träger ist betroffen: DRV, Knappschaft, Versorgungswerk, Zusatzversorgung, ausländischer Träger oder Mischfall?
- Gibt es einen Bescheid, eine Renteninformation, eine Rentenauskunft, einen Versicherungsverlauf oder nur Einzelunterlagen?
- Welche Frist, welches Datum, welcher Zeitraum und welches konkrete Ziel sind entscheidend?
- Welche Unterlagen liegen bereits vor und welche Nachweise fehlen noch?

## Spezifischer Intake

Geburtsjahr, Wartezeit, Schwerbehinderung, Hinzuverdienst, Arbeitsende, Krankenversicherung, Ausland.

## Prüfprogramm

1. **Systemroute klären:** gesetzliche Rente, Versorgungswerk, Ausland, Nachversicherung oder Rechtsbehelf trennen.
2. **Tatsachen sichern:** Zeiträume monatsgenau, Träger, Bescheide, Nachweise, Übersetzungen und Zustellungen erfassen.
3. **Norm- und Quellencheck:** SGB VI, SGB X, SGG, FRG, DRV-Informationen, Sozialversicherungsabkommen oder konkrete Satzung live prüfen.
4. **Beweiswert bewerten:** Original, beglaubigte Kopie, ausländische Urkunde, Arbeitsbuch, Zeuge, Arbeitgeberarchiv, Behördenauskunft.
5. **Handlung ableiten:** Antrag, Kontenklärung, Nachreichung, Widerspruch, Klage, Vergleich, Nachfassschreiben oder Mandantenbrief.

## Output

Entscheidungsmatrix Rentenbeginn mit Vor- und Nachteilen.

## Qualitäts-Hardening

- Keine nicht überprüfbaren Fundstellen, keine privaten Datenbankzitate, keine Kommentar- oder Aufsatzblindzitate.
- Bei ausländischen Zeiten nie pauschal anerkennen: EU/EWR/Schweiz, Abkommensstaat, vertragsloser Drittstaat und FRG strikt trennen.
- Bei Versorgungswerken immer Beruf, Kammer, Bundesland und aktuelle Satzung verlangen.
- Zahlen, Fristen und Altersgrenzen nur mit aktueller Quelle oder als ausdrücklich zu prüfenden Punkt ausgeben.
