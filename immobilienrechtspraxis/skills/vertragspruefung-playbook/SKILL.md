---
name: vertragspruefung-playbook
description: Prueft externe Immobilienvertraege gegen das hauseigene Playbook der Rechtsabteilung. Drei Ausgaben — Ampelmatrix nach Klauselkatalog, Redline-Empfehlung als chirurgische Tracked Changes und Business-Memo fuer das Asset-Management. Playbook wird als Markdown oder JSON geladen und liefert pro Klauseltyp Soll-Formulierung Toleranzband und Eskalationsstufe. Geeignet fuer Mietvertraege Kaufvertraege Bauvertraege Hausverwaltervertraege Property-Management-Vertraege Facility-Vertraege. Erkennt regelmaessig kritische Themen wie Schriftform Indexierung Konkurrenzschutz Untervermietung Schoenheitsreparaturen-AGB und Gewaehrleistungsausschluss beim Grundstueckskauf.
---

# Vertragspruefung gegen Playbook

## Leitidee

Externe Vertraege werden nicht freihaendig geprueft, sondern gegen ein
hauseigenes Playbook. Das Playbook ist die institutionalisierte
Verhandlungserfahrung der Abteilung. Der Skill liefert Pruefergebnis,
Redline-Empfehlung und Business-Memo in einem Lauf.

## Inputs

- Externer Vertrag (.docx oder .pdf)
- Playbook (`playbook.md` oder `playbook.json`) mit Klauselkatalog
- Optional: interne Richtlinien (zB Mindest-Indexschwelle Maximalmietzeit)
- Optional: Vorvertrag oder LOI als Auslegungshilfe

## Playbook-Schema

```json
{
  "klausel_id": "indexmiete",
  "soll": "VPI mit Schwelle 5 Prozent und Mindestabstand zwoelf Monate",
  "toleranz": "Schwelle drei bis sieben Prozent",
  "rot": "Vollindexierung ohne Schwelle oder Mindestabstand",
  "eskalation": "Asset-Management bei Abweichung",
  "fundstelle": "§ 557b BGB"
}
```

## Methodik

1. Vertrag in Klauseln segmentieren
2. Jede Klausel einem Playbook-Eintrag zuordnen (Klassifikation per
   Schluesselwort und Semantik)
3. Ampel setzen — GRUEN entspricht Soll, GELB innerhalb Toleranz, ROT
   ausserhalb Toleranz
4. Fehlende Klauseln als WEISS markieren (Schutzluecke)
5. Redline-Vorschlag in Tracked Changes erzeugen wo ROT oder WEISS
6. Business-Memo mit drei bis fuenf Punkten was wirklich wirtschaftlich
   relevant ist

## Output

- `Pruefbericht_<Vertragsname>.md` mit Ampelmatrix in Tabellenform
- `<Vertragsname>_redlined.docx` mit Tracked Changes auf Klauselbasis
- `Memo_Business.md` — eine Seite, in Klartext, fuer Geschaeftsleitung

## Typische Pruefthemen im Immobilienrecht

- Schriftform Gewerbemiete § 550 BGB inklusive aller Nachtraege
- Indexmiete § 557b BGB versus Staffelmiete § 557a BGB
- Konkurrenzschutz und Sortimentsschutz bei Gewerberaum
- Untervermietung und Nutzungsaenderung
- Betriebskostenkatalog Verordnung 2003 und Umlagevereinbarung
- Schoenheitsreparaturen-Klauseln (BGH-Rechtsprechung Quotenklausel)
- Endrenovierungsklauseln (unwirksam wenn formularmaessig)
- Mietpreisbremse §§ 556d ff. BGB bei Wohnraum
- Kappungsgrenze § 558 Abs. 3 BGB
- Kuendigungsausschluss und Mindestlaufzeit
- Gewaehrleistungsausschluss beim Grundstueckskaufvertrag und Arglist
- Erschliessungskosten und Anliegerbeitraege
- Altlasten und Baulastenverzeichnis
- Belastung mit Grunddienstbarkeiten und Wegerechten

## Beispielformulierungen

- "Pruefe diesen Gewerbemietvertrag gegen unser Playbook. Schwerpunkt
  Schriftform Indexierung und Konkurrenzschutz."
- "Externer Kaufvertrag liegt vor. Vergleiche mit Playbook und liefere
  Ampelmatrix plus Redline."
- "Property-Management-Vertrag ist gekommen. Was muss vor Unterschrift
  geaendert werden, gemessen an unseren Mindeststandards?"

## Integration mit Projekten und Agenten

Der Skill ist so gebaut, dass er in einem Projekt-Ordner mit fixiertem
Playbook und Vertragstyp laeuft. Ein Agent kann auf eingehende Vertraege
auf einem Watch-Ordner reagieren und automatisch die Pruefung anstossen.
Siehe Skill `projekt-arbeitsweise`.
