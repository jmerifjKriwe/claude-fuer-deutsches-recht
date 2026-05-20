---
name: grundbuchanalyse
description: Strukturierte Auswertung grosser Mengen Grundbuchdaten — Grundbuchauszuege Flurkarten Baulastenverzeichnis Altlastenkataster. Extrahiert pro Objekt Eigentuemerkette Belastungen in Abteilung II und III Rang Loeschungserleichterungen Grunddienstbarkeiten Reallasten Vorkaufsrechte sowie offene Briefgrundschulden. Erzeugt Risikomatrix und Portfoliosicht ueber alle Objekte. Geeignet fuer Due-Diligence-Portfolios Bestandsaufnahme nach Erwerb Refinanzierungs-Vorbereitung und laufende Asset-Management-Kontrolle. Akzeptiert PDF-Scans mit OCR und konsumiert Tabellen aus XML oder CSV des Grundbuchamtes.
---

# Grundbuchanalyse

## Leitidee

Grundbuchdaten kommen in der Praxis als Stapel von PDF-Auszuegen, oft
gescannt, mit dazwischengewuerfelten Baulastenverzeichnissen, Flurkarten
und Altlastenausweisen. Der Skill normalisiert alles auf eine
Objekttabelle und ein einheitliches Risikoschema.

## Inputs

- Grundbuchauszuege (.pdf, gescannt oder digital)
- Optional: Baulastenverzeichnis-Ausdrucke
- Optional: Altlastenkataster-Auskuenfte
- Optional: Flurkarten und Lagepruefungen
- Objektliste als .xlsx oder .csv

## Methodik

1. OCR auf gescannten PDFs
2. Pro Auszug Identifikation Bestandsverzeichnis Abteilung I II III
3. Strukturierte Extraktion:
   - Bestandsverzeichnis: Gemarkung Flur Flurstueck Wirtschaftsart
     Groesse
   - Abteilung I: Eigentuemerkette mit Erwerbsgrund
   - Abteilung II: Lasten und Beschraenkungen (Dienstbarkeiten
     Reallasten Vorkaufsrechte Nacherbenvermerk Sanierungsvermerk)
   - Abteilung III: Grundpfandrechte mit Rang Betrag Glaeubiger
     Loeschungserleichterung Brieftyp
4. Querverweis mit Baulastenverzeichnis (Baulasten existieren NICHT
   im Grundbuch)
5. Risikobewertung pro Objekt und Aggregation auf Portfolio
6. Generierung Risikomatrix Excel-Tabelle und Memo

## Output

- `Grundbuch_Portfolio.xlsx` — eine Zeile pro Flurstueck, Spalten je
  Risikofeld
- `Risikomatrix.md` mit Ampel pro Objekt und Aggregat-Statistik
- `Auffaelligkeiten.md` — Objekte mit ungewoehnlichen Vermerken
  (Insolvenzvermerk Zwangsversteigerungsvermerk Nacherbenvermerk
  Sanierungsvermerk § 144 BauGB Vorkaufsrecht nach BauGB)

## Typische Risikofelder

- Briefgrundschuld ohne Loeschungsbewilligung
- Rangverhaeltnis Abteilung III nicht eindeutig
- Dienstbarkeit zugunsten unbekannter Dritter (Leitungsrechte
  Wegerechte)
- Vorkaufsrecht der Gemeinde nach §§ 24 ff. BauGB
- Sanierungsvermerk § 144 BauGB — Genehmigung erforderlich
- Nacherbenvermerk § 2113 BGB
- Insolvenz- oder Zwangsversteigerungsvermerk
- Baulast nicht im Grundbuch aber gegen Eigentuemer wirksam
- Altlastenverdachtsflaeche und mietminderungsrelevante Schadstoffe

## Beispielformulierungen

- "Werte alle Grundbuchauszuege aus diesem Ordner aus. Erzeuge
  Portfoliosicht und markiere Objekte mit Sanierungsvermerk."
- "Ich habe 87 PDF-Auszuege. Zeig mir Objekte mit offenen
  Briefgrundschulden und Baulasten."
- "Pruefe diese 15 Objekte auf Vorkaufsrechte der Gemeinde nach
  Paragraph 24 BauGB."

## Grenzen

Der Skill ersetzt nicht die Pruefung durch einen Immobilienjuristen.
Er liefert Vorstrukturierung und Risiko-Heatmap, damit der Mensch
seine Zeit dort einsetzt, wo es wirklich brennt.
