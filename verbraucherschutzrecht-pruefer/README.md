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

<!-- BEGIN TESTAKTEN-SECTION (auto-generated) -->

## Testakte

Zu diesem Plugin existiert eine vollständige Beispielakte: **Verbraucherakte SmartMeter-Abo** ([`testakten/verbraucherschutzrecht-smartmeter-abo-plattform/`](../testakten/verbraucherschutzrecht-smartmeter-abo-plattform/)).

Direkt-Download als ZIP: [testakte-verbraucherschutzrecht-smartmeter-abo-plattform.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verbraucherschutzrecht-smartmeter-abo-plattform.zip)

Die Akte ist absichtlich unordentlich, widersprüchlich und ungefiltert. Sie eignet sich für End-to-End-Tests, Demos und zum Üben.

<!-- END TESTAKTEN-SECTION (auto-generated) -->

Dieses Plugin prüft verbraucherschützende Vorschriften nicht als lose Sammlung, sondern als Schutzarchitektur: Informationspflicht, Widerruf, AGB-Kontrolle, Gewährleistung, Lauterkeit, Streitbeilegung, Plattform und Durchsetzung.

## Start

Beginne mit `allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| `allgemein` | Verbraucherschutzrecht Prüfer: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Spezialskill-Routing und erste Ausgabe. |
| `vbr-001-kaltstart-verbraucherfall-sortieren` | Verbraucherschutzrecht Prüfer: Kaltstart Verbraucherfall sortieren. Kaltstart Verbraucherfall sortieren im Fachgebiet Verbraucherschutzrecht Prüfer als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `vbr-abo-vbr-abo-vbr-abo-vbr-abo` | Nutze dies, wenn Vbr 062 Abo Falle Widerruf Formulieren, Vbr 064 Abo Falle Beweise Sichern, Vbr 065 Abo Falle Agb Redlinen, Vbr 066 Abo Falle Beschwerde Schreiben im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet werden soll. Au... |
| `vbr-abo-vbr-abo-vbr-abo-vbr-abo-02` | Nutze dies, wenn Vbr 067 Abo Falle Schlichtung Waehlen, Vbr 068 Abo Falle Klagepfad Skizzieren, Vbr 069 Abo Falle Vergleich Vorschlagen, Vbr 070 Abo Falle Behoerdenmeldung Prüfen im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet... |
| `vbr-abo-vbr-digitale-vbr-saas-vbr-smart` | Nutze dies, wenn Vbr 063 Abo Falle Frist Berechnen, Vbr 073 Digitale Inhalte Frist Berechnen, Vbr 083 Saas Für Verbraucher Frist Berechnen, Vbr 093 Smart Device Frist Berechnen im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet w... |
| `vbr-agb-vbr-energievertrag-vbr-gesundheit-vbr` | Nutze dies, wenn Vbr 006 Agb Klausel Im Verbrauchervertrag Prue, Vbr 016 Energievertrag Und Abschlag, Vbr 019 Gesundheit Und Pflegevertrag, Vbr 002 Verbraucher Oder Kleines Unternehmen E im Plugin Verbraucherschutzrecht Prüfer konkret be... |
| `vbr-digitale-inhalte-saas-verbraucher` | Nutze dies, wenn Vbr 080 Digitale Inhalte Behoerdenmeldung Prue, Vbr 081 Saas Für Verbraucher Anspruch Prüfen, Vbr 082 Saas Für Verbraucher Widerruf Formuli, Vbr 084 Saas Für Verbraucher Beweise Sichern im Plugin Verbraucherschutzrecht P... |
| `vbr-digitale-inhalte-schlichtung-waehlen` | Nutze dies, wenn Vbr 076 Digitale Inhalte Beschwerde Schreiben, Vbr 077 Digitale Inhalte Schlichtung Waehlen, Vbr 078 Digitale Inhalte Klagepfad Skizzieren, Vbr 079 Digitale Inhalte Vergleich Vorschlagen im Plugin Verbraucherschutzrecht... |
| `vbr-digitale-inhalte-widerruf-formulieren` | Nutze dies, wenn Vbr 071 Digitale Inhalte Anspruch Prüfen, Vbr 072 Digitale Inhalte Widerruf Formulieren, Vbr 074 Digitale Inhalte Beweise Sichern, Vbr 075 Digitale Inhalte Agb Redlinen im Plugin Verbraucherschutzrecht Prüfer konkret bea... |
| `vbr-fernabsatz-anspruch-widerruf-formulieren` | Nutze dies, wenn Vbr 031 Fernabsatz Anspruch Prüfen, Vbr 032 Fernabsatz Widerruf Formulieren, Vbr 034 Fernabsatz Beweise Sichern, Vbr 035 Fernabsatz Agb Redlinen im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet werden soll. Aus... |
| `vbr-fernabsatz-behoerdenmeldung-online-shop` | Nutze dies, wenn Vbr 040 Fernabsatz Behoerdenmeldung Prüfen, Vbr 041 Online Shop Anspruch Prüfen, Vbr 042 Online Shop Widerruf Formulieren, Vbr 044 Online Shop Beweise Sichern im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet we... |
| `vbr-fernabsatz-beschwerde-schlichtung-waehlen` | Nutze dies, wenn Vbr 036 Fernabsatz Beschwerde Schreiben, Vbr 037 Fernabsatz Schlichtung Waehlen, Vbr 038 Fernabsatz Klagepfad Skizzieren, Vbr 039 Fernabsatz Vergleich Vorschlagen im Plugin Verbraucherschutzrecht Prüfer konkret bearbeite... |
| `vbr-haustuergeschaeft-frist-fernabsatz` | Nutze dies, wenn Vbr 023 Haustuergeschaeft Frist Berechnen, Vbr 033 Fernabsatz Frist Berechnen, Vbr 043 Online Shop Frist Berechnen, Vbr 053 Marketplace Frist Berechnen im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet werden so... |
| `vbr-haustuergeschaeft-vbr-vbr` | Nutze dies, wenn Vbr 022 Haustuergeschaeft Widerruf Formulieren, Vbr 024 Haustuergeschaeft Beweise Sichern, Vbr 025 Haustuergeschaeft Agb Redlinen, Vbr 026 Haustuergeschaeft Beschwerde Schreiben im Plugin Verbraucherschutzrecht Prüfer ko... |
| `vbr-haustuergeschaeft-vbr-vbr-02` | Nutze dies, wenn Vbr 027 Haustuergeschaeft Schlichtung Waehlen, Vbr 028 Haustuergeschaeft Klagepfad Skizzieren, Vbr 029 Haustuergeschaeft Vergleich Vorschlage, Vbr 030 Haustuergeschaeft Behoerdenmeldung Pru im Plugin Verbraucherschutzrec... |
| `vbr-inkasso-vbr-gewaehrleistung-vbr-kaufrecht` | Nutze dies, wenn Vbr 012 Inkasso Und Mahnung Einordnen, Vbr 013 Gewährleistung Und Garantie Trennen, Vbr 014 Kaufrecht Reparatur Und Right To Repai, Vbr 015 Reise Und Flug Schnittstelle im Plugin Verbraucherschutzrecht Prüfer konkret bea... |
| `vbr-marketplace-beweise-agb-redlinen` | Nutze dies, wenn Vbr 054 Marketplace Beweise Sichern, Vbr 055 Marketplace Agb Redlinen, Vbr 056 Marketplace Beschwerde Schreiben, Vbr 057 Marketplace Schlichtung Waehlen im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet werden s... |
| `vbr-marketplace-klagepfad-vorschlagen` | Nutze dies, wenn Vbr 058 Marketplace Klagepfad Skizzieren, Vbr 059 Marketplace Vergleich Vorschlagen, Vbr 060 Marketplace Behoerdenmeldung Prüfen, Vbr 061 Abo Falle Anspruch Prüfen im Plugin Verbraucherschutzrecht Prüfer konkret bearbeit... |
| `vbr-online-shop-beschwerde-schreiben` | Nutze dies, wenn Vbr 045 Online Shop Agb Redlinen, Vbr 046 Online Shop Beschwerde Schreiben, Vbr 047 Online Shop Schlichtung Waehlen, Vbr 048 Online Shop Klagepfad Skizzieren im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet wer... |
| `vbr-online-vbr-vbr-marketplace-vbr` | Nutze dies, wenn Vbr 049 Online Shop Vergleich Vorschlagen, Vbr 050 Online Shop Behoerdenmeldung Prüfen, Vbr 051 Marketplace Anspruch Prüfen, Vbr 052 Marketplace Widerruf Formulieren im Plugin Verbraucherschutzrecht Prüfer konkret bearbe... |
| `vbr-saas-vbr-saas-vbr-smart-vbr-smart` | Nutze dies, wenn Vbr 089 Saas Für Verbraucher Vergleich Vorsch, Vbr 090 Saas Für Verbraucher Behoerdenmeldung, Vbr 091 Smart Device Anspruch Prüfen, Vbr 092 Smart Device Widerruf Formulieren im Plugin Verbraucherschutzrecht Prüfer konkre... |
| `vbr-saas-verbraucher-beschwerde-schre` | Nutze dies, wenn Vbr 085 Saas Für Verbraucher Agb Redlinen, Vbr 086 Saas Für Verbraucher Beschwerde Schre, Vbr 087 Saas Für Verbraucher Schlichtung Waeh, Vbr 088 Saas Für Verbraucher Klagepfad Skizzi im Plugin Verbraucherschutzrecht Prüf... |
| `vbr-smart-device-agb-redlinen-beschwerde` | Nutze dies, wenn Vbr 094 Smart Device Beweise Sichern, Vbr 095 Smart Device Agb Redlinen, Vbr 096 Smart Device Beschwerde Schreiben, Vbr 097 Smart Device Schlichtung Waehlen im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet werd... |
| `vbr-smart-vbr-verbraucherrecht-abo` | Nutze dies, wenn Vbr 098 Smart Device Klagepfad Skizzieren, Vbr 099 Smart Device Vergleich Vorschlagen, Verbraucherrecht Abo Kündigung Button, Verbraucherrecht Behörden Beschwerden im Plugin Verbraucherschutzrecht Prüfer konkret bearbeit... |
| `vbr-telekommunikation-vbr` | Nutze dies, wenn Vbr 017 Telekommunikation Und Laufzeit, Vbr 018 Finanzdienstleistung Fernabsatz, Vbr 020 Verbraucherbericht Erzeugen, Vbr 021 Haustuergeschaeft Anspruch Prüfen im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet w... |
| `vbr-unternehmerrolle-vbr` | Nutze dies, wenn Vbr 003 Unternehmerrolle Und Plattformrolle Pr, Vbr 004 Informationspflichten Matrix Bauen, Vbr 005 Widerrufsrecht Und Erloeschen Prüfen, Vbr 007 Digitale Produkte Und Updatepflichten im Plugin Verbraucherschutzrecht Prü... |
| `vbr-waren-vbr-preisangaben-vbr-uwg-vbr` | Nutze dies, wenn Vbr 008 Waren Mit Digitalen Elementen, Vbr 009 Preisangaben Und Dark Patterns, Vbr 010 Uwg Irrefuehrung Verbraucherbezug, Vbr 011 Schlichtung Und Vsbg Prüfen im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet wer... |
| `verbraucherrecht-digitale-energie` | Nutze dies, wenn Verbraucherrecht Digitale Produkte 327 Bgb, Verbraucherrecht Energie Smartmeter Waerme, Verbraucherrecht Finanzdienstleistung Online, Verbraucherrecht Plattform Marktplatz Haendler im Plugin Verbraucherschutzrecht Prüfer... |
| `verbraucherrecht-preisangaben-reise` | Nutze dies, wenn Verbraucherrecht Preisangaben Und Dark Patterns, Verbraucherrecht Reise Flug Pauschal, Verbraucherrecht Right To Repair, Verbraucherrecht Verbandsklage Musterfeststellung im Plugin Verbraucherschutzrecht Prüfer konkret b... |
| `verbraucherrecht-waren-widerruf` | Nutze dies, wenn Verbraucherrecht Waren Mit Digitalen Elementen, Verbraucherrecht Widerruf Fernabsatz im Plugin Verbraucherschutzrecht Prüfer konkret bearbeitet werden soll. Auslöser: Bitte Verbraucherrecht Waren Mit Digitalen Elementen,... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
