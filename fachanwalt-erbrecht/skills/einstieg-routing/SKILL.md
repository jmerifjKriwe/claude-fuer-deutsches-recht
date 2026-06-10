---
name: einstieg-routing
description: "Anwalts-Dashboard Fachanwalt Erbrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat."
---

# Anwalts-Dashboard Fachanwalt Erbrecht

> Erbfall, Pflichtteil, Erbschein, Erbengemeinschaft, Testament — Ausschlagungsfrist tickt ab Kenntnis. Wer beerbt wen, wann?
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | **§ 1944 BGB: 6 Wochen** Ausschlagung ab Kenntnis von Anfall und Berufungsgrund (6 Monate bei Auslandsbezug). § 1954 BGB: Anfechtung der Annahme/Ausschlagung 6 Wochen. § 2306 BGB: Ausschlagungsrecht bei Beschwerung 6 Wochen. § 2082 BGB: Anfechtung Testament 1 Jahr ab Kenntnis. § 2332 BGB: Pflichtteils-Verjährung 3 Jahre. | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Erbe §§ 1922, 1942 BGB · Pflichtteil §§ 2303 ff. BGB · Pflichtteilsergänzung §§ 2325 ff. BGB · Auskunft § 2314 BGB · Auseinandersetzung §§ 2042 ff. BGB · Erbschein §§ 2353 ff. BGB · Vermächtnis §§ 2147 ff. BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Nachlassgericht am letzten gewöhnlichen Aufenthalt (§ 343 FamFG). Streitige Erbsachen: LG/AG nach Streitwert (§ 27 ZPO). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Ausschlagungsfrist 6 Wochen läuft ab Kenntnis; Akten dokumentieren. 🟠 Pflichtteilsergänzung (10-Jahresfrist § 2325 III BGB) und Pflichtteils-Verjährung (3 Jahre) gegen Schenkungen verfolgen.
- **Beweislage:** 🟠 Pflichtteils-Auskunft § 2314 BGB lückenhaft → notarielles Verzeichnis erzwingen. 🔴 Testament: Testierfähigkeit Beweis (medizinische Akten, Zeugen, ggf. Sachverständige).
- **Wirtschaftlich:** 🔴 Nachlassinsolvenz droht → § 1980 BGB Antrag (binnen 3 Monaten), Erbenhaftungsbeschränkung. 🟠 Hoher Nachlasswert: Pflichtteilsanspruch parallel zu Auseinandersetzung.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Pflichtteil berechnen / geltend machen** | `pflichtteil-berechnen` | Pflichtteilsquote, Wertermittlung, Auskunftsverfahren § 2314 BGB |
| Ausschlagung der Erbschaft | `erbschaftsausschlagung` | 6-Wochen-Frist § 1944 BGB, notarielle/gerichtliche Erklärung |
| Testament auslegen | `testament-auslegung-und-andeutung` | Andeutungstheorie, Auslegungsregeln, ergänzende Auslegung |
| Erbschein beantragen | `erbschein-antrag` | Antrag, Glaubhaftmachung, eidesstattliche Versicherung |
| Erbengemeinschaft blockiert | `erbengemeinschaft-blockade-auseinandersetzung` | Teilungsklage, Vermittlungsverfahren §§ 363 ff. FamFG |

## Norm-Radar (live verifizieren)

- **§ 1944 BGB** — Ausschlagungsfrist 6 Wochen
- **§ 2303 BGB** — Pflichtteilsanspruch
- **§ 2314 BGB** — Auskunftsanspruch des Pflichtteilsberechtigten
- **§ 2325 BGB** — Pflichtteilsergänzung; 10-Jahres-Abschmelzung
- **§ 2353 BGB** — Erbschein
- **§ 1980 BGB** — Antrag Nachlassinsolvenz

## Genau eine Rückfrage (nur wenn nötig)

> Vertreten Sie **Erbe(n), Pflichtteilsberechtigte oder Vermächtnisnehmer** — und steht eine **Frist** (Ausschlagung, Anfechtung) oder eine **Verteilungsfrage** im Vordergrund?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.
