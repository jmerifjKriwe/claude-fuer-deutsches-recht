# Kanzlei-Builder-Hub

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`kanzlei-builder-hub`) | [`kanzlei-builder-hub.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/kanzlei-builder-hub.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Kanzleigründung Eckermann Friedrich Sandhof Rechtsanwaltsgesellschaft mbH — Aachen** (`kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen`) | [Gesamt-PDF lesen](../testakten/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen/gesamt-pdf/kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen_gesamt.pdf) | [`testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-kanzleigruendung-rechtsanwaltsgesellschaft-eckermann-friedrich-aachen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Community-Skills für Kanzleien: Entdecken, prüfen und installieren. Durchsucht GitHub-Registries (kanzlei-skills und weitere, die über `/kanzlei-builder-hub:verzeichnis-durchsuchen` ergänzt werden können), installiert und aktualisiert Skills automatisch (mit Diff-Review), und zeigt in anderen Kanzlei-Plugins verwandte Community-Skills an. Das Erstgespräch-Interview (`kanzlei-builder-hub-kaltstart-interview`) ist gleichzeitig der Starter-Pack-Empfehlungsassistent — es fragt nach Kanzleityp und Tätigkeitsschwerpunkt und empfiehlt passende Skills zur Installation.

**Jeder Community-Skill wird vor der Installation im Rohformat angezeigt, auf Prompt-Injection-Muster gescannt und gegen das Kanzlei-Skill-Design-Framework geprüft. Sicherheits- und Berufsrechtsprüfung (DSGVO, BRAO/BORA, Mandantengeheimnis) erfolgen vor jeder Installation. Der Hub hilft beim Finden und Bewerten — die Entscheidung, was vertraut wird, liegt beim Anwender.**

---

## Für wen ist dieser Hub

Für alle, die die anderen Kanzlei-Plugins nutzen. Dies ist der App-Store.

---

## Erster Start: Kaltstart-Interview

Das Interview fragt nach Kanzleityp, Rechtsgebiet, Teamgröße und technischer Vertrautheit. Es empfiehlt ein Starter-Paket passender Community-Skills und installiert die ausgewählten.

```
/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview
```

Die Konfiguration wird gespeichert unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` und bleibt bei Plugin-Updates erhalten.

---

## Sicherheits- und Datenschutzhaltung

Installierte Community-Skills laufen mit Zugriff auf Mandantendaten, Aktendateien und das Kanzlei-Playbook. Der Hub behandelt jede Installation und jedes Update als Vertrauensentscheidung.

### Vier Verteidigungsebenen

- **Positivliste (admin-kontrolliert):** `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/positivliste.yaml` legt fest, welche Registries, Publisher und MCP-Konnektoren Community-Skills nutzen dürfen. Der Modus `permissive` (Standard) warnt bei allem außerhalb der Liste; der Modus `restrictive` (empfohlen für Kanzlei- und Unternehmensdeployments) verweigert die Installation. Die Positivliste wird geprüft, bevor Drittanbieterinhalte geladen werden.
- **Rohquelle statt Zusammenfassung:** Der Installer zeigt den vollständigen SKILL.md-Rohtext — keine KI-Zusammenfassung — bevor irgendetwas geschrieben wird.
- **Heuristische Scans:** Installer und `skills-qualitaetspruefung` scannen den Skill auf Prompt-Injection-Muster (Override-/Authority-Claims, unerlaubte Lese-/Schreibzugriffe, externe URLs, verstecktes Unicode, Shell-Ausführung, Credential-Anfragen). Diese KI-Heuristik ist kein Sicherheitsaudit.
- **Menschliche Genehmigung, jedes Mal:** Nichts wird ohne frisch eingetipptes `ja` auf Disk geschrieben. Genehmigung wird nicht aus früheren Nachrichten abgeleitet.

### Berufsrechtliches Security-Review-Gate

**Vor jeder Community-Skill-Installation** prüft der Installer:

1. **Datenschutz (DSGVO/BDSG):** Werden personenbezogene Mandantendaten verarbeitet? Ist eine Auftragsverarbeitung nach Art. 28 DSGVO erforderlich? Existiert ein entsprechender AVV?
2. **Berufsrecht (BRAO/BORA):** Entspricht der Skill den Berufspflichten nach §§ 43 ff. BRAO und §§ 2 ff. BORA? Wird die anwaltliche Unabhängigkeit gewahrt?
3. **Mandantengeheimnis:** Könnten Mandantendaten den vertraulichen Bereich verlassen (§ 43a Abs. 2 BRAO, § 203 StGB)? Ist sichergestellt, dass keine Daten unverschlüsselt übertragen oder bei Drittanbietern gespeichert werden?
4. **Technisch-organisatorische Maßnahmen (TOM):** Wurde vor dem Einsatz geprüft, ob eine TOM nach Art. 25, 32 DSGVO erforderlich ist? Dokumentation in der Verfahrensübersicht empfohlen.

Updates verwenden dieselbe Haltung: Der Auto-Updater pinnt auf Commit-SHAs (keine veränderbaren Tags), zeigt den vollständigen Diff inklusive Hooks und MCP-Änderungen und erfordert explizite Genehmigung pro Update.

Bei Problemen nach der Installation: `/kanzlei-builder-hub:deaktivieren [skill]` deaktiviert den Skill ohne Dateientfernung; `/kanzlei-builder-hub:deinstallieren [skill]` entfernt ihn vollständig. Beide Befehle sind auf Community-Skills beschränkt, die über diesen Hub installiert wurden — Erstanbieter-Plugin-Skills sind geschützt.

---

## Voraussetzungen

- Slack-Benachrichtigungen des Registry-Sync-Agenten erfordern einen konfigurierten Slack-MCP-Server. Ohne diesen schreibt der Agent seinen Digest in eine Datei.
- Die Standard-Registry-Liste in `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` wird leer ausgeliefert (außer `kanzlei-skills`). Weitere Registries können über `/kanzlei-builder-hub:verzeichnis-durchsuchen` oder durch direktes Bearbeiten von `CLAUDE.md` hinzugefügt werden.

---

## Befehle

| Befehl | Funktion |
|---|---|
| `/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview` | Kanzleiprofil erstellen + Starter-Paket empfehlen |
| `/kanzlei-builder-hub:verzeichnis-durchsuchen [Suchbegriff]` | Beobachtete Registries nach Skills durchsuchen |
| `/kanzlei-builder-hub:skill-installierer [skill]` | Community-Skill installieren (mit Security- und Berufsrechtsprüfung) |
| `/kanzlei-builder-hub:automatischer-aktualisierer` | Updates für installierte Skills prüfen (mit Diff-Review) |
| `/kanzlei-builder-hub:verwandte-skills-vorschlag` | Verwandte Skills basierend auf aktueller Tätigkeit empfehlen |
| `/kanzlei-builder-hub:skills-qualitaetspruefung [skill]` | Skill gegen das Kanzlei-Skill-Design-Framework prüfen (inkl. Zitierweise und Methodik) |
| `/kanzlei-builder-hub:kanzlei-builder-hub-anpassen` | Kanzleiprofil und Einstellungen anpassen |
| `/kanzlei-builder-hub:deaktivieren [skill]` | Installierten Community-Skill deaktivieren (Dateien bleiben erhalten) |
| `/kanzlei-builder-hub:deinstallieren [skill]` | Community-Skill vollständig entfernen |

---

## Skills im Überblick

| Skill | Zweck |
|---|---|
| **kaltstart-interview** | Kanzleiprofil → Starter-Paket |
| **verzeichnis-durchsuchen** | Registries nach Skills durchsuchen |
| **skill-installierer** | Positivliste-Gate, Abruf, Rohtext-Anzeige, DSGVO/BRAO-Prüfung, QA, Installation |
| **uninstall** | Community-Skill deinstallieren (Erstanbieter-Plugin-Skills sind gesperrt) |
| **disable** | Community-Skill ohne Dateilöschung deaktivieren; später wieder aktivierbar |
| **skill-verwalter** | Referenz: Detaillierte Deinstallations-, Deaktivierungs- und Reaktivierungsworkflows |
| **skills-qualitaetspruefung** | Skill gegen das Kanzlei-Skill-Design-Framework prüfen — Design, Fehlerquellen, Trust-Surface, Zitierweise, Methodik |
| **automatischer-aktualisierer** | Updates prüfen; Diff und Trust-Review anzeigen; Anwendung nur nach expliziter Genehmigung |
| **verwandte-skills-vorschlag** | Verwandte Community-Skills nach einer Aufgabe empfehlen |
| **anpassen** | Kanzleiprofil, Positivliste, Registry-Watchlist und Aktualisierungseinstellungen anpassen |
| **playbook-aus-eigenen-daten** | Aus E-Mails, Mandantenkorrespondenz und eigenen Dokumenten ein wiederverwendbares Kanzlei-Spielbuch destillieren (DSGVO/BRAO-konforme Pseudonymisierung) |
| **fundstellenglattzieher** | Juristische Fundstellen im Text gegen die hauseigene Zitierweise prüfen und vereinheitlichen (Heftnummern, `S.`-Zusätze, Bearbeiter, Auflage, Aufsatztitel-Entfall, `vgl.`-Floskeln, Abkürzungen) |

---

## Interaktive Befehle vs. geplante Agenten

Die obigen Befehle werden bei Aufruf ausgeführt — für die aktive Mandatsarbeit. Die folgenden Agenten laufen planmäßig im Hintergrund:

| Agent | Was er beobachtet | Standard-Kadenz |
|---|---|---|
| **verzeichnis-synchronisierung** | Beobachtete Registries auf neue und aktualisierte Skills; sendet Benachrichtigungen gemäß Einstellungen | Wöchentlich |

---

## Beobachtete Registries (Standard)

Die Standard-Positivliste enthält von uns geprüfte Community-Registries. Eigene Registries können über `references/positivliste-standard.yaml` im Repo oder über die persönliche Positivliste unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/positivliste.yaml` hinzugefügt, entfernt oder zwischen den Modi gewechselt werden.

- **kanzlei-skills** — Skills für deutsche Kanzleien und Rechtsabteilungen — Kanzlei-Community auf GitHub

---

## Wie der Hub dazulernt

Das Kanzleiprofil unter `~/.claude/plugins/config/claude-fuer-deutsches-recht/kanzlei-builder-hub/CLAUDE.md` ist nicht statisch — es verbessert sich mit der Nutzung. Der Hub liest es bei jedem `/kanzlei-builder-hub:verzeichnis-durchsuchen`- und `/kanzlei-builder-hub:verwandte-skills-vorschlag`-Aufruf neu, sodass Änderungen an Kanzleityp, Rechtsgebiet oder beobachteten Registries künftige Empfehlungen schärfen. Die Datei kann direkt bearbeitet oder mit `/kanzlei-builder-hub:kanzlei-builder-hub-kaltstart-interview --redo` neu durchgeführt werden.

---

## Hinweise

- Community-Skills werden vor der Installation gelesen. Der **Rohtext** der SKILL.md wird angezeigt — keine Zusammenfassung — bevor etwas akzeptiert wird.
- Auto-Update ist standardmäßig deaktiviert. Pro Skill aktivierbar, wenn die Quelle vertrauenswürdig ist.
- Der `verwandte-skills-vorschlag` läuft innerhalb anderer Plugins: Während einer Aufgabe prüft er, ob die Community etwas Passendes anbietet.
- **Kanzlei-/Unternehmensdeployments:** `mode: restrictive` in `positivliste.yaml` setzen und `registries`, `publishers` und `connectors` befüllen. Im Restrictive-Modus verweigert der Installer das Abrufen, Analysieren und Installieren von allem aus nicht gelisteten Quellen.
- **Datenschutz-Hinweis:** Für jede KI-gestützte Verarbeitung von Mandantendaten empfiehlt sich eine Datenschutz-Folgenabschätzung (Art. 35 DSGVO) sowie die Überprüfung, ob eine Auftragsverarbeitung (Art. 28 DSGVO) vorliegt. Installierte Skills sind in der Verfahrensübersicht nach Art. 30 DSGVO zu dokumentieren.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 27 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `community-leistungsmatrix-fristennotiz` | Community Leistungsmatrix Fristennotiz: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `deployment-eigenen-einsteiger` | Deployment Eigenen Einsteiger: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `findet-gate-installiert` | Findet Gate Installiert: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `grosskanzlei-rollout-thema-prozesse-abbilden` | Grosskanzlei Rollout Thema Prozesse Abbilden: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kanzlei-builder-hub-anschluss-router` | Anschluss Router: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kanzlei-builder-hub-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `kanzlei-builder-hub-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `kanzlei-builder-hub-fristen-risikoampel-mandantenkommunikation` | Fristen Risikoampel Mandantenkommunikation: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `kanzlei-builder-hub-kaltstart-interview` | Kaltstart-Interview für den Kanzlei-Builder-Hub: Kanzleiprofil, Rechtsgebiete, gewuenschte Plugins. Normen: technisch/intern. Prüfraster: Rechtsgebietsabdeckung, Mandantenstruktur, Technikvoraussetzungen. Output: Kanzlei-Profil-Konfigura... |
| `kanzlei-builder-hub-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `kanzlei-builder-hub-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `kanzlei-builder-hub-rechtsquellen` | Rechtsquellen: Quellenprüfung; Compliance-Dokumentation und Aktenvermerk: Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `kanzlei-builder-hub-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `kanzlei-fundstellencheck-zitate-links` | Normen- und Rechtsprechungszitate in Schriftsätzen, Memos und Skills vereinheitlichen. Setzt die Zitierweise v4.1 durch: keine BeckRS-, juris-, Kommentar- oder Aufsatz-Blindzitate; Rechtsprechung nur mit Datum, Aktenzeichen und verifizie... |
| `kanzlei-quellenkarte` | Kanzlei Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `kanzleiumgebung-khub-sonderfall-livecheck` | Kanzleiumgebung Khub Sonderfall Livecheck: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `khub-kanzlei-coi-onboarding-bauleiter` | Khub Kanzlei COI Onboarding Bauleiter: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `khub-mandantenkonferenz-paralegal-rollen` | Khub Mandantenkonferenz Paralegal Rollen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `playbook-aus-eigenen-daten` | Kanzleieigenes Playbook aus vorhandenen Musterdokumenten und Vorlagen automatisch erstellen. Normen: technisch/intern, BRAO. Prüfraster: Dokumentenqualitaet, Kategorisierung, Normverankerung. Output: Kanzlei-Playbook aus eigenen Daten. A... |
| `playbook-qualitaetspruefung-beweislast-review` | Playbook Qualitaetspruefung Beweislast Review: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `qa-kanzleiweit-templating-praxis-verwalter` | QA Kanzleiweit Templating Praxis Verwalter: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `qualitaetspruefung-builder-daten-red` | Qualitaetspruefung Builder Daten RED: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `security-installation` | Security Installation: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `skill-installierer` | Neue Skills in der KI-Anwaltskanzlei installieren: Verfuegbarkeitscheck, Abhaengigkeiten, Konfiguration. Normen: technisch/intern. Prüfraster: Kompatibilitaet, Abhaengigkeitsprüfung, Testlauf. Output: Installationsprotokoll neuer Skill.... |
| `uebersicht-einsteiger-deaktivieren` | Uebersicht Einsteiger Deaktivieren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verwandte-skills-vorschlag` | Verwandte Skills zu einem Mandat oder Rechtsproblem vorschlagen: Ergaenzungsempfehlungen. Normen: technisch/intern. Prüfraster: Rechtsgebiet, Verfahrensphase, Mandantentyp. Output: Vorschlagsliste verwandter Skills. Abgrenzung: nicht Kom... |
| `verzeichnis-durchsuchen` | Skill-Verzeichnis nach Rechtsgebiet, Norm oder Mandantentyp durchsuchen. Normen: technisch/intern. Prüfraster: Suchbegriff, Kategoriefilter, Ergebnispriorisierung. Output: Suchergebnisliste Skills. Abgrenzung: nicht Skill-Installation od... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
