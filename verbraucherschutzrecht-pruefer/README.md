# Verbraucherschutzrecht Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verbraucherschutzrecht-pruefer`) | [`verbraucherschutzrecht-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verbraucherschutzrecht-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Verbraucherakte SmartMeter-Abo** (`verbraucherschutzrecht-smartmeter-abo-plattform`) | [Gesamt-PDF lesen](../testakten/verbraucherschutzrecht-smartmeter-abo-plattform/gesamt-pdf/verbraucherschutzrecht-smartmeter-abo-plattform_gesamt.pdf) | [`testakte-verbraucherschutzrecht-smartmeter-abo-plattform.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verbraucherschutzrecht-smartmeter-abo-plattform.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin prüft verbraucherschützende Vorschriften nicht als lose Sammlung, sondern als Schutzarchitektur: Informationspflicht, Widerruf, AGB-Kontrolle, Gewährleistung, Lauterkeit, Streitbeilegung, Plattform und Durchsetzung.

## Start

Beginne mit `verbraucherschutzrecht-pruefer-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

## Arbeitsweise

- Es arbeitet mit Akten- und Fristenlogik statt mit Bauchgefühl.
- Es trennt Rechtsgrundlage, Verfahren, Beweis, Kosten, Kommunikation und Eskalation.
- Es soll Nutzerinnen und Nutzer befähigen: verständliche Erklärung, präzise Rückfragen, dann belastbarer Entwurf.
- Rechtsprechung und Gesetzesstände werden nicht halluziniert, sondern als Live-Check über amtliche oder frei zugängliche Quellen markiert.

## Typische Outputs

- Kaltstart-Interview und Aktenlandkarte
- Behörden-, Gerichts- oder Gegneranschreiben
- Widerspruchs-/Klage-/Eilantragsbausteine
- Kosten-, Fristen- und Zuständigkeitsmatrix
- Dashboard/Tracker für laufende Vorgänge
- Kurzfassung für Mandant, Vorstand, Verband, Redaktion oder Bürgerin

## Quellenhygiene

Siehe [`references/QUELLEN.md`](./references/QUELLEN.md). Dieses Plugin gibt keine endgültige Rechtsberatung, sondern robuste Arbeitsfassungen, Prüfpfade und Dokumentationshilfen.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 30 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `vbr-001-kaltstart-verbraucherfall-sortieren` | Verbraucherschutzrecht Prüfer: Kaltstart Verbraucherfall sortieren. Kaltstart Verbraucherfall sortieren im Fachgebiet Verbraucherschutzrecht Prüfer als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `vbr-digitale-inhalte-saas-verbraucher` | Vbr 080 Digitale Inhalte Behoerdenmeldung Prue, Vbr 081 Saas Für Verbraucher Anspruch Prüfen, Vbr 082 Saas Für Verbraucher Widerruf Formuli, Vbr 084 Saas Für Verbraucher Beweise Sichern: wählt den konkreten Prüfpfad, trennt Frist, Zustän... |
| `vbr-digitale-inhalte-schlichtung-waehlen` | Vbr 076 Digitale Inhalte Beschwerde Schreiben, Vbr 077 Digitale Inhalte Schlichtung Waehlen, Vbr 078 Digitale Inhalte Klagepfad Skizzieren, Vbr 079 Digitale Inhalte Vergleich Vorschlagen: wählt den konkreten Prüfpfad, trennt Frist, Zustä... |
| `vbr-digitale-inhalte-widerruf-formulieren` | Vbr 071 Digitale Inhalte Anspruch Prüfen, Vbr 072 Digitale Inhalte Widerruf Formulieren, Vbr 074 Digitale Inhalte Beweise Sichern, Vbr 075 Digitale Inhalte Agb Redlinen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege u... |
| `vbr-fernabsatz-anspruch-widerruf-formulieren` | Vbr 031 Fernabsatz Anspruch Prüfen, Vbr 032 Fernabsatz Widerruf Formulieren, Vbr 034 Fernabsatz Beweise Sichern, Vbr 035 Fernabsatz Agb Redlinen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und l... |
| `vbr-fernabsatz-behoerdenmeldung-online-shop` | Vbr 040 Fernabsatz Behoerdenmeldung Prüfen, Vbr 041 Online Shop Anspruch Prüfen, Vbr 042 Online Shop Widerruf Formulieren, Vbr 044 Online Shop Beweise Sichern: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsg... |
| `vbr-fernabsatz-beschwerde-schlichtung-waehlen` | Vbr 036 Fernabsatz Beschwerde Schreiben, Vbr 037 Fernabsatz Schlichtung Waehlen, Vbr 038 Fernabsatz Klagepfad Skizzieren, Vbr 039 Fernabsatz Vergleich Vorschlagen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rec... |
| `vbr-haustuergeschaeft-frist-fernabsatz` | Vbr 023 Haustuergeschaeft Frist Berechnen, Vbr 033 Fernabsatz Frist Berechnen, Vbr 043 Online Shop Frist Berechnen, Vbr 053 Marketplace Frist Berechnen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlag... |
| `vbr-marketplace-beweise-agb-redlinen` | Vbr 054 Marketplace Beweise Sichern, Vbr 055 Marketplace Agb Redlinen, Vbr 056 Marketplace Beschwerde Schreiben, Vbr 057 Marketplace Schlichtung Waehlen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundla... |
| `vbr-marketplace-klagepfad-vorschlagen` | Vbr 058 Marketplace Klagepfad Skizzieren, Vbr 059 Marketplace Vergleich Vorschlagen, Vbr 060 Marketplace Behoerdenmeldung Prüfen, Vbr 061 Abo Falle Anspruch Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Re... |
| `vbr-online-shop-beschwerde-schreiben` | Vbr 045 Online Shop Agb Redlinen, Vbr 046 Online Shop Beschwerde Schreiben, Vbr 047 Online Shop Schlichtung Waehlen, Vbr 048 Online Shop Klagepfad Skizzieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgr... |
| `vbr-saas-verbraucher-beschwerde-schre` | Vbr 085 Saas Für Verbraucher Agb Redlinen, Vbr 086 Saas Für Verbraucher Beschwerde Schre, Vbr 087 Saas Für Verbraucher Schlichtung Waeh, Vbr 088 Saas Für Verbraucher Klagepfad Skizzi: wählt den konkreten Prüfpfad, trennt Frist, Zuständig... |
| `vbr-smart-device-agb-redlinen-beschwerde` | Vbr 094 Smart Device Beweise Sichern, Vbr 095 Smart Device Agb Redlinen, Vbr 096 Smart Device Beschwerde Schreiben, Vbr 097 Smart Device Schlichtung Waehlen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgru... |
| `vbr-smart-verbraucherrecht-abo` | Vbr 098 Smart Device Klagepfad Skizzieren, Vbr 099 Smart Device Vergleich Vorschlagen, Verbraucherrecht Abo Kündigung Button, Verbraucherrecht Behörden Beschwerden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Re... |
| `vbr-telekommunikation` | Vbr 017 Telekommunikation Und Laufzeit, Vbr 018 Finanzdienstleistung Fernabsatz, Vbr 020 Verbraucherbericht Erzeugen, Vbr 021 Haustuergeschaeft Anspruch Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechts... |
| `vbr-unternehmerrolle` | Vbr 003 Unternehmerrolle Und Plattformrolle Pr, Vbr 004 Informationspflichten Matrix Bauen, Vbr 005 Widerrufsrecht Und Erloeschen Prüfen, Vbr 007 Digitale Produkte Und Updatepflichten: wählt den konkreten Prüfpfad, trennt Frist, Zuständi... |
| `verbraucherrecht-abo-falle-frist-digitale-inhalte-saas` | Abo Falle Frist Berechnen / Digitale Inhalte Frist Berechnen / Saas Verbraucher Frist Berechnen / Smart Device Frist Berechnen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten b... |
| `verbraucherrecht-abo-falle-schlichtung-klagepfad-vergleich` | Abo Falle Schlichtung Waehlen / Abo Falle Klagepfad Skizzieren / Abo Falle Vergleich Vorschlagen / Abo Falle Behoerdenmeldung Pruefen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den näc... |
| `verbraucherrecht-abo-falle-widerruf-beweise-agb-beschwerde` | Abo Falle Widerruf Formulieren / Abo Falle Beweise Sichern / Abo Falle Agb Redlinen / Abo Falle Beschwerde Schreiben: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbaren... |
| `verbraucherrecht-agb-klausel-verbrauchervertrag-energievertrag` | Agb Klausel Verbrauchervertrag Prue / Energievertrag Abschlag / Gesundheit Pflegevertrag / Verbraucher Kleines Unternehmen E: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten bel... |
| `verbraucherrecht-digitale-energie` | Verbraucherrecht Digitale Produkte 327 Bgb, Verbraucherrecht Energie Smartmeter Waerme, Verbraucherrecht Finanzdienstleistung Online, Verbraucherrecht Plattform Marktplatz Haendler: wählt den konkreten Prüfpfad, trennt Frist, Zuständigke... |
| `verbraucherrecht-haustuergeschaeft-schlichtung-waehlen-klagepfad` | Haustuergeschaeft Schlichtung Waehlen / Haustuergeschaeft Klagepfad Skizzieren / Haustuergeschaeft Vergleich Vorschlage / Haustuergeschaeft Behoerdenmeldung Pru: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden P... |
| `verbraucherrecht-haustuergeschaeft-widerruf-formulieren-beweise` | Haustuergeschaeft Widerruf Formulieren / Haustuergeschaeft Beweise Sichern / Haustuergeschaeft Agb Redlinen / Haustuergeschaeft Beschwerde Schreiben: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und... |
| `verbraucherrecht-inkasso-mahnung-einordnen-gewaehrleistung` | Inkasso Mahnung Einordnen / Gewaehrleistung Garantie Trennen / Kaufrecht Reparatur Right To Repai / Reise Flug Schnittstelle: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten bel... |
| `verbraucherrecht-online-shop-vergleich-behoerdenmeldung` | Online Shop Vergleich Vorschlagen / Online Shop Behoerdenmeldung Pruefen / Marketplace Anspruch Pruefen / Marketplace Widerruf Formulieren: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt de... |
| `verbraucherrecht-preisangaben-reise` | Verbraucherrecht Preisangaben Und Dark Patterns, Verbraucherrecht Reise Flug Pauschal, Verbraucherrecht Right To Repair, Verbraucherrecht Verbandsklage Musterfeststellung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `verbraucherrecht-saas-verbraucher-vergleich-behoerdenmeldung` | Saas Verbraucher Vergleich Vorsch / Saas Verbraucher Behoerdenmeldung / Smart Device Anspruch Pruefen / Smart Device Widerruf Formulieren: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den... |
| `verbraucherrecht-waren-digitalen-elementen-preisangaben-dark` | Waren Digitalen Elementen / Preisangaben Dark Patterns / Uwg Irrefuehrung Verbraucherbezug / Schlichtung Vsbg Pruefen: führt durch diese fachlich verbundenen Arbeitsmodule, wählt den passenden Prüfpfad und erzeugt den nächsten belastbare... |
| `verbraucherrecht-waren-widerruf` | Verbraucherrecht Waren Mit Digitalen Elementen, Verbraucherrecht Widerruf Fernabsatz: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `verbraucherschutzrecht-pruefer-kaltstart-triage` | Verbraucherschutzrecht Prüfer: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
