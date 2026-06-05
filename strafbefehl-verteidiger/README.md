# Strafbefehl-Verteidiger

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`strafbefehl-verteidiger`) | [`strafbefehl-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/strafbefehl-verteidiger.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **LUMEN Studios GmbH — Insolvenz- und Wirtschaftsstrafverfahren** (`lumen-studios-insolvenz-strafverfahren`) | [Gesamt-PDF lesen](../testakten/lumen-studios-insolvenz-strafverfahren/gesamt-pdf/lumen-studios-insolvenz-strafverfahren_gesamt.pdf) | [`testakte-lumen-studios-insolvenz-strafverfahren.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-lumen-studios-insolvenz-strafverfahren.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein freistehender Strafbefehls-Assistent für Kanzleien: vom Fristnotruf über Akteneinsicht und Einspruch bis zur beschränkten Rechtsfolgenstrategie oder Hauptverhandlung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn Register, Kanzleisoftware, beA, E-Mail, Datenraum oder Aktenexport fehlen, arbeitet es mit manuellen Uploads oder mit einem klar gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `strafbefehl-kommandocenter` starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nicht raten lassen, sondern mit der passenden Vorlage nachfordern oder Simulation ausdrücklich aktivieren.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `strafbefehl-kommandocenter` - Strafbefehl-Kommandocenter
- `strafbefehl-aktenanlage` - Aktenanlage Strafbefehl
- `strafbefehl-fristen-einspruch` - Frist und Einspruch nach § 410 StPO
- `strafbefehl-akteneinsicht-147` - Akteneinsicht
- `strafbefehl-zulaessigkeit-407` - Zulässigkeit des Strafbefehls
- `strafbefehl-inhalt-409-pruefung` - Inhaltsprüfung nach § 409 StPO
- `strafbefehl-einspruch-beschraenkung` - Einspruch beschränken oder nicht
- `strafbefehl-wiedereinsetzung` - Wiedereinsetzung
- `strafbefehl-pflichtverteidiger` - Pflichtverteidigung
- `strafbefehl-polizeifilmerei-201-kug` - Film-, Foto- und Tonaufnahmen von Polizeieinsätzen
- `strafbefehl-tagessaetze-geldstrafe` - Tagessätze und Geldstrafe
- `strafbefehl-nebenfolgen-fahrerlaubnis` - Nebenfolgen
- `strafbefehl-beweis-und-einlassung` - Beweis und Einlassung
- `strafbefehl-zeugen-befragungsstrategie` - Zeugenbefragung
- `strafbefehl-hauptverhandlung-vorbereitung` - Hauptverhandlung vorbereiten
- `strafbefehl-abwesenheit-vertretung` - Abwesenheit und Vertretung
- `strafbefehl-einstellung-153-153a-170` - Einstellung und Verständigung
- `strafbefehl-deal-verstaendigung` - Gesprächsstrategie mit Gericht und Staatsanwaltschaft
- `strafbefehl-rechtsmittel-nach-urteil` - Rechtsmittel nach Urteil
- `strafbefehl-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `strafbefehl-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/strafbefehl-mandatskarte.md` - Strafbefehl-Mandatskarte
- `assets/templates/frist-einspruch-410.md` - Frist und Einspruch nach § 410 StPO
- `assets/templates/akteneinsicht-147.md` - Akteneinsicht nach § 147 StPO
- `assets/templates/strafbefehl-inhaltspruefung.md` - Inhaltsprüfung Strafbefehl
- `assets/templates/einspruch-unbeschraenkt.md` - Unbeschränkter Einspruch
- `assets/templates/einspruch-beschraenkt.md` - Beschränkter Einspruch
- `assets/templates/wiedereinsetzung.md` - Wiedereinsetzung
- `assets/templates/pflichtverteidiger-check.md` - Pflichtverteidiger-Check
- `assets/templates/tagessaetze.md` - Tagessatzprüfung
- `assets/templates/einlassungsstrategie.md` - Einlassungsstrategie
- `assets/templates/zeugen-fragenkatalog.md` - Zeugenfragen
- `assets/templates/hauptverhandlung-plan.md` - Hauptverhandlung
- `assets/templates/einstellung-153-153a.md` - Einstellung nach §§ 153, 153a StPO
- `assets/templates/nebenfolgen-fahrerlaubnis.md` - Nebenfolgen
- `assets/templates/rechtsmittel-nach-urteil.md` - Rechtsmittel nach Urteil
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `aktenanlage-fehlerkatalog` | Aktenanlage Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |
| `deal-beweislast-einspruch` | Deal Beweislast Einspruch: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `einstellung-153a-hauptverhandlung` | Einstellung 153a Hauptverhandlung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `einstellung-fahrerlaubnis` | Einstellung Fahrerlaubnis: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `nebenfolgen-fahrerlaubnis-strafbefehl` | Nebenfolgen Fahrerlaubnis Strafbefehl: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `nebenfolgen-strafbefehl-strafbefehls` | Nebenfolgen Strafbefehl Strafbefehls: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `pflichtverteidigung-quellenkarte` | Pflichtverteidigung Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `rechtsmittel-tagessaetze-geldstrafe` | Rechtsmittel Tagessaetze Geldstrafe: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `stbv-einspruch-strafbefehl-fahrerlaubnis` | Stbv Einspruch Strafbefehl Fahrerlaubnis: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `stbv-strafbefehl-abwesenheit-vertretung` | Stbv Strafbefehl Abwesenheit Vertretung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafbefehl-einlassung-deal-verstaendigung` | Einlassung Deal Verstaendigung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafbefehl-einspruch-aktenanlage` | Einspruch Aktenanlage: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafbefehl-mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation Redteam Qualitygate: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafbefehl-quality-gate-akteneinsicht` | Quality Gate Akteneinsicht: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafbefehl-verteidiger-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `strafbefehl-verteidiger-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `strafbefehl-verteidiger-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `strafbefehl-verteidiger-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `strafbefehl-verteidiger-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `strafbefehl-verteidiger-start-chronologie-fristen` | Start Chronologie Fristen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `strafbefehl-verteidiger-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `tagessaetze-verstaendigung-sonderfall` | Tagessaetze Verstaendigung Sonderfall: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verteidigung-wiedereinsetzung-zeugenstrategie` | Verteidigung Wiedereinsetzung Zeugenstrategie: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `zeugen-befragungsstrategie-strafbefehl` | Zeugen Befragungsstrategie Strafbefehl: bündelt 2 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
