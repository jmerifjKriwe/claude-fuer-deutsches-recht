---
name: richtlinien-skelett-erzeugen
description: "Generiert eine 13-Kapitel-Standardgliederung einer KI-Nutzungsrichtlinie analog der Master-Vorlage: Einleitung, Executive Summary, Potenziale, Rechtsbegriff, Fragen, Handlungsempfehlungen, Spezifische Vorgaben, RDG-Exkurs, KI-Kompetenz, KI-VO-Exkurs, Ausblick, Disclaimer, Literatur sowie Prompting-Anlage."
---

# Richtlinien-Skelett erzeugen

Dieses Skill erzeugt das vollständige Grundgerüst einer KI-Nutzungsrichtlinie für Kanzleien und Rechtsabteilungen. Das Skelett folgt einer 13-Kapitel-Struktur, die alle wesentlichen rechtlichen, organisatorischen und praktischen Aspekte abdeckt und als Ausgangspunkt für die Individualisierung dient.

## Rechtlicher Hintergrund

Eine vollständige KI-Nutzungsrichtlinie muss die relevanten Rechtsquellen kohärent abbilden: Die DSGVO (Art. 5, 6, 9, 28) zum Datenschutz, die BRAO (§§ 43, 43a, 43e) und BORA (§ 2) zum Berufsrecht, das UrhG (§ 2 Abs. 2, § 5) zum Urheberrecht, das GeschGehG zum Geheimnisschutz sowie die KI-VO (Art. 3, 4, 6, 50, Anhang III) zur Regulierung von KI-Systemen. Die BRAK-Hinweise vom Dezember 2024 und die DAV-Stellungnahme Nr. 32/2025 geben den Stand der berufsrechtlichen Diskussion wieder.

## Vorgehen

1. **Kanzlei-Kontext abfragen**: Ergebnis des Skills `kanzlei-kontext-analyse` als Grundlage nutzen.
2. **13 Kapitel anlegen**: Alle Kapitel mit Überschrift und Kurzbeschreibung vorstrukturieren.
3. **Kapitel priorisieren**: Je nach Kanzlei-Profil einzelne Kapitel ausführlicher oder schlanker gestalten (z.B. Drittland-Transfer nur bei internationalen Mandaten relevant).
4. **Prompting-Anlage anhängen**: Vier-Elemente-Methode als Anhang immer beifügen.
5. **Platzhalter einbauen**: Für kanzleispezifische Angaben (Name, DSB, Ansprechpartner, Datum) Platzhalter „[...]" verwenden.
6. **Versionierung einrichten**: Stand-Datum und Versions-Nummer im Dokumentkopf festhalten.

## Vorlagentext / Bausteine

**Standardgliederung KI-Nutzungsrichtlinie:**

```
Richtlinie zur Nutzung von KI-Systemen in [Name der Kanzlei/Rechtsabteilung]
Stand: [Monat/Jahr] | Version [X.X]
Verantwortlich: [Name Geschäftsführung/Partnerkreis]

1. KI im Einsatz – worum geht es?
2. Executive Summary (6 Eckpunkte)
3. Potenziale und Einsatzmöglichkeiten
4. Rechtlicher Begriff des KI-Systems (Art. 3 Nr. 1 KI-VO, OECD-Definition)
5. Rechtliche Rahmenbedingungen (DSGVO, BRAO, UrhG, GeschGehG)
6. Generelle Handlungsempfehlungen
   6.1 Datenschutz (DSGVO)
   6.2 Berufsrecht (BRAO/BORA/StGB)
   6.3 Urheberrecht (UrhG)
   6.4 Geheimnisschutz (GeschGehG)
   6.5 Technisch-vertragliche Absicherung
   6.6 Ausländische Dienstleister (§ 43e Abs. 4 BRAO)
7. Spezifische Vorgaben
   7.1 Schatten-KI
   7.2 Compliance-Regelsatz
   7.3 Organisatorische Maßnahmen
8. Exkurs: Rechtsberatung und RDG
9. KI-Kompetenz als Pflicht (Art. 4 KI-VO)
10. Exkurs: KI-Verordnung (KI-VO)
11. Ausblick und Fazit
12. Disclaimer
13. Weiterführende Literatur
Anlage: Prompting-Leitfaden
Anlage: Musterklauseln § 43e BRAO
```

## Hinweise zur Aktualisierung

Das Skelett ist bei wesentlichen Rechtsänderungen (neue KI-VO-Durchführungsrechtsakte, neue BRAK-Hinweise, neue BAG- oder OLG-Entscheidungen) anzupassen. Der Skill `richtlinien-update-zyklus` legt das Prüfintervall fest.
