---
name: fall-fingerabdruck-und-schnelltriage
description: "Fall-Fingerabdruck für Bauträgerakten: extrahiert Urkunde, Verkäufer, Verbraucherrolle, Wohnung/Haus/Stellplatz, Kaufpreis, Raten, Sicherheiten, Baubeschreibung, Teilungserklärung, Technik, Baufortschritt und Streitstand, bevor eine rote oder orange Bewertung gesetzt wird."
---

# Fall-Fingerabdruck und Schnelltriage

## Zweck

Dieser Skill verhindert abstrakte Bauträgervertragskritik. Bevor ein Risiko bewertet wird, wird die konkrete Urkunde mit Käufer, Projekt, Einheit, Ratenplan, Sicherheiten, Baubeschreibung und WEG-Struktur erfasst.

## Erfassungstabelle

| Feld | In der Akte konkret suchen |
| --- | --- |
| Urkunde | UR-Nr., Notar, Datum, Entwurf/Beurkundung, Bezugsurkunden, Verbraucherfrist, Anlagenstand |
| Verkäufer | Bauträgerfirma, Rechtsform, Projektgesellschaft, Vollmachten, Konzernbezug, Globalfinanzierer |
| Käufer | natürliche Person, Verbraucherstatus, Eigennutzung/private Kapitalanlage, Finanzierungsdruck, Notartermin |
| Grundstück | Grundbuch, Gemarkung, Flurstück, Baufelder, Bauabschnitte, Erschließung, Grundpfandrechte |
| Einheit | Wohnung/Haus, Nummer, Geschoss, Keller, Terrasse/Balkon, Sondernutzungsrecht, Stellplatz, Wohnfläche |
| Preis | Gesamtkaufpreis, Stellplatzpreis, Reservierungsentgelt, Sonderwünsche, Erschließung, Hausanschlüsse |
| Zahlungen | § 3-MaBV-Raten, § 7-MaBV-Modell, Schlussrate, Zahlungsaufforderungen, Bautenstandsbestätigungen |
| Sicherheiten | Vormerkung, Lastenfreistellung, § 650m-Abs.-2-Sicherheit, Bürgschaft, Notaranderkonto |
| Bausoll | Baubeschreibungsversion, Pläne, Bemusterung, Wohnflächenmethode, Schall, Energie, Feuchte, Brandschutz |
| Technik | Baugrund, Grundwasser, Altlasten, Kampfmittel, Baugrube, Statik, TGA, Aufzug, Tiefgarage, Lüftung |
| WEG | Teilungserklärung, Gemeinschaftsordnung, Erstverwalter, Wartungsverträge, Kostenverteilung |
| Streitstand | vor Beurkundung, vor Rate, vor Abnahme, Schlussrate, Mängel, Insolvenzsignal, Klage-/Rücktrittslage |

## Normenanker

§§ 13, 14, 305, 306, 307, 308 Nr. 4, 309 Nr. 12, 309 Nr. 15, 311b, 650j, 650k Abs. 2/3, 650m Abs. 2, 650n, 650u, 650v, 883, 925 BGB; §§ 3, 7, 12 MaBV; § 17 Abs. 2a BeurkG.

## Triage-Logik

1. **Vor Notartermin:** Fokus auf Beurkundungsfrist, Anlagenvollständigkeit, MaBV, Sicherheit, AGB, Baubeschreibung, Änderungsvollmachten.
2. **Nach Beurkundung vor erster Rate:** Fokus auf Fälligkeitsmitteilung, Vormerkung, Freistellung, Baugenehmigung, § 650m Abs. 2 BGB, Reservierungsentgelt.
3. **Während Bau:** Fokus auf Bautenstand, Ratenmeilensteine, Sonderwünsche, Verzögerung, Baugrund/Technik, Nachweise.
4. **Vor Abnahme/Schlussrate:** Fokus auf Sondereigentum, Gemeinschaftseigentum, Protokoll, Mängel, vollständige Fertigstellung, Zurückbehaltung.
5. **In der Krise:** Fokus auf Vormerkungsrang, Lastenfreistellung, Insolvenz, Rücktritt, Selbstvornahme, Vorschuss, Klageziel.

## Ausgabe

Gib zuerst eine knappe Fallkarte aus. Danach erst die rechtliche Bewertung. Jede Ampel muss auf ein konkretes Element der Fallkarte zurückführbar sein.
