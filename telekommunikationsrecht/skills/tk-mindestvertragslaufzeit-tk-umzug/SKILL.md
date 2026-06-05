---
name: tk-mindestvertragslaufzeit-tk-umzug
description: "Tk Mindestvertragslaufzeit Kündigung, Tk Umzug Vertragsanpassung: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Mindestvertragslaufzeit Kündigung, Tk Umzug Vertragsanpassung

## Arbeitsbereich

In diesem Skill wird **Tk Mindestvertragslaufzeit Kündigung, Tk Umzug Vertragsanpassung** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-mindestvertragslaufzeit-kuendigung` | TK-Verträge: Mindestlaufzeit, automatische Verlängerung, monatliche Kündbarkeit, Kündigungsbutton/Onlinekündigung, AGB und Nachweis. |
| `tk-umzug-vertragsanpassung` | Umzug bei TK-Vertrag: Fortführung, Sonderkündigung, Leistungsfähigkeit am neuen Standort, Glasfaser-/Kabelanschluss und Kosten. |

## Arbeitsweg

Für **Tk Mindestvertragslaufzeit Kündigung, Tk Umzug Vertragsanpassung** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-mindestvertragslaufzeit-kuendigung`

**Fokus:** TK-Verträge: Mindestlaufzeit, automatische Verlängerung, monatliche Kündbarkeit, Kündigungsbutton/Onlinekündigung, AGB und Nachweis.

# Mindestlaufzeit, Verlängerung, Kündigung

## Einsatz

Der Skill prüft, ob Kunden aus einem Vertrag herauskommen oder Anbieter ihre Laufzeitklauseln sauber gestalten.

## Norm- und Quellenanker

TKG Kundenschutz; BGB §§ 309, 312k, 314; TDDDG bei Onlineabschluss; AGB-Recht.

## Arbeitsfragen

1. Welche Laufzeit wurde wann vereinbart?
2. Welche Verlängerungsmechanik gilt nach aktueller Rechtslage?
3. Wie wurde gekündigt und wie bestätigt?
4. Ist eine außerordentliche Kündigung möglich?

## Output

Kündigungsprüfung, Anbieterbrief, AGB-Redline und Fristenkalender.

## Red Flags

- alte Laufzeitlogik verwendet
- Kündigung im Portal nicht beweisbar
- Businessvertrag mit Verbraucherrecht verwechselt
- Sonderkündigungsgrund nicht dokumentiert

## Anschluss-Skills

- tk-umzug-vertragsanpassung
- tk-output-beschwerde-antrag-klage

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-umzug-vertragsanpassung`

**Fokus:** Umzug bei TK-Vertrag: Fortführung, Sonderkündigung, Leistungsfähigkeit am neuen Standort, Glasfaser-/Kabelanschluss und Kosten.

# Umzug und Telekommunikationsvertrag

## Einsatz

Für Streit, wenn Anbieter am neuen Wohn-/Geschäftsort nicht gleichwertig liefern kann.

## Norm- und Quellenanker

TKG Kundenschutzvorschriften zum Umzug live prüfen; BGB Dauerschuldverhältnis; AGB-Recht.

## Arbeitsfragen

1. Welche Leistung ist am neuen Standort technisch möglich?
2. Wurde Umzug rechtzeitig angezeigt?
3. Welche Laufzeit/Kündigungsfrist gilt?
4. Welche Umzugsgebühren sind vereinbart?

## Output

Umzugsprüfung, Kündigungs-/Fortführungsschreiben und Kostencheck.

## Red Flags

- Anbieter liefert anderes Produkt
- Laufzeit wird neu gestartet
- Umzug ins Ausland
- Hausanschluss fehlt

## Anschluss-Skills

- tk-mindestvertragslaufzeit-kuendigung
- tk-glasfaser-hausanschluss-wegerecht

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
