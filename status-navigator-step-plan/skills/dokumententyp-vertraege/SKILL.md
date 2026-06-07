---
name: dokumententyp-vertraege
description: "Erkennt Vertraege als Dokumentenklasse: Darlehensvertraege, Wandeldarlehen, Gesellschaftervereinbarungen, Pflichtenheft, Kaufvertraege, Sicherungsvertraege. Ordnet sie nach Vertragspartei, Datum, Vertragstyp und Bezug zu uebrigen Dokumenten."
---

> **Hinweis:** Plugin `status-navigator-step-plan`, Dokumentenverarbeitung
> ohne Normen-Anker. Rechtliche Pruefung bleibt anwaltliche Aufgabe.

# Dokumententyp Vertraege erkennen

## Rolle und Fokus
Erkennt Vertraege als Dokumentenklasse. Pachtvertraege, Darlehensvertraege, Konsortialvertraege, Sicherungsvertraege, Gesellschaftervereinbarungen. Ordnet nach Vertragspartei, Datum, Vertragstyp.

## Vorgehen

1. **Vertragstyp und Rechtsrahmen** — BGB-Werkvertrag, Mietvertrag, Pachtvertrag, Darlehen, Gesellschaftsvertrag, Konsortialvertrag (BGB-Gesellschaft).
2. **Parteien und Vertretung** — Vollstaendige Firmierung, Vertreter, HR-Bezug; bei i.G.-Gesellschaft besondere Beachtung.
3. **Verweisstruktur** — Welche Anlagen, welche Vorvertraege, welche Bedingungen?
4. **Schluesselklauseln markieren** — Laufzeit, Kuendigung, MAC-Klausel, Sicherheiten, Zustimmungserfordernisse.
5. **Nachtraege chronologisch verknuepfen** — Nachtragsnummer, Datum, geaenderte Klauseln.

## Anwendungsbeispiel
LausitzStorage-Vertragslandschaft: Pachtvertrag LEAG mit 2 Nachtraegen, Senior-Darlehen NordCap, Wandeldarlehen NordCap, Konsortialvertrag Stadtwerke Cottbus, Avalrahmenvertrag ILB, Netzanschluss 50Hertz. Sieben Vertraege mit teils ueberlappenden Sicherheiten und Zustimmungserfordernissen — eine Vertragslandkarte vor der Reiterpflege ist Pflicht.

## Output-Module
- Vertragslandkarte (Bezugsgraph) als Vorblatt
- Eintraege in Reiter 2 mit Typ-Tag Vertrag und Untertyp
- Querverweise auf abhaengige Beschluesse, Vollmachten und Sicherheitenbestellungen

## Grenzen
- **Keine rechtliche Wirksamkeitspruefung.** Subsumtion bleibt anwaltliche Aufgabe.
- **Hinweise, keine Befunde.** Markierungen muessen anwaltlich verifiziert werden.
- **Datenschutz und Berufsrecht.** Nutzung nur mit System, das DSGVO, § 203 StGB und §§ 43a, 43e BRAO erfuellt.
