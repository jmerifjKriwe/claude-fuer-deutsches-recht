# See- und Schifffahrtsrecht

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`seerecht-schifffahrtsrecht`) | [`seerecht-schifffahrtsrecht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/seerecht-schifffahrtsrecht.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Schifffahrtsakte** (`seerecht-schiffshypothek-werft-wrack-bermuda`) | [Gesamt-PDF lesen](../testakten/seerecht-schiffshypothek-werft-wrack-bermuda/gesamt-pdf/seerecht-schiffshypothek-werft-wrack-bermuda_gesamt.pdf) | [`testakte-seerecht-schiffshypothek-werft-wrack-bermuda.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-seerecht-schiffshypothek-werft-wrack-bermuda.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Dieses Plugin verbindet deutsches Seehandels- und Registerrecht mit internationaler Schifffahrtspraxis: Schiffbau, Verkauf, Finanzierung, Schiffshypothek, Arrest, Wrack/Bergung, Charter, Kollision, Insolvenz und ITLOS/UNCLOS.

## Start

Beginne mit `seerecht-schifffahrtsrecht-allgemein`. Das Plugin fragt zuerst nach Rolle, Ziel, Frist, Behörde/Gericht/Register, vorhandenen Unterlagen und gewünschtem Output. Danach schlägt es die passenden Spezialskills aus diesem Plugin vor.

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
| `see-001-kaltstart-schifffahrtsmandat` | 'Erstkontakt mit Schifffahrtsmandat: Mandant meldet Schiffsunfall; Arrest oder neues Mandat. Sofort-Triage nach HGB §§ 476-480 (Reeder/Ausruester); SchRG §§ 8-74 (Hypothek); UNCLOS Art. 94 (Flaggenstaat); ISM-Code. Klaert Schiffstyp; Fla... |
| `see-auslandsflagge-local-insolvenz-reederei` | See 012 Auslandsflagge Und Local Counsel, See 014 Insolvenz Der Reederei, See 015 Versicherung P I Hull, See 016 Hafenrecht Und Liegegeld: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert... |
| `see-binnenschiff-arrest-wrackpflicht` | See 084 Binnenschiff Arrest Vorbereiten, See 085 Binnenschiff Wrackpflicht Prüfen, See 086 Binnenschiff Versicherung Melden, See 087 Binnenschiff Local Counsel Instruieren: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Beleg... |
| `see-charterparty-local-closing-planen` | See 117 Charterparty Local Counsel Instruieren, See 118 Charterparty Closing Planen, See 119 Charterparty Klagepfad Waehlen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten b... |
| `see-charterparty-register-hypothek-bestellen` | See 111 Charterparty Register Prüfen, See 112 Charterparty Hypothek Bestellen, See 114 Charterparty Arrest Vorbereiten, See 115 Charterparty Wrackpflicht Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Recht... |
| `see-containerschiff-local-closing-planen` | See 067 Containerschiff Local Counsel Instruie, See 068 Containerschiff Closing Planen, See 069 Containerschiff Klagepfad Waehlen, See 070 Containerschiff Risiko Memo Schreiben: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `see-containerschiff-register-hypothek` | See 061 Containerschiff Register Prüfen, See 062 Containerschiff Hypothek Bestellen, See 064 Containerschiff Arrest Vorbereiten, See 065 Containerschiff Wrackpflicht Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Bele... |
| `see-konnossement-versicherung-local-counsel` | See 106 Konnossement Versicherung Melden, See 107 Konnossement Local Counsel Instruieren, See 108 Konnossement Closing Planen, See 109 Konnossement Klagepfad Waehlen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `see-kreuzfahrtschiff-wrackpflicht` | See 095 Kreuzfahrtschiff Wrackpflicht Prüfen, See 096 Kreuzfahrtschiff Versicherung Melden, See 097 Kreuzfahrtschiff Local Counsel Instrui, See 098 Kreuzfahrtschiff Closing Planen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkei... |
| `see-offshore-schiff-arrest-vorbereiten` | See 072 Offshore Schiff Hypothek Bestellen, See 074 Offshore Schiff Arrest Vorbereiten, See 075 Offshore Schiff Wrackpflicht Prüfen, See 076 Offshore Schiff Versicherung Melden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit,... |
| `see-offshore-schiff-klagepfad-waehlen-risiko` | See 078 Offshore Schiff Closing Planen, See 079 Offshore Schiff Klagepfad Waehlen, See 080 Offshore Schiff Risiko Memo Schreiben, See 081 Binnenschiff Register Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und... |
| `see-schiffbauvertrag-werft-schiffshypothek` | See 005 Schiffbauvertrag Werft, See 023 Schiffshypothek Kaufvertrag Scopen, See 033 Schiffbauwerk Kaufvertrag Scopen, See 041 Werftvertrag Register Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrund... |
| `see-schiffbauwerk-risiko-yachtkauf-register` | See 040 Schiffbauwerk Risiko Memo Schreiben, See 051 Yachtkauf Register Prüfen, See 052 Yachtkauf Hypothek Bestellen, See 054 Yachtkauf Arrest Vorbereiten: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrund... |
| `see-schiffbauwerk-wrackpflicht-versicherung` | See 035 Schiffbauwerk Wrackpflicht Prüfen, See 036 Schiffbauwerk Versicherung Melden, See 037 Schiffbauwerk Local Counsel Instruiere, See 038 Schiffbauwerk Closing Planen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `see-schiffshypothek-arrest-wrackpflicht` | See 024 Schiffshypothek Arrest Vorbereiten, See 025 Schiffshypothek Wrackpflicht Prüfen, See 026 Schiffshypothek Versicherung Melden, See 027 Schiffshypothek Local Counsel Instruie: wählt den konkreten Prüfpfad, trennt Frist, Zuständigke... |
| `see-schiffshypothek-klagepfad-risiko` | See 029 Schiffshypothek Klagepfad Waehlen, See 030 Schiffshypothek Risiko Memo Schreiben, See 031 Schiffbauwerk Register Prüfen, See 032 Schiffbauwerk Hypothek Bestellen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege... |
| `see-umwelt-marpol-itlos-hamburg-dokumenten` | See 018 Umwelt Und Marpol, See 019 Itlos Hamburg Und Unclos, See 020 Dokumenten Cockpit Schiff, See 021 Schiffshypothek Register Prüfen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert de... |
| `see-werftvertrag-closing-klagepfad-waehlen` | See 048 Werftvertrag Closing Planen, See 049 Werftvertrag Klagepfad Waehlen, See 050 Werftvertrag Risiko Memo Schreiben, See 053 Yachtkauf Kaufvertrag Scopen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgr... |
| `see-werftvertrag-kaufvertrag-arrest` | See 043 Werftvertrag Kaufvertrag Scopen, See 044 Werftvertrag Arrest Vorbereiten, See 045 Werftvertrag Wrackpflicht Prüfen, See 046 Werftvertrag Versicherung Melden: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und R... |
| `see-yachtkauf-versicherung-local-counsel` | See 056 Yachtkauf Versicherung Melden, See 057 Yachtkauf Local Counsel Instruieren, See 058 Yachtkauf Closing Planen, See 059 Yachtkauf Klagepfad Waehlen: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundl... |
| `seerecht-schifffahrtsrecht-kaltstart-triage` | See- und Schifffahrtsrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Fachmodul-Routing und erste Ausgabe. |
| `seerecht-schifffahrtsrecht-see-bermuda-struktur-seeschiff` | See Bermuda Struktur Pruefen / See Seeschiff Binnenschiff / See Schiffsregister Eigentum / See Schiffshypothek Pruefen / 1 ergänzende Prüffelder: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächst... |
| `seerecht-schifffahrtsrecht-see-binnenschiff-klagepfad-risiko` | See Binnenschiff Klagepfad Waehlen / See Binnenschiff Risiko Memo Schreiben / See Kreuzfahrtschiff Register Pruefen / See Kreuzfahrtschiff Hypothek Bestellen / 1 ergänzende Prüffelder: bearbeitet die maßgeblichen Prüffelder, setzt den pa... |
| `seerecht-schifffahrtsrecht-see-charterparty-einordnen-fracht` | See Charterparty Einordnen / See Fracht Konnossement / See Havarie Kollision / See Bergung Wrack / 1 ergänzende Prüffelder: bearbeitet die maßgeblichen Prüffelder, setzt den passenden Prüfpfad und erzeugt den nächsten belastbaren Output. |
| `seerecht-schifffahrtsrecht-see-kreuzfahrtschiff-risiko` | See Kreuzfahrtschiff Risiko Memo Schreiben / See Konnossement Register Pruefen / See Konnossement Hypothek Bestellen / See Konnossement Arrest Vorbereiten / 1 ergänzende Prüffelder: bearbeitet die maßgeblichen Prüffelder, setzt den passe... |
| `seerecht-schifffahrtsrecht-see-offshore-schiff-binnenschiff` | See Offshore Schiff Kaufvertrag Scopen / See Binnenschiff Kaufvertrag Scopen / See Kreuzfahrtschiff Kaufvertrag Scopen / See Konnossement Kaufvertrag Scopen / 1 ergänzende Prüffelder: bearbeitet die maßgeblichen Prüffelder, setzt den pas... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
