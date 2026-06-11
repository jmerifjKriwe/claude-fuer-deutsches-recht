# Lizenzvertragsersteller

Baukastensystem fuer IP-Lizenzvertraege nach deutschem und internationalem Recht. Pro Rolle, IP-Typ und Klauselbaustein ein Skill — die Skills greifen ineinander, vom Mandats-Intake bis zum unterschriftsreifen Vertrag in DE, EN oder bilingual.


<!-- BEGIN megaprompt-und-vorlagen (autogen) -->
## Experimentell: dieses Plugin auch ohne Claude Code

### Megaprompt (alle Kern-Skills in einer Datei)

Das Plugin gibt es zusaetzlich als **single-file Megaprompt** — ein experimentelles Markdown, das die wichtigsten Skills in einer einzigen Datei buendelt. Drop das in einen Chat ohne Claude-Code-Integration; der Agent erhaelt damit die gebuendelten Skill-Anweisungen.

- **Direkt-Download**: [`lizenzvertragsersteller.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/megaprompts/lizenzvertragsersteller.md) (52 KB)
- Im Repo: [`testakten/megaprompts/lizenzvertragsersteller.md`](../testakten/megaprompts/lizenzvertragsersteller.md)

*Keine Haftung, keine Gewaehr — Megaprompts sind eine Best-Effort-Kompression, kein vollwertiger Plugin-Ersatz.*

### Formatvorlagen (Markdown + ODT)

Sofort verwendbare Vorlagen (Times Roman 11pt, A4, mit Disclaimer und Feldern in [Klammern]). Markdown zum Lesen / Anpassen, ODT zum Bearbeiten in LibreOffice/Word.

| Vorlage | Markdown | ODT |
| --- | --- | --- |
| Patent Lizenz Kurzform Bilingual | [`.md`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/lizenzvertragsersteller/patent-lizenz-kurzform-bilingual.md) | [`.odt`](https://raw.githubusercontent.com/Klotzkette/claude-fuer-deutsches-recht/main/testakten/formatvorlagen-paradebeispiele/lizenzvertragsersteller/patent-lizenz-kurzform-bilingual.odt) |

*Experimentelle KI-Vorlagen — keine Haftung. Vor Verwendung im Mandat anwaltlich pruefen und an konkreten Fall anpassen.*

<!-- END megaprompt-und-vorlagen (autogen) -->

## Was deckt das Plugin ab?

### IP-Typen
- **Urheberrecht und Software** (UrhG; $$ 31, 32, 32a, 69a-g)
- **Patente** (PatG; TT-GVO-Konformitaet)
- **Marken** (MarkenG $ 30; DPMA/EUIPO; Qualitaetskontrolle)
- **Geschmacksmuster / Design** (DesignG; EU-VO 6/2002)
- **Gebrauchsmuster** (GebrMG; Schnellschuss-Strategie neben Patent)
- **Geschaeftsgeheimnisse / Know-how** (GeschGehG; Reverse-Engineering-Verbot)

### Parteienrollen
- Lizenzgeber / Lizenznehmer
- Sicherheitengeber / Sicherheitennehmer (Bank, Investor)
- Verwahrer / Escrow-Agent (Source-Code-Hinterlegung)
- Cross-Lizenz-Partner (Patent-Pool, Forschungspartnerschaft)
- Konzernlizenznehmer

### Vertragsbausteine
- Lizenzgegenstand mit Anlage A (IP-Liste, Reg.-Nr., Belastungen)
- Lizenzumfang (Territorium, Zeit, Anwendungsfeld)
- Exklusivitaet (sole, exclusive, non-exclusive, Most-Favoured-Customer)
- Verguetung (Pauschale, Running Royalty, Tiered, Mindestlizenz, Milestones)
- Reporting, Audit, Strafzinsen
- Sub-Lizenzen
- Verbesserungen / Grant-Back
- Haftung / Gewaehrleistung / Indemnification
- Rechtswahl + Gerichtsstand + Schiedsklausel (DE/EN/Schiedsinstitute)
- Vertragsdauer + Kuendigung + Folgen
- Vertraulichkeit + NDA-Interimsphase
- Source-Code-Escrow
- Insolvenzfestigkeit ($ 103 InsO)
- Sicherungslizenz / Pfandrecht an Immaterialguetern

### Compliance-Schichten
- Kartellrecht (TT-GVO EU 316/2014)
- Exportkontrolle (Dual-Use VO EU 2021/821; AWG/AWV; Sanktionen)
- Datenschutz (DSGVO Art. 28, 44 ff., 26)
- Steuern + Quellensteuer + DBA

### Output-Module
- Vertrag DE (Fertigentwurf, 20 Paragraphen, Anlagen A-E)
- Vertrag EN (Licence Agreement, English Law oder German Law)
- Bilingual DE/EN (side-by-side + Massgeb-Klausel)

## Workflow

```
1. einstieg-routing                          (Dashboard, Sofort-Triage)
2. mandat-intake-und-konfliktpruefung        (Konflikt-Check, Eilfristen)
3. ip-identifikation-und-bestandsaufnahme    (Anlage A: IP-Inventar)
4. parteienrolle-klaeren-...                  (Rollenmatrix)
5. transaktionsstruktur-visualisieren-ascii  (Diagramm)
6. pro IP-Typ: lizenz-XXX-spezialskill        (UrhG, PatG, MarkenG, ...)
7. Klauselbausteine waehlen + adaptieren     (klausel-XXX)
8. Compliance-Pruefung                        (TT-GVO, Dual-Use, DSGVO, Steuern)
9. Output                                     (DE / EN / bilingual)
```

## Quellenhygiene

- Rechtsprechung nur live verifizieren auf `bundesgerichtshof.de`, `dejure.org`, `curia.europa.eu`, `bundespatentgericht.de`.
- Keine BeckRS-/juris-/Kommentar-/Aufsatz-Blindzitate.
- Norm-Stellen aus `gesetze-im-internet.de` und `eur-lex.europa.eu`.

Konvention: siehe `references/quellenhygiene.md`, `references/zitierweise.md`, `references/leitentscheidungen-anker.md`.

## 32 Skills auf einen Blick

| Gruppe | Skills |
|---|---|
| Einstieg + Intake | `einstieg-routing`, `mandat-intake-und-konfliktpruefung`, `ip-identifikation-und-bestandsaufnahme`, `parteienrolle-klaeren-lizenzgeber-nehmer-sicherheiten-verwahrer`, `transaktionsstruktur-visualisieren-ascii` |
| IP-Typ | `lizenz-urheberrecht-und-software-urhg`, `lizenz-patent-patg`, `lizenz-marke-markeng`, `lizenz-geschmacksmuster-design-designg`, `lizenz-gebrauchsmuster-gebrmg`, `lizenz-geschaeftsgeheimnis-knowhow-geschgehg` |
| Klauseln | `klausel-lizenzgegenstand-und-anlage-ip-liste`, `klausel-lizenzumfang-territorium-zeit-feld`, `klausel-exklusivitaet-sole-non-exclusive`, `klausel-verguetung-pauschale-royalty-tiered`, `klausel-mindestlizenzen-meldungen-audit`, `klausel-unterlizenzen-sublicensing`, `klausel-verbesserungen-grant-back`, `klausel-haftung-gewaehrleistung-indemnification`, `klausel-rechtswahl-gerichtsstand-schiedsklausel`, `klausel-vertragsdauer-kuendigung-rueckwirkung`, `klausel-vertraulichkeit-und-nda-interimsphase` |
| Insolvenz + Sicherheiten | `escrow-quellcode-verwahrer-vereinbarung`, `insolvenz-fortbestand-paragraf-103-inso-lizenz`, `sicherungslizenz-pfandrecht-an-immaterialguetern` |
| Compliance | `kartellrecht-tt-gvo-eu-316-2014`, `exportkontrolle-dual-use-eu-2021-821`, `datenschutz-dsgvo-im-lizenzvertrag`, `steuern-quellensteuer-und-dba-lizenz` |
| Output | `output-vertrag-deutsch-fertigentwurf`, `output-vertrag-englisch-fertigentwurf`, `output-zweisprachig-bilingual-deutsch-englisch` |

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfaenger.
