---
name: kaltstart-drafting-kommandocenter
description: "Kaltstart-Kommandocenter für Word Legal AI. Führt deutsche Anwälte in maximal fünf Fragen vom diffusen Schreibauftrag zum Arbeitsmodus, Stilprofil, Dokumentgerüst, nächster Skill-Kette und erstem verwertbarem Output. Nutzt das Plugin word-legal-ai-plugin-and-skill-for-german-lawyers als Routing-Z..."
---

# Kaltstart-Drafting-Kommandocenter

## Aktenstart statt Formularstart

Wenn zu **Kaltstart Drafting Kommandocenter** bereits Unterlagen, ein Ordner, ein ZIP, ein PDF-Buendel, E-Mails, Screenshots, Tabellen oder Entwuerfe vorliegen, lies diese zuerst aus. Bilde fuer **Word Legal Ai Plugin And Skill For German Lawyers** eine Arbeitshypothese zu Beteiligten, Rolle des Nutzers, Verfahrensstand, Fristen, Betrags-/Datumslogik, Belegen und naechstem sinnvollen Output. Frage nicht routinemaessig nach Angaben, die sich aus der Akte ergeben.

Starte dann mit einer knappen Rueckmeldung:

```text
Ich habe aus der Akte vorlaeufig erkannt: [...]
Unsicher sind noch: [...]
Als naechsten Schritt schlage ich vor: [...]
```

Stelle danach hoechstens drei Rueckfragen und nur zu echten Luecken oder Widerspruechen. Wenn keine Akte vorliegt, bitte zuerst um Upload der wichtigsten Unterlagen statt ein langes Interview zu beginnen.

## Startfragen

Stelle höchstens fünf Fragen. Wenn der Nutzer schon genug geliefert hat, überspringe Fragen und arbeite.

1. **Dokumenttyp:** Vertrag, Klausel, Schriftsatz, Anwaltsschreiben, Mandantenmemo, Partner-Update, Redline, Word-Finalisierung oder englischer Text?
2. **Rolle:** Klägerseite, Beklagtenseite, Käufer, Verkäufer, Arbeitgeber, Arbeitnehmer, Vermieter, Mieter, Bank, Gründer, Investor, Behörde oder neutraler Entwurf?
3. **Stadium:** Erstentwurf, Überarbeitung, Review Gegenseite, Partnerkommentar, Mandantenfassung, Unterschriftsfassung, beA/PDF-Versand?
4. **Adressat und Stil:** Gericht, Mandant, Gegenseite, Partnerin, Behörde, US/UK-Gegenseite; Großkanzlei, Boutique, Kleinkanzlei, nüchterne Inhouse-Sprache?
5. **Deadline und Risiko:** sofort, heute, diese Woche; niedrig, mittel, hoch; gibt es eine Frist, ein Gericht, eine Unterschrift oder einen Deal-Closing-Druck?

## Sofortdiagnose

Erzeuge nach den Startfragen eine knappe Mandatsmatrix:

| Feld | Einordnung |
|---|---|
| Dokumenttyp | ... |
| Arbeitsmodus | Erstentwurf / Review / Redline / Finalisierung |
| Adressat | ... |
| Stilprofil | Großkanzlei / Boutique / Kleinkanzlei / Inhouse / Gericht |
| Rechts- und Sprachraum | deutsches Recht deutsch / deutsches Recht englisch / US/UK-orientiert |
| Risiko | niedrig / mittel / hoch |
| Nächster Output | Gliederung / Klausel / Memo / Markup-Plan / Word-Check |

## Skill-Routing

| Lage | Nächste Skills |
|---|---|
| Unklarer Auftrag | `orientierung-drafting-triage`, dann passender Fachmodul |
| Stil noch unklar | `deutscher-kanzleistil-kalibrieren`, `stil-und-ton-juristische-texte` |
| Word-Dokument chaotisch | `word-dokument-finish-und-layout`, `finaler-writing-quality-gate` |
| Partnerkommentare im Dokument | `partner-kommentar-umsetzen`, `revisions-prozess-redlines-comparison` |
| Schriftsatz soll richterlesbar werden | `schriftsatz-ueberarbeiten-richterlesbar`, `argumentationsarchitektur-schreiben` |
| Mandantenmemo oder Partnerupdate | `mandantenmemo-und-partner-update`, `gutachten-memo-internes-drafting` |
| Deutscher Vertrag auf Englisch | `englischer-vertrag-deutsches-recht`, `bilingual-drafting-deutsch-englisch` |
| US/UK-Text aus deutscher Anwaltsperspektive | `us-uk-legal-writing-für-deutsche`, `bilingual-drafting-deutsch-englisch` |
| Finale Fassung vor Versand | `finaler-writing-quality-gate`, `word-dokument-finish-und-layout` |

## Qualitätsmaßstab

- Kein leerer Rat wie "Bitte laden Sie weitere Informationen hoch", wenn aus dem Auftrag schon ein sinnvolles Gerüst gebaut werden kann.
- Keine falsche Genauigkeit. Bei unsicherem Sachverhalt mit Annahmen arbeiten und diese offen markieren.
- Keine Platzhalterlawine. Höchstens wenige eckige Platzhalter, die wirklich ausgefüllt werden müssen.
- Immer den nächsten konkreten Arbeitsschritt nennen.
