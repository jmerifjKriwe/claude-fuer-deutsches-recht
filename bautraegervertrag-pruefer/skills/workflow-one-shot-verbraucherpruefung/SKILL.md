---
name: workflow-one-shot-verbraucherpruefung
description: "One-Shot-Workflow für die verbraucherseitige Prüfung eines deutschen Bauträgervertrags: startet aus Vertrags-PDF, DOCX, Markdown oder Aktenordner ohne Rückfragenkaskade, bildet den Fall-Fingerabdruck, prüft MaBV, § 650u/§ 650v BGB, § 650m Abs. 2 BGB, AGB, Baubeschreibung, Abnahme, WEG, Eigentumssicherung und erzeugt Mandantenanschreiben, Gutachten und Gegenseitenschreiben."
---

# One-Shot-Verbraucherprüfung Bauträgervertrag

## Gegenstand

Dieser Skill ist der kompakte Gesamtworkflow für eine Käuferin oder einen Käufer, der einen deutschen Bauträgervertrag über Wohnung, Haus, Stellplatz, Keller, Sondernutzungsrecht oder Erbbaurecht prüfen lassen will. Er ersetzt keine Einzelskills, sondern hält den gesamten Ablauf zusammen, wenn nur ein einziges Skill-Dokument geladen werden kann.

## Sofortstart aus der Akte

Wenn ein Vertrag, Notarentwurf, PDF, DOCX, Markdown, OCR-Text, Scan oder Aktenordner vorliegt, beginne sofort mit der Auswertung. Frage nicht zuerst allgemein nach Rolle, Ziel oder Sachverhalt, wenn diese Informationen aus der Urkunde erkennbar sind. Stelle höchstens am Ende eine gebündelte Rückfrage, wenn ohne die Antwort eine Bewertung objektiv falsch oder irreführend wäre.

Arbeite in dieser Reihenfolge:

1. Vertragsstatus: Entwurf, beurkundet, Bauphase, vor Abnahme, nach Abnahme, Streit um Rate, Streit um Mängel, Insolvenzsignal.
2. Erwerberrolle: Verbraucher, private Kapitalanlage, Eigennutzung, gemischte Nutzung, Unternehmenseinsatz; bei Gewerbeeinheit nicht vorschnell Unternehmerstatus annehmen.
3. Kaufgegenstand: Einheit, Miteigentumsanteil, Keller, Stellplatz, Sondernutzungsrecht, Wohnfläche, Bauabschnitt, Teilungserklärung.
4. Zahlungen: Kaufpreis, Reservierungsentgelt, Sonderwünsche, MaBV-Raten, Schlussrate, Erschließungs-/Anschlusskosten, Finanzierungsvollmacht.
5. Sicherheiten: Auflassungsvormerkung, Lastenfreistellung, § 650m Abs. 2 BGB, § 7 MaBV, Notaranderkonto, Freigabemechanik.
6. Bausoll: Baubeschreibung, Pläne, Bemusterung, DIN-/ART-Verweise, Wohnflächenmethode, Energie-/Schall-/Brand-/Feuchteschutz, technische Nachweise.
7. Abnahme: Sondereigentum, Gemeinschaftseigentum, Vertreter-/Sachverständigenabnahme, Erstverwalter, Schlussrate, Mängelrechte.
8. WEG: Teilungserklärung, Gemeinschaftsordnung, Untergemeinschaften, Kostenverteilung, Erstverwalter, Wartungsverträge, Änderungsvollmachten.
9. Eigentum und Insolvenz: Rang, Grundpfandrechte, Pfandfreigabe, Löschung, Projektgesellschaft, Globalfinanzierung, Vorinsolvenzzeichen.
10. Ausgaben: Mandantenanschreiben, Mandantengutachten, Aufforderungsschreiben an Bauträger und Notar.

## Normenanker

Prüfe mindestens: §§ 305-310, 306, 307, 308 Nr. 4, 309 Nr. 12, 309 Nr. 15, 311b, 315, 320, 323, 326, 346 ff., 433, 631, 633-641, 642, 643, 650a, 650i, 650j, 650k Abs. 2/3, 650m Abs. 2, 650n, 650u, 650v, 883, 925 BGB; §§ 3, 7, 12 MaBV; § 17 Abs. 2a BeurkG; WEG, soweit Teilungserklärung, Gemeinschaftseigentum und GdWE betroffen sind; HOAI-Leistungsbild nur als Organisations- und Plausibilitätsraster, nicht als direkter Käuferanspruch gegen Planer.

## Rechtsprechungsanker, nur nach Live-Prüfung verwenden

- BGH, Urteil vom 26.03.2026 - VII ZR 68/24: Erwerbervertreter-Abnahme des Gemeinschaftseigentums in Bauträger-AGB nur tragfähig, wenn das eigene Prüf- und Abnahmerecht jedes Erwerbers nicht entzogen wird; vor Ausgabe über BGH/dejure prüfen.
- BGH, Urteil vom 26.03.2026 - VII ZR 108/24: Sachverständigenabnahme des Gemeinschaftseigentums in Bauträger-AGB ist kritisch, wenn sie die eigene Abnahmeentscheidung des Erwerbers ersetzt; vor Ausgabe über BGH/dejure prüfen.
- BGH, Urteil vom 22.04.2026 - VII ZR 88/25: Schlussrate nach vollständiger Fertigstellung nicht fällig, wenn nach Vertragslogik protokollierte Mängel/Restarbeiten vorher zu beseitigen sind; vor Ausgabe über BGH prüfen.
- BGH, Urteil vom 23.01.2026 - V ZR 91/25: Zustimmungspflichten zu Änderungen der Teilungserklärung/Gemeinschaftsordnung brauchen triftige, konkret benannte Gründe; § 308 Nr. 4 BGB; vor Ausgabe über BGH prüfen.
- BGH, Urteil vom 09.11.2023 - VII ZR 241/22: Abnahme des Gemeinschaftseigentums durch bauträgernahe Erstverwalter-/Tochtergesellschaft ist AGB-rechtlich angreifbar; vor Ausgabe über dejure/openjur/BGH prüfen.
- BGH, Beschluss vom 02.08.2023 - VII ZB 28/20: Notaranderkonto, MaBV-Schutz, Verwahrungsanweisung und Auszahlungsanspruch getrennt prüfen; vor Ausgabe über BGH/dejure prüfen.

## Pflichtausgabe

Gib nie nur eine Fundstellenliste oder abstrakte Kritik aus. Erzeuge immer:

1. **Mandantenanschreiben:** klare Empfehlung, ob Beurkundung/Zahlung/Abnahme derzeit empfohlen wird, welche Unterlagen fehlen und welche Punkte sofort geklärt werden müssen.
2. **Mandantengutachten:** paragraphen- und klauselorientierte Prüfung mit Ampelsymbolen, Normen, Rechtsprechungsankern, Gegenargumenten und Risikoauswirkung.
3. **Aufforderungsschreiben an Bauträger und Notar:** ausformuliert, höflich-fest, mit konkreten Streichungen, Ergänzungen oder Alternativformulierungen.

## Anti-Generik-Regel

Jeder Befund braucht mindestens zwei Fallanker: Klauselnummer, Originalwortlaut, Betrag, Rate, Datum, Haus-/Wohnungsnummer, Baubeschreibungsabschnitt, Gewerk, Partei, Urkundenrolle, Grundbuchblatt oder Bauabschnitt. Ein Satz wie „die Baubeschreibung ist unklar“ ist unzulässig; schreibe stattdessen, welcher Abschnitt zu welcher technischen oder wirtschaftlichen Folge führt und welche konkrete Vertragsfassung verlangt wird.
