---
name: workflow-dokumentenintake
description: "Dokumentenintake für das Plugin gewerblicher-rechtsschutz: Uploads lesen, Dokumentarten identifizieren, Fristen markieren, Arbeitsakte aufbauen und passende Spezialskills vorschlagen. Erster Schritt bei jeder neuen Mandatsunterlage."
---

# Workflow: Dokumentenintake

## Zweck

Dieser Skill nimmt **neue Dokumente und Unterlagen** entgegen, klassifiziert sie, markiert kritische Fristen und baut eine strukturierte Arbeitsakte auf. Er ist der erste Schritt bei jeder neuen Mandatsunterlage – ob Abmahnung, Registerauszug, Beschluss, Vertrag oder Korrespondenz.

Mandatsbezug: Mandant schickt eine Abmahnung mit Anlagen. Kanzleimitarbeiter lädt Unterlagen hoch. Anwalt erhält einen Schriftstapel und braucht einen schnellen Überblick. Dieser Skill sortiert, priorisiert und leitet an die richtigen Spezialskills weiter.

## Schritt 1 – Dokumentart identifizieren

Bei jedem eingehenden Dokument zuerst bestimmen:

| Dokumentkategorie | Typische Merkmale | Kritische Sofortfrage |
|---|---|---|
| Abmahnung | „Wir fordern Sie auf..." + Unterlassungserklärung beigefügt | Frist! Wann muss reagiert werden? |
| EV-Beschluss | „Im Wege der einstweiligen Verfügung wird angeordnet..." | Vollziehungsfrist (§ 929 Abs. 2 ZPO)! |
| Klage / Klageschrift | „Wir erheben Klage..." | Antwortfrist! |
| DPMA-Bescheid | Auf Markenbriefkopf; Markenblatt-Veröffentlichung | Widerspruchsfrist (3 Monate)? |
| EUIPO-Bescheid | Auf EUIPO-Briefkopf; englisch/deutsch | Fristen EUIPO? |
| Registereintragung | DPMA/EUIPO Eintragungsurkunde | Schutz aktiv? Verlängerungsfristen? |
| Abmahnreaktionsschreiben | Antwort auf eigene Abmahnung | Ist UE enthalten? Frist gewahrt? |
| Urteil / Beschluss | Auf Gerichtsbriefkopf; Tenor klar | Rechtsmittelfrist (1 Monat)? |
| Lizenzvertrag | „...wird eine Lizenz gewährt..." | Vertragskonditionen, Pflichten, Kündigungsfristen |
| Rechnung/Kaufbeleg | Produktname, Kaufdatum | Verletzungsbeleg? |

## Schritt 2 – Fristen sofort markieren

**Sofortprüfung:** Enthält das Dokument eine Frist oder löst es eine Frist aus?

| Dokumenttyp | Ausgelöste Frist | Dauer | Aktion |
|---|---|---|---|
| Abmahnung | Reaktionsfrist | Gesetzt (i.d.R. 14 Tage) | Sofort in Fristenbuch; Mandant informieren |
| EV-Beschluss (bei Antragsteller) | Vollziehungsfrist § 929 Abs. 2 ZPO | 1 Monat | GV-Auftrag vorbereiten |
| DPMA-Markenblatt-Veröffentlichung | Widerspruchsfrist | 3 Monate | DPMA-Widerspruch prüfen |
| EUIPO-Veröffentlichung | Widerspruchsfrist | 3 Monate | EUIPO-Widerspruch prüfen |
| Gerichtsurteil | Rechtsmittelfrist | 1 Monat | Berufung prüfen |
| EPA-Erteilungsveröffentlichung | Einspruchsfrist | 9 Monate | Einspruch prüfen |

## Schritt 3 – Dokument in Arbeitsakte einordnen

**Aktengliederung nach Dokumenttyp:**

```
Arbeitsakte [Mandant ./. Gegenseite / Sache]
│
├── A – Schutzrechte
│   ├── Registerauszüge (Marke, Patent, Design)
│   └── Schutzrechtsurkunden
│
├── B – Verletzungsnachweis
│   ├── Screenshots mit Datum und URL
│   ├── Kaufbelege / Testkauf
│   └── Zeugenaussagen / Eidesstattliche Versicherungen
│
├── C – Abmahnkorrespondenz
│   ├── Abmahnschreiben (versandt)
│   ├── Abmahnreaktionen (empfangen)
│   └── Unterlassungserklärungen
│
├── D – Gerichtsverfahren
│   ├── Antragsschriften (EV, Klage)
│   ├── Gerichtsbeschlüsse / Urteile
│   └── Vollstreckungsunterlagen (Zustellurkunden)
│
├── E – Behördenverfahren
│   ├── DPMA-Schriftsätze
│   ├── EUIPO-Schriftsätze
│   └── EPA-Schriftsätze
│
└── F – Mandantenkommunikation
    ├── Entscheidungsvorlagen
    ├── Mandantenbriefe
    └── Honorarvereinbarungen
```

## Schritt 4 – Spezialskills vorschlagen

Nach Dokumentklassifizierung passenden Spezialskill auswählen:

| Dokument erkannt | Empfohlener Skill |
|---|---|
| Abmahnung UWG empfangen | `gewr-uwg-abmahnung-checkliste` |
| Abmahnung Markenrecht empfangen | `verletzungs-triage` + `unterlassungsverlangen` |
| EV-Beschluss (Antragsteller) | `evvollzug-neu-001` |
| EV-Beschluss (Antragsgegner) | `evvollzug-neu-008` (Schutzschrift) + `unterlassungsverlangen` |
| DPMA-Veröffentlichung | `spezial-dpma-fristen-form-und-zustaendigkeit` |
| EUIPO-Veröffentlichung | `spezial-euipo-dokumentenmatrix-und-lueckenliste` |
| Lizenzvertrag zur Prüfung | `ip-klausel-pruefung` |
| Registerauszug | `markenrecherche` oder `fto-triage` |
| Zollbeschlagnahme | `takedown-anweisung` |

## Schritt 5 – Kurzlage erstellen

Nach Intake sofortige Kurzlage ausgeben:

```
KURZLAGE – DOKUMENTENINTAKE
Datum: _______________
Eingehendes Dokument: _______________
Dokumentkategorie: _______________
Kritische Frist: _______________  (Fristende: _______)
Empfohlener nächster Skill: _______________
Fehlende Informationen: _______________
Mandant informiert: Ja / Nein / Ausstehend
```

## Quellenregel

- Keine externen Quellen für diesen Prozess-Skill.
- Bei identifizierten Fristen: Normen immer live prüfen (gesetze-im-internet.de, dejure.org).
- Dateien und Dokumente niemals in ihrer Substanz verändern oder umformulieren ohne ausdrückliche Anweisung.

## Anschluss-Skills

- `workflow-fristen-und-risikoampel` – Fristenworkflow
- `workflow-chronologie-und-belegmatrix` – Sachverhalts-Chronologie
- `workflow-kaltstart-und-routing` – Kaltstart-Router
- `spezial-schutzrechts-fristennotiz-und-naechster-schritt` – Fristennotiz
