---
name: allgemein
description: "Einstieg, Schnelltriage und Workflow-Routing im Kanzlei Builder Hub-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan."
---

# Kanzlei-Builder-Hub — Allgemein

## Schnellstart-Workflow

Dieser Allgemein-Skill ist der schöne, schnelle Eingang in das Plugin **Kanzlei Builder Hub**. Er funktioniert wie Empfang, Triage, Projektsteuerung und Qualitätskontrolle in einem: erst knapp klären, dann den richtigen Arbeitsweg wählen, dann passende Spezial-Skills aus diesem Plugin vorschlagen.

**Plugin-Fokus:** Findet, prüft und installiert Community-Skills mit Security-Review-Gate vor dem Deployment in die Kanzleiumgebung.

### 1. Intake in 60 Sekunden

Frage zu Beginn nur das ab, was für die Weichenstellung wirklich nötig ist. Wenn der Nutzer schon genug geliefert hat, nicht erneut abfragen, sondern sichtbar zusammenfassen.

| Punkt | Frage | Warum wichtig? |
|---|---|---|
| Rolle | Wer fragt: Anwalt, Kanzlei, Rechtsabteilung, Verwalter, Betroffener, Unternehmen, Behörde? | Perspektive und Ton bestimmen. |
| Ziel | Was soll am Ende entstehen: Prüfung, Schriftsatz, Memo, Checkliste, Vertrag, E-Mail, Strategie, Datenraum-Auswertung? | Output sofort sauber ausrichten. |
| Sachverhalt | Was ist passiert, wer sind die Beteiligten, welche Daten und Beträge sind sicher? | Keine Arbeit auf Luft bauen. |
| Fristen | Gibt es Termine, Fristablauf, Zustellung, Einspruch, Klagefrist, Behördenfrist oder Closing-Datum? | Eilsachen zuerst sichern. |
| Unterlagen | Welche Dateien, Registerauszüge, Bescheide, Verträge, Tabellen, E-Mails oder PDFs liegen vor? | Aktenarbeit statt Raten. |
| Risiko | Wo drohen Haftung, Verjährung, Bußgeld, Strafbarkeit, Kosten, Reputationsschaden oder Eskalation? | Priorität und Vorsicht einstellen. |
| Format | Wie ausführlich, für wen, in welchem Stil und mit welcher Zitier-/Ausgabeform? | Ergebnis direkt verwendbar machen. |

### 2. Sofort-Triage

Arbeite danach in dieser Reihenfolge:

1. **Eilprüfung:** Fristen, Zuständigkeiten, Formerfordernisse und irreversible Schritte sofort markieren.
2. **Sachverhaltskern:** In drei bis sieben Sätzen festhalten, was sicher ist, was streitig ist und was fehlt.
3. **Arbeitsmodus wählen:** Kurzprüfung, Deep Dive, Dokumententwurf, Verhandlungsstrategie, Aktenextraktion, Red Team oder Mandantenkommunikation.
4. **Spezial-Skills vorschlagen:** Zwei bis fünf passende Skills aus diesem Plugin nennen, jeweils mit einem kurzen Grund.
5. **Nächsten Schritt anbieten:** Wenn ein Skill eindeutig passt, mit diesem Skill weiterarbeiten; wenn mehrere passen, eine knappe Auswahl anbieten.
6. **Qualitätsgate:** Am Ende prüfen: Quellen, Fristen, Annahmen, offene Tatsachen, nächste Handlung.

### 3. Routing-Regeln

- Schlage **immer zuerst Skills aus diesem Plugin** vor. Andere Plugins nur als Schnittstelle nennen, wenn das Thema sichtbar auswandert.
- Nenne nie nur einen Skillnamen. Immer auch sagen: **wofür**, **wann**, **welcher Input fehlt** und **was als Output kommt**.
- Wenn die Akte groß oder unordentlich ist, zuerst einen Akten-, Tabellen- oder Triage-Skill vorschlagen, bevor materiell geprüft wird.
- Wenn ein Schriftsatz, Vertrag oder Register-/Behördenoutput gewünscht ist, zuerst die Prüfung strukturieren und danach den passenden Output-Skill nehmen.
- Wenn Rechtslage, Rechtsprechung oder Behördenpraxis aktuell sein kann, ausdrücklich Quellen-/Aktualitätsprüfung einplanen.
- Wenn der Nutzer nur schnell arbeiten will, mit einem **Minimalpfad** starten: Frist sichern, Sachverhalt ordnen, nächster Spezial-Skill.

### 4. Antwortformat für den Einstieg

Nutze als erste Antwort nach Aktivierung möglichst dieses kompakte Format:

**Kurzbild**
- Ziel: [...]
- Rolle/Perspektive: [...]
- Eilt wegen: [...]
- Fehlende Unterlagen: [...]

**Vorgeschlagener Workflow**
1. [...]
2. [...]
3. [...]

**Passende Skills aus diesem Plugin**
| Skill | Warum jetzt? | Erwarteter Output |
|---|---|---|
| `...` | [...] | [...] |

**Nächste Frage**
[Eine kurze, entscheidende Frage stellen, wenn wirklich etwas fehlt.]

### 5. Spezial-Skills in diesem Plugin

| Skill | Wann vorschlagen? |
|---|---|
| `automatischer-aktualisierer` | Plugins und Skills in der KI-Anwaltskanzlei automatisch aktualisieren: neue Norm-Versionen, Rechtsprechungsaenderungen. Normen: technisch/intern. Prüfraster: aeltere Versionen identifizieren, Update-Prioritaet,… |
| `deaktivieren` | Einzelne Skills oder Plugins temporaer deaktivieren ohne Deinstallation. Normen: technisch/intern. Prüfraster: Abhaengigkeiten, Deaktivierungsumfang, Reaktivierungsweg. Output: Deaktivierungsbestätigung. Abgrenzung:… |
| `deinstallieren` | Plugins oder Skills vollständig deinstallieren: Abhaengigkeitsprüfung, Datensicherung. Normen: technisch/intern. Prüfraster: Abhaengigkeitscheck, Datensicherung vor Löschung, Bestätigung. Output:… |
| `fundstellenglattzieher` | Normen- und Rechtsprechungszitate in Schriftsaetzen und Skills vereinheitlichen: einheitliche Zitierweise. Normen: allgemein BRAO. Prüfraster: Normzitat-Format, BGH-Aktenzeichen, Quellenangaben. Output: Text mit… |
| `kanzlei-builder-hub-anpassen` | Kanzlei-Builder-Hub an kanzleispezifische Anforderungen anpassen: eigene Plugins, Branding, Workflows. Normen: technisch/intern. Prüfraster: Anpassungsumfang, Kompatibilitaet, Testbedarf. Output:… |
| `kanzlei-builder-hub-kaltstart-interview` | Kaltstart-Interview für den Kanzlei-Builder-Hub: Kanzleiprofil, Rechtsgebiete, gewuenschte Plugins. Normen: technisch/intern. Prüfraster: Rechtsgebietsabdeckung, Mandantenstruktur, Technikvoraussetzungen. Output:… |
| `playbook-aus-eigenen-daten` | Kanzleieigenes Playbook aus vorhandenen Musterdokumenten und Vorlagen automatisch erstellen. Normen: technisch/intern, BRAO. Prüfraster: Dokumentenqualitaet, Kategorisierung, Normverankerung. Output: Kanzlei-Playbook… |
| `skill-installierer` | Neue Skills in der KI-Anwaltskanzlei installieren: Verfuegbarkeitscheck, Abhaengigkeiten, Konfiguration. Normen: technisch/intern. Prüfraster: Kompatibilitaet, Abhaengigkeitsprüfung, Testlauf. Output:… |
| `skill-verwalter` | Übersicht und Verwaltung aller installierten Skills: Status, Version, Abhaengigkeiten. Normen: technisch/intern. Prüfraster: aktive Skills, deaktivierte Skills, Update-Bedarf. Output: Skills-Verwaltungsuebersicht.… |
| `skills-qualitaetspruefung` | Qualitaet installierter Skills prüfen: Normaktualitaet, Description-Qualitaet, Struktur-Compliance. Normen: technisch/intern, SKILL.md-Schema. Prüfraster: Description-Laenge, Normverankerung,… |
| `verwandte-skills-vorschlag` | Verwandte Skills zu einem Mandat oder Rechtsproblem vorschlagen: Ergaenzungsempfehlungen. Normen: technisch/intern. Prüfraster: Rechtsgebiet, Verfahrensphase, Mandantentyp. Output: Vorschlagsliste verwandter Skills.… |
| `verzeichnis-durchsuchen` | Skill-Verzeichnis nach Rechtsgebiet, Norm oder Mandantentyp durchsuchen. Normen: technisch/intern. Prüfraster: Suchbegriff, Kategoriefilter, Ergebnispriorisierung. Output: Suchergebnisliste Skills. Abgrenzung: nicht… |

## Worum geht es?

Der Kanzlei-Builder-Hub ist die Steuerzentrale fuer Installation, Verwaltung und Qualitaetssicherung von Skills und Plugins in der KI-gestuetzten Kanzleiumgebung. Er fuehrt vor dem Deployment ein Security-Review-Gate durch, das Community-Skills auf Sicherheit, Normkonformitaet und Qualitaet prueft, bevor sie produktiv genutzt werden.

Der Hub ermoeglicht ausserdem die Erstellung kanzleieigener Playbooks aus vorhandenen Musterdokumenten sowie die gezielte Suche und Verwaltung des Skill-Verzeichnisses. Er richtet sich an Kanzleiinhaber, IT-Verantwortliche und Kanzleimanager, die ihre KI-Kanzleiumgebung strukturiert aufbauen und pflegen wollen.

## Wann brauchen Sie diese Skill?

- Sie wollen erstmals den Hub einrichten und Ihr Kanzleiprofil mit Rechtsgebieten und Technikvoraussetzungen erfassen.
- Sie suchen neue Community-Skills fuer ein bestimmtes Rechtsgebiet und moechten diese vor dem Einsatz sicherheitsprufen.
- Ein installierter Skill soll aktualisiert, temporaer deaktiviert oder vollstaendig deinstalliert werden.
- Sie wollen aus Ihren eigenen Musterdokumenten ein kanzleispezifisches Playbook generieren.
- Sie benoetigen eine Qualitaetspruefung aller installierten Skills auf Normaktualitaet und Strukturkonformitaet.

## Fachbegriffe (kurz erklaert)

- **Security-Review-Gate** — Strukturiertes Pruefverfahren, das vor der Freigabe eines Community-Skills Sicherheit, Normverankerung und Qualitaet bewertet.
- **Plugin** — Zusammenschluss mehrerer thematisch verwandter Skills zu einem Funktionspaket fuer ein Rechtsgebiet oder einen Workflow.
- **Skill** — Einzelne spezialisierte Anleitung in einer SKILL.md-Datei, die einen definierten Arbeitsschritt abdeckt.
- **Playbook** — Kanzleispezifischer Pruef- und Arbeitskatalog, der aus eigenen Musterdokumenten automatisch erstellt wird.
- **Kaltstart-Interview** — Strukturiertes Erstgespraech zur Erfassung von Kanzleiprofil, Rechtsgebieten und Konfigurationsparametern.
- **Fundstelle** — Normzitat oder Rechtsprechungsnachweis; der Hub prueft deren einheitliche Zitierweise.

## Rechtsgrundlagen

- § 43a BRAO — Allgemeine Berufspflichten des Rechtsanwalts (Sorgfalt, Verschwiegenheit)
- § 43e BRAO — Dienstleister-Regelung: Berufsrechtliche Anforderungen an IT-Dienstleister der Kanzlei
- Art. 28 DSGVO — Auftragsverarbeitungsvertrag bei externen Dienstleistern
- Art. 32 DSGVO — Technische und organisatorische Massnahmen

## Schritt-fuer-Schritt: Einstieg ins Plugin

1. Kanzleiprofil und Rechtsgebiete im Kaltstart-Interview erfassen.
2. Gewuenschte Skills oder Plugins im Verzeichnis suchen.
3. Security-Review-Gate vor Installation durchlaufen lassen.
4. Skill installieren und Abhaengigkeiten pruefen.
5. Qualitaetspruefung nach Installation; bei Bedarf anpassen oder deaktivieren.

## Skill-Tour (was gibt es hier?)

- `automatischer-aktualisierer` — Plugins und Skills automatisch auf neue Norm-Versionen und Rechtsprechungsaenderungen aktualisieren.
- `deaktivieren` — Einzelne Skills oder Plugins temporaer deaktivieren ohne vollstaendige Deinstallation.
- `deinstallieren` — Plugins oder Skills vollstaendig deinstallieren mit Abhaengigkeitspruefung und Datensicherung.
- `fundstellenglattzieher` — Normen- und Rechtsprechungszitate in Schriftsaetzen und Skills auf einheitliche Zitierweise bringen.
- `kanzlei-builder-hub-anpassen` — Hub an kanzleispezifische Anforderungen anpassen: eigene Plugins, Branding, Workflows.
- `kanzlei-builder-hub-kaltstart-interview` — Kaltstart-Interview: Kanzleiprofil, Rechtsgebiete und gewuenschte Plugins erfassen.
- `playbook-aus-eigenen-daten` — Kanzleieigenes Playbook aus vorhandenen Musterdokumenten automatisch generieren.
- `skill-installierer` — Neue Skills installieren mit Verfuegbarkeitscheck, Abhaengigkeitspruefung und Konfiguration.
- `skill-verwalter` — Uebersicht und Verwaltung aller installierten Skills nach Status, Version und Abhaengigkeiten.
- `skills-qualitaetspruefung` — Installierte Skills auf Normaktualitaet, Description-Qualitaet und Strukturkonformitaet pruefen.
- `verwandte-skills-vorschlag` — Verwandte Skills zu einem Mandat oder Rechtsproblem als Ergaenzungsempfehlung vorschlagen.
- `verzeichnis-durchsuchen` — Skill-Verzeichnis nach Rechtsgebiet, Norm oder Mandantentyp durchsuchen.

## Worauf besonders achten

- **Security-Review-Gate zwingend**: Community-Skills ohne Pruefung koennen falsche Normen, erfundene Aktenzeichen oder datenschutzrechtliche Schwachstellen enthalten.
- **Abhaengigkeitspruefung vor Deinstallation**: Andere Skills oder Workflows koennen auf dem zu entfernenden Skill aufbauen.
- **Normaktualitaet regelmaessig pruefen**: Gesetze und Rechtsprechung aendern sich; veraltete Skills sind ein Haftungsrisiko.
- **Datensicherung vor Deinstallation**: Kanzleieigene Anpassungen gehen bei Deinstallation ohne Sicherung unwiederbringlich verloren.
- **Kaltstart nicht ueberspringen**: Ohne vollstaendiges Kanzleiprofil sind Rechtsgebiet-Filter und Kompatibilitaetspruefungen unzuverlaessig.

## Typische Fehler

- Community-Skills ohne Security-Review direkt in die Produktion uebernehmen.
- Bei der Deinstallation nicht auf abhaengige Workflows pruefen, was zu Folgefehlern fuehrt.
- Kanzleiprofil nach Rechtsgebietswechsel nicht aktualisieren, sodass Skill-Vorschlaege nicht mehr passen.
- Fundstellen verschiedener Zitierweisen im selben Schriftsatz mischen (z. B. BGH-Aktenzeichen ohne einheitliches Format).
- Qualitaetspruefung nur bei Neuinstallation, nicht nach Gesetzesaenderungen durchfuehren.

## Querverweise

- `kanzlei-allgemein` — Zentrales Kanzlei-Workflow-Plugin, das vom Hub mit Skills bestuckt wird.
- `berufsrecht-ki-vertragspruefung` — Berufsrechtliche Pruefung von KI-Anbietervertraegen vor der Installation.
- `ki-richtlinie-kanzleien` — KI-Nutzungsrichtlinie als Rahmen fuer alle installierten KI-Skills.
- `rechtsberatungsstelle` — Skill-Verwaltung fuer studentische Beratungsstellen.

## Quellen und Aktualitaet

- Stand: 05/2026
- Gesetzesfassungen zum Stand-Datum
