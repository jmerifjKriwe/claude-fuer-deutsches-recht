---
name: workflow-kaltstart-und-routing
description: "Kaltstart und Routing im Plugin fachanwalt-gewerblicher-rechtsschutz: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko, Frist und Anschluss-Skills. Enthält Routing-Heuristik für alle fünf Rechtsgebiete."
---

# Kaltstart und Routing

## Aufgabe
Dieser Workflow-Skill startet jede neue Arbeitssession im Plugin `fachanwalt-gewerblicher-rechtsschutz` und steuert die Erstorientierung: Rolle und Ziel erkennen, Frist identifizieren, Unterlagen sichten, passenden Spezialskill vorschlagen.

## Kaltstart-Fragen (maximal 5)

Wenn kein Material vorliegt, nur die nächsten Weichen klären:

1. **Wer fragt in welcher Rolle?** Anwalt / Kanzlei, Mandant (Unternehmen / Privatperson), Behördenvertreter, Richter?
2. **Was ist das gewünschte Ergebnis?** Abmahnung, EV, Klage, Vertragsgestaltung, Registrierung, Nichtigkeitsangriff, Beratung?
3. **Gibt es Fristen, Termine, Zustellungen oder Sanktionen?** Wenn ja: welche und bis wann?
4. **Welche Unterlagen, Daten oder Belege liegen vor?** Registerauszug, Abmahnung, Bescheid, Screenshot, Vertrag, Vollmacht?
5. **Welcher Output wird gebraucht?** Memo, Schriftsatz, Checkliste, Tabelle, Entwurf, Brief, Risikoampel?

Wenn Material vorliegt: zuerst mit dem Material arbeiten; nur eine gezielte Rückfrage stellen.

## Routing-Heuristik Gewerblicher Rechtsschutz

### Markenrecht
- **Verletzung (Abmahnung):** → `gr-abmahnung-workflow`
- **Risikoampel / Gegenargumente:** → `spezial-markeng-risikoampel-und-gegenargumente`
- **Anmeldung / Portfolio:** → `spezial-markenanmeldung-compliance-dokumentation-und-akte`
- **Widerspruch DPMA / EUIPO:** → `spezial-dpma-mehrparteien-konflikt-und-interessen`
- **International (EUIPO / IR-Marke):** → `spezial-euipo-internationaler-bezug-und-schnittstellen`
- **AT / CH:** → `gr-uebersetzung-marke-osterreich-schweiz-spezial`

### Patentrecht
- **Verletzungsschriftsatz:** → `spezial-patg-schriftsatz-brief-und-memo-bausteine`
- **Nichtigkeitsklage BPatG:** → `fachanwalt-gewerblicher-rechtsschutz-patent-nichtigkeitsklage`
- **Gebrauchsmuster:** → `spezial-gebrmg-verhandlung-vergleich-und-eskalation`

### Designrecht
- **Grundlagen / Verletzungsprüfung:** → `designrecht-praxis-grundlagen`
- **Red-Team:** → `spezial-designverletzung-red-team-und-qualitaetskontrolle`
- **Behörde / Register:** → `spezial-designg-behoerden-gericht-und-registerweg`

### Urheberrecht
- **Abmahnung / Verletzung:** → `gr-abmahnung-workflow`
- **Rechtsprechungs-Check:** → `spezial-urhg-livequellen-und-rechtsprechungscheck`
- **KI / TDM:** → `ki-trainingsdaten-und-urheberrecht-spezial`

### Lauterkeitsrecht (UWG)
- **Systematik / Prüfschema:** → `uwg-systematik-und-anwendung`
- **Aktivlegitimation Mitbewerber:** → `gr-mitbewerberabmahnung-aktivlegitimation-spezial`
- **Influencer-Kennzeichnung:** → `influencer-marketing-uwg-spezial`

### Einstweilige Verfügung (Prozess)
- **Dringlichkeit / Vollziehungscheck:** → `faevvollzug-neu-001-ev-vollziehungscheck-dringlichkeit-titel-zustellung`
- **GV / Parteibetrieb:** → `faevvollzug-neu-002-parteibetrieb-und-gerichtsvollzieher-bei-unterlassungstiteln`
- **Schutzschrift:** → `faevvollzug-neu-005-gegnerische-schutzschrift-auswerten`
- **Qualitätsgate:** → `faevvollzug-neu-008-qualitaetsgate-vor-vollziehung`

### Strategie und Abschluss
- **Vergleich:** → `vergleich-statt-streit-strategie`
- **Schadensersatz:** → `spezial-schadensersatz-abschlussprodukt-und-uebergabe`
- **Lizenzanalogie:** → `spezial-lizenzanaloger-fristennotiz-und-naechster-schritt`

### Workflow-Unterstützung
- **Dokumentenintake:** → `workflow-dokumentenintake`
- **Fristen / Ampel:** → `workflow-fristen-und-risikoampel`
- **Chronologie / Belege:** → `workflow-chronologie-und-belegmatrix`
- **Rechtsquellen live:** → `workflow-rechtsquellen-livecheck`
- **Red-Team:** → `workflow-redteam-qualitygate`
- **Output wählen:** → `workflow-output-waehlen`

## Praxis-Hinweise für den Kaltstart

- **Streitgenossenschaft (§ 60 ZPO):** Bei mehreren Verletzern; Streitwert je Verletzer.
- **Fliegender Gerichtsstand UWG:** Eingeschränkt (§ 14 Abs. 2 UWG n.F.); Beklagten-Sitz prüfen.
- **Schutzschrift ZSSR:** Immer prüfen ([zssr.de](https://www.zssr.de)) bevor EV-Antrag eingereicht wird.
- **§ 945 ZPO-Risiko:** Vor EV-Vollziehung bewerten; verschuldensunabhängige Haftung.

## Output-Standard

- **Kurzbild:** Worum es geht, was gesichert ist, was offen ist – in max. 5 Sätzen.
- **Prüf- oder Bearbeitungsmatrix:** Punkt, Norm, Tatsache, Beleg, Bewertung, To-do.
- **Konkreter nächster Schritt:** Mit Frist, Zuständigkeit und benötigten Unterlagen.
- **Bei Außenkommunikation:** Knapper, sachlicher Textbaustein.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Register und EU-Recht live prüfen.
- Rechtsprechung: [dejure.org](https://dejure.org), [bgh.de](https://www.bundesgerichtshof.de), [curia.europa.eu](https://curia.europa.eu).
- ZSSR: [zssr.de](https://www.zssr.de).
- Keine BeckRS-, juris-, Kommentar- oder Handbuch-Blindzitate aus Modellwissen.
- Unsicherheiten und Annahmen ausdrücklich markieren.

## Was dieser Skill nicht macht
- Keine inhaltliche Tiefprüfung (das übernehmen die Spezialskills).
- Kein Ersatz für vollständige Mandantenberatung.
- Keine eigenständige Fristberechnung ohne vollständige Daten.
