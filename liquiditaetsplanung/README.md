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
Quote      = Lücke abs. ÷ (Passiva I + Passiva II)
```

**Ampel**: 🟢 Quote < 10 % und Liquidität KW t+2 ≥ 0 und < 2 Indizien. 🟡 Quote ≥ 10 %, KW t+2 ≥ 0, < 2 Indizien (schließbar). 🔴 sonst — § 17 InsO indiziert.

## Leitentscheidungen und Livecheck

Diese Entscheidungen sind als frei prüfbare Arbeitsanker gedacht; vor einer Mandatsausgabe immer Gericht, Datum, Aktenzeichen, Randnummer/Sachverhalt und Aussage anhand einer amtlichen oder frei zugänglichen Quelle nachziehen.

1. **BGH, Urteil vom 24.05.2005 - IX ZR 123/04**: Abgrenzung Zahlungsstockung/Zahlungsunfähigkeit; Liquiditätslücke von 10 Prozent oder mehr regelmäßig kritisch, wenn sie nicht kurzfristig nahezu vollständig geschlossen werden kann.
2. **BGH, Urteil vom 19.12.2017 - II ZR 88/16**: Liquiditätsstatus und Liquiditätsbilanz; Einbeziehung der innerhalb von drei Wochen fällig werdenden Verbindlichkeiten (Passiva II) in die Prüfung des § 17 InsO.
3. **BGH, Urteil vom 28.06.2022 - II ZR 112/21**: Zahlungsunfähigkeit kann mit geordneter Liquiditätsgegenüberstellung und Buchhaltungsunterlagen dargelegt werden; keine mechanische Scheingenauigkeit, sondern belegbare Zahlenbasis.
4. **Aktualitätsregel**: Keine BeckRS-, juris-, Kommentar- oder Aufsatzfundstellen aus Modellwissen. Wenn weitere Rechtsprechung gebraucht wird, erst live über `bundesgerichtshof.de`, `dejure.org` oder eine vom Nutzer bereitgestellte Quelle verifizieren.

Berufsständischer Hintergrund: Methodenrahmen zu Insolvenzeröffnungsgründen und Sanierungskonzepten; nicht als Ersatz für Gesetz, Rechtsprechung und konkrete Subsumtion zitieren.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

## Quellen-Disclaimer

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 69 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Fallrouting im Liquiditaetsplanung-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Fachmodule aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei Dok... |
| `allgemein-workflow-chronologie-fristen` | Nutze dies bei Allgemein, Chronologie Und Belegmatrix, Fristen Und Risikoampel, ...: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `ampel` | Nutze dies bei Ampel: Zahlen, Schwellenwerte und Berechnung: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `anschluss-routing` | Nutze dies zum Einstieg in Anschluss-Routing: klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `ausgabengruppen-fristennotiz-naechster` | Nutze dies bei Ausgabengruppen: Fristennotiz und nächster Schritt: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `chronologie-und-belegmatrix` | Nutze dies bei Chronologie und Belegmatrix: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `deutschem` | Nutze dies bei Deutschem: Tatbestandsmerkmale, Beweisfragen und Beleglage: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `deutschem-dokumentationspaket-excel` | Nutze dies bei Deutschem Tatbestand Beweis Und Belege, Dokumentationspaket Compliance Dokumentation Und Akte, Excel Behörden Gericht Und Registerweg: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert... |
| `dokumentationspaket` | Nutze dies für Unterlagen zu Dokumentationspaket: Compliance-Dokumentation und Aktenvermerk: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `dokumente-intake` | Nutze dies für Unterlagen zu Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `einstieg-routing` | Nutze dies zum Einstieg in Einstieg und Routing: klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `excel` | Nutze dies bei Excel: Behörden-, Gerichts- oder Registerweg: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `export` | Nutze dies bei Export: Schriftsatz-, Brief- und Memo-Bausteine: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `export-forecast-fortbestehensprognose` | Nutze dies bei Export Schriftsatz Brief Und Memo Bausteine, Forecast Risikoampel Und Gegenargumente, Fortbestehensprognose International Schnittstellen: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und lief... |
| `forecast` | Nutze dies bei Forecast: Risikoampel, Gegenargumente und Verteidigungslinien: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `fortbestehensprognose-international` | Nutze dies bei Fortbestehensprognose: Internationaler Bezug und Schnittstellen: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `fristen-und-risikoampel` | Nutze dies bei Fristen- und Risikoampel: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `idw-s6-integrierte-sanierungsplanung` | Verbindet Liquiditätsvorschau, GuV-Planung und Planbilanz zu einer Sanierungsplanung auf IDW-S-6-Niveau. Prüft Maßnahmenwirkung, Fortbestehensprognose, Sanierungsfähigkeit, Szenarien, Planungsannahmen, Belegregister, kleinere Unternehmen... |
| `insolvenzrecht` | Nutze dies bei Insolvenzrecht: Formular, Portal und Einreichungslogik: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `insolvenzrecht-liqui-sonderfall` | Nutze dies bei Insolvenzrecht Formular Portal Und Einreichung, Liqui Sonderfall Und Edge Case, Liquiditaetsplanung Erstpruefung Und Mandatsziel: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den... |
| `interessen` | Nutze dies bei Schnittstellen: Mehrparteienkonflikt und Interessenmatrix: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `interessen-verifikation-beweislast-vorschau` | Nutze dies bei Schnittstellen Mehrparteien Konflikt Und Interessen, Verifikation Beweislast Und Darlegungslast, Vorschau Dokumentenmatrix Und Lueckenliste: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und l... |
| `liqp-bankenreporting-leitfaden` | Leitfaden Bankenreporting bei Krise: Anforderungen Hausbank, Konsortium, KfW, Reportingfrequenz, Covenant-Reporting. Pruefraster fuer CFO und Berater. |
| `liqp-liquiditaetspool-cash-pooling-spezial` | Spezialfall Liquiditaetspool und Cash-Pooling im Konzern: § 30 GmbHG, BGH-Rechtsprechung, vollwertiger Rueckzahlungsanspruch. Pruefraster fuer Konzernmutter und Tochter. |
| `liqp-liquiditaetspool-cash-rollende-13wochen` | Nutze dies bei Liqp Liquiditaetspool Cash Pooling Spezial, Liqp Rollende 13wochen Bauleiter, Liqp Warenkredit Skonto Szenarien Spezial: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten... |
| `liqp-rollende-13wochen-bauleiter` | Bauleiter rollende 13-Wochen-Liquiditaetsplanung: Einnahmen / Ausgaben / Saldo / kumulierter Saldo, Granularitaet, Update-Zyklen. Pruefraster Mittelstand und Konzerntochter. |
| `liqp-warenkredit-skonto-szenarien-spezial` | Spezialfall Warenkredit und Skontostrategien in der Krise: Lieferantenverhandlung, Vorkasse, verlaengerter Eigentumsvorbehalt, Factoring. Pruefraster fuer Treasury. |
| `liqui-ausgabengruppen-systematik` | Ausgabengruppen systematisch erfassen: Personal (Lohn, SV, LSt), Material/Wareneinsatz, Miete, Energie, Versicherungen, Beratungs-/Anwaltskosten, Steuerzahlungen, Investitionen, Zinsen, Tilgung. Vorlage Tabelle. |
| `liqui-bei-drohender-zahlungsunfaehigkeit` | Liquiditaetsplanung bei drohender Zahlungsunfaehigkeit § 18 InsO: 24-Monats-Planung, Zugang StaRUG-Restrukturierung, Geschaeftsleiterpflichten. Pruefraster und Schnittstelle Insolvenzantrag. |
| `liqui-bei-eingetretener-zahlungsunfaehigkeit` | Liquiditaetsplanung bei eingetretener Zahlungsunfaehigkeit § 17 InsO: 3-Wochen-Vorschau zur Pruefung Insolvenzantragspflicht, Liquiditaetsluecke kleiner 10 Prozent + Schliessung binnen 3 Wochen waere Liquiditaetsstockung. Pruefraster BGH... |
| `liqui-cash-pooling-konzern` | Cash-Pooling im Konzern: rechtliche Risiken Existenzvernichtung BGH II ZR 78/06, Sanierungstauglichkeit, Pruefung Avale gegen Konzerngesellschaften, Steuerrisiken § 8b KStG. Output: Cash-Pool-Risiko-Memo. |
| `liqui-drohender-zahlungsunfaehigkeit` | Nutze dies bei Liqui Bei Drohender Zahlungsunfaehigkeit, Liqui Bei Eingetretener Zahlungsunfaehigkeit, Liqui Für Bankgespraech: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastba... |
| `liqui-eingangsdaten-checkliste` | Eingangsdaten-Checkliste fuer Liquiditaetsplanung: BWA, OPOS Debitoren/Kreditoren, Kontoauszuege, Steuerkonten, SV-Konten, Personalkosten, Investitionsplanung. Pruefliste Quellen und Vollstaendigkeit. Output: standardisiertes Datentemplate. |
| `liqui-eingangsdaten-idw-s6-liqp` | Nutze dies bei Liqui Eingangsdaten Checkliste, Idw S6 Integrierte Sanierungsplanung, Liqp Bankenreporting Leitfaden: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeits... |
| `liqui-fuer-bankgespraech` | Liquiditaetsplanung fuer Bankgespraech: kompakte Vorlage 13 Wochen + Jahresansicht, Annahmen-Block, Sensitivitaet, Kreditlinien-Ausnutzung, Begleittext. Empfehlung: realistisch, nicht zu optimistisch, mit Fallback-Hebeln. |
| `liqui-grundbegriffe-cashflow` | Liquiditaetsplanung Grundbegriffe: Cashflow vs. Gewinn, indirekte vs. direkte Methode, Liquiditaet 1./2./3. Grades, Working Capital. Abgrenzung zur GuV-Planung. Empfehlung: direkte Methode fuer 13-Wochen-Forecast, indirekte fuer Jahrespl... |
| `liqui-grundbegriffe-cashflow-kreditlinien` | Nutze dies bei Liqui Grundbegriffe Cashflow, Liqui Kreditlinien Prüfen, Liqui Mahnstufen Debitoren: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `liqui-kreditlinien-pruefen` | Kreditlinien pruefen: Kontokorrent, Investitionskredit, Avalkredit, Factoring-Linie, Lieferantenkredit. Ausnutzungsgrade, Tilgungsplaene, Sicherheiten, Covenants. Pruefraster fuer Bankgespraech. |
| `liqui-leasing-lp-restrukturierungsplan-starug` | Nutze dies bei Liqui Mit Leasing Und Lp, Liqui Restrukturierungsplan Starug, Liqui Saisonalitaet Erkennen: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `liqui-mahnstufen-debitoren` | Debitorenseite optimieren: DSO-Kennzahl, Mahnstufen, Skontostrategie, Factoring-Optionen, Forderungsausfallversicherung. Empfehlung: 3-Wochen-Forecast getrennt nach Kategorie 'sicher / wahrscheinlich / fraglich'. |
| `liqui-mit-leasing-und-lp` | Leasing- und Lebenspartnerzahlungen in Liquiditaetsplan: operate lease als opex, finance lease wirkt sich auf Bilanz aus, vorzeitige Aufloesung kostenpflichtig. Empfehlung: Aufnahme nach Faelligkeit, Pruefung Beendigungskosten. |
| `liqui-restrukturierungsplan-starug` | Liquiditaetsplanung im Restrukturierungsplan StaRUG: Plan-Liquiditaet, Sanierungsbeitraege Glaeubiger, Working-Capital-Plan, Cash-Out-Termine. Output: integrierter Plan und Glaeubigerverteilungsschema. |
| `liqui-saisonalitaet-erkennen` | Saisonalitaet erkennen: Vorjahres-Kontodaten gegen Liquiditaetsplan abgleichen, Monats- und Wochenmuster, Sondereffekte (Inventur, Jahresabschluss, Ferien). Empfehlung: saisonale Korrekturfaktoren je Branche. |
| `liqui-sondereffekt-grossauftrag` | Sondereffekt Grossauftrag in Liquiditaetsplanung: Vorfinanzierung Material, Abschlagsrechnungen, Sicherheitseinbehalt § 17 VOB-B, MaBV-Raten bei Bauauftraegen. Liquiditaetsspitze pruefen, Zwischenfinanzierung organisieren. |
| `liqui-sondereffekt-grossauftrag-stundungs` | Nutze dies bei Liqui Sondereffekt Grossauftrag, Liqui Stundungs Strategie, Liqui Szenarien Aufbauen: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `liqui-sonderfall-edge-case` | Nutze dies bei Liqui: Sonderfall und Edge-Case-Prüfung: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `liqui-stundungs-strategie` | Stundungs-Strategie mit Finanzamt, Krankenkassen, Lieferanten: § 222 AO Stundung, Ratenzahlungsvereinbarung Krankenkasse, Lieferantenstundung. Pruefraster: wann beantragen, Mindestanforderungen Antrag, Reichweite (keine Glaeubigerbenacht... |
| `liqui-szenarien-aufbauen` | Szenarien aufbauen: Base Case, Best Case, Worst Case (mit Stresshebel: Umsatzeinbruch, Forderungsausfaelle, Lieferantenforderungen). Empfehlung: drei Szenarien mit dokumentierten Annahmen, Sensitivitaeten in Excel. |
| `liquiditaetsplanung` | Nutze dies bei Liquiditaetsplanung: Erstprüfung, Rollenklärung und Mandatsziel: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `liquiditaetsstatus-quellenbelege` | Liquiditätsstatus nur aus belastbaren Quellenbelegen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `liquiditaetsstatus-quellenbelege-live-quote` | Nutze dies bei Liquiditaetsstatus Quellenbelege, Live Mandantenkommunikation Entscheidungsvorlage, Quote Verhandlung Vergleich Und Eskalation: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nä... |
| `liquiditaetsvorschau-3-6-12-monate` | Rollierende Liquiditaetsvorschau fuer 3/6/12 Monate mit Fortfuehrungsprognose, Wochenraster, Excel-Export und Quellenhygiene. Rechtsprechung nur nach Live-Pruefung. |
| `liquiditaetsvorschau-3wochen` | Drei-Wochen-Liquiditaetsvorschau nach § 17 InsO mit Wochenraster, Excel-Export, Quote/Luecken-Ampel und Dokumentation. Rechtsprechung nur nach Live-Pruefung. |
| `liquiditaetsvorschau-3wochen-02` | Nutze dies bei Liquiditaetsvorschau 3wochen, Liquiditaetsvorschau Insolvenzrechtlich, Ampel Zahlen Schwellen Und Berechnung: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren... |
| `liquiditaetsvorschau-insolvenzrechtlich` | Arbeitsmodul zu liquiditaetsvorschau insolvenzrechtlich: prüft Normtext, Nutzerangaben, Fristen, Belege und verifizierte Rechtsprechung mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle. |
| `live` | Nutze dies bei Live: Mandantenkommunikation und Entscheidungsvorlage: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `luecken-quellenkarte` | Nutze dies zur Quellenprüfung bei Luecken Quellenkarte: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `mandantenkommunikation` | Nutze dies bei Mandantenkommunikation: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `mandantenkommunikation-redteam-qualitygate` | Nutze dies bei Mandantenkommunikation, Redteam Qualitygate, Ausgabengruppen Fristennotiz Und Naechster Schritt: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeitsschritt. |
| `output-waehlen` | Nutze dies bei Output wählen: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `quellen-livecheck` | Nutze dies zur Quellenprüfung bei Rechtsquellen-Livecheck: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `quote` | Nutze dies bei Quote: Verhandlung, Vergleich und Eskalation: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `rechtsprechung-fehlerkatalog` | Nutze dies als Fehlerbremse bei Rechtsprechung Fehlerkatalog: prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `redteam-qualitygate` | Nutze dies als Fehlerbremse bei Red-Team Qualitygate: prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `unterlagen-luecken` | Nutze dies für Unterlagen zu Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verifikation-beweislast-darlegungslast` | Nutze dies bei Verifikation: Beweislast, Darlegungslast und Substantiierung: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `vorschau` | Nutze dies bei Vorschau: Dokumentenmatrix, Lückenliste und Nachforderung: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `wochen` | Nutze dies bei Wochen: Fristen, Form, Zuständigkeit und Rechtsweg: prüft die konkrete Fachfrage mit Normen, Belegen, Risiken, Gegenargumenten und einem verwertbaren Arbeitsergebnis. |
| `wochen-liqui-ausgabengruppen-liqui-cash` | Nutze dies bei Wochen Fristen Form Und Zustaendigkeit, Liqui Ausgabengruppen Systematik, Liqui Cash Pooling Konzern: führt durch diese fachlich verbundenen Module, wählt den passenden Prüfpfad und liefert den nächsten belastbaren Arbeits... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
