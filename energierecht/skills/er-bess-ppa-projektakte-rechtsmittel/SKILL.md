---
name: er-bess-ppa-projektakte-rechtsmittel
description: "ER Bess PPA Projektakte Rechtsmittel im Plugin Energierecht: prüft konkret Prüft Erlösverträge für Speicher, Prüft die gesamte Speicherakte auf Lücken, Widersprüche, fehlende Quellen. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# ER Bess PPA Projektakte Rechtsmittel

## Arbeitsbereich

**ER Bess PPA Projektakte Rechtsmittel** ordnet den Fall über die tragenden Prüffelder: Prüft Erlösverträge für Speicher, Prüft die gesamte Speicherakte auf Lücken, Widersprüche. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `er-bess-ppa-und-merchant-risk` | Prüft Erlösverträge für Speicher: Tolling, Capacity, Arbitrage, Regelenergie, Floor/Cap und Verfügbarkeitsgarantien. |
| `er-bess-projektakte-qualitygate` | Prüft die gesamte Speicherakte auf Lücken, Widersprüche, fehlende Quellen, falsche Rollen und unrealistische Annahmen. |
| `er-bess-rechtsmittel-und-nachbarabwehr` | Prüft Widerspruch/Klage, Nachbarrechte, Sofortvollzug, Baustopp, Umweltverbandsklage und Verteidigung. |
| `er-bess-regelenergie-systemdienstleistung` | Prüft Präqualifikation, Vermarktung, Verfügbarkeit, Messdaten, Sanktionen und Aggregator-Struktur. |

## Arbeitsweg

- Rolle und Ziel im Energierecht klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: KWKG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `er-bess-ppa-und-merchant-risk`

**Fokus:** Prüft Erlösverträge für Speicher: Tolling, Capacity, Arbitrage, Regelenergie, Floor/Cap und Verfügbarkeitsgarantien.

# PPA, Tolling und Merchant-Risk

## Wofür dieser Arbeitsgang da ist

Der Skill macht Vertragsmodell und Regulierungsstatus gemeinsam sichtbar.

## Rechts- und Praxisanker

BGB, EnWG, REMIT/MAR-Schnittstelle, Bilanzkreis, Garantien, Haftung.

## Workflow

1. Projektrolle und gewünschtes Ergebnis festlegen: Betreiber, Investor, Kommune, Netzbetreiber, Nachbar, Bank oder Behörde.
2. Standort, Technik, Netzebene, Leistung, Kapazität, Betriebsmodell und Dokumentenstand erfassen.
3. Genehmigungs-, Netz-, Sicherheits-, Markt- und Vertragsfragen in getrennte Spuren legen.
4. Rote Punkte mit Belegen, zuständiger Stelle, Frist und konkretem nächsten Dokument ausgeben.

## Output

- Risikomatrix
- Unterlagen- und Behördenliste
- Mandantenmemo oder Board-Paper-Baustein

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 2. `er-bess-projektakte-qualitygate`

**Fokus:** Prüft die gesamte Speicherakte auf Lücken, Widersprüche, fehlende Quellen, falsche Rollen und unrealistische Annahmen.

# BESS-Projektakte und Qualitygate

## Wofür dieser Arbeitsgang da ist

Der Skill ist der finale Kamm vor Board Paper, Bank-DD, Behördeneinreichung oder Mandantenmemo.

## Rechts- und Praxisanker

Quellenhygiene, Dokumentenmatrix, Fristen, Zuständigkeit, technische Annahmen, keine Normfiktion.

## Workflow

1. Projektrolle und gewünschtes Ergebnis festlegen: Betreiber, Investor, Kommune, Netzbetreiber, Nachbar, Bank oder Behörde.
2. Standort, Technik, Netzebene, Leistung, Kapazität, Betriebsmodell und Dokumentenstand erfassen.
3. Genehmigungs-, Netz-, Sicherheits-, Markt- und Vertragsfragen in getrennte Spuren legen.
4. Rote Punkte mit Belegen, zuständiger Stelle, Frist und konkretem nächsten Dokument ausgeben.

## Output

- Risikomatrix
- Unterlagen- und Behördenliste
- Mandantenmemo oder Board-Paper-Baustein

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 3. `er-bess-rechtsmittel-und-nachbarabwehr`

**Fokus:** Prüft Widerspruch/Klage, Nachbarrechte, Sofortvollzug, Baustopp, Umweltverbandsklage und Verteidigung.

# Rechtsmittel, Nachbarabwehr und Eilrechtsschutz

## Wofür dieser Arbeitsgang da ist

Der Skill erzeugt Prozessrisiko und Eilstrategie.

## Rechts- und Praxisanker

VwGO, BauGB/Bauordnungsrecht, BImSchG, UmwRG, Nachbarschutz.

## Workflow

1. Projektrolle und gewünschtes Ergebnis festlegen: Betreiber, Investor, Kommune, Netzbetreiber, Nachbar, Bank oder Behörde.
2. Standort, Technik, Netzebene, Leistung, Kapazität, Betriebsmodell und Dokumentenstand erfassen.
3. Genehmigungs-, Netz-, Sicherheits-, Markt- und Vertragsfragen in getrennte Spuren legen.
4. Rote Punkte mit Belegen, zuständiger Stelle, Frist und konkretem nächsten Dokument ausgeben.

## Output

- Risikomatrix
- Unterlagen- und Behördenliste
- Mandantenmemo oder Board-Paper-Baustein

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.

## 4. `er-bess-regelenergie-systemdienstleistung`

**Fokus:** Prüft Präqualifikation, Vermarktung, Verfügbarkeit, Messdaten, Sanktionen und Aggregator-Struktur.

# Regelenergie und Systemdienstleistungen

## Wofür dieser Arbeitsgang da ist

Fokus auf Speicher als Flexibilitätsanbieter statt bloßer Netzanschlussfall.

## Rechts- und Praxisanker

EnWG, Übertragungsnetzbetreiber-Regeln, Präqualifikationsunterlagen live prüfen.

## Workflow

1. Projektrolle und gewünschtes Ergebnis festlegen: Betreiber, Investor, Kommune, Netzbetreiber, Nachbar, Bank oder Behörde.
2. Standort, Technik, Netzebene, Leistung, Kapazität, Betriebsmodell und Dokumentenstand erfassen.
3. Genehmigungs-, Netz-, Sicherheits-, Markt- und Vertragsfragen in getrennte Spuren legen.
4. Rote Punkte mit Belegen, zuständiger Stelle, Frist und konkretem nächsten Dokument ausgeben.

## Output

- Risikomatrix
- Unterlagen- und Behördenliste
- Mandantenmemo oder Board-Paper-Baustein

## Qualitätsgate

- Keine Blindzitate: Rechtsprechung, Behördenpraxis und Schwellenwerte vor tragender Aussage live anhand amtlicher oder frei zugänglicher Quellen prüfen.
- Keine LMA-, Banken- oder Fondsformularsprache nacherzählen: Nutzer soll das aktuelle Dokument hochladen; der Skill arbeitet dann am konkreten Text.
- Jede Annahme sichtbar markieren, insbesondere Zahlen, Fristen, regulatorische Rollen, Genehmigungsstand und Parteiperspektive.
