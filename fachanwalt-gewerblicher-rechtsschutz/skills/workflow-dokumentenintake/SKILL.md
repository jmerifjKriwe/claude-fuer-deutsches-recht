---
name: workflow-dokumentenintake
description: "Dokumentenintake im gewerblichen Rechtsschutz: Ersterfassung eingehender Unterlagen, Dokument-Screening, Kategorisierung, Vollständigkeitsprüfung und Weiterleitung an passende Spezialskills. Checkliste für alle Schutzrechts- und Verfahrenstypen."
---

# Dokumentenintake

## Aufgabe
Dieser Workflow-Skill steuert die Ersterfassung und Kategorisierung eingehender Mandantenunterlagen im gewerblichen Rechtsschutz: Screening, Lückenanalyse und Weiterleitung an den passenden Bearbeitungsweg.

## Warum strukturierter Dokumentenintake?

- Verhindert, dass wichtige Unterlagen übersehen werden.
- Identifiziert sofort Lücken, die die Bearbeitung blockieren.
- Ermöglicht gezielte Rückfragen statt pauschaler Fragelisten.
- Sichert Fristen durch frühe Erkennung zeitkritischer Dokumente.

## Intake-Checkliste nach Verfahrenstyp

### A) Markenrechtsverletzung / Markenabmahnung

| Dokument | Priorität | Vorhanden? |
|---|---|---|
| Registerauszug (DPMA / EUIPO) mit aktuellem Datum | MUSS | ☐ |
| Benutzungsnachweise (§ 26 MarkenG, 5 Jahre) | MUSS | ☐ |
| Screenshot / Foto der Verletzungshandlung | MUSS | ☐ |
| Eingehende Abmahnung (falls vorhanden) | MUSS | ☐ |
| Vollmacht für Kanzlei | MUSS | ☐ |
| Handelsregisterauszug Mandant | SOLL | ☐ |
| Lizenzvertrag (falls Lizenznehmer klagt) | KANN | ☐ |

### B) Patentverletzung

| Dokument | Priorität | Vorhanden? |
|---|---|---|
| Patentschrift mit Ansprüchen | MUSS | ☐ |
| Registerauszug (DPMA / EPA) | MUSS | ☐ |
| Verletzende Ware / Produkt (Testkauf, Datenblatt) | MUSS | ☐ |
| Verletzungsanalyse (Eigenanalyse oder SV-Gutachten) | MUSS | ☐ |
| Lizenznehmer-Vereinbarungen (falls relevant) | SOLL | ☐ |
| ArbnErfG-Dokumentation (falls Arbeitnehmererfindung) | KANN | ☐ |

### C) Designverletzung

| Dokument | Priorität | Vorhanden? |
|---|---|---|
| Designregistrierung (DPMA / EUIPO) | MUSS | ☐ |
| Abbildungen des Klagedesigns | MUSS | ☐ |
| Abbildungen der angegriffenen Ausführungsform | MUSS | ☐ |
| Entstehungsdokumentation (Entwürfe, Datum) | SOLL | ☐ |
| Formenschatz-Recherche (Vordesigns) | SOLL | ☐ |

### D) UWG-Abmahnung

| Dokument | Priorität | Vorhanden? |
|---|---|---|
| Eingehende Abmahnung (vollständig) | MUSS | ☐ |
| Beanstandetes Werbematerial / Screenshot | MUSS | ☐ |
| Belege zur eigenen Branchenzugehörigkeit (Mitbewerber) | MUSS | ☐ |
| UE-Entwurf (falls vorhanden) | SOLL | ☐ |
| Vollmacht | MUSS | ☐ |

### E) Einstweilige Verfügung (beantragen)

| Dokument | Priorität | Vorhanden? |
|---|---|---|
| Alle obigen Grundlagen je Schutzrecht | MUSS | ☐ |
| Nachweis Kenntnisdatum (E-Mail, Datum Screenshot) | MUSS | ☐ |
| Eidesstattliche Versicherung unterschrieben | MUSS | ☐ |
| Vollstreckbarer Titel falls schon vorhanden | SOLL | ☐ |

## Dokumenten-Screening

Bei Eingang von Unterlagen:

1. **Dokumententyp identifizieren:** Bescheid, Registerauszug, Urteil, Vertrag, Abmahnung, Schriftsatz, E-Mail, Screenshot?
2. **Zeitkritisch?** Ablauffristen, Antwortfristen, Dringlichkeit?
3. **Vollständig?** Seiten vollständig; Anhänge vollständig; Datum und Unterschriften vorhanden?
4. **Verfahren zuordnen:** Welches Verfahren / welche Partei / welches Schutzrecht?
5. **Lücken notieren:** Was fehlt und wann ist Nachlieferung nötig?

## Intake-Protokoll (Muster)

```
Intake-Protokoll – Mandat: [Aktenzeichen] – Datum: [Datum]

Eingang: [Eingangskanal: Post / E-Mail / beA / Übergabe]

Eingegangene Dokumente:
1. [Dokument 1] – [Datum des Dokuments] – vollständig: Ja / Nein
2. [Dokument 2] – [Datum] – vollständig: Ja / Nein
...

Zeitkritische Fristen:
- [Frist 1]: [Datum] – [Handlung]
- [Frist 2]: [Datum] – [Handlung]

Fehlende Dokumente (Nachlieferung angefordert):
- [Dokument X] – angefordert per [E-Mail / Telefon] am [Datum]

Weitergeleitet an Skill / Bearbeiter:
[Skill-Name oder Bearbeiter-Kürzel]
```

## Kaltstart
1. Welche Unterlagen liegen dem Intake-Prozess vor?
2. Welches Verfahren / Schutzrecht ist betroffen?
3. Gibt es zeitkritische Fristen (sofort erkennbar aus Dokumenten)?
4. Was fehlt für den nächsten Bearbeitungsschritt?
5. Output: Intake-Protokoll, Lückenliste, Fristenüberblick, Weiterleitungsvorschlag?

## Anschluss-Skills
- `workflow-chronologie-und-belegmatrix` – Zeitachse und Belege.
- `workflow-fristen-und-risikoampel` – Fristencheck.
- `spezial-fachanwalt-erstpruefung-und-mandatsziel` – Erstprüfung.

## Quellenregel
- Normen: [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Register: [dpma.de](https://www.dpma.de), [euipo.europa.eu](https://euipo.europa.eu).
- Keine inhaltlichen Urteile in diesem Skill; nur Prozessteuerung.
- Annahmen und Lücken ausdrücklich markieren.

## Was dieser Skill nicht macht
- Keine inhaltliche Rechtsprüfung (das machen die Spezialskills).
- Kein Ersatz für vollständige Mandantenberatung.
- Keine Fristberechnung ohne vollständige Sachverhaltskenntnis.
