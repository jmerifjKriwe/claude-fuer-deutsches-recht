---
name: tk-cloud-tk-cookies
description: "Tk Cloud Telefonie Voip Compliance, Tk Cookies Telemedien Ttdsg Tdddg: wählt den konkreten Prüfpfad, trennt Frist, Zuständigkeit, Belege und Rechtsgrundlage und liefert den nächsten belastbaren Output."
---

# Tk Cloud Telefonie Voip Compliance, Tk Cookies Telemedien Ttdsg Tdddg

## Arbeitsbereich

In diesem Skill wird **Tk Cloud Telefonie Voip Compliance, Tk Cookies Telemedien Ttdsg Tdddg** als eigenständiger Arbeitsgang geprüft und in ein belastbares Arbeitsergebnis überführt. Die Prüffelder werden nach Aktenlage, Frist, Zuständigkeit, Beweislast und gewünschtem Output priorisiert.

## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `tk-cloud-telefonie-voip-compliance` | Cloud-PBX/VoIP: Notruf, Standort, Datenschutz, Aufzeichnung, Ausfallsicherheit, Rufnummern und internationale Nutzer. |
| `tk-cookies-telemedien-ttdsg-tdddg` | Telemedien-/TK-Schnittstelle: Cookies, Einwilligung, Endgerätezugriff, Consent-Banner und Telekommunikationsdienste. |

## Arbeitsweg

Für **Tk Cloud Telefonie Voip Compliance, Tk Cookies Telemedien Ttdsg Tdddg** zuerst das tragende Prüffeld bestimmen, dessen Tatsachen im konkreten Fall wirklich angelegt sind. Im Plugin `telekommunikationsrecht` bleiben Rollen, Fristen, Zuständigkeit, Anspruchs- oder Verfahrensgrundlage, Beweislast und gewünschter Output getrennt; ergänzende Prüffelder nur nutzen, wenn dieselbe Akte mehrere dieser Punkte trägt. Tragende Normen und Fundstellen nach `references/quellenhygiene.md` verifizieren.


## Prüffelder im Detail

## 1. `tk-cloud-telefonie-voip-compliance`

**Fokus:** Cloud-PBX/VoIP: Notruf, Standort, Datenschutz, Aufzeichnung, Ausfallsicherheit, Rufnummern und internationale Nutzer.

# Cloud-Telefonie und VoIP

## Einsatz

Für Unternehmen und Provider mit Teams-/Zoom-/Cloud-Telefonie.

## Norm- und Quellenanker

TKG; TDDDG; DSGVO; Notrufvorschriften; BGB.

## Arbeitsfragen

1. Wer ist Anbieter/Reseller?
2. Wie funktionieren Notruf und Standort?
3. Welche Aufzeichnungen/Logs?

## Output

VoIP-Compliance-Check und Nutzerinformation.

## Red Flags

- Notruf bei Homeoffice falsch
- Aufzeichnung ohne Rechtsgrund
- Rufnummernmissbrauch

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.

## 2. `tk-cookies-telemedien-ttdsg-tdddg`

**Fokus:** Telemedien-/TK-Schnittstelle: Cookies, Einwilligung, Endgerätezugriff, Consent-Banner und Telekommunikationsdienste.

# Cookies, Telemedien und TDDDG-Schnittstelle

## Einsatz

Für Anbieter, die TK-Dienste und Web-/App-Dienste kombinieren.

## Norm- und Quellenanker

TDDDG; DSGVO; ePrivacy; TKG.

## Arbeitsfragen

1. Ist Zugriff auf Endeinrichtung betroffen?
2. Welche Einwilligung ist erforderlich?
3. Wie passt das zu TK-Daten?

## Output

Consent- und Datenflusscheck.

## Red Flags

- Cookie und Verkehrsdaten vermischt
- berechtigtes Interesse überdehnt
- CMP falsch konfiguriert

## Anschluss-Skills

- Starte wieder mit `tk-allgemeiner-kaltstart`, wenn Rechtsweg, Rolle oder Bescheid noch unklar sind.

## Qualitätsregel

Keine Rechtsweg- oder Normbehauptung aus dem Bauch heraus. Bei Streit mit der Bundesnetzagentur immer Bescheid, Norm, Tenor, Nebenbestimmungen und Rechtsbehelfsbelehrung lesen; bei Verbraucherfällen Vertrag, Leistungsbeschreibung, Messprotokoll und Anbieterkommunikation trennen.
