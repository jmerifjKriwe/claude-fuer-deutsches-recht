---
name: tk-stoerung-tk-streitbeilegung
description: "Tk Stoerung Minderung Ausfallentschaedigung, Tk Streitbeilegung Bnetza: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Stoerung Minderung Ausfallentschaedigung, Tk Streitbeilegung Bnetza

## Arbeitsbereich

In diesem Skill wird **Tk Stoerung Minderung Ausfallentschaedigung, Tk Streitbeilegung Bnetza** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-stoerung-minderung-ausfallentschaedigung` | Internet-/Telefonstörung: Minderung, Ausfallentschädigung, Entstörungspflichten, Messprotokolle, SLA und Schadensersatz. |
| `tk-streitbeilegung-bnetza` | Streitbeilegung bei Zugang, Mitnutzung, Entgelt, Nummerierung oder Anbieterwechsel mit BNetzA-Beteiligung. |

## Arbeitsweg

Für **Tk Stoerung Minderung Ausfallentschaedigung, Tk Streitbeilegung Bnetza** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-stoerung-minderung-ausfallentschaedigung`

**Fokus:** Internet-/Telefonstörung: Minderung, Ausfallentschädigung, Entstörungspflichten, Messprotokolle, SLA und Schadensersatz.

# Störung, Minderung und Ausfallentschädigung

## Einsatz

Der Skill bearbeitet juristische Rechte mit ordentlicher technischer Dokumentation.

## Norm- und Quellenanker

TKG Kundenschutz, insbesondere Minderungs-/Entschädigungsregeln live prüfen; BGB §§ 280, 536 analog nur vorsichtig; ZPO.

## Arbeitsfragen

1. Welche vertraglich vereinbarte Leistung fehlt?
2. Wie wurde die Störung gemeldet und dokumentiert?
3. Ist eine BNetzA-konforme Messkampagne nötig?
4. Welche Ausfallentschädigung/Minderung/Schäden sind realistisch?

## Output

Minderungsberechnung, Providerbrief, Schlichtungs-/Klagebasis und Beweisplan.

## Red Flags

- Messung über WLAN
- Störung nicht gemeldet
- Business-SLA ignoriert
- Schadenshöhe nicht kausal belegt

## Anschluss-Skills

- tk-beweisplan-messung-stoerung-protokoll
- tk-schlichtung-verbraucher

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-streitbeilegung-bnetza`

**Fokus:** Streitbeilegung bei Zugang, Mitnutzung, Entgelt, Nummerierung oder Anbieterwechsel mit BNetzA-Beteiligung.

# BNetzA-Streitbeilegung zwischen Unternehmen

## Einsatz

Für schnelle regulatorische Konfliktlösung statt langer Zivilstreitigkeit.

## Norm- und Quellenanker

TKG Streitbeilegungsnormen live prüfen; VwVfG/VwGO.

## Arbeitsfragen

1. Welche Norm eröffnet Streitbeilegung?
2. Welche Vorverhandlungen sind dokumentiert?
3. Welche Entscheidung soll die BNetzA treffen?

## Output

Streitbeilegungsantrag mit Sachverhalt, Antrag und Anlagen.

## Red Flags

- Antrag zu unbestimmt
- keine Verhandlungshistorie
- Zuständigkeit nicht begründet

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
