---
name: dokumententyp-erklaerungen
description: "Erkennt einseitige Willenserklaerungen: Kuendigungen, Faelligstellungen, Anfechtungen, Ruecktritte, Widerrufe, Wandlungserklaerungen. Markiert besonders zugangsbeduerftige Erklaerungen fuer den spaeteren Zustellungs-Check."
---

# Dokumententyp einseitige Erklaerungen

## Rolle und Fokus
Erkennt einseitige Willenserklaerungen: Kuendigungen, Faelligstellungen, Anfechtungen, Ruecktritte, Widerrufe, Wandlungserklaerungen. Markiert besonders zugangsbeduerftige Erklaerungen.

## Anwendungsbeispiel
Drawstop-Schreiben NordCap vom 22.05.2026: einseitige Erklaerung der Auszahlungsverweigerung gestuetzt auf 'material adverse change' und 'documentation gaps'. Versand per E-Mail an Bauernfeind; Zugangsnachweis fehlt; Vertretungsbefugnis des Unterzeichners (NordCap-Investment-Director) ist im Senior-Darlehensvertrag nicht eindeutig geregelt.

## Output-Module
- Eintrag in Reiter 2 mit Typ-Tag Erklaerung und Untertyp
- Pflicht-Querverweis an `zugang-zustellung-pruefung`
- Bei Vollmachtsfrage: Querverweis an `unterschriftspruefung`
