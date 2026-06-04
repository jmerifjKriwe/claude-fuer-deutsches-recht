---
name: kompendium-12-dsfa-edpb-leitlinien-bis-dsfa-update-bei-aend
description: "datenschutzrecht: Konsolidiertes Skill-Kompendium 12; bündelt 10 frühere Spezialskills (dsfa-edpb-leitlinien-9-19-anwendung, dsfa-erstellung, dsfa-fuer-internationale-datentransfers, dsfa-fuer-ki-systeme-schnittstelle-art-26-kivo, dsfa-methodik-cnil-pia-vs-bsfd-bsi und 5 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 12 - datenschutzrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `dsfa-edpb-leitlinien-9-19-anwendung` | Anwendung der EDPB-/EDSA-Leitlinien WP 248 rev.01 zur DSFA: die neun Kriterien fuer voraussichtlich hohes Risiko strukturiert pruefen. Output: Kriterien-Tabelle mit Subsumtion und Schwellwertergebnis. |
| `dsfa-erstellung` | Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO durchführen wenn hohes Risiko für Betroffene vorliegt. Art. 35 36 DSGVO DSFA § 67 BDSG. Prüfraster: Risikobewertung Verarbeitungsbeschreibung Notwendigkeit Verhältnismäßigkeit Massnahmen Restrisiko Vorabkonsultation. Output: DSFA-Dokument Massnahmenkatalog. Abgrenzung: nicht für regulaere Verarbeitungen ohne hohes Risiko. |
| `dsfa-fuer-internationale-datentransfers` | DSFA bei internationalen Datentransfers nach Kapitel V DSGVO: Integration der Transfer Impact Assessment (TIA) in die DSFA, Pruefung Angemessenheit SCC BCR Ausnahmen Art. 49. Output: erweiterte DSFA-Sektion fuer Drittlandbezug. |
| `dsfa-fuer-ki-systeme-schnittstelle-art-26-kivo` | DSFA fuer KI-Systeme an der Schnittstelle zur KI-Verordnung: Koordination Art. 35 DSGVO mit Art. 26 KI-VO Betreiberpflichten und Art. 27 KI-VO Grundrechte-Folgenabschaetzung. Output: integriertes DSFA-FRIA-Konzept. |
| `dsfa-methodik-cnil-pia-vs-bsfd-bsi` | Vergleich der DSFA-Methoden: CNIL PIA Software (Frankreich) gegenueber dem BSI Standard-Datenschutzmodell (SDM) und dem BSFD-Ansatz. Output: Methodenwahl mit Begruendung, Anwendungshinweisen und Werkzeugauswahl. |
| `dsfa-restrisiko-und-art-36-konsultation` | Restrisiko nach Massnahmen bewerten und Vorab-Konsultation Art. 36 DSGVO vorbereiten. Output: Konsultationsantrag mit Verarbeitungsbeschreibung Massnahmen Restrisiko Begruendung warum die Konsultation erforderlich ist. |
| `dsfa-stakeholder-konsultation-art-35-9` | Konsultation der Betroffenen oder ihrer Vertreter nach Art. 35 Abs. 9 DSGVO im Rahmen einer DSFA: Pruefung Erforderlichkeit Form Reichweite Dokumentation. Output: Konsultationsplan mit Begruendung Form und Dokumentation. |
| `dsfa-template-deutsch-vollvorlage` | Deutsche DSFA-Vollvorlage nach Art. 35 Abs. 7 DSGVO mit ausgefuellten Platzhaltern fuer alle sechs Pflichtsektionen Beschreibung Verhaeltnismaessigkeit Risiken Massnahmen Restrisiko Freigabe. Output: vollstaendige DSFA-Vorlage zum Befuellen. |
| `dsfa-typische-fehler-bei-erstpruefung` | Katalog typischer Fehler bei der DSFA-Erstpruefung und Gegenmassnahmen. Output: Fehlerkatalog mit Pruefliste fuer DSB und Verantwortliche samt Beispielen aus Aufsichtspraxis. |
| `dsfa-update-bei-aenderungen-und-revision` | Aktualisierung einer DSFA bei wesentlichen Aenderungen der Verarbeitung nach Art. 35 Abs. 11 DSGVO. Output: Revisionsplan mit Trigger-Liste Aenderungsanalyse Risikoreassessment und Versionshistorie. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `dsfa-edpb-leitlinien-9-19-anwendung`

**Frühere Beschreibung:** Anwendung der EDPB-/EDSA-Leitlinien WP 248 rev.01 zur DSFA: die neun Kriterien fuer voraussichtlich hohes Risiko strukturiert pruefen. Output: Kriterien-Tabelle mit Subsumtion und Schwellwertergebnis.

# Anwendung der EDPB-Leitlinien WP 248 rev.01 zur DSFA

## Zweck

Strukturierte Anwendung der neun Kriterien der EDPB-/EDSA-Leitlinien WP 248 rev.01 zur Bestimmung von voraussichtlich hohem Risiko. Ergebnis ist eine Kriterien-Tabelle mit Subsumtion und einer klaren Schwellwertaussage: 0 Kriterien (DSFA entbehrlich), 1 Kriterium (Empfehlung mit Begruendung), 2 oder mehr Kriterien (DSFA zwingend, soweit keine entgegenstehende Whitelist-Position einschlaegig ist).

## Wann brauchen Sie diesen Skill

- In der Schwellwertanalyse einer DSFA-Trigger-Pruefung, wenn weder Art. 35 Abs. 3 noch Abs. 4 DSGVO greift
- Wenn die Aufsichtsbehoerde eine Begruendung der DSFA-Entscheidung verlangt
- Zur Vorpruefung von KI-, Profiling- oder Beschaeftigtendaten-Verarbeitungen
- Wenn die DSB-Stellungnahme eine EDSA-Konformitaet anfordert

## Rechtlicher Rahmen

- EDPB-/EDSA-Leitlinien WP 248 rev.01 (Artikel-29-Gruppe, von EDSA uebernommen): neun Kriterien fuer voraussichtlich hohes Risiko.
- Art. 35 Abs. 1 DSGVO Generalklausel — die WP-248-Kriterien konkretisieren den Tatbestand.
- Art. 35 Abs. 2 DSGVO Anhoerung des DSB.
- Art. 70 Abs. 1 lit. e DSGVO Aufgabe des EDSA zur Konkretisierung.

## Die neun WP-248-Kriterien

1. Bewertung oder Scoring (einschliesslich Profiling und Prognose)
2. Automatisierte Entscheidung mit rechtlicher oder aehnlich erheblicher Wirkung (Art. 22 DSGVO)
3. Systematische Ueberwachung
4. Sensible Daten oder hoechstpersoenliche Daten (Art. 9, Art. 10 DSGVO; auch Standortdaten, Finanzdaten, Kommunikationsinhalte)
5. Verarbeitung in grossem Umfang (Anzahl Betroffene, Datenmenge, Dauer, geografische Reichweite)
6. Abgleich oder Zusammenfuehrung von Datensaetzen aus unterschiedlichen Quellen
7. Daten ueber schutzbeduerftige Personen (Kinder, Patienten, Beschaeftigte, Asylsuchende, aeltere Menschen)
8. Innovative Nutzung oder Anwendung neuer technologischer oder organisatorischer Loesungen (KI, Biometrie, IoT)
9. Wenn die Verarbeitung selbst die Betroffenen daran hindert, ein Recht auszuueben oder eine Dienstleistung in Anspruch zu nehmen

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Kurze, faktenfeste Beschreibung der Verarbeitung; ohne diese ist die WP-248-Pruefung Spekulation.
2. **Verhaeltnismaessigkeitspruefung.** Erste Plausibilitaet: Reicht die Verarbeitung in eines der neun Felder hinein oder nicht?
3. **Risikoanalyse Kriterien.** Jedes der neun Kriterien einzeln pruefen und mit ja oder nein beantworten, jeweils mit kurzer Begruendung. Wo Grenzfaelle bestehen, das Pro und Contra dokumentieren.
4. **Massnahmen.** Pruefen ob bereits geplante Massnahmen ein Kriterium so entkraeften, dass es nicht mehr greift (z. B. echte Anonymisierung statt Pseudonymisierung kann das Kriterium besondere Kategorien entfallen lassen).
5. **Restrisiko / Schwellwert.** Zaehlung der erfuellten Kriterien:
   - 0 Kriterien — DSFA voraussichtlich entbehrlich
   - 1 Kriterium — Grenzfall, schriftliche Begruendung der Entscheidung
   - 2 oder mehr Kriterien — DSFA zwingend
6. **Konsultation / Genehmigung.** Ergebnis dem DSB vorlegen; Aufsichtsbehoerde wird nur konsultiert, wenn nach DSFA hohes Restrisiko verbleibt (Art. 36 DSGVO).

## Mustertext / Template

```
WP-248-PRUEFUNG ZUR DSFA-PFLICHT [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME]

Kriterium                                       | Erfuellt | Begruendung
1 Scoring / Profiling / Prognose                | ja/nein  | [...]
2 Automatisierte Entscheidung Art. 22 DSGVO     | ja/nein  | [...]
3 Systematische Ueberwachung                    | ja/nein  | [...]
4 Sensible Daten Art. 9 / Art. 10 DSGVO         | ja/nein  | [...]
5 Verarbeitung in grossem Umfang                | ja/nein  | [...]
6 Abgleich / Zusammenfuehrung                   | ja/nein  | [...]
7 Schutzbeduerftige Personen                    | ja/nein  | [...]
8 Neue Technologien                             | ja/nein  | [...]
9 Verhinderung Rechtsausuebung                  | ja/nein  | [...]

Summe erfuellter Kriterien: [X] von 9

Ergebnis
[ ] 0 — DSFA voraussichtlich entbehrlich
[ ] 1 — Grenzfall; schriftliche Entscheidung beigefuegt
[ ] 2 oder mehr — DSFA zwingend nach Art. 35 Abs. 1 DSGVO i. V. m. WP 248 rev.01

Naechster Schritt: [Vollstaendige DSFA / Dokumentation der Negativentscheidung]

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Indikatoren fuer Kriterium 5 (grosser Umfang)

- Anzahl Betroffener absolut und relativ zur Bevoelkerung der Zielregion.
- Datenmenge pro Betroffenem (Datensaetze, Bytes, Dokumente).
- Dauer und Persistenz der Verarbeitung.
- Geografische Ausdehnung (regional, national, EU-weit, global).
- Aufbewahrungsdauer.
- Indikatorenkombinationen statt Einzelschwellen verwenden.

## Hinweise zu Kriterium 8 (neue Technologien)

- KI- und Maschinelles-Lernen-Systeme — regelmaessig einschlaegig.
- Biometrische Identifikation (Gesicht, Stimme, Fingerabdruck).
- IoT-Geraete mit personenbezogenen Sensoren.
- Verhaltensbasierte Verfahren (Tippmuster, Mausbewegung).
- Auch neue organisatorische Loesungen (z. B. neue Form der Zusammenarbeit mit Auftragsverarbeitern, neue Datenpools).

## Typische Fehler

- Kriterium 5 (grosser Umfang) wird ohne Zahlen behauptet — EDSA verlangt konkrete Indikatoren.
- Kriterium 4 wird auf Art. 9 reduziert; Standort-, Finanz- und Kommunikationsdaten werden uebersehen.
- Kriterium 8 wird auf KI beschraenkt — auch neue organisatorische Loesungen koennen einschlaegig sein.
- Begruendung wird in Floskeln gehalten — Aufsicht erwartet faktenfeste Subsumtion.
- Die Zahl 2 wird als starre Schwelle verstanden — Art. 35 Abs. 1 DSGVO kennt auch das Einzelkriterium, wenn dessen Intensitaet hoch ist.
- Negativabgrenzung fehlt — wenn Kriterium nicht erfuellt ist, muss auch das begruendet werden.
- Mehrfachzaehlung (ein Sachverhalt fuer zwei Kriterien) ohne Begruendung.

## Querverweise

- `datenschutzrecht/skills/dsfa-art-35-dsgvo-trigger-und-anwendungsbereich/SKILL.md` — Trigger-Gesamtpruefung
- `datenschutzrecht/skills/dsfa-bfdi-und-laender-blacklist/SKILL.md` — Listenabgleich
- `datenschutzrecht/skills/dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden/SKILL.md` — Risikoanalyse-Methodik
- `datenschutzrecht/skills/dsfa-fuer-ki-systeme-schnittstelle-art-26-kivo/SKILL.md` — KI-DSFA-Schnittstelle
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- EDSA-/EDPB-Leitlinien WP 248 rev.01 — neun Kriterien
- Art. 35 Abs. 1, 2, 3 DSGVO
- Art. 70 Abs. 1 lit. e DSGVO
- EDSA-Stellungnahme 28/2024 zu KI-Modellen — Auslegungshilfe fuer Kriterium 8
- BfDI- und Landeslisten (live pruefen)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle

## 2. `dsfa-erstellung`

**Frühere Beschreibung:** Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO durchführen wenn hohes Risiko für Betroffene vorliegt. Art. 35 36 DSGVO DSFA § 67 BDSG. Prüfraster: Risikobewertung Verarbeitungsbeschreibung Notwendigkeit Verhältnismäßigkeit Massnahmen Restrisiko Vorabkonsultation. Output: DSFA-Dokument Massnahmenkatalog. Abgrenzung: nicht für regulaere Verarbeitungen ohne hohes Risiko.

# DSFA – Datenschutz-Folgenabschätzung Art. 35 DSGVO

## Zweck

Vollständige Datenschutz-Folgenabschätzung nach Art. 35 DSGVO: von der Schwellwertanalyse über die Risikoidentifikation bis zur Maßnahmenplanung und Freigabe. Das Format richtet sich nach dem Hausformat aus der Referenz-DSFA in `CLAUDE.md`; fehlt diese, wird die EDSA-Methodik (Leitlinien 09/2022) genutzt.

## Eingaben

- Beschreibung des Verarbeitungsvorhabens (Zweck, Datenarten, Betroffene, Technologie)
- Vorabklassifikation aus `anwendungsfall-triage` (falls bereits erfolgt)
- Praxisprofil aus `CLAUDE.md` (Systemliste, Hausformat, Freigabe-Eskalation)
- Optional: technische Spezifikation, Dienstleisterbeschreibung, AVV-Entwurf

## Ablauf

1. **Schwellwertanalyse (Muss-DSFA-Prüfung).**

   Art. 35 Abs. 1 DSGVO: DSFA erforderlich bei voraussichtlich hohem Risiko. Mindestens zwei der folgenden Kriterien aus EDSA-Leitlinien 09/2022 treffen zu:

   | Kriterium | Prüfung |
   |---|---|
   | Bewertung / Scoring | Ja / Nein |
   | Automatisierte Entscheidung mit Rechtswirkung (Art. 22 DSGVO) | Ja / Nein |
   | Systematische Überwachung | Ja / Nein |
   | Verarbeitung sensibler Daten (Art. 9/10 DSGVO) | Ja / Nein |
   | Verarbeitung großer Mengen oder im großen Umfang | Ja / Nein |
   | Abgleich oder Zusammenführung von Datensätzen | Ja / Nein |
   | Verarbeitung betreffend schutzbedürftige Personen (Kinder, Patienten) | Ja / Nein |
   | Einsatz neuer Technologien (KI, Biometrie, IoT) | Ja / Nein |
   | Verarbeitung verhindert Betroffenenrechte oder Dienstnutzung | Ja / Nein |

   Art. 35 Abs. 3 DSGVO: In jedem Fall DSFA bei systematischer umfangreicher Verarbeitung besonderer Kategorien, umfangreicher Überwachung öffentlicher Bereiche, oder wenn auf der BfDI-Blacklist aufgeführt.

2. **BfDI-Blacklist-Abgleich.**
   Abgleich gegen die Blacklist des BfDI (§ 67 BDSG i.V.m. Art. 35 Abs. 4 DSGVO). `[Modellwissen – aktuellen Stand auf bfdi.bund.de prüfen]`
   Typische Blacklist-Einträge: Biometrische Erfassungssysteme zur eindeutigen Identifizierung, Videoüberwachung öffentlicher Bereiche im großen Umfang, Scoring-Systeme für Kreditwürdigkeit, Gesundheitsdaten-Plattformen für Forschung.

   BfDI-Whitelist (§ 67 Abs. 2 BDSG): Wenn Verarbeitungsart auf Whitelist, entfällt DSFA-Pflicht. `[Modellwissen – prüfen]`

3. **Beschreibung der Verarbeitungstätigkeit (Art. 35 Abs. 7 lit. a DSGVO).**
   - Zweck und Art der Verarbeitung
   - Datenkategorien und betroffene Personengruppen
   - Empfänger, Übermittlungen (inkl. Drittland)
   - Aufbewahrungsfristen
   - Technische Umgebung (Hosting, Sub-AVs)
   - Eigentümer der Verarbeitung (Fachabteilung, Produkt)

4. **Notwendigkeit und Verhältnismäßigkeit (Art. 35 Abs. 7 lit. b DSGVO).**
   - Ist die Verarbeitung für den Zweck erforderlich (Erforderlichkeit)?
   - Werden nicht mehr Daten verarbeitet als nötig (Datenminimierung Art. 5 Abs. 1 lit. c DSGVO)?
   - Ist die Zweckbindung eingehalten (Art. 5 Abs. 1 lit. b DSGVO)?
   - Ist die Rechtsgrundlage klar (Art. 6, 9 DSGVO)?
   - Ist die Speicherfrist verhältnismäßig (Art. 5 Abs. 1 lit. e DSGVO)?

5. **Risikoidentifikation und -bewertung (Art. 35 Abs. 7 lit. c DSGVO).**
   Für jeden identifizierten Risikotyp: Eintrittswahrscheinlichkeit × Schwere des Schadens:

   | Risiko | Kategorie | Eintrittsws. | Schwere | Risikostufe |
   |---|---|---|---|---|
   | Unbefugter Zugriff | Vertraulichkeit | [hoch/mittel/gering] | [hoch/mittel/gering] | 🔴/🟠/🟡/🟢 |
   | Datenverlust | Verfügbarkeit | … | … | … |
   | Profiling ohne Kenntnis | Transparenz | … | … | … |
   | Diskriminierung | Schaden Betroffener | … | … | … |
   | Identitätsdiebstahl | Sicherheit | … | … | … |

   Referenz: EDSA-Leitlinien 09/2022, Abschn. 6; ENISA-Leitfaden DSFA.

6. **Maßnahmen zur Risikominimierung (Art. 35 Abs. 7 lit. d DSGVO).**
   Für jedes Risiko ≥ 🟡 konkrete Maßnahme:
   - Technische Maßnahmen (Verschlüsselung, Pseudonymisierung, Zugriffskontrolle)
   - Organisatorische Maßnahmen (Schulungen, Vier-Augen-Prinzip, Berechtigungskonzept)
   - Vertragsmaßnahmen (AVV, SCC)
   - Restrisiko nach Maßnahmen (bleibt 🔴? → Vorab-Konsultation Art. 36 DSGVO)

7. **Vorab-Konsultation Art. 36 DSGVO.**
   Wenn nach Maßnahmen ein hohes Restrisiko verbleibt: Pflicht zur Vorab-Konsultation bei der zuständigen Aufsichtsbehörde (Art. 36 Abs. 1 DSGVO). Frist: Aufsichtsbehörde hat 8 Wochen zur Antwort (Art. 36 Abs. 2 DSGVO), verlängerbar um 6 Wochen.

8. **DSB-Beteiligung.**
   DSB ist bei der DSFA zu beteiligen (Art. 35 Abs. 2 DSGVO). Stellungnahme des DSB einholen und dokumentieren.

9. **Freigabe und Dokumentation.**
   Freigabeprozess aus `CLAUDE.md`; DSFA im Verarbeitungsverzeichnis vermerken (Art. 30 Abs. 1 DSGVO). DSFA ist bei wesentlicher Änderung der Verarbeitung zu wiederholen (Art. 35 Abs. 11 DSGVO).

## Quellen und Zitierweise

Verbindlich nach `../../references/zitierweise.md`.

- Art. 35 DSGVO (DSFA: Pflicht, Inhalt, Vorab-Konsultation)
- Art. 36 DSGVO (Vorab-Konsultation Aufsichtsbehörde)
- Art. 5 Abs. 1 lit. b, c, e DSGVO (Zweckbindung, Datenminimierung, Speicherbegrenzung)
- § 67 BDSG (Blacklist/Whitelist BfDI)
- EDSA-Leitlinien 09/2022 zur DSFA und Bestimmung von "voraussichtlich hohem Risiko"
- Artikel-29-Datenschutzgruppe, WP 248 rev.01 (DSFA-Methodik, heute EDSA-Referenz)
- Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen zitieren. Literatur nur nutzen, wenn der Nutzer die Quelle bereitstellt oder ein lizenzierter Live-Zugriff sie verifiziert.
- Martini, in: Paal/Pauly, DSGVO/BDSG, 3. Aufl. 2021, Art. 35 Rn. 1 ff.
- Klabunde, in: Simitis/Hornung/Spiecker, Datenschutzrecht, 1. Aufl. 2019, Art. 35 Rn. 1 ff.
- Quellenregel: Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff; keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.

## Strategische Optionen (vor dem Template entscheiden)

Bevor das Template eins-zu-eins gefuellt wird, ist zu pruefen welche Variante zur Mandantenkonstellation passt. Das Template ist **eine** moegliche Form — nicht die einzige.

| Konstellation | Empfohlener Weg |
|---|---|
| Standard — DSFA fuer neue Verarbeitung durchfuehren | Schwellenwertanalyse und vollstaendige DSFA nach Template unten |
| Variante A — Verarbeitung schon laeuft ohne DSFA | Nachtraegliche DSFA; Massnahmen-Umsetzungsplan erstellen |
| Variante B — Ergebnis der DSFA negativ (hohes Restrisiko) | Verarbeitung anpassen oder Aufsichtsbehoerde konsultieren |
| Variante C — DSFA fuer mehrere aehnliche Verarbeitungen | Muster-DSFA-Dokument erstellen; individuell anpassen |

Wenn die Mandantenkonstellation **nicht** ins Standardschema passt, ist das Template anzupassen oder durch ein anderes Skill abzuloesen — nicht das Mandat in das Schema zu pressen.

## Ausgabeformat

DSFA im Hausformat (aus Referenz-DSFA in `CLAUDE.md`) oder, falls nicht verfügbar, folgendes Standardformat:

1. Deckblatt (Vorhaben, Datum, Verantwortlicher, DSB, Version)
2. Zusammenfassung (Executive Summary: Risikostufe Gesamt, Ergebnis, Freigabe-Status)
3. Beschreibung Verarbeitungstätigkeit
4. Schwellwertanalyse (Tabelle + Begründung)
5. Notwendigkeit und Verhältnismäßigkeit
6. Risikoidentifikation und -bewertung (Risikotabelle)
7. Maßnahmen (Tabelle: Risiko | Maßnahme | Verantwortlich | Frist | Restrisiko)
8. DSB-Stellungnahme (Platzhalter für Unterschrift)
9. Freigabe-Dokumentation
10. Überprüfungsplan (wann wiederholen)

## Beispiel (Schwellwertanalyse)

**Vorhaben:** Einführung eines KI-gestützten Bewerberscreenings mit automatischer Vorauswahl.

**Schwellwertanalyse:**
- Bewertung/Scoring: **Ja** (Bewerber werden automatisch bewertet und gereiht)
- Automatisierte Entscheidung mit Rechtswirkung: **Ja** (Vorauswahl entscheidet über Einladung zum Gespräch → erhebliche Beeinträchtigung i.S.d. Art. 22 Abs. 1 DSGVO, sofern keine Menschenentscheidung zwischengeschaltet)
- Einsatz neuer Technologien (KI): **Ja**
- Schutzbedürftige Personen: ggf. (Bewerber in angespannter Arbeitsmarktsituation)

**Ergebnis Schwellwert:** Mindestens 3 Kriterien erfüllt → **DSFA erforderlich**. Zusätzlich: § 26 Abs. 1 BDSG (Beschäftigtendaten) und Art. 22 DSGVO (automatisierte Einzelentscheidung) sind eigenständige Schutznormen, die eine DSFA unabhängig von der Schwellwertanalyse nahelegen.

## Risiken / typische Fehler

- **Fehlende DSB-Beteiligung:** Art. 35 Abs. 2 DSGVO schreibt ausdrücklich Beteiligung vor; unterlassene Beteiligung ist ein eigenständiger Verstoß, selbst wenn die DSFA inhaltlich korrekt ist.
- **DSFA als Einmalvorgang:** Art. 35 Abs. 11 DSGVO – DSFA muss bei wesentlichen Änderungen der Verarbeitungstätigkeit wiederholt werden. Änderungsmanagement im Verfahren verankern.
- **Vorab-Konsultation übergangen:** Wenn Restrisiko nach Maßnahmen hoch bleibt, ist Art. 36 DSGVO keine Option, sondern Pflicht. Unterlassung ist eigenständiger Bußgeldtatbestand (Art. 83 Abs. 4 lit. a DSGVO).
- **BfDI-Blacklist-Stand nicht geprüft:** Blacklist kann aktualisiert werden. Immer aktuelle Fassung auf bfdi.bund.de prüfen.
- **KI-VO-Überschneidung (ab 2026):** Für KI-Systeme mit hohem Risiko nach VO (EU) 2024/1689 (KI-VO) ist eine Konformitätsprüfung nach KI-VO und eine DSFA nach Art. 35 DSGVO durchzuführen. Beide Instrumente ergänzen sich; die KI-VO-Konformitätsbewertung ersetzt die DSFA nicht. `[Modellwissen – Zeitplan KI-VO prüfen]`

## Quellen / Updates

Stand: 05/2026. Aktualität prüfen bei EDSA-Aktualisierungen der Leitlinien 09/2022, neuen BfDI-Blacklist-Einträgen sowie KI-VO-Hochrisiko-Kategorien (VO (EU) 2024/1689, Anhang III).

**Querverweise:**
- `datenschutzrecht/skills/anwendungsfall-triage/SKILL.md` — Vorgelagerte DSFA-Pflichtprüfung
- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — TIA als Bestandteil der DSFA bei Drittlandbezug
- `datenschutzrecht/skills/datenpanne-meldung/SKILL.md` — Vorab-Konsultation Art. 36 DSGVO nach negativer DSFA

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Faktische Updates (Stand 05/2026)

- **DSFA + FRIA (Art. 27 KI-VO) bei Hochrisiko-KI:** Ab 02.08.2026 muessen Betreiber bestimmter Hochrisiko-KI-Systeme (oeffentliche Stellen, oeffentlich-finanzierte Dienste, Kreditwuerdigkeitsbewertung, Kranken-/Lebensversicherungs-Risikobewertung) eine Grundrechte-Folgenabschaetzung (Fundamental Rights Impact Assessment, FRIA) durchfuehren. DSFA und FRIA koennen integriert werden, sind aber rechtlich eigenstaendig. Quelle: VO (EU) 2024/1689, Art. 27.
- **EDSA-Stellungnahme 28/2024 zu KI-Modellen:** verbindliche Auslegungshilfe zur DSGVO-Bewertung von KI-Modellen und KI-Diensten, insb. zu personenbezogenen Daten in Modell-Gewichten und Training. Quelle: edpb.europa.eu.
- **BfDI-/LfDI-Blacklist Art. 35 Abs. 4 DSGVO:** Aktuelle Liste verpflichtender DSFA-Faelle live ueber bfdi.bund.de pruefen; auch Landesdatenschutzbehoerden veroeffentlichen Listen (z.B. LfDI BW, LDA Bayern).
- **Art. 36 DSGVO Vorab-Konsultation:** Bei Restrisiko nach DSFA Pflicht zur Konsultation der Aufsichtsbehoerde. Frist 8 Wochen, Verlaengerung 6 Wochen moeglich.

## Triage zu Beginn

1. Liegt bereits ein Ergebnis aus `anwendungsfall-triage` vor (DSFA PFLICHT)?
2. Welche EDSA-Kriterien sind erfüllt? (Mindestens 2 für DSFA-Pflicht)
3. Ist die Verarbeitung auf der BfDI-Blacklist?
4. Gibt es ein Hausformat in CLAUDE.md?
- **Was will der Mandant wirklich erreichen?** (Nicht: was steht im Standardweg, sondern: welches Ergebnis ist fuer den Mandanten persoenlich/wirtschaftlich das beste? Manchmal ist der schnellere Vergleich besser als der formal "richtige" Weg.)

## Output-Template — DSFA-Zusammenfassung

**Adressat:** DSB / Geschäftsführung / Aufsichtsbehörde — Tonfall: sachlich-juristisch

```
DSFA-Zusammenfassung [DATUM]
Verarbeitungsvorgang: [BEZEICHNUNG]
Verantwortlicher: [NAME]

Schwellwertanalyse: DSFA erforderlich: JA / NEIN
EDSA-Kriterien erfüllt: [X] von 9 ([LISTE])
BfDI-Blacklist: ja / nein

Rechtsgrundlage: Art. [X] DSGVO [§ BDSG]
Datenkategorien: [LISTE]
Betroffene: [GRUPPEN]

Risikobewertung (Vor Massnahmen):
- Wahrscheinlichkeit: hoch / mittel / gering
- Schwere: hoch / mittel / gering
- Gesamtrisiko: HOCH / MITTEL / GERING

Vorgesehene Massnahmen: [LISTE]

Restrisiko (Nach Massnahmen): AKZEPTABEL / NICHT AKZEPTABEL

Entscheidung: Freigabe / Vorab-Konsultation Art. 36 DSGVO erforderlich
Genehmigende Person: [NAME, FUNKTION]
Datum: [DATUM]
```

--- vor Versand klaeren ---
1. Welches Verhandlungsziel hat der Mandant? [Bestand / Abfindung / Reputation / Schnelle Loesung]
2. Welche Kompromisslinien sind absolut? [Mindestabfindung / Freistellung / Zeugnisformulierung]
3. Sind Anschlusswege erwuenscht? [Mediation / Direktgespraech / Settlement vor Klageerhebung]

## 3. `dsfa-fuer-internationale-datentransfers`

**Frühere Beschreibung:** DSFA bei internationalen Datentransfers nach Kapitel V DSGVO: Integration der Transfer Impact Assessment (TIA) in die DSFA, Pruefung Angemessenheit SCC BCR Ausnahmen Art. 49. Output: erweiterte DSFA-Sektion fuer Drittlandbezug.

# DSFA bei internationalen Datentransfers

## Zweck

Erweiterung einer DSFA um die transferbezogene Pruefung nach Kapitel V DSGVO. Wenn die Verarbeitung einen Drittlandtransfer beinhaltet, ist eine Transfer Impact Assessment (TIA) erforderlich, die in die DSFA integriert oder als deren Bestandteil gefuehrt wird. Ergebnis ist eine erweiterte DSFA-Sektion mit Transferregister, Rechtsgrundlage des Transfers, Risikobewertung des Drittlandes und ergaenzenden Massnahmen.

## Wann brauchen Sie diesen Skill

- Bei Auftragsverarbeiter mit Sitz oder Unterauftrag im Drittland
- Bei eigener Niederlassung im Drittland
- Bei US-Cloud-Diensten (auch bei EU-Hosting wegen Zugriffsmoeglichkeit US-Behoerden)
- Bei Konzernintern-Transfers ueber Landesgrenzen
- Bei KI-Anbietern mit Training oder Inferenz im Drittland
- Bei nationalen Sicherheitsgesetzen des Drittlands (z. B. CLOUD Act, FISA 702, China DSL)

## Rechtlicher Rahmen

- Art. 44 DSGVO Grundsatz: jeder Transfer muss eine Rechtsgrundlage in Kapitel V haben.
- Art. 45 DSGVO Angemessenheitsbeschluss der Kommission.
- Art. 46 DSGVO geeignete Garantien (SCC, BCR, Verhaltensregeln, Zertifizierungen).
- Art. 47 DSGVO Binding Corporate Rules.
- Art. 49 DSGVO Ausnahmen fuer besondere Faelle (Einwilligung, Vertragserfuellung, oeffentliche Interessen).
- Schrems II — EuGH Urt. v. 16.07.2020, C-311/18 — Transfer-Pruefungspflicht; TIA erforderlich. (Aktenzeichen verifiziert; sonstige Folgeentscheidungen verifizierungspflichtig.)
- EDSA Leitlinien 04/2022 zu personenbezogenen Datentransfers (Nutzer sollte Aktualitaet prüfen).
- Angemessenheitsbeschluss EU-US Data Privacy Framework (DPF) 10.07.2023, Implementing Decision (EU) 2023/1795.
- SCC Implementing Decision (EU) 2021/914 vom 04.06.2021 mit Modulen 1 bis 4.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welche Daten gehen wohin, an wen, in welcher Form, wie oft, in welchem Umfang?
2. **Verhaeltnismaessigkeitspruefung.** Ist der Drittlandtransfer fuer den Zweck erforderlich, oder gaebe es EU-Alternativen?
3. **Risikoanalyse.**
   - Drittlandrecht: Zugriffsbefugnisse von Behoerden, Rechtsbehelfe Betroffener.
   - Anbieter-Risiko: Branche, Datentyp, Subunternehmer.
   - Daten-Risiko: Sensitivitaet, Aggregation, Identifizierbarkeit.
4. **Massnahmen.**
   - Rechtsgrundlage: Angemessenheitsbeschluss, SCC mit passendem Modul, BCR, Ausnahme Art. 49.
   - Ergaenzende Massnahmen nach EDSA Empfehlungen 01/2020 (verifizierungspflichtig): technisch (Verschluesselung, Schluesselhoheit), vertraglich (Information ueber Behoerdenanfragen), organisatorisch (Audit, Schulung).
5. **Restrisiko.** Pruefung ob die ergaenzenden Massnahmen das Schutzniveau auf das EU-Niveau anheben oder ob das Restrisiko hoch bleibt.
6. **Konsultation / Genehmigung.** DSB-Anhoerung; bei verbleibendem hohem Restrisiko Art. 36 DSGVO Vorabkonsultation; bei US-Anbietern Pruefung DPF-Zertifizierung.

## Mustertext / Template (Transfer-Sektion einer DSFA)

```
TRANSFER IMPACT ASSESSMENT [DATUM]
(Erweiterung der DSFA Sektion 4 / Anlage zur DSFA)

Verantwortlicher: [NAME]
Empfaenger im Drittland: [Name, Land, Konzernverbund]
Sub-AVs: [Liste mit Land]

1. Transferbeschreibung
- Datenkategorien: [...]
- Datenmenge: [...]
- Betroffenenkreise: [...]
- Uebermittlungsweg: [API / SFTP / DB-Replikation]
- Verschluesselung: [Transport / Ruhe / Ende-zu-Ende]
- Schluesselhoheit: [EU / Drittland / Hybrid]

2. Rechtsgrundlage des Transfers
[ ] Angemessenheitsbeschluss Art. 45 DSGVO: [Land, Beschlussdatum]
[ ] SCC Modul: [1 C-C / 2 C-P / 3 P-P / 4 P-C], Datum [...]
[ ] BCR: [Genehmigung, Datum]
[ ] Ausnahme Art. 49 Abs. 1 lit. [a/b/c/...] mit Begruendung
[ ] DPF-Zertifizierung Empfaenger: ja / nein, Stand [Datum]

3. Drittlandrechtspruefung
- Zugriffsbefugnisse Behoerden: [CLOUD Act / FISA 702 / Section 702 / China DSL / Russland TK-Gesetz]
- Rechtsbehelfe Betroffener: [vorhanden / nicht aequivalent]
- Aufsichtsstruktur: [unabhaengig / nicht unabhaengig]
- Pruefung Schrems-II-Standard erfuellt: ja / nein
- Quelle: [EDSA-Laenderbericht, Anbietererklaerung, Stand]

4. Ergaenzende Massnahmen
- Technisch:
  [ ] Ende-zu-Ende-Verschluesselung mit EU-Schluesselhoheit
  [ ] Pseudonymisierung vor Transfer
  [ ] Tokenisierung
  [ ] Split-Processing (sensitive Felder in EU)
- Vertraglich:
  [ ] Transparenz-Pflicht ueber Behoerdenanfragen
  [ ] Audit-Recht
  [ ] Loeschpflicht nach Vertragsende
- Organisatorisch:
  [ ] Anbieterschulung Datenschutz
  [ ] Notfallplan bei Behoerdenzugriff

5. Restrisikobewertung
[GRUEN / GELB / ORANGE / ROT]
Begruendung: [...]

6. Entscheidung
[ ] Transfer zulaessig — Massnahmen umgesetzt
[ ] Transfer zulaessig mit Auflagen
[ ] Vorabkonsultation Art. 36 DSGVO erforderlich
[ ] Transfer nicht zulaessig — Alternative pruefen

7. Ueberwachung
- Naechste Re-Pruefung: [Datum]
- Trigger: [Schrems-III-Folgeurteil / DPF-Status-Aenderung / Anbieterwechsel]

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Typische Fehler

- TIA wird separat vom DSFA-Prozess gefuehrt — Schnittstellen gehen verloren.
- US-Cloud mit EU-Hosting wird als reiner EU-Verarbeitung behandelt — Zugriffsbefugnis US-Behoerden uebersehen.
- SCC-Modul falsch gewaehlt (C-P statt C-C oder umgekehrt).
- Ergaenzende Massnahmen werden nur rechtlich, nicht technisch dokumentiert.
- Ausnahme Art. 49 wird als Daueroption verwendet, obwohl sie nur fuer Einzelfaelle gedacht ist.
- Re-Pruefung nach Schrems-Folgeurteil unterbleibt.
- DPF-Zertifizierung des Anbieters wird nicht jaehrlich nachgeprueft.

## Querverweise

- `datenschutzrecht/skills/drittlandstransfer-pruefung/SKILL.md` — Allgemeine Pruefung
- `datenschutzrecht/skills/standardvertragsklauseln-scc-paket/SKILL.md` — SCC-Pakete
- `datenschutzrecht/skills/us-transfer-tia-dokumentation/SKILL.md` — US-spezifische TIA
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Integration in DSFA
- `datenschutzrecht/skills/spezial-transfer-livequellen-und-rechtsprechungscheck/SKILL.md` — Livequellen
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 44 bis 49 DSGVO
- EuGH Urt. v. 16.07.2020, C-311/18 (Schrems II)
- Durchfuehrungsbeschluss (EU) 2021/914 vom 04.06.2021 (SCC)
- Durchfuehrungsbeschluss (EU) 2023/1795 vom 10.07.2023 (DPF)
- EDSA Leitlinien 04/2022 (Aktualitaet pruefen)
- EDSA Empfehlungen 01/2020 zu ergaenzenden Massnahmen (Aktualitaet pruefen)
- Rechtsprechung: weitere Entscheidungen nicht aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle

## 4. `dsfa-fuer-ki-systeme-schnittstelle-art-26-kivo`

**Frühere Beschreibung:** DSFA fuer KI-Systeme an der Schnittstelle zur KI-Verordnung: Koordination Art. 35 DSGVO mit Art. 26 KI-VO Betreiberpflichten und Art. 27 KI-VO Grundrechte-Folgenabschaetzung. Output: integriertes DSFA-FRIA-Konzept.

# DSFA fuer KI-Systeme an der Schnittstelle zur KI-Verordnung

## Zweck

Koordination einer Datenschutz-Folgenabschaetzung nach Art. 35 DSGVO mit den Anwender- bzw. Betreiberpflichten nach Art. 26 KI-VO und der Grundrechte-Folgenabschaetzung (Fundamental Rights Impact Assessment, FRIA) nach Art. 27 KI-VO. Ergebnis ist ein integriertes Konzept, das DSFA und FRIA koordiniert, ohne sie rechtlich zu verschmelzen.

## Wann brauchen Sie diesen Skill

- Bei Einsatz von Hochrisiko-KI-Systemen nach Anhang III KI-VO (Verordnung EU 2024/1689)
- Bei generativen KI-Diensten, die personenbezogene Daten verarbeiten
- Bei Profiling-Systemen mit Rechtswirkung (Art. 22 DSGVO und Anhang III KI-VO)
- Bei Biometrie, Beschaeftigtenscoring, Kreditscoring, Versicherungsrisikobewertung
- Vor Vertragsschluss mit KI-Anbietern (Anbieter- versus Betreiberrolle)

## Rechtlicher Rahmen

- Art. 35 DSGVO Pflicht-DSFA bei voraussichtlich hohem Risiko, insbesondere bei neuen Technologien (Art. 35 Abs. 1, Abs. 3 lit. a DSGVO).
- Art. 22 DSGVO automatisierte Einzelentscheidung.
- VO (EU) 2024/1689 KI-VO:
  - Art. 6, Anhang III: Hochrisiko-KI-Kategorien
  - Art. 26 Betreiberpflichten (englisch: deployers): bestimmungsgemaesse Nutzung, menschliche Aufsicht, Logging, Information Betroffener
  - Art. 27 Pflicht zur Grundrechte-Folgenabschaetzung (FRIA) fuer bestimmte Betreiber (oeffentliche Stellen, oeffentlich finanzierte Dienste, Kreditwuerdigkeit, Kranken- und Lebensversicherung)
  - Art. 50 Transparenzpflichten generative KI
- EDSA-Stellungnahme 28/2024 zu KI-Modellen (Auslegung DSGVO bei KI).
- EDSA-Leitlinien WP 248 rev.01 zur DSFA.
- Anwendungsbeginn KI-VO: gestaffelt, Hochrisiko-Pflichten 02.08.2026.

## Abgrenzung Anbieter und Betreiber

- Anbieter (provider) entwickelt oder bringt das KI-System in Verkehr und ist primaer adressiert durch Art. 8 bis Art. 21 KI-VO.
- Betreiber (deployer) setzt das KI-System ein und ist adressiert durch Art. 26, 27 KI-VO.
- Die DSGVO-Verantwortlichkeit haengt nicht an dieser Rolle, sondern an der Entscheidung ueber Zwecke und Mittel der Verarbeitung (Art. 4 Nr. 7 DSGVO).
- Praxisregel: Wer ein KI-System fuer eigene Personalentscheidung, Kundenbewertung oder Behoerdenentscheidung nutzt, ist regelmaessig Betreiber nach KI-VO und Verantwortlicher nach DSGVO.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welches KI-System, welcher Zweck, welche Datenarten, welche Betroffenenkreise? Anbieter und Betreiber benennen, Anhang-III-Kategorie pruefen.
2. **Verhaeltnismaessigkeitspruefung.** Notwendigkeit und Verhaeltnismaessigkeit der KI-gestuetzten Verarbeitung; Pruefung ob ein nicht-automatisiertes Verfahren ausreicht. Art. 5 Abs. 1 DSGVO und Erforderlichkeitspruefung.
3. **Risikoanalyse.** Doppelblick:
   - DSGVO-Risiken: Profiling, automatisierte Entscheidung, Trainingsdatenleck, Halluzination ueber Personen.
   - KI-VO-Risiken: Diskriminierung durch Datenbias, fehlende menschliche Aufsicht, fehlende Robustheit.
4. **Massnahmen.** TOMs nach Art. 32 DSGVO plus KI-VO-Massnahmen: menschliche Aufsicht, Logging, Transparenz, Information Betroffener (Art. 26 Abs. 11 KI-VO).
5. **Restrisiko.** Doppelte Restrisikobewertung — fuer DSFA (Art. 35 DSGVO) und fuer FRIA (Art. 27 KI-VO), wenn diese Pflicht besteht.
6. **Konsultation / Genehmigung.** DSB Anhoerung Art. 35 Abs. 2 DSGVO. Bei hohem Restrisiko: Art. 36 DSGVO Vorabkonsultation. Nach KI-VO: nationale Marktueberwachungsbehoerde nach Art. 70 KI-VO ggf. einbinden. Integration in Verarbeitungsverzeichnis und KI-Bestandsverzeichnis.

## Integriertes DSFA-FRIA-Konzept Template

```
INTEGRIERTES DSFA-FRIA-KONZEPT [DATUM]

KI-System: [BEZEICHNUNG, Version, Anbieter]
Betreiber (Verantwortlicher): [NAME]
Anhang-III-Kategorie: [Nummer, Beschreibung]

1. Beschreibung
- KI-Funktion: [Klassifikation / Regression / Generation / Profiling]
- Trainingsdaten Herkunft: [Anbieterangabe]
- Personenbezogene Eingabedaten: [Datenarten, Betroffenenkreise]
- Personenbezogene Ausgabe: [...]

2. Rechtsgrundlage DSGVO
- Art. 6 / Art. 9 DSGVO: [...]
- Art. 22 DSGVO Schutzmechanismus: [Menschenentscheidung / Einwilligung / Vertragserforderlichkeit / Rechtsvorschrift]

3. DSFA nach Art. 35 DSGVO
- Schwellwert: erfuellt durch [Profiling / neue Technologien / sensible Daten]
- Risikoanalyse: [Verweis auf Risikomatrix]
- Massnahmen: [TOMs Art. 32 DSGVO]
- Restrisiko: [GRUEN / GELB / ORANGE / ROT]

4. KI-VO Betreiberpflichten Art. 26
- Bestimmungsgemaesse Nutzung: [...]
- Menschliche Aufsicht Art. 14 KI-VO: [Rollen, Eingriffsmoeglichkeiten]
- Logging Art. 26 Abs. 6 KI-VO: [Aufbewahrungsdauer, Inhalt]
- Information Betroffener Art. 26 Abs. 11 KI-VO: [Form, Zeitpunkt]
- Datenqualitaet bei Inputdaten Art. 26 Abs. 4 KI-VO: [...]

5. FRIA nach Art. 27 KI-VO (falls einschlaegig)
- Beschreibung Einsatz: [Zweck, Zeitraum, Betroffenenkreise]
- Auswirkungen Grundrechte: [Wuerde, Gleichheit, Datenschutz, Meinungsaeusserung]
- Risikomindernde Massnahmen: [...]
- Beobachtung: [...]
- Meldung an nationale Marktueberwachungsbehoerde: [Datum, Aktenzeichen]

6. Vorab-Konsultation
- Art. 36 DSGVO: erforderlich ja / nein
- KI-VO Konsultation Marktueberwachung: erforderlich ja / nein

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
Unterschrift KI-Beauftragter (falls bestellt): ____________________
```

## Typische Fehler

- DSFA und FRIA werden vermischt — beide Instrumente sind rechtlich eigenstaendig und muessen getrennt nachweisbar sein.
- Betreiberpflichten Art. 26 KI-VO werden auf den Anbieter abgeschoben — die Pflicht trifft den Einsetzenden.
- Logging-Pflicht Art. 26 Abs. 6 KI-VO wird mit DSGVO-Loeschpflichten konfligierend behandelt, ohne Pruefung der Rechtsgrundlage des Loggings.
- Anhang III KI-VO wird nicht geprueft — Kategorisierung fehlt.
- KI-Anbieter im Drittland: zusaetzliche Transferpruefung uebersehen (Skill dsfa-fuer-internationale-datentransfers).
- Generative KI: Art. 50 KI-VO Transparenzpflichten uebersehen.

## Querverweise

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Vollvorlage
- `datenschutzrecht/skills/dsfa-restrisiko-und-art-36-konsultation/SKILL.md` — Vorab-Konsultation
- `datenschutzrecht/skills/dsfa-fuer-internationale-datentransfers/SKILL.md` — Drittlandtransfer
- `datenschutzrecht/skills/ki-verordnung-compliance/SKILL.md` — KI-VO Compliance
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35, 36, 22 DSGVO
- VO (EU) 2024/1689 KI-VO, insbesondere Art. 6, 14, 26, 27, 50, Anhang III
- EDSA-Stellungnahme 28/2024 zu KI-Modellen
- EDSA-Leitlinien WP 248 rev.01
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle

## 5. `dsfa-methodik-cnil-pia-vs-bsfd-bsi`

**Frühere Beschreibung:** Vergleich der DSFA-Methoden: CNIL PIA Software (Frankreich) gegenueber dem BSI Standard-Datenschutzmodell (SDM) und dem BSFD-Ansatz. Output: Methodenwahl mit Begruendung, Anwendungshinweisen und Werkzeugauswahl.

# DSFA-Methodik CNIL PIA versus SDM/BSI

## Zweck

Vergleich der drei in Deutschland und Frankreich gaengigen DSFA-Methoden — CNIL PIA Software, Standard-Datenschutzmodell (SDM) der Datenschutzkonferenz und der BSI-Bausteine zum Standard-Datenschutz — und Auswahl der jeweils passenden Methodik fuer die konkrete Mandantenkonstellation. Ergebnis ist eine begruendete Methodenwahl mit Werkzeughinweis.

## Wann brauchen Sie diesen Skill

- Vor der Erstdurchfuehrung einer DSFA, wenn keine Hausmethodik vorgegeben ist
- Beim Aufbau eines Datenschutzmanagementsystems (DSMS)
- Wenn die Aufsichtsbehoerde eine methodische Begruendung verlangt
- Bei grenzueberschreitenden Verarbeitungen (Frankreich-Bezug erleichtert CNIL-PIA)

## Rechtlicher Rahmen

- Art. 35 Abs. 7 DSGVO Mindestinhalte der DSFA — methodenoffen.
- EDSA-Leitlinien WP 248 rev.01 verweisen auf etablierte Methoden, ohne eine vorzuschreiben.
- CNIL PIA Methodology (Privacy Impact Assessment): freie Software der franzoesischen Datenschutzbehoerde CNIL, modular, dreiteilig (Knowledge Base, Methodology, Templates).
- Standard-Datenschutzmodell (SDM) der Datenschutzkonferenz: Schutzziele Vertraulichkeit, Integritaet, Verfuegbarkeit, Transparenz, Intervenierbarkeit, Nicht-Verkettung, Datenminimierung; Referenz fuer Aufsichtsverfahren in Deutschland.
- BSI-Grundschutz mit Datenschutz-Baustein: technische Bausteine mit Bezug zu Schutzbedarfsfeststellung; nicht primaer DSFA-spezifisch, aber kompatibel.

## Methoden im Vergleich

| Merkmal | CNIL PIA | SDM (DSK) | BSI-Grundschutz |
|---|---|---|---|
| Rechtsrahmen | DSGVO (FR) | DSGVO (DE) | IT-Sicherheit primaer |
| Werkzeug | Open-Source-Software | Methodenpapier | Kompendium |
| Risikomodell | Schadensszenarien | Schutzziele | Schutzbedarf |
| Strukturtiefe | hoch (sehr granular) | hoch (rechtlich praezise) | mittel (technikfokus) |
| Aufsichtsakzeptanz DE | gut | sehr gut | gut bei TOM |
| Aufsichtsakzeptanz FR | sehr gut | -- | -- |
| Eignung KI-Systeme | gut | sehr gut (Schutzziele) | begrenzt |
| Eignung TOM Art. 32 | mittel | gut | sehr gut |

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Was wird verarbeitet, wer ist Verantwortlicher, in welcher Jurisdiktion?
2. **Verhaeltnismaessigkeitspruefung.** Welche Methodik passt zur Verarbeitung? Standortbezug DE: SDM bevorzugt; FR-Bezug: CNIL PIA; reine TOM-Fragen: BSI-Bausteine ergaenzend.
3. **Risikoanalyse.** Methodisches Risikomodell waehlen: Schadensszenarien (CNIL), Schutzziele (SDM) oder Schutzbedarf (BSI).
4. **Massnahmen.** Methode steuert die Massnahmenstruktur: CNIL fragt pro Szenario, SDM pro Schutzziel, BSI pro Baustein.
5. **Restrisiko.** Methodenwahl beeinflusst Bewertungsmassstab; bei Hybridansatz beide Skalen dokumentieren.
6. **Konsultation / Genehmigung.** DSB-Anhoerung; Methodenwahl in der DSFA explizit begruenden.

## Mustertext / Template (Methodenwahl-Memo)

```
METHODENWAHL DSFA [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME] | Sitzland: [DE/FR/...]

1. Methodenkandidaten
- CNIL PIA Software (Version [X], Sprache [DE/EN/FR])
- Standard-Datenschutzmodell SDM (Version V3.0)
- BSI-Grundschutz Datenschutz-Baustein

2. Bewertung
- Aufsichtsakzeptanz: [Begruendung]
- Werkzeugverfuegbarkeit: [Lizenz, Sprache, Schulung]
- Eignung Risikotyp: [...]
- Eignung TOM: [...]

3. Methodenwahl
[ ] CNIL PIA (Software-gestuetzt, modular, Schadensszenarien)
[ ] SDM (Schutzziele, DE-Aufsicht, KI-tauglich)
[ ] BSI ergaenzend fuer TOM Art. 32
[ ] Hybrid: SDM-Hauptmethodik plus BSI fuer TOM

4. Begruendung
[Warum diese Methode fuer diese Verarbeitung]

5. Werkzeug
- CNIL: cnil.fr/de/das-pia-tool-software-die-die-durchfuehrung-von-datenschutz
- SDM: datenschutzkonferenz-online.de/standard-datenschutzmodell.html
- BSI: bsi.bund.de/grundschutz

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Werkzeug-Hinweise zur Auswahl

- CNIL PIA Software: kostenfrei, Open Source, mehrsprachig (DE-Lokalisierung verfuegbar), Export PDF und XML.
- SDM V3.0: Methodenbeschreibung der DSK, frei verfuegbar, keine Software, sondern Pruefkatalog.
- BSI-Grundschutz: Kompendium mit Bausteinen, GSTOOL bzw. verinice als Werkzeug.
- Hybridansatz Empfehlung: SDM als methodische Klammer, CNIL PIA Software fuer strukturierte Risikoszenarien, BSI fuer TOM nach Art. 32 DSGVO.

## Anwendungsfaelle

- KI-System mit Profiling: SDM bevorzugt, weil Schutzziele die KI-typischen Risiken (Transparenz, Nicht-Verkettung) sauber adressieren.
- Cloud-Migration mit US-Anbieter: CNIL PIA Software fuer Risikoszenarien plus BSI-Bausteine fuer technische Schutzmassnahmen.
- Beschaeftigtenverarbeitung mit Mitbestimmung: SDM mit ergaenzendem Stakeholder-Modul.
- Forschungsverarbeitung mit besonderen Kategorien: SDM und CNIL PIA kombinieren; Beweislast-Aspekt nach Art. 5 Abs. 2 DSGVO mitfuehren.

## Typische Fehler

- Methode wird nicht explizit gewaehlt — Aufsicht verlangt Begruendung.
- CNIL PIA wird wegen schoener Software gewaehlt, ohne dass die Schutzziele DE adressiert werden.
- BSI-Grundschutz wird als DSFA-Ersatz behandelt — er ist primaer Sicherheitsmethodik.
- Hybridansatz wird gewaehlt, ohne die Schnittstellen zu definieren — Doppelarbeit oder Luecken.
- Sprache der Methodenartefakte passt nicht zur Aufsicht (CNIL-Output franzoesisch bei deutscher Aufsicht).
- Methodenwahl wird im Projektverlauf gewechselt — kein Quervergleich der Risikobewertung mehr moeglich.
- Aufsichtshinweise zur Methodenfreiheit werden als Beliebigkeit verstanden — die Methode muss zur Verarbeitung passen.

## Querverweise

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Vollvorlage DE
- `datenschutzrecht/skills/dpia-en-template-full-version/SKILL.md` — Englische Vollvorlage
- `datenschutzrecht/skills/dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden/SKILL.md` — Risikoanalyse
- `datenschutzrecht/skills/dsfa-fuer-ki-systeme-schnittstelle-art-26-kivo/SKILL.md` — KI-DSFA
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35 Abs. 7 DSGVO
- EDSA-Leitlinien WP 248 rev.01
- CNIL: cnil.fr — PIA Software, Knowledge Base, Methodology, Templates
- DSK Datenschutzkonferenz: datenschutzkonferenz-online.de — SDM V3.0
- BSI: bsi.bund.de — Grundschutz-Kompendium, Baustein zum Datenschutz
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle

## 6. `dsfa-restrisiko-und-art-36-konsultation`

**Frühere Beschreibung:** Restrisiko nach Massnahmen bewerten und Vorab-Konsultation Art. 36 DSGVO vorbereiten. Output: Konsultationsantrag mit Verarbeitungsbeschreibung Massnahmen Restrisiko Begruendung warum die Konsultation erforderlich ist.

# Restrisiko und Vorab-Konsultation nach Art. 36 DSGVO

## Zweck

Bewertung des Restrisikos nach Umsetzung der DSFA-Massnahmen und, falls erforderlich, Vorbereitung der Vorab-Konsultation bei der zustaendigen Aufsichtsbehoerde nach Art. 36 DSGVO. Ergebnis ist ein vollstaendiger Konsultationsantrag mit Verarbeitungsbeschreibung, Massnahmen, Restrisiko und Begruendung der Konsultationsnotwendigkeit.

## Wann brauchen Sie diesen Skill

- Wenn die DSFA-Risikoanalyse nach Massnahmen ein hohes Restrisiko ergibt
- Wenn die Aufsichtsbehoerde von sich aus eine Konsultation anregt
- Bei besonders sensiblen Verarbeitungen, bei denen die Konsultation reputationsklug erscheint
- Vor Einfuehrung neuer Hochrisiko-Technologien (KI nach Anhang III KI-VO, Biometrie)

## Rechtlicher Rahmen

- Art. 36 Abs. 1 DSGVO: Konsultationspflicht bei voraussichtlich hohem Risiko trotz Massnahmen.
- Art. 36 Abs. 2 DSGVO: Aufsichtsbehoerde hat 8 Wochen zur schriftlichen Empfehlung, verlaengerbar um 6 Wochen bei komplexen Faellen.
- Art. 36 Abs. 3 DSGVO: erforderlicher Inhalt des Konsultationsersuchens (Verantwortliche, Aufgabenteilung, Zwecke, Massnahmen, Kontaktdaten DSB, DSFA, sonstige Informationen).
- Art. 36 Abs. 4 DSGVO: Konsultation bei gesetzgeberischen Massnahmen.
- Art. 36 Abs. 5 DSGVO: nationale Sonderregeln zur Voraberlaubnis oder Vorabkonsultation.
- Art. 58 Abs. 3 lit. a DSGVO: Aufsichtsbehoerden duerfen Empfehlungen aussprechen oder Verarbeitung untersagen.
- Art. 83 Abs. 4 lit. a DSGVO: Bussgeldtatbestand bei Verstoss gegen Art. 36.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Vollstaendige Beschreibung aus der DSFA uebernehmen — Zweck, Datenarten, Betroffene, Empfaenger, Technologie, Drittlandbezug.
2. **Verhaeltnismaessigkeitspruefung.** Wurde die Verhaeltnismaessigkeitspruefung der DSFA mit nachvollziehbarem Ergebnis abgeschlossen? Wenn nein, zurueck zur DSFA.
3. **Risikoanalyse.** Risikomatrix vor und nach Massnahmen; Identifizierung der Szenarien, die im hohen Bereich verbleiben.
4. **Massnahmen.** Sind alle technisch und organisatorisch zumutbaren Massnahmen ergriffen? Pruefung Art. 32 DSGVO, Stand der Technik, Implementierungskosten gegen Risikoreduktion.
5. **Restrisiko.** Wenn hoch verbleibend: Art. 36 Konsultation Pflicht. Begruendung warum das Restrisiko nicht weiter reduzierbar ist (Wirtschaftlichkeit, technische Grenzen, gesetzlicher Zweck).
6. **Konsultation / Genehmigung.** Konsultationsantrag an die zustaendige Aufsichtsbehoerde mit den Inhalten nach Art. 36 Abs. 3 DSGVO. Frist 8 Wochen; Verarbeitung darf bis zur Antwort nicht aufgenommen werden.

## Mustertext / Template (Konsultationsantrag)

```
VORAB-KONSULTATION NACH ART. 36 DSGVO
[DATUM, AKTENZEICHEN intern]

An: [Zustaendige Aufsichtsbehoerde, Anschrift]

Antragsteller (Verantwortlicher)
- Name / Firma: [...]
- Sitz: [...]
- Kontaktdaten: [...]
- DSB: [Name, E-Mail]

Falls gemeinsam Verantwortliche oder Auftragsverarbeiter beteiligt
- Rollen und Aufgabenteilung nach Art. 26 / Art. 28 DSGVO: [...]

1. Beschreibung der Verarbeitung
[Zweck, Datenarten, Betroffene, Technologie, Aufbewahrung, Drittlandbezug]

2. Rechtsgrundlage
[Art. 6 / Art. 9 DSGVO, ggf. § ... BDSG / Spezialgesetz]

3. DSFA Zusammenfassung
[Schwellwertanalyse, Risikobewertung, Massnahmen, Restrisiko]

4. Restrisiko
[Welche Szenarien bleiben im hohen Bereich? Warum nicht weiter reduzierbar?]

5. Geplante Massnahmen
[Technisch, organisatorisch, vertraglich]

6. Begruendung der Konsultation
[Warum nach Massnahmen weiterhin voraussichtlich hohes Risiko nach Art. 36 Abs. 1 DSGVO]

7. Anlagen
- DSFA in vollstaendiger Fassung
- AVV-Entwurf
- Datenflussdiagramm
- DSB-Stellungnahme
- TOM-Konzept

Mit freundlichen Gruessen
[Unterschrift Verantwortlicher]
[Unterschrift DSB]
```

## Hinweise zur Frist

- 8 Wochen Antwortfrist Art. 36 Abs. 2 DSGVO ab vollstaendigem Eingang.
- Verlaengerung um 6 Wochen moeglich, schriftlich mitzuteilen.
- Verarbeitungsbeginn vor Antwort: Pflichtverletzung, kann Anordnung und Bussgeld ausloesen (Art. 58, Art. 83 DSGVO).
- Wenn Aufsichtsbehoerde untersagt: aufschiebende Wirkung beachten; Rechtsbehelfe nach VwGO bzw. § 20 BDSG.

## Typische Fehler

- Restrisiko wird kuenstlich kleingerechnet, um Art. 36 zu vermeiden — bei spaeterem Vorfall verdoppelter Vorwurf (Materialfehler plus Verfahrensfehler).
- Antrag enthaelt keine Aufgabenteilung gemeinsam Verantwortlicher.
- DSFA wird nicht beigefuegt — Antrag wird zurueckgewiesen.
- Verarbeitung wird vor Antwort der Aufsicht aufgenommen.
- Frist 8 Wochen wird nicht im Projektplan beruecksichtigt.
- Anlagen fehlen — Aufsichtsbehoerde fordert nach und Frist beginnt erst dann.

## Querverweise

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Vollvorlage
- `datenschutzrecht/skills/dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden/SKILL.md` — Restrisiko-Berechnung
- `datenschutzrecht/skills/dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii/SKILL.md` — Dokumentation
- `datenschutzrecht/skills/dsfa-fuer-ki-systeme-schnittstelle-art-26-kivo/SKILL.md` — KI-DSFA und Konsultation
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 36 Abs. 1, 2, 3, 4, 5 DSGVO
- Art. 35 Abs. 11 DSGVO
- Art. 58, 83 DSGVO
- EDSA-Leitlinien WP 248 rev.01
- BfDI / Landesbehoerden — Verfahrenshinweise zur Vorabkonsultation
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle

## 7. `dsfa-stakeholder-konsultation-art-35-9`

**Frühere Beschreibung:** Konsultation der Betroffenen oder ihrer Vertreter nach Art. 35 Abs. 9 DSGVO im Rahmen einer DSFA: Pruefung Erforderlichkeit Form Reichweite Dokumentation. Output: Konsultationsplan mit Begruendung Form und Dokumentation.

# Stakeholder-Konsultation nach Art. 35 Abs. 9 DSGVO

## Zweck

Pruefung und Strukturierung der Konsultation Betroffener oder ihrer Vertreter im Rahmen einer DSFA. Art. 35 Abs. 9 DSGVO sieht vor, dass der Verantwortliche, soweit angemessen, den Standpunkt Betroffener oder ihrer Vertreter einholt. Ergebnis dieses Skills ist ein dokumentierter Konsultationsplan mit Begruendung, Form, Reichweite und Verwertung des Ergebnisses.

## Wann brauchen Sie diesen Skill

- Bei DSFA mit Beschaeftigtendaten (Betriebsrat als Vertretung)
- Bei DSFA mit Patientendaten oder Kundendaten in grossem Umfang
- Bei oeffentlichen Konsultationen (z. B. Smart-City-Projekte)
- Wenn die Aufsichtsbehoerde im Vorabkonsultationsverfahren Art. 36 Stakeholder-Beteiligung erwartet
- Bei KI-Systemen, die viele Betroffene treffen

## Rechtlicher Rahmen

- Art. 35 Abs. 9 DSGVO: Der Verantwortliche holt gegebenenfalls den Standpunkt der betroffenen Personen oder ihrer Vertreter zu der beabsichtigten Verarbeitung ein, unbeschadet des Schutzes gewerblicher oder oeffentlicher Interessen oder der Sicherheit der Verarbeitungsvorgaenge.
- § 26 BDSG, BetrVG (§§ 87, 90, 94): Beteiligung des Betriebsrats bei Beschaeftigtendatenverarbeitungen mit Mitbestimmungsbezug.
- EDSA-Leitlinien WP 248 rev.01 zur Konsultation.
- EDSA-Stellungnahmen zur Konsultation in komplexen Verarbeitungen.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welche Verarbeitung? Welche Betroffenenkreise? Gibt es etablierte Vertretungen (Betriebsrat, Patientenvertretung, Verbraucherverbaende)?
2. **Verhaeltnismaessigkeitspruefung.** Ist eine Konsultation angemessen (Art. 35 Abs. 9 verlangt nur soweit angemessen)? Faktoren: Eingriffstiefe, Anzahl Betroffener, Erkennbarkeit der Verarbeitung, Existenz strukturierter Vertretung.
3. **Risikoanalyse.** Risiken bei Konsultation: Geheimhaltungsinteressen, Wettbewerb, Sicherheitsrisiken. Risiken ohne Konsultation: Reputationsverlust, Aufsichtsanstoss, Akzeptanzproblem.
4. **Massnahmen / Form der Konsultation.**
   - Schriftliche Konsultation des Betriebsrats mit Beschreibung der Verarbeitung
   - Umfrage unter Betroffenenstichprobe
   - Workshop oder Diskussionsrunde
   - Oeffentliche Anhoerung (oeffentliche Stellen)
   - Verbaendekonsultation (Verbraucherzentralen, Datenschutzvereine)
5. **Restrisiko.** Bewertung des Konsultationsergebnisses und Eingang in die DSFA. Wenn Konsultation unterbleibt: Begruendung dokumentieren (Art. 35 Abs. 9 Halbsatz 2 — Schutzinteressen).
6. **Konsultation / Genehmigung.** DSB einbinden; Ergebnis der Stakeholder-Konsultation explizit in der DSFA verarbeiten.

## Mustertext / Template

```
STAKEHOLDER-KONSULTATION DSFA [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME]

1. Betroffenenkreise
- [Beschaeftigte / Kunden / Patienten / Buerger / ...]
- Anzahl (ca.): [X]

2. Identifizierte Vertretungen
- Betriebsrat: [Ansprechpartner, BetrVG-Bezug]
- Verbraucherverband: [...]
- Sonstige: [...]

3. Angemessenheit der Konsultation
[ ] erforderlich (Begruendung: [...])
[ ] entbehrlich (Begruendung Art. 35 Abs. 9 Halbsatz 2: [...])

4. Form der Konsultation
[ ] schriftliche Stellungnahme Betriebsrat (BetrVG §§ 87, 90, 94)
[ ] strukturierte Umfrage (Stichprobe N=[X])
[ ] Workshop / Diskussionsrunde
[ ] oeffentliche Anhoerung
[ ] Verbaendebeteiligung

5. Zeitplan
- Versand / Einladung: [DATUM]
- Rueckmeldefrist: [DATUM]
- Auswertung: [DATUM]
- Aufnahme in DSFA: [DATUM]

6. Verwertung
[Wie wird das Ergebnis in der DSFA verarbeitet? Welche Punkte fuehren zu Massnahmen-Anpassungen?]

7. Schutzinteressen
[Welche Informationen sind aus Gruenden Wettbewerb / Sicherheit / Geheimhaltung nicht offengelegt? Begruendung.]

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Beispielfaelle Konsultationspflicht

- KI-Personalauswahl im Konzern: schriftliche Stellungnahme Betriebsrat plus Mitarbeiterumfrage.
- Patientenakten-Migration in Cloud: Patientenvertretung anhoeren, Patienteninformation vorbereiten.
- Smart-City-Sensorik: oeffentliche Anhoerung, Verbaendebeteiligung Datenschutzverein.
- Connected-Vehicle-Telematik: Verbraucherverbaende anhoeren, ggf. Nutzerstichprobe.
- Schueler-Lernplattform: Eltern- und Schuelervertretung anhoeren, Landesdatenschutz informieren.

## Form der Dokumentation

- Verteilte Fragenliste mit Datum, Empfaengerkreis, Rueckmeldefrist.
- Eingaenge protokolliert mit Datum und Eingangsnummer.
- Auswertung mit Begruendung welche Hinweise wie in die DSFA eingeflossen sind.
- Nicht aufgenommene Hinweise mit Begruendung der Nicht-Beruecksichtigung.
- Anonymisierung der Stellungnahmen wenn personenbezogen.

## Typische Fehler

- Konsultation wird ganz unterlassen ohne dokumentierte Begruendung — Verstoss gegen Art. 35 Abs. 9 und Art. 5 Abs. 2 DSGVO.
- Konsultation wird nur formal durchgefuehrt, Ergebnis nicht in die DSFA aufgenommen.
- Betriebsrat wird umgangen, obwohl Mitbestimmung nach BetrVG ausgeloest ist.
- Konsultation wird nach DSFA-Abschluss durchgefuehrt — verfehlt den Zweck der Risikoabwaegung.
- Schutzinteressen werden pauschal behauptet ohne konkrete Begruendung.
- Bei oeffentlichen Stellen werden Beteiligungsrechte nach Landesrecht uebersehen.
- Eingaenge der Stakeholder werden nicht im Verarbeitungsverzeichnis Art. 30 verlinkt.

## Querverweise

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Aufnahme in Vollvorlage
- `datenschutzrecht/skills/dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden/SKILL.md` — Risikoanalyse
- `datenschutzrecht/skills/dsfa-restrisiko-und-art-36-konsultation/SKILL.md` — Aufsichtskonsultation
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35 Abs. 9 DSGVO
- § 26 BDSG; §§ 87, 90, 94 BetrVG
- EDSA-Leitlinien WP 248 rev.01
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle

## 8. `dsfa-template-deutsch-vollvorlage`

**Frühere Beschreibung:** Deutsche DSFA-Vollvorlage nach Art. 35 Abs. 7 DSGVO mit ausgefuellten Platzhaltern fuer alle sechs Pflichtsektionen Beschreibung Verhaeltnismaessigkeit Risiken Massnahmen Restrisiko Freigabe. Output: vollstaendige DSFA-Vorlage zum Befuellen.

# DSFA-Vollvorlage Deutsch

## Zweck

Vollstaendige deutsche Vorlage einer Datenschutz-Folgenabschaetzung nach Art. 35 Abs. 7 DSGVO. Alle sechs Pflichtsektionen sind enthalten und mit Platzhaltern vorausgefuellt, so dass eine Kanzlei oder ein Unternehmen die DSFA direkt befuellen und der Aufsicht oder dem DSB vorlegen kann. Die Vorlage folgt der methodischen Struktur Beschreibung, Verhaeltnismaessigkeit, Risiken, Massnahmen, Restrisiko, Freigabe.

## Wann brauchen Sie diesen Skill

- Wenn die Trigger-Pruefung ergeben hat, dass eine DSFA durchzufuehren ist
- Wenn ein Hausformat fehlt und ein kanzleitaugliches Standardformat benoetigt wird
- Wenn die Aufsichtsbehoerde eine schriftliche DSFA anfordert
- Vor Vorabkonsultation nach Art. 36 DSGVO

## Rechtlicher Rahmen

- Art. 35 Abs. 7 DSGVO Mindestinhalte:
  - lit. a systematische Beschreibung der Verarbeitungsvorgaenge und Zwecke
  - lit. b Bewertung der Notwendigkeit und Verhaeltnismaessigkeit
  - lit. c Bewertung der Risiken fuer die Rechte und Freiheiten der Betroffenen
  - lit. d Abhilfemassnahmen mit Garantien und Sicherheitsvorkehrungen
- Art. 35 Abs. 2 DSGVO DSB-Anhoerung.
- Art. 35 Abs. 9 DSGVO Stakeholder-Konsultation soweit angemessen.
- Art. 5 Abs. 2 DSGVO Rechenschaftspflicht.
- EDSA-Leitlinien WP 248 rev.01.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Sektion 1 der Vorlage befuellen.
2. **Verhaeltnismaessigkeitspruefung.** Sektion 2.
3. **Risikoanalyse.** Sektion 3 mit Risikomatrix.
4. **Massnahmen.** Sektion 4.
5. **Restrisiko.** Sektion 5.
6. **Konsultation / Genehmigung.** Sektion 6 mit Unterschriften.

## Mustertext / Vollvorlage Deutsch

```
DATENSCHUTZ-FOLGENABSCHAETZUNG (DSFA)
nach Art. 35 DSGVO

Aktenzeichen intern: [...]
Version: [1.0] | Datum: [TT.MM.JJJJ]
Verantwortlicher: [Firma, Anschrift, Vertretung]
DSB: [Name, E-Mail, Telefon]
Federfuehrend (Fachabteilung): [...]
Klassifikation: [vertraulich / intern]

DECKBLATT
Verarbeitungsvorgang: [Bezeichnung]
Rechtsgrundlage: [Art. 6 / Art. 9 DSGVO, ggf. § BDSG / Spezialgesetz]
Zustaendige Aufsichtsbehoerde: [BfDI / LfDI ...]
Stand der Versionen: [Aenderungshistorie]

EXECUTIVE SUMMARY (1 Seite)
Zweck: [...]
Datenarten: [...]
Betroffene: [...]
Gesamtrisiko vor Massnahmen: [HOCH / MITTEL / GERING]
Gesamtrisiko nach Massnahmen: [HOCH / MITTEL / GERING]
Freigabeempfehlung: [Ja / Vorab-Konsultation Art. 36 / Nein]

1. BESCHREIBUNG DER VERARBEITUNGSTAETIGKEIT
   (Art. 35 Abs. 7 lit. a DSGVO)
1.1 Zweck und Art der Verarbeitung
[...]
1.2 Datenkategorien
- Stammdaten: [...]
- Inhaltsdaten: [...]
- Nutzungsdaten: [...]
- Besondere Kategorien Art. 9: [...]
- Strafrechtliche Daten Art. 10: [...]
1.3 Betroffene Personengruppen
[Kunden / Beschaeftigte / Patienten / Buerger]
1.4 Empfaenger und Uebermittlungen
- Interne Stellen: [...]
- Externe Auftragsverarbeiter: [...]
- Drittland: [Land, Garantien]
1.5 Aufbewahrungsfristen
[Frist, Loeschkonzept]
1.6 Technische Umgebung
[Hosting, Sub-AVs, Betriebssystem, Verschluesselung]
1.7 Datenfluss
[Diagramm-Verweis oder Kurzbeschreibung]

2. BEWERTUNG DER NOTWENDIGKEIT UND VERHAELTNISMAESSIGKEIT
   (Art. 35 Abs. 7 lit. b DSGVO)
2.1 Erforderlichkeit der Verarbeitung fuer den Zweck
[Geeignet, erforderlich, kein milderes Mittel]
2.2 Datenminimierung (Art. 5 Abs. 1 lit. c DSGVO)
[...]
2.3 Zweckbindung (Art. 5 Abs. 1 lit. b DSGVO)
[...]
2.4 Speicherbegrenzung (Art. 5 Abs. 1 lit. e DSGVO)
[...]
2.5 Rechtmaessigkeit (Art. 6, ggf. Art. 9 DSGVO)
[Rechtsgrundlage je Datenkategorie / Betroffenengruppe]
2.6 Betroffenenrechte
[Wie sind Auskunft, Berichtigung, Loeschung, Einschraenkung, Datenuebertragbarkeit, Widerspruch sichergestellt?]
2.7 Transparenz Art. 12 ff. DSGVO
[...]

3. RISIKOANALYSE
   (Art. 35 Abs. 7 lit. c DSGVO)
3.1 Risikomatrix vor Massnahmen
| Nr | Szenario                          | Wahrsch. | Schwere | Risiko |
|----|-----------------------------------|----------|---------|--------|
| 1  | Unbefugter Zugriff (Vertraul.)    | [h/m/g]  | [h/m/g] | [R/O/G/Gn] |
| 2  | Datenleck nach aussen             |          |         |        |
| 3  | Verdecktes Profiling              |          |         |        |
| 4  | Datenverlust / Verfuegbarkeit     |          |         |        |
| 5  | Manipulation / Integritaet        |          |         |        |
| 6  | Diskriminierung Betroffener       |          |         |        |
| 7  | Identitaetsdiebstahl              |          |         |        |
3.2 Schutzziele beruehrt
[Vertraulichkeit / Integritaet / Verfuegbarkeit / Transparenz / Intervenierbarkeit / Nicht-Verkettung / Datenminimierung]
3.3 Schutzbeduerftige Personen
[Kinder / Patienten / Beschaeftigte / Verbraucher]

4. ABHILFEMASSNAHMEN
   (Art. 35 Abs. 7 lit. d DSGVO)
4.1 Technische Massnahmen (Art. 32 DSGVO)
- Verschluesselung: [Art, Schluessellaenge]
- Pseudonymisierung: [...]
- Zugriffskontrolle: [Rolle / Recht-Konzept]
- Protokollierung: [...]
- Sicherung / Backup: [...]
- Stand der Technik: [...]
4.2 Organisatorische Massnahmen
- Schulungen: [Zielgruppe, Frequenz]
- Vier-Augen-Prinzip: [...]
- Berechtigungskonzept: [...]
- Notfallplan / Incident Response: [...]
4.3 Vertragliche Massnahmen
- AVV (Art. 28 DSGVO): [Anbieter, Datum, Version]
- SCC bei Drittlandtransfer: [Modul, Datum]
- TIA: [Verweis]
4.4 Massnahmen-Tabelle
| Nr | Risiko | Massnahme | Verantwortlich | Frist | Restrisiko |

5. RESTRISIKO
5.1 Risikomatrix nach Massnahmen
[Tabelle wie 3.1 mit Werten nach Massnahmen]
5.2 Bewertung Restrisiko
[Verbleibendes Risiko pro Szenario; Gesamtbewertung]
5.3 Erforderlichkeit Art. 36 DSGVO
[ ] Keine Konsultation erforderlich (Restrisiko mittel oder gering)
[ ] Vorab-Konsultation Art. 36 DSGVO erforderlich (Restrisiko hoch)

6. KONSULTATION UND FREIGABE
6.1 DSB-Stellungnahme (Art. 35 Abs. 2 DSGVO)
[Wortlaut oder Verweis auf Anlage]
Unterschrift DSB: ____________________ Datum: ____________________

6.2 Stakeholder-Konsultation (Art. 35 Abs. 9 DSGVO)
[Durchgefuehrt / nicht durchgefuehrt mit Begruendung]

6.3 Freigabe Verantwortlicher
Name: ____________________
Funktion: ____________________
Unterschrift: ____________________ Datum: ____________________

6.4 Aufnahme in Verarbeitungsverzeichnis Art. 30 DSGVO
Verweis: [...]

6.5 Ueberpruefungsplan (Art. 35 Abs. 11 DSGVO)
Naechste Pruefung: [DATUM]
Trigger fuer ausserplanmaessige Pruefung: [Aenderung Datenarten / Empfaenger / Technologie / Rechtslage]
```

## Typische Fehler

- Vorlage wird verwendet, ohne den Datenfluss konkret zu beschreiben — Sektion 1 bleibt floskelhaft.
- Verhaeltnismaessigkeit wird auf Rechtsgrundlage reduziert — Datenminimierung und Speicherbegrenzung werden uebersehen.
- Risikoszenarien werden nur fuer Vertraulichkeit gepflegt, andere Schutzziele bleiben leer.
- Massnahmen-Tabelle ohne Verantwortliche und Fristen — nicht steuerbar.
- DSB unterschreibt nicht oder spaeter — Beweisluecke.
- Versionierung fehlt — bei Aenderung nicht nachvollziehbar.

## Querverweise

- `datenschutzrecht/skills/dpia-en-template-full-version/SKILL.md` — Englische Vollvorlage
- `datenschutzrecht/skills/dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden/SKILL.md` — Risikomethodik
- `datenschutzrecht/skills/dsfa-stakeholder-konsultation-art-35-9/SKILL.md` — Stakeholder
- `datenschutzrecht/skills/dsfa-update-bei-aenderungen-und-revision/SKILL.md` — Update
- `datenschutzrecht/skills/dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii/SKILL.md` — Dokumentation
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35 Abs. 7 DSGVO Mindestinhalte
- Art. 35 Abs. 2, 9, 11 DSGVO
- Art. 5 Abs. 2 DSGVO Rechenschaftspflicht
- Art. 30, 32 DSGVO
- EDSA-Leitlinien WP 248 rev.01
- SDM V3.0 — Schutzziele
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle

## 9. `dsfa-typische-fehler-bei-erstpruefung`

**Frühere Beschreibung:** Katalog typischer Fehler bei der DSFA-Erstpruefung und Gegenmassnahmen. Output: Fehlerkatalog mit Pruefliste fuer DSB und Verantwortliche samt Beispielen aus Aufsichtspraxis.

# Typische Fehler bei der DSFA-Erstpruefung

## Zweck

Strukturierter Katalog der typischen Fehler bei der ersten Durchfuehrung einer DSFA, einschliesslich Gegenmassnahmen, Vermeidungsstrategien und Verweis auf die jeweils einschlaegigen Skills. Ergebnis ist eine Pruefliste fuer DSB und Verantwortliche, die vor Freigabe einer DSFA durchgegangen wird.

## Wann brauchen Sie diesen Skill

- Vor Freigabe einer DSFA durch den Verantwortlichen
- Bei Audit einer bestehenden DSFA
- In der Schulung neuer DSB oder Datenschutz-Koordinatoren
- Bei Aufsichtsanfrage zur Plausibilisierung einer durchgefuehrten DSFA
- Bei Re-Pruefung nach Art. 35 Abs. 11 DSGVO

## Rechtlicher Rahmen

- Art. 35 DSGVO mit allen Absaetzen.
- Art. 5 Abs. 2 DSGVO Rechenschaftspflicht.
- Art. 83 Abs. 4 lit. a DSGVO Bussgeldtatbestand fuer Verstoesse gegen Art. 35.
- EDSA-Leitlinien WP 248 rev.01 und einschlaegige Aufsichtsbehoerdenpraxis.

## Fehlerkatalog mit Gegenmassnahmen

### 1. Triage-Phase

- Trigger-Pruefung ohne dokumentierten Vermerk; nur muendlich. Gegenmassnahme: Triage-Vermerk gemaess Skill dsfa-art-35-dsgvo-trigger-und-anwendungsbereich.
- Nur Art. 35 Abs. 3 DSGVO geprueft, Generalklausel Abs. 1 uebersehen. Gegenmassnahme: Doppelblick auf Generalklausel und Regelbeispiele.
- Blacklist der eigenen Landesbehoerde uebersehen. Gegenmassnahme: Skill dsfa-bfdi-und-laender-blacklist.
- EDSA-Kriterien nicht durchgepruft. Gegenmassnahme: Skill dsfa-edpb-leitlinien-9-19-anwendung.

### 2. Beschreibung der Verarbeitung

- Beschreibung floskelhaft, ohne Datenfluss. Gegenmassnahme: Datenflussdiagramm und konkrete Empfaengeraufzaehlung.
- Drittlandbezug uebersehen, weil EU-Hosting. Gegenmassnahme: Zugriffsbefugnis pruefen, Skill dsfa-fuer-internationale-datentransfers.
- Sub-Auftragsverarbeiter nicht gelistet. Gegenmassnahme: vollstaendige AVV-Kette.
- Aufbewahrungsfristen pauschal. Gegenmassnahme: Loeschkonzept beifuegen.

### 3. Verhaeltnismaessigkeit

- Verhaeltnismaessigkeitspruefung wird auf Rechtsgrundlage reduziert. Gegenmassnahme: Datenminimierung, Zweckbindung und Speicherbegrenzung separat pruefen.
- Mildere Mittel nicht erwogen. Gegenmassnahme: Alternativ-Optionen explizit dokumentieren und verwerfen.
- Betroffenenrechte nicht beschrieben. Gegenmassnahme: Pro Recht eine Zeile, wie es operativ umgesetzt wird.

### 4. Risikoanalyse

- Risiko nur fuer Vertraulichkeit untersucht. Gegenmassnahme: alle Schutzziele SDM durchgehen.
- Wahrscheinlichkeit ohne Bedrohungsmodell. Gegenmassnahme: Bedrohungsannahmen explizit machen.
- Schadenschwere aus Sicht des Verantwortlichen statt Betroffener. Gegenmassnahme: Erwaegungsgrund 75 DSGVO als Massstab.
- Risikomatrix bleibt fuer Massnahmen-Spalte leer. Gegenmassnahme: Pro Risiko mindestens eine Massnahme zuordnen.

### 5. Massnahmen

- TOM-Konzept fehlt oder ist generisch. Gegenmassnahme: konkrete Massnahmen mit Verantwortlichen und Fristen.
- Vertragliche Massnahmen (AVV, SCC) nicht referenziert. Gegenmassnahme: Verweis auf konkrete Vertragsversion und Datum.
- KI-Spezifika fehlen. Gegenmassnahme: Skill dsfa-fuer-ki-systeme-schnittstelle-art-26-kivo.
- Stand der Technik nicht begruendet. Gegenmassnahme: BSI- oder ENISA-Referenz beifuegen.

### 6. Restrisiko

- Restrisiko wird kuenstlich kleingerechnet, um Art. 36 zu vermeiden. Gegenmassnahme: Ehrliche Bewertung; bei spaeterem Vorfall verdoppelter Vorwurf.
- Restrisiko ohne Begruendung pauschal als gering bewertet. Gegenmassnahme: pro Szenario Begruendung.
- Vorab-Konsultation Art. 36 als Option statt Pflicht behandelt. Gegenmassnahme: Skill dsfa-restrisiko-und-art-36-konsultation.

### 7. Konsultation und Freigabe

- DSB-Anhoerung nur muendlich oder gar nicht. Gegenmassnahme: schriftliche Stellungnahme, datiert und unterzeichnet.
- Stakeholder-Konsultation Art. 35 Abs. 9 nicht erwogen. Gegenmassnahme: Skill dsfa-stakeholder-konsultation-art-35-9.
- Freigabe ohne Datum oder durch Unbefugten. Gegenmassnahme: definierter Eskalations- und Freigabeprozess.
- Verarbeitung wird vor Antwort der Aufsicht aufgenommen. Gegenmassnahme: Projektplan an Frist 8 Wochen ankoppeln.

### 8. Dokumentation und Update

- DSFA wird einmal erstellt und nie aktualisiert. Gegenmassnahme: Skill dsfa-update-bei-aenderungen-und-revision.
- Versionen werden ueberschrieben. Gegenmassnahme: Versionshistorie als Pflichtfeld.
- Aktenzeichen oder Aufbewahrungsfrist fehlt. Gegenmassnahme: Skill dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii.
- Verweis im Verarbeitungsverzeichnis Art. 30 fehlt. Gegenmassnahme: Doppelnachweis VV plus DSFA.

## Pruefliste vor Freigabe

```
DSFA-FREIGABE-PRUEFLISTE [DATUM]

Verarbeitung: [BEZEICHNUNG]
Pruefer: [NAME, ROLLE]

A. Triage
[ ] Triage-Vermerk schriftlich vorhanden
[ ] Blacklist-Abgleich dokumentiert
[ ] WP-248-Kriterien gepruet

B. Beschreibung
[ ] Datenfluss konkret beschrieben
[ ] Drittlandbezug geprueft
[ ] Sub-AV-Kette vollstaendig
[ ] Aufbewahrungsfristen konkret

C. Verhaeltnismaessigkeit
[ ] Datenminimierung
[ ] Zweckbindung
[ ] Speicherbegrenzung
[ ] Mildere Mittel erwogen
[ ] Betroffenenrechte operativ

D. Risikoanalyse
[ ] Alle Schutzziele gepruet
[ ] Wahrscheinlichkeit begruendet
[ ] Schadenschwere aus Sicht Betroffener
[ ] Risikomatrix vor und nach Massnahmen

E. Massnahmen
[ ] TOM konkret mit Eigentuemer und Frist
[ ] Vertragliche Massnahmen referenziert
[ ] KI-Spezifika beruecksichtigt

F. Restrisiko
[ ] Bewertung begruendet
[ ] Art. 36 gepruet

G. Konsultation
[ ] DSB schriftlich angehoert
[ ] Stakeholder-Konsultation Art. 35 Abs. 9 erwogen
[ ] Freigabe durch befugte Person

H. Dokumentation
[ ] Aktenzeichen vergeben
[ ] Versionshistorie gefuehrt
[ ] Verweis im VV Art. 30

Freigabeempfehlung: ja / nachzubessern / nein
Unterschrift Pruefer: ____________________
```

## Querverweise

- `datenschutzrecht/skills/dsfa-art-35-dsgvo-trigger-und-anwendungsbereich/SKILL.md`
- `datenschutzrecht/skills/dsfa-edpb-leitlinien-9-19-anwendung/SKILL.md`
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md`
- `datenschutzrecht/skills/dsfa-restrisiko-und-art-36-konsultation/SKILL.md`
- `datenschutzrecht/skills/dsfa-update-bei-aenderungen-und-revision/SKILL.md`
- `datenschutzrecht/skills/dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii/SKILL.md`
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35, 36, 5 Abs. 2, 83 Abs. 4 lit. a DSGVO
- EDSA-Leitlinien WP 248 rev.01
- BfDI- und Landesbehoerden-Pruefberichte (live abzurufen)
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle

## 10. `dsfa-update-bei-aenderungen-und-revision`

**Frühere Beschreibung:** Aktualisierung einer DSFA bei wesentlichen Aenderungen der Verarbeitung nach Art. 35 Abs. 11 DSGVO. Output: Revisionsplan mit Trigger-Liste Aenderungsanalyse Risikoreassessment und Versionshistorie.

# DSFA Update bei Aenderungen und Revision

## Zweck

Steuerung der Aktualisierung einer bestehenden DSFA bei wesentlichen Aenderungen der Verarbeitungstaetigkeit nach Art. 35 Abs. 11 DSGVO. Ergebnis ist ein Revisionsplan mit Trigger-Liste, Aenderungsanalyse, Risikoreassessment und Versionshistorie. Ziel ist, die DSFA als lebendes Dokument zu fuehren und nicht als Einmalvorgang.

## Wann brauchen Sie diesen Skill

- Bei Aenderung der Zwecke einer Verarbeitung
- Bei neuem Auftragsverarbeiter oder Sub-Auftragsverarbeiter
- Bei neuem Drittlandtransfer
- Bei neuer Technologie (KI-Modul, Biometrie)
- Bei neuer Datenkategorie oder neuem Betroffenenkreis
- Bei aktualisierter Rechtsprechung oder Aufsichtsbehoerdenpraxis
- Bei wesentlich erweiterter Datenmenge oder Aufbewahrungsfrist
- Bei Vorfall (Art. 33 Datenpanne) — Risikobewertung neu ueberpruefen

## Rechtlicher Rahmen

- Art. 35 Abs. 11 DSGVO: Der Verantwortliche fuehrt erforderlichenfalls eine Ueberpruefung durch, um zu bewerten, ob die Verarbeitung gemaess der DSFA durchgefuehrt wird; dies gilt zumindest, wenn sich das mit den Verarbeitungsvorgaengen verbundene Risiko aendert.
- Art. 5 Abs. 2 DSGVO Rechenschaftspflicht — Versionshistorie und Begruendung der Re-Pruefung.
- Art. 30 DSGVO Verarbeitungsverzeichnis — Aenderungen sind dort zu spiegeln.
- EDSA-Leitlinien WP 248 rev.01.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Aktuellen Stand der Verarbeitung erfassen und mit der dokumentierten DSFA-Version vergleichen.
2. **Verhaeltnismaessigkeitspruefung.** Aenderung wesentlich? Schwellenwerte:
   - Neue oder weggefallene Zweck
   - Neue Datenkategorie
   - Neue Empfaenger oder neuer Drittlandtransfer
   - Neue Technologie
   - Neue Aufbewahrungsfrist (> 50 Prozent Verlaengerung)
   - Aufsichtsbehoerden- oder Rechtsprechungsaenderung
3. **Risikoanalyse.** Erneute Risikoanalyse nach Methodik des urspruenglichen DSFA-Skills; Risikomatrix vor und nach erneuten Massnahmen.
4. **Massnahmen.** Pruefung, ob bestehende Massnahmen ausreichen oder ergaenzt werden muessen.
5. **Restrisiko.** Vergleich Restrisiko alt versus neu; ggf. neue Art. 36 Konsultation.
6. **Konsultation / Genehmigung.** DSB-Anhoerung, Freigabe und Versionierung; alte Versionen archivieren, nicht loeschen.

## Mustertext / Template Revisionsplan

```
DSFA-REVISIONSPLAN [DATUM]

Verarbeitung: [BEZEICHNUNG]
DSFA-Version aktuell: [X.Y]
DSFA-Version neu: [X.Y+1]
Verantwortlicher: [NAME]

1. Aenderungsanlass
[ ] Zweckaenderung
[ ] Neue Datenkategorie
[ ] Neuer Empfaenger / Sub-AV
[ ] Neuer Drittlandtransfer
[ ] Neue Technologie (z. B. KI-Modul)
[ ] Aufbewahrungsfrist
[ ] Rechtsprechungs- / Aufsichtspraxis-Update
[ ] Vorfall (Art. 33 DSGVO)
[ ] Routine-Revision (Datum: [DATUM])

2. Aenderungsanalyse
[Konkrete Beschreibung der Aenderung im Vergleich zur Vorversion]

3. Auswirkungen auf Schwellwertanalyse
[ ] Schwellwert unveraendert
[ ] Schwellwert neu erreicht (z. B. neues EDSA-Kriterium)
[ ] Schwellwert entfallen (z. B. Anonymisierung)

4. Risikoreassessment
- Risiken neu identifiziert: [Liste]
- Risikomatrix aktualisiert: ja / nein
- Restrisiko aendert sich: ja / nein
- Vorab-Konsultation Art. 36 ggf. neu erforderlich: ja / nein

5. Massnahmen
[Liste der zusaetzlichen oder geaenderten Massnahmen]

6. Freigabe
- DSB-Anhoerung: [Datum, Stellungnahme]
- Genehmigung Verantwortlicher: [Name, Datum]
- Aufsicht informiert (falls Art. 36): [Datum]
- Eintrag Verarbeitungsverzeichnis aktualisiert: [Datum]
- Naechste Routine-Revision: [DATUM]

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________

Versionshistorie
| Version | Datum | Aenderung | Autor | Freigabe |
| 1.0     | [...] | Erstfassung | [...] | [...] |
| 1.1     | [...] | [...] | [...] | [...] |
| 2.0     | [...] | [...] | [...] | [...] |
```

## Empfohlene Revisionsfrequenz

- Routine-Revision: einmal jaehrlich, dokumentiert auch wenn keine Aenderung
- Anlassbezogene Revision: unverzueglich nach Trigger
- KI-Verarbeitungen: alle 6 Monate (wegen Modell- und Datenaenderungen)
- Beschaeftigtenverarbeitungen bei BetrVG-Tatbestand: nach jeder Betriebsvereinbarung
- Drittlandtransfer: nach jedem Schrems-Folgeurteil oder EDSA-Update

## Typische Fehler

- DSFA wird einmal erstellt und nie aktualisiert — Verstoss gegen Art. 35 Abs. 11 DSGVO.
- Aenderungen werden im Original-Dokument ueberschrieben — Versionshistorie geht verloren.
- Routine-Revision wird unterlassen, weil sich nichts geaendert hat — ohne Dokumentation kein Nachweis.
- Trigger werden nicht in das Change-Management-Verfahren integriert.
- Nach Datenpanne (Art. 33) wird die DSFA nicht ueberprueft.
- KI-Modellupdate wird nicht als Trigger erkannt.

## Querverweise

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Basisvorlage
- `datenschutzrecht/skills/dsfa-restrisiko-und-art-36-konsultation/SKILL.md` — Vorabkonsultation bei Aenderung
- `datenschutzrecht/skills/dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii/SKILL.md` — Versionierung
- `datenschutzrecht/skills/datenpanne-meldung/SKILL.md` — Trigger Datenpanne
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35 Abs. 11 DSGVO
- Art. 5 Abs. 2, Art. 30, Art. 33 DSGVO
- EDSA-Leitlinien WP 248 rev.01
- EDSA-Stellungnahme 28/2024 zu KI-Modellen (Update-Trigger)
- BfDI / Landesbehoerden — Verfahrenshinweise
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
