# Außenwirtschaft, Sanktionen, Zoll und CBAM

<!-- BEGIN plugin-sofort-download-section (autogen) -->
## ⬇️ Sofort-Downloads

Direkt-Downloads ohne Umwege. Die URLs sind stabil und zeigen immer auf die aktuelle Version (`latest`-Release).

### Plugin als ZIP

| Inhalt | Download |
| --- | --- |
| **Dieses Plugin** (`aussenwirtschaft-zoll-sanktionen`) | [`aussenwirtschaft-zoll-sanktionen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/aussenwirtschaft-zoll-sanktionen.zip) |

### Demonstrations-Akten

| Akte | PDF lesen | Akten-ZIP |
| --- | --- | --- |
| **Außenwirtschaft, Zoll, Sanktionen und CBAM – Globalmaschinen GmbH** (`aussenwirtschaft-zoll-sanktionen-globalmaschinen`) | [Gesamt-PDF lesen](../testakten/aussenwirtschaft-zoll-sanktionen-globalmaschinen/gesamt-pdf/aussenwirtschaft-zoll-sanktionen-globalmaschinen_gesamt.pdf) | [`testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-aussenwirtschaft-zoll-sanktionen-globalmaschinen.zip) |
| **Akte Waldkrone HealthTech GmbH - NDA, Meldekanal und Lieferantenhinweis** (`hinweisgeberschutz-nda-meldekanal-waldkrone`) | [Gesamt-PDF lesen](../testakten/hinweisgeberschutz-nda-meldekanal-waldkrone/gesamt-pdf/hinweisgeberschutz-nda-meldekanal-waldkrone_gesamt.pdf) | [`testakte-hinweisgeberschutz-nda-meldekanal-waldkrone.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-hinweisgeberschutz-nda-meldekanal-waldkrone.zip) |
| **Akte Vellbruck Robotics GmbH — Roboterflotte AtlasCare / LumaMove / Werkbank C7** (`robotikrecht-roboterflotte-vellbruck-muenchen`) | [Gesamt-PDF lesen](../testakten/robotikrecht-roboterflotte-vellbruck-muenchen/gesamt-pdf/robotikrecht-roboterflotte-vellbruck-muenchen_gesamt.pdf) | [`testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/testakte-robotikrecht-roboterflotte-vellbruck-muenchen.zip) |

<!-- END plugin-sofort-download-section (autogen) -->

Freistehendes Außenwirtschafts-, Sanktions-, Zoll- und CBAM-Plugin für international tätige Unternehmen, Einzelpersonen, Verbände, Import-/Exportabteilungen, Zollteams, Compliance, Geschäftsleitung und anwaltliche Krisenmandate.

Dieses Plugin ist **vollständig freistehend**. Es verweist nicht auf andere Plugins und bringt eigene Skills, Vorlagen, Leitplanken, Vorschau und Testakte mit. Wenn keine Schnittstelle zu ERP, Zollsoftware, Screening-Tool, CBAM-Register, ELAN-K2, Bundesbank-Portal oder Kanzleisystem besteht, arbeitet es mit manuellen Uploads oder einem ausdrücklich gekennzeichneten Simulationsmodus.

#

## Schnellstart

1. Plugin aktivieren oder ZIP aus dem Release installieren.
2. Neue Sache mit `aussenwirtschaft-kommandocenter` starten.
3. Ware, Software, Technologie, Dienstleistung oder Zahlung nennen.
4. Länder, Beteiligte, Banken, Endverwender, Zolltarifnummer und vorhandene Dokumente hochladen oder simulieren.
5. Am Ende immer das Qualitätstor ausgeben lassen: Quellenstand, Trefferlog, Fristen, Verbote, Genehmigungen, Meldungen, Abgaben, Anlagen und Sofortmaßnahmen.

## Enthaltene Skills

- `aussenwirtschaft-kommandocenter` - Außenwirtschaft-Kommandocenter
- `aussenwirtschaft-exportkontrolle-dual-use` - Exportkontrolle und Dual-Use
- `aussenwirtschaft-gueterlisten-klassifizierung` - Güterlisten- und Klassifizierungslog
- `aussenwirtschaft-bafa-genehmigungen` - BAFA-Genehmigungen und Anfragen
- `aussenwirtschaft-sanktionen-embargos` - Sanktionen, Embargos und Bereitstellungsverbote
- `aussenwirtschaft-us-ear-itar` - US EAR, ITAR und Extraterritorialität
- `aussenwirtschaft-zolltarif-vzta` - Zolltarif, TARIC und vZTA
- `aussenwirtschaft-zollwert-ursprung` - Zollwert, Ursprung und Präferenzen
- `aussenwirtschaft-zollverfahren-bewilligungen` - Zollverfahren, Bewilligungen und Vereinfachungen
- `aussenwirtschaft-vub-einfuhr-ausfuhr` - Verbote und Beschränkungen bei Ein- und Ausfuhr
- `aussenwirtschaft-cbam-co2-zoll` - CBAM und CO2-Grenzausgleich
- `aussenwirtschaft-verbrauchsteuer` - Verbrauchsteuer
- `aussenwirtschaft-antidumping-ausgleich` - Antidumping- und Ausgleichszölle
- `aussenwirtschaft-wto-handelspolitik` - WTO und handelspolitische Maßnahmen
- `aussenwirtschaft-awv-bundesbank` - AWV- und Bundesbank-Meldepflichten
- `aussenwirtschaft-aml-kyc-sanktionen` - AML, KYC und Sanktions-Compliance
- `aussenwirtschaft-pruefung-ermittlung` - Prüfungen, Ermittlungen und Offenlegung
- `aussenwirtschaft-presse-krise` - Presse, Reputation und Krisenkommunikation
- `aussenwirtschaft-icp-kontrollsystem` - Internal Compliance Program

## Vorlagen

- `assets/templates/aussenwirtschaft-mandatskarte.md` - Außenwirtschaft-Mandatskarte
- `assets/templates/transaction-screening-matrix.md` - Transaktions-Screening-Matrix
- `assets/templates/exportkontrolle-dual-use-pruefung.md` - Exportkontrolle- und Dual-Use-Prüfung
- `assets/templates/gueterlisten-klassifizierungslog.md` - Güterlisten-Klassifizierungslog
- `assets/templates/bafa-genehmigungsantrag.md` - BAFA-Genehmigungs- und Anfragepaket
- `assets/templates/sanktions-embargo-trefferlog.md` - Sanktions- und Embargo-Trefferlog
- `assets/templates/us-ear-itar-touchpoint.md` - US EAR/ITAR-Touchpoint-Check
- `assets/templates/zolltarif-vzta-antrag.md` - Zolltarif- und vZTA-Antrag
- `assets/templates/zollwert-ursprung-praeferenz.md` - Zollwert, Ursprung und Präferenzmatrix
- `assets/templates/zollverfahren-bewilligungen.md` - Zollverfahren- und Bewilligungsmatrix
- `assets/templates/vub-einfuhr-ausfuhr.md` - VuB-Check Einfuhr/Ausfuhr
- `assets/templates/cbam-emissionsdaten-register.md` - CBAM-Emissionsdatenregister
- `assets/templates/verbrauchsteuer-bewilligung.md` - Verbrauchsteuer-Bewilligungs- und Entlastungscheck
- `assets/templates/antidumping-ausgleichszoll-check.md` - Antidumping- und Ausgleichszollcheck
- `assets/templates/wto-handelspolitik-memo.md` - WTO- und Handelspolitik-Memo
- `assets/templates/awv-bundesbank-meldekalender.md` - AWV-Bundesbank-Meldekalender
- `assets/templates/aml-kyc-sanktions-risk-assessment.md` - AML/KYC- und Sanktions-Risikoanalyse
- `assets/templates/pruefung-ermittlung-sofortplan.md` - Prüfungs- und Ermittlungs-Sofortplan
- `assets/templates/offenlegung-verstoss-plan.md` - Offenlegungs- und Nachholplan
- `assets/templates/presse-krisenkommunikation.md` - Presse- und Krisenkommunikationskarte
- `assets/templates/icp-kontrollsystem.md` - Internal-Compliance-Program-Blueprint

## Offizielle Startquellen

- [BAFA Exportkontrolle](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Allgemeine_Einfuehrung/allgemeine_einfuehrung.html)
- [BAFA Embargos und Namenslistenhinweise](https://www.bafa.de/DE/Aussenwirtschaft/Ausfuhrkontrolle/Embargos/embargos.html)
- [EU Sanctions Map und konsolidierte Finanzsanktionsliste](https://finance.ec.europa.eu/eu-and-world/sanctions-restrictive-measures/overview-sanctions-and-related-resources_en)
- [EU TARIC](https://taxation-customs.ec.europa.eu/customs/common-customs-tariff-cct/tariff-classification-goods/eu-customs-tariff-taric_de)
- [EU CBAM](https://taxation-customs.ec.europa.eu/carbon-border-adjustment-mechanism_en)
- [Deutsche Bundesbank AWV-Zahlungsmeldungen](https://www.bundesbank.de/de/service/meldewesen/aussenwirtschaft-formular-center/zahlungsmeldungen)
- [EU Trade Defence Antidumping](https://policy.trade.ec.europa.eu/enforcement-and-protection/trade-defence/anti-dumping-measures_en)
- [Zoll Verbrauchsteuererhebung](https://www.zoll.de/DE/Der-Zoll/Aufgaben-des-Zolls/Einnahmen-fuer-Deutschland-und-Europa/Verbrauchsteuererhebung/verbrauchsteuererhebung.html)

## Freistehende Leitplanken

- Keine Entscheidung auf Basis eingebauter Altdaten: Sanktionen, Embargos, TARIC, CBAM und AWV werden live oder mit dokumentiertem Abrufstand geprüft.
- Keine Sanktionsfreigabe ohne Trefferlog, Eigentum/Kontrolle, Umgehungsprüfung und Freigabeprozess.
- Keine Exportkontrollfreigabe ohne Produktdaten, technische Spezifikation, Güterlistenprüfung, Endverwendung und Endverwender.
- Keine Zollfreigabe ohne Einreihung, Ursprung, Zollwert, Dokumentencodes und TARIC-Maßnahmen.
- Keine CBAM-Aussage ohne Warencode, Warenmenge, Emissionsdatenquelle und sichtbare Annahmen.
- Bei Prüfung, Anhörung, Durchsuchung, Presseanfrage oder möglichem Verstoß: erst Legal Hold, Zuständigkeiten und Verteidigungsstrategie.

<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 26 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `allgemein` | Einstieg, Schnelltriage und Workflow-Routing im Aussenwirtschaft Zoll Sanktionen-Plugin. Fragt Rolle, Ziel, Fristen, Unterlagen, Risiken und Wunsch-Output ab, schlägt passende Spezial-Skills aus diesem Plugin vor und führt in einen klare... |
| `kompendium-01-aussenwirtschaft-ver-bis-aussenwirtschaft-exp` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 01; bündelt 4 frühere Spezialskills (aussenwirtschaft-versandverfahren-ncts, aussenwirtschaft-zollverfahren-bewilligungen, aussenwirtschaft-distributor-vertrag-exportkontr... |
| `kompendium-02-aussenwirtschaft-aml-bis-aussenwirtschaft-san` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 02; bündelt 4 frühere Spezialskills (aussenwirtschaft-aml-kyc-sanktionen, aussenwirtschaft-finanzsanktionen-eigentum-kontrolle, aussenwirtschaft-sanktionen-embargos, ausse... |
| `kompendium-03-aussenwirtschaft-san-bis-aussenwirtschaft-atl` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 03; bündelt 4 frühere Spezialskills (aussenwirtschaft-sanktionsumgehung-red-flags, aussenwirtschaft-zoll-straf-bussgeld-selbstkorrektur, aussenwirtschaft-zollschuld-entste... |
| `kompendium-04-aussenwirtschaft-baf-bis-aussenwirtschaft-kom` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 04; bündelt 4 frühere Spezialskills (aussenwirtschaft-bafa-genehmigungen, aussenwirtschaft-cbam-co2-zoll, aussenwirtschaft-cbam-zertifikate-kosten, aussenwirtschaft-komman... |
| `kompendium-05-aussenwirtschaft-pas-bis-aussenwirtschaft-ver` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 05; bündelt 4 frühere Spezialskills (aussenwirtschaft-passive-veredelung, aussenwirtschaft-rueckwaren-erlass-erstattung, aussenwirtschaft-technologie-transfer-cloud-downlo... |
| `kompendium-06-aussenwirtschaft-zol-bis-aussenwirtschaft-akt` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 06; bündelt 4 frühere Spezialskills (aussenwirtschaft-zolllager-freilager, aussenwirtschaft-abfallverbringung, aussenwirtschaft-aeo-bewilligung-monitoring, aussenwirtschaf... |
| `kompendium-07-aussenwirtschaft-all-bis-aussenwirtschaft-ant` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 07; bündelt 4 frühere Spezialskills (aussenwirtschaft-allgemeingenehmigung-agg-finder, aussenwirtschaft-antidumping-ausgleich, aussenwirtschaft-antidumping-erstattung-revi... |
| `kompendium-08-aussenwirtschaft-ass-bis-aussenwirtschaft-aus` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 08; bündelt 4 frühere Spezialskills (aussenwirtschaft-asset-freeze-sofortmassnahmen, aussenwirtschaft-atlas-ausfuhranmeldung-check, aussenwirtschaft-audit-trail-freigaben,... |
| `kompendium-09-aussenwirtschaft-awv-bis-aussenwirtschaft-baf` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 09; bündelt 4 frühere Spezialskills (aussenwirtschaft-awv-beteiligungsmeldungen, aussenwirtschaft-awv-bundesbank, aussenwirtschaft-awv-z4-z10-z11-meldungen, aussenwirtscha... |
| `kompendium-10-aussenwirtschaft-baf-bis-aussenwirtschaft-cba` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 10; bündelt 4 frühere Spezialskills (aussenwirtschaft-bafa-nullbescheid-azg, aussenwirtschaft-catch-all-pruefung, aussenwirtschaft-cbam-berichtspflichten-uebergang, aussen... |
| `kompendium-11-aussenwirtschaft-che-bis-aussenwirtschaft-emb` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 11; bündelt 4 frühere Spezialskills (aussenwirtschaft-chemikalien-reach-pic, aussenwirtschaft-cites-artenschutz, aussenwirtschaft-dual-use-forschung-hochschule, aussenwirt... |
| `kompendium-12-aussenwirtschaft-emb-bis-aussenwirtschaft-emb` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 12; bündelt 4 frühere Spezialskills (aussenwirtschaft-embargo-iran, aussenwirtschaft-embargo-myanmar, aussenwirtschaft-embargo-nordkorea, aussenwirtschaft-embargo-russland... |
| `kompendium-13-aussenwirtschaft-emb-bis-aussenwirtschaft-erp` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 13; bündelt 4 frühere Spezialskills (aussenwirtschaft-embargo-syrien, aussenwirtschaft-endverwendung-endverwender-euc, aussenwirtschaft-eori-registrierung-stammdaten, auss... |
| `kompendium-14-aussenwirtschaft-ers-bis-aussenwirtschaft-f-g` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 14; bündelt 4 frühere Spezialskills (aussenwirtschaft-ersatzteile-dual-use, aussenwirtschaft-exporteur-ausfuehrer-anmelder-rollen, aussenwirtschaft-exportkontrolle-dual-us... |
| `kompendium-15-aussenwirtschaft-fin-bis-aussenwirtschaft-icp` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 15; bündelt 4 frühere Spezialskills (aussenwirtschaft-financial-institutions-correspondent-banking, aussenwirtschaft-freiwillige-offenlegung-bafa-zoll, aussenwirtschaft-gu... |
| `kompendium-16-aussenwirtschaft-inc-bis-aussenwirtschaft-kno` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 16; bündelt 4 frühere Spezialskills (aussenwirtschaft-incoterms-exportkontrolle, aussenwirtschaft-internal-investigation-aussenwirtschaft, aussenwirtschaft-investitionspru... |
| `kompendium-17-aussenwirtschaft-kon-bis-aussenwirtschaft-leb` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 17; bündelt 4 frühere Spezialskills (aussenwirtschaft-kontingente-lizenzen-trq, aussenwirtschaft-kritische-infrastruktur-investment, aussenwirtschaft-kulturgut-einfuhr-aus... |
| `kompendium-18-aussenwirtschaft-leg-bis-aussenwirtschaft-ma` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 18; bündelt 4 frühere Spezialskills (aussenwirtschaft-legal-hold-datenextraktion, aussenwirtschaft-lieferanten-onboarding-aussenhandel, aussenwirtschaft-lieferkettensorgfa... |
| `kompendium-19-aussenwirtschaft-nic-bis-aussenwirtschaft-pra` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 19; bündelt 4 frühere Spezialskills (aussenwirtschaft-nichtpraeferenzieller-ursprung-made-in, aussenwirtschaft-ofac-sdn-non-sdn, aussenwirtschaft-post-merger-icp-integrati... |
| `kompendium-20-aussenwirtschaft-pre-bis-aussenwirtschaft-ree` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 20; bündelt 4 frühere Spezialskills (aussenwirtschaft-presse-krise, aussenwirtschaft-produktsicherheit-vub-schnittstelle, aussenwirtschaft-pruefung-ermittlung, aussenwirts... |
| `kompendium-21-aussenwirtschaft-sam-bis-aussenwirtschaft-scr` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 21; bündelt 4 frühere Spezialskills (aussenwirtschaft-sammelgenehmigung-export, aussenwirtschaft-schulung-exportkontrolle-rollout, aussenwirtschaft-schutzmassnahmen-safegu... |
| `kompendium-22-aussenwirtschaft-sof-bis-aussenwirtschaft-tra` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 22; bündelt 4 frühere Spezialskills (aussenwirtschaft-software-verschluesselung-kryptografie, aussenwirtschaft-swiss-sanctions-touchpoint, aussenwirtschaft-trade-finance-l... |
| `kompendium-23-aussenwirtschaft-uk-bis-aussenwirtschaft-vub` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 23; bündelt 4 frühere Spezialskills (aussenwirtschaft-uk-sanctions-touchpoint, aussenwirtschaft-us-ear-itar, aussenwirtschaft-voruebergehende-verwendung-ata-carnet, aussen... |
| `kompendium-24-aussenwirtschaft-vzt-bis-aussenwirtschaft-zol` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 24; bündelt 4 frühere Spezialskills (aussenwirtschaft-vzta-antrag-qualitaetsgate, aussenwirtschaft-warennummer-hs-cn-taric-einreihung, aussenwirtschaft-wto-handelspolitik,... |
| `kompendium-25-aussenwirtschaft-zol-bis-aussenwirtschaft-zol` | aussenwirtschaft-zoll-sanktionen: Konsolidiertes Skill-Kompendium 25; bündelt 3 frühere Spezialskills (aussenwirtschaft-zolltarif-vzta, aussenwirtschaft-zollwert-royalties-assists, aussenwirtschaft-zollwert-ursprung) und bewahrt deren Wo... |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
