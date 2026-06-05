# Luftrecht und Flughafenrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`luftrecht-flughafenrecht`) | [`luftrecht-flughafenrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/luftrecht-flughafenrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Luftrechtsakte** (`luftrecht-airline-insolvenz-flugzeugpfand-flughafen`) | [Gesamt-PDF lesen](../testakten/luftrecht-airline-insolvenz-flugzeugpfand-flughafen/gesamt-pdf/luftrecht-airline-insolvenz-flugzeugpfand-flughafen_gesamt.pdf) | [`testakte-luftrecht-airline-insolvenz-flugzeugpfand-flughafen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-luftrecht-airline-insolvenz-flugzeugpfand-flughafen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin deckt ziviles und öffentliches Luftrecht ab: Luftfahrzeug, Flughafen, Betriebsgenehmigung, LBA, Luftsicherheit, Slots, Flugzeugfinanzierung, Registerpfandrechte, Pfändung, Airline-Krise und internationale Bezüge.

## Start

Beginne mit `luftrecht-flughafenrecht-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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

Automatisch generierte Komplett-Liste aller 26 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `luft-001-kaltstart-luftrechtsmandat` | 'Mandant erscheint erstmals mit Luftrechtsfall: Airline-Insolvenz Flugzeugbeschlagnahme Slot-Verlust oder Planfeststellungsklage. Klaert Zustaendigkeit LBA vs. Landesbehoerde vs. Gericht sichert Fristen LuftVG §§ 20 ff. und EU-Recht und... |
| `luft-acc3-genehmigung-sicherheitsauflage` | Luft Acc3 Genehmigung Sicherheitsauflage: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-acc3-mandantenmemo-slot-register` | Luft Acc3 Mandantenmemo Slot Register: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-aircraft-arrest-airline-finanzielle` | Luft Aircraft Arrest Airline Finanzielle: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-airline-local-dashboard-bauen` | Luft Airline Local Dashboard Bauen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-airline-pfandrecht-pfaendung-planen` | Luft Airline Pfandrecht Pfaendung Planen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-bodenabfertigung-insolvenzrisiko-local` | Luft Bodenabfertigung Insolvenzrisiko Local: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-bodenabfertigung-pruefe-luftvg` | Luft Bodenabfertigung Pruefe Luftvg: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-bodenabfertigung-register-pfandrecht` | Luft Bodenabfertigung Register Pfandrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-drohne-local-dashboard-bauen` | Luft Drohne Local Dashboard Bauen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-drohne-pfandrecht-pfaendung-planen` | Luft Drohne Pfandrecht Pfaendung Planen: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-ersatzteillager-drohne-luftfracht-acc3` | Luft Ersatzteillager Drohne Luftfracht Acc3: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-ersatzteillager-insolvenzrisiko-local` | Luft Ersatzteillager Insolvenzrisiko Local: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-ersatzteillager-register-pfandrecht` | Luft Ersatzteillager Register Pfandrecht: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-flughafen-dashboard-mandantenmemo` | Luft Flughafen Dashboard Mandantenmemo: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-flughafen-pfaendung-genehmigung` | Luft Flughafen Pfaendung Genehmigung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-fluglaerm-anwohner-insolvenz` | Luft Fluglaerm Anwohner Insolvenz: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-flugzeugleasing-genehmigung` | Luft Flugzeugleasing Genehmigung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-flugzeugleasing-mandantenmemo` | Luft Flugzeugleasing Mandantenmemo: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-lba-airline-flughafen-flugzeugleasing` | Luft LBA Airline Flughafen Flugzeugleasing: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-luftfracht-dashboard-mandantenmemo` | Luft Luftfracht Dashboard Mandantenmemo: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-luftfracht-pfaendung-genehmigung` | Luft Luftfracht Pfaendung Genehmigung: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-luftsicherheit-luftsig` | Luft Luftsicherheit Luftsig: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-registerpfandrecht-sicherheitsauflage` | Luft Registerpfandrecht Sicherheitsauflage: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luft-slot-sicherheitsauflage-insolvenzrisiko` | Luft Slot Sicherheitsauflage Insolvenzrisiko: bündelt 5 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `luftrecht-flughafenrecht-kaltstart-triage` | Luftrecht und Flughafenrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
