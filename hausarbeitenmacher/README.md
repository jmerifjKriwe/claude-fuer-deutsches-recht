# hausarbeitenmacher — Didaktisches Plugin für juristische Hausarbeiten und Seminararbeiten

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`hausarbeitenmacher`) | [`hausarbeitenmacher.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/hausarbeitenmacher.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Hausarbeit BGB Übung Fortgeschrittene — Pohlmann / Leipzig / SS 26** (`hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung`) | [Gesamt-PDF lesen](../testakten/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung/gesamt-pdf/hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung_gesamt.pdf) | [`testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hausarbeit-bgb-uebung-fortgeschrittene-pohlmann-leipzig-ss26-vertragsbruch-aufrechnung.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Plugin für Studierende der Rechtswissenschaft, das durch das Erstellen einer **Hausarbeit oder Seminararbeit lernfördernd** hindurchführt. Es liefert **keine fertigen Lösungen**, sondern stellt Fragen, gibt Strukturen, Methoden-Hinweise und Zitierweise — Du subsumierst selbst.

## Installation

1. Claude Code oder Claude Desktop/Cowork öffnen.
2. **Customize Plugins** bzw. **Personal plugins** wählen.
3. **Install from .zip** und `hausarbeitenmacher.zip` hochladen.
4. Mit einer konkreten Aufgabenstellung starten, zum Beispiel: `Hilf mir bei einer Hausarbeit. Sachverhalt folgt.`

Alternativ via Marketplace:

```
/plugin marketplace add Klotzkette/claude-fuer-deutsches-recht
/plugin install hausarbeitenmacher@claude-fuer-deutsches-recht
```

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json` und `skills/` enthalten.

## Mandatsperspektive

**Du als Studierende oder Studierender.** Du gibst Deine Aufgabenstellung ein und gehst Schritt für Schritt durch die Lösung. Das Plugin

- fragt zu Beginn nach der **Lehrkraft** und entwickelt eine Adressaten-Strategie ohne Schleimerei,
- unterscheidet **Hausarbeit (Korrekturassistent)** und **Seminararbeit (persönliche Lektüre + Vortrag)**,
- analysiert Deine Aufgabenstellung,
- sortiert Dich in das passende Fachgebiet (Zivilrecht, Öffentliches Recht, Strafrecht — oder mehrere),
- gibt Dir die Prüfungs-Schemata,
- erklärt Dir den Gutachtenstil (Hausarbeit) bzw. den wissenschaftlichen Aufsatz-Stil (Seminararbeit),
- führt Dich durch jede Subsumtion oder jeden Erörterungs-Schritt,
- zeigt Dir typische Fehler und
- prüft am Ende, ob Du das Lernziel erreicht hast.

**Es löst die Arbeit nicht für Dich. Es lehrt Dich, sie zu lösen.**

## Adressaten-Strategie statt Schleimerei

Zu Beginn fragt das Plugin: **Von welchem Lehrstuhl stammt die Aufgabe?**

Wenn Du die Lehrkraft nennst, schlägt das Plugin eine kurze Recherche zu deren Auffassung vor (Publikationen, Kommentar-Bearbeitungen, Aufsätze). Dann kommt die ehrliche Komplizen-Frage:

> *Wollen wir nach dem Munde reden — oder die Aufgabe sauber lösen, auch wenn wir der Lehrkraft widersprechen müssen?*

Das Plugin empfiehlt **die saubere Lösung**. Selbst wenn Du der Lehrkraft am Ende widersprichst — eine begründete, mit guten Argumenten gestützte eigene Auffassung wird respektiert. **Schleim ist erkennbar und macht keine Karriere. Argumente machen Karriere.**

## Aufbau

Der Lebenszyklus einer Arbeit läuft in fünf Phasen:

```
Phase 0 — Adressaten-Klärung (Stunde 1)
  └─ Lehrkraft? → Hausarbeit oder Seminararbeit?
     → Adressaten-Strategie (kein Schleim, aber kluge Argumentation)

Phase A — Auftakt und Routing (Tag 1-3)
  └─ Aufgabenstellung erfassen → Fachgebiet identifizieren
     → Bearbeitungs-Plan festlegen

Phase B — Methodisches Fundament (Tag 4-10)
  └─ Gutachtenstil → Methodenlehre Auslegung
     → Gliederung mit Tiefenstruktur → Zitierweise
     → Quellenrecherche

Phase C — Fachgebiet-spezifische Prüfungsschemata (Tag 11-30)
  └─ Zivilrecht: Anspruchsgrundlagen-Reihenfolge
     ÖR: Statthaftigkeit → Zulässigkeit → Begründetheit
     Strafrecht: Tatbestand → Rechtswidrigkeit → Schuld
     Europarecht: Anwendungs-Vorrang Vorabentscheidung
     Verfassungsrecht: Grundrechts-Schema
     Rechtstheorie/-philosophie: Anbindung

Phase D — Schreiben, Reflektieren, Polieren (Tag 31-40)
  └─ Subsumtions-Übung → Meinungsstreit darstellen
     → Häufige Fehler vermeiden → Selbstkontrolle
     → Abgabe-Vorbereitung
     → Bei Seminararbeit: Vortrag und Disputation
```

## Enthaltene Skills (23)

### Phase 0 — Adressaten-Klärung (2 Skills)

| Slug | Beschreibung |
|---|---|
| `professor-erkennen-und-strategie` | Fangfrage Lehrkraft Kurz-Recherche Adressaten-Strategie ohne Schleim |
| `seminararbeit-modus` | Spezifika der Seminararbeit Forschungsfrage eigene These Vortrag Disputation |

### Phase A — Auftakt (3 Skills)

| Slug | Beschreibung |
|---|---|
| `aufgabenstellung-erfassen` | Falltext zerlegen Wesentliche/Unwesentliche unterscheiden Bearbeitungsvermerk verstehen |
| `fachgebiet-routing-zivil-oeffentlich-straf` | Welches Fachgebiet? Gemischte Konstellationen erkennen Reihenfolge bei Mix |
| `bearbeitungsplan-erstellen` | Zeitplan Stoff-Aufteilung Lern-Ziele für die Arbeit |

### Phase B — Methodisches Fundament (6 Skills)

| Slug | Beschreibung |
|---|---|
| `gutachtenstil-vs-urteilsstil` | Obersatz-Definition-Subsumtion-Ergebnis vs. begründungs-knapp Urteilsstil |
| `methodenlehre-auslegung` | Wortlaut-Systematik-Geschichte-Sinn-Zweck + verfassungs-/EU-konform |
| `gliederung-mit-tiefenstruktur` | A. B. C. → I. II. III. → 1. 2. 3. → a) b) c) — Tiefe richtig setzen |
| `zitierweise-jura-fundstellen` | Rspr. Kommentare Aufsätze BGH BVerfG amtliche/freie Quellen und lizenzierte Datenbanken nur bei vorhandenem Zugang |
| `quellenrecherche-rechtsprechung-literatur` | Bibliothek amtliche/freie Quellen und lizenzierte Datenbanken nur bei vorhandenem Zugang Google-Scholar Suchstrategie |
| `subsumtion-schritt-fuer-schritt` | Wie subsumiere ich richtig? Häufige Fehler |

### Phase C — Fachgebiet-Schemata (6 Skills)

| Slug | Beschreibung |
|---|---|
| `zivilrecht-anspruchsgrundlagen-pruefung` | V-C-G-D-D-B Reihenfolge BGB-Anspruch prüfen |
| `oeffentliches-recht-statthaft-zulaessig-begruendet` | VwGO §§ 40 42 47 113 Schemata Verwaltungsklage |
| `strafrecht-tatbestand-rechtswidrigkeit-schuld` | Schema 3-Stufen-Verbrechensaufbau |
| `verfassungsrecht-grundrechtspruefung` | Schutzbereich-Eingriff-verfassungsrechtliche Rechtfertigung |
| `europarecht-anwendbarkeit-vorrang-vorabentscheidung` | Art. 267 AEUV RL-Auslegung EuGH-Bezug |
| `rechtstheorie-rechtsphilosophie-anbindung` | Kelsen Hart Dworkin Radbruch Naturrecht Positivismus |

### Phase D — Schreiben und Reflektieren (4 Skills)

| Slug | Beschreibung |
|---|---|
| `meinungsstreit-darstellen` | h.M. — a.A. — eigene Stellungnahme strukturiert |
| `haeufige-fehler-vermeiden` | Top-20 typische Hausarbeit-Fehler |
| `selbstkontrolle-vor-abgabe` | Checkliste vor Abgabe Lernziel-Selbstprüfung |
| `behutsame-frech-wertschaetzende-rueckfragen` | Stil-Anleitung für das Plugin selbst: trocken-ketzerische Würze am Rande |

Plus der Master-Skill **`hausarbeit-workflow-start`** als Einstiegs-Schiene.

## Bedienungs-Hinweis

Das Plugin ist freistehend nutzbar und benötigt keine anderen Plugins. Für vertiefte methodische Fragen kann das Plugin `methodenlehre-buergerliches-recht` ergänzend geladen werden, für Lösungsschemata `jurastudium`, für die Zitierweise das Reference-Plugin `zitierweise-deutsches-recht`.

## Lern-Prinzip — Sokratische Methode

Das Plugin folgt der **sokratischen Methode**:

- Statt "Hier ist die Lösung" → "Welche Anspruchsgrundlage kommt zuerst in Betracht?"
- Statt "Subsumiere wie folgt" → "Welche Tatbestandsmerkmale müssen Sie prüfen?"
- Statt "Die h.M. sagt X" → "Welche Stimmen haben Sie gefunden? Wer argumentiert wie?"
- Statt "Schreibe diesen Absatz" → "Welche Struktur ist hier sinnvoll? Welche Definition brauchen Sie?"

Das Plugin liefert **Methoden, Schemata, Fragen, Quellen-Hinweise, Strukturen** — aber **niemals den Volltext einer Lösung**. Das Lernen erfolgt durch eigenständige Subsumtion oder eigenständige Erörterung.

## Dialog-Stil

Der Grundton des Plugins ist **sokratisch, gentle, ermutigend**. In Aufwärtsphasen erlaubt sich das Plugin gelegentlich — höchstens alle 5-7 Schritte — eine **behutsam-trockene, frech-wertschätzende Rückfrage**: ein leicht ironisches Staunen, eine alltagsphilosophische Beobachtung, eine selbstironische Wendung, eine scheinbar naive Nachfrage.

Beispiele für den Ton:

- *"Hmm. § 985 BGB als erste Anspruchsgrundlage. Mutig. Was hat denn der gute alte Vertrag Dir je angetan?"*
- *"Mir fällt auf, dass Du den Streit-Stand drei Mal anders zusammengefasst hast. Eine der drei Versionen ist vielleicht Deine eigene Stimme — kannst Du sie wiederfinden?"*
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**Niemals herablassend, niemals zynisch, niemals besserwisserisch.** Bei Frust oder Lebensbelastung der lernenden Person wechselt das Plugin sofort in den klassisch warm-fragenden Modus zurück.

→ Skill `behutsame-frech-wertschaetzende-rueckfragen` regelt diesen Stil detailliert.

## Bei Unsicherheit

Wenn die Aufgabenstellung mehrdeutig ist, frage zuerst die Lehrkraft. Wenn die Bibliothek nicht ausreicht, ist das Plugin keine Ersatz-Bibliothek. Wenn die Klausur in 14 Tagen ist, ist das Plugin keine Last-Minute-Lösung.

**Das Plugin ist Dein Lern-Begleiter, kein Spickzettel.**

## ⚠️ Vorsicht: hiermit bitte nicht mogeln im Studium

Das Plugin ist ein **Lern- und Trainingswerkzeug** für Studierende, Tutor/-innen und Lehrkräfte. Es ist ausdrücklich **nicht** dafür gedacht, irgendeinen vom Plugin generierten Text (Subsumtion, Gliederungs-Vorschlag, Argumentations-Skizze, Probe-Gutachten) **als eigene Leistung** in einer Hausarbeit, Seminararbeit, Klausur, Aktenklausur, mündlichen Prüfung oder im juristischen Vorbereitungsdienst einzureichen. Das wäre ein **Täuschungsversuch** im Sinne der jeweiligen Prüfungsordnung der Universitäten bzw. § 14 JAG NRW / § 12 JAPO Bayern / vergleichbarer Vorschriften der anderen Länder. Folge ist regelmäßig **Nichtbestehen, Aberkennung der Prüfung oder disziplinarrechtliche Konsequenzen**. Der erlaubte Lernweg: erst selbst denken und schreiben, dann mit dem Plugin gegenprüfen, hinterfragen und verbessern lassen.

## Verbotenes (Eigen-Einschränkung)

Das Plugin

- gibt **keinen** Arbeits-Volltext aus,
- löst **keine** konkreten Subsumtionen oder Erörterungen für Dich,
- liefert **keine** fertigen Gutachten- oder Aufsatz-Texte zum Kopieren,
- ersetzt **keine** Lehrkraft.

Das Plugin

- erklärt Methoden, Schemata, Strukturen,
- stellt Fragen und Hilfsfragen,
- verweist auf Literatur und Rechtsprechung,
- prüft Deine Reflexion,
- unterstützt Deine eigene Lösungs-Findung.

## Sprachform und Du-/Sie-Form

Die Skills sprechen Dich teils mit "Du", teils mit "Sie" an — je nach Sprach-Konvention des betreffenden Rechtsgebiets (BGH-Stil eher Sie, Skript-Stil eher Du). Eine bewusste Mischform.

## Zitierweise

Sämtliche Zitierweise-Vorgaben folgen `references/zitierweise.md` des übergeordneten Repositories `claude-fuer-deutsches-recht`. Plus: Hausarbeits- und Seminararbeits-spezifische Standards (z.B. Sigel-Verzeichnis, bei Seminararbeit erweiterte Literaturschau).

## Tipps für die Bearbeitung

1. **Plane Zeit ein**: Hausarbeiten und Seminararbeiten brauchen Wochen, nicht Stunden. Plane sechs Wochen für eine Anfänger-/Fortgeschrittenenübung, drei Monate für eine Examenshausarbeit oder Seminararbeit.

2. **Lies den Sachverhalt mindestens dreimal**: Erst Überblick, dann Detail, dann Skizze der Beteiligten/Akten. Bei Seminararbeit: das Thema mit verwandter Literatur einlesen, dann die eigene Forschungsfrage scharf machen.

3. **Bearbeitungs-Vermerk genau lesen**: Was wird geprüft (Gutachten/Hilfsgutachten)? Welcher Standpunkt (Antragsteller/Antragsgegner)?

4. **Anspruchsgrundlagen-Reihenfolge wahren**: Bei Zivilrecht V-C-G-D-D-B (Vertrag-c.i.c.-GoA-Dinglich-Delikt-Bereicherung).

5. **Methodenlehre einbeziehen**: Nicht nur subsumieren, sondern bei Streit auch auslegen.

6. **Quellen sortieren**: Rechtsprechung vor Literatur, neueste zuerst, Bearbeiter-Name beachten.

7. **Selbstkontrolle vor Abgabe**: Mindestens zwei Durchgänge — einmal inhaltlich, einmal formal.

8. **Bei Seminararbeit zusätzlich**: Vortrag mindestens zweimal proben, Schwachstellen der Arbeit kennen, für die Disputation vorbereitet sein.

## Königsklasse

Eine Arbeit, die die Lehrkraft beeindruckt, **gerade weil Du gegen sie argumentiert hast** — aber mit so guten Argumenten, dass sie es Dir nicht übel nimmt, sondern respektiert. Das ist die Königsklasse. Sie ist erlernbar.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 24 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `anschluss-routing` | Nutze dies, wenn Anschluss-Routing im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Hausarbeitenmacher.; Welche Unterlagen brauchen Sie?; Welcher Spezialskill passt?. |
| `aufgabenstellung-erfassen-fachgebiet` | Nutze dies, wenn Aufgabenstellung Erfassen, Fachgebiet Routing Zivil Öffentlich Straf, Gliederung Mit Tiefenstruktur im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Hausarbeitenm... |
| `ausfluegen-didaktisches-durch` | Nutze dies, wenn Spezial Ausfluegen Compliance Dokumentation Und Akte, Spezial Didaktisches Erstpruefung Und Mandatsziel, Spezial Durch Schriftsatz Brief Und Memo Bausteine im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Aus... |
| `behutsame-frech-haeufige-fehler` | Nutze dies, wenn Behutsame Frech Wertschaetzende Rueckfragen, Haeufige Fehler Vermeiden, Selbstkontrolle Vor Abgabe im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.... |
| `dokumente-intake` | Nutze dies, wenn Dokumentenintake im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `einstieg-routing` | Nutze dies, wenn Einstieg und Routing im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Hausarbeitenmacher.; Welche Unterlagen brauchen Sie?; Welcher Spezialskill passt?. |
| `europarecht-anwendbarkeit-hausarbeiten` | Nutze dies, wenn Europarecht Anwendbarkeit Vorrang Vorabentscheidung, Spezial Hausarbeiten Fristen Form Und Zustaendigkeit, Bearbeitungsplan Erstellen im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Bitte Europarec... |
| `europarecht-interessen-fertigen-sonderfall` | Nutze dies, wenn Spezial Europarecht Mehrparteien Konflikt Und Interessen, Spezial Fertigen Sonderfall Und Edge Case, Spezial Fuehrt Risikoampel Und Gegenargumente im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Bi... |
| `gutachtenstil-vs-haus-fussnotenstil` | Nutze dies, wenn Gutachtenstil Vs Urteilsstil, Haus Fussnotenstil Spezial, Haus Literaturrecherche Leitfaden im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Bitte Gutachtenstil Vs Urteilsstil, Haus Fussnotenstil Sp... |
| `haus-plagiatscheck-themaeingrenzung` | Nutze dies, wenn Haus Plagiatscheck Eigenstaendigkeit Spezial, Haus Themaeingrenzung Bauleiter, Meinungsstreit Darstellen im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Bitte Haus Plagiatscheck Eigenstaendigkeit S... |
| `hausarbeit-start` | Nutze dies, wenn Allgemein, Hausarbeit Workflow Start, Workflow Chronologie Und Belegmatrix im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Bitte Allgemein, Hausarbeit Workflow Start, Workflow Chronologie Und Beleg... |
| `juristische-liefert-beweislast-rechtstheorie` | Nutze dies, wenn Spezial Juristische Tatbestand Beweis Und Belege, Spezial Liefert Beweislast Und Darlegungslast, Spezial Rechtstheorie Internationaler Bezug Und Schnittstellen im Plugin Hausarbeitenmacher konkret bearbeitet werden soll.... |
| `methodenlehre-auslegung-oeffentliches` | Nutze dies, wenn Methodenlehre Auslegung, Oeffentliches Recht Statthaft Zulaessig Begruendet, Professor Erkennen Und Strategie im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Bitte Methodenlehre Auslegung, Oeffentl... |
| `oeffentliches-quellenkarte` | Nutze dies, wenn Oeffentliches Quellenkarte im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `output-waehlen` | Nutze dies, wenn Output wählen im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Bitte Output wählen prüfen.; Erstelle eine Arbeitsfassung zu Output wählen.; Welche Normen und Nachweise brauche ich?. |
| `quellen-livecheck` | Nutze dies, wenn Rechtsquellen-Livecheck im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `quellenrecherche` | Nutze dies, wenn Workflow Fristen Und Risikoampel, Workflow Redteam Qualitygate, Quellenrecherche Rechtsprechung Literatur im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; G... |
| `rechtstheorie-rechtsphilosophie-seminararbeit` | Nutze dies, wenn Rechtstheorie Rechtsphilosophie Anbindung, Seminararbeit Modus, Spezial Adressaten Formular Portal Und Einreichung im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Bitte Rechtstheorie Rechtsphilosop... |
| `schleimerei-seminararbeiten-sokratisch` | Nutze dies, wenn Spezial Schleimerei Mandantenkommunikation Entscheidungsvorlage, Spezial Seminararbeiten Dokumentenmatrix Und Lueckenliste, Spezial Sokratisch Behörden Gericht Und Registerweg im Plugin Hausarbeitenmacher konkret bearbei... |
| `strafrecht-zivilrecht-rechtswidrigkeit` | Nutze dies, wenn Spezial Strafrecht Zahlen Schwellen Und Berechnung, Spezial Zivilrecht Verhandlung Vergleich Und Eskalation, Strafrecht Tatbestand Rechtswidrigkeit Schuld im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Ausl... |
| `strategie-fehlerkatalog` | Nutze dies, wenn Strategie Fehlerkatalog im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Frist oder Beweislast übersehe ich?. |
| `subsumtion-schritt-verfassungsrecht` | Nutze dies, wenn Subsumtion Schritt Für Schritt, Verfassungsrecht Grundrechtspruefung, Zitierweise Jura Fundstellen im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Bitte Subsumtion Schritt Für Schritt, Verfassungsr... |
| `unterlagen-luecken` | Nutze dies, wenn Unterlagen und Lücken im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `zivilrecht-anspruchsgrundlagen` | Nutze dies, wenn Zivilrecht Anspruchsgrundlagen Prüfung im Plugin Hausarbeitenmacher konkret bearbeitet werden soll. Auslöser: Bitte Zivilrecht Anspruchsgrundlagen Prüfung prüfen.; Erstelle eine Arbeitsfassung zu Zivilrecht Anspruchsgrun... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
