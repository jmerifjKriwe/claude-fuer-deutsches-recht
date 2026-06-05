# VerkehrsOWi-Verteidiger

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`verkehrsowi-verteidiger`) | [`verkehrsowi-verteidiger.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/verkehrsowi-verteidiger.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Norderhof-Tannenmoor — Abstandsverstoß Section Control BAB 7 Bispingen, Bußgeld und Fahrverbot** (`verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof`) | [Gesamt-PDF lesen](../testakten/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof/gesamt-pdf/verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof_gesamt.pdf) | [`testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-verkehrsowi-abstand-section-control-bab-7-bispingen-bussgeld-und-fahrverbot-norderhof.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Ein freistehender Verteidigungsassistent für Verkehrsordnungswidrigkeiten: vom Anhörungsbogen über Einspruch, Akteneinsicht, Messakte und Punkte bis zur Amtsgerichtsverhandlung.

Dieses Plugin ist **vollständig freistehend**. Es erwartet keine anderen Plugins, keine externen Agenten und keine besonderen Repo-Dateien außerhalb seines eigenen Ordners. Wenn Register, Kanzleisoftware, beA, E-Mail, Datenraum oder Aktenexport fehlen, arbeitet es mit manuellen Uploads oder mit einem klar gekennzeichneten Simulationsmodus.

## Schnellstart

1. Plugin aktivieren oder die ZIP aus dem Release installieren.
2. Mit `verkehrsowi-kommandocenter` starten.
3. Frist, Zustellung, Aktenzeichen, vorhandene Unterlagen und Mandantenziel nennen.
4. Fehlende Unterlagen nicht raten lassen, sondern mit der passenden Vorlage nachfordern oder Simulation ausdrücklich aktivieren.
5. Vor Versand oder Termin immer das Qualitätstor laufen lassen.

## Enthaltene Skills

- `verkehrsowi-kommandocenter` - VerkehrsOWi-Kommandocenter
- `verkehrsowi-aktenanlage` - Aktenanlage und Dokumentenregister
- `verkehrsowi-anhoerung-bussgeldbescheid` - Anhörung und Bußgeldbescheid prüfen
- `verkehrsowi-fristen-einspruch` - Fristen und Einspruch
- `verkehrsowi-verjaehrung-zustellung` - Verjährung und Zustellung
- `verkehrsowi-akteneinsicht-messakte` - Akteneinsicht und Messakte
- `verkehrsowi-messverfahren-geschwindigkeit` - Geschwindigkeitsmessung
- `verkehrsowi-rotlicht-abstand-handy` - Rotlicht, Abstand und Handy
- `verkehrsowi-alkohol-drogen-24a` - Alkohol und Drogen nach § 24a StVG
- `verkehrsowi-fahreridentifizierung` - Fahreridentifizierung
- `verkehrsowi-punkte-fahrverbot-flensburg` - Punkte, Fahrverbot und Flensburg
- `verkehrsowi-haertefall-fahrverbot` - Härtefall beim Fahrverbot
- `verkehrsowi-beweisverwertung-standardisiert` - Beweisverwertung und Standardisierung
- `verkehrsowi-zeugen-polizei-strategie` - Zeugen- und Polizeibefragung
- `verkehrsowi-hauptverhandlung-amtsgericht` - Hauptverhandlung vor dem Amtsgericht
- `verkehrsowi-rechtsbeschwerde` - Rechtsbeschwerde
- `verkehrsowi-rechtsprechungsrecherche` - Rechtsprechungsrecherche
- `verkehrsowi-mandantenkommunikation` - Mandantenkommunikation
- `verkehrsowi-simulation-training` - Simulation und Training
- `verkehrsowi-quality-gate` - Qualitätstor

## Vorlagen

- `assets/templates/verkehrsowi-mandatskarte.md` - VerkehrsOWi-Mandatskarte
- `assets/templates/frist-und-verjaehrung.md` - Fristen- und Verjährungsblatt
- `assets/templates/anhoerungsbogen-check.md` - Anhörungsbogen-Check
- `assets/templates/bussgeldbescheid-pruefung.md` - Bußgeldbescheid-Prüfung
- `assets/templates/einspruch-owig-67.md` - Einspruch nach § 67 OWiG
- `assets/templates/akteneinsicht-messakte.md` - Akteneinsicht und Messakte
- `assets/templates/messverfahren-checkliste.md` - Messverfahren-Checkliste
- `assets/templates/fahreridentifizierung.md` - Fahreridentifizierung
- `assets/templates/punkte-fahrverbot-matrix.md` - Punkte- und Fahrverbotsmatrix
- `assets/templates/haertefall-fahrverbot.md` - Härtefallpaket Fahrverbot
- `assets/templates/zeugen-polizei-fragenkatalog.md` - Zeugen- und Polizeifragen
- `assets/templates/hauptverhandlung-amtsgericht.md` - Hauptverhandlung Amtsgericht
- `assets/templates/rechtsbeschwerde-check.md` - Rechtsbeschwerde-Check
- `assets/templates/rechtsprechungsrecherche.md` - Rechtsprechungsrecherche
- `assets/templates/mandantenanschreiben.md` - Mandantenanschreiben
- `assets/templates/quality-gate.md` - Qualitätstor

## Freistehende Leitplanken

- Keine stillen Verweise auf andere Plugins.
- Keine produktive Rechtsberatung ohne anwaltliche Prüfung.
- Keine echten Mandatsgeheimnisse in ungeprüfte Cloud- oder KI-Umgebungen.
- Keine erfundenen Fundstellen, Aktenzeichen oder Rechtsprechung.
- Fristen, Rechtsmittel, Aussageverhalten und Nebenfolgen werden sichtbar geprüft.
- Jede Ausgabe muss so gestaltet sein, dass eine Berufsträgerin oder ein Berufsträger sie sofort prüfen, kürzen, freigeben oder verwerfen kann.

## Arbeitsakte

Zum Arbeiten liegt die Akte unter `testakten/verkehrsowi-rotlicht-tempo`. Sie wird im Release als `testakte-verkehrsowi-rotlicht-tempo.zip` bereitgestellt und ist kein Bestandteil des Plugin-ZIPs.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `abstand-quellenkarte` | Abstand Quellenkarte: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `alkohol-drogen-beweisverwertung` | Alkohol Drogen Beweisverwertung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `amtsgericht-drogen-interessen-einspruch` | Amtsgericht Drogen Interessen Einspruch: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `anhoerung-verkehrsowi-einspruch-messverfahren` | Anhoerung Verkehrsowi Einspruch Messverfahren: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `fahrverbot-geschwindigkeit-handy` | Fahrverbot Geschwindigkeit Handy: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `hauptverhandlung-sonderfall-messakte-messung` | Hauptverhandlung Sonderfall Messakte Messung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `punkte-rotlicht-verkehrsowi` | Punkte Rotlicht Verkehrsowi: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `simulation-training-verjaehrung-zustellung` | Simulation Training Verjaehrung Zustellung: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkehrsowi-haertefall-fahrverbot` | Haertefall Fahrverbot: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkehrsowi-mandantenkommunikation-redteam-qualitygate` | Mandantenkommunikation Redteam Qualitygate: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkehrsowi-punkte-fahrverbot` | Punkte Fahrverbot: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkehrsowi-verteidiger-anschluss-routing` | Anschluss-Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `verkehrsowi-verteidiger-dokumente-intake` | Dokumentenintake: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verkehrsowi-verteidiger-einstieg-routing` | Einstieg und Routing: Einstieg und Routing; klärt Rolle, Ziel, Frist, Aktenlage und den passenden nächsten Fachpfad. |
| `verkehrsowi-verteidiger-output-waehlen` | Output wählen: prüft Normen, Belege, Risiken, Gegenargumente und erzeugt ein verwertbares Arbeitsergebnis. |
| `verkehrsowi-verteidiger-quellen-livecheck` | Rechtsquellen-Livecheck: Quellenprüfung; Normenstand, Rechtsprechung, Behördenpraxis und Zitierfähigkeit werden vor einer tragenden Aussage verifiziert. |
| `verkehrsowi-verteidiger-start-chronologie-fristen` | Start Chronologie Fristen: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `verkehrsowi-verteidiger-unterlagen-luecken` | Unterlagen und Lücken: sortiert Dokumente, erkennt Lücken, ordnet Beweiswert und formuliert gezielte Rückfragen. |
| `verteidiger-beweislast-verkehrsowi` | Beweislast Verkehrsowi: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vowi-akteneinsicht` | Vowi Akteneinsicht: bearbeitet den maßgeblichen Prüfpfad und erzeugt den nächsten belastbaren Output im Mandat. |
| `vowi-bussgeldbescheid-verkehrsowi-quality` | Vowi Bussgeldbescheid Verkehrsowi Quality: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vowi-handyverstoss-akteneinsicht-alkohol` | Vowi Handyverstoss Akteneinsicht Alkohol: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `vowi-tempomessverfahren-bussgeldbescheid` | Vowi Tempomessverfahren Bussgeldbescheid: bündelt 3 verwandte Prüffelder und erzeugt den nächsten belastbaren Output — nach Frist, Zuständigkeit, Beweislast und gewünschtem Ergebnis priorisiert. |
| `zeugenstrategie-fehlerkatalog` | Zeugenstrategie Fehlerkatalog: Fehlerbremse; prüft Fristen, Zuständigkeit, Beweislast, Quellen und taktische Risiken vor Abgabe oder Versand. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
