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
| `anrede-anwaltskanzleien-bittet` | Anrede Anwaltskanzleien Bittet im Mandantenanfragen-Triage: prüft konkret Anrede, Anwaltskanzleien, Bittet. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `bietet-fehlerkatalog` | Bietet Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `dankt-dsgvo-sonderfall-e-mail` | Dankt DSGVO Sonderfall E Mail im Mandantenanfragen-Triage: prüft konkret Dankt, DSGVO, E-Mail-Erstantwort, Terminrouting und Mandatsannahmehinweis. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `dringlichkeitsmarker-einwilligung-hinweis` | Dringlichkeitsmarker Einwilligung Hinweis im Mandantenanfragen-Triage: prüft konkret Eingehende Mandantenanfrage enthaelt möglicherweise, Kanzlei bietet telefonischen Transkriptionsservice an und, Sekretariat oder Anwalt muss professione... |
| `eingehenden-quellenkarte` | Eingehenden Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `erstantwort-foermlich-mail` | Erstantwort Foermlich Mail im Mandantenanfragen-Triage: prüft konkret Erstantwort, Foermlich, Mail. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `folgekorrespondenz-vorbereiten-konfliktcheck` | Folgekorrespondenz Vorbereiten Konfliktcheck im Mandantenanfragen-Triage: prüft konkret Nach Eingang einer Anfrage muss Sekretariat CRM-Eintrag und, Sekretariat soll vor Terminvergabe Interessenkonflikt prüfen, Aufnahmegespraechsleitfade... |
| `ma-mandant-manda-erstgespraechsleitfaden` | MA Mandant Manda Erstgespraechsleitfaden im Mandantenanfragen-Triage: prüft konkret Spezialfall Mandant mit gesetzlicher Betreuung oder, Checkliste Erstgespraechsleitfaden, Bauleiter Triagebogen Erstkontakt. Liefert priorisierten Output... |
| `manda-mandatsablehnung-rechtsschutz` | Manda Mandatsablehnung Rechtsschutz im Mandantenanfragen-Triage: prüft konkret Spezialfall Mandatsablehnung und COI-Kommunikation, Spezialfall Rechtsschutzversicherung-Eintrittsanfrage, Antwortmail muss klar machen dass noch kein. Liefer... |
| `mandantenanfragen-anfrage-eingang-anrede` | Anfrage Eingang Anrede im Mandantenanfragen-Triage: prüft konkret Mandantenanfragen, Sekretariat oder Anwalt erhielt E-Mail-Anfrage eines, Antwort-E-Mail soll mit exakt richtiger Anrede des. Liefert priorisierten Output mit Norm-Pinpoint... |
| `mandantenanfragen-assistent-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `mandantenanfragen-assistent-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `mandantenanfragen-assistent-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `mandantenanfragen-assistent-ma-einfuehrung-erstkontakt` | MA Einfuehrung Erstkontakt im Mandantenanfragen-Triage: prüft konkret Erstkontakt-Typen einfuehrend, Erstvermerk fuer die Mandantenakte, Spezialfall Konfliktcheck im Konzern. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel u... |
| `mandantenanfragen-assistent-mandantenkommunikation-redteam` | Mandantenkommunikation Redteam im Mandantenanfragen-Triage: prüft konkret Mandantenkommunikation im Plugin mandantenanfragen-assistent, Red-Team Qualitygate im Plugin mandantenanfragen-assistent, Einwilligungshinweis. Liefert priorisiert... |
| `mandantenanfragen-assistent-output-waehlen` | Output wählen im Mandantenanfragen-Triage: Diese Output-Weiche für Mandantenanfragen Assistent entscheidet, ob Memo, Antrag, Schriftsatz, Tabelle, Risikoampel, Fragenliste oder Mandantenbrief der richtige nächste Schritt ist. |
| `mandantenanfragen-assistent-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `mandantenanfragen-assistent-start-chronologie-fristen` | Start Chronologie Fristen im Mandantenanfragen-Triage: prüft konkret Einstieg, Schnelltriage und Fallrouting im Mandantenanfragen, Chronologie und Belegmatrix im Plugin, Fristen- und Risikoampel im Plugin. Liefert priorisierten Output mi... |
| `mandantenanfragen-assistent-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `mehrsprachige-antwort-muster-erstantwort-spam` | Mehrsprachige Antwort Muster Erstantwort Spam im Mandantenanfragen-Triage: prüft konkret Mandantenanfrage kam auf Englisch Franzoesisch oder, Kanzlei benoetigt fertige ausfuellbare Vorlage für die, Sekretariat hat Anfrage erhalten die ve... |
| `nennt-sachverhalt-telefon` | Nennt Sachverhalt Telefon im Mandantenanfragen-Triage: prüft konkret Nennt, Sachverhalt, Telefon. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `telefonische-terminvergabe-interessen` | Telefonische Terminvergabe Interessen im Mandantenanfragen-Triage: prüft konkret Telefonische, Terminvergabe, Transkription. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt. |
| `uebernimmt-telefon-konfiguration` | Uebernimmt Telefon Konfiguration im Mandantenanfragen-Triage: prüft konkret Uebernimmt, Kanzlei muss Telefonnummern für Sekretariat und, Mandant kann seinen Fall nicht schriftlich schildern und. Liefert priorisierten Output mit Norm-Pinp... |
| `vertraulichkeit-erinnerung` | Vertraulichkeit Erinnerung im Mandantenanfragen-Triage: fachlicher Arbeitsgang mit Prüffeldwahl, Norm-/Quellencheck, Risikoampel und verwertbarem Output. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
