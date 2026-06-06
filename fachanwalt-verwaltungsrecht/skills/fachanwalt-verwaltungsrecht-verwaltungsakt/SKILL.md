---
name: fachanwalt-verwaltungsrecht-verwaltungsakt
description: "Verwaltungsakt im Plugin Fachanwalt Verwaltungsrecht: prüft konkret Beamten-Disziplinarverfahren führen oder verteidigen, Verwaltungsakt, Rechtsbehelf und Vorverfahren, VwGO. Liefert priorisierten Output mit Norm-Pinpoints, Risikoampel und nächstem Schritt."
---

# Verwaltungsakt

## Arbeitsbereich

**Verwaltungsakt** ordnet den Fall über die tragenden Prüffelder: Beamten-Disziplinarverfahren führen oder verteidigen, Verwaltungsakt, Rechtsbehelf und Vorverfahren. Zuerst wird das Feld bestimmt, das die Akte wirklich trägt; ergänzende Felder kommen nur hinzu, wenn sie dieselbe Frist, Zuständigkeit, Beweislast oder denselben Output berühren.
## Prüffelder

| Prüffeld | Fokus |
| --- | --- |
| `fachanwalt-verwaltungsrecht-beamten-disziplinarverfahren` | Beamten-Disziplinarverfahren führen oder verteidigen: Beamter hat Dienstvergehen begangen oder ist Dienstherr bei Einleitung Disziplinarverfahren. Normen: BBG/BeamtStG, Bundesdisziplinargesetz BDG, Landesdisziplinargesetze. Prüfraster: Dienstvergehen-Tatbestand, Disziplinarmassnahmen (Verweis bis Entfernung aus Beamtenverhältnis), Anhoerung, VG-Klage. Output Anhoerungsschrift, Klageschrift, Verteidigungskonzept. Abgrenzung: Beamtenrecht materiell (Befoerderung, Besoldung) siehe mandat-triage-verwaltungsrecht; Anfechtungsklage allgemein siehe fachanwalt-verwaltungsrecht-anfechtungsklage. |
| `spezial-verwaltungsakt-rechtsbehelf-vorverfahren` | Verwaltungsakt, Rechtsbehelf und Vorverfahren: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output. |
| `spezial-vwgo-fristen-form-und-zustaendigkeit` | VwGO: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt verwaltungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung. |

## Arbeitsweg

- Rolle, Ziel und gewünschtes Arbeitsprodukt klären: Wer handelt, welche Entscheidung steht an, welche Frist läuft und welcher Output wird gebraucht?
- Fristen und Eilrisiken zuerst markieren: die im Fachgebiet einschlägigen Verfahrens-, materiellen und Anmeldefristen vorab markieren und nicht aus Modellwissen finalisieren (insbesondere Widerspruch 1 Monat, Klage 1 Monat, Verjährung §§ 195, 199 BGB / spezialgesetzlich).
- Tragende Normen verifizieren: VwGO; VwVfG — Fundstellen über gesetze-im-internet.de, dejure.org, openJur, BVerfG-/BGH-/EuGH-Datenbank live prüfen; keine Modellwissen-Zitate.
- Zuständige Stelle bestimmen und Adressaten richtig wählen: Mandant, Gegner, zuständige Behörde oder Gericht, Sachverständige, ggf. EU-/internationale Stelle (siehe Skill-Detail).
- Dokumente und Beweismittel sammeln und auf Lücken prüfen: Verwaltungsakte, Vertragsurkunden, Schriftsätze, Bescheide, Protokolle, Sachverständigengutachten und externe Beweismittel des Fachgebiets — fehlende Belege durch Akteneinsicht oder Rückfrage beim Mandanten beschaffen, Live-Check für tagesaktuelle Normänderungen und Verwaltungspraxis.
## Prüffelder im Detail

## 1. `fachanwalt-verwaltungsrecht-beamten-disziplinarverfahren`

**Fokus:** Beamten-Disziplinarverfahren führen oder verteidigen: Beamter hat Dienstvergehen begangen oder ist Dienstherr bei Einleitung Disziplinarverfahren. Normen: BBG/BeamtStG, Bundesdisziplinargesetz BDG, Landesdisziplinargesetze. Prüfraster: Dienstvergehen-Tatbestand, Disziplinarmassnahmen (Verweis bis Entfernung aus Beamtenverhältnis), Anhoerung, VG-Klage. Output Anhoerungsschrift, Klageschrift, Verteidigungskonzept. Abgrenzung: Beamtenrecht materiell (Befoerderung, Besoldung) siehe mandat-triage-verwaltungsrecht; Anfechtungsklage allgemein siehe fachanwalt-verwaltungsrecht-anfechtungsklage.

# Beamten-Disziplinarverfahren

## Zweck

Verteidigung Beamten bei Disziplinar-Vorwurf.

## 1) Rechtsgrundlagen

- BBG (Bundesbeamten-Gesetz)
- BeamtStG (Beamtenstatusgesetz)
- Bundes-DG / Landes-DG (Disziplinargesetze)

## 2) Dienstpflicht-Verletzungen

### Beispiele

- Verletzung Verschwiegenheits-Pflicht
- Verspaetete Diensterscheinung
- Drogen-Konsum
- Privat-Strafraten mit Bezug
- Beleidigungen
- Unerlaubte Nebentaetigkeit

### Schwere

- Leichter Verstoß: Verweis
- Mittel: Geldbuße / Kürzung Bezüge
- Schwer: Aberkennung Ruhegehalt
- Sehr schwer: Entfernung aus Dienst

## 3) Disziplinar-Maßnahmen

| Maßnahme | Pflicht-Voraussetzung |
|---|---|
| Verweis | leichter Verstoß |
| Geldbuße | bis 1 Monatsbezüge |
| Kürzung Bezüge | befristet bis 5 Jahre |
| Zurueckstufung | dauerhafte Demotion |
| Entfernung Dienst | schwere Verstöße |
| Aberkennung Ruhegehalt | bei Ruhe-Beamten |

## 4) Verfahren

### Schritt 1 — Voruntersuchung

- Dienstvorgesetzter prüft Vorwurf
- Anhörung Beamter

### Schritt 2 — Förmliches Disziplinarverfahren

- Eröffnung durch Dienstherr
- Ermittlungsfuhrer
- Beweisaufnahme

### Schritt 3 — Disziplinarmaßnahme

- Bescheid mit Begründung
- Bei schwerer Maßnahme: Klage VG Pflicht

### Schritt 4 — Klage VG

- Disziplinargericht (im VG-Gefuege)
- Disziplinarklage Dienstherr
- Vollumfaengliche Prüfung

## 5) Beamten-Strategie

### Sofort-Maßnahmen

- Schweige-Recht (in Disziplinar-Verfahren begrenzt)
- Anwalt einschalten
- Pflicht-Aussage nur zu Sachen, die nicht selbst-belasten

### Vorbereitung

- Akten-Einsicht
- Gegen-Beweise
- Milderungs-Faktoren (Krankheit, Belastung)

### Vergleichs-Möglichkeit

- Einstellung gegen Auflage
- Anwendung Mildere-Maßnahme

## 6) Schwerwiegende Folgen

### Bei Aberkennung Ruhegehalt

- Verlust Pensionsanspruch
- Sozialer Sturz

### Bei Entfernung aus Dienst

- Wegfall Versorgung
- Verlust Status
- Schwere persönliche Folge

## 7) Strafverfahren parallel

### Bei Straf-Tat

- Strafverteidigung im Vorder-Grund
- Disziplinar typisch erst nach Strafurteil
- Bindung Disziplinar-Verfahren an Strafurteil § 22 BDG

### Praxis

- Strafmilderung -> Disziplinar-Erleichterung
- Bei Freispruch: Disziplinar oft eingestellt

## 8) Workflow

### Phase 1 — Erstgespräch

- Vorwurfs-Aufnahme
- Verteidigungs-Strategie

### Phase 2 — Anhörung

- Schriftliche Stellungnahme
- Beweise

### Phase 3 — Bei Bescheid

- Klage Disziplinar-VG
- Frist meist 1 Monat

### Phase 4 — Verhandlung

- Vor Disziplinarkammer
- Beweisaufnahme
- Urteil

## 9) Honorar

- Anwaltsgebuehren nach RVG
- Bei Erfolg: Erstattung durch Dienstherr (begrenzt)
- Beamtenbund-Mitgliedschaft typisch hilfreich

## 10) Typische Fehler

1. **Unüberlegte Aussage** in Voruntersuchung
2. **Klage-Frist 1 Monat verpasst**
3. **Milderungs-Faktoren nicht dargelegt**
4. **Strafverfahren ohne Disziplinar-Beratung**

## 11) BVerwG-Linien

- BVerwG laufende Disziplinar-Rspr.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Aktuelle BVerwG-Leitentscheidungen

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Quellenregel

Quellenregel: Keine Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen; Literatur nur mit Nutzerquelle oder lizenziertem Live-Zugriff.
## Anschluss

- `fachanwalt-verwaltungsrecht-orientierung` — Triage
- `fachanwalt-strafrecht-orientierung` — bei parallelem Strafverfahren
- `widerspruch-oder-klage-erstpruefung` — bei VG-Triage

## 2. `spezial-verwaltungsakt-rechtsbehelf-vorverfahren`

**Fokus:** Verwaltungsakt, Rechtsbehelf und Vorverfahren: führt schnell durch Sachverhalt, Rechtsgrundlagen, Belege, Risiken und erzeugt einen verwertbaren nächsten Output.

# Verwaltungsakt, Rechtsbehelf und Vorverfahren

## Aufgabe
Dieser Skill ersetzt einen zu groben Spezial-Slot durch einen konkreten Fachim Plugin `fachanwalt-verwaltungsrecht`. Kontext des Plugins: Plugin Fachanwalt für Verwaltungsrecht. VwGO VwVfG. Anfechtungs- und Verpflichtungsklage Eilrechtsschutz § 80 Abs 5 VwGO einstweilige Anordnung Normenkontrolle Polizei- und Ordnungsrecht. Schnittstelle Plugin kanzlei-allgemein.

Er arbeitet nicht lexikalisch, sondern fallbezogen: Er trennt zuerst Rollen, Ziel, Fristen, Zuständigkeiten und Belege, prüft dann die fachlichen Weichen und liefert ein Ergebnis, mit dem weitergearbeitet werden kann.

## Einstieg
Wenn Material vorliegt, nutze es zuerst. Frage nur nach, was für die nächste Entscheidung fehlt:

1. Wer handelt in welcher Rolle und gegen wen?
2. Welches praktische Ziel soll erreicht werden?
3. Welche Fristen, Termine, Zustellungen, Schwellenwerte oder Sanktionen stehen im Raum?
4. Welche Unterlagen, Daten, Registerauszüge, Bescheide, Verträge, Screenshots oder sonstigen Belege liegen vor?
5. Soll der Output intern, für Mandantschaft, Behörde, Gericht, Gegnerseite oder Gremium formuliert werden?

## Arbeitsworkflow
1. **Sortieren:** Sachverhalt, Dokumente und offene Punkte in eine knappe Fallmatrix bringen.
2. **Rechtsrahmen:** Einschlägige Normen, Zuständigkeiten, Verfahren, Fristen und formelle Anforderungen live prüfen, soweit Aktualität tragend ist.
3. **Materielle Weichen:** Die Kernfragen zu **Verwaltungsakt, Rechtsbehelf und Vorverfahren** mit Tatbestandsmerkmalen, Belegen, Gegenargumenten und typischen Praxisfehlern abarbeiten.
4. **Risikoampel:** Ergebnis in Grün/Gelb/Rot mit Begründung, Unsicherheiten und Beweisbedarf einordnen.
5. **Anschluss:** Passende weitere Skills desselben Plugins vorschlagen, wenn Spezialprüfung, Schriftsatz, Tabelle, Brief oder Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- Kurzbild in fünf Sätzen: Lage, Ziel, Frist, Risiko, nächster Schritt.
- Prüfmatrix mit Punkt, Norm/Quelle, Tatsachen, Beleg, Bewertung, To-do.
- Konkreter Textbaustein oder Arbeitsprodukt passend zur Lage: Memo, Mandantenbrief, Behörden-/Gerichtsschreiben, Checkliste, Tabelle oder Verhandlungsagenda.
- Keine Scheingenauigkeit: Annahmen, Lücken und Live-Check-Bedarf offen markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwenden, wenn die Nutzerin oder der Nutzer den Text selbst bereitstellt; dann nicht als frei verifizierte Quelle ausgeben.

## 3. `spezial-vwgo-fristen-form-und-zustaendigkeit`

**Fokus:** VwGO: Fristen, Form, Zuständigkeit und Rechtsweg im Plugin fachanwalt verwaltungsrecht; schärft Rollen, Belege, Fachnormen, Risiken, Gegenargumente und nächsten verwertbaren Schritt statt austauschbarer Standardprüfung.

# VwGO: Fristen, Form, Zuständigkeit und Rechtsweg

## Spezialwissen: VwGO: Fristen, Form, Zuständigkeit und Rechtsweg
- **Normen-/Quellenanker:** VwGO, VwVfG.

## Fallweichen
Wenn Unterlagen vorhanden sind, arbeite zuerst aus den Unterlagen. Stelle nur Rückfragen, die die nächste Weiche verändern:

1. Welche Rolle hat die fragende Person und wer ist Gegenüber?
2. Welches konkrete Ziel soll erreicht oder verhindert werden?
3. Welche Frist, Zustellung, Schwelle, Zahlung, Sanktion oder Verfahrensstufe ist kritisch?
4. Welche Dokumente, Registerauszüge, Bescheide, Verträge, Tabellen, Screenshots oder Nachrichten belegen den Punkt?
5. Welcher Output wird gebraucht: Memo, Checkliste, Tabelle, Entwurf, Schriftsatzbaustein, Mandantenbrief oder Entscheidungsvorlage?

## Arbeitsworkflow
1. **Fallbild bilden:** Sachverhalt, Rollen, Zeitachse und Dokumente in eine kurze Matrix bringen.
2. **Rechtsrahmen setzen:** Normen, Zuständigkeiten, Fristen, Formfragen und Verfahrensstand zum Themenfeld **VwGO** prüfen.
3. **Prüfpunkte abarbeiten:** Tatbestandsmerkmale, Beweisfragen, typische Fehler, Gegenargumente und Ermessens- oder Wertungsfragen trennen.
4. **Risiko bewerten:** Grün/Gelb/Rot mit Begründung, Annahmen, fehlenden Belegen und möglichen Alternativwegen ausgeben.
5. **Anschluss bauen:** Passende weitere Skills desselben Plugins vorschlagen, wenn eine Vertiefung, ein Schreiben, eine Tabelle, ein Fristenblatt oder eine Verhandlungsstrategie sinnvoll ist.

## Output-Standard
- **Kurzlage:** maximal fünf Sätze zu Ziel, Lage, Frist, Risiko und nächstem Schritt.
- **Prüfmatrix:** Punkt, Norm/Quelle, Tatsache, Beleg, Bewertung, To-do.
- **Arbeitsprodukt:** direkt nutzbarer Entwurf oder Baustein in der passenden Tonalität.
- **Qualitätsgate:** keine Scheingenauigkeit; Lücken, Annahmen und Live-Check-Bedarf ausdrücklich markieren.

## Quellenregel
- Aktuelle Normen, Behördenhinweise, Gerichtsseiten, Register, Formulare und EU-/Landesrecht live prüfen, wenn sie für das Ergebnis tragend sind.
- Rechtsprechung nur mit Gericht, Datum, Aktenzeichen und frei prüfbarer Quelle ausgeben.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate aus Modellwissen.
- Paywall-Literatur nur verwerten, wenn sie von der Nutzerin oder dem Nutzer als Text bereitgestellt wurde; dann nicht als frei verifizierte Quelle ausgeben.
