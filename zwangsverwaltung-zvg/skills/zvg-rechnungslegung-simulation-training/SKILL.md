---
name: zvg-rechnungslegung-simulation-training
description: "Rechnungslegung Simulation Training im Zwangsverwaltung (ZVG): prüft konkret Jahresrechnung und Schlussrechnung des Zwangsverwalters, Simulation und Training für Zwangsverwaltung mit einem, Schnittstelle zwischen laufender Zwangsverwaltung und dem. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Rechnungslegung Simulation Training

## Arbeitsbereich

Dieser Skill behandelt **Rechnungslegung Simulation Training** als zusammenhängenden Arbeitsgang im Zwangsverwaltung (ZVG). Im Mittelpunkt steht die Prüfung von Jahresrechnung und Schlussrechnung des Zwangsverwalters, Simulation und Training für Zwangsverwaltung mit einem, Schnittstelle zwischen laufender Zwangsverwaltung und dem. Die unten gelisteten Prüffelder bauen aufeinander auf: zuerst das im konkreten Fall tragende Feld identifizieren, dann ergänzend nur die Felder heranziehen, deren Tatbestand die Akte wirklich trägt. Rolle, Frist, Zuständigkeit, Beweislast und gewünschter Output bleiben dabei klar getrennt.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `zvg-rechnungslegung` | Jahresrechnung und Schlussrechnung des Zwangsverwalters nach § 161 ZVG. Anwendungsfall Rechnungslegungsperiode ist abgelaufen und Jahres- oder Schlussrechnung muss für Gericht erstellt werden. Normen § 161 ZVG Rechnungslegungspflicht § 155 ZVG Einnahmen Ausgaben § 10 ZVG Rangklassen. Prüfraster Jahresrechnung Schlussrechnung Endabrechnung Einnahme-Ausgaben-Rechnung Soll-Ist Belege Salden Verteilung. Output Gerichtsfähige Rechnungslegung mit Saldouebersicht Belegverzeichnis und Verteilungsnachweis. Abgrenzung zu zvg-konten-kassenführung (laufend) und zvg-verteilungsplan-155. |
| `zvg-simulation-training` | Simulation und Training für Zwangsverwaltung mit einem achtstuendigen Praxistag. Anwendungsfall Verwalter oder Kanzleimitarbeiter will Zwangsverwaltungs-Workflows trainieren oder Plugin demonstrieren. Deckt Mieterpost Objektgefahr Kontoabgleich Gericht Bericht und Verteilung ab. Output Simulationsprotokoll mit Tagesereignissen Fehlerhinweisen Lernnotizen und Leistungsbewertung. Abgrenzung zu zvg-kommandocenter (Echtbetrieb) und zvg-quality-gate. |
| `zvg-verkauf-versteigerung-schnittstelle` | Schnittstelle zwischen laufender Zwangsverwaltung und dem Zwangsversteigerungsverfahren. Anwendungsfall Zwangsverwaltung soll aufgehoben werden weil Zwangsversteigerung angeordnet wird oder laeuft. Normen § 153b ZVG Aufhebung der Verwaltung §§ 85 ff. ZVG Versteigerungsverfahren. Prüfraster Objektinformationen Besichtigungen Werterhalt Mieterlage Bieterfragen Übergabeprotokoll Aufhebung. Output Übergabebericht für Versteigerungsverfahren mit Objektzustand Mietlage und Schnittstellen-Dokumentation. Abgrenzung zu zvg-rechnungslegung (Abschluss) und zvg-bieterangebot-bewertung. |

## Arbeitsweg

- Rolle und Ziel im Zwangsverwaltung (ZVG) klären: Welche Partei vertritt der Mandant, welcher Ergebnistyp ist gefragt (Schriftsatz, Bescheidprüfung, Vertragsentwurf, Eilantrag, Stellungnahme)? Welches der oben gelisteten Prüffelder trägt die Akte wirklich?
- Fristen und Eilrisiken zuerst markieren: ZVG § 149 Beschlagnahme mit Anordnung, Rechnungslegung 12 Monate, Verteilungstermin nach Plan, sofortige Beschwerde 2 Wochen.
- Tragende Normen verifizieren: ZVG §§ 146-161 (Zwangsverwaltung), 1-150 (Zwangsversteigerung), §§ 869-882 ZPO, GVKostG, RPflG, GBO §§ 19, 20, 53 — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Gläubiger, Schuldner, Zwangsverwalter, Vollstreckungsgericht (AG), Rechtspfleger, Grundbuchamt, Mieter, Hausverwaltung.
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Zwangsverwaltungsantrag, Anordnungsbeschluss, Verwalterbestallung, Verwaltervergütungsfestsetzung, Rechnungslegung, Verteilungsplan, Aufhebungsbeschluss — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `zvg-rechnungslegung`

**Fokus:** Jahresrechnung und Schlussrechnung des Zwangsverwalters nach § 161 ZVG. Anwendungsfall Rechnungslegungsperiode ist abgelaufen und Jahres- oder Schlussrechnung muss für Gericht erstellt werden. Normen § 161 ZVG Rechnungslegungspflicht § 155 ZVG Einnahmen Ausgaben § 10 ZVG Rangklassen. Prüfraster Jahresrechnung Schlussrechnung Endabrechnung Einnahme-Ausgaben-Rechnung Soll-Ist Belege Salden Verteilung. Output Gerichtsfähige Rechnungslegung mit Saldouebersicht Belegverzeichnis und Verteilungsnachweis. Abgrenzung zu zvg-konten-kassenführung (laufend) und zvg-verteilungsplan-155.

# Rechnungslegung

## Aufgabe

Erstellt prüffähige Jahresrechnung, Schlussrechnung und Endabrechnung nach ZwVwV.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Kalenderjahr endet
- Zwangsverwaltung aufgehoben wird
- Gericht oder Beteiligte Auskunft verlangen

## Eingaben

- Kontoauszüge, Belege, Buchungsjournal
- Rent Roll, Anfangssaldo, Schlussbestand
- Vergütung, Gerichtskosten, Zahlungen an Gläubiger

## Workflow

1. **Daten schließen** - Zeitraum, Anfangsbestand, Endbestand, Kontoauszüge und Belege festlegen.
2. **Gliedern** - Soll-/Isteinnahmen und Ausgaben nach ZwVwV-Konten darstellen.
3. **Prüfen** - Saldo, Belege, USt-Option und Einzelbuchungen abgleichen.
4. **Einreichen** - Jahresrechnung, Schlussrechnung oder Endabrechnung mit Anlagen erstellen.

## Ausgabe

- Jahresrechnung
- Schlussrechnung
- Endabrechnung mit Belegliste

## Qualitätsgates

- Saldo rechnerisch stimmig
- Soll-Ist vollständig
- Umsatzsteuer gesondert, falls Option

## Rote Schwellen

- Konto nicht auf Null bei Endabrechnung
- fehlende Belege
- ungeklärter Anfangsbestand

## Interne Vorlagen

- assets/templates/rechnungslegung.md
- assets/templates/konto-kassenbuch.md

## Amtliche Erstquellen

- § 14 ZwVwV
- § 15 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Rechnungslegung

§ 152 ZVG (Verwalterpflichten) → § 154 ZVG (Gerichtsaufsicht) → § 14 ZwVwV (Jahresrechnung) → § 15 ZwVwV (Schlussrechnung) → § 155 ZVG (Verteilungsplan) → § 675 BGB (Rechenschaftspflicht Geschäftsbesorger) → § 667 BGB (Herausgabe)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Rechnungslegung

1. Jahresrechnung oder Schlussrechnung? (Jahresrechnung nach § 14 ZwVwV / Schlussrechnung bei Aufhebung)
2. Liegen alle Kontoauszüge des Rechnungszeitraums lückenlos vor?
3. Sind alle Einnahmen nach Nutzungsarten gegliedert? (Mieteinnahmen/Pachtzins/Sonstiges)
4. Sind Ausgaben nach ZwVwV-Konten kategorisiert?
5. Wird Umsatzsteuer ausgewiesen? (bei bestehender USt-Option)

## Output-Template Jahresrechnung (Schema)

```
JAHRESRECHNUNG ZWANGSVERWALTUNG
Objekt: [ADRESSE]
AZ: [X]
Rechnungszeitraum: 01.01.[JAHR] — 31.12.[JAHR]

A. EINNAHMEN
Sollmieten gesamt: [BETRAG]
Tatsächlich eingezogen: [BETRAG]
Rückstände: [BETRAG]
Sonstige Einnahmen: [BETRAG]
SUMME EINNAHMEN: [BETRAG]

B. AUSGABEN
Betriebskosten/Hausgeld: [BETRAG]
Instandhaltung: [BETRAG]
Öffentliche Lasten (Grundsteuer): [BETRAG]
Versicherungen: [BETRAG]
Verwaltervergütung (brutto): [BETRAG]
Gerichtskosten: [BETRAG]
Sonstiges: [BETRAG]
SUMME AUSGABEN: [BETRAG]

C. ERGEBNIS
Überschuss/Fehlbetrag: [BETRAG]
Anfangsbestand Treuhandkonto: [BETRAG]
Endbestand Treuhandkonto: [BETRAG]

Anlagen: Kontoauszüge K1-K[X], Belege A1-A[Y]
[ORT, DATUM, UNTERSCHRIFT ZWANGSVERWALTER]
```

## 2. `zvg-simulation-training`

**Fokus:** Simulation und Training für Zwangsverwaltung mit einem achtstuendigen Praxistag. Anwendungsfall Verwalter oder Kanzleimitarbeiter will Zwangsverwaltungs-Workflows trainieren oder Plugin demonstrieren. Deckt Mieterpost Objektgefahr Kontoabgleich Gericht Bericht und Verteilung ab. Output Simulationsprotokoll mit Tagesereignissen Fehlerhinweisen Lernnotizen und Leistungsbewertung. Abgrenzung zu zvg-kommandocenter (Echtbetrieb) und zvg-quality-gate.

# Simulation und Training

## Aufgabe

Erzeugt einen realistischen Trainingslauf für Zwangsverwaltungsfälle, wenn echte Schnittstellen oder Akten fehlen.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- das Plugin ausprobiert werden soll
- keine echten Objekt- oder Gerichtsdaten genutzt werden dürfen
- ein neuer Mitarbeiter den Ablauf trainiert

## Eingaben

- gewünschter Schwierigkeitsgrad
- optional Testakte oder eigener Objektsteckbrief
- Simulationsdauer

## Workflow

1. **Szenario wählen** - Wohnhaus, Gewerbe, WEG, Leerstand oder gemischtes Objekt auswählen.
2. **Tageslauf** - Mieterpost, Kontoeingänge, Gefahrmeldung, Gerichtsanfrage und Gläubigerdruck simulieren.
3. **Entscheidungen** - Nutzer durch Rückfragen, Entwürfe und Korrekturen führen.
4. **Auswertung** - Fehler, bessere Reihenfolge und Folgeaufgaben ausgeben.

## Ausgabe

- Simulationsakte
- Tagesprotokoll
- Lern- und Fehlerliste

## Qualitätsgates

- Simulation klar markiert
- keine echten personenbezogenen Daten
- Auswertung mit Rechtsquellen

## Rote Schwellen

- Nutzer verwechselt Simulation mit echter Akte
- fehlende Freigabe für echte Daten
- unzulässige Selbsthilfeidee

## Interne Vorlagen

- assets/templates/simulationstag.md
- assets/templates/quality-gate.md

## Amtliche Erstquellen

- ZVG Gesamtfassung
- ZwVwV Gesamtfassung

## Ergänzende Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Aus-/Fortbildung ZVG

§ 152 ZVG (Sorgfaltspflicht ordnungsgemäße Verwaltung) → § 280 BGB (Haftung Pflichtverletzung) → ZwVwV vollständig (Pflichtenprogramm)

## Typische Trainingsszenarien

1. **Mieter zahlt nicht:** Mahnverfahren, Kündigung, Klage — Schritt für Schritt
2. **Schuldner verweigert Zutritt:** Antrag auf gerichtliche Hilfe, § 154 ZVG
3. **Wasserschaden im Objekt:** Sofortmaßnahmen, Versicherungsmeldung, Gerichtsantrag Instandhaltung
4. **Insolvenzantrag des Schuldners kommt während Verwaltung:** Koordination mit Insolvenzverwalter
5. **Gläubiger fordert sofortige Ausschüttung:** Verteilungsplan § 155 ZVG, Rücklagen-Check
6. **Mieter kündigt und hinterlässt Schäden:** Dokumentation, Kautionseinbehalt, ggf. Klage

## Trainings-Template: Fallaufbau

```
Szenario: [TITEL]
Ausgangslage: [SACHVERHALT IN 3-5 SÄTZEN]
Handlungsdruck: [WAS PASSIERT WENN NICHTS GETAN WIRD]
Aufgabe: [KONKRETE HANDLUNG]
Lösung: [VORGEHEN SCHRITT FÜR SCHRITT]
Normen: [EINSCHLÄGIGE PARAGRAPHEN]
Häufige Fehler: [TYPISCHE FEHLER IN DIESER SITUATION]
```

## 3. `zvg-verkauf-versteigerung-schnittstelle`

**Fokus:** Schnittstelle zwischen laufender Zwangsverwaltung und dem Zwangsversteigerungsverfahren. Anwendungsfall Zwangsverwaltung soll aufgehoben werden weil Zwangsversteigerung angeordnet wird oder laeuft. Normen § 153b ZVG Aufhebung der Verwaltung §§ 85 ff. ZVG Versteigerungsverfahren. Prüfraster Objektinformationen Besichtigungen Werterhalt Mieterlage Bieterfragen Übergabeprotokoll Aufhebung. Output Übergabebericht für Versteigerungsverfahren mit Objektzustand Mietlage und Schnittstellen-Dokumentation. Abgrenzung zu zvg-rechnungslegung (Abschluss) und zvg-bieterangebot-bewertung.

# Schnittstelle zu Verkauf und Zwangsversteigerung

## Aufgabe

Unterstützt die Zwangsverwaltung, wenn parallel Versteigerung, freihändiger Verkauf oder Objektverwertung vorbereitet wird.

Der Skill arbeitet freistehend. Er setzt keine anderen Plugins voraus. Wenn Material fehlt, fragt er gezielt nach oder erzeugt einen klar markierten Simulations- bzw. Platzhalterstand.

## Startet bei

- Zwangsversteigerung parallel läuft
- Bieter oder Sachverständige Objektinformationen anfragen
- Verwaltung auf Zuschlag oder Aufhebung zuläuft

## Eingaben

- Versteigerungsakte, Wertgutachten, Besichtigungstermine
- Mieterliste, Objektzustand, laufende Kosten
- Gerichtliche Terminsdaten

## Workflow

1. **Informationspaket** - Objektzustand, Mieterlage, Versicherungen, Lasten und Rückstände zusammenstellen.
2. **Besichtigung** - Zutritt, Mieterkommunikation, Datenschutz und Protokoll steuern.
3. **Werterhalt** - notwendige Maßnahmen bis Zuschlag oder Aufhebung priorisieren.
4. **Übergang** - Aufhebung, Schlussrechnung, Endabrechnung und Übergabe planen.

## Ausgabe

- Objektinfopaket
- Besichtigungsplan
- Übergabe- und Aufhebungscheck

## Qualitätsgates

- Mieterrechte beachtet
- Daten nicht unnötig offengelegt
- Schlussrechnung vorbereitet

## Rote Schwellen

- Bieterzugang ohne Abstimmung
- Objektwertgefährdung
- Aufhebung ohne Endabrechnungspfad

## Interne Vorlagen

- assets/templates/besitzuebernahme-protokoll.md
- assets/templates/schlussrechnung-aufhebung.md

## Amtliche Erstquellen

- ZVG Gesamtfassung
- § 12 ZwVwV

## Aktuelle Rechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Paragrafenkette Versteigerungsschnittstelle

§ 180 ZVG (Anordnung Zwangsversteigerung parallel) → § 55 ZVG (Zuschlag Wirkungen) → § 56 ZVG (Übergabepflicht) → § 57 ZVG (Mieterschutz Ersteher) → § 57a ZVG (Sonderkündigung Ersteher) → §§ 566 BGB (Kauf bricht nicht Miete) → § 155 ZVG (Schlussrechnung bei Zuschlag)

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Triage Versteigerungsschnittstelle

1. Läuft parallel ein Zwangsversteigerungsverfahren?
2. Wann ist der Versteigerungstermin? (Schlussrechnung vorzubereiten)
3. Liegen alle Mietvertragsdaten für die Bieterinformation vor?
4. Sind Mietkautions-Guthaben der Mieter dokumentiert? (Übertragung auf Ersteher)

## bei Zuschlag

1. Zuschlagsdatum und Ersteher festhalten
2. Nutzungen bis Zuschlagsdatum verbuchen
3. Schlussrechnung nach § 15 ZwVwV erstellen
4. Kontostand an Vollstreckungsgericht melden
5. Mietverhältnisse und Kautionen an Ersteher übergeben
6. Abschluss-Bericht an Gericht und Gläubiger
