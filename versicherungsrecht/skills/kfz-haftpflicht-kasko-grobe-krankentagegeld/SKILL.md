---
name: kfz-haftpflicht-kasko-grobe-krankentagegeld
description: "KFZ Haftpflicht Kasko Grobe Krankentagegeld im Plugin Versicherungsrecht: prüft konkret Kfz-Haftpflichtversicherung, Kfz-Kaskoversicherung, Krankentagegeldversicherung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# KFZ Haftpflicht Kasko Grobe Krankentagegeld

## Arbeitsbereich

Dieser Skill behandelt **KFZ Haftpflicht Kasko Grobe Krankentagegeld** als zusammenhängenden Arbeitsgang im Plugin Versicherungsrecht. Im Mittelpunkt steht die Prüfung von Kfz-Haftpflichtversicherung, Kfz-Kaskoversicherung, Krankentagegeldversicherung. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `kfz-haftpflicht-regress-alkohol-flucht` | Kfz-Haftpflichtversicherung: Außenregulierung, Innenregress, Obliegenheitsverletzung, Alkohol, Unfallflucht, Fahrerlaubnis und Regresshöchstgrenzen. |
| `kfz-kasko-grobe-fahrlaessigkeit-entwendung` | Kfz-Kaskoversicherung: Entwendung, Unfall, Wild, Alkohol, grobe Fahrlässigkeit, Obliegenheiten, Wiederbeschaffungswert und Sachverständigenstreit. |
| `krankentagegeld-berufsunfaehigkeit-abgrenzung` | Krankentagegeldversicherung: Arbeitsunfähigkeit, Berufsunfähigkeit, Leistungseinstellung, Nachweis, PKV-Schnittstelle und existenzielle Liquidität. |

## Arbeitsweg

- Rolle und Ziel im Versicherungsrecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: die im Plugin-Kontext einschlägigen Normen über gesetze-im-internet.de, dejure.org, eur-lex.europa.eu und die amtlichen Bundes-/Landesportale live prüfen — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `kfz-haftpflicht-regress-alkohol-flucht`

**Fokus:** Kfz-Haftpflichtversicherung: Außenregulierung, Innenregress, Obliegenheitsverletzung, Alkohol, Unfallflucht, Fahrerlaubnis und Regresshöchstgrenzen.

# Kfz-Haftpflicht: Regress bei Alkohol, Flucht, Obliegenheit

## Einsatz

Für Mandate, in denen die Haftpflicht zwar den Dritten bezahlt, dann aber den Versicherungsnehmer regressiert.

## Norm- und Quellenanker

VVG §§ 28, 116; PflVG; AKB; StVG; StGB § 142 als Sachkontext.

## Arbeitsfragen

1. Welche Pflichtverletzung wird regressbegründend behauptet?
2. Welche Regressgrenze und AKB-Regel gilt?
3. War die Pflichtverletzung kausal oder vorsätzlich?
4. Welche Straf-/OWi-Akte beeinflusst die Beweisführung?

## Output

Regressabwehr, Kausalitätsargumente, Zahlungs-/Ratenvergleich und Schnittstelle Strafverfahren.

## Red Flags

- Strafurteil ungeprüft übernommen
- Regresshöchstgrenze übersehen
- Fahrer und Halter verwechselt
- Kausalitätsgegenbeweis nicht genutzt

## Anschluss-Skills

- kfz-kasko-grobe-fahrlaessigkeit-entwendung
- subrogation-regress-86-vvg

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 2. `kfz-kasko-grobe-fahrlaessigkeit-entwendung`

**Fokus:** Kfz-Kaskoversicherung: Entwendung, Unfall, Wild, Alkohol, grobe Fahrlässigkeit, Obliegenheiten, Wiederbeschaffungswert und Sachverständigenstreit.

# Kfz-Kasko: Entwendung, Unfall, grobe Fahrlässigkeit

## Einsatz

Der Skill prüft Kaskoablehnungen und Kürzungen, ohne Haftpflichtregulierung zu vermischen.

## Norm- und Quellenanker

VVG §§ 28, 81, 82; AKB; StVG nur als Sachkontext; ZPO.

## Arbeitsfragen

1. Welche Kaskogefahr und welche AKB-Fassung gilt?
2. Ist Entwendung plausibel und dokumentiert?
3. Welche grobe Fahrlässigkeit wird behauptet?
4. Wie werden Wiederbeschaffungswert, Restwert und Selbstbeteiligung berechnet?

## Output

Kasko-Deckungsmemo, Beweisplan, Wertgutachtenfragen und Regulierungsschreiben.

## Red Flags

- Alkohol/Flucht als Totalablehnung ohne Quote
- Zweitschlüsselproblem
- Wertgutachten dünn
- Obliegenheiten nach Unfall übersehen

## Anschluss-Skills

- kfz-haftpflicht-regress-alkohol-flucht
- vvg-obliegenheit-28-quotelung-kausalitaet

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.

## 3. `krankentagegeld-berufsunfaehigkeit-abgrenzung`

**Fokus:** Krankentagegeldversicherung: Arbeitsunfähigkeit, Berufsunfähigkeit, Leistungseinstellung, Nachweis, PKV-Schnittstelle und existenzielle Liquidität.

# Krankentagegeld vs. Berufsunfähigkeit

## Einsatz

Der Skill klärt die gefährliche Grenze: krankgeschrieben, aber angeblich dauerhaft berufsunfähig.

## Norm- und Quellenanker

VVG §§ 192 ff.; MB/KT; BGB; ZPO; ggf. SGB V Abgrenzung.

## Arbeitsfragen

1. Welche Tätigkeit wird aktuell ausgeübt und seit wann besteht AU?
2. Welche AU-Nachweise liegen vor?
3. Warum behauptet der Versicherer BU und ab wann?
4. Welche Anschlussdeckung oder BU-Police existiert?

## Output

KT/Bu-Abgrenzungsmemo, Liquiditätsplan, Nachweisbrief und Eil-/Klageoption.

## Red Flags

- Versicherer beendet KT ohne tragfähige BU-Begründung
- AU und BU begrifflich verwechselt
- Selbstständige Tätigkeit nicht konkret erfasst
- Lücke zwischen KT und BU-Leistung

## Anschluss-Skills

- bu-berufsbild-50-prozent-substantiierung
- pkv-kostenerstattung-medizinische-notwendigkeit

## Qualitätsregel

Keine Rechtsprechung aus Modellwissen zitieren. Wenn eine Entscheidung gebraucht wird: Gericht, Entscheidungsform, Datum, Aktenzeichen und frei zugängliche Quelle verifizieren; sonst nur als Prüfpunkt formulieren.
