# mandantenanfragen-assistent

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`mandantenanfragen-assistent`) | [`mandantenanfragen-assistent.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/mandantenanfragen-assistent.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Mandantenanfragen Q2/2026 — Kanzlei Roosendaal & Tannenfels, Köln** (`mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026`) | [Gesamt-PDF lesen](../testakten/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026/gesamt-pdf/mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026_gesamt.pdf) | [`testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-mandantenanfragen-kanzlei-roosendaal-koeln-erstkontakt-q2-2026.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

**Version:** 3.2.1
**Author:** Klotzkette
**Lizenz:** Apache-2.0 OR MIT

---

Assistent für Anwaltskanzleien zur automatisierten Erstantwort auf eingehende Mandantenanfragen per E-Mail. Das Plugin dankt formell für die Anfrage, übernimmt die exakte Anrede aus der eingehenden Mail, weist auf die telefonische Terminvergabe hin und bittet um eine Sachverhaltszusammenfassung per E-Mail. Für Personen, die nicht schreiben können oder möchten, bietet es einen automatisierten Transkriptionsservice an — mit DSGVO-konformem Einwilligungshinweis.

---

## Installation

1. ZIP aus dem Release herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `mandantenanfragen-assistent.zip` hochladen.
5. Mit einem konkreten Auftrag starten, zum Beispiel: `Beantworte diese Mandantenanfrage: [E-Mail einfügen]`

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

---

## Skills-Übersicht (15 Skills)

| # | Skill-Name | Beschreibung | Lade-Trigger (Beispiele) |
|---|---|---|---|
| 1 | `anfrage-eingang-parser` | Extrahiert aus der Eingangsmail: Anrede, Name, E-Mail, Kontaktdaten, Sachverhaltsfetzen, Dringlichkeitssignale | "Anfrage auswerten", "E-Mail analysieren", "Kontaktdaten extrahieren" |
| 2 | `anrede-uebernehmen` | Übernimmt die EXAKTE Anrede aus der Eingangsmail; Heuristiken für Titel, Doppelnamen, Adelsprädikat, kirchliche Titel, Ehepaar | "Anrede übernehmen", "formelle Anrede", "Titel erkennen" |
| 3 | `erstantwort-generator` | Hauptskill: erstellt die vollständige formelle Erstantwort-Mail mit allen Bausteinen | "Erstantwort schreiben", "Antwortmail erstellen", "Eingangsbestätigung" |
| 4 | `telefon-konfiguration` | Verwaltet Kanzlei-Kontaktdaten (Sekretariat + Transkriptionsservice) aus `kanzlei.json` und setzt sie in Templates ein | "Telefonnummer konfigurieren", "kanzlei.json bearbeiten" |
| 5 | `transkriptionsdienst-erklaerung` | Formuliert den Hinweis auf den automatisierten Transkriptionsservice: Ablauf, Datenschutz, Einwilligungserfordernis | "Transkriptionsservice erklären", "kann nicht schreiben" |
| 6 | `einwilligung-hinweis-datenschutz` | DSGVO-konforme Einwilligungsklausel für die Sprachaufnahme (Art. 6 Abs. 1 lit. a DSGVO, Art. 13 DSGVO) | "DSGVO Einwilligung formulieren", "Datenschutz Transkription" |
| 7 | `mandatsverhaeltnis-hinweis` | Formuliert den Disclaimer: kein Mandatsverhältnis, keine Rechtsberatung, keine Pflichten der Kanzlei | "kein Mandat Hinweis", "Disclaimer Erstanfrage" |
| 8 | `vertraulichkeit-erinnerung` | Hinweis auf anwaltliche Schweigepflicht § 43a Abs. 2 BRAO — gilt erst ab Mandatsbegründung | "Schweigepflicht Anwalt", "wann gilt Verschwiegenheit" |
| 9 | `folgekorrespondenz-vorbereiten` | Erstellt Skeleton-Eintrag für CRM/Akte: Name, Mail, Telefon, Anliegen, Dringlichkeit, Konfliktcheck-Status | "CRM Eintrag erstellen", "Akte anlegen" |
| 10 | `spam-und-massen-anfrage-filter` | Erkennt Spam-Muster: 419-Scams, Massen-Anfragen, Phishing, Recruiter-Mails; kennzeichnet zur Aussortierung | "Spam prüfen", "verdächtige Anfrage", "Scam-Mail" |
| 11 | `dringlichkeitsmarker` | Erkennt Fristen und Eile-Signale; setzt Stufe HOCH/MITTEL/NIEDRIG; bei HOCH: Sofortanruf des Anwalts erforderlich | "Dringlichkeit prüfen", "Frist erkannt", "Eilbedarf" |
| 12 | `konfliktcheck-vorab` | Hinweis auf Konfliktcheck-Pflicht (§ 43a Abs. 4 BRAO, § 3 BORA); instruiert Sekretariat, Gegenseite vor Terminvergabe zu erfragen | "Konfliktcheck", "Interessenkonflikt prüfen" |
| 13 | `mehrsprachige-antwort` | Erkennt Sprache der Anfrage (DE/EN/FR/IT) und schaltet Erstantwort in die entsprechende Sprache um | "Antwort auf Englisch", "mehrsprachige Erstantwort" |
| 14 | `muster-erstantwort` | Vorlage-Skill mit drei vollständigen Musterschreiben (Standard, nur Vorname, Transkriptionsservice-Modus) für Copy-paste | "Musterschreiben zeigen", "Vorlage Erstantwort" |

---

## Beispiel-Prompt

```
Ich habe soeben diese E-Mail erhalten. Bitte erstelle eine formelle Erstantwort:

Von: Dr. Klaus-Dieter Müller-Strauss <kdms@example.de>
Betreff: Frage zur fristlosen Kündigung meines Angestellten

Sehr geehrte Damen und Herren,

mein Name ist Dr. Klaus-Dieter Müller-Strauss, ich führe ein kleines
Unternehmen im Bereich Maschinenbau. Ich möchte einem meiner Mitarbeiter
fristlos kündigen wegen grober Pflichtverletzung. Was muss ich beachten?

Mit freundlichen Grüßen
Dr. Klaus-Dieter Müller-Strauss
```

Das Plugin extrahiert automatisch die Anrede, prüft auf Dringlichkeit und Spam und erstellt die vollständige Erstantwort — einschließlich aller berufsrechtlichen Hinweise.

---

## Konfiguration (kanzlei.json)

Legen Sie im Plugin-Verzeichnis eine Datei `kanzlei.json` an:

```json
{
  "kanzlei": {
    "name": "[KANZLEI-NAME]",
    "adresse": {
      "strasse": "[STRASSE UND HAUSNUMMER]",
      "plz": "[POSTLEITZAHL]",
      "ort": "[ORT]"
    },
    "telefon_sekretariat": "[SEKRETARIATS-TELEFON]",
    "telefon_transkription": "[TRANSKRIPTIONS-TELEFON]",
    "erreichbarkeit": "[Z.B. Mo-Fr 09:00-17:00 Uhr]",
    "email_kanzlei": "[KANZLEI-E-MAIL]",
    "unterzeichnende_ra": "[VORNAME NACHNAME, Rechtsanwalt/Rechtsanwaeltin]"
  }
}
```

---

## Musterschreiben

Vollständig ausformulierte Musterschreiben für drei Szenarien (mit Anrede, ohne klare Anrede, Transkriptionsservice-Variante) finden Sie in:

[references/musteranschreiben.md](references/musteranschreiben.md)

---

## Rechtliche Hinweise

Dieses Plugin ist ein Hilfswerkzeug für Anwaltskanzleien. Es ersetzt nicht die Prüfung durch einen zugelassenen Rechtsanwalt. Alle generierten Texte sind Vorschläge — die abschließende Prüfung und Freigabe jeder Erstantwort liegt beim Sekretariat und der verantwortlichen Rechtsanwältin bzw. dem verantwortlichen Rechtsanwalt.

Das Plugin enthält keine Rechtsberatung. Alle Musterschreiben sind unverbindliche Formulierungshilfen.

Berufsrechtliche Grundlagen: §§ 43 ff. BRAO, §§ 1 ff. BORA, RVG, DSGVO.

---

## Lizenz

Apache-2.0 OR MIT — siehe [LICENSE](../LICENSE), [LICENSE-APACHE](../LICENSE-APACHE), [LICENSE-MIT](../LICENSE-MIT)


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `kompendium-01-allgemein-bis-workflow-fristen-und` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 01; bündelt 3 frühere Spezialskills (allgemein, workflow-chronologie-und-belegmatrix, workflow-fristen-und-risikoampel) und bewahrt deren Workflows, Normanker, Prüfprogramme un... |
| `kompendium-02-workflow-mandantenko-bis-spezial-einwilligung` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 02; bündelt 3 frühere Spezialskills (workflow-mandantenkommunikation, workflow-redteam-qualitygate, spezial-einwilligungshinweis-fristennotiz-und-naechster-schritt) und bewahrt... |
| `kompendium-03-spezial-mandantenanf-bis-anrede-uebernehmen` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 03; bündelt 3 frühere Spezialskills (spezial-mandantenanfragen-fristen-form-und-zustaendigkeit, anfrage-eingang-parser, anrede-uebernehmen) und bewahrt deren Workflows, Normank... |
| `kompendium-04-dringlichkeitsmarker-bis-erstantwort-generato` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 04; bündelt 3 frühere Spezialskills (dringlichkeitsmarker, einwilligung-hinweis-datenschutz, erstantwort-generator) und bewahrt deren Workflows, Normanker, Prüfprogramme und Au... |
| `kompendium-05-folgekorrespondenz-v-bis-ma-aufnahmegespraech` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 05; bündelt 3 frühere Spezialskills (folgekorrespondenz-vorbereiten, konfliktcheck-vorab, ma-aufnahmegespraech-leitfaden) und bewahrt deren Workflows, Normanker, Prüfprogramme... |
| `kompendium-06-ma-einfuehrung-erstk-bis-ma-konfliktcheck-kon` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 06; bündelt 3 frühere Spezialskills (ma-einfuehrung-erstkontakt-typen, ma-erstvermerk-mandantenakte, ma-konfliktcheck-konzern) und bewahrt deren Workflows, Normanker, Prüfprogr... |
| `kompendium-07-ma-mandant-mit-betre-bis-manda-erstkontakt-tr` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 07; bündelt 3 frühere Spezialskills (ma-mandant-mit-betreuung, manda-erstgespraechsleitfaden-checkliste, manda-erstkontakt-triagebogen-bauleiter) und bewahrt deren Workflows, N... |
| `kompendium-08-manda-mandatsablehnu-bis-mandatsverhaeltnis-h` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 08; bündelt 3 frühere Spezialskills (manda-mandatsablehnung-coi-spezial, manda-rechtsschutz-eintrittsanfrage-spezial, mandatsverhaeltnis-hinweis) und bewahrt deren Workflows, N... |
| `kompendium-09-mehrsprachige-antwor-bis-spam-und-massen-anfr` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 09; bündelt 3 frühere Spezialskills (mehrsprachige-antwort, muster-erstantwort, spam-und-massen-anfrage-filter) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgab... |
| `kompendium-10-spezial-anrede-verha-bis-spezial-bittet-inter` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 10; bündelt 3 frühere Spezialskills (spezial-anrede-verhandlung-vergleich-und-eskalation, spezial-anwaltskanzleien-erstpruefung-und-mandatsziel, spezial-bittet-internationaler-... |
| `kompendium-11-spezial-dankt-risiko-bis-spezial-e-mail-ersta` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 11; bündelt 3 frühere Spezialskills (spezial-dankt-risikoampel-und-gegenargumente, spezial-dsgvo-sonderfall-und-edge-case, spezial-e-mail-erstantwort-und-terminrouting) und bew... |
| `kompendium-12-spezial-erstantwort-bis-spezial-mail-dokumen` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 12; bündelt 3 frühere Spezialskills (spezial-erstantwort-tatbestand-beweis-und-belege, spezial-foermlich-behoerden-gericht-und-registerweg, spezial-mail-dokumentenmatrix-und-lu... |
| `kompendium-13-spezial-nennt-zahlen-bis-spezial-telefon-mand` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 13; bündelt 3 frühere Spezialskills (spezial-nennt-zahlen-schwellen-und-berechnung, spezial-sachverhalt-formular-portal-und-einreichung, spezial-telefon-mandantenkommunikation-... |
| `kompendium-14-spezial-telefonische-bis-spezial-transkriptio` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 14; bündelt 3 frühere Spezialskills (spezial-telefonische-compliance-dokumentation-und-akte, spezial-terminvergabe-mehrparteien-konflikt-und-interessen, spezial-transkription-b... |
| `kompendium-15-spezial-uebernimmt-s-bis-transkriptionsdienst` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 15; bündelt 3 frühere Spezialskills (spezial-uebernimmt-schriftsatz-brief-und-memo-bausteine, telefon-konfiguration, transkriptionsdienst-erklaerung) und bewahrt deren Workflow... |
| `kompendium-16-vertraulichkeit-erin-bis-vertraulichkeit-erin` | mandantenanfragen-assistent: Konsolidiertes Skill-Kompendium 16; bündelt 1 frühere Spezialskills (vertraulichkeit-erinnerung) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster. |
| `spezial-bietet-red-team-und-qualitaetskontrolle` | Bietet: Red-Team und Qualitätskontrolle im Plugin mandantenanfragen assistent; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `spezial-eingehenden-livequellen-und-rechtsprechungscheck` | Eingehenden: Livequellen- und Rechtsprechungscheck im Plugin mandantenanfragen assistent; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin mandantenanfragen-assistent: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin mandantenanfragen-assistent: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin mandantenanfragen-assistent: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-output-waehlen` | Output wählen im Plugin mandantenanfragen-assistent: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin mandantenanfragen-assistent: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin mandantenanfragen-assistent: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
