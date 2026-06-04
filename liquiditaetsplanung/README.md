# Liquiditätsplanung — Power-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`liquiditaetsplanung`) | [`liquiditaetsplanung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/liquiditaetsplanung.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Edelholz Manufaktur Berlin GmbH — Liquiditäts- und Steuerakte** (`beispielakte-edelholz-berlin`) | [Gesamt-PDF lesen](../testakten/beispielakte-edelholz-berlin/gesamt-pdf/beispielakte-edelholz-berlin_gesamt.pdf) | [`testakte-beispielakte-edelholz-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-beispielakte-edelholz-berlin.zip) |
| **Forschungszulage Riedblick Sensorik GmbH** (`forschungszulage-sensorik-startup-taunus`) | [Gesamt-PDF lesen](../testakten/forschungszulage-sensorik-startup-taunus/gesamt-pdf/forschungszulage-sensorik-startup-taunus_gesamt.pdf) | [`testakte-forschungszulage-sensorik-startup-taunus.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-forschungszulage-sensorik-startup-taunus.zip) |
| **Fortbestehensprognose Paragrafix GmbH** (`fortbestehensprognose-paragrafix-gmbh`) | [Gesamt-PDF lesen](../testakten/fortbestehensprognose-paragrafix-gmbh/gesamt-pdf/fortbestehensprognose-paragrafix-gmbh_gesamt.pdf) | [`testakte-fortbestehensprognose-paragrafix-gmbh.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-fortbestehensprognose-paragrafix-gmbh.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

**Eigenständiges Power-Plugin** für wochenaktuelle Liquiditätsvorschauen nach deutschem Recht (§§ 17, 18, 19 InsO; § 1 StaRUG; BGH-Schema Passiva II). Funktioniert allein. Ergänzt sich optional mit `insolvenzrecht` und `steuerrecht-anwalt-und-berater`, hängt aber nicht von ihnen ab.

---

## Was ist drin

Vier Fachskills plus Allgemein-Skill, alle fachlich autark:

| Skill | Zweck | Horizont |
| --- | --- | --- |
| `idw-s6-integrierte-sanierungsplanung` | Brücke von Liquiditätsvorschau zu Sanierungskonzept: GuV, Planbilanz, Maßnahmenlog, Annahmenregister, Sensitivitäten und Sanierungsfähigkeits-Ampel. | 12-24 Monate |
| `liquiditaetsvorschau-3wochen` | Wochenaktuelle Vorprüfung § 17 InsO (Freitag-Stichtag), Verhältnis zu offenen Forderungen, Ampel. | 3 Wochen |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Planung mit Sensitivität (Best/Base/Worst), Fortbestehensprognose nach § 19 InsO und Übergabe in die Sanierungsplanung. | 13 / 26 / 52 Wochen |
| `liquiditaetsvorschau-insolvenzrechtlich` | Gerichtsfeste Liquiditätsbilanz nach BGH-Schema (Passiva II zwingend, Volumeneffekt der Quote, titulierte Forderungen mit Nennwert). | Stichtagsbezogen |

## Ergebnisformate

Jeder Skill liefert standardmäßig eine **Excel-Tabelle** nach der hinterlegten Vorlage (`assets/excel/Liquiditaetsplan-Wochenbasis.xlsx`, KW-Spalten × Kategorien-Zeilen, Freitag als Wochenstichtag). Zusätzlich auf Wahl:

- **Interaktives HTML-Padlet** (`assets/padlet/liquiditaets-padlet.html`) — single-file, autark, rechnet die Ampel live nach BGH-Schema, speichert in `localStorage`, exportiert/importiert JSON.
- **Markdown-Artefakt** (`assets/markdown/liquiditaets-artefakt-vorlage.md`) — Tabellen, Indizienliste, Kurzfazit; wird bei jeder Folgemeldung neu geschrieben.
- **Memo** im Gutachtenstil (DOCX oder Markdown) — **nur auf ausdrückliche Anfrage**.

Die Skills fragen einmal am Anfang nach Format und merken sich die Antwort.

## Banking

Jeder Skill fragt einmal nach der Datenquelle:

1. **Manuell** im Padlet/Artefakt/Chat.
2. **Datei-Import** — CAMT.053, MT940, CSV-Bankexport, DATEV-OPOS.
3. **Connector** — PSD2/FinTS oder verfügbare Anbieter (per `list_external_tools`).

Mandatsgeheimnis (§§ 203/204 StGB, § 43e BRAO) und Drittlandtransfer (DSGVO Art. 44 ff.) werden adressiert.

## BGH-Schema (Passiva II)

```
Aktiva I   = Bank + Kasse + freier zugesagter Kontokorrent (Stichtag)
Aktiva II  = Σ Einzahlungen KW t..t+2
Passiva I  = am Stichtag fällig, eingefordert, nicht echt gestundet
Passiva II = binnen 3 Wochen fällig (KW t+1 + KW t+2)

Lücke abs. = max(0, (Passiva I + Passiva II) − (Aktiva I + Aktiva II))
Quote      = Lücke abs. ÷ (Passiva I + Passiva II)   (Volumeneffekt
             Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
```

**Ampel**: 🟢 Quote < 10 % und Liquidität KW t+2 ≥ 0 und < 2 Indizien. 🟡 Quote ≥ 10 %, KW t+2 ≥ 0, < 2 Indizien (schließbar). 🔴 sonst — § 17 InsO indiziert.

## Leitentscheidungen (Volltexte: `references/rechtsprechung/`)

1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
1. Rechtsprechung live prüfen: Keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über amtliche oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

Berufsständischer Hintergrund: Methodenrahmen zu Insolvenzeröffnungsgründen und Sanierungskonzepten; nicht als Ersatz für Gesetz, Rechtsprechung und konkrete Subsumtion zitieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 26 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `kompendium-02-workflow-mandantenko-bis-spezial-ausgabengrup` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-ausgabengruppen-fristennotiz-und-naechster-schritt) und bewahrt deren Workfl... |
| `kompendium-03-spezial-wochen-frist-bis-liqui-cash-pooling-k` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-wochen-fristen-form-und-zustaendigkeit, liqui-ausgabengruppen-systematik, liqui-cash-pooling-konzern) und bewahrt deren Workflows, Normanke... |
| `kompendium-04-liqui-eingangsdaten-bis-liqp-bankenreporting` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (liqui-eingangsdaten-checkliste, idw-s6-integrierte-sanierungsplanung, liqp-bankenreporting-leitfaden) und bewahrt deren Workflows, Normanker, Prüfp... |
| `kompendium-05-liqp-liquiditaetspoo-bis-liqp-warenkredit-sko` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (liqp-liquiditaetspool-cash-pooling-spezial, liqp-rollende-13wochen-bauleiter, liqp-warenkredit-skonto-szenarien-spezial) und bewahrt deren Workflow... |
| `kompendium-06-liqui-bei-drohender-bis-liqui-fuer-bankgespr` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (liqui-bei-drohender-zahlungsunfaehigkeit, liqui-bei-eingetretener-zahlungsunfaehigkeit, liqui-fuer-bankgespraech) und bewahrt deren Workflows, Norm... |
| `kompendium-07-liqui-grundbegriffe-bis-liqui-mahnstufen-deb` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (liqui-grundbegriffe-cashflow, liqui-kreditlinien-pruefen, liqui-mahnstufen-debitoren) und bewahrt deren Workflows, Normanker, Prüfprogramme und Aus... |
| `kompendium-08-liqui-mit-leasing-un-bis-liqui-saisonalitaet` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (liqui-mit-leasing-und-lp, liqui-restrukturierungsplan-starug, liqui-saisonalitaet-erkennen) und bewahrt deren Workflows, Normanker, Prüfprogramme u... |
| `kompendium-09-liqui-sondereffekt-g-bis-liqui-szenarien-aufb` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (liqui-sondereffekt-grossauftrag, liqui-stundungs-strategie, liqui-szenarien-aufbauen) und bewahrt deren Workflows, Normanker, Prüfprogramme und Aus... |
| `kompendium-10-liquiditaetsvorschau-bis-spezial-ampel-zahlen` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (liquiditaetsvorschau-3wochen, liquiditaetsvorschau-insolvenzrechtlich, spezial-ampel-zahlen-schwellen-und-berechnung) und bewahrt deren Workflows,... |
| `kompendium-11-spezial-deutschem-ta-bis-spezial-excel-behoer` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-deutschem-tatbestand-beweis-und-belege, spezial-dokumentationspaket-compliance-dokumentation-und-akte, spezial-excel-behoerden-gericht-und-... |
| `kompendium-12-spezial-export-schri-bis-spezial-fortbestehen` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-export-schriftsatz-brief-und-memo-bausteine, spezial-forecast-risikoampel-und-gegenargumente, spezial-fortbestehensprognose-international-s... |
| `kompendium-13-spezial-insolvenzrec-bis-spezial-liquiditaets` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-insolvenzrecht-formular-portal-und-einreichung, spezial-liqui-sonderfall-und-edge-case, spezial-liquiditaetsplanung-erstpruefung-und-mandat... |
| `kompendium-14-spezial-liquiditaets-bis-spezial-quote-verhan` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-liquiditaetsstatus-quellenbelege, spezial-live-mandantenkommunikation-entscheidungsvorlage, spezial-quote-verhandlung-vergleich-und-eskalat... |
| `kompendium-15-spezial-schnittstell-bis-spezial-vorschau-dok` | liquiditaetsplanung: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-schnittstellen-mehrparteien-konflikt-und-interessen, spezial-verifikation-beweislast-und-darlegungslast, spezial-vorschau-dokumentenmatrix-... |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditaetsvorschau fuer 3/6/12 Monate mit Fortfuehrungsprognose, Wochenraster, Excel-Export und Quellenhygiene. Rechtsprechung nur nach Live-Pruefung. |
| `liquiditaetsvorschau-3wochen` | Drei-Wochen-Liquiditaetsvorschau nach § 17 InsO mit Wochenraster, Excel-Export, Quote/Luecken-Ampel und Dokumentation. Rechtsprechung nur nach Live-Pruefung. |
| `liquiditaetsvorschau-insolvenzrechtlich` | Workflow-Skill zu liquiditaetsvorschau insolvenzrechtlich. Nutzt Normtext, Nutzerangaben und verifizierte Quellen; Rechtsprechung nur nach Live-Pruefung mit Gericht, Datum und Aktenzeichen. |
| `spezial-luecken-livequellen-und-rechtsprechungscheck` | Luecken: Livequellen- und Rechtsprechungscheck im Plugin liquiditaetsplanung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-rechtsprechung-red-team-und-qualitaetskontrolle` | Rechtsprechung: Red-Team und Qualitätskontrolle im Plugin liquiditaetsplanung; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin liquiditaetsplanung: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin liquiditaetsplanung: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin liquiditaetsplanung: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin liquiditaetsplanung: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin liquiditaetsplanung: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin liquiditaetsplanung: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
