---
name: workflow-anschluss-skills-router
description: "Anschluss-Skills-Router für das Plugin gewerblicher-rechtsschutz: Weichenstellung nach abgeschlossener Prüfung, Ergebnis oder Folgefrage. Zeigt, welcher Skill als nächstes eingesetzt werden soll und begründet die Weiterleitung."
---

# Workflow: Anschluss-Skills-Router

## Zweck

Dieser Skill ist der **Routing-Skill** des Plugins `gewerblicher-rechtsschutz`. Er wird eingesetzt, wenn eine Prüfung abgeschlossen ist, ein Ergebnis vorliegt oder eine Folgefrage entsteht, und der nächste passende Skill gefunden werden muss. Der Router verhindert, dass Nutzer im Plugin verloren gehen.

## Wann wird dieser Skill aktiviert?

- Nach Abschluss einer Erstprüfung (z.B. `spezial-gewerblicher-erstpruefung-und-mandatsziel`).
- Wenn das bisherige Ergebnis einen Folgeprozess auslöst (EV nach Abmahnung, Ordnungsmittel nach EV).
- Wenn der Nutzer fragt: „Was muss ich jetzt tun?" oder „Welcher Skill hilft weiter?"
- Wenn ein Workflow-Schritt abgeschlossen ist und der nächste unklar ist.

## Router-Logik: Entscheidungsbaum

### Eingangsfrage: Was ist der aktuelle Stand?

```
Aktueller Stand → Nächster Skill

A) Neue Anfrage ohne Vorkenntnisse
   → workflow-kaltstart-und-routing

B) Schutzrechtsfrage (Anmeldung, Portfolio, FTO)
   → gewr-markenanmeldung-bauleiter (Marke)
   → fto-triage (Patent FTO)
   → schutzrechts-portfolio (Portfolio-Übersicht)
   → erfindungsmeldung-aufnahme (Patent ArbnErfG)

C) Verletzung entdeckt, noch keine Abmahnung
   → verletzungs-triage (Erstentscheidung)
   → gewr-uwg-abmahnung-checkliste (UWG)
   → abmahnung-urheberrecht (UrhG)

D) Abmahnung vorbereiten
   → gewr-uwg-abmahnung-checkliste (UWG)
   → spezial-freedom-schriftsatz-brief-und-memo-bausteine (Textbausteine)

E) Abmahnung empfangen, Reaktion nötig
   → verletzungs-triage (Erstentscheidung)
   → unterlassungsverlangen (UE-Reaktion)
   → evvollzug-neu-008 (Schutzschrift)

F) EV beantragen
   → gewr-einstweilige-verfuegung-eilverfahren-spezial (Antrag)
   → gw-einstweilige-verfuegung-spezial (Strategie)

G) EV erlassen, Vollzug nötig
   → evvollzug-neu-001 (Vollziehungsfrist)
   → evvollzug-neu-002 (Beschluss vs. Urteil)
   → evvollzug-neu-003 (GV-Zustellung)

H) EV vollzogen, Folgeschritte
   → evvollzug-neu-005 (Ordnungsmittelantrag)
   → evvollzug-neu-007 (Abschlussschreiben)

I) Auslandszustellung nötig
   → evvollzug-neu-006 (Auslandszustellung)

J) Verhandlung, Vergleich
   → spezial-operate-verhandlung-vergleich-und-eskalation

K) Fristen kritisch
   → workflow-fristen-und-risikoampel
   → spezial-schutzrechts-fristennotiz-und-naechster-schritt

L) Dokumente einlesen/sortieren
   → workflow-dokumentenintake

M) Qualitätssicherung vor Versand
   → spezial-source-red-team-und-qualitaetskontrolle
   → workflow-redteam-qualitygate

N) Internationaler Bezug
   → spezial-reaktion-internationaler-bezug-und-schnittstellen

O) Rechtsquellen live prüfen
   → workflow-rechtsquellen-livecheck

P) Output-Format unklar
   → workflow-output-waehlen

Q) Mehrparteien / Interessenkonflikt
   → spezial-versand-mehrparteien-konflikt-und-interessen
```

## Routing-Entscheidungshilfe (Kurzform)

| Stichwort | Empfohlener Skill |
|---|---|
| Erstgespräch, neue Anfrage | `workflow-kaltstart-und-routing` |
| Verletzung, Abmahnung senden | `verletzungs-triage` |
| Abmahnung erhalten | `verletzungs-triage` + `unterlassungsverlangen` |
| EV beantragen | `gewr-einstweilige-verfuegung-eilverfahren-spezial` |
| EV vollziehen | `evvollzug-neu-001` |
| GV-Zustellung | `evvollzug-neu-003` |
| beA-Zustellung | `evvollzug-neu-004` |
| Auslandszustellung | `evvollzug-neu-006` |
| Ordnungsmittelantrag | `evvollzug-neu-005` |
| Abschlussschreiben | `evvollzug-neu-007` |
| Schutzschrift | `evvollzug-neu-008` |
| Markenanmeldung | `gewr-markenanmeldung-bauleiter` |
| Markenrecherche | `markenrecherche` |
| DPMA-Verfahren | `spezial-dpma-fristen-form-und-zustaendigkeit` |
| EUIPO-Verfahren | `spezial-euipo-dokumentenmatrix-und-lueckenliste` |
| Patent FTO | `fto-triage` |
| Patentrecherche | `spezial-patentscreening-livequellen-und-rechtsprechungscheck` |
| ArbnErfG | `erfindungsmeldung-aufnahme` |
| Geschäftsgeheimnis | `gewr-geschaeftsgeheimnisgesetz-spezial` |
| Urheberrecht Abmahnung | `abmahnung-urheberrecht` |
| UWG Abmahnung | `gewr-uwg-abmahnung-checkliste` |
| Beweislast | `spezial-klausel-beweislast-und-darlegungslast` |
| Fristen | `workflow-fristen-und-risikoampel` |
| Dokumente | `workflow-dokumentenintake` |
| Qualitätssicherung | `workflow-redteam-qualitygate` |
| Vergleich | `spezial-operate-verhandlung-vergleich-und-eskalation` |
| International | `spezial-reaktion-internationaler-bezug-und-schnittstellen` |
| Mehrparteien | `spezial-versand-mehrparteien-konflikt-und-interessen` |

## Ausgabeformat des Routers

Der Router gibt immer aus:
1. **Aktueller Stand:** Was liegt vor, was ist geklärt?
2. **Nächster Skill:** Welcher Skill wird als nächstes empfohlen?
3. **Begründung:** Warum dieser Skill?
4. **Alternativskills:** Falls mehr als eine Option sinnvoll.
5. **Zeitkritische Warnung:** Falls eine Frist nah ist.

## Quellenregel

- Dieser Skill verweist nur auf andere Skills; keine externen Quellen erforderlich.
- Bei rechtlichen Fragen im Routing-Gespräch: Normtext über gesetze-im-internet.de prüfen.

## Anschluss-Skills

Alle Skills des Plugins `gewerblicher-rechtsschutz` – je nach Routing-Entscheidung.
