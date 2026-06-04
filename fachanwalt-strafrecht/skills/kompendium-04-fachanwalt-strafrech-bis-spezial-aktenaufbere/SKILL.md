---
name: kompendium-04-fachanwalt-strafrech-bis-spezial-aktenaufbere
description: "fachanwalt-strafrecht: Konsolidiertes Skill-Kompendium 04; bündelt 10 frühere Spezialskills (fachanwalt-strafrecht-orientierung, fachanwalt-strafrecht-untersuchungshaft-haftpruefung, fachanwalt-strafrecht-verstaendigung-257c-toa-46a, fachanwalt-strafrecht-wahlverteidiger-mandat, fachanwalt-strafrecht-zeugenbeistand und 5 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 04 - fachanwalt-strafrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `fachanwalt-strafrecht-orientierung` | Orientierung im Strafrecht-Mandat und Workflow-Routing: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und richtigen Spezial-Skill finden. § 136 StPO Belehrung, § 137 StPO Verteidigerrecht, StGB Straftatbestaende. Prüfraster Deliktstyp allgemeines oder Wirtschaftsstrafrecht, Verfahrensstand Ermittlung Anklage Hauptverhandlung, Mandantenrolle Beschuldigter Zeuge Nebenklaeger. Output Mandat-Einordnung mit Weiterleitung zum richtigen Workflow-Skill. Abgrenzung zu Mandat-Triage-Strafrecht für ausführliche Erstaufnahme. |
| `fachanwalt-strafrecht-untersuchungshaft-haftpruefung` | Untersuchungshaft und Haftprüfung nach §§ 112 ff. StPO: Anwendungsfall Mandant wurde verhaftet und Strafverteidiger muss Haftbefehl anfechten oder Haftprüfungsantrag stellen. §§ 112-113 StPO Haftgründe Fluchtgefahr Verdunkelungsgefahr Wiederholungsgefahr, § 117 StPO Haftprüfung 3-Monats-Frist, § 304 StPO Haftbeschwerde. Prüfraster dringender Tatverdacht prüfen, Haftgrundargumente widerlegen, verhältnismäßige Alternativmassnahmen anbieten. Output Haftbefehlsanfechtung oder Haftprüfungsantrag mit Argumentationsstrategie. Abgrenzung zu Erstgespraeach und zu Hauptverhandlung-Vorbereiten. |
| `fachanwalt-strafrecht-verstaendigung-257c-toa-46a` | Verständigung § 257c StPO und Taeter-Opfer-Ausgleich § 46a StGB vorbereiten: Anwendungsfall Strafverteidiger prüft ob Einigung durch Deal Einstellung oder TOA für Mandanten vorteilhaft ist. § 257c StPO Verständigung Gestaendnis gegen Strafrahmen, § 46a StGB Taeter-Opfer-Ausgleich Strafmilderung, § 153a StPO Einstellung gegen Auflage. Prüfraster Verständigungs-Eignung beurteilen, Gestaendnis-Risiken prüfen, TOA-Bereitschaft Opfer, Mandant belehren. Output Verständigungs-Strategie-Memo mit Gespraeachsskript und Belehrungsprotokoll. Abgrenzung zu Plaedoyer-Vorbereitung für Hauptverhandlung und zu Einlassung. |
| `fachanwalt-strafrecht-wahlverteidiger-mandat` | Wahlverteidiger-Mandat im Strafrecht beginnen: Anwendungsfall Beschuldigter waehlt Strafverteidiger und Erstgespraeach muss Schweigerecht Akteneinsicht Honorar und Strategie klaeren. § 136 StPO Schweigerecht Erstbelehrung, § 137 StPO Verteidigerrecht, § 147 StPO Akteneinsicht. Prüfraster Schweigerecht kommunizieren, eigene Einschaetzung zurückhalten bis Akte vorliegt, Honorarvereinbarung über RVG hinaus, Verteidigungsstrategie aktiv vs. passiv besprechen. Output Erstgespraeach-Protokoll mit Sofortmassnahmen und Honorarvereinbarung. Abgrenzung zu Erstgespraeach-Mandatsannahme für allgemeine Aufnahme und zu Akteneinsicht. |
| `fachanwalt-strafrecht-zeugenbeistand` | Zeugenbeistand im Strafverfahren für Zeugen mit eigenem Rechtsinteresse: Anwendungsfall Person ist als Zeuge geladen hat aber eigenes Aussageverweigerungsrecht oder Selbstbelastungsrisiko und benoetigt anwaltlichen Beistand. § 68b StPO Zeugenbeistand, § 55 StPO Auskunftsverweigerungsrecht, § 52 StPO Zeugnisverweigerungsrecht. Prüfraster Auskunftsverweigerungsrecht nach § 55 prüfen, Schutz vor Selbstbelastung, Zeugen-Aussage vorbereiten oder Aussage verweigern, Beistand aktiv ausüben. Output Strategie-Memo für Zeugenbeistand mit Aussagepfaden und Verweigerungs-Optionen. Abgrenzung zu Erstgespraeach für Beschuldigte und zu Nebenklage. |
| `mandat-triage-strafrecht` | Strukturierte Eingangs-Abfrage für Strafmandate. Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungshaft Vollzug Hausverbot) Beschuldigtenrechte § 136 § 137 § 140 § 141 StPO Pflichtverteidiger-Bestellung Mitbeschuldigte (Konflikt-Check § 43a BRAO § 146 StPO). Sofort-Fristen-Check Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Akteneinsicht § 147 StPO, Rechtsmittel und U-Haft-Eskalation. Routing zu Akteneinsicht, Haftmanagement und Strafprozess-Cockpit. |
| `plaedoyer-vorbereitung-strafverteidigung` | Plaedoyer für Strafverteidigung vorbereiten und strukturieren: Anwendungsfall nach Abschluss der Beweisaufnahme muss Strafverteidiger Schlusspledoyer mit Schuldfrage Strafzumessung und Verfahrenshindernissen vorbereiten. § 258 StPO Schlusspledoyer, § 46 StGB Strafzumessung, § 261 StPO freie Beweiswürdigung. Prüfraster Schuldfrage anhand Beweisaufnahme, Beweiswürdigungs-Angriff, Strafzumessung Milderungsgründe, Verfahrenshindernisse. Output Plaedoyer-Gliederung mit Kernargumentation und Antragsformulierungen. Abgrenzung zu Hauptverhandlung-Vorbereiten für Gesamtvorbereitung und zu Schriftsatzkern. |
| `schriftsatzkern-substantiierung` | Substantiierter Schriftsatzkern für Strafverfahren Einspruch und Revision: Anwendungsfall Strafverteidiger muss Einspruch gegen Strafbefehl Revisionsbegründung oder Klageerzwingungsantrag verfassen. §§ 410 ff. StPO Einspruch Strafbefehl, § 344 StPO Revisionsbegründung, § 172 Abs. 2 bis 3 StPO Klageerzwingungsantrag, § 147 StPO Akteneinsicht. Prüfraster Tatsachenvortrag-Geruest, Beweisantrag-Liste, Verfahrenshindernisse, Sachrügen und Verfahrensrügen, Strafmass-Hilfsantrag. Output vollständiger Verteidigungs-Schriftsatz mit Antrag Begründung und Beweisangebot. Abgrenzung zu Plaedoyer-Vorbereitung und zu Hauptverhandlung. |
| `spezial-adhaesion-formular-portal-und-einreichung` | Adhaesion: Formular, Portal und Einreichungslogik im Plugin fachanwalt strafrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-aktenaufbereiter-beweislast-und-darlegungslast` | Aktenaufbereiter: Beweislast, Darlegungslast und Substantiierung im Plugin fachanwalt strafrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `fachanwalt-strafrecht-orientierung`

**Frühere Beschreibung:** Orientierung im Strafrecht-Mandat und Workflow-Routing: Anwendungsfall Strafverteidiger erhaelt neue Anfrage und muss Strafrechts-Konstellation einordnen und richtigen Spezial-Skill finden. § 136 StPO Belehrung, § 137 StPO Verteidigerrecht, StGB Straftatbestaende. Prüfraster Deliktstyp allgemeines oder Wirtschaftsstrafrecht, Verfahrensstand Ermittlung Anklage Hauptverhandlung, Mandantenrolle Beschuldigter Zeuge Nebenklaeger. Output Mandat-Einordnung mit Weiterleitung zum richtigen Workflow-Skill. Abgrenzung zu Mandat-Triage-Strafrecht für ausführliche Erstaufnahme.

# Fachanwalt für Strafrecht — Orientierung

## FAO-Voraussetzungen

- **Theoretischer Lehrgang** 120 Stunden.
- **Drei Klausuren** zum Strafrecht.
- **60 Fälle** in den letzten drei Jahren, davon mindestens 40 Hauptverhandlungen mit eigener Beteiligung.
- Anmeldung bei der Rechtsanwaltskammer.

## Wichtige Normen

| Bereich | Norm |
|---|---|
| StGB Allgemeiner Teil | §§ 1 ff. StGB |
| StGB Besonderer Teil | §§ 80 ff. StGB |
| Strafverfahren | StPO §§ 1 ff. |
| Strafvollstreckung | StVollstrO StVollzG |
| Nebenstrafrecht | BtMG WaffG AO § 370 (Steuerhinterziehung) |
| Strafrecht Wirtschaft | §§ 263 263a 266 299 StGB GwG |
| Jugendstrafrecht | JGG |
| Beruf Strafverteidiger | § 137 StPO § 138 StPO § 142 StPO Pflichtverteidigung § 140 StPO |

## Typische Mandate

- Ermittlungsverfahren Erstvernehmung
- Untersuchungshaft (§§ 112 ff. StPO Haftprüfungsantrag § 117 StPO Haftbeschwerde § 304 StPO)
- Hauptverhandlung Strafrichter Schöffengericht Schwurgericht
- Verteidigung in Wirtschaftsstrafsachen (Wirtschaftsstrafkammer Landgericht)
- Berufung Revision Verfassungsbeschwerde
- Strafvollstreckung Bewährung Reststrafenaussetzung

## Notfristen

- **Berufung** § 314 StPO — **eine Woche** Notfrist.
- **Revision** § 341 StPO — **eine Woche** Notfrist.
- **Revisionsbegründung** § 345 StPO — **ein Monat**.
- **Beschwerde** § 311 StPO — **eine Woche**.
- **Verfassungsbeschwerde** § 93 BVerfGG — **ein Monat**.
- **Wiedereinsetzung** § 44 StPO — eine Woche.

## Hauptgerichte

- **Amtsgericht** Strafrichter § 25 GVG (Vergehen Privatklage oder keine höhere Strafe als zwei Jahre zu erwarten) Schöffengericht § 28 GVG (bis vier Jahre Straferwartung).
- **Landgericht** Große Strafkammer Wirtschaftsstrafkammer Schwurgericht.
- **OLG** Berufungs- und Revisionsinstanz; Anklage erstinstanzlich bei Staatsschutzdelikten.
- **BGH 1.–5. Strafsenat** Revisionsinstanz.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Berufsverband

- Deutscher Strafverteidiger e. V. (DSV).
- Vereinigung Berliner Strafverteidiger.
- Strafverteidigervereinigung Niedersachsen / NRW / Bayern.

## Schnittstellen

- **aktenaufbereiter-strafrecht** für Aktenaufbereitung.
- **kanzlei-allgemein** für Fristenbuch und Versand.

## Hinweis

Plugin fuer Fachanwaltschaft-Orientierung. Tiefe Verteidigung erfordert die Erfahrung des Fachanwalts; insbesondere bei Schwurgerichts- und Wirtschaftsstrafrecht.

## Zentrale Strafrecht-Normen im Ueberblick

- §§ 1-2 StGB — Gesetzlichkeitsprinzip; keine Strafe ohne Gesetz (nullum crimen)
- §§ 13-16 StGB — Begehungs-/Unterlassungsdelikt, Vorsatz, Irrtum
- §§ 20-21 StGB — Schuldunfaehigkeit, verminderte Schuldfaehigkeit
- §§ 46-49 StGB — Strafzumessung, besonderer Milderungsgrund
- § 78 StGB — Verjaehrungsfristen (z.B. 30 Jahre bei Mord)
- §§ 112-130 StPO — Untersuchungshaft, Haftbefehl, Haftgruende, Haftpruefung
- §§ 136-136a StPO — Beschuldigtenbelehrung, Aussageverweigerungsrecht, Beweisverwertungsverbote
- §§ 140-142 StPO — notwendige Verteidigung, Pflichtverteidiger

## Aktuelle Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 2. `fachanwalt-strafrecht-untersuchungshaft-haftpruefung`

**Frühere Beschreibung:** Untersuchungshaft und Haftprüfung nach §§ 112 ff. StPO: Anwendungsfall Mandant wurde verhaftet und Strafverteidiger muss Haftbefehl anfechten oder Haftprüfungsantrag stellen. §§ 112-113 StPO Haftgründe Fluchtgefahr Verdunkelungsgefahr Wiederholungsgefahr, § 117 StPO Haftprüfung 3-Monats-Frist, § 304 StPO Haftbeschwerde. Prüfraster dringender Tatverdacht prüfen, Haftgrundargumente widerlegen, verhältnismäßige Alternativmassnahmen anbieten. Output Haftbefehlsanfechtung oder Haftprüfungsantrag mit Argumentationsstrategie. Abgrenzung zu Erstgespraeach und zu Hauptverhandlung-Vorbereiten.

# Untersuchungshaft Haftprüfung

## Zweck

Verteidigung bei drohender oder bestehender Untersuchungshaft.

## 1) Haftgründe § 112 II StPO

### Fluchtgefahr

- Konkrete Anhaltspunkte (Auslandsverbindungen, Mittel)
- Nicht: nur Strafe-Höhe

### Verdunkelungsgefahr

- Beweisbeeinflussung
- Zeugen-Beeinflussung
- Beweismittel-Verschwindung

### Wiederholungsgefahr

- Nur bei bestimmten Straftaten (§ 112a StPO)

### Schwerverbrechens-Haft § 112 III StPO

- Bei besonders schweren Delikten ohne weiteren Grund

## 2) Voraussetzungen

### Dringender Tatverdacht

- Wahrscheinlichkeit Verurteilung > Freispruch
- Beweis-Stand

### Verhältnismaessigkeit

- Auch bei dringendem Tatverdacht
- Erwartete Strafe vs. Haft-Dauer
- Schonungsbedürftige (Kinder, Pflege)

## 3) Haftbefehl § 114 StPO

### Inhalt

- Konkrete Vorwurf
- Haftgrund
- Verhältnismaessigkeit

### Bekanntgabe

- Sofort bei Verhaftung
- Anwalts-Information

## 4) Haftprüfung § 117 StPO

### Antrag

- Jederzeit möglich
- Schriftlich oder zu Protokoll

### Verfahren

- AG-Richter entscheidet
- Muendliche Anhörung
- Bei Aufhebung: sofortige Entlassung

### Frist § 121 StPO

- Nach **6 Monaten** Haft: Prüfung OLG
- Bei Verlängerung: durch OLG-Beschluss

## 5) Haftbeschwerde § 304 StPO

### Voraussetzungen

- Beschwerde gegen Haftbefehl oder Verlängerung
- Frist: jederzeit (ohne Frist)

### Verfahren

- LG-Beschwerdekammer entscheidet
- Bei Niederlage: weiterer Rechtsweg OLG

## 6) Haftverschont § 116 StPO

### Voraussetzungen

- Haftgrund kann durch mildere Maßnahmen abgewendet werden
- Beispiele:
  - Meldepflicht
  - Pass-Hinterlegung
  - Kaution

### Typische Maßnahmen

- Wohnsitz-Auflage
- Tag-Anwesenheits-Auflage
- Kontakt-Verbot

## 7) Workflow Verteidigung

### Sofort-Schritte

- Mandanten-Besuch (binnen Stunden)
- Akteneinsicht-Antrag
- Haftprüfungs-Antrag oder Beschwerde

### Phase 2

- Vorbereitung Anhörung
- Beweise gegen Haftgründe
- Verschon-Alternativen vorschlagen

### Phase 3

- Bei Niederlage: Beschwerde
- Bei Erfolg: Verschon-Vereinbarung

### Phase 4 — Dauer-U-Haft

- Anfechtung Verlängerung
- Nach 6 Monaten: OLG-Prüfung
- Strategie Hauptverhandlungs-Vorbereitung

## 8) Praktische Aspekte

### Mandanten-Betreuung

- Regelmäßige Besuche
- Schreib-Kommunikation
- Familien-Info

### Akteneinsicht bei U-Haft

- § 147 II 2 StPO: voller Zugang
- Schnelles Verfahren

### Wirtschaftliche Folgen

- Lohnausfall
- Familien-Belastung
- Reputations-Schaden

## 9) Typische Fehler

1. **Pflichtverteidiger ohne Strafrecht-Expertise**
2. **Haftprüfung zu spaet beantragt**
3. **Verschon-Alternativen nicht ausgearbeitet**
4. **Akteneinsicht verzoegert**

## 10) BGH/BVerfG-Linien (Stand Mai 2026)

- Verfassungsrechtliche Maßstaebe der Untersuchungshaft (Verhaeltnismaessigkeit, Beschleunigungsgebot in Haftsachen): Grundlage BVerfG 17.01.2013 — 2 BvR 2098/12 und BVerfG-Linie zur ueberlangen Haft; Aktualisierungen vor Ausgabe in bverfg.de und dejure.org pruefen. Offene Fundstelle (Verzeichnis): https://dejure.org/dienste/lex/StPO/112/1.html
- BVerfG 23.09.2025 — 2 BvR 625/25: ANOM-Kommunikation und Verwertbarkeit im Strafverfahren; relevant fuer Tatverdacht und damit Haftgrund. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BVerfG&Datum=23.09.2025&Aktenzeichen=2+BvR+625/25
- Hinweis: Eine BGH-Leitentscheidung 2025/2026 speziell zu § 112 StPO / Haftpruefung ist Stand Mai 2026 nicht in dejure.org / openjur.de mit Volltext zugänglich; vor Ausgabe Aktenzeichen-Recherche unter "§ 112 StPO Haftgrund" durchführen.

## Anschluss

- `fachanwalt-strafrecht-wahlverteidiger-mandat` — bei Mandats-Beginn
- `fachanwalt-strafrecht-anklage-reaktion` — bei Anklage
- `aktenaufbereiter-strafrecht` — bei Akten-Auswertung


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `fachanwalt-strafrecht-verstaendigung-257c-toa-46a`

**Frühere Beschreibung:** Verständigung § 257c StPO und Taeter-Opfer-Ausgleich § 46a StGB vorbereiten: Anwendungsfall Strafverteidiger prüft ob Einigung durch Deal Einstellung oder TOA für Mandanten vorteilhaft ist. § 257c StPO Verständigung Gestaendnis gegen Strafrahmen, § 46a StGB Taeter-Opfer-Ausgleich Strafmilderung, § 153a StPO Einstellung gegen Auflage. Prüfraster Verständigungs-Eignung beurteilen, Gestaendnis-Risiken prüfen, TOA-Bereitschaft Opfer, Mandant belehren. Output Verständigungs-Strategie-Memo mit Gespraeachsskript und Belehrungsprotokoll. Abgrenzung zu Plaedoyer-Vorbereitung für Hauptverhandlung und zu Einlassung.

# Verständigung § 257c StPO / TOA § 46a StGB

## Zweck

Strafrechtliche Erledigungs-Formen jenseits der Hauptverhandlung: **Verständigung § 257c StPO** (Strafrahmen gegen Geständnis), **Täter-Opfer-Ausgleich § 46a StGB** (Strafmilderung), **§ 153a StPO Einstellung gegen Auflage**, **Adhäsionsverfahren § 403 StPO** (Schmerzensgeld im Strafverfahren).

## Eingaben

- Tatbestand (Strafrahmen)
- Beweislage (Geständnis-Bereitschaft?)
- Opfer / Geschädigte Person
- Wirtschaftliche Verhältnisse (Geldauflage)
- Vorstrafen
- Verfahrensphase (Ermittlung, Anklage, Hauptverhandlung)

## Rechtlicher Rahmen

- **§ 257c StPO** — Verständigung über Strafrahmen
- **§ 257c Abs. 5 StPO** — Belehrungspflicht
- **§ 153a StPO** — Einstellung gegen Auflage
- **§ 46a StGB** — TOA als Strafmilderung
- **§ 403 ff. StPO** — Adhäsionsverfahren

### Leitentscheidungen (Stand Mai 2026)

- BGH, Beschluss vom 20.11.2025 — 4 StR 232/25 (4. Strafsenat): TOA bei sexuellem Missbrauch — § 46a Nr. 1 StGB setzt friedensstiftenden kommunikativen Prozess voraus, der eine Verantwortungsübernahme des Täters erkennen lässt; bloße Schadenswiedergutmachung ohne kommunikatives Element genügt nicht. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25
- BGH, Beschluss des Großen Senats für Strafsachen vom 03.02.2025 — GSSt 1/24: Cannabisbesitz neben Handeltreiben nach KCanG — bei Vorrätighalten teils zum gewinnbringenden Absatz, teils zum Eigenkonsum tritt der Besitz nach Konkurrenzgrundsätzen zurück, sofern die Eigenkonsummenge die straffreien Grenzen des § 3 KCanG nicht überschreitet; sanktionsfreie Mengen sind aus der Einziehung herauszunehmen. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- BGH, Beschluss vom 15.07.2025 — 2 StR 644/24 (2. Strafsenat): KCanG-Strafzumessung — die in § 1 Nr. 8 ff. KCanG gezogene gesetzliche Wertung ist als bestimmender Strafzumessungsgrund zu berücksichtigen. Offene Fundstelle: https://dejure.org/dienste/vernetzung/rechtsprechung?Text=2+StR+644/24
- Hinweis zu § 257c StPO: Es gibt keine vom Modell verifizierte BGH-Leitentscheidung 2025/2026, die § 257c StPO neu fasst; weitere Entscheidungen vor Verwendung live in dejure.org / openjur.de prüfen.

## ADR-Pfade im Strafrecht

### Pfad 1 — § 153a StPO Einstellung gegen Auflage

- Geringe Schuld
- Geldauflage (typisch an gemeinnützige Einrichtung)
- Kein Eintrag ins BZR
- StA / Gericht-Zustimmung

### Pfad 2 — Verständigung § 257c StPO

- Geständnis gegen Strafrahmen-Limit
- Belehrungs-Pflicht zwingend
- Geständnis-Rabatt 25-33 %
- Hauptverhandlung verkürzt

### Pfad 3 — TOA § 46a StGB

- Aussöhnung mit Opfer
- Schadenswiedergutmachung
- Strafmilderung § 49 StGB (analog) bis Strafrahmen-Verschiebung
- Bewertung durch Konfliktstellen / Schlichtungsstellen

### Pfad 4 — Adhäsionsverfahren § 403 StPO

- Geschädigter macht zivilrechtlichen Anspruch im Strafverfahren geltend
- Schmerzensgeld + Schadensersatz
- Bei Anerkennung: Vollstreckungs-Titel im Strafurteil

### Pfad 5 — Strafbefehl § 407 StPO

- Schriftliches Verfahren
- Bis 360 Tagessätze Geldstrafe oder 1 Jahr zur Bewährung
- Einspruch 2 Wochen

## Workflow

### Phase 1 — Akteneinsicht § 147 StPO

- Vollakteneinsicht
- Beweislage beurteilen
- Geständnis-Strategie planen

### Phase 2 — TOA-Versuch

- Konfliktstelle einschalten
- Opfer-Kontakt aufnehmen
- Schadenswiedergutmachung
- Schriftliche TOA-Vereinbarung

### Phase 3 — Verständigungs-Gespräch StA / Gericht

- Strafrahmen verhandeln
- Geständnis-Umfang
- Auflagen (Anti-Aggressionstraining, Drogen-Therapie etc.)

### Phase 4 — Hauptverhandlung mit Verständigung

- Belehrung § 257c V durch Gericht
- Geständnis abgeben
- Strafrahmen-Bestätigung

### Phase 5 — Bei Scheitern

- Streitige Hauptverhandlung
- Beweisanträge
- Volles Urteil

## Strategie und Taktik

- TOA-Strategie nach BGH 20.11.2025 — 4 StR 232/25: friedensstiftender kommunikativer Prozess (Aussöhnungsversuch, Verantwortungsübernahme) muss dokumentiert sein; reine Zahlung an Opfer reicht für § 46a Nr. 1 StGB nicht. Weitere Rechtsprechung vor Ausgabe live in dejure.org / openjur.de prüfen.
- **Geständnis nach Akteneinsicht**: nie vorab; Beweislage muss geprüft sein
- **TOA-Strategie**: Schadenswiedergutmachung sichtbar machen (Zahlungsplan)
- **Vorstrafen**: bei nicht-Geständigem Verteidigungs-Pfad häufig vorteilhaft
- **Bei Wirtschaftsstraftaten**: § 153a-Auflage orientiert sich an 30 % des Schadens

## Querverweise

- `fachanwalt-strafrecht-orientierung` — Triage
- `fachanwalt-strafrecht-wahlverteidiger-mandat` — Mandatsannahme
- `fachanwalt-strafrecht-anklage-reaktion` — Reaktion auf Anklage
- `fachanwalt-strafrecht-chatcontrol-csam-anwaltsgeheimnis-53-stpo` — Sonderfall
- `anw-steuerstrafverteidigung-verstaendigung` — Steuerstraf-Variante

## Quellen und Updates (Stand Mai 2026)

- BGH 20.11.2025 — 4 StR 232/25 (TOA § 46a Nr. 1 StGB, sexueller Missbrauch): https://dejure.org/dienste/vernetzung/rechtsprechung?Gericht=BGH&Datum=20.11.2025&Aktenzeichen=4+StR+232/25
- BGH (GSSt) 03.02.2025 — GSSt 1/24 (KCanG, Cannabisbesitz vs. Handeltreiben, sanktionsfreie Mengen): https://dejure.org/dienste/vernetzung/rechtsprechung?Text=GSSt+1/24
- BGH 15.07.2025 — 2 StR 644/24 (KCanG-Strafzumessung): https://dejure.org/dienste/vernetzung/rechtsprechung?Text=2+StR+644/24
- KCanG (Konsumcannabisgesetz) in Kraft seit 01.04.2024 (BGBl. I 2024 Nr. 109): https://dejure.org/BGBl/2024/BGBl._I_Nr._109
- Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff. Aktenzeichen und Volltext vor Verwendung in dejure.org bzw. openjur.de verifizieren.

## 4. `fachanwalt-strafrecht-wahlverteidiger-mandat`

**Frühere Beschreibung:** Wahlverteidiger-Mandat im Strafrecht beginnen: Anwendungsfall Beschuldigter waehlt Strafverteidiger und Erstgespraeach muss Schweigerecht Akteneinsicht Honorar und Strategie klaeren. § 136 StPO Schweigerecht Erstbelehrung, § 137 StPO Verteidigerrecht, § 147 StPO Akteneinsicht. Prüfraster Schweigerecht kommunizieren, eigene Einschaetzung zurückhalten bis Akte vorliegt, Honorarvereinbarung über RVG hinaus, Verteidigungsstrategie aktiv vs. passiv besprechen. Output Erstgespraeach-Protokoll mit Sofortmassnahmen und Honorarvereinbarung. Abgrenzung zu Erstgespraeach-Mandatsannahme für allgemeine Aufnahme und zu Akteneinsicht.

# Wahlverteidiger-Mandat

## Zweck

Beratung Beschuldigter bei Wahl Strafverteidiger und Mandats-Beginn.

## 1) Erstgespräch

### Vor jedem Inhalt

- **Schweigerecht** kommunizieren (§ 136 I StPO)
- Verteidiger-Geheimnis § 53 StPO
- Eigene Sicht erst nach Akteneinsicht

### Sachverhalts-Aufnahme

- Was wirft Polizei / StA vor?
- Sind schon Aussagen gemacht?
- Beweismittel-Lage?

### Honorar-Vereinbarung

- RVG-Minimum oder Pauschal-Vereinbarung
- Komplex-Sachen oft Pauschal 5.000-50.000 EUR

## 2) Akteneinsicht § 147 StPO (Reform 2017)

### Beschuldigter

- **§ 147 IV StPO**: Eigenes Akteneinsichtsrecht (auch ohne Anwalt)
- Begleitende Voraussetzung: nicht im Verfahrens-Stadium der Gefährdung
- Polizeiakten-Anfrage

### Anwalt

- § 147 II StPO: Voll-Recht
- Bei U-Haft: § 147 II 2 StPO
- Mitnahme Papierakten § 32f II 3 StPO
- Kopie über Anwalt-Kanzlei

### Rechtsbehelf

- § 147 V 2 StPO: Antrag auf gerichtliche Entscheidung
- Bei Verweigerung
- Auch bei eingeschraenkter Einsicht

## 3) Verteidigungs-Strategien

### Aktive Strategie

- Anfechtung Beweise
- Eigene Beweis-Anträge
- Sachverständige
- Gegenermittlungen

### Passive Strategie

- Schweigen
- Beobachtung Vorwurfs-Beweis
- Reaktion bei Schwaeche der Beweise

### Mischformen

- Phasen-Wechsel je nach Verfahrensstand
- Bei Untersuchungs-Haft: oft Aktivität erforderlich

## 4) Workflow

### Phase 1 — Erstgespräch (1-2 Stunden)

- Vorwurfs-Aufnahme
- Schweigerecht erklären
- Honorar-Vereinbarung
- Vollmacht

### Phase 2 — Akteneinsicht

- Antrag StA / Polizei
- Auswertung Akte
- Schwachstellen-Analyse

### Phase 3 — Vernehmungs-Strategie

- Eigene Aussage / Schweigen
- Vorbereitung bei aktiver Strategie

### Phase 4 — Eröffnungs-Beschluss / Anklage

- Antrag auf Einstellung § 153/153a StPO
- Beweisanträge
- Vorbereitung Hauptverhandlung

### Phase 5 — Hauptverhandlung

- Plaedoyer-Strategie
- Anträge auf Strafmilderung
- Geringfuegigkeits-Antrag

## 5) Standard-Fehler des Beschuldigten

1. **Aussage vor anwaltlicher Beratung** -> oft unwiderruflich
2. **"Ich erklaere das mal eben" bei Polizei** — taktisch fatal
3. **Eigene Anrufe / Briefe** an Anzeigenerstatter
4. **Mitwirkung in WhatsApp-Gruppen** des Falls
5. **Pflichtverteidigung statt Wahl** bei komplexen Fällen

## 6) Mandanten-Pflichten

### Wahrheit gegenüber Anwalt

- Anwalt-Vertraulichkeit § 43a BRAO
- Strategie braucht volle Information

### Schweigen gegenüber Dritten

- Keine Aussagen ohne Anwalt
- Auch in sozialen Medien

## 7) Bei Untersuchungshaft

### Sofortige Schritte

- Haftprüfungs-Antrag
- Akteneinsicht beschleunigen
- Familien-Information

### Vertretungs-Pflicht

- Notwendige Verteidigung § 140 StPO
- Pflichtverteidiger bei Mittel-Fehlen

## 8) BGH-Linien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Anschluss

- `fachanwalt-strafrecht-untersuchungshaft-haftpruefung` — bei U-Haft
- `fachanwalt-strafrecht-anklage-reaktion` — bei Anklage
- `aktenaufbereiter-strafrecht` — bei Akten-Aufbereitung

## Aktuelle Rechtsprechung Wahlverteidigung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen Wahlverteidigung

- § 137 StPO — freie Wahl des Verteidigers (bis zu drei gleichzeitig)
- § 138 StPO — Verteidiger-Eigenschaft (Rechtsanwaelte, andere Personen mit Gerichtsgenehmigung)
- § 140 StPO — notwendige Verteidigung (Verbrechen, U-Haft, Gehoerlosen, Vergehen ab 1 Jahr Straferwartung)
- § 146 StPO — Verbot der Mehrfachverteidigung bei Mitbeschuldigten
- § 43a II BRAO — Verschwiegenheitspflicht
- § 53 StPO — Zeugnisverweigerungsrecht

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 5. `fachanwalt-strafrecht-zeugenbeistand`

**Frühere Beschreibung:** Zeugenbeistand im Strafverfahren für Zeugen mit eigenem Rechtsinteresse: Anwendungsfall Person ist als Zeuge geladen hat aber eigenes Aussageverweigerungsrecht oder Selbstbelastungsrisiko und benoetigt anwaltlichen Beistand. § 68b StPO Zeugenbeistand, § 55 StPO Auskunftsverweigerungsrecht, § 52 StPO Zeugnisverweigerungsrecht. Prüfraster Auskunftsverweigerungsrecht nach § 55 prüfen, Schutz vor Selbstbelastung, Zeugen-Aussage vorbereiten oder Aussage verweigern, Beistand aktiv ausüben. Output Strategie-Memo für Zeugenbeistand mit Aussagepfaden und Verweigerungs-Optionen. Abgrenzung zu Erstgespraeach für Beschuldigte und zu Nebenklage.

# Zeugenbeistand im Strafverfahren

## Kernsachverhalt & Mandantenfragen

Der Zeugenbeistand ist die anwaltliche Begleitperson eines Zeugen – nicht des Beschuldigten. Die Rolle ist strukturell eigenstaendig: Der Beistand berät den Zeugen, darf aber nicht den Verfahrensverlauf lenken wie ein Verteidiger. Mandantinnen und Mandanten verstehen diese Unterscheidung selten.

**8 Kaltstart-Rückfragen:**

1. Haben Sie eine Ladung erhalten und von wem (Polizei, Staatsanwaltschaft, Gericht)? Bitte Ladungsschreiben vorlegen.
2. Sind Sie selbst beschuldigt oder verdaechtig in derselben Sache oder einer verwandten Sache?
3. Sind Sie mit der/dem Beschuldigten verwandt, verschwägert, verlobt oder verheiratet?
4. Üben Sie einen Beruf aus, der eine gesetzliche Schweigepflicht begründet (Arzt, Rechtsanwalt, Steuerberater, Pfarrer, Psychotherapeut)?
5. Sind Sie Beamter oder Angestellter des öffentlichen Dienstes und benötigen Sie eine Aussagegenehmigung Ihres Dienstherrn?
6. Wurden Ihnen Drohungen gemacht oder fühlen Sie sich durch das Umfeld der/des Beschuldigten gefährdet?
7. Sind Sie zugleich Verletzte/r der dem Verfahren zugrundeliegenden Tat?
8. Haben Sie bereits Angaben gegenüber der Polizei gemacht und wenn ja, in welchem Umfang?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 48 StPO | Pflicht zur Aussage; grundsätzliche Erscheinens- und Aussagepflicht des Zeugen |
| § 52 StPO | Zeugnisverweigerungsrecht der Angehörigen (Ehegatten, Verwandte gerader Linie, Seitenlinie bis 3. Grad) |
| § 53 StPO | Zeugnisverweigerungsrecht der Berufsgeheimnisträger (Ärzte, Anwälte, Steuerberater, Geistliche u.a.) |
| § 53a StPO | Zeugnisverweigerungsrecht beruflicher Gehilfen (z.B. Rechtsanwaltsfachangestellte) |
| § 54 StPO | Aussagegenehmigung für Amtsträger; Versagung mit Begruendungspflicht |
| § 55 StPO | Auskunftsverweigerungsrecht bei Selbstbelastungsgefahr (einzelne Fragen oder ganze Aussage) |
| § 68 StPO | Vernehmung zur Person; Adressanonymisierung Abs. 2 und Abs. 3 |
| § 68a StPO | Beschränkung ehrenrühriger Fragen |
| § 68b StPO | Anwaltlicher Beistand des Zeugen; Beiordnung Abs. 2 bei Schutzbedürftigkeit |
| § 70 StPO | Zwangsmittel bei unberechtigter Zeugnisverweigerung (Ordnungsgeld, Erzwingungshaft) |
| § 97 StPO | Beschlagnahmeverbot bei Berufsgeheimnissen |
| § 136a StPO | Verbotene Vernehmungsmethoden (analog für Zeugen) |
| § 161a StPO | Vernehmung von Zeugen durch die Staatsanwaltschaft |
| § 163a StPO | Vernehmung durch die Polizei |
| § 247 StPO | Entfernung des Angeklagten bei Zeugenvernehmung (Schutzvorschrift) |
| § 406e StPO | Akteneinsicht für Verletzte (analog für Zeugenbeistand anerkannt) |

---

## Leitentscheidungen

| Aktenzeichen | Gericht / Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

---

## Prüfschema Zeugenbeistand

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Ladung prüfen: Wer lädt (Polizei/StA/Gericht)? Verfahrensstadium? Beweisthema? | § 48, § 161a, § 163a StPO |
| 2 | Zeugnisverweigerungsrecht § 52 StPO: Angehörigeneigenschaft prüfen (Ehe, Verwandtschaft, Lebenspartnerschaft) | § 52 StPO |
| 3 | Zeugnisverweigerungsrecht § 53 StPO: Berufsgeheimnisträger? Entbindungserklärung vorhanden? | § 53, § 53a StPO |
| 4 | Aussagegenehmigung § 54 StPO: Amtsträger? Genehmigung erteilt oder beantragt? | § 54 StPO |
| 5 | Auskunftsverweigerungsrecht § 55 StPO: Welche Fragen beinhalten Selbstbelastungsgefahr? Einzelfragen oder gesamte Aussage betroffen? | § 55 StPO |
| 6 | Akteneinsicht beantragen (analog § 406e StPO oder über § 475 StPO) | § 406e, § 475 StPO |
| 7 | Beiordnungsantrag § 68b Abs. 2 StPO prüfen: Schutzbedürftigkeit, Minderjährigkeit, Gefährdungslage, Verbindung zu Organisierter Kriminalität | § 68b Abs. 2 StPO |
| 8 | Adressanonymisierung § 68 Abs. 2/3 StPO prüfen: Stalking, häusliche Gewalt, Zeugenschutzbedarf | § 68 StPO |
| 9 | Aussage-Chronologie mit Mandantschaft erarbeiten: Was weiß sie/er und aus welcher Quelle? Erinnerungslücken offen lassen | § 68b StPO |
| 10 | Schriftliche Mandantenbelehrung über Rechte (§§ 52, 55 StPO) und Pflichten (§ 48 StPO) | § 48, § 52, § 55 StPO |
| 11 | Vernehmungsbegleitung: Anwesenheit, Wortmeldungsrecht; Schutz vor § 136a-StPO-Methoden; Pausenanträge bei § 55-Konstellationen | § 68b StPO |
| 12 | Protokollkontrolle: Richtigkeit und Vollständigkeit; ggf. Berichtigungsantrag | § 168 S. 2 StPO |
| 13 | Nachbereitung: Zeugen-Memo, Prüfung weiterer Schritte (Beschwerde, Strafanzeige bei Druckausübung) | §§ 162, 306 StPO |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Zeugen-Beistand | Zeugenbeistand-Protokoll; Template unten |
| Variante A — Zeuge wird Beschuldigter | Sofort Aussageverweigerung; Mandatsumwandlung |
| Variante B — Zeuge im Ausland | Internationale Rechtshilfe; Aussagepflicht pruefen |
| Variante C — Behoedenzeuge (Beamter) | Aussagegenehmigung Dienststelle; Amtsgeheimnis |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 – Beiordnungsantrag § 68b Abs. 2 StPO

```
An das [Gericht / Staatsanwaltschaft]
Aktenzeichen: [...]

Antrag auf Beiordnung als anwaltlicher Zeugenbeistand
gemäß § 68b Abs. 2 StPO

In der Strafsache gegen [Name Beschuldigte/r]
zeige ich die anwaltliche Vertretung der Zeugin / des Zeugen
[Name, Geburtsdatum, Anschrift]
an.

Ich beantrage, mich als anwaltlichen Beistand der Zeugin / des Zeugen
gemäß § 68b Abs. 2 StPO beizuordnen.

Begründung:
Die Beiordnung ist erforderlich, weil [konkret: z.B.
"die Zeugin minderjährig und einem erheblichen Drohungsdruck
durch den Beschuldigten ausgesetzt ist; es liegen Erkenntnisse
vor, dass der Beschuldigte über Mittelsleute Einfluss auf
das Aussageverhalten ausübt (dokumentiert durch SMS-Nachrichten
vom [Datum], Anlage 1)"].

Die Vernehmung ist für den [Termin] vor [Behörde/Gericht]
angesetzt.

[Ort, Datum]
[Unterschrift, Kanzlei]
```

### Baustein 2 – Erklärung Auskunftsverweigerungsrecht § 55 StPO

```
An den/die Vernehmungsbeamten/-beamtin / Vorsitzenden
[Behörde / Gericht]

In der Vernehmung der Zeugin / des Zeugen [Name]
am [Datum], Aktenzeichen [...]

Erklärung gemäß § 55 StPO

Ich erkläre namens und in Vollmacht der Zeugin / des Zeugen
[Name]:

Auf die Frage [ggf. konkrete Frage nennen oder: "betreffend
den Sachverhaltskomplex X"] verweigert die Zeugin / der Zeuge
die Auskunft gemäß § 55 StPO.

Die wahrheitsgemäße Beantwortung würde die Zeugin / den Zeugen
der Gefahr aussetzen, wegen einer Straftat verfolgt zu werden
(§ 55 Abs. 1 StPO). Eine Belehrung gemäß § 55 Abs. 2 StPO
ist [nicht] erfolgt.

Soweit die Vernehmungsperson die Berechtigung dieser
Verweigerung bezweifelt, beantrage ich die Entscheidung
des zuständigen Richters (§ 55 Abs. 2 S. 3 StPO).

[Ort, Datum]
[Unterschrift]
```

### Baustein 3 – Akteneinsichtsantrag (Zeugenbeistand, analog § 406e StPO)

```
An die Staatsanwaltschaft [...]
Aktenzeichen: [...]

Antrag auf Akteneinsicht gemäß § 406e StPO (analog) /
§ 475 StPO

Ich zeige die anwaltliche Vertretung der Zeugin / des Zeugen
[Name] an.

Ich beantrage Einsicht in die Verfahrensakte, insbesondere:
- Anklageschrift / Eröffnungsbeschluss
- Vernehmungsprotokolle
- Sachverständigengutachten
- [weitere konkrete Unterlagen]

Das berechtigte Interesse ergibt sich aus der bevorstehenden
Zeugenvernehmung am [Termin]. Eine sachgerechte Vorbereitung
ist ohne Kenntnis des Verfahrensstands und der bereits vor-
Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

[Ort, Datum]
[Unterschrift]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Berechtigung zur Zeugnisverweigerung § 52 StPO | Zeugin/Zeuge behauptet Angehörigeneigenschaft; Gericht prüft von Amts wegen, ggf. eidesstattliche Erklärung |
| Auskunftsverweigerungsrecht § 55 StPO | Zeugin/Zeuge muss Verfolgungsgefahr glaubhaft machen; keine volle Beweispflicht, aber substantiiertes Vorbringen |
| Beiordnung § 68b Abs. 2 StPO | Antragstellerin/Antragsteller trägt Schutzbedürftigkeit vor; Gericht entscheidet nach freiem Ermessen |
| Beschlagnahmeverbot § 97 StPO | Beschuldigtenverteidigung trägt Schutzwürdigkeit vor; Staatsanwaltschaft muss keine Ausnahme beweisen |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Sofort | Beiordnungsantrag vor Vernehmungstermin stellen | § 68b Abs. 2 StPO |
| 2 Wochen | Beschwerde gegen Ablehnung der Beiordnung (§ 306 StPO) | § 311 StPO |
| Vor Aussage | Akteneinsicht rechtzeitig beantragen; Reaktionszeit der Behörde einplanen (3–5 Tage bei StA) | § 406e StPO |
| Sofort in der Vernehmung | § 55-Erklärung muss vor der strittigen Antwort abgegeben werden, nicht nachträglich | § 55 StPO |
| 1 Woche nach Vernehmung | Protokollberichtigung beantragen, wenn Fehler vorliegen | § 168 S. 2 StPO |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Die Zeugin muss aussagen, § 48 StPO gilt uneingeschränkt" | § 48 StPO begründet Pflicht, enthält aber keine Aussagepflicht bei Verweigerungsrechten; §§ 52, 53, 55 StPO gehen als lex specialis vor |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Zeugenbeistand darf nicht sprechen" | § 68b Abs. 1 S. 2 StPO erlaubt Beanstandungen; bei Beiordnung auch Erklärungen; BGH hat Erklärungsrecht bestätigt |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Adressanonymisierung ist unverhältnismäßig" | § 68 Abs. 3 StPO erfordert nur drohende Gefahr, nicht bereits eingetretene Schädigung; pauschal aber unzureichend |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Wahlmandat Zeugenbeistand | RVG Teil 4 (analog Verteidigergebühren VV 4100 ff.); Mittelgebühr nach Aufwand |
| Beiordnung § 68b Abs. 2 StPO | Pflichtverteidigergebühren nach VV-RVG; Kostentragung durch Staatskasse |
| Akteneinsicht als Nebenleistung | keine gesonderte Gebühr; im Verfahrensgebühren-Rahmen enthalten |
| Mehrere Vernehmungstermine | Terminsgebühr je Termin (VV 4102/4103 je nach Gericht/Behörde) |
| Beschwerdeverfahren | eigenständige Verfahrens- und Terminsgebühr nach Teil 4 VV-RVG |

---

## Typische Konstellationen im Detail

### Konstellation A: Familienmitglied als Zeuge gegen Angehörigen

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

### Konstellation B: Mit-Beschuldigter als Zeuge im Parallelverfahren

Höchste Vorsicht: § 55 StPO greift für jede einzelne Frage. Vorher Akteneinsicht in Parallelverfahren beantragen. Aussage mit eigener Strafverteidigungsstrategie abstimmen. Beiordnung nach § 68b Abs. 2 StPO beantragen. Bei Kollision Zeugenbeistand/Verteidigung: § 146 StPO beachten – zwei getrennte Mandate.

### Konstellation C: Berufsgeheimnisträger (Arzt, Anwalt, Steuerberater)

Prüfen, ob Entbindungserklärung des Mandanten/Patienten vorliegt. Ohne Entbindung: § 53 StPO geltend machen. Bei Sicherstellung von Unterlagen: § 97 StPO Beschlagnahmeverbot prüfen (nur greift wenn Zeuge selbst nicht verdächtig). Bei vorliegender Entbindung: Aussage auf gedeckten Umfang beschränken; keine freiwillige Ausweitung.

### Konstellation D: Zeuge in Wirtschaftsstrafverfahren

§ 55 StPO regelmäßig einschlägig. Compliance-Untersuchungen (Internal Investigations) vorab analysieren: Verwertungsverbote nach sog. Mannheimer Modell prüfen. Geschäftsgeheimnisse: § 53 StPO greift nur für Berufsgeheimnisträger, nicht pauschal für Unternehmensgeheimnisse. Sicherstellungen nach § 94 StPO im Vorfeld der Vernehmung sind häufig; Beschlagnahmeverbot § 97 StPO prüfen.

### Konstellation E: Whistleblower / Hinweisgeber

HinSchG-Schutz prüfen (Hinweisgeberschutzgesetz 2023). Identitätsschutz und Adressanonymisierung § 68 Abs. 2/3 StPO. Beiordnung § 68b Abs. 2 StPO mit Schutzbedürftigkeit begründen. Repressalienschutz dokumentieren (Art. 19 HinSchG: Verbot der Benachteiligung).

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Zeugin hat keine Kenntnisse von der Tat | Offene, ehrliche Aussage mit Begleitung; kein Schweigen ohne Grund (Glaubwürdigkeitsrisiko) |
| Zeugin könnte sich selbst belasten | § 55 StPO konsequent einsetzen; Akteneinsicht vor Aussage zwingend |
| Angehörige/r ist zeugnisverweigerungsberechtigt | Entscheidung ausführlich besprechen; emotionale und strategische Aspekte abwägen; schriftlich dokumentieren |
| Gefährdungslage vorhanden | Adressanonymisierung § 68 StPO + Beiordnung § 68b Abs. 2 StPO gleichzeitig beantragen |
| Amtsträger ohne Genehmigung | Aussage verweigern bis Genehmigung vorliegt; Rechtsweg gegen Versagung (§ 54 Abs. 3 StPO) |
| Zeuge ist auch Verletzter | Nebenklage prüfen; doppelte Mandat-Führung (Zeugenbeistand + Nebenklage) möglich, aber klar trennen |

---

## Anschluss-Skills

- `fachanwalt-strafrecht-nebenklage-opfervertretung` – wenn Zeuge zugleich Verletzter ist
- `fachanwalt-strafrecht-adhaesionsverfahren` – wenn Verletzter zivilrechtliche Ansprüche geltend macht
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` – bei Wirtschaftsstrafverfahren mit Vermögensbezug
- `plaedoyer-vorbereitung-strafverteidigung` – Hauptverhandlungsbegleitung nach Anschluss als Nebenklage

---

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 6. `mandat-triage-strafrecht`

**Frühere Beschreibung:** Strukturierte Eingangs-Abfrage für Strafmandate. Klaert Verfahrensstadium (Ermittlungs- Zwischen- Hauptverfahren Vollstreckung) Tatvorwurf nach Strafrahmen (Vergehen Verbrechen) Haftsituation (Untersuchungshaft Vollzug Hausverbot) Beschuldigtenrechte § 136 § 137 § 140 § 141 StPO Pflichtverteidiger-Bestellung Mitbeschuldigte (Konflikt-Check § 43a BRAO § 146 StPO). Sofort-Fristen-Check Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Akteneinsicht § 147 StPO, Rechtsmittel und U-Haft-Eskalation. Routing zu Akteneinsicht, Haftmanagement und Strafprozess-Cockpit.

# Mandat-Triage Strafrecht

## Zweck

Erstkontakt im Strafverfahren — oft mit hoher Eilbedürftigkeit (Festnahme U-Haft Durchsuchung). Strukturierte Triage stellt rechtliche und kommunikative Priorität sicher.

## Ablauf — acht Fragen

### Frage 1 — Wer ruft an und für wen?

- Beschuldigter selbst
- Angehöriger
- Polizei (selten — Notdienst)
- Anderer Anwalt (Vertretung)

### Frage 2 — Akute Eilbedürftigkeit?

- Festnahme erfolgt — Vorführung läuft heute
- Untersuchungshaft seit Stunden / Tagen
- Durchsuchung läuft / steht bevor
- Aussage bei Polizei für heute terminiert
- Hauptverhandlung beginnt morgen

**Eskalation:** Festnahme U-Haft Durchsuchung → Telefon-Sofort an Anwalt; binnen einer Stunde Beistand; Anwesenheit bei Vernehmung Pflicht.

### Frage 3 — Verfahrensstadium?

- Ermittlungsverfahren bei Polizei (kein Aktenzeichen StA noch nicht)
- Ermittlungsverfahren bei Staatsanwaltschaft (Az StA vorhanden)
- Zwischenverfahren (Anklage zugestellt — Eröffnungsbeschluss?)
- Hauptverfahren (Hauptverhandlungstermin)
- Berufung / Revision
- Strafvollstreckung
- Strafvollzug (Vollzugsplan Lockerungen Strafaussetzung)

### Frage 4 — Tatvorwurf?

- Norm (§ ggf. StGB Nebengesetz)
- Strafrahmen — Vergehen unter ein Jahr Vergehen ab ein Jahr Verbrechen ab ein Jahr Mindeststrafe (§ 12 StGB)
- Bei Verbrechen oder Strafrahmen ab ein Jahr — notwendige Verteidigung § 140 StPO

### Frage 5 — Haftsituation?

- In Freiheit
- Vorgeführt — Vorführungsbeschluss / Haftbefehl?
- Untersuchungshaft — Haftgründe (Flucht-, Verdunkelungs-, Wiederholungs-)
- Strafvollzug

### Frage 6 — Mitbeschuldigte?

- Wer ist mitbeschuldigt?
- Ist Mitbeschuldigter bereits anwaltlich vertreten?
- Konflikt-Check § 43a Abs. 4 BRAO § 146 StPO Mehrfachverteidigung verboten

### Frage 7 — Aktenstand?

- Aktenstand nachgefragt?
- Akteneinsicht beantragt § 147 StPO
- Bei U-Haft haftrelevante Informationen nach § 147 Abs. 2 S. 2 StPO sichern; in der Regel Akteneinsicht

### Frage 8 — Wirtschaftliche Verhältnisse / Pflichtverteidigung?

- Pflichtverteidigung § 140 § 141 StPO bei notwendiger Verteidigung
- Vergütung nach RVG plus eventuell Honorarvereinbarung

## Routing-Matrix

| Verfahrensstadium | Folge-Skill | Frist-Sofort-Check |
|---|---|---|
| U-Haft | `strafprozess-haft-und-besuchsmanagement` | Haftprüfung § 117 StPO, Haftbeschwerde § 304 StPO, Sechs-Monats-Kontrolle § 121 StPO |
| Vorfeld Durchsuchung | Beschwerde § 304 StPO | ggf. nicht statthaft wenn beendet — Feststellungsantrag |
| Polizei-Vernehmung steht an | Verteidigerbeistand § 168c StPO | Termin verlegen oder begleiten |
| Anklage zugestellt | Stellungnahme zur Eröffnung | Frist nach § 201 StPO |
| Anzeige/Anklage § 188 StGB | `strafrecht-spezial-188-stgb-easy-verteidigung` | Strafantrag/besonderes öffentliches Interesse § 194 StGB, vollständiger Äußerungskontext, Art. 5 GG |
| Strafbefehl § 188 StGB | `strafrecht-spezial-188-stgb-anklage-und-strafbefehl` | Einspruch § 410 StPO binnen zwei Wochen ab Zustellung |
| Hauptverhandlung | `akteneinsicht-strafrecht-auswerten` | Beweisanträge vor Schluss Beweisaufnahme |
| Berufung/Revision | `strafprozess-rechtsmittel-und-notfristencockpit` | Berufung/Revision Einlegung binnen 1 Woche; Revisionsbegründung § 345 StPO gesondert berechnen |

## Konflikt-Check

- Mehrfachverteidigung verboten § 146 StPO
- § 43a Abs. 4 BRAO Interessenkollision
- Frühere Vertretung von Mitbeschuldigtem oder Geschädigtem prüfen

## Sofort-Fristen

- **Haftprüfung** § 117 Abs. 1 StPO — jederzeit
- **Haftbeschwerde** § 304 StPO — keine gesetzliche Wochenfrist wie bei sofortiger Beschwerde, aber praktisch sofort vorbereiten
- **Sechs-Monats-Prüfung** OLG § 121 StPO
- **Einspruch Strafbefehl** § 410 StPO zwei Wochen
- **Berufung** § 314 StPO eine Woche
- **Revision** § 341 StPO eine Woche; Revisionsbegründung § 345 StPO grundsätzlich ein Monat nach Ablauf der Einlegungsfrist, bei späterer Urteilszustellung ab Zustellung

## Eskalationspfad

- **Telefon-Sofort** Vorführung Untersuchungshaft Durchsuchung Vernehmung-Termin heute
- **Binnen einer Stunde** Anfahrt zur Vernehmung — Verteidigerbeistand
- **Heute** Akteneinsichtsantrag § 147 StPO, Haftprüfung § 117 StPO oder Haftbeschwerde § 304 StPO prüfen
- **Diese Woche** Stellungnahme Anklage Berufungseinlegung

## Ausgabe

- `triage-protokoll-strafrecht.md` mit acht Fragen
- Aktenanlage Az-Vorschlag
- Fristenbuch-Eintrag (Hauptfrist Vorfrist)
- Mandatsvereinbarung Vorlage mit Pflichtverteidigerbestellungs-Antrag falls notwendig
- Empfehlung Folge-Skill plus Begründung

## Quellen

- StPO §§ 117 121 137 140 141 146 147 168c 201 304 314 341 410
- StGB § 12 (Verbrechen-Vergehen)
- BRAO § 43a
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aktuelle Rechtsprechung Mandat-Triage

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Normen Triage-Check

- § 112 StPO — Haftbefehl (Flucht-, Verdunkelungs-, Wiederholungsgefahr)
- § 117 StPO — Haftpruefungsantrag (jederzeit)
- § 118a StPO — Haftpruefungstermin mit muendlicher Verhandlung
- § 140 StPO — notwendige Verteidigung (Bestellungsgrunde)
- § 141 StPO — Pflichtverteidiger-Bestellung (Zeitpunkt, Ablauf)
- § 146 StPO — Verbot Mehrfachverteidigung
- §§ 10 ff. GwG — Identifizierungspflichten Sorgfaltspflichten Rechtsanwalt

## 7. `plaedoyer-vorbereitung-strafverteidigung`

**Frühere Beschreibung:** Plaedoyer für Strafverteidigung vorbereiten und strukturieren: Anwendungsfall nach Abschluss der Beweisaufnahme muss Strafverteidiger Schlusspledoyer mit Schuldfrage Strafzumessung und Verfahrenshindernissen vorbereiten. § 258 StPO Schlusspledoyer, § 46 StGB Strafzumessung, § 261 StPO freie Beweiswürdigung. Prüfraster Schuldfrage anhand Beweisaufnahme, Beweiswürdigungs-Angriff, Strafzumessung Milderungsgründe, Verfahrenshindernisse. Output Plaedoyer-Gliederung mit Kernargumentation und Antragsformulierungen. Abgrenzung zu Hauptverhandlung-Vorbereiten für Gesamtvorbereitung und zu Schriftsatzkern.

# Plädoyer-Vorbereitung Strafverteidigung

## Kernsachverhalt & Mandantenfragen

Das Plädoyer ist der letzte große Auftritt der Verteidigung in der Hauptverhandlung. Es fasst Beweiswürdigung und Rechtslage zusammen – und muss klar, strukturiert und überzeugend sein. Verteidigerinnen und Verteidiger, die das Plädoyer nicht vorbereiten, verschenken wesentliches Strafminderungspotenzial.

**8 Kaltstart-Rückfragen:**

1. Was ist der genaue Tatvorwurf und welcher Straftatbestand liegt der Anklage zugrunde?
2. Welches Verteidigungsziel ist vereinbart: Freispruch (Tatbestand verneinend oder Rechtfertigung), milderer Schuldspruch, Bewährungsstrafe oder Mindeststrafe?
3. Welche Beweise hat die Staatsanwaltschaft in der Hauptverhandlung eingeführt (Zeugen, Sachverständige, Urkunden, Geständnis)?
4. Liegen Verwertungsverbote vor (Durchsuchung ohne richterliche Anordnung, Belehrungsmangel, verbotene Vernehmungsmethoden)?
5. Hat der/die Angeklagte ein Geständnis abgelegt oder bestreitet er/sie den Tatvorwurf vollständig?
6. Sind Hilfsbeweisanträge noch offen oder müssen sie vor dem Plädoyer gestellt werden?
7. Welche Strafzumessungsargumente stehen zur Verfügung (Geständnis, Schadenswiedergutmachung, Erstmaligkeit, Familie)?
8. Besteht die Möglichkeit einer Verständigung nach § 257c StPO oder ist das Plädoyer ohne Absprache zu halten?

---
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Rechtsgrundlagen

| Norm | Inhalt |
|---|---|
| § 258 StPO | Schlussvorträge; Reihenfolge: StA – Nebenklage – Verteidigung; letztes Wort des Angeklagten Abs. 3 |
| § 244 StPO | Beweisaufnahme; Ablehnungsgründe für Beweisanträge (Abs. 3–6) |
| § 257 StPO | Erklärungsrecht nach Beweisaufnahme |
| § 257c StPO | Verständigung im Strafverfahren |
| § 136a StPO | Verbotene Vernehmungsmethoden; absolutes Verwertungsverbot |
| § 344 StPO | Revisionsbegründung; Verfahrensrüge und Sachrüge |
| § 20 StGB | Schuldunfähigkeit; Voraussetzungen und Folgen |
| § 21 StGB | Verminderte Schuldfähigkeit; Strafrahmenverschiebung nach § 49 StGB |
| § 22 StGB | Versuch; Definition |
| § 23 StGB | Strafbarkeit und Strafrahmenmilderung beim Versuch (Abs. 2) |
| § 24 StGB | Rücktritt vom Versuch; Straflosigkeit |
| § 32 StGB | Notwehr |
| § 34 StGB | Rechtfertigender Notstand |
| § 35 StGB | Entschuldigender Notstand |
| § 46 StGB | Strafzumessung: Grundsätze und Gesichtspunkte |
| § 46a StGB | Täter-Opfer-Ausgleich als Strafmilderungsgrund |
| § 49 StGB | Mildernde Umstände; Strafrahmenverschiebung (Abs. 1 und Abs. 2) |
| § 52 StGB | Tateinheit (Idealkonkurrenz) |
| § 53 StGB | Tatmehrheit (Realkonkurrenz) |
| § 56 StGB | Strafaussetzung zur Bewährung |

---

## Leitentscheidungen

| Aktenzeichen | Gericht / Datum | Leitsatz |
|---|---|---|
| Rechtsprechung live prüfen | Live-Verifikation erforderlich | keine Entscheidung aus Modellwissen zitieren; vor Ausgabe offizielle oder frei zugängliche Quelle mit Gericht, Datum, Aktenzeichen und Aussage protokollieren |

---

## Prüfschema Plädoyervorbereitung

| Schritt | Inhalt | Grundlage |
|---|---|---|
| 1 | Hilfsbeweisanträge prüfen: Noch offene Beweisfragen vor Schluss der Beweisaufnahme sichern; ggf. Ablehnung als Revisionsstoff | § 244 StPO |
| 2 | Verfahrensrügen dokumentieren: Verstöße gegen StPO während HV notieren; Formalvoraussetzungen prüfen | § 344 StPO |
| 3 | Beweisaufnahme-Protokoll auswerten: Widersprüche in Zeugenaussagen, Inkonsistenzen zwischen Polizeiprotokoll und HV-Aussage | § 261 StPO |
| 4 | Verwertungsverbote prüfen: § 136a StPO (verbotene Methoden), § 100a StPO (TKÜ ohne Voraussetzungen), § 105 StPO (Durchsuchung ohne richterliche Anordnung) | §§ 136a, 100a, 105 StPO |
| 5 | Tatbestand subsumieren: Objektiver Tatbestand (Handlung, Erfolg, Kausalität, objektive Zurechnung); Subjektiver Tatbestand (Vorsatz, Fahrlässigkeit) | Einschlägige §§ StGB |
| 6 | Rechtfertigung/Entschuldigung prüfen: Notwehr § 32, Notstand §§ 34/35, Einwilligung, Erlaubnisirrtum | §§ 32, 34, 35 StGB |
| 7 | Schuldfähigkeit prüfen: § 20 StGB (Ausschluss), § 21 StGB (Verminderung); psychiatrisches Gutachten auswerten | §§ 20, 21 StGB |
| 8 | Versuch/Vollendung prüfen: Versuch nach § 22 StGB; Strafrahmenverschiebung § 23 Abs. 2 i.V.m. § 49 Abs. 1 StGB; Rücktritt § 24 StGB | §§ 22–24, 49 StGB |
| 9 | Konkurrenzen prüfen: Tateinheit § 52 oder Tatmehrheit § 53 StGB; Gesetzeskonkurrenz (Spezialität, Subsidiarität, Konsumtion) | §§ 52, 53 StGB |
| 10 | Strafzumessung vorbereiten: Strafrahmen feststellen; Verschiebung nach § 49 StGB einbeziehen; Zumessungsgesichtspunkte nach § 46 Abs. 2 StGB sammeln | §§ 46, 49 StGB |
| 11 | Bewährungsvoraussetzungen prüfen: § 56 StGB – Straferwartung unter 2 Jahre; positive Sozialprognose; ggf. besondere Umstände § 56 Abs. 2 StGB | § 56 StGB |
| 12 | Plädoyerstruktur erstellen: Eröffnung (Sachverhalt aus Verteidigersicht), Beweiswürdigung (Zeugenkritik), Rechtliche Würdigung (Subsumtion), Strafzumessung | § 258 StPO |
| 13 | Letztes Wort vorbereiten: Mandant über Inhalt und Wirkung aufklären; Reue, Entschuldigung, Sachverhalt – auf Plädoyer abstimmen | § 258 Abs. 3 StPO |
| 14 | Revisions-Rügeliste finalisieren: Verfahrensrügen geordnet nach Schluss der HV; Fristenkontrolle Revisionsbegründung (1 Monat) | § 344 StPO, § 345 StPO |

---

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — Plaedoyer Strafverteidigung vorbereiten | Plaedoyerstruktur; Template unten |
| Variante A — Verstaendigung nach § 257c StPO | Absprachen-Plaedoyer; andere Argumentation |
| Variante B — Freispruch angestrebt | Beweis-Plaedoyer; jede Anklage-Schwaeche herausarbeiten |
| Variante C — Strafmass streitig | Strafzumessungs-Plaedoyer; § 46 StGB-Aspekte |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.


## Schriftsatzbausteine

### Baustein 1 – Plädoyerstruktur (Muster-Gliederung)

```
PLÄDOYER
Strafsache gegen [Name]
Aktenzeichen: [...]
Hauptverhandlung am [Datum]

I. ERÖFFNUNG
   Zusammenfassung des Sachverhalts aus Verteidigersicht.
   "Was ist in dieser Sache tatsächlich passiert?"

II. BEWEISWÜRDIGUNG – TATSÄCHLICHES
   A. Zeugenaussagen
      - Zeuge X: Widerspruch zwischen polizeilicher Vernehmung
        vom [Datum] (Protokoll Bl. [X]) und HV-Aussage am
        [Datum]; Aussage daher nicht glaubwürdig.
      - Zeuge Y: Eigeninteresse; Vorwurf von [Datum].
   B. Sachverständigengutachten
      - Methode anerkannt? Anknüpfungstatsachen vollständig?
      - Gegen-Auslegung möglich?
   C. Verwertungsverbote
      - Beschlagnahme vom [Datum]: ohne richterliche Anordnung
        (§ 105 StPO); Beweisverwertungsverbot geltend machen.

III. RECHTLICHE WÜRDIGUNG
   A. Tatbestand
      - Objektiver Tatbestand: [Handlung X] führte nicht zu
        [Erfolg Y]; Kausalität fehlt / obj. Zurechnung ausgeschlossen.
      - Subjektiver Tatbestand: Vorsatz nicht nachgewiesen.
   B. Schuldfähigkeit / Versuch / Konkurrenzen
      - [Ggf. § 21 StGB; § 23 Abs. 2 StGB; § 52 StGB.]

IV. STRAFZUMESSUNG (hilfsweise)
   Strafrahmen: § [X] StGB: [Mindeststrafe] bis [Höchststrafe].
   Strafmilderung:
   - Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
   - Erstmals straffällig
   - Schadenswiedergutmachung: [Betrag EUR] bereits geleistet
   - Familie: [X] Kinder, Alleinverdiener
   - Lange Verfahrensdauer: [X] Jahre; Belastung für Mandanten

V. BEWÄHRUNG (§ 56 StGB)
   Sozialprognose positiv: keine Vorstrafen, stabiles Umfeld,
   Arbeitsstelle gesichert, Wohnverhältnisse geordnet.

VI. ANTRAG
   Ich beantrage, [Name] vom Vorwurf der [Straftat]
   freizusprechen / zu einer Freiheitsstrafe von [X] Monaten
   auf Bewährung zu verurteilen.
```

### Baustein 2 – Hilfsbeweisantrag (vor Schluss der Beweisaufnahme)

```
An den Vorsitzenden
Aktenzeichen: [...]

Hilfsbeweisantrag gemäß § 244 Abs. 3 StPO

In der Hauptverhandlung gegen [Name] beantrage ich
hilfsweise für den Fall, dass das Gericht von einer
Verurteilung wegen [Tatbestand] ausgeht:

Beweis darüber, dass [Beweisbehauptung], durch Einvernahme
des Zeugen [Name, Anschrift] / Einholung eines Sachverstän-
digengutachtens des [Institut/Sachverstand].

Das Beweismittel ist erheblich, weil [Begründung].

Eine Ablehnung wäre rechtsmittelrelevant (§ 344 StPO).

[Ort, Datum]
[Unterschrift]
```

### Baustein 3 – Memo letztes Wort des Angeklagten

```
VORBEREITUNG LETZTES WORT
(Vertraulich – Anwalt-Mandant-Gespräch)

Empfehlung für Inhalt des letzten Wortes:

1. Reue / Entschuldigung:
   Falls Geständnis oder Teilgeständnis: Kurze ehrliche
   Entschuldigung gegenüber dem Gericht und ggf. der Verletzten.
   Nicht ausschweifend – Glaubwürdigkeit durch Kürze.

2. Sachverhaltshinweise:
   Nur wenn Plädoyer und letztes Wort koordiniert:
   "Ich möchte noch einmal betonen, dass ich nie die Absicht
   hatte, [Person X] zu schädigen."

3. Persönliche Situation:
   Kurz: Familie, Arbeit, Therapie, Wiedergutmachung.

4. Was NICHT sagen:
   – Schuldzuweisung an Zeugen oder Opfer
   – Rechtsmittelankündigung
   – Lange Stellungnahmen zur Rechtslage (das ist Sache der Verteidigung)

Timing: Kurz (1–3 Minuten). Wirkung: Menschlichkeit zeigen.
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

---

## Beweislast

| Konstellation | Beweislast |
|---|---|
| Tatnachweis | Staatsanwaltschaft trägt volle Beweislast; in dubio pro reo bei Zweifeln |
| Schuldunfähigkeit § 20 StGB | Im Strafverfahren: Gericht prüft von Amts wegen; Gutachten erforderlich; Zweifel gehen zu Lasten der Anklage |
| Notwehr § 32 StGB | Angeklagte/r muss Notwehrlage behaupten; StA muss Überschreitung beweisen |
| Rücktritt § 24 StGB | Angeklagte/r trägt Freiwilligkeit des Rücktritts; Zweifelssatz gilt |
| Verwertungsverbot | Verteidigung muss Verfahrensverstoß konkret rügen; Gericht prüft dann von Amts wegen |

---

## Fristen und Verjährung

| Frist | Inhalt | Norm |
|---|---|---|
| Vor Schluss der Beweisaufnahme | Hilfsbeweisanträge stellen | § 244 StPO |
| 1 Woche nach Urteilsverkündung | Revision einlegen (Einlegungsfrist) | § 341 StPO |
| 1 Monat nach Urteilszustellung | Revisionsbegründungsfrist; Verfahrensrügen müssen vollständig sein | § 345 StPO |
| Laufend | Verfahrensrügen in der HV protokollieren lassen | § 344 StPO |
| Je nach Delikt | Strafverfolgungsverjährung (§ 78 StGB): 3 Jahre (leichte Delikte) bis 30 Jahre (Mord) | § 78 StGB |

---

## Typische Gegenargumente

| Gegenargument | Erwiderung |
|---|---|
| "Geständnis wurde freiwillig abgelegt" | § 136a StPO prüfen; Geständnis nach langer Vernehmung ohne Pause, unter psychischem Druck oder nach falscher Versprechung kann Verwertungsverbot begründen |
| "Zeuge ist glaubwürdig, kein Grund zur Zweifel" | Methodische Glaubwürdigkeitsprüfung: Konstanz (Aussage-Polizei vs. HV), Detailreichtum, Eigeninteresse; BGH-Maßstäbe (BGH NStZ 2007, 112) |
| Rechtsprechung live prüfen | keine Entscheidung aus Modellwissen; Quelle vor Ausgabe protokollieren |
| "Keine Revision möglich, da Berufungsurteil" | § 333 StPO erlaubt Revision auch gegen Berufungsurteile; Verfahrensrügen aus der Berufungsverhandlung sind rügefähig |

---

## Streitwert / Kosten

| Position | Berechnung |
|---|---|
| Hauptverhandlungsgebühr | VV-RVG Nr. 4112 (Verfahrensgebühr) + Nr. 4114/4115 (Terminsgebühr je Sitzungstag) |
| Mehrtägige HV | Erhöhung ab 2. Sitzungstag; Pauschbetrag nach VV-RVG Nr. 4116 |
| Verständigung § 257c StPO | Keine gesonderte Gebühr; im Rahmen HV-Mandat |
| Revisionsmandat | Eigenständige Verfahrensgebühr VV-RVG Nr. 4130 (Sprungrevision) oder 4134 (Revision nach Berufung) |
| Kostenentscheidung bei Freispruch | Kosten trägt Staatskasse; notwendige Auslagen des/der Freigesprochenen nach § 467 StPO |

---

## Strategische Empfehlung

| Situation | Empfehlung |
|---|---|
| Freispruch realistisch | Plädoyer fokussiert auf Beweiswürdigung und in dubio pro reo; keine Strafzumessungsargumente in Hilfsplädoyer rein, solange kein Geständnis |
| Verurteilung sicher, Strafmaß offen | Vollständige Strafzumessungsargumentation: Erstmaligkeit, Familie, Geständnis, § 46a StGB, Verfahrensdauer |
| Bewährung das Ziel | Sozialprognose aufbereiten: Arbeitsplatznachweis, Wohnanschrift, Familiensituation, ggf. Therapiebereitschaft |
| Verständigung § 257c StPO gescheitert | Plädoyer ohne Absprache hält; eigene Beweiswürdigung betonen; Verständigungsablauf für Revision dokumentieren |
| § 21 StGB und § 49 StGB relevant | Strafrahmenverschiebung ausdrücklich beantragen; Gutachten auswerten; psychiatrische Befunde zitieren |
| Revision vorbereiten | Verfahrensrügen während HV notieren; vollständige Rügedokumentation; Einlegungsfrist 1 Woche nach Urteil |

---

## Anschluss-Skills

- `fachanwalt-strafrecht-adhaesionsverfahren` – Schadenswiedergutmachung im Plädoyer als § 46a StGB-Argument
- `fachanwalt-strafrecht-nebenklage-opfervertretung` – Gegenstrategie zur Nebenklage-Schlussvortrag
- `fachanwalt-strafrecht-zeugenbeistand` – Verwertbarkeit von Zeugenaussagen im Plädoyer
- `fachanwalt-strafrecht-insolvenzantrag-staatsanwaltschaft` – Strafzumessung bei Wirtschaftsstrafsachen

---

## Quellen

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.

## 8. `schriftsatzkern-substantiierung`

**Frühere Beschreibung:** Substantiierter Schriftsatzkern für Strafverfahren Einspruch und Revision: Anwendungsfall Strafverteidiger muss Einspruch gegen Strafbefehl Revisionsbegründung oder Klageerzwingungsantrag verfassen. §§ 410 ff. StPO Einspruch Strafbefehl, § 344 StPO Revisionsbegründung, § 172 Abs. 2 bis 3 StPO Klageerzwingungsantrag, § 147 StPO Akteneinsicht. Prüfraster Tatsachenvortrag-Geruest, Beweisantrag-Liste, Verfahrenshindernisse, Sachrügen und Verfahrensrügen, Strafmass-Hilfsantrag. Output vollständiger Verteidigungs-Schriftsatz mit Antrag Begründung und Beweisangebot. Abgrenzung zu Plaedoyer-Vorbereitung und zu Hauptverhandlung.

# Schriftsatzkern und Substantiierung im Allgemeines und Wirtschaftsstrafrecht

## Wann dieser Skill greift

- Es soll ein vollwertiger Verteidigungs- oder Antragsschriftsatz im Strafverfahren erstellt werden, typischerweise: Einspruch gegen Strafbefehl (§§ 410 ff. StPO), Revisionsbegruendung (§ 344 StPO), Klageerzwingungsantrag (§ 172 Abs. 2-3 StPO), Beschwerde, Antrag auf gerichtliche Entscheidung (§ 23 EGGVG), Adhaesionsantrag-Erwiderung (§§ 403 ff. StPO).
- Mandatsannahme und ggf. Verstaendigung sind abgeschlossen oder gescheitert.
- Einspruchs-, Revisions-, Beschwerde- oder Klageerzwingungsfrist ist bekannt und im Kalender eingetragen.

## Aufbauschema

### A. Rubrum

- Beschuldigte/Angeklagte/Verurteilte (Name, Geburtsdatum, ladungsfaehige Anschrift) - exakte Schreibweise wie in Strafbefehl/Anklage/Urteil.
- Verteidigerin/Verteidiger mit Beiordnung-/Wahlvermerk (Pflicht-/Wahlverteidigung).
- Gericht/Staatsanwaltschaft (Zustaendigkeit pruefen; bei Revision zustaendiges Revisionsgericht).
- Aktenzeichen (Bezugs-Az., neues Az. nach Eingang).
- Bezeichnung der angefochtenen Entscheidung mit Datum.

### B. Antraege

Strafprozessual passende Antraege je nach Verfahrenstyp:

- **Einspruch gegen Strafbefehl:** Antrag auf Aufhebung des Strafbefehls und Freispruch, hilfsweise Einstellung (§§ 153, 153a, 154, 170 Abs. 2 StPO entsprechend), hilfsweise milderes Strafmass.
- **Revisionsbegruendung:** Antrag auf Aufhebung des Urteils und Zurueckverweisung, hilfsweise eigene Sachentscheidung (§ 354 StPO), bei reinem Strafausspruch ggf. nur Aufhebung des Rechtsfolgenausspruchs.
- **Klageerzwingung:** Antrag auf Anordnung der Anklageerhebung gegen Beschuldigte/n (§ 175 StPO).
- **Beschwerde gegen Haftbefehl:** Aufhebung des Haftbefehls, hilfsweise Aussetzung des Vollzugs gegen Auflagen (§ 116 StPO).
- **Beweisantraege** gem. § 244 Abs. 3-6 StPO als gesonderter Block; Connexitaet, Konnex zum Tatvorwurf und konkrete Beweistatsache.

### C. Tatsachenvortrag (Verteidigungs-Sachverhalt)

Der Substantiierungs-Kern; pro Tatvorwurf bzw. Tatbestand eine eigene Tatsachen-Sequenz:

1. **Sachverhalts-Chronologie** mit konkreten Daten (Tag, Uhrzeit, Ort, Personen) - eigene Version der Verteidigung.
2. **Bestrittene Tatsachen der Anklage** explizit benennen; pauschales Bestreiten reicht in der Revision nicht.
3. **Entlastende Tatsachen** mit Beweismitteln (Zeugen, Urkunden, Sachverstaendige, Augenschein).
4. **Verfahrensgeschichte** (Beschuldigtenvernehmung, Akteneinsicht, Haftgrund, Belehrungen § 136 StPO).

### D. Rechtliche Wuerdigung

Strafrechtlicher Pruefungsaufbau:

1. **Tatbestand** des StGB/Nebenstrafrechts (BtMG, AO §§ 369 ff., StVG, WaffG) nennen.
2. **Tatbestandsmerkmale** durchgehen; jedes Merkmal gegen den eigenen Tatsachenvortrag spiegeln (objektive und subjektive Seite; Vorsatz/Fahrlaessigkeit).
3. **Rechtfertigungsgruende** (§§ 32, 34 StGB) und **Entschuldigungsgruende** (§§ 33, 35 StGB) pruefen.
4. **Verfahrenshindernisse:** Verjaehrung (§ 78 StGB), Strafklageverbrauch (Art. 103 III GG, ne bis in idem), fehlender Strafantrag (§ 77 StGB), Immunitaet, Verfolgungsverjaehrung im Steuerstrafrecht (§ 376 AO).
5. **Beweiswuerdigung-Kritik:** Indizienkette, Aussage-gegen-Aussage-Konstellation, Glaubwuerdigkeitsanalyse.
6. **Rechtsprechungs-Verweise:** BGH-Strafsenate, BVerfG (Art. 103 GG, Schuldprinzip), EGMR (Art. 6 EMRK).
7. **Subsumtions-Ergebnis** klar formulieren (Freispruch, Einstellung, Strafmilderung).

### E. Beweisantraege (§ 244 StPO)

Pflichtbestandteil, ohne den Substantiierung nicht ausreicht:

- **Zeugenbeweis:** Name, ladungsfaehige Anschrift, Beweistatsache in einem Satz, Konnexitaet (Wieso kennt Zeugin die Tatsache?).
- **Sachverstaendigenbeweis:** Beweistatsache, vorgeschlagene Sachgebietsbezeichnung; bei DNA, Blutalkohol, IT-Forensik, Brandursache, Schussspurenanalyse.
- **Urkundenbeweis:** konkrete Aktenfundstelle, Inhalt mit Bezug zur Beweistatsache (Verlesung gem. § 249 StPO).
- **Augenscheinsbeweis:** Tatort, Tatwaffe, Lichtbild, Videoaufnahme.
- **Praesente Beweismittel** in der Hauptverhandlung (§ 245 StPO).
- Abgrenzung Beweisantrag / Beweisermittlungsantrag - Beweisantrag braucht bestimmte Tatsache + bestimmtes Beweismittel.

### F. Anlagenverzeichnis

- Anlagen mit Datum, Aussteller, Inhaltsbeschreibung in einem Satz.
- Erwaehnung im Tatsachenvortrag mit Aktenfundstelle (Bl. ... d.A.).
- Bei Revision: keine neuen Tatsachen, sondern Verweis auf Aktenstellen.

## Substantiierungs-Fallen im Strafverfahren

- **Pauschales Bestreiten** in der Revision (§ 344 Abs. 2 StPO verlangt bei Verfahrensruege bestimmte Tatsachen, die den Verfahrensmangel ergeben).
- **Verfahrensruege ohne Tatsachenvortrag** zum Verfahrensgeschehen (Schweigegrund § 261 StPO, abgelehnter Beweisantrag, Verletzung § 244 StPO).
- **Sachruege** zu allgemein ("Beweiswuerdigung sei luckenhaft") - notwendig: konkret welche Lueke und warum sie ergebnisrelevant ist.
- **Beweisantrag zur falschen Tatsache** - Beweistatsache deckt nur Teilaussage ab; Gericht lehnt mit § 244 Abs. 3 StPO ab.
- **Konkurrenzen** (Tateinheit/Tatmehrheit, §§ 52, 53 StGB) nicht ausgearbeitet.

## Pruefkette vor Versand

1. Antragsformulierung strafprozessual passend (Freispruch, Einstellung, Aufhebung, Zurueckverweisung)?
2. Jede Tatbestandsmerkmals-Subsumtion mit eigener Tatsache + Beweis hinterlegt?
3. Frist eingehalten (Einspruchsfrist 2 Wochen § 410 StPO; Revisionseinlegung 1 Woche § 341 StPO, Revisionsbegruendung 1 Monat § 345 StPO; Klageerzwingung 1 Monat § 172 Abs. 2 StPO)?
4. Verfahrenshindernisse von Amts wegen geprueft (Verjaehrung, Strafantrag)?
5. Beweisantraege bestimmt formuliert (Tatsache + Mittel + Konnexitaet)?
6. Anlagenverzeichnis vollstaendig?
7. beA-Konformitaet (PDF/A, ERVV, qeS bzw. sicherer Uebermittlungsweg)?
8. Vier-Augen-Pruefung durch Sozius oder Senior-Verteidigerin?

## Rechtsprechungs-Werkzeugkasten

- BVerfG (Art. 103 GG, Schuldprinzip, faires Verfahren), BGH-Strafsenate, OLG-Linien, EGMR (Art. 6 EMRK).
- StGB, StPO, BtMG, AO (§§ 369 ff.), OWiG, JGG sowie Nebenstrafrecht (StVG, WaffG, KCanG, AWG).
- Aktuelle Reform- und Gesetzgebungslage einbeziehen (z.B. KCanG-Folgeanpassungen, RAusBeitrG).

## Pflicht-Output

1. **Schriftsatz** mit Rubrum, Antraegen, Tatsachenvortrag, Rechtsausfuehrung, Beweisantraegen, Anlagenverzeichnis.
2. **Anlagen-Konvolut** numerisch geordnet, jede Anlage einzeln benannt.
3. **Frist-Doku** mit Eingangsbestaetigung (beA-Eingangsnachricht).
4. **Mandanten-Erinnerung** mit Naechster-Schritt-Aufgaben (Zeuginnen vorbereiten, Sachverstaendiger, Aktenstudium).

## Beispiel-Tatbestaende im Wirtschaftsstrafrecht

Drei haeufige Tatbestaende und ihre Substantiierungs-Anforderungen:

### Tatbestand 1: Steuerhinterziehung (§ 370 AO)

- Steueranspruch nach Steuergesetz: konkrete Steuerart, Veranlagungszeitraum, Bemessungsgrundlage.
- Unrichtige/unvollstaendige Angabe oder pflichtwidriges Unterlassen: konkrete Erklaerung, konkretes Feld.
- Steuerverkuerzung in bestimmter Hoehe: Differenz aus Steueranspruch und Festsetzung.
- Vorsatz: Wissen und Wollen, bedingter Vorsatz reicht (BGH-Linie).
- Strafzumessung: § 370 Abs. 3 AO (besonders schwerer Fall), Selbstanzeige § 371 AO.

### Tatbestand 2: Betrug (§ 263 StGB)

- Taeuschung ueber Tatsachen: konkrete Aeusserung oder konkludentes Verhalten.
- Irrtum: Vorstellung des Getaeuschten; Indizien.
- Vermoegensverfuegung: konkrete Verfuegung mit Schadensrelevanz.
- Vermoegensschaden: Saldo; bei Eingehungsbetrug auch Gefaehrdungsschaden (BVerfG-Konkretisierungsgebot).
- Bereicherungsabsicht und Stoffgleichheit.

### Tatbestand 3: Untreue (§ 266 StGB)

- Vermoegensbetreuungspflicht: Rechtsgrund (Anstellungsvertrag, gesetzliche Pflicht, Geschaeftsfuehrer).
- Pflichtverletzung: konkrete Handlung gegen das Innenverhaeltnis.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- Vorsatz auch hinsichtlich Pflichtwidrigkeit.

## Antrags-Muster nach Verfahrenstyp

### Einspruch gegen Strafbefehl

- "Es wird beantragt, den Strafbefehl des AG ... vom ... (Az. ...) aufzuheben und die Angeklagte/den Angeklagten freizusprechen."
- Hilfsweise: "... das Verfahren gemaess § 153 Abs. 2 StPO (alternativ § 153a StPO mit konkreter Auflage) einzustellen."
- Hilfsweise: "... auf eine Geldstrafe von hoechstens X Tagessaetzen zu erkennen."

### Revisionsbegruendung

- "Es wird beantragt, das Urteil des LG ... vom ... mit den ihm zugrundeliegenden Feststellungen aufzuheben und die Sache zur erneuten Verhandlung und Entscheidung an eine andere Strafkammer des LG ... zurueckzuverweisen."
- Bei reinem Rechtsfolgenangriff: "... das Urteil im Rechtsfolgenausspruch aufzuheben."

### Klageerzwingung

- "Es wird beantragt, die Staatsanwaltschaft ... anzuweisen, oeffentliche Klage gegen die Beschuldigte/n ... wegen ... zu erheben."

### Annex-Antraege

- Pflichtverteidigerbestellung (§ 140 StPO).
- Akteneinsicht (§ 147 StPO).
- Haftaussetzung (§ 116 StPO) oder -aufhebung.
- Wiedereinsetzung in den vorigen Stand (§§ 44 ff. StPO).

## Beweisaufnahme - was das Gericht sehen will

### Zeugenbeweis

- Form: "Beweis: Vernehmung der Zeugin Name, ladungsfaehige Anschrift, zum Beweis der Tatsache, dass ...; Konnexitaet: Die Zeugin war anwesend / hat das Gespraech selber gefuehrt / hat den Vorgang dokumentiert."
- Keine Beweisermittlung ueber Zeugnis - Beweistatsache muss bestimmt sein.

### Sachverstaendigenbeweis

- Beweistatsache: konkret (z.B. Blutalkoholwert zum Tatzeitpunkt, Programmierfehler im Buchungssystem, Brandursache).
- Sachgebiet benennen, Notwendigkeit gegenueber anderen Beweismitteln darlegen.
- Bei Gegengutachten: Privatgutachten beilegen und gerichtlich neues Sachverstaendigengutachten beantragen.

### Urkundenbeweis

- Aktenstelle: Bl. ... d.A. mit konkretem Inhalt.
- Verlesung gem. § 249 StPO oder Selbstleseverfahren gem. § 249 Abs. 2 StPO beantragen.

### Augenschein

- Tatort, Tatwaffe, Aufnahme - Antrag auf Inaugenscheinnahme in der Hauptverhandlung.

## Verfahrens- und Sachruege in der Revision

Schon im Schriftsatz die Trennung sauber durchziehen:

- **Verfahrensruegen:** § 244 StPO (Ablehnung Beweisantrag), § 261 StPO (Wuerdigungs-Lueke aus Inbegriff der Hauptverhandlung), § 338 StPO (absolute Revisionsgruende), § 136 StPO (Belehrungsverstoss); jede Ruege braucht Tatsachenvortrag, der den Mangel ergibt (§ 344 Abs. 2 S. 2 StPO).
- **Sachruegen:** Subsumtions-, Konkurrenz-, Strafzumessungs-, Schuldfahigkeits-Fehler; Bezug auf die Urteilsgruende, nicht auf das Akteninhalt.

## Elektronische Einreichung (beA, EGVP, EBO)

- PDF/A-2 oder PDF/A-3, mit eingebetteten Schriften.
- Strukturdatensatz nach ERVV pflicht-konform (Sender, Empfaenger, Az., Versanddatum).
- Qualifizierte elektronische Signatur (qeS) der einreichenden RA-Person oder einfacher elektronischer Versand ueber beA (sicherer Uebermittlungsweg).
- Eingangsbestaetigung aufbewahren - Datum der Einreichung ist Fristwahrungs-Beweis.
- Spezifika im Strafverfahren: Strafverteidiger reichen Schriftsaetze regelmaessig ueber beA an Strafkammer/Staatsanwaltschaft ein; Postausgang nach § 32a StPO.

## Schriftsatz-Stil

- Aktiv, kurze Saetze, klare Subsumtion.
- Keine Floskeln; Beweismittel-Zitate woertlich mit Aktenfundstelle.
- Sachlich auch bei provokanter Anklage.
- Bei Revision: keine Tatsachenwertung jenseits der Urteilsgruende.

## Vier-Augen-Check

Vor Versand:

- [ ] Antrag strafprozessual passend (Freispruch/Einstellung/Aufhebung/Zurueckverweisung)
- [ ] Frist gewahrt mit Reserve (Einspruch 2 Wochen, Revisionseinlegung 1 Woche, Revisionsbegruendung 1 Monat)
- [ ] Jede Tatsache hat Beweisantrag oder Aktenfundstelle
- [ ] Verfahrenshindernisse von Amts wegen geprueft
- [ ] Sachruege/Verfahrensruege sauber getrennt
- [ ] Rechtsprechungs-Zitat aktuell (BGH/BVerfG/EGMR)
- [ ] beA-konform mit qeS oder sicherem Uebermittlungsweg
- [ ] Senior-/Sozius-Freigabe

## Cross-Refs

- `erstgespraech-mandatsannahme` (im selben Plugin) fuer Mandatsannahme und Erstprognose.
- `vergleichsverhandlung-strategie` (im selben Plugin) fuer Verstaendigung § 257c StPO, Einstellung § 153a StPO und Adhaesion.
- `fachanwalt-strafrecht-hauptverhandlung-vorbereiten` fuer Beweisantraege in der Hauptverhandlung.

## 9. `spezial-adhaesion-formular-portal-und-einreichung`

**Frühere Beschreibung:** Adhaesion: Formular, Portal und Einreichungslogik im Plugin fachanwalt strafrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Adhaesion: Formular, Portal und Einreichungslogik

## Spezialwissen: Adhaesion: Formular, Portal und Einreichungslogik
- **Spezialgegenstand:** Adhaesion: Formular, Portal und Einreichungslogik / spezial adhaesion formular portal und einreichung. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StPO.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Adhaesion** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.

## 10. `spezial-aktenaufbereiter-beweislast-und-darlegungslast`

**Frühere Beschreibung:** Aktenaufbereiter: Beweislast, Darlegungslast und Substantiierung im Plugin fachanwalt strafrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# Aktenaufbereiter: Beweislast, Darlegungslast und Substantiierung

## Spezialwissen: Aktenaufbereiter: Beweislast, Darlegungslast und Substantiierung
- **Spezialgegenstand:** Aktenaufbereiter: Beweislast, Darlegungslast und Substantiierung / spezial aktenaufbereiter beweislast und darlegungslast. Der Skill löst diese konkrete Lage und darf nicht in allgemeines Routing ausweichen.
- **Normen-/Quellenanker:** StPO, Art. 6, EMRK.
- **Entscheidende Weiche:** Aus dem Sachverhalt sind Tatbestandsmerkmal, Zuständigkeit, Frist, Beweislast, Ermessen/Wertung und Rechtsfolge getrennt herauszuarbeiten; offene Tatsachen werden als offen markiert.
- **Arbeitsprodukt:** Erzeuge eine fallbezogene Matrix `Norm / Tatsache / Beleg / Gegenargument / Risiko / nächster Schritt` plus einen direkt verwendbaren Baustein für Vermerk, Schreiben, Antrag, Schriftsatz oder Entscheidungsvorlage.


## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **Aktenaufbereiter** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
