---
name: einstieg-routing
description: "Anwalts-Dashboard Fachanwalt Familienrecht: Sofort-Triage als Tabelle (Rolle, Verfahrensstand, Eilfrist, Hauptanspruch, Zuständigkeit), Risiko-Ampel, Anschluss-Skill-Router mit echten Slugs, Norm-Radar; maximal eine Rückfrage. Der Anwalt bleibt im Driver Seat."
---

# Anwalts-Dashboard Fachanwalt Familienrecht

> Trennung, Unterhalt, Versorgungsausgleich, Sorge- und Umgangsrecht — meist Verbundverfahren, meist im Hintergrund das Kindeswohl.
>
> Sie sehen unten die Sofort-Triage. Keine Rückfragen, bis die Tabelle steht. Wenn die Akte 80 % trägt, gehen wir direkt zum Anschluss-Skill — Sie entscheiden, ob.

## Sofort-Triage

| Punkt | Schnellprüfung | Standardquelle / Hilfsweg |
| --- | --- | --- |
| Rolle | Wen vertrete ich? (Mandant · Gegenseite · Mehrere) | Mandantenmail, Vertretungsbestellung |
| Verfahrensstand | Vorprozessual · außergerichtlich · Klage · Rechtsmittel · Vollstreckung | Vorhandene Schriftsätze, Eingangsstempel |
| Eilfrist | Keine 3-Wochen-Frist wie im ArbR, aber: § 1565 II BGB (Härtefall-Scheidung vor Trennungsjahr), §§ 1666, 1666a BGB i. V. m. § 49 FamFG (Kindeswohlgefährdung — sofort), § 36 GewSchG (Gewaltschutz — sofortige Wirksamkeit). | Frist aus Zugangs-/Kenntnisdatum berechnen |
| Hauptanspruch | Scheidung §§ 1564 ff. BGB · Trennungsunterhalt § 1361 BGB · Nachehelicher Unterhalt §§ 1569 ff. BGB · Kindesunterhalt §§ 1601 ff. BGB · Zugewinn §§ 1372 ff. BGB · Versorgungsausgleich §§ 1, 9 VersAusglG · Sorge §§ 1671, 1684 BGB · Umgang § 1684 BGB. | Sachverhaltsabgleich mit Tatbestandsmerkmalen |
| Zuständigkeit | Familiengericht (Abt. AG) am Aufenthalt des Kindes oder gemeinsamen Wohnsitzes (§§ 122, 152, 232 FamFG). Anwaltszwang in Ehesachen (§ 114 FamFG). | Gesetz, Vertrag, Gerichtsstandsklausel |

## Risiko-Ampel

- **Frist:** 🔴 Kindeswohlgefährdung: sofort Eilantrag (§ 49 FamFG). 🔴 Häusliche Gewalt: Schutzanordnung § 1 GewSchG. 🟠 Trennungsjahr: Datum dokumentieren (Beweis!).
- **Beweislage:** 🟠 Trennungszeitpunkt — Indizien (Kontotrennung, Schlafzimmer, schriftliche Erklärung). 🔴 Sorgekonflikt: Beweismittel sorgsam (kein Aufschaukeln, Verfahrensbeistand respektieren).
- **Wirtschaftlich:** 🟠 Hohes Vermögen: Zugewinn parallel zur Scheidung (Verbund). 🔴 Drohende Verschiebung von Vermögen: § 1379 BGB Auskunft + § 1390 BGB Anfechtung.

## Anschluss-Skills (Router)

| Wenn der Fall trägt … | dann Skill | Erwartung |
| --- | --- | --- |
| **Trennung — Trennungsjahr / Folgen** | `famr-trennungsjahr-praxis` | Trennungszeitpunkt dokumentieren, Trennungsunterhalt vorbereiten |
| Kindesunterhalt zu prüfen | `kindesunterhalt-mindestsatz-paragraf-1612a-bgb` | Mindestunterhalt, Düsseldorfer Tabelle, Mangelfall-Berechnung |
| Versorgungsausgleich offen | `famr-versorgungsausgleich-spezial` | Auskunftsverfahren VAB-Fragebogen, Halbteilung, Ausschluss |
| Gewaltschutz / Umgang in Konflikt | `gewaltschutz-und-umgang-schnittstelle` | GewSchG-Anordnung, Schnittstelle Umgang § 1684 BGB |
| Kindeswohlgefährdung — Eilantrag | `famr-kindeswohlgefaehrdung-eilantrag-spezial` | Eilantrag § 1666 BGB, Verfahrensbeistand, Jugendamt |

## Norm-Radar (live verifizieren)

- **§ 1565 BGB** — Scheidungsvoraussetzung, Trennungsjahr
- **§ 1361 BGB** — Trennungsunterhalt
- **§ 1612a BGB** — Mindestkindesunterhalt
- **§ 1666 BGB** — Maßnahmen bei Kindeswohlgefährdung
- **§ 1684 BGB** — Umgangsrecht / Umgangspflicht
- **§ 1 VersAusglG** — Halbteilungsgrundsatz

## Genau eine Rückfrage (nur wenn nötig)

> Geht es vorrangig um **Trennungs-/Scheidungsfolgen (Unterhalt, Zugewinn, VA)** oder um eine **akute Kindes- bzw. Gewaltschutz-Sache** (dann sofortiger Eilantrag)?

Wenn die Akte die Frage selbst beantwortet, **diese überspringen** und direkt den passenden Anschluss-Skill arbeiten.

## Hinweis

Diese Triage ist Ihre Vorbereitung, nicht Ihre Entscheidung. Sie führen das Mandat; der Skill liefert die Karte. Quellenhygiene nach `references/quellenhygiene.md`, Zitierform nach `references/zitierweise.md`. Die Konvention dieses Einstiegs-Dashboards steht in `references/anwalts-dashboard-konvention.md`.
