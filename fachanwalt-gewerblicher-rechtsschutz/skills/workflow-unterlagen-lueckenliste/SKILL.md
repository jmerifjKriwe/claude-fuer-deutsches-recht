---
name: workflow-unterlagen-lueckenliste
description: "Unterlagen-Lückenliste im gewerblichen Rechtsschutz: systematische Identifikation fehlender Dokumente für alle Verfahrenstypen (Marke, Patent, Design, UWG, EV), gezielte Nachforderungsschreiben und Priorisierung nach Dringlichkeit."
---

# Unterlagen-Lückenliste

## Aufgabe
Dieser Workflow-Skill identifiziert fehlende Unterlagen für den aktuellen Verfahrensstand und erstellt gezielte, priorisierte Nachforderungslisten mit Erklärung für Mandant oder Gegenseite.

## Systematik: Fehlende Unterlagen erkennen

**Grundregel:** Nur die Unterlagen nachfordern, die für die nächste Entscheidungsweiche tatsächlich gebraucht werden. Keine Fragebogen-Bürokratie.

**Priorisierung:**
- **P1 (Blockiert):** Ohne dieses Dokument kann die nächste Handlung nicht erfolgen.
- **P2 (Wichtig):** Fehlen schadet der Qualität erheblich; aber Teilvorgehen möglich.
- **P3 (Nützlich):** Vervollständigt das Bild; kann nachgereicht werden.

## Lückenliste nach Verfahrenstyp

### Markenrechtsverletzung / Abmahnung

| Dokument | Priorität | Zweck | Status |
|---|---|---|---|
| Registerauszug DPMA / EUIPO (aktuell) | P1 | Schutzrechtsnachweis | ☐ |
| Benutzungsnachweise (5 Jahre, § 26 MarkenG) | P1 | Gegen Nichtbenutzungseinrede | ☐ |
| Screenshots / Fotos Verletzungshandlung | P1 | Verletzungsnachweis | ☐ |
| Vollmacht | P1 | Kanzlei-Mandat | ☐ |
| Testkauf-Belege (Quittung, Ware) | P2 | Verletzungsbeleg | ☐ |
| Handelregisterauszug Gegenseite | P2 | Zustellung | ☐ |
| Eingehende Abmahnung (falls vorhanden) | P2 | Reaktion vorbereiten | ☐ |

### Patentverletzung

| Dokument | Priorität | Zweck | Status |
|---|---|---|---|
| Patentschrift mit Ansprüchen (alle Ansprüche) | P1 | Schutzbereichsbestimmung | ☐ |
| Registerauszug DPMA / EPA | P1 | Aktivlegitimation | ☐ |
| Verletzende Ware / Datenblatt | P1 | Verletzungsnachweis | ☐ |
| Verletzungsanalyse (Merkmalsgliederung) | P1 | Subsumtion | ☐ |
| ArbnErfG-Unterlagen (falls AN-Erfindung) | P2 | Inhaberschaft klären | ☐ |

### Designverletzung

| Dokument | Priorität | Zweck | Status |
|---|---|---|---|
| Designregistrierung mit Abbildungen | P1 | Schutzrecht | ☐ |
| Angegriffene Ausführungsform (Fotos/Produktbilder) | P1 | Verletzungsnachweis | ☐ |
| Formenschatz-Recherche (Vordesigns) | P2 | Schutzbereich bestimmen | ☐ |
| Entwicklungsunterlagen des eigenen Designs | P2 | Entstehungsnachweis | ☐ |

### UWG-Abmahnung

| Dokument | Priorität | Zweck | Status |
|---|---|---|---|
| Vollständige eingehende Abmahnung | P1 | Reaktion | ☐ |
| Beanstandetes Werbemittel / Screenshot | P1 | Tatbestand prüfen | ☐ |
| Nachweis Mitbewerbereigenschaft | P1 | Aktivlegitimation § 8 UWG | ☐ |
| Umsatzbelege im betroffenen Bereich | P2 | Konkrete Beeinträchtigung | ☐ |

### Einstweilige Verfügung

| Dokument | Priorität | Zweck | Status |
|---|---|---|---|
| Alle o.g. Grundlagen je Schutzrecht | P1 | EV-Antrag | ☐ |
| Nachweis Kenntnisdatum (E-Mail, Screenshot mit Datum) | P1 | Dringlichkeit | ☐ |
| Eidesstattliche Versicherung (unterschrieben) | P1 | Glaubhaftmachung § 294 ZPO | ☐ |
| Vollmacht für Gerichtsverfahren | P1 | Prozessvollmacht | ☐ |

## Nachforderungsschreiben (Muster)

```
An [Mandant]                                  [Ort, Datum]

Unterlagencheck – Mandat [Aktenzeichen]

Sehr geehrte/r [Mandant],

für die Vorbereitung des [EV-Antrags / der Abmahnung / des Schriftsatzes]
benötigen wir noch folgende Unterlagen. Bitte übermitteln Sie uns diese
bis zum [Datum], um den nächsten Schritt fristgerecht durchführen zu können:

DRINGEND (P1 – blockiert weiteres Vorgehen):
1. [Dokument]: [kurze Erklärung, warum nötig]
2. [Dokument]: [kurze Erklärung]

WICHTIG (P2 – erhebliche Qualitätsverbesserung):
3. [Dokument]: [kurze Erklärung]

Bitte melden Sie sich, falls Sie Fragen zur Beschaffung haben.

[Kanzlei]
```

## Kaltstart
1. Welches Verfahren läuft und in welcher Phase befindet es sich?
2. Welche Unterlagen liegen bereits vor?
3. Welche Handlung ist als nächstes geplant (Abmahnung / EV / Klage)?
4. Gibt es Fristen, die die Nachforderung beschleunigen?
5. Output: Priorisierte Lückenliste, Nachforderungsschreiben, Fristenhinweis?

## Anschluss-Skills
- `workflow-dokumentenintake` – Erfassung eingehender Dokumente.
- `workflow-chronologie-und-belegmatrix` – Belege chronologisch ordnen.
- `faevvollzug-neu-008-qualitaetsgate-vor-vollziehung` – Qualitätsgate.

## Quellenregel
- Dieser Skill enthält keine Rechtsquellen-Zitate (nur Prozesssteuerung).
- Normen für Beweisanforderungen: ZPO, MarkenG, PatG usw. über [gesetze-im-internet.de](https://www.gesetze-im-internet.de).
- Annahmen und Lücken ausdrücklich markieren.

## Was dieser Skill nicht macht
- Keine inhaltliche Rechtsprüfung.
- Kein Ersatz für vollständige Mandantenberatung.
- Keine automatische Prüfung auf Dokumentenvollständigkeit ohne Eingaben.
