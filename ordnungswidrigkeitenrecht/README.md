# Ordnungswidrigkeitenrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`ordnungswidrigkeitenrecht`) | [`ordnungswidrigkeitenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ordnungswidrigkeitenrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **OWiG-Akte** (`ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier`) | [Gesamt-PDF lesen](../testakten/ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier/gesamt-pdf/ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier_gesamt.pdf) | [`testakte-ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ordnungswidrigkeitenrecht-bussgeldmix-gewerbe-datenschutz-tier.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist das allgemeine Betriebssystem für Bußgeldsachen, nicht nur Verkehr: OWiG-Verfahren, Fachordnungswidrigkeiten, Anhörung, Bußgeldbescheid, Einspruch, Akteneinsicht, Amtsgericht und Rechtsbeschwerde.

## Start

Beginne mit `ordnungswidrigkeitenrecht-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `ordnungswidrigkeitenrecht-kaltstart-triage` | Ordnungswidrigkeitenrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `ordnungswidrigkeitenrecht-owi-akteneinsicht-beantragen` | OWI Akteneinsicht Beantragen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ordnungswidrigkeitenrecht-owi-aussenwirtschaft-gerichtstermin` | OWI Aussenwirtschaft Gerichtstermin: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ordnungswidrigkeitenrecht-owi-baurecht-frist-strassenverkehr` | OWI Baurecht Frist Strassenverkehr: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ordnungswidrigkeitenrecht-owi-baurecht-mandantenbrief` | OWI Baurecht Mandantenbrief: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ordnungswidrigkeitenrecht-owi-datenschutzbussgeld-beweis` | OWI Datenschutzbussgeld Beweis: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ordnungswidrigkeitenrecht-owi-datenschutzbussgeld-tatbestand` | OWI Datenschutzbussgeld Tatbestand: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ordnungswidrigkeitenrecht-owi-einspruch-fristgerecht` | OWI Einspruch Fristgerecht: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ordnungswidrigkeitenrecht-owi-lebensmittelrecht-einspruch` | OWI Lebensmittelrecht Einspruch: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ordnungswidrigkeitenrecht-owi-lebensmittelrecht-gerichtstermin` | OWI Lebensmittelrecht Gerichtstermin: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `ordnungswidrigkeitenrecht-owi-umwelt-rechtsbeschwerde` | OWI Umwelt Rechtsbeschwerde: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-001-kaltstart-bussgeldverfahren` | Ordnungswidrigkeitenrecht: Kaltstart Bußgeldverfahren. Kaltstart Bußgeldverfahren im Fachgebiet Ordnungswidrigkeitenrecht als geführten Arbeitsgang mit Fragen, Dokumentenlogik und Ausgabeformat bearbeiten. |
| `owi-amtsgericht-hauptverhandlung` | OWI Amtsgericht Hauptverhandlung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-aussenwirtschaft-einspruch-einstellung` | OWI Aussenwirtschaft Einspruch Einstellung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-baurecht-ruegen-verjaehrung-berechnen` | OWI Baurecht Ruegen Verjaehrung Berechnen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-baurecht-zerlegen-akteneinsicht-schreiben` | OWI Baurecht Zerlegen Akteneinsicht Schreiben: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-datenschutzbussgeld-mandantenbrief-abgabe` | OWI Datenschutzbussgeld Mandantenbrief Abgabe: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-gewerberecht-frist-umwelt` | OWI Gewerberecht Frist Umwelt: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-gewerberecht-mandantenbrief-umwelt` | OWI Gewerberecht Mandantenbrief Umwelt: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-gewerberecht-ruegen-verjaehrung-berechnen` | OWI Gewerberecht Ruegen Verjaehrung Berechnen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-gewerberecht-zerlegen-akteneinsicht` | OWI Gewerberecht Zerlegen Akteneinsicht: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-strassenverkehr-einstellung-ruegen` | OWI Strassenverkehr Einstellung Ruegen: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-strassenverkehr-rechtsbeschwerde` | OWI Strassenverkehr Rechtsbeschwerde: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-tierschutz-akteneinsicht-einspruch` | OWI Tierschutz Akteneinsicht Einspruch: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-tierschutz-verjaehrung-gerichtstermin` | OWI Tierschutz Verjaehrung Gerichtstermin: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-umwelt-einstellung-ruegen-verjaehrung` | OWI Umwelt Einstellung Ruegen Verjaehrung: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `owi-unternehmen-verbandsgeldbusse` | OWI Unternehmen Verbandsgeldbusse: bündelt 4 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
