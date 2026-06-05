# Strafzumessung

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strafzumessung`) | [`strafzumessung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafzumessung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Strafzumessung Bankert — Untreue, LG Frankfurt / BGH Revision** (`strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung`) | [Gesamt-PDF lesen](../testakten/strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung/gesamt-pdf/strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung_gesamt.pdf) | [`testakte-strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-strafzumessung-vermoegensdelikt-bankert-frankfurt-untreue-haupt-und-revisionsverhandlung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Plugin für die **Strafzumessung nach deutschem Strafrecht** — vom Strafbefehl bis zur großen Strafkammer. Adressaten: Strafverteidiger und Staatsanwaltschaft.

## Worum geht es?

Strafzumessung ist die zentrale richterliche Aufgabe nach Schuldspruch: Bestimmung von Strafart und Strafhoehe innerhalb des gesetzlichen Strafrahmens auf Grundlage der **Schuld** (§ 46 Abs. 1 Satz 1 StGB), unter Beruecksichtigung der **praeventiven Wirkungen** (§ 46 Abs. 1 Satz 2 StGB), nach den **Strafzumessungstatsachen** des § 46 Abs. 2 StGB und unter Beachtung des **Doppelverwertungsverbots** (§ 46 Abs. 3 StGB).

Das Plugin deckt die Strafzumessung vom Strafbefehlsverfahren ueber die Hauptverhandlung bis zur Vollstreckung ab, inklusive Bewaehrung, Strafmilderung, Regelbeispielen, Gesamtstrafenbildung, Verstaendigung und Jugendstrafrecht.

## Schnellstart

1. Mit `orientierung-strafzumessung-triage` einsteigen.
2. Rolle (Strafverteidigung, Staatsanwaltschaft) und Verfahrensstadium (Strafbefehl, Anklage, Hauptverhandlung, Urteil, Berufung, nachtraegliche Gesamtstrafe) angeben.
3. Den vom Triage-Skill empfohlenen Spezial-Skill aktivieren.
4. Bei Bedarf parallel mit den Plugins `strafbefehl-verteidiger` oder `fachanwalt-strafrecht` arbeiten.

## Enthaltene Skills

### Block A — Orientierung und Grundlagen
- `orientierung-strafzumessung-triage` — Einstieg, Triage, Spezial-Skill-Routing.
- `paragraph-46-stgb-grundsatz-strafzumessung` — § 46 StGB, Schuld als Grundlage.
- `strafzumessungs-tatsachen-46-ii-stgb` — Katalog § 46 Abs. 2 StGB.
- `strafrahmen-und-strafzumessungsstufen` — Strafrahmen-Logik vor jeder Zumessung.

### Block B — Geldstrafe
- `geldstrafe-tagessatzanzahl-bestimmen` — § 40 Abs. 1 StGB, Tagessatzanzahl als Schuldgroesse.
- `tagessatzhoehe-40-ii-stgb-nettotagesverdienst` — § 40 Abs. 2 StGB, Nettoeinkommen / 30.
- `geldstrafe-vs-freiheitsstrafe-47-stgb` — Vorrang Geldstrafe; § 47 StGB.

### Block C — Freiheitsstrafe und Bewaehrung
- `freiheitsstrafe-strafmass-pruefen` — Konkrete Zumessung im Strafrahmen.
- `bewaehrung-56-stgb-positive-sozialprognose` — § 56 StGB.
- `bewaehrung-auflagen-und-weisungen-56b-c-stgb` — §§ 56b, 56c StGB.
- `bewaehrungswiderruf-56f-stgb` — § 56f StGB.
- `freiheitsstrafe-ohne-bewaehrung-vollstreckung` — U-Haft-Anrechnung § 51 StGB, Reststrafenaussetzung § 57 StGB.

### Block D — Strafmilderung und Schaerfung
- `strafmilderung-49-stgb-zwingend-fakultativ` — § 49 StGB.
- `minder-schwerer-fall-und-besonders-schwerer-fall` — Strafrahmen-Modifikation.
- `regelbeispiele-rechtsprechung` — § 243 StGB, § 263 Abs. 3 StGB u.a.
- `taeter-opfer-ausgleich-46a-stgb-und-schadenswiedergutmachung` — § 46a StGB; BGH 4 StR 232/25.

### Block E — Strafbefehl und kleine Verfahren
- `strafbefehl-strafzumessung-407-stpo` — Strafzumessung im Strafbefehl.
- `153a-stpo-einstellung-gegen-auflage` — Einstellung mit Auflage.

### Block F — Hauptverhandlung und Verstaendigung
- `verstaendigung-257c-stpo-strafzumessung` — § 257c StPO; BVerfG 2 BvR 2628/10; BGH 1 StR 525/11.
- `gestaendnis-und-strafmilderung` — Gestaendnis als Strafmilderungsgrund.
- `267-iii-stpo-begruendungsanforderungen-strafurteil` — Strafurteil-Begruendung.

### Block G — Gesamtstrafenbildung
- `gesamtstrafenbildung-53-54-stgb-erste-instanz` — §§ 53, 54 StGB.
- `nachtraegliche-gesamtstrafenbildung-55-stgb` — § 55 StGB, Zaesurwirkung, § 460 StPO.
- `haerteausgleich-bei-nachtraeglicher-gesamtstrafenbildung` — BGH-staendige Linie.

### Block H — Sonderfaelle
- `jgg-strafzumessung-jugendstrafe-erziehungsmassregeln` — JGG; § 105 JGG Heranwachsende.

## Querverweise zu anderen Plugins

- `strafbefehl-verteidiger` — Spezial-Plugin Strafbefehlsverfahren.
- `fachanwalt-strafrecht` — Strafrechts-Gesamtverteidigung, Plaedoyer, Revision.
- `verkehrsowi-verteidiger` — Verkehrs-OWi-Strafzumessung.
- `urteilsbauer-relationsmacher` — Urteilsverfassung.
- `subsumtions-pruefer` — vor Schuldspruch.

## Hinweise zur Anwendung

- **Quellenregel beachten**: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen. Aktenzeichen vor Zitat in **dejure.org** oder **openjur.de** verifizieren. Lizenzierte Datenbanken nur bei vorhandenem Zugang.
- **Keine Praejudizienbindung** (Ausnahme § 31 BVerfGG). BGH-Linien sind argumentationsstuetzend, nicht bindend.
- **Mandantengeheimnis** wahren (§ 43a Abs. 2 BRAO; § 203 StGB).
- **Frueher BGH-Beschluss** zum TOA: BGH, Beschluss vom 20.11.2025 — 4 StR 232/25 (friedensstiftender kommunikativer Prozess).
- **BVerfG zur Verstaendigung**: 2 BvR 2628/10 vom 19.03.2013.
- **BGH-Belehrungspflicht**: 1 StR 525/11 vom 07.02.2012.

## Stand

- 05/2026.
- §§ 38 ff. StGB, §§ 407 ff. StPO, JGG, BtMG.
- Aktualitaetspruefung jaehrlich empfohlen.

## Lizenz

Apache-2.0 OR MIT (siehe Plugin-Root).


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `153a-stpo-iii-bewaehrung-stgb` | 153a Stpo III Bewaehrung Stgb im Plugin Strafzumessung: prüft konkret Einstellung gegen Auflage nach § 153a StPO, Begruendungsanforderungen an die Strafzumessung im, Aussetzung der Vollstreckung zur Bewaehrung nach § 56 StGB. Liefert pri... |
| `bewaehrung-auflagen-bewaehrungswiderruf-56f` | Bewaehrung Auflagen Bewaehrungswiderruf 56F im Plugin Strafzumessung: prüft konkret Auflagen § 56b StGB und Weisungen § 56c StGB im, Widerruf der Strafaussetzung zur Bewaehrung nach § 56f StGB, Freiheitsstrafe ohne Bewaehrung. Liefert pr... |
| `bewaehrung-interessen-deutschem` | Bewaehrung Interessen Deutschem im Plugin Strafzumessung: prüft konkret Bewaehrung, Deutschem, Freiheitsstrafe. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `freiheitsstrafe-strafmass-geldstrafe` | Freiheitsstrafe Strafmass Geldstrafe im Plugin Strafzumessung: prüft konkret Konkrete Zumessung der Freiheitsstrafe nach §§ 38 39 46 StGB, Bestimmung der Tagessatzanzahl der Geldstrafe nach § 40 Abs, Vorrang der Geldstrafe vor kurzer Fre... |
| `geldstrafe-grossen-rechtsmittel` | Geldstrafe Grossen Rechtsmittel im Plugin Strafzumessung: prüft konkret Geldstrafe, Grossen, Rechtsmittel-, Bewährungs- und Gesamtstrafenfolgen nach der Zumessung. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem... |
| `gesamtstrafenbildung-stgb-gestaendnis` | Gesamtstrafenbildung Stgb Gestaendnis im Plugin Strafzumessung: prüft konkret Erstinstanzliche Gesamtstrafenbildung bei Realkonkurrenz §§, Gestaendnis als Strafmilderungsgrund, Haerteausgleich bei nachtraeglicher Gesamtstrafenbildung. Li... |
| `jgg-jugendstrafe-minder-schwerer` | JGG Jugendstrafe Minder Schwerer im Plugin Strafzumessung: prüft konkret Strafzumessung im Jugendstrafrecht, Strafrahmen-Modifikation durch minder schweren Fall, Nachtraegliche Gesamtstrafenbildung nach § 55 StGB. Liefert priorisierten O... |
| `orientierung-triage-paragraph-stgb-besonders` | Orientierung Triage Paragraph Stgb Besonders im Plugin Strafzumessung: prüft konkret Einstieg und Triage im Plugin Strafzumessung, Grundsatznorm der Strafzumessung § 46 StGB, Besonders. Liefert priorisierten Output mit Norm-Pinpoints, Ri... |
| `regelbeispiele-stgb-strafbefehl` | Regelbeispiele Stgb Strafbefehl im Plugin Strafzumessung: prüft konkret Regelbeispiele, Stgb, Strafbefehl. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `schwerer-fehlerkatalog` | Schwerer Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `strafbefehl-stpo-strafmilderung-stgb` | Strafbefehl Stpo Strafmilderung Stgb im Plugin Strafzumessung: prüft konkret Strafzumessung im Strafbefehl § 407 StPO, Strafmilderung nach § 49 StGB, Strafrahmen-Logik vor der konkreten Zumessung. Liefert priorisierten Output mit Norm-Pi... |
| `strafkammer-strafzumessung` | Strafkammer Strafzumessung im Plugin Strafzumessung: prüft konkret Strafkammer, Strafzumessung, Strafzumessungstatsachen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `strafrecht-verfahrensstadium-strafbefehl` | Strafrecht Verfahrensstadium Strafbefehl im Plugin Strafzumessung: prüft konkret Strafrecht, Strafzumessung vom Strafbefehl bis zur großen Strafkammer, Taeter-Opfer-Ausgleich § 46a StGB und. Liefert priorisierten Output mit Norm-Pinpoint... |
| `strafz-aufklaerungshilfe-kronzeuge` | Strafz Aufklaerungshilfe Kronzeuge im Plugin Strafzumessung: prüft konkret Spezialfall Aufklaerungshilfe Kronzeugenregelung § 46b StGB, Spezialfall Sicherungsverwahrung §§ 66 ff, Leitfaden Strafrahmenmilderung § 49 StGB und benannte. Lie... |
| `strafz-strafzumessungstatsachen` | Strafz Strafzumessungstatsachen im Plugin Strafzumessung: prüft konkret Bauleiter Strafzumessungstatsachen § 46 StGB, Katalog der Strafzumessungstatsachen § 46 Abs, Bestimmung der Tagessatzhoehe nach § 40 Abs. Liefert priorisierten Outpu... |
| `strafzumessung-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `strafzumessung-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `strafzumessung-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `strafzumessung-output-waehlen` | Output wählen im Plugin Strafzumessung: Diese Output-Weiche für Strafzumessung entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `strafzumessung-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `strafzumessung-regelbeispiele-strafrahmenwahl` | Regelbeispiele Strafrahmenwahl im Plugin Strafzumessung: prüft konkret Chronologie und Belegmatrix im Plugin strafzumessung, Fristen- und Risikoampel im Plugin strafzumessung, Regelbeispielkataloge im Strafrecht, Bandentat. Liefert prior... |
| `strafzumessung-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `tagessatz-quellenkarte` | Tagessatz Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verstaendigung-257c` | Verstaendigung 257c im Plugin Strafzumessung: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
