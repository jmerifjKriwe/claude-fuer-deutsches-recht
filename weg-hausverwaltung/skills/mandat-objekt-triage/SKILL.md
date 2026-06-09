---
name: mandat-objekt-triage
description: "Erfasst eine WEG-/Hausverwaltungsakte (Stand 05/2026): Objekt, Rollen, Teilungserklärung, Gemeinschaftsordnung, Verwaltervertrag, Beschlusssammlung, Abrechnungen, Vermögensbericht, Angebote, Fristen, Risiken und nächsten Workflow. Identifiziert Fristen aus § 45 WEG, § 556 BGB sowie GEG-/CO2KostAu..."
---

# Mandat- und Objekt-Triage

## Aktenstart statt Formularstart

Wenn zu **Mandat Objekt Triage** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Weg Hausverwaltung** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Fachlicher Anker

- **Normen:** §§ 535, §§ 18, § 16 Abs. 2.
- **Entscheidungs-/Quellenanker:** Tragende Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle einsetzen; keine Entscheidung aus Modellwissen erzwingen.
- **Quellenhygiene:** `references/quellenhygiene.md` und `references/zitierweise.md` beachten.

## Fachkern: Mandat- und Objekt-Triage
- **Normen-/Quellenanker:** WEG §§ 18-28, 44/45, BGB-Miet-/Werkvertragsrecht, BetrKV, HeizkostenV, GEG, DSGVO und landesrechtliche Bau-/Sicherheitsfragen.
- **Entscheidende Weiche:** Trenne Beschlusskompetenz, ordnungsmäßige Verwaltung, Kostenverteilung, Anfechtungsfrist, Verwalterpflicht, Belegprüfung und Vollzug.

Stand: 05/2026.

## Ziel

Aus einer ungeordneten Verwaltungsakte entsteht ein arbeitsfähiges Objektprofil mit Fristen, Zuständigkeiten, Dokumentenlage und nächstem Skill.

## Abfrage

| Bereich | Klären |
| --- | --- |
| Objekt | Adresse, Einheiten, Wohn-/Gewerbeanteil, Baujahr, Verwaltung seit wann, Bundesland |
| Rollen | GdWE, Verwalter, Beirat, einzelne Eigentümer, vermietende Eigentümer, Mieter |
| Grundakte | Teilungserklärung, Gemeinschaftsordnung, Aufteilungsplan, Beschlusssammlung |
| Verwaltung | Verwaltervertrag, Vollmachten, Beiratsbestellung, Sonderzuständigkeiten, Sondervergütungen |
| Finanzen | Wirtschaftsplan, Jahresabrechnung, Vermögensbericht, Erhaltungsrücklage, Hausgeldrückstände, Sonderumlagen |
| Bau/Technik | Instandhaltungsstau, Angebote, Gutachten, Gewährleistungsfristen, GEG-Heizungsstatus, Steckersolar/Wallbox-Anträge |
| Streit | laufende Beschlussklagen, Beschwerden, Störungen, Datenschutzprobleme, vermieterspezifische Mieter-Konflikte |
| Energie/CO₂ | Energieausweis, Brennstoff/Heizart, CO₂-Stufe nach CO2KostAufG, anstehende GEG § 71-Fristen |

## Arbeitsweise

1. **Dokumente benennen und Lücken markieren.** (Liste: vorhanden / fehlt / unklar)
2. **Fristen und irreversible Risiken nach oben ziehen.**
 - § 45 WEG: 1 Monat Klage, 2 Monate Begründung (BGH V ZR 33/23).
 - 1 Jahr Erkundigungsobliegenheit bei Zustellungsverzug (BGH V ZR 17/24).
 - § 556 Abs. 3 BGB: 12 Monate Betriebskostenabrechnung Mieter.
 - Gewährleistung Werkvertrag 5 J. / VOB 4 J.
 - GEG § 71 Übergangsfristen für Heizungstausch (Großstädte 30.06.2026, sonst 30.06.2028).
3. **Vorgänge in Körbe sortieren**: Versammlung, Beschluss, Abrechnung, Bau, Hausgeld, Kommunikation, Datenschutz, Gericht.
4. **Primären Folge-Skill vorschlagen**.

## Cross-Refs

- Bei Versammlung-Stapel → `eigentuemerversammlung-vorbereiten`
- Bei Abrechnungsfragen → `wirtschaftsplan-jahresabrechnung-28-weg`
- Bei Hausgeld/Liquidität → `hausgeld-sonderumlage-liquiditaet`
- Bei baulichen Veränderungen → `bauliche-veraenderungen-20-weg`
- Bei Konflikt / Eskalation → `eskalation-anwalt-amtsgericht`

## Quellenpflicht

`rechtsstand-mai-2026-faktenbank` laden, sobald rechtliche Bewertung erfolgt.
