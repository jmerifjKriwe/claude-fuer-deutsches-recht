---
name: workflow-kaltstart-und-routing
description: "Kaltstart-Workflow für das Plugin gewerblicher-rechtsschutz: strukturiertes Erstgespräch, Rollenklärung, Themen-Routing und Auswahl des passenden Spezialskills. Erster Kontaktpunkt für neue Anfragen und unklare Sachlagen."
---

# Workflow: Kaltstart und Routing

## Zweck

Dieser Skill ist der **primäre Einstiegspunkt** des Plugins `gewerblicher-rechtsschutz`. Er führt ein strukturiertes Erstgespräch durch, klärt die Situation in wenigen Rückfragen und leitet an den richtigen Spezialskill weiter. Er ist kein Wissensskill, sondern ein Prozessskill.

Mandatsbezug: Eine Person startet das Plugin ohne weitere Angaben. Oder: Anfrage ist unklar und muss erst eingeordnet werden, bevor ein passender Spezialskill ausgewählt werden kann.

## Kaltstart-Gespräch: Vier Pflichtfragen

Das Kaltstart-Gespräch stellt maximal vier Fragen. Wenn Material vorliegt, erste Auswertung sofort aus dem Material.

### Frage 1 – Wer fragt?

Rolle identifizieren:
- Mandant (Unternehmensinhaber, Rechtsabteilung, Privatperson)
- Anwalt (für eigenes Mandat)
- Kanzleimitarbeiter (Aktenführung, Fristencheck)
- Richter / Rechtspfleger
- Sonstiges (Journalist, Wissenschaftler, Student)

**Warum wichtig:** Tiefe und Tonalität der Antwort hängen von der Rolle ab.

### Frage 2 – Was ist das Problem oder die Aufgabe?

Kurzbeschreibung aus der Anfrage extrahieren oder fragen:
- Verletzung eigener IP-Rechte?
- Abmahnung empfangen?
- Schutzrecht anmelden?
- Freedom-to-Operate prüfen?
- Verfahren führen (EV, Klage, Widerspruch)?
- Allgemeine rechtliche Frage?

### Frage 3 – Gibt es eine Frist?

- Fristsetzung in empfangener Abmahnung?
- Vollziehungsfrist nach EV?
- DPMA/EUIPO-Widerspruchsfrist läuft?
- Hauptsacheklage nach § 926 ZPO gefordert?

**Wenn ja:** Frist sofort erfassen und Risikoampel setzen.

### Frage 4 – Welche Unterlagen liegen vor?

Kurze Unterlagenliste:
- Schutzrechtsurkunde, Registerauszug
- Abmahnung mit Anlagen
- EV-Beschluss oder Urteil
- Korrespondenz mit Gegenseite
- Sonstiges

## Routing-Matrix

Basierend auf den vier Fragen den richtigen Skill auswählen:

| Ausgangslage | Empfohlener Skill |
|---|---|
| Erste Orientierung gewünscht | `gw-einfuehrung-rechtsschutzwege` |
| Verletzung entdeckt, unklar was tun | `verletzungs-triage` |
| Abmahnung UWG erhalten | `gewr-uwg-abmahnung-checkliste` |
| Abmahnung Marke erhalten | `verletzungs-triage` + `unterlassungsverlangen` |
| Abmahnung Urheberrecht erhalten | `abmahnung-urheberrecht` |
| Abmahnung versenden wollen (UWG) | `gewr-uwg-abmahnung-checkliste` |
| EV beantragen | `gewr-einstweilige-verfuegung-eilverfahren-spezial` |
| EV vollziehen (erhalten) | `evvollzug-neu-001` |
| Schutzschrift einreichen | `evvollzug-neu-008` + `schutzschrift-eilverfuegung` |
| Marke anmelden | `gewr-markenanmeldung-bauleiter` |
| Marke recherchieren | `markenrecherche` |
| Patent FTO | `fto-triage` |
| Patentrecherche | `spezial-patentscreening-livequellen-und-rechtsprechungscheck` |
| Arbeitnehmererfindung | `erfindungsmeldung-aufnahme` |
| Geschäftsgeheimnis schützen | `gewr-geschaeftsgeheimnisgesetz-spezial` |
| Fristen kontrollieren | `workflow-fristen-und-risikoampel` |
| Dokumente einlesen | `workflow-dokumentenintake` |
| Vergleich / Verhandlung | `spezial-operate-verhandlung-vergleich-und-eskalation` |
| Internationaler Bezug | `spezial-reaktion-internationaler-bezug-und-schnittstellen` |
| Qualitätskontrolle | `workflow-redteam-qualitygate` |
| Rechtsquellen live prüfen | `workflow-rechtsquellen-livecheck` |

## Schnell-Routing bei bekannter Lage

Wenn die Anfrage eindeutig ist, direkt routing ohne Rückfragen:

**Erkanntes Muster → Direktrouting:**
- „Ich habe eine Abmahnung bekommen" → `verletzungs-triage`
- „Wir wollen eine Marke anmelden" → `gewr-markenanmeldung-bauleiter`
- „Einstweilige Verfügung vollziehen" → `evvollzug-neu-001`
- „Was macht der Gerichtsvollzieher?" → `evvollzug-neu-003`
- „Ich brauche eine Schutzschrift" → `evvollzug-neu-008`
- „Widerspruch beim DPMA" → `spezial-dpma-fristen-form-und-zustaendigkeit`

## Kaltstart-Output: Kurzlage

Nach dem Kaltstart-Gespräch sofort ausgeben:

```
KURZLAGE
Rolle: _______________
Problem: _______________
Frist: _______________  (Ampel: 🔴/🟡/🟢)
Unterlagen: _______________
Empfohlener Skill: _______________
Begründung: _______________
```

## Eskalation bei Unklarheit

Wenn nach vier Fragen immer noch unklar:
- Konkreten Sachverhalt in 2–3 Sätzen formulieren lassen.
- Dann Routing-Entscheidung treffen.
- Nie mehr als sechs Fragen im Kaltstart; danach Arbeitshypothese aufstellen.

## Quellenregel

- Dieser Skill führt nur den Routing-Prozess durch; keine Rechtsquellen nötig.
- Sobald ein Spezialskill aktiviert wird, gelten dessen Quellenregeln.

## Anschluss-Skills

Alle Spezialskills des Plugins `gewerblicher-rechtsschutz` – je nach Routing.
Erste Empfehlung bei breiter Orientierungsanfrage: `gw-einfuehrung-rechtsschutzwege`.
