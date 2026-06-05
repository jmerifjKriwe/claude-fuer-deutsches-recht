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

Automatisch generierte Komplett-Liste aller 26 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | See- und Schifffahrtsrecht: Kaltstart, Aktenlandkarte, Rollenklärung, Fristen, Quellenprüfung, Spezialskill-Routing und erste Ausgabe. |
| `see-001-kaltstart-schifffahrtsmandat` | 'Erstkontakt mit Schifffahrtsmandat: Mandant meldet Schiffsunfall; Arrest oder neues Mandat. Sofort-Triage nach HGB §§ 476-480 (Reeder/Ausruester); SchRG §§ 8-74 (Hypothek); UNCLOS Art. 94 (Flaggenstaat); ISM-Code. Klaert Schiffstyp; Fla... |
| `see-auslandsflagge-local-insolvenz-reederei` | Nutze dies, wenn See 012 Auslandsflagge Und Local Counsel, See 014 Insolvenz Der Reederei, See 015 Versicherung P I Hull, See 016 Hafenrecht Und Liegegeld, See 017 Seearbeitsrecht Schnittstelle im Plugin Seerecht Schifffahrtsrecht konkre... |
| `see-bermuda-see-seeschiff-see-schiffsregister` | Nutze dies, wenn See 013 Bermuda Struktur Prüfen, See 002 Seeschiff Oder Binnenschiff, See 003 Schiffsregister Und Eigentum, See 004 Schiffshypothek Prüfen, See 006 Schiffsverkauf Closing im Plugin Seerecht Schifffahrtsrecht konkret bear... |
| `see-binnenschiff-arrest-wrackpflicht` | Nutze dies, wenn See 084 Binnenschiff Arrest Vorbereiten, See 085 Binnenschiff Wrackpflicht Prüfen, See 086 Binnenschiff Versicherung Melden, See 087 Binnenschiff Local Counsel Instruieren, See 088 Binnenschiff Closing Planen im Plugin S... |
| `see-binnenschiff-see-see-kreuzfahrtschiff-see` | Nutze dies, wenn See 089 Binnenschiff Klagepfad Waehlen, See 090 Binnenschiff Risiko Memo Schreiben, See 091 Kreuzfahrtschiff Register Prüfen, See 092 Kreuzfahrtschiff Hypothek Bestellen, See 094 Kreuzfahrtschiff Arrest Vorbereiten im Pl... |
| `see-charterparty-local-closing-planen` | Nutze dies, wenn See 117 Charterparty Local Counsel Instruieren, See 118 Charterparty Closing Planen, See 119 Charterparty Klagepfad Waehlen im Plugin Seerecht Schifffahrtsrecht konkret bearbeitet werden soll. Auslöser: Bitte See 117 Cha... |
| `see-charterparty-register-hypothek-bestellen` | Nutze dies, wenn See 111 Charterparty Register Prüfen, See 112 Charterparty Hypothek Bestellen, See 114 Charterparty Arrest Vorbereiten, See 115 Charterparty Wrackpflicht Prüfen, See 116 Charterparty Versicherung Melden im Plugin Seerech... |
| `see-charterparty-see-fracht-see-havarie-see` | Nutze dies, wenn See 007 Charterparty Einordnen, See 008 Fracht Und Konnossement, See 009 Havarie Und Kollision, See 010 Bergung Und Wrack, See 011 Pfaendung Und Arrest Schiff im Plugin Seerecht Schifffahrtsrecht konkret bearbeitet werde... |
| `see-containerschiff-local-closing-planen` | Nutze dies, wenn See 067 Containerschiff Local Counsel Instruie, See 068 Containerschiff Closing Planen, See 069 Containerschiff Klagepfad Waehlen, See 070 Containerschiff Risiko Memo Schreiben, See 071 Offshore Schiff Register Prüfen im... |
| `see-containerschiff-register-hypothek` | Nutze dies, wenn See 061 Containerschiff Register Prüfen, See 062 Containerschiff Hypothek Bestellen, See 064 Containerschiff Arrest Vorbereiten, See 065 Containerschiff Wrackpflicht Prüfen, See 066 Containerschiff Versicherung Melden im... |
| `see-konnossement-versicherung-local-counsel` | Nutze dies, wenn See 106 Konnossement Versicherung Melden, See 107 Konnossement Local Counsel Instruieren, See 108 Konnossement Closing Planen, See 109 Konnossement Klagepfad Waehlen, See 110 Konnossement Risiko Memo Schreiben im Plugin... |
| `see-kreuzfahrtschiff-see-konnossement-see-see` | Nutze dies, wenn See 100 Kreuzfahrtschiff Risiko Memo Schreiben, See 101 Konnossement Register Prüfen, See 102 Konnossement Hypothek Bestellen, See 104 Konnossement Arrest Vorbereiten, See 105 Konnossement Wrackpflicht Prüfen im Plugin S... |
| `see-kreuzfahrtschiff-wrackpflicht` | Nutze dies, wenn See 095 Kreuzfahrtschiff Wrackpflicht Prüfen, See 096 Kreuzfahrtschiff Versicherung Melden, See 097 Kreuzfahrtschiff Local Counsel Instrui, See 098 Kreuzfahrtschiff Closing Planen, See 099 Kreuzfahrtschiff Klagepfad Waeh... |
| `see-offshore-schiff-arrest-vorbereiten` | Nutze dies, wenn See 072 Offshore Schiff Hypothek Bestellen, See 074 Offshore Schiff Arrest Vorbereiten, See 075 Offshore Schiff Wrackpflicht Prüfen, See 076 Offshore Schiff Versicherung Melden, See 077 Offshore Schiff Local Counsel Inst... |
| `see-offshore-schiff-klagepfad-waehlen-risiko` | Nutze dies, wenn See 078 Offshore Schiff Closing Planen, See 079 Offshore Schiff Klagepfad Waehlen, See 080 Offshore Schiff Risiko Memo Schreiben, See 081 Binnenschiff Register Prüfen, See 082 Binnenschiff Hypothek Bestellen im Plugin Se... |
| `see-offshore-see-binnenschiff-see` | Nutze dies, wenn See 073 Offshore Schiff Kaufvertrag Scopen, See 083 Binnenschiff Kaufvertrag Scopen, See 093 Kreuzfahrtschiff Kaufvertrag Scopen, See 103 Konnossement Kaufvertrag Scopen, See 113 Charterparty Kaufvertrag Scopen im Plugin... |
| `see-schiffbauvertrag-werft-schiffshypothek` | Nutze dies, wenn See 005 Schiffbauvertrag Werft, See 023 Schiffshypothek Kaufvertrag Scopen, See 033 Schiffbauwerk Kaufvertrag Scopen, See 041 Werftvertrag Register Prüfen, See 042 Werftvertrag Hypothek Bestellen im Plugin Seerecht Schif... |
| `see-schiffbauwerk-risiko-yachtkauf-register` | Nutze dies, wenn See 040 Schiffbauwerk Risiko Memo Schreiben, See 051 Yachtkauf Register Prüfen, See 052 Yachtkauf Hypothek Bestellen, See 054 Yachtkauf Arrest Vorbereiten, See 055 Yachtkauf Wrackpflicht Prüfen im Plugin Seerecht Schifff... |
| `see-schiffbauwerk-wrackpflicht-versicherung` | Nutze dies, wenn See 035 Schiffbauwerk Wrackpflicht Prüfen, See 036 Schiffbauwerk Versicherung Melden, See 037 Schiffbauwerk Local Counsel Instruiere, See 038 Schiffbauwerk Closing Planen, See 039 Schiffbauwerk Klagepfad Waehlen im Plugi... |
| `see-schiffshypothek-arrest-wrackpflicht` | Nutze dies, wenn See 024 Schiffshypothek Arrest Vorbereiten, See 025 Schiffshypothek Wrackpflicht Prüfen, See 026 Schiffshypothek Versicherung Melden, See 027 Schiffshypothek Local Counsel Instruie, See 028 Schiffshypothek Closing Planen... |
| `see-schiffshypothek-klagepfad-risiko` | Nutze dies, wenn See 029 Schiffshypothek Klagepfad Waehlen, See 030 Schiffshypothek Risiko Memo Schreiben, See 031 Schiffbauwerk Register Prüfen, See 032 Schiffbauwerk Hypothek Bestellen, See 034 Schiffbauwerk Arrest Vorbereiten im Plugi... |
| `see-umwelt-marpol-itlos-hamburg-dokumenten` | Nutze dies, wenn See 018 Umwelt Und Marpol, See 019 Itlos Hamburg Und Unclos, See 020 Dokumenten Cockpit Schiff, See 021 Schiffshypothek Register Prüfen, See 022 Schiffshypothek Hypothek Bestellen im Plugin Seerecht Schifffahrtsrecht kon... |
| `see-werftvertrag-closing-klagepfad-waehlen` | Nutze dies, wenn See 048 Werftvertrag Closing Planen, See 049 Werftvertrag Klagepfad Waehlen, See 050 Werftvertrag Risiko Memo Schreiben, See 053 Yachtkauf Kaufvertrag Scopen, See 063 Containerschiff Kaufvertrag Scopen im Plugin Seerecht... |
| `see-werftvertrag-kaufvertrag-arrest` | Nutze dies, wenn See 043 Werftvertrag Kaufvertrag Scopen, See 044 Werftvertrag Arrest Vorbereiten, See 045 Werftvertrag Wrackpflicht Prüfen, See 046 Werftvertrag Versicherung Melden, See 047 Werftvertrag Local Counsel Instruieren im Plug... |
| `see-yachtkauf-versicherung-local-counsel` | Nutze dies, wenn See 056 Yachtkauf Versicherung Melden, See 057 Yachtkauf Local Counsel Instruieren, See 058 Yachtkauf Closing Planen, See 059 Yachtkauf Klagepfad Waehlen, See 060 Yachtkauf Risiko Memo Schreiben im Plugin Seerecht Schiff... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
