# Insolvenzrecht-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`insolvenzrecht`) | [`insolvenzrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/insolvenzrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Fortbestehensprognose Paragrafix GmbH** (`fortbestehensprognose-paragrafix-gmbh`) | [Gesamt-PDF lesen](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf) | [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |
| **LUMEN Studios GmbH — Insolvenz- und Wirtschaftsstrafverfahren** (`lumen-studios-insolvenz-strafverfahren`) | [Gesamt-PDF lesen](../testakten/lumen-studios-insolvenz-strafverfahren/gesamt-pdf/lumen-studios-insolvenz-strafverfahren_gesamt.pdf) | [`testakte-lumen-studios-insolvenz-strafverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) |
| **Projekt Nachtfalter — Private Equity Buyout, Schuldschein und NPL-Portfolio** (`private-equity-buyout-schuldschein-npl-heidelberg`) | [Gesamt-PDF lesen](../testakten/private-equity-buyout-schuldschein-npl-heidelberg/gesamt-pdf/private-equity-buyout-schuldschein-npl-heidelberg_gesamt.pdf) | [`testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-private-equity-buyout-schuldschein-npl-heidelberg.zip) |
| **Sanierungsgewinn im Insolvenzplan — Grossbach Druckguss & Präzision GmbH & Co. KG Erfurt (2026)** (`sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026`) | [Gesamt-PDF lesen](../testakten/sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026/gesamt-pdf/sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026_gesamt.pdf) | [`testakte-sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sanierungsgewinn-insolvenzplan-grossbach-druckguss-erfurt-2026.zip) |
| **Sanierungsgewinn bei solventer GmbH-Liquidation — Strassburger Handelshof GmbH (Berlin-Charlottenburg)** (`sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026`) | [Gesamt-PDF lesen](../testakten/sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026/gesamt-pdf/sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026_gesamt.pdf) | [`testakte-sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sanierungsgewinn-solvente-liquidation-strassburger-handelshof-2026.zip) |
| **Sanierungsgewinn im StaRUG-Plan — Pellbach Windenergie GmbH Brandenburg (2026)** (`sanierungsgewinn-starug-plan-windenergie-pellbach-2026`) | [Gesamt-PDF lesen](../testakten/sanierungsgewinn-starug-plan-windenergie-pellbach-2026/gesamt-pdf/sanierungsgewinn-starug-plan-windenergie-pellbach-2026_gesamt.pdf) | [`testakte-sanierungsgewinn-starug-plan-windenergie-pellbach-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-sanierungsgewinn-starug-plan-windenergie-pellbach-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Insolvenz- und sanierungsrechtliche Skills nach deutschem Recht (InsO, StaRUG, COVInsAG-Nachwirkungen). Zielgruppe: Insolvenzverwalter, beratende Rechtsanwälte (Insolvenz-/Sanierungsrecht), Geschäftsführer, Vorstände, Sanierungsberater, Wirtschaftsprüfer (IDW-S-11-/S-6-/S-9-Praxis).


## Enthaltene Skills

| Skill | Zweck |
|---|---|
| `zahlungsunfaehigkeit-pruefung-17-inso` | Prüfung der Zahlungsunfähigkeit gem. § 17 InsO anhand BGH-Liquiditätsstatus (10%-/3-Wochen-Schwelle) |
| `ueberschuldung-pruefung-19-inso` | Zweistufige Überschuldungsprüfung gem. § 19 InsO: Fortbestehensprognose + insolvenzrechtlicher Überschuldungsstatus |
| `liquiditaetsvorschau-insolvenzrechtlich` | Rollierende 13-/26-/52-Wochen-Liquiditätsvorschau mit Ampel als Beweismittel für § 17 InsO und Fortbestehensprognose § 19 InsO; Excel-Export |
| `antragspflicht-15a-inso` | Höchstfrist nach § 15a InsO, Haftung bei Insolvenzverschleppung, Schutz Geschäftsführer/Vorstand |
| `glaeubigerantrag-pruefung` | Prüfung Zulässigkeit/Begründetheit eines Gläubigerantrags (§ 14 InsO), Glaubhaftmachung Forderung + Eröffnungsgrund |

## Abgrenzung zu den Schwester-Plugins

- Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Dieses Plugin `insolvenzrecht` ist **gerichtsfähig-formal** ausgerichtet: Es liefert die rechtlichen Subsumtionsbausteine und Beweismittel, wenn die Krise bereits eingetreten ist — Zeitpunkt der Zahlungsunfähigkeit, Überschuldungsstatus zum Stichtag, Antragspflichtfrist, Haftung Geschäftsleiter.

## Rechtlicher Rahmen (übergreifend)

- **InsO**: §§ 14, 15, 15a, 16, 17, 18, 19, 130, 131, 133, 142
- **StaRUG**: §§ 29 ff. (Restrukturierungsverfahren), § 102 (Hinweispflicht)
- **GmbHG**: § 64 a.F. (ersetzt durch § 15b InsO), § 30 (Auszahlungsverbot)
- **AktG**: § 92 Abs. 2 (Anzeigepflichten), § 93 (Sorgfaltspflicht)
- **HGB**: § 252 Abs. 1 Nr. 2 (going concern)
- **StGB**: §§ 283–283d (Bankrott, Verletzung der Buchführungspflicht), § 266a (Vorenthalten Arbeitsentgelt)

## Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Lizenz

Doppellizenziert unter Apache License, Version 2.0 ODER MIT License, nach Wahl der Nutzerin / des Nutzers (`SPDX-License-Identifier: Apache-2.0 OR MIT`). Siehe `LICENSE`, `LICENSE-APACHE`, `LICENSE-MIT` und `NOTICE` im Repository-Wurzelverzeichnis.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anfechtungsrechte-antragspflicht-15a` | Anfechtungsrechte Antragspflicht 15A: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `feststellung-sonderfall-glaeubigerantrag-inso` | Feststellung Sonderfall Glaeubigerantrag Inso: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `glaeubigerantrag-glaeubigerausschuss` | Glaeubigerantrag Glaeubigerausschuss: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `glaeubigerausschuss-fristennotiz` | Glaeubigerausschuss Fristennotiz: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-gerichtliche-aufsichtswege` | Inso Gerichtliche Aufsichtswege: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-lma-facility-massearmut` | Inso LMA Facility Massearmut: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-npl-kreditkauf-restschuldbefreiung` | Inso NPL Kreditkauf Restschuldbefreiung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-pl` | Inso PL: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `inso-tabelle-verbraucherinsolvenz-leitfaden` | Inso Tabelle Verbraucherinsolvenz Leitfaden: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `insol-sanierungsgewinn-7b-debt-equity` | Insol Sanierungsgewinn 7B Debt Equity: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `insol-sanierungsgewinn-insolvenzreife` | Insol Sanierungsgewinn Insolvenzreife: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `insol-sanierungsgewinn-liquidation` | Insol Sanierungsgewinn Liquidation: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `insol-sanierungsgewinn-uebertragende` | Insol Sanierungsgewinn Uebertragende: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `insolvenzrecht-anschluss` | Anschluss: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `insolvenzrecht-antragspflicht-15a-17-19` | Antragspflicht 15A 17 19: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `insolvenzrecht-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `insolvenzrecht-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `insolvenzrecht-kaltstart-interview` | Kaltstart-Interview für das Insolvenzrecht-Plugin. Befüllt das Praxisprofil unter ~/.claude/plugins/config/claude-fuer-deutsches-recht/insolvenzrecht/CLAUDE.md mit Angaben zur Rolle (Insolvenzverwalter / Sachwalter / beratender Anwalt /... |
| `insolvenzrecht-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `insolvenzrecht-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `insolvenzrecht-rechtsquellen` | Rechtsquellen: Zahlen, Schwellenwerte und Berechnung im Insolvenzrecht: fachlich vertiefter Fachmodul mit Normenradar (InsO/StaRUG/GesR), Tatbestands-/Beweislastmatrix, Fristen- und Formcheck, Gegenargumenten, Fehlerbremse und direkt nut... |
| `insolvenzrecht-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `insolvenzrechtliche-livecheck-red-team` | Insolvenzrechtliche Livecheck RED Team: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `internationales-drittstaaten-konzerninsolvenz` | Internationales Drittstaaten Konzerninsolvenz: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `liquiditaetsvorschau-insolvenzrechtlich` | Erstellt und bewertet die rollierende Liquiditätsvorschau als strukturierte Arbeitsgrundlage für insolvenzrechtliche Tatbestände nach § 17 InsO (Zahlungsunfähigkeit) und § 19 Abs. 2 InsO (Fortbestehensprognose). Lädt, wenn geprüft werden... |
| `rechtsabteilung-lieferantenpool-npl` | Rechtsabteilung Lieferantenpool NPL: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `triage-verbraucherinsolvenz` | Triage Verbraucherinsolvenz: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `uebertragende-sanierung-auslaendischer-office` | Uebertragende Sanierung Auslaendischer Office: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verfahrenstypen-quellenkarte` | Verfahrenstypen Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
