---
name: fachanwalt-it-recht-software-mangel
description: "Mangel an Standard- oder Individualsoftware nach Kauf- oder Werkvertragsrecht pruefen. Sach- und Rechtsmaengel § 434 BGB § 435 BGB beim Kauf; Werkmangel § 633 BGB bei Individualsoftware. Nacherfuellungspflicht § 439 BGB bzw. § 635 BGB Fristsetzung Nachfristablauf danach Ruecktritt § 437 Nr. 2 BGB Minderung § 441 BGB oder Schadensersatz § 437 Nr. 3 BGB § 280 BGB. Garantievertragsklauseln pruefen. BGH-Linie zu SaaS und Cloud."
---

# Software-Mangel

## Kaltstart-Rückfragen

1. Handelt es sich um Standardsoftware (Kaufrecht), Individualentwicklung (Werkvertrag) oder SaaS/Cloud-Bereitstellung (Mietvertrag § 535 BGB)?
2. Wurde das Werk bzw. die Software bereits abgenommen oder geliefert? Liegt ein Übergabeprotokoll vor?
3. Welche konkreten Funktionen fehlen oder funktionieren nicht wie zugesagt? Liegt ein Lasten-/Pflichtenheft vor?
4. Wurde dem Lieferanten bereits eine Nacherfüllungsfrist gesetzt und welche Reaktion erfolgte?
5. Ist der Mandant Verbraucher oder Unternehmer? Welche AGB-Klauseln gelten?

## Anspruchsgrundlagen

- Standardsoftware: Kaufrecht — Sachmangel § 434 BGB (objektive und subjektive Anforderungen), Rechtsmangel § 435 BGB.
- Individualsoftware: Werkvertrag — Mangel § 633 BGB, Werk frei von Sach- und Rechtsmängeln bei Abnahme.
- SaaS/Cloud: Mietrecht § 535 BGB — fortlaufende Gebrauchsgewährung, Mangel § 536 BGB führt zu Minderung kraft Gesetzes.
- Nacherfüllungspflicht: § 439 BGB (Kauf) bzw. § 635 BGB (Werk) — Nachbesserung oder Neulieferung.
- Sekundäre Rechte nach erfolglosem Fristablauf: Rücktritt § 437 Nr. 2 i.V.m. § 323 BGB, Minderung § 441 BGB, Schadensersatz § 437 Nr. 3 i.V.m. §§ 280, 281 BGB.
- BGH zu Standardsoftware als Sache: BGH VIII ZR 219/06, Urt. v. 15.11.2006, Rn. 12 ff.

## Beweislast und Frist

- Käufer/Besteller trägt nach Gefahrübergang bzw. Abnahme die Beweislast für den Mangel.
- Verbrauchsgüterkauf: Beweislastumkehr § 477 BGB für ein Jahr ab Gefahrübergang (vor 01.01.2022: sechs Monate).
- Verjährung Kaufrecht: zwei Jahre § 438 Abs. 1 Nr. 3 BGB; Werkvertrag bei nicht-Bauleistung: zwei Jahre § 634a Abs. 1 Nr. 1 BGB.
- Bei arglistig verschwiegenem Mangel: Regelverjährung § 438 Abs. 3 BGB bzw. § 634a Abs. 3 BGB.

## Prüfschema

```
1. Vertragstyp bestimmen (Kauf / Werk / Miete-SaaS)
2. Sollbeschaffenheit aus Lasten/Pflichtenheft und Vertrag ableiten
3. Istbeschaffenheit aus Tests und Logs dokumentieren
4. Soll/Ist-Abweichung = Mangel
5. Nacherfuellungsfrist setzen (zwei bis vier Wochen je nach Komplexitaet)
6. Bei Fristablauf: Ruecktritt oder Minderung oder Schadensersatz
7. Verjaehrung im Kalender notieren
```

Standardliteratur: Grüneberg BGB §§ 434, 633; Schneider IT-Vertragsrecht; MüKo-BGB / Westermann § 434.

## Schreibvorlage Mängelrüge mit Fristsetzung

```
Sehr geehrte Damen und Herren,

namens und in Vollmacht unserer Mandantschaft ruegen wir die nachfolgend
beschriebenen Maengel der gelieferten Software [Produktbezeichnung,
Versionsnummer]:

1. [Mangel 1 — Soll laut Pflichtenheft Ziff. X / Ist laut Test-Protokoll vom ...]
2. [Mangel 2 — ...]
3. [Mangel 3 — ...]

Wir fordern Sie auf bis spaetestens [Datum, mindestens zwei Wochen] die
Maengel im Wege der Nacherfuellung gemaess § 439 BGB / § 635 BGB zu
beseitigen.

Nach fruchtlosem Fristablauf werden wir vom Vertrag zuruecktreten den
Kaufpreis zurueckverlangen sowie Schadensersatz statt der Leistung
geltend machen (§§ 437 Nr. 2 und Nr. 3 BGB i.V.m. §§ 323 280 281 BGB).

Mit freundlichen Gruessen
```

## Übergabe

- Bei Fristablauf ohne Nacherfüllung: Übergang in `forderungsmanagement-klagewerkstatt` zur Klageerhebung.
- Bei laufendem SaaS: parallel Minderungsmitteilung an Vermieter nach § 536 BGB.
- Verjährungsfrist im Aktenkalender notieren.
