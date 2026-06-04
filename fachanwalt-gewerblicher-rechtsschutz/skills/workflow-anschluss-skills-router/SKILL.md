---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills Router im Plugin fachanwalt-gewerblicher-rechtsschutz: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor, erklärt die Weiterleitung und minimiert Doppelarbeit."
---

# Anschluss-Skills Router

## Aufgabe
Dieser Workflow-Skill steuert den Übergang von der Erstprüfung zu den richtigen Spezialskills im Plugin `fachanwalt-gewerblicher-rechtsschutz`. Er erkennt den Falltyp, identifiziert die nächste Arbeitsphase und schlägt konkrete Anschluss-Skills mit Begründung vor.

## Routing-Logik

### Nach Falltyp

| Falltyp | Primärer Anschluss-Skill | Warum |
|---|---|---|
| Markenrechtsverletzung (Abmahnung / EV) | `gr-abmahnung-workflow` | Vollständiger Abmahnungs-Workflow |
| Markenrechtsverletzung (Risikoeinschätzung) | `spezial-markeng-risikoampel-und-gegenargumente` | Ampel und Gegenargumente |
| Markenanmeldung DPMA / EUIPO | `spezial-markenanmeldung-compliance-dokumentation-und-akte` | Anmelde-Compliance |
| Markenwiderspruch DPMA | `spezial-dpma-mehrparteien-konflikt-und-interessen` | DPMA-Verfahren |
| Designverletzung | `designrecht-praxis-grundlagen` | Schutzvoraussetzungen und Verletzung |
| Designbehörde / Register | `spezial-designg-behoerden-gericht-und-registerweg` | Behörden und Registerweg |
| Patentverletzung / Schriftsatz | `spezial-patg-schriftsatz-brief-und-memo-bausteine` | Schriftsatzbausteine |
| Gebrauchsmusterstreit | `spezial-gebrmg-verhandlung-vergleich-und-eskalation` | GebrMG-Eskalation |
| UWG-Abmahnung | `uwg-systematik-und-anwendung` | UWG-Prüfschema |
| UWG Aktivlegitimation | `gr-mitbewerberabmahnung-aktivlegitimation-spezial` | Aktivlegitimations-Check |
| EV beantragen / vollziehen | `faevvollzug-neu-001-ev-vollziehungscheck-dringlichkeit-titel-zustellung` | EV-Vollziehung |
| EV-Qualitätsgate | `faevvollzug-neu-008-qualitaetsgate-vor-vollziehung` | Letzter Check |
| Schutzschrift auswerten | `faevvollzug-neu-005-gegnerische-schutzschrift-auswerten` | Schutzschrift |
| Ordnungsmittelantrag | `faevvollzug-neu-004-vollstreckung-aus-unterlassungsverfuegung-ordnungsmittel` | Vollstreckung |
| EUIPO / internationale Marke | `spezial-euipo-internationaler-bezug-und-schnittstellen` | EUIPO international |
| Österreich / Schweiz | `gr-uebersetzung-marke-osterreich-schweiz-spezial` | AT/CH-Schnittstellen |
| Grenzüberschreitende EV | `faevvollzug-neu-007-grenzueberschreitende-ip-eilverfuegung` | Cross-border EV |
| Schadensersatz | `spezial-schadensersatz-abschlussprodukt-und-uebergabe` | Schadensabschluss |
| Lizenzanalogie | `spezial-lizenzanaloger-fristennotiz-und-naechster-schritt` | Lizenzberechnung |
| Vergleich anstreben | `vergleich-statt-streit-strategie` | Vergleichsstrategie |
| Beweis sichern / Tatbestand | `spezial-gewerblichen-tatbestand-beweis-und-belege` | Beweismittel |
| Fristen und Zuständigkeit | `spezial-rechtsschutz-fristen-form-und-zustaendigkeit` | Fristenkatalog |
| Portfoliopflege | `gr-portfolio-pflege-workflow` | Portfolio |
| Influencer / UWG | `influencer-marketing-uwg-spezial` | Influencer |
| KI / TDM | `ki-trainingsdaten-und-urheberrecht-spezial` | KI und UrhG |
| UrhG Rechtsprechung | `spezial-urhg-livequellen-und-rechtsprechungscheck` | UrhG Live-Check |
| FAO Nachweis | `spezial-fao-dokumentenmatrix-und-lueckenliste` | FAO-Dokumentation |

## Übergangsformat

Nach Erstprüfung (z.B. in `spezial-fachanwalt-erstpruefung-und-mandatsziel`):

```
Erste Einschätzung:
[Kurzlage in 3 Sätzen: Schutzrecht / Verletzung / Frist]

Empfohlener nächster Skill:
→ [Skill-Name]: [Warum dieser Skill die Arbeit jetzt beschleunigt]

Alternativ:
→ [Skill-Name]: [Wenn Alternative B zutrifft]
```

## Workflow nach Phase

| Phase | Empfohlener Skill |
|---|---|
| Erstprüfung | `spezial-fachanwalt-erstpruefung-und-mandatsziel` |
| Abmahnvorbereitung | `gr-abmahnung-workflow` |
| Beweissicherung | `spezial-gewerblichen-tatbestand-beweis-und-belege` |
| EV-Antrag | `faevvollzug-neu-001-ev-vollziehungscheck-dringlichkeit-titel-zustellung` |
| Qualitätsgate EV | `faevvollzug-neu-008-qualitaetsgate-vor-vollziehung` |
| Vollziehung | `faevvollzug-neu-002-parteibetrieb-und-gerichtsvollzieher-bei-unterlassungstiteln` |
| Abschlussschreiben | `faevvollzug-neu-006-abschlussschreiben-kosten-und-frist` |
| Hauptsache / Schadensersatz | `spezial-schadensersatz-abschlussprodukt-und-uebergabe` |
| Vergleich | `vergleich-statt-streit-strategie` |
| Mandantenübergabe | `spezial-schadensersatz-abschlussprodukt-und-uebergabe` |

## Qualitätssicherung beim Routing

- Nie in ein Spezialgebiet weiterleiten ohne zu prüfen, ob der korrekte Falltyp erkannt wurde.
- Wenn unklar: Zuerst Kaltstart-Fragen stellen (max. 3).
- Wenn mehrere Skills parallel relevant sind: Priorisierung nach Dringlichkeit.

## Kaltstart
1. Was ist der aktuelle Stand der Sache (Abmahnung / EV / Klage / Nichtigkeitsverfahren)?
2. Welcher konkrete Output wird als nächstes gebraucht?
3. Gibt es Fristen, die das Routing beschleunigen?
4. Liegt Material vor, das den nächsten Schritt konkretisiert?
5. Output: Routing-Vorschlag, Übergangstext für nächsten Skill, Phasenplan?

## Plugin-Kontext
Skill gehört zu `fachanwalt-gewerblicher-rechtsschutz`. Er wird typischerweise nach einem ersten Kaltstart oder nach Abschluss einer Arbeitsphase aktiviert, um nahtlos weiterzuarbeiten.

## Quellenregel
- Normen werden im jeweils aufgerufenen Spezialskill benannt.
- Dieser Skill trifft keine inhaltlichen Aussagen, sondern steuert den Workflow.
- Annahmen und fehlende Informationen ausdrücklich benennen.

## Was dieser Skill nicht macht
- Keine inhaltliche Rechtsprüfung (das übernehmen die Spezialskills).
- Kein Ersatz für vollständige Mandantenberatung.
- Keine Priorisierung ohne Kenntnis der Fristen und Dringlichkeit.
