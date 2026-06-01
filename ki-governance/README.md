# KI-Governance-Plugin

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`ki-governance`) | [`ki-governance.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-governance.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **KI-Governance Konzern-Rollout — Thalheim Industries SE** (`ki-governance-konzern-rollout-thalheim-industries`) | [Gesamt-PDF lesen](../testakten/ki-governance-konzern-rollout-thalheim-industries/gesamt-pdf/ki-governance-konzern-rollout-thalheim-industries_gesamt.pdf) | [`testakte-ki-governance-konzern-rollout-thalheim-industries.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-governance-konzern-rollout-thalheim-industries.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

<!-- BEGIN plugin-testakten-section (autogen) -->
## Demonstrations-Akten

Folgende anonymisierte Akte demonstriert dieses Plugin im laufenden Mandatsbetrieb. Das Gesamt-PDF ist sofort im Browser lesbar. Das Akten-ZIP enthaelt saemtliche Originaldateien (Markdown-Aktenstuecke, Tabellen, E-Mails, PDFs, DOCX, XLSX, Bildanlagen) im Originalordnerlayout.

| Akte | Lesen | Herunterladen |
| --- | --- | --- |
| **KI-Governance Konzern-Rollout — Thalheim Industries SE** (`ki-governance-konzern-rollout-thalheim-industries`) | [Gesamt-PDF lesen](../testakten/ki-governance-konzern-rollout-thalheim-industries/gesamt-pdf/ki-governance-konzern-rollout-thalheim-industries_gesamt.pdf) | [Akten-ZIP herunterladen](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-ki-governance-konzern-rollout-thalheim-industries.zip) |

Die ZIP-URLs sind stabil und zeigen immer auf die aktuelle Version. Eine vollstaendige Aktenuebersicht steht in [`testakten/README.md`](../testakten/README.md).

<!-- END plugin-testakten-section (autogen) -->

Abläufe für betriebliche und kanzleiinterne KI-Governance: Use-Case-Triage, KI-Folgenabschätzungen,
Vendor-KI-Review und Gap-Analyse neuer Rechtsakte gegenüber bestehender Richtlinien- und Praxislage.
Das Plugin ist auf die EU-KI-Verordnung (VO 2024/1689, "KI-VO"), die DSGVO, das BDSG sowie
einschlägige deutschsprachige Rechtsgrundlagen (ProdHaftG, GeschGehG, UrhG, § 203 StGB) ausgerichtet.

**Jede Ausgabe ist ein Entwurf zur anwaltlichen Prüfung – mit Fundstellen, Markierungen und
Kontrollgates versehen; kein Rechtsgutachten.** Das Plugin erledigt die Vorarbeit: Dokumente
lesen, Prüfrahmen anwenden, Probleme aufdecken, Memo entwerten. Der Anwalt prüft, verifiziert
und entscheidet. Quellenangaben sind nach Herkunft gekennzeichnet. Berufsrechtliche Markierungen
(§ 203 StGB, § 43a Abs. 2 BRAO) werden konservativ gesetzt. Folgenreiche Handlungen
(Einreichen, Versenden, Ausführen) werden vor Umsetzung explizit bestätigt.

## ⬇️ Direkt-Download (einzelnes ZIP)

| Plugin | Direkt-Download |
| --- | --- |
| KI-Governance (`ki-governance`, dieses Plugin) | [ki-governance.zip](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/ki-governance.zip) |

Die URL ist stabil und zeigt immer auf die neueste Version. Alle weiteren Plugins sind unter [Releases · latest](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest) genauso einzeln verfügbar.

### Installation in Claude Code

1. ZIP herunterladen (Link oben).
2. Claude Code → **Customize Plugins** → **Install from .zip** → Datei wählen.
3. Fertig. Skills sind sofort verfügbar.

> **Hinweis:** Für den ZIP-Upload muss das Archiv direkt `.claude-plugin/plugin.json`, `skills/`, `assets/` und `references/` im ZIP-Root enthalten. **Nicht** das komplette Repository-ZIP aus "Code → Download ZIP" verwenden.


## Zielgruppe

| Rolle | Primäre Abläufe |
|---|---|
| **Datenschutzbeauftragte / KI-Governance-Counsel** | Folgenabschätzungen, Vendor-KI-Review, Gap-Analyse |
| **Syndikusanwälte / Produktjuristen** | Use-Case-Triage, Launch-Review mit KI-Komponente |
| **GC / Legal Ops** | KI-Richtlinien-Governance, Eskalation, Vorstandsthemen |
| **Einkauf / Vertragsrecht** | Vendor-KI-Vertragsreview nach Art. 28 DSGVO / Art. 11 KI-VO |

## Erster Start: das Kaltstart-Interview

Das Plugin befragt Sie, um zu erfahren: Sind Sie Anbieter, Betreiber oder beides? Welche
Regelwerke greifen konkret? Wo sind die roten Linien? Wie sieht eine interne Folgenabschätzung
bei Ihnen aus? Danach liest es Ihre Seed-Dokumente und lernt Ihre tatsächlichen Positionen
und Ihren Haustil.

```
/ki-governance:ki-governance-kaltstart-interview
```

## Befehle

| Befehl | Funktion |
|---|---|
| `/ki-governance:ki-governance-kaltstart-interview` | Kaltstart-Interview – schreibt Ihr Praxisprofil |
| `/ki-governance:ki-inventar [list \| add \| edit \| classify \| show]` | KI-Inventar verwalten – Rolle und Risikoklasse je KI-System nach KI-VO erfassen |
| `/ki-governance:anwendungsfall-triage [Anwendungsfall]` | Use-Case gegen Ihr Register prüfen (genehmigt / bedingt / nie) |
| `/ki-governance:ki-folgenabschaetzung [Anwendungsfall]` | KI-Folgenabschätzung (FRIA Art. 27 KI-VO + DSFA Art. 35 DSGVO) erstellen |
| `/ki-governance:ki-anbieter-pruefung [Anbieter/Datei]` | Vendor-KI-Vertrag gegen Ihre Positionen prüfen |
| `/ki-governance:regulierungs-luecken-analyse [Rechtsakt]` | Neuen Rechtsakt oder Leitlinie gegen aktuelle Richtlinien/Praxis abgleichen |
| `/ki-governance:richtlinien-monitor` | Wöchentliche Prüfung auf Richtliniendrift oder direkte Anfrage zu neuer Praxis |
| `/ki-governance:richtlinien-vorlage` | Erstentwurf einer KI-Richtlinie auf Basis Ihres Praxisprofils erstellen |
| `/ki-governance:ki-governance-mandat-arbeitsbereich` | Mandatsworkspaces verwalten (nur Kanzleipraxis) – new, list, switch, close, none |

## Skills

| Skill | Zweck |
|---|---|
| **kaltstart-interview** | Schreibt `~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md` aus Interview + Seed-Dokumente |
| **ki-inventar** | KI-Inventar nach KI-VO – Rolle (Anbieter, Betreiber, Einführer, Händler, Bevollmächtigter, Produkthersteller) und Risikoklasse je System, Art. 6 KI-VO |
| **anwendungsfall-triage** | Prüft Anwendungsfälle gegen das Register; meldet fehlende Folgenabschätzungen |
| **ki-folgenabschaetzung** | KI-Folgenabschätzung im Hausformat (FRIA + DSFA) |
| **ki-anbieter-pruefung** | KI-spezifischer Vertragsreview gegen Governance-Positionen (Art. 11 KI-VO, Art. 28 DSGVO) |
| **regulierungs-luecken-analyse** | Neuer Rechtsakt/Leitlinie vs. Ist-Stand, Remediation-Plan |
| **richtlinien-monitor** | Prüft Ausgaben auf Praxisdrift; entwirft KI-Richtlinien-Updates |
| **richtlinien-vorlage** | Erstellt KI-Richtlinien-Entwurf auf Basis publizierter Musterrichtlinien (BVDW, Bitkom, EDSA, BSI, KI-VO), angepasst an Ihr Praxisprofil |
| **mandat-arbeitsbereich** | Mandatsworkspaces anlegen, auflisten, wechseln und schließen; isoliert jeden Mandanten/Auftrag, damit Kontext nicht durchsickert |

## Schnellstart

### 1. Einrichtung

```
/ki-governance:ki-governance-kaltstart-interview
```

Halten Sie bereit (soweit vorhanden): Ihre KI- oder Acceptable-Use-Richtlinie, eine frühere
Folgenabschätzung, Vendor-KI-Verträge, KI-Modell-Inventar oder genehmigte Tool-Liste.

Ihre Konfiguration wird gespeichert unter
`~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
und überlebt Plugin-Updates.

### 2. Neuen Anwendungsfall prüfen

```
/ki-governance:anwendungsfall-triage "Vertrieb möchte KI zur automatischen Lead-Bewertung einsetzen"
```

Ausgabe: Risikoklasse nach KI-VO, Registerabgleich oder -lücke, erforderliche Bedingungen,
Folgenabschätzung erforderlich oder nicht.

### 3. Folgenabschätzung erstellen

```
/ki-governance:ki-folgenabschaetzung "KI-gestützte Lebenslauf-Analyse für HR"
```

Aufnahme-Fragen → Folgenabschätzung im Hausformat → Richtlinien-Konsistenzprüfung →
Mitigationsbedingungen.

### 4. Vendor-KI-Vertrag prüfen

```
/ki-governance:ki-anbieter-pruefung openai-terms.pdf
```

Ausgabe: Klausel-für-Klausel-Vergleich mit Ihren Positionen, vorgeschlagene Änderungen,
Eskalationslücken.

## Dreieck: KI-Governance ↔ Produktrecht ↔ Datenschutzrecht

Diese drei Plugins sind aufeinander abgestimmt. KI-Governance ist das dritte Element.

- **Produktrecht** erkennt, wenn ein Launch eine KI-Komponente enthält → Übergabe an
  `/ki-governance:anwendungsfall-triage` und `/ki-governance:ki-folgenabschaetzung`
- **Datenschutzrecht** erkennt, wenn ein KI-Anwendungsfall personenbezogene Daten umfasst →
  Übergabe an `/datenschutzrecht:dsfa-erstellung`, sofern das Plugin installiert ist
- **KI-Governance** erkennt, wenn eine Folgenabschätzung datenschutzrechtliche Fragen aufwirft →
  Übergabe an `/datenschutzrecht:dsfa-erstellung`

Die Übergabe ist explizit: Jedes Plugin meldet, wann das andere benötigt wird, und benennt
die zu klärende Frage.

## Rechtliche Grundlagen (Überblick)

| Rechtsakt | Relevanz im Plugin |
|---|---|
| **KI-VO (VO 2024/1689)** | Risikoklassen (Art. 6, Anh. I–III), Verbote (Art. 5), Betreiberpflichten (Art. 26), Transparenz (Art. 50), Bußgeld (Art. 99), FRIA (Art. 27), Technische Dokumentation (Art. 11) |
| **DSGVO** | DSFA (Art. 35), Auftragsverarbeitung (Art. 28), Auskunftsrecht (Art. 15), Automatisierte Entscheidungen (Art. 22) |
| **BDSG** | Beschäftigtendatenschutz (§ 26), ergänzende Regelungen zur DSGVO |
| **ProdHaftG / Produktsicherheitsrecht** | KI-Systeme als Produkte; Haftung für fehlerhafte KI-Ausgaben |
| **GeschGehG** | Schutz von Trainings- und Prozessdaten, Geheimhaltungspflichten |
| **UrhG / § 44b UrhG** | Text- und Data-Mining-Schranke (Art. 4 DSM-RL), Trainingsdaten, Opt-out |
| **§ 203 StGB** | Mandantengeheimnis, Schweigepflicht bei KI-Einsatz in der Kanzlei |

## Dateistruktur

```
ki-governance/
├── CLAUDE.md
├── README.md
├── references/
│   └── currency-watch.md
└── skills/
    ├── kaltstart-interview/
    ├── ki-inventar/          (ki-inventar)
    ├── anwendungsfall-triage/
    ├── ki-folgenabschaetzung/
    ├── ki-anbieter-pruefung/
    ├── regulierungs-luecken-analyse/
    ├── richtlinien-monitor/
    ├── richtlinien-vorlage/
    ├── mandat-arbeitsbereich/
    └── anpassen/
```

## Wie das Plugin lernt

Ihr Praxisprofil unter
`~/.claude/plugins/config/claude-fuer-deutsches-recht/ki-governance/CLAUDE.md`
ist nicht statisch – es verbessert sich durch die Nutzung. Skills zeigen an, wenn eine Ausgabe
auf einem Standard basiert, den Sie anpassen sollten. Der `richtlinien-monitor`-Agent beobachtet
Drift zwischen Ihrer KI-Governance-Richtlinie und Ihrer Praxis und schlägt Updates vor.
Sie können das Setup wiederholen, die Datei direkt bearbeiten oder einem Skill mitteilen, eine
neue Position zu erfassen.

## Hinweise

- **Gap-Analyse** (`regulierungs-luecken-analyse`) verarbeitet eingehende Rechtsakte. **Policy-Monitor**
  behandelt internen Praxisdrift. Verschiedene Werkzeuge für verschiedene Änderungsrichtungen.
- Policy-Monitor benötigt einen konfigurierten Ausgabeordner für den Sweep. Direktabfrage-Modus
  funktioniert ohne diesen.
- Use-Case-Triage ist nur so gut wie das Register. Verbringen Sie Zeit im Setup-Interview damit,
  die roten Linien richtig zu erfassen – sie steuern alles.
- Format der Folgenabschätzung kommt aus Ihrer Seed-Folgenabschätzung. Ohne Seed-Dokument
  wird eine Grundstruktur verwendet – führen Sie das Setup erneut durch, um es zu verbessern.
- Anbieter- und Betreiberpflichten werden getrennt behandelt. Wenn Sie beides sind, fragen die
  Skills, welche Rolle Sie für die jeweilige Aufgabe tragen.
- Gap-Analyse ist manuell (Sie weisen auf einen Rechtsakt oder ein Leitliniendokument hin). Für
  automatisiertes Monitoring koppeln Sie mit dem `regulatorisches-recht`-Plugin.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 54 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im KI Governance-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klaren Arbeitsplan. Bei... |
| `anwendungsfall-triage` | 'Klassifiziert einen vorgeschlagenen KI-Anwendungsfall gegen das Unternehmensregister — freigegeben, bedingt oder nicht freigegeben — und erstellt Auflagenliste und nächste Schritte. Prüft gegen verbotene Praktiken (Art. 5 KI-VO) und Hoc... |
| `gpai-modelle-systemic-risk` | General-Purpose-AI-Modelle Art. 51 ff. KI-VO: Standardpflichten (Dokumentation, Trainingsdaten, Urheberrecht), zusaetzliche Pflichten fuer Modelle mit systemischem Risiko ab 10E25 FLOPs Trainingsrechenleistung. Verhaltenskodex und CE-Mod... |
| `ki-anbieter-pruefung` | 'Prüft KI-Anbieterverträge gegen die unternehmenseigenen Governance- Positionen; kennzeichnet Training auf Daten, Haftung, Modelländerungen und KI-Richtlinien-Konsistenz. Unterscheidet Anbieter/Betreiber-Rolle nach Art. 3 KI-VO; prüft Ve... |
| `ki-arbeitsrecht-mitbestimmung` | Arbeitsrechtliche Folgen des KI-Einsatzes: Mitbestimmung des Betriebsrats § 87 Abs. 1 Nr. 6 BetrVG technische Einrichtung zur Verhaltens- und Leistungskontrolle, Betriebsvereinbarung KI, Datenschutz BDSG-neu und DSGVO. Bewerber-KI und Au... |
| `ki-folgenabschaetzung` | 'KI-Folgenabschätzung (FRIA nach Art. 27 KI-VO + DSFA nach Art. 35 DSGVO) erstellen – strukturierte Aufnahme, Risikoanalyse, Regulierungsklassifizierung nach KI-VO und DSGVO, Richtlinien-Konsistenzprüfung und Empfehlung mit Bedingungen.... |
| `ki-governance-anpassen` | 'Geführte Anpassung Ihres KI-Governance-Praxisprofils – eine Einstellung ändern, ohne das vollständige Kaltstart-Interview neu zu starten. Risikoeinstellung, Eskalationskontakte, Use-Case-Register-Einträge, Vendor-KI-Positionen, KI-Richt... |
| `ki-governance-kaltstart-interview` | KI-Governance-Plugin erstmalig einrichten oder Inventar der KI-Systeme im Unternehmen erfassen und AI-Act-Anwendungsbereich prüfen. Führt Erstgespraech durch ermittelt KI-Inventar Rolle im KI-Lieferkette (Anbieter/Betreiber Art. 3 KI-VO... |
| `ki-governance-mandat-arbeitsbereich` | 'Mandats-Arbeitsbereiche verwalten – neu, liste, wechseln, schließen oder keines (Praxisebene). Datei- Verwaltungslogik, um den Kontext eines Mandanten oder Auftrags von jedem anderen zu trennen. Verwenden, wenn mandatsübergreifend gearb... |
| `ki-governance-rollen-rasci` | Rollen-Modell RASCI fuer KI-Governance: KI-Beauftragte, IT-Sicherheit, Datenschutzbeauftragte, Compliance, Fachbereiche, Geschaeftsfuehrung, Betriebsrat. Pro Rolle: Responsibility, Accountability, Support, Consulted, Informed. Vorlage fu... |
| `ki-haftung-und-versicherung` | Haftung beim Einsatz von KI: Anbieter- und Betreiberhaftung KI-VO, Produkthaftungsgesetz neu nach RL EU 2024 2853, ueberschiessende KI-Haftungs-RL (Entwurf), Vertragshaftung. Versicherbarkeit (D and O, Cyber, KI-spezifisch). Pruefraster... |
| `ki-hochrisiko-anhang-iii-pruefen` | Hochrisiko-KI nach Anhang III KI-VO pruefen: Biometrie, kritische Infrastruktur, Bildung, Beschaeftigung, Zugang zu Diensten, Strafverfolgung, Migration, Justiz, demokratische Prozesse. Pruefraster Schritt fuer Schritt mit Belegen aus de... |
| `ki-incident-management-art-73` | Incident-Management nach Art. 73 KI-VO: ernsthafte Vorfaelle melden binnen 15 Tagen, bei Tod oder schwerer Gesundheit binnen 10 Tagen. Pflicht zur Ursachenanalyse, Korrekturmassnahmen. Datenbank der Marktueberwachungsbehoerden. Playbook... |
| `ki-inventar` | 'KI-System-Inventar nach EU-KI-VO (VO 2024/1689) – erfasst je KI-System Rolle (Anbieter, Betreiber, Einführer, Händler, Bevollmächtigter, Produkthersteller) und Risikoklasse (verboten, hochrisiko, begrenzt, minimal, Allzweck-KI, systemis... |
| `ki-marketing-und-werbung` | KI im Marketing und Werbung: KI-VO-Transparenzpflichten bei synthetischen Inhalten Art. 50, Persoenlichkeitsrecht bei Stimmen- und Gesichtssimulation, UWG bei irrefuehrender Werbung, Empfehlungslogiken und Manipulationsverbot. Compliance... |
| `ki-rote-linien-art-5-pruefen` | Verbotene KI-Praktiken Art. 5 KI-VO im konkreten Anwendungsfall pruefen: unterschwellige Beeinflussung, Vulnerabilitaetsausnutzung, Social Scoring, biometrische Echtzeit-Identifikation im oeffentlichen Raum, Emotionserkennung am Arbeitsp... |
| `ki-vo-pflichtenpyramide-einfuehrung` | Pflichtenpyramide KI-VO einfuehrend: verbotene KI Art. 5, Hochrisiko-KI Art. 6 in Verbindung mit Anhang III, GPAI (General Purpose AI) Art. 51 ff., begrenztes Risiko mit Transparenzpflichten Art. 50, minimales Risiko. Tabellarische Ueber... |
| `kig-ai-act-rollenmodell-bauleiter` | Bauleiter AI-Act-Rollenmodell: Anbieter, Betreiber, Importeur, Vertriebshaendler, Bevollmaechtigter. Pruefraster fuer Identifikation und Pflichtenkatalog je Rolle. |
| `kig-foundation-model-anbieterpflichten-spezial` | Spezialfall Foundation Model und GPAI-Anbieterpflichten Art. 53 ff. AI Act: Transparenz, Trainingsdaten, systemisches Risiko ab Schwellenwert. Pruefraster fuer Anbieter und Downstream-Deployer. |
| `kig-konformitaetsbewertung-spezial` | Spezialfall Konformitaetsbewertungsverfahren Hochrisiko-KI Art. 43 AI Act: interne Kontrolle, benannte Stelle, EU-Konformitaetserklaerung, CE-Kennzeichnung. Pruefraster fuer Anbieter. |
| `kig-risikobewertung-hochrisiko-leitfaden` | Leitfaden Risikobewertung Hochrisiko-KI Anhang III AI Act: Bereiche Bildung / Beschaeftigung / Kreditscoring / Migration. Pruefraster fuer Klassifizierung und Ausnahme. |
| `regulierungs-luecken-analyse` | 'Gleicht eine neue KI-Regulierung oder Behördenleitlinie mit der aktuellen Governance-Position ab — identifiziert Lücken, Prioritäten und einen Maßnahmenplan mit Verantwortlichen und Fristen. Lädt, wenn der Nutzer "Lückenanalyse AI Act",... |
| `richtlinien-monitor` | 'Überwacht die interne KI-Richtlinie auf Abweichungen von der gelebten Praxis — wöchentlicher Abgleich gespeicherter Folgenabschätzungen, Triage-Ergebnisse und Anbieterprüfungen, oder direkte Prüfung einer geplanten neuen KI-Praxis. Lädt... |
| `richtlinien-vorlage` | 'Entwirft eine interne KI-Nutzungsrichtlinie auf Basis veröffentlichter Musterrichtlinien und des Praxisprofils — Recherche- und Synthese-Tool, dessen Ausgabe ein Entwurf für die anwaltliche Prüfung und Freigabe ist, keine fertige Richtl... |
| `spezial-anbieter-mehrparteien-konflikt-und-interessen` | Anbieter: Mehrparteienkonflikt und Interessenmatrix: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-case-tatbestand-beweis-und-belege` | Case: Tatbestandsmerkmale, Beweisfragen und Beleglage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-dpia-risikoampel-und-gegenargumente` | Dpia: Risikoampel, Gegenargumente und Verteidigungslinien: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-drift-verhandlung-vergleich-und-eskalation` | Drift: Verhandlung, Vergleich und Eskalation: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-dsgvo-erstpruefung-und-mandatsziel` | DSGVO: Erstprüfung, Rollenklärung und Mandatsziel: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-governance-compliance-dokumentation-und-akte` | Governance: Compliance-Dokumentation und Aktenvermerk: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-inventar-dokumentenmatrix-und-lueckenliste` | Inventar: Dokumentenmatrix, Lückenliste und Nachforderung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-ki-inventar-governance-und-kontrollen` | KI-Inventar, Governance und Kontrollen: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-konformitaetsbewertung-red-team-und-qualitaetskontrolle` | Konformitaetsbewertung: Red-Team und Qualitätskontrolle: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-marketing-mandantenkommunikation-entscheidungsvorlage` | Marketing: Mandantenkommunikation und Entscheidungsvorlage: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-monitoring-livequellen-und-rechtsprechungscheck` | Monitoring: Livequellen- und Rechtsprechungscheck: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-pruefung-internationaler-bezug-und-schnittstellen` | Pruefung: Internationaler Bezug und Schnittstellen: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rechtsquellen-sonderfall-und-edge-case` | Rechtsquellen: Sonderfall und Edge-Case-Prüfung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-review-schriftsatz-brief-und-memo-bausteine` | Review: Schriftsatz-, Brief- und Memo-Bausteine: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-richtlinie-zahlen-schwellen-und-berechnung` | Richtlinie: Zahlen, Schwellenwerte und Berechnung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-rollenmodell-formular-portal-und-einreichung` | Rollenmodell: Formular, Portal und Einreichungslogik: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-triage-fristen-form-und-zustaendigkeit` | Triage: Fristen, Form, Zuständigkeit und Rechtsweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-use-case-risk-classification` | Use-Case-Risikoklassifizierung nach KI-VO und DSGVO: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-vendor-behoerden-gericht-und-registerweg` | Vendor: Behörden-, Gerichts- oder Registerweg: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `spezial-werbung-beweislast-und-darlegungslast` | Werbung: Beweislast, Darlegungslast und Substantiierung: konkreter Spezialworkflow mit Sachverhaltsklärung, Rechtsrahmen, Belegen, Risikoampel und verwertbarem Output. |
| `workflow-anschluss-skills-router` | Anschluss-Skills Router im Plugin ki-governance: schlägt nach der ersten Prüfung die passenden Spezialskills aus demselben Plugin vor. |
| `workflow-chronologie-und-belegmatrix` | Chronologie und Belegmatrix im Plugin ki-governance: macht aus unordentlichem Material eine Timeline mit Belegstellen und offenen Widersprüchen. |
| `workflow-dokumentenintake` | Dokumentenintake im Plugin ki-governance: liest Uploads, sortiert Dokumentarten, markiert Fristen und baut eine knappe Arbeitsakte. |
| `workflow-fristen-und-risikoampel` | Fristen- und Risikoampel im Plugin ki-governance: macht eine Sofortampel für Frist, Zuständigkeit, Haftung, Eilbedarf und fehlende Unterlagen. |
| `workflow-kaltstart-und-routing` | Kaltstart und Routing im Plugin ki-governance: führt vom ersten Satz oder Dokument in den passenden Arbeitsweg, erkennt Rolle, Ziel, Risiko und Anschluss-Skills. |
| `workflow-mandantenkommunikation` | Mandantenkommunikation im Plugin ki-governance: übersetzt das Ergebnis in eine klare Nachricht mit Entscheidungspunkten, Risiken und nächsten Schritten. |
| `workflow-output-waehlen` | Output wählen im Plugin ki-governance: entscheidet zwischen Memo, Schriftsatz, Tabelle, Brief, Checkliste, Vermerk, Redline oder Mandantenübersetzung. |
| `workflow-rechtsquellen-livecheck` | Rechtsquellen-Livecheck im Plugin ki-governance: zwingt vor tragenden Aussagen zum aktuellen Quellencheck bei Gesetzen, Behörden, Gerichten und Formularen. |
| `workflow-redteam-qualitygate` | Red-Team Qualitygate im Plugin ki-governance: prüft das Ergebnis auf Halluzinationen, Fristenfehler, Zuständigkeit, Quellen, Beweise und Ton. |
| `workflow-unterlagen-lueckenliste` | Unterlagen- und Lückenliste im Plugin ki-governance: erstellt eine präzise Nachforderungsliste statt allgemeiner Fragebögen. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
