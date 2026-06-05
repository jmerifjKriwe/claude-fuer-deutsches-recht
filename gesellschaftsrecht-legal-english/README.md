# Didaktisches Gesellschaftsrecht — English Business Terms

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`gesellschaftsrecht-legal-english`) | [`gesellschaftsrecht-legal-english.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/gesellschaftsrecht-legal-english.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Roeschen Tech GmbH — Gründung, Series A, B-Shares und Streit-Eskalation** (`gesellschaftsgruender-streit-roeschen-tech`) | [Gesamt-PDF lesen](../testakten/gesellschaftsgruender-streit-roeschen-tech/gesamt-pdf/gesellschaftsgruender-streit-roeschen-tech_gesamt.pdf) | [`testakte-gesellschaftsgruender-streit-roeschen-tech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsgruender-streit-roeschen-tech.zip) |
| **Akte Kometenfalter Systems GmbH — Series A Project Comet Moth** (`gesellschaftsrecht-legal-english-frankfurt-startup`) | [Gesamt-PDF lesen](../testakten/gesellschaftsrecht-legal-english-frankfurt-startup/gesamt-pdf/gesellschaftsrecht-legal-english-frankfurt-startup_gesamt.pdf) | [`testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-gesellschaftsrecht-legal-english-frankfurt-startup.zip) |
| **Nebelstern Ventures - Berliner VC-Pipeline, Wandeldarlehen und Follow-on-Chaos** (`venture-capital-geber-nebelstern-portfolio-berlin`) | [Gesamt-PDF lesen](../testakten/venture-capital-geber-nebelstern-portfolio-berlin/gesamt-pdf/venture-capital-geber-nebelstern-portfolio-berlin_gesamt.pdf) | [`testakte-venture-capital-geber-nebelstern-portfolio-berlin.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-venture-capital-geber-nebelstern-portfolio-berlin.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Didaktisches Plugin für die zweisprachige Gesellschaftsrechts- und Transaktionspraxis. Es erklärt nicht nur Begriffe, sondern führt Anfängerinnen, Anfänger und laterale Quereinsteiger durch echte Arbeitsprodukte: Cap Table, Term Sheet, Investment Agreement, Gesellschaftervereinbarung, Satzung, SPA, Due-Diligence-Report, Closing-Checkliste, Mandantenmemo und Partnerbriefing.

Der Leitgedanke: Deutsche Dogmatik bleibt der Anker, aber die Praxis spricht oft zweisprachig. Ein `Cap Table` ist nicht einfach eine Gesellschafterliste. `Liquidation Preference` ist nicht bloß Vorzugsrecht. `Drag-along` ist nicht nur Mitverkaufspflicht. Das Plugin erklärt jeweils:

- was der englische Begriff im Deal-Kontext meint,
- welche deutsche Struktur oder Norm danebensteht,
- wo die Übersetzung verführt oder falsch wird,
- welches Dokument betroffen ist,
- welche Rückfragen ein First-Year Associate stellen muss,
- welcher Output für Partner, Mandant, Notar, Register oder Gegenseite sinnvoll ist.

## Installation

1. ZIP herunterladen.
2. Claude Code oder Claude Desktop/Cowork öffnen.
3. **Customize Plugins** bzw. **Personal plugins** öffnen.
4. **Install from .zip** wählen und `gesellschaftsrecht-legal-english.zip` hochladen.

Nicht das komplette Repository-ZIP hochladen. Das Plugin-ZIP muss im Root direkt `.claude-plugin/plugin.json`, `skills/` und `references/` enthalten.

## Arbeitsweise

Das Plugin arbeitet in drei Schichten:

| Schicht | Zweck |
| --- | --- |
| Begriff | Deutsch/Englisch dekodieren, False Friends markieren, dogmatische Nähe und Differenz erklären |
| Dokument | Begriff im konkreten Dokument verorten: Gesellschafterliste, Satzung, SHA, Term Sheet, SPA, DD-Report |
| Workflow | Aufgabe in ein anwaltliches Arbeitsprodukt übersetzen: Matrix, Memo, Markup-Hinweis, Rückfragenliste, Partnerbriefing |

## Enthaltene Skills

| Skill | Zweck |
| --- | --- |
| `allgemein` | Einstieg, Erfahrungslevel, Deal-Kontext, Begriffsfeld und Spezialskills auswählen. |
| `rookie-modus` | First-Year-Associate-Modus mit Kleinschritten, Rückfragen und Review-Gates. |
| `lernpfad-dealroom-simulator` | Führt Anfänger durch eine mehrteilige Transaktionsakte mit Materialinventar, Lernpfad, Übungen und Senior-Gates. |
| `anschauungsmaterial-multiformat-auswertung` | Wertet PDF, Scan, Screenshot, JPEG, Excel, Chat, Email und Dealroom-Fragmente als Quellen mit unterschiedlicher Verlässlichkeit aus. |
| `begriffskompass-intake` | Begriff, Dokument, Rechtsordnung, Parteirolle und Outputbedarf erfassen. |
| `cap-table-gesellschafterliste` | Cap Table gegen Gesellschafterliste, § 40 GmbHG und wirtschaftliche Beteiligung abgleichen. |
| `fully-diluted-esop-option-pool` | Fully diluted basis, ESOP/VSOP, Option Pool und Verwässerung erklären und rechnen. |
| `share-classes-vorzugsrechte` | Share classes, preferred/common shares und deutsche Umsetzung in GmbH/AG/Satzung einordnen. |
| `liquidation-preference-waterfall` | Liquidation Preference, participating/non-participating und Exit-Waterfall didaktisch aufbereiten. |
| `anti-dilution-protection` | Full ratchet, broad-based weighted average und deutsche Kapitalerhöhungsmechanik unterscheiden. |
| `vesting-leaver-cliff` | Vesting, Cliff, Good Leaver, Bad Leaver und Einziehung/Abtretung strukturieren. |
| `drag-tag-piggyback` | Drag-along, Tag-along und Piggyback Rights voneinander trennen. |
| `term-sheet-investment-agreement` | Term Sheet, Investment Agreement und rechtliche Bindungswirkung prüfen. |
| `sha-gesellschaftervereinbarung` | Shareholders Agreement, Pooling, Stimmbindung und Satzungsschnittstelle erklären. |
| `articles-association-satzung` | Articles of association, Satzung/Gesellschaftsvertrag und Registerfähigkeit abgleichen. |
| `governance-board-consent-matters` | Board, Advisory Board, Consent Matters und deutsche Organlogik übersetzen. |
| `protective-provisions-vetorechte` | Protective provisions, Reserved Matters, Veto und Sperrminorität praktisch prüfen. |
| `transfer-restrictions-vinkulierung` | Transfer restrictions, ROFR, ROFO, Lock-up und Vinkulierung trennen. |
| `exit-spa-closing-cp` | Exit, SPA, signing, closing, CPs und Closing Deliverables didaktisch erklären. |
| `earn-out-kaufpreismechanik` | Earn-out, Milestones, Leakage und Kaufpreisanpassung in deutscher Vertragslogik aufbereiten. |
| `reps-warranties-indemnities` | Representations, warranties, covenants und indemnities ohne deutsche Scheinsynonyme erklären. |
| `due-diligence-red-flag-report` | DD-Begriffe, Red-Flag-Report, Materiality und Quellenbelege in Anfängerlogik führen. |
| `financing-convertible-loan-safe` | Convertible Loan, SAFE, Wandeldarlehen und deutsche Notar-/Kapitalerhöhungsfragen erklären. |
| `financial-debt-net-debt-working-capital` | Financial Debt, Net Debt, Cash Free Debt Free und Working Capital in Kaufpreisformeln prüfen. |
| `upstream-security-financial-assistance` | Upstream Loan/Security/Guarantee und Kapitalerhaltung/Financial Assistance markieren. |
| `reasonable-efforts-covenants` | Best/reasonable efforts, undertakings und covenants nach deutschem Recht konkretisieren. |
| `deutsches-recht-englische-vertraege` | Englische Vertragssprache bei deutschem Recht, Gerichtssprache und Commercial Courts absichern. |
| `client-explainer-legal-english` | Mandantenfreundliche Erklärung ohne Kanzleijargon erstellen. |
| `partner-briefing-memo` | Kurzes Partnerbriefing mit Issue, Risiko, Vorschlag und Rückfragen schreiben. |
| `qualitaetsgate-corporate-legal-english` | Schlussprüfung: Übersetzung, Rechtsanker, Dokument, Zahlenlogik, Risiken und offene Annahmen. |

## Typische Workflows

**Schneller Begriffsschock:** `allgemein` -> `rookie-modus` -> `begriffskompass-intake` -> passender Spezialskill -> `partner-briefing-memo`.

**Unübersichtlicher Dealroom:** `allgemein` -> `lernpfad-dealroom-simulator` -> `anschauungsmaterial-multiformat-auswertung` -> passende Spezialskills -> `qualitaetsgate-corporate-legal-english`.

**Startup-Finanzierungsrunde:** `cap-table-gesellschafterliste` -> `fully-diluted-esop-option-pool` -> `liquidation-preference-waterfall` -> `anti-dilution-protection` -> `term-sheet-investment-agreement` -> `qualitaetsgate-corporate-legal-english`.

**M&A-Dokumente auf Englisch bei deutschem Recht:** `deutsches-recht-englische-vertraege` -> `reps-warranties-indemnities` -> `financial-debt-net-debt-working-capital` -> `exit-spa-closing-cp` -> `partner-briefing-memo`.

## Quellenhygiene

- Dieses Plugin verarbeitet keine Aufsätze, Rezensionen oder sonstige Materialien als zitierfähige Vorlage. Es darf keine externen Texte wörtlich übernehmen, keine Autorennamen oder Fundstellen als Autorität nennen und keine besondere Nähe zu einzelnen Veröffentlichungen behaupten.
- Keine Paywall-Literatur, keine Kommentarzitate und keine Blindzitate.
- Gesetzesanker aus amtlichen oder frei zugänglichen Quellen verwenden.
- Amtliche englische Übersetzungen deutscher Gesetze sind Hilfsmittel, nicht die verbindliche Fassung.
- Bei Rechtsprechung nur Gericht, Entscheidungsform, Datum, Aktenzeichen und frei prüfbare Quelle ausgeben.

## Demo-Material

Die Testakte `gesellschaftsrecht-legal-english-frankfurt-startup` eignet sich für Live-Demos:

- erst `00` bis `03` für Einstieg, Deal-Personen, Cap Table und Term Sheet,
- dann `04` bis `06` für SHA/Satzung/Vesting, DD-Red-Flags und den Associate-Arbeitsstand,
- dann `10` bis `14` für Wandeldarlehen-Vorgeschichte, Investor-Counsel-Markup, Notar-Checkliste, Side Letter und Board-/Consent-Mapping,
- dann `16` und `18` bis `22` für die Multi-Format-Materialien (WhatsApp-Thread im Chatlook, Cap-Table-Excel samt PDF-Ausdruck, Notar-Memo, Whiteboard, Investor-Email- und WhatsApp-Screenshot) sowie `chats/` für Slack-Thread und WhatsApp je als eigenes Dokument,
- zum Schluss `15`, `24` und `25` für Closing-Checkliste, Agio-/Kapitalrücklage-Streitfrage und Mailbox-/Call-Fragmente.
- Für schnelle Vorführungen ohne Fragmentwechsel: `26-gesamtakte-kometenfalter-series-a.pdf`.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 28 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg fuer das Gesellschaftsrecht-Legal-English-Plugin: erkennt Begriffsschock, Deal-Kontext, Erfahrungslevel, Dokumenttyp und routet zu den passenden Corporate-English-Skills. |
| `anti-dilution-articles-association` | Nutze dies, wenn Anti Dilution Protection, Articles Association Satzung im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Anti Dilution Protection, Articles Association Satzung prüfen.; Erstelle e... |
| `begriffskompass-intake-bgb-at` | Nutze dies, wenn Begriffskompass Intake, Bgb At Schuldrecht At Im Ma im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `business-corporate` | Nutze dies, wenn Spezial Business Dokumentenmatrix Und Lueckenliste, Spezial Corporate Behörden Gericht Und Registerweg im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Spezial Business Dokumente... |
| `cap-table-client-explainer` | Nutze dies, wenn Cap Table Gesellschafterliste, Client Explainer Legal English im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Cap Table Gesellschafterliste, Client Explainer Legal English prüfe... |
| `chronologie-fristen` | Nutze dies, wenn Workflow Chronologie Und Belegmatrix, Workflow Fristen Und Risikoampel im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Workflow Chronologie Und Belegmatrix, Workflow Fristen Und... |
| `dealroom-quellenkarte` | Nutze dies, wenn Dealroom Quellenkarte im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Welche amtliche Quelle prüfe ich zuerst?; Gibt es aktuelle Rechtsprechung?; Bitte Fundstellen verifizieren.. |
| `deutsches-englische-drag-tag` | Nutze dies, wenn Deutsches Recht Englische Vertraege, Drag Tag Piggyback im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Deutsches Recht Englische Vertraege, Drag Tag Piggyback prüfen.; Erstelle... |
| `didaktisches-gesellschafterliste` | Nutze dies, wenn Spezial Didaktisches Erstpruefung Und Mandatsziel, Spezial Gesellschafterliste Compliance Dokumentation Und Akte im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Spezial Didaktis... |
| `dokumente-intake` | Nutze dies, wenn Dokumentenintake im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `due-diligence-earn-out` | Nutze dies, wenn Due Diligence Red Flag Report, Earn Out Kaufpreismechanik im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Due Diligence Red Flag Report, Earn Out Kaufpreismechanik prüfen.; Erst... |
| `einstieg-routing` | Nutze dies, wenn Einstieg und Routing im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Ich habe ein neues Thema im Bereich Gesellschaftsrecht Legal English.; Welche Unterlagen brauchen Sie?; Welcher Sp... |
| `english-anschauungsmaterial-multiformat` | Nutze dies, wenn Spezial English Fristen Form Und Zustaendigkeit, Anschauungsmaterial Multiformat Auswertung im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Spezial English Fristen Form Und Zust... |
| `exit-spa-financial-debt` | Nutze dies, wenn Exit Spa Closing Cp, Financial Debt Net Debt Working Capital im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Exit Spa Closing Cp, Financial Debt Net Debt Working Capital prüfen.... |
| `financing-convertible-fully-diluted` | Nutze dies, wenn Financing Convertible Loan Safe, Fully Diluted Esop Option Pool im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Financing Convertible Loan Safe, Fully Diluted Esop Option Pool p... |
| `gesellschaftsrecht-legal` | Nutze dies, wenn Spezial Gesellschaftsrecht Tatbestand Beweis Und Belege, Spezial Legal Schriftsatz Brief Und Memo Bausteine im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Spezial Gesellschafts... |
| `governance-board-lernpfad-dealroom` | Nutze dies, wenn Governance Board Consent Matters, Lernpfad Dealroom Simulator im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Governance Board Consent Matters, Lernpfad Dealroom Simulator prüfe... |
| `liquidation-preference-partner-briefing` | Nutze dies, wenn Liquidation Preference Waterfall, Partner Briefing Memo im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Liquidation Preference Waterfall, Partner Briefing Memo prüfen.; Erstelle... |
| `output-waehlen` | Nutze dies, wenn Output wählen im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Output wählen prüfen.; Erstelle eine Arbeitsfassung zu Output wählen.; Welche Normen und Nachweise brauche ich?. |
| `protective-provisions-qualitaetsgate` | Nutze dies, wenn Protective Provisions Vetorechte, Qualitaetsgate Corporate Legal English im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Was kann hier schiefgehen?; Bitte red-team prüfen.; Welche Fri... |
| `reasonable-efforts-reps-warranties` | Nutze dies, wenn Reasonable Efforts Covenants, Reps Warranties Indemnities im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Reasonable Efforts Covenants, Reps Warranties Indemnities prüfen.; Erst... |
| `rookie-modus-sha-gesellschaftervereinbarung` | Nutze dies, wenn Rookie Modus, Sha Gesellschaftervereinbarung im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Rookie Modus, Sha Gesellschaftervereinbarung prüfen.; Erstelle eine Arbeitsfassung z... |
| `share-classes-anfaenger` | Nutze dies, wenn Share Classes Vorzugsrechte, Spezial Anfaenger Verhandlung Vergleich Und Eskalation im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Share Classes Vorzugsrechte, Spezial Anfaenge... |
| `table-term-interessen` | Nutze dies, wenn Spezial Table Zahlen Schwellen Und Berechnung, Spezial Term Mehrparteien Konflikt Und Interessen im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Spezial Table Zahlen Schwellen U... |
| `terms-term-sheet` | Nutze dies, wenn Spezial Terms Risikoampel Und Gegenargumente, Term Sheet Investment Agreement im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Spezial Terms Risikoampel Und Gegenargumente, Term... |
| `transfer-restrictions-upstream-security` | Nutze dies, wenn Transfer Restrictions Vinkulierung, Upstream Security Financial Assistance im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Transfer Restrictions Vinkulierung, Upstream Security... |
| `unterlagen-luecken` | Nutze dies, wenn Unterlagen und Lücken im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Ich lade Unterlagen hoch.; Was fehlt noch?; Bitte Dokumente sortieren.. |
| `verdeckte-sacheinlage-vesting-leaver` | Nutze dies, wenn Verdeckte Sacheinlage, Vesting Leaver Cliff im Plugin Gesellschaftsrecht Legal English konkret bearbeitet werden soll. Auslöser: Bitte Verdeckte Sacheinlage, Vesting Leaver Cliff prüfen.; Erstelle eine Arbeitsfassung zu... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
