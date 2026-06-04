# AGB-Recht-Prüfer

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`agb-recht-pruefer`) | [`agb-recht-pruefer.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/agb-recht-pruefer.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **BGB BT — Smart-Kühlschrank, digitale Elemente und Reparaturblockade** (`bgb-bt-smart-kuehlschrank-digital-repair-koeln`) | [Gesamt-PDF lesen](../testakten/bgb-bt-smart-kuehlschrank-digital-repair-koeln/gesamt-pdf/bgb-bt-smart-kuehlschrank-digital-repair-koeln_gesamt.pdf) | [`testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-bgb-bt-smart-kuehlschrank-digital-repair-koeln.zip) |
| **Akte Nordstern MedTech Vertrieb - Provision, Buchauszug und Ausgleich** (`handelsvertreterrecht-provisionsausgleich-nordstern-medtech`) | [Gesamt-PDF lesen](../testakten/handelsvertreterrecht-provisionsausgleich-nordstern-medtech/gesamt-pdf/handelsvertreterrecht-provisionsausgleich-nordstern-medtech_gesamt.pdf) | [`testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-handelsvertreterrecht-provisionsausgleich-nordstern-medtech.zip) |
| **Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7** (`robotikrecht-roboterflotte-vellbruck-muenchen`) | [Gesamt-PDF lesen](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Gigantisches Plugin für deutsches AGB-Recht: Prüfen, Entwerfen, Redlinen, Verhandeln, Rollout und Streitverteidigung von Allgemeinen Geschäftsbedingungen in allen praktischen Varianten.

Das Plugin ist bewusst zweigleisig gebaut:

- **AGB prüfen:** Klauseln zerlegen, Einbeziehung und Transparenz prüfen, §§ 305 bis 310 BGB sauber anwenden, Risiko bewerten, bessere Fassung vorschlagen.
- **AGB entwerfen:** Geschäftsmodell verstehen, Klauselfamilien auswählen, sichere oder bewusst risikobehaftete Fassungen erzeugen, Rollout und Nachweisfähigkeit mitdenken.

## Start

```text
/agb-recht-prüfer:allgemein
```

Der Einstieg fragt zürst nicht zwanzig Dinge ab, sondern klärt die wichtigste Weiche: **prüfen oder entwerfen?** Danach routet er in passende Spezialskills, etwa Verbraucher-AGB, B2B-AGB, Online-Checkout, Preisanpassung, Haftung, Laufzeit, UKlaG, Redline oder konkrete Branchenbedingungen.

## Arbeitsweise

1. Klausel und Vertragstyp erfassen.
2. AGB-Eigenschaft und Einbeziehung prüfen.
3. Überraschung, Mehrdeutigkeit und Transparenz klären.
4. Inhaltskontrolle nach §§ 307 bis 309 BGB und Besonderheiten nach § 310 BGB.
5. Rechtsfolge, Rückabwicklung, UKlaG-/Prozessrisiko prüfen.
6. Bessere Klausel entwerfen: sicher, balanced oder aggressiv mit Warnlabel.
7. Rollout, Versionierung, Nachweisbarkeit und Fachbereichskommunikation erledigen.

## Live-Quellen

Das Plugin soll bei tragenden Aussagen immer die aktülle amtliche Fassung auf **Gesetze im Internet** prüfen, insbesondere BGB §§ 305 bis 310 und UKlaG. Siehe [`references/QUELLEN.md`](./references/QUELLEN.md).

## Typische Ergebnisse

| Bedarf | Ergebnis |
| --- | --- |
| Fremde AGB schnell prüfen | Klauselampel, Risikobegründung, Redline-Kommentar |
| Eigene AGB neu entwerfen | Klauselarchitektur, sichere Fassungen, Fallbacks |
| B2C-Rollout vorbereiten | Checkout-/Einbeziehungscheck, Versionierung, Kundenkommunikation |
| B2B-Verhandlung führen | Playbook mit Must-have, Fallback, No-Go und Argumenten |
| Abmahnung erhalten | Fristenscan, UKlaG-Risiko, modifizierte Unterlassungserklärung |
| Management informieren | kurze Legal Note mit Risiko, Optionen und Empfehlung |

## Enthaltene Skills

Die vollständige Skill-Liste wird automatisch am Ende dieser README aktualisiert.

## Lizenz

Apache-2.0 OR MIT — Auswahl beim Empfänger.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 29 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `agb-entwurf-kaltstart` | Einstiegs- und Workflow-Skill für AGB Entwurf Kaltstart: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `agb-pruefung-kaltstart` | Einstiegs- und Workflow-Skill für AGB Prüfung Kaltstart: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `allgemein` | Einstiegs- und Workflow-Skill für Allgemein: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `ki-output-nutzung` | Klausel-Spezialskill für KI Output Nutzung: prüft, redlined und entwirft die Klausel mit Risikoampel, Verbraucher-/B2B-Unterscheidung und praxistauglicher Ersatzfassung. |
| `kompendium-01-product-counsel-work-bis-agb-im-bauvertrag-vo` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 01; bündelt 10 frühere Spezialskills (product-counsel-workflow, feedback-rechte, annahmefrist-leistungsfrist-308, kuendigungsfiktion-und-nachfrist-308, kurzfristige-preiserhoehung-309 un... |
| `kompendium-02-agb-im-leasingvertra-bis-klausel-entwerfen-ag` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 02; bündelt 10 frühere Spezialskills (agb-im-leasingvertrag-fortwirkung, agb-schiedsklausel-opt-out-deutsches-recht, agb-vertragsstrafe-309-nr-6, ergaenzende-vertragsauslegung-bei-agb-lu... |
| `kompendium-03-klausel-entwerfen-ba-bis-preisanpassung-klaus` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 03; bündelt 10 frühere Spezialskills (klausel-entwerfen-balanced, klausel-entwerfen-low-risk, klauselbibliothek-aufbau, klauselinventar-und-scope, klauselvarianten-vergleich und 5 weiter... |
| `kompendium-04-rechtsabteilung-chan-bis-agb-haftung-erfuellu` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 04; bündelt 10 frühere Spezialskills (rechtsabteilung-change-control-klauseln-im-konzernvertrag, rechtsabteilung-vertragsstrafe-in-einheitspreis-und-liefervertra, salvatorische-klausel,... |
| `kompendium-05-compliance-sanktione-bis-abnahme-testing` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 05; bündelt 10 frühere Spezialskills (compliance-sanktionen, haftung-grobe-fahrlaessigkeit-vorsatz, haftung-indirekte-schaeden, haftung-leben-koerper-gesundheit-309, haftungscap-summe un... |
| `kompendium-06-abtretung-bis-agb-bei-vereinen-und` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 06; bündelt 10 frühere Spezialskills (abtretung, adversarial-test-agb, aenderungsvorbehalt-308, agb-arbeitnehmerueberlassung-aueg, agb-begriff-vorformuliert-305 und 5 weitere) und bewahr... |
| `kompendium-07-agb-bei-versicherung-bis-agb-und-cookie-einwi` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 07; bündelt 10 frühere Spezialskills (agb-bei-versicherungsvertraegen-vvg, agb-im-konzernverbund, agb-im-mietrecht-wohnraum-vs-gewerbe, agb-in-kapitalanlagen-effektenhandel, agb-preisanp... |
| `kompendium-08-agb-und-ipr-art-6-ro-bis-automatische-verlaen` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 08; bündelt 10 frühere Spezialskills (agb-und-ipr-art-6-rom-i-verbraucher, agb-versionierung-aenderungshistorie, agb-werkleistung-vob-b-aktuell, agentur-marketing-agb, app-agb und 5 weit... |
| `kompendium-09-avv-und-agb-schnitts-bis-bildungs-kurs-agb` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 09; bündelt 10 frühere Spezialskills (avv-und-agb-schnittstelle, b2b-harte-fassung, b2c-b2b-b2b2c-rollencheck, backup-datenverlust, bank-agb und 5 weitere) und bewahrt deren Workflows, N... |
| `kompendium-10-blue-pencil-und-gelt-bis-crowdfunding-agb` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 10; bündelt 10 frühere Spezialskills (blue-pencil-und-geltungserhaltende-reduktion, board-brief-agb, bonitaetspruefung, bonus-rabatt, business-summary-agb und 5 weitere) und bewahrt dere... |
| `kompendium-11-crypto-exchange-agb-bis-ecommerce-shop-agb` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 11; bündelt 10 frühere Spezialskills (crypto-exchange-agb, darlehen-finanzierung-agb, datenexport-portabilitaet, datenschutzverweise-agb, definitionen-glossar-agb und 5 weitere) und bewa... |
| `kompendium-12-eigentumsvorbehalt-bis-fiktive-erklaerung-z` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 12; bündelt 10 frühere Spezialskills (eigentumsvorbehalt, einbeziehung-hinweis-kenntnisnahme-305, einbeziehung-online-clickwrap-browsewrap, einkaufsbedingungen-b2b, einstweilige-verfuegu... |
| `kompendium-13-fitnessstudio-agb-bis-gesellschaftsrechtli` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 13; bündelt 10 frühere Spezialskills (fitnessstudio-agb, force-majeure-hoehere-gewalt, formvorgaben-anzeigen-erklaerungen-309, forschung-entwicklung-agb, fragebogen-agb-automation und 5... |
| `kompendium-14-gesetzliches-leitbil-bis-kardinalpflichten` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 14; bündelt 10 frühere Spezialskills (gesetzliches-leitbild-abweichung-307, gewahrleistung-ausschluss, gewerbemiete-agb, handelsvertreter-agb, indexierung und 5 weitere) und bewahrt dere... |
| `kompendium-15-ki-service-agb-bis-liquidated-damages` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 15; bündelt 10 frühere Spezialskills (ki-service-agb, kollisionsrecht-ipr-agb, konto-kuendigung-sperre, kuendigung-aus-wichtigem-grund, kuendigung-ordentlich und 5 weitere) und bewahrt d... |
| `kompendium-16-logistik-spedition-a-bis-mehrsprachige-agb-ch` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 16; bündelt 10 frühere Spezialskills (logistik-spedition-agb, maengelrechte-309, mahngebuehren-und-zinsanpassung-agb, mandanteninterview-agb, mandantenmail-agb und 5 weitere) und bewahrt... |
| `kompendium-17-mindestabnahme-bis-plain-language-polit` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 17; bündelt 10 frühere Spezialskills (mindestabnahme, mitwirkungspflichten, nacherfuellung-vorrang, nda-standardbedingungen, negative-feststellung-agb und 5 weitere) und bewahrt deren Wo... |
| `kompendium-18-plattform-und-online-bis-referenznennung` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 18; bündelt 10 frühere Spezialskills (plattform-und-online-checkout, quality-gate-vor-rollout, rangfolge-sprache, rechtsabteilung-preisanpassung-bei-dauervertraegen-nach-energiek, rechts... |
| `kompendium-19-reisebedingungen-bis-security-incidents` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 19; bündelt 10 frühere Spezialskills (reisebedingungen, reseller-agb, risk-acceptance-memo, rollout-mail-bestandskunden, rollout-monitoring-agb und 5 weitere) und bewahrt deren Workflows... |
| `kompendium-20-sicherungsrechte-bis-subunternehmer` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 20; bündelt 10 frühere Spezialskills (sicherungsrechte, sla-service-credits, social-media-agb, softwarelizenz-agb, sperrung-suspendierung und 5 weitere) und bewahrt deren Workflows, Norm... |
| `kompendium-21-support-response-tim-bis-verbraucherbesonderh` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 21; bündelt 10 frühere Spezialskills (support-response-times, telekommunikation-agb, transparenzgebot-307, uklag-unterlassung-verbandsklage, unterlassungserklaerung-modifizieren und 5 we... |
| `kompendium-22-verbraucherfreundlic-bis-vollmacht-vertretung` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 22; bündelt 10 frühere Spezialskills (verbraucherfreundliche-fassung, verbraucherschutz-schnellcheck, vereinsbedingungen, verfuegbarkeit-wartungsfenster, verhandlungs-playbook-agb und 5... |
| `kompendium-23-vorkasse-abschlag-si-bis-zahlungsverzug-mahnk` | agb-recht-pruefer: Konsolidiertes Skill-Kompendium 23; bündelt 9 frühere Spezialskills (vorkasse-abschlag-sicherheit, wartung-maintenance, website-update-check, wesentliche-rechte-pflichten-307, widerruf-umfeld-agb und 4 weitere) und bew... |
| `legal-note-redline-output` | Einstiegs- und Workflow-Skill für Legal Note Redline Output: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |
| `red-team-gegneransicht-agb` | Einstiegs- und Workflow-Skill für Red Team Gegneransicht AGB: sortiert Ziel, Rolle, Dokumente, Normenstand, AGB-Risiko und nächsten Output schnell und anfängertauglich. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
