---
name: er-bess-ppa-projektakte-rechtsmittel
description: "Nutze dies, wenn Er Bess Ppa Und Merchant Risk, Er Bess Projektakte Qualitygate, Er Bess Rechtsmittel Und Nachbarabwehr, Er Bess Regelenergie Systemdienstleistung im Plugin Energierecht konkret bearbeitet werden soll. Auslöser: Bitte Er Bess Ppa Und Merchant Risk, Er Bess Projektakte Qualitygate, Er Bess Rechtsmittel Und Nachbarabwehr, Er Bess Regelenergie Systemdienstleistung prüfen.; Erstelle eine Arbeitsfassung zu Er Bess Ppa Und Merchant Risk, Er Bess Projektakte Qualitygate, Er Bess Rechtsmittel Und Nachbarabwehr, Er Bess Regelenergie Systemdienstleistung.; Welche Normen und Nachweise brauche ich?."
---

# Er Bess Ppa Und Merchant Risk, Er Bess Projektakte Qualitygate, Er Bess Rechtsmittel Und Nachbarabwehr, Er Bess Regelenergie Systemdienstleistung

## Zweck

Dieser Skill ist ein eigenständiger Arbeitsbereich. Er verbindet mehrere sachlich benachbarte Arbeitsmodule. Wähle anhand des Sachverhalts das passende Modul, arbeite dessen Prüfroutine vollständig ab und kombiniere Module nur, wenn der Fall tatsächlich mehrere Themen berührt.

## Arbeitsmodule

| Arbeitsmodul | Fokus |
| --- | --- |
| `er-bess-ppa-und-merchant-risk` | Prüft Erlösverträge für Speicher: Tolling, Capacity, Arbitrage, Regelenergie, Floor/Cap und Verfügbarkeitsgarantien. |
| `er-bess-projektakte-qualitygate` | Prüft die gesamte Speicherakte auf Lücken, Widersprüche, fehlende Quellen, falsche Rollen und unrealistische Annahmen. |
| `er-bess-rechtsmittel-und-nachbarabwehr` | Prüft Widerspruch/Klage, Nachbarrechte, Sofortvollzug, Baustopp, Umweltverbandsklage und Verteidigung. |
| `er-bess-regelenergie-systemdienstleistung` | Prüft Präqualifikation, Vermarktung, Verfügbarkeit, Messdaten, Sanktionen und Aggregator-Struktur. |

## Arbeitsweg

Für **Er Bess Ppa Und Merchant Risk, Er Bess Projektakte Qualitygate, Er Bess Rechtsmittel Und Nachbarabwehr, Er Bess Regelenergie Systemdienstleistung** zuerst das Arbeitsmodul wählen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `energierecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; Module nur kombinieren, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Arbeitsmodule im Detail

## 1. `er-bess-ppa-und-merchant-risk`

**Fokus:** Prüft Erlösverträge für Speicher: Tolling, Capacity, Arbitrage, Regelenergie, Floor/Cap und Verfügbarkeitsgarantien.

# PPA, Tolling und Merchant-Risk

## Wofür dieser Skill da ist

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

## Wofür dieser Skill da ist

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

## Wofür dieser Skill da ist

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

## Wofür dieser Skill da ist

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
