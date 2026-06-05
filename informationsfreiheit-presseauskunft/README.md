# Informationsfreiheit und Presseauskunft

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`informationsfreiheit-presseauskunft`) | [`informationsfreiheit-presseauskunft.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/informationsfreiheit-presseauskunft.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **IFG-/Presseauskunftsakte Hafenstadt** (`informationsfreiheit-presseauskunft-klinikdaten-hafenstadt`) | [Gesamt-PDF lesen](../testakten/informationsfreiheit-presseauskunft-klinikdaten-hafenstadt/gesamt-pdf/informationsfreiheit-presseauskunft-klinikdaten-hafenstadt_gesamt.pdf) | [`testakte-informationsfreiheit-presseauskunft-klinikdaten-hafenstadt.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-informationsfreiheit-presseauskunft-klinikdaten-hafenstadt.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin ist das Cockpit für Menschen, Journalistinnen, Kanzleien, NGOs und Unternehmen, die amtliche Informationen bekommen wollen, ohne an Zuständigkeitsnebel, Gebührenbescheiden oder Ausweichantworten hängen zu bleiben.

## Start

Beginne mit `informationsfreiheit-presseauskunft-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| `ifg-001-informationsbegehren-sortier` | Informationsfreiheit und Presseauskunft: Kaltstart Informationsbegehren sortieren. Kaltstart Informationsbegehren sortieren im Fachgebiet Informationsfreiheit und Presseauskunft als geführten Arbeitsgang mit Fragen, Dokumentenlogik und A... |
| `ifg-ablehnungsbescheid-angriffspunkte` | Ifg 013 Ablehnungsbescheid In Angriffspunkte Z, Ifg 014 Widerspruch Gegen Ifg Ablehnung, Ifg 015 Verpflichtungsklage Und Eilrechtsschut, Ifg 016 Gebuehrenbescheid Angreifen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Bele... |
| `ifg-archivrecht-zustaendigkeit-pruefen-frist-setzen` | Archivrecht Zustaendigkeit Pruefen / Archivrecht Frist Setzen / Presseauskunft Richtig Routen / Bundesbehoerde Landesbehoerde Erk: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren... |
| `ifg-bund-antrag-formulieren-kosten-deckeln-schwaerzung-angreifen` | Bund Antrag Formulieren / Bund Kosten Deckeln / Bund Schwaerzung Angreifen / Bund Drittanhoerung Begleiten: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `ifg-bund-widerspruch-bauen-klage-vorbereiten-presseantwort` | Bund Widerspruch Bauen / Bund Klage Vorbereiten / Bund Presseantwort Nachfassen / Bund Tracking Aktualisieren: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `ifg-fristenkalender-untaetigkeitstrack-bund-zustaendigkeit` | Fristenkalender Untaetigkeitstrack / Bund Zustaendigkeit Pruefen / Bund Frist Setzen / Ifggebv Gebuehren Zustaendigkeit Pruef: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `ifg-ifggebv-gebuehren-frist-umweltinformation-zustaendigkeit-p` | Ifggebv Gebuehren Frist Setzen / Umweltinformation Zustaendigkeit P / Umweltinformation Frist Setzen / Lebensmittel Produkte Frist SE: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastba... |
| `ifg-ifggebv-gebuehren-klage-vorbereiten` | Ifg 053 Ifggebv Gebuehren Widerspruch Bauen, Ifg 054 Ifggebv Gebuehren Klage Vorbereiten, Ifg 055 Ifggebv Gebuehren Presseantwort Nachfa, Ifg 056 Ifggebv Gebuehren Tracking Aktualisier: wählt den konkreten Prüfpfad, trennt Frist, Zuständ... |
| `ifg-ifggebv-gebuehren-kosten-deckeln` | Ifg 047 Ifggebv Gebuehren Antrag Formulieren, Ifg 050 Ifggebv Gebuehren Kosten Deckeln, Ifg 051 Ifggebv Gebuehren Schwaerzung Angreife, Ifg 052 Ifggebv Gebuehren Drittanhoerung Begle: wählt den konkreten Prüfpfad, trennt Frist, Zuständig... |
| `ifg-informationszugang-baden-wuerttemberg-bayern-livecheck` | Informationszugang Baden Wuerttemberg / Informationszugang Bayern Livecheck / Informationszugang Berlin Livecheck / Informationszugang Brandenburg Liveche: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt... |
| `ifg-informationszugang-beliehenen-parlaments` | Ifg 017 Informationszugang Bei Beliehenen Priv, Ifg 018 Parlaments Und Rechnungshofgrenzen, Ifg 019 Sicherheitsinteressen Und Geheimschutz, Ifg 020 Veroeffentlichung Erhaltene Dokumente: wählt den konkreten Prüfpfad, trennt Frist, Zustän... |
| `ifg-informationszugang-bremen-livecheck-hamburg-hessen` | Informationszugang Bremen Livecheck / Informationszugang Hamburg Livecheck / Informationszugang Hessen Livecheck / Informationszugang Mecklenburg Vorpomm: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt d... |
| `ifg-informationszugang-niedersachsen-livec-nordrhein-westfalen` | Informationszugang Niedersachsen Livec / Informationszugang Nordrhein Westfalen / Informationszugang Rheinland Pfalz Liv / Informationszugang Saarland Livecheck: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und er... |
| `ifg-informationszugang-sachsen-livecheck-anhalt-schleswig` | Informationszugang Sachsen Livecheck / Informationszugang Sachsen Anhalt Live / Informationszugang Schleswig Holstein / Informationszugang Thueringen Livechec: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erze... |
| `ifg-kein-land-ersatzwege-kostenrisiko-gebuehrenankuendigung` | Kein Land Ersatzwege Finden / Kostenrisiko Gebuehrenankuendigung / Drittbeteiligung Bei Betriebsgeheimnis / Personenbezogene Daten Schwaerzung: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten... |
| `ifg-landespressegesetz-drittanhoerung-begl-widerspruch-bauen` | Landespressegesetz Drittanhoerung Begl / Landespressegesetz Widerspruch Bauen / Landespressegesetz Klage Vorbereiten / Landespressegesetz Presseantwort Nachf: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeu... |
| `ifg-landespressegesetz-transparenzgesetz` | Ifg 086 Landespressegesetz Tracking Aktualisie, Ifg 087 Transparenzgesetz Antrag Formulieren, Ifg 090 Transparenzgesetz Kosten Deckeln, Ifg 091 Transparenzgesetz Schwaerzung Angreife: wählt den konkreten Prüfpfad, trennt Frist, Zuständig... |
| `ifg-landespressegesetz-zustaendigkeit-prue-frist-setzen` | Landespressegesetz Zustaendigkeit Prue / Landespressegesetz Frist Setzen / Transparenzgesetz Zustaendigkeit Pruef / Transparenzgesetz Frist Setzen: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den näch... |
| `ifg-lebensmittel-produkte-antrag-zustaend-kosten-schwaerz` | Lebensmittel Produkte Antrag F / Lebensmittel Produkte Zustaend / Lebensmittel Produkte Kosten D / Lebensmittel Produkte Schwaerz: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren... |
| `ifg-lebensmittel-produkte-drittanh-widerspr-klage-pressean` | Lebensmittel Produkte Drittanh / Lebensmittel Produkte Widerspr / Lebensmittel Produkte Klage / Lebensmittel Produkte Pressean: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Out... |
| `ifg-lebensmittel-produkte-tracking-landespressegesetz-antrag` | Lebensmittel Produkte Tracking / Landespressegesetz Antrag Formulieren / Landespressegesetz Kosten Deckeln / Landespressegesetz Schwaerzung Angreif: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den näc... |
| `ifg-transparenzgesetz-archivrecht` | Ifg 096 Transparenzgesetz Tracking Aktualisier, Ifg 097 Archivrecht Antrag Formulieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output. |
| `ifg-transparenzgesetz-drittanhoerung-begle-widerspruch-bauen` | Transparenzgesetz Drittanhoerung Begle / Transparenzgesetz Widerspruch Bauen / Transparenzgesetz Klage Vorbereiten / Transparenzgesetz Presseantwort Nachfa: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt... |
| `ifg-umweltinformation-antrag-formulier-kosten-deckeln` | Umweltinformation Antrag Formulier / Umweltinformation Kosten Deckeln / Umweltinformation Schwaerzung Angr / Umweltinformation Drittanhoerung B: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächste... |
| `ifg-umweltinformation-widerspruch-baue-klage-vorbereite` | Umweltinformation Widerspruch Baue / Umweltinformation Klage Vorbereite / Umweltinformation Presseantwort Na / Umweltinformation Tracking Aktuali: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächs... |
| `ifg-umweltinformationen-abgrenzen-verbraucherinformationen-nutze` | Umweltinformationen Abgrenzen / Verbraucherinformationen Nutze / Akteneinsicht Auskunft Kopie / Presseanfrage Schnell Knapp Formul: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren... |
| `informationsfreiheit-presseauskunft-kaltstart-triage` | Informationsfreiheit und Presseauskunft: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
