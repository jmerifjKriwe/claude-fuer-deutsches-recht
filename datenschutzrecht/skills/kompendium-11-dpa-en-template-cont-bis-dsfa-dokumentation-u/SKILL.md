---
name: kompendium-11-dpa-en-template-cont-bis-dsfa-dokumentation-u
description: "datenschutzrecht: Konsolidiertes Skill-Kompendium 11; bündelt 10 frühere Spezialskills (dpa-en-template-controller-processor, dpa-en-tom-annex-template, dpia-en-summary-for-management, dpia-en-template-full-version, drittlandstransfer-pruefung und 5 weitere) und bewahrt deren Workflows, Normanker, Prüfprogramme und Ausgabemuster."
---

# Kompendium 11 - datenschutzrecht

## Zweck

Dieser Skill bündelt frühere Einzelskills dieses Plugins. Er ist bewusst länger: Die Nutzerin soll nicht zwischen vielen fast benachbarten Skills suchen müssen, sondern in einem Kompendium ein vollständiges Prüf-, Workflow- und Ausgabeprogramm finden.

## Enthaltene frühere Skills

| Früherer Skill | Frühere Beschreibung |
| --- | --- |
| `dpa-en-template-controller-processor` | English language Data Processing Agreement (DPA) template under Article 28 GDPR between a controller and a processor. Use when the contract language is English (cross-border deals UK Ireland US providers) and the parties require a stand-alone DPA. Output is a complete English DPA template covering all eight mandatory items of Article 28 (3) GDPR. |
| `dpa-en-tom-annex-template` | English language technical and organisational measures (TOM) annex template for a DPA under Article 32 GDPR. Covers pseudonymisation encryption confidentiality integrity availability resilience recoverability and regular testing. Output: complete English TOM annex template suitable for ISO 27001 SOC 2 and BSI C5 alignment. |
| `dpia-en-summary-for-management` | Concise English DPIA management summary aligned with Art. 35 GDPR for board executive committee or non-legal stakeholders. Output: one-pager covering processing necessity risk measures residual risk approval recommendation. |
| `dpia-en-template-full-version` | Full English DPIA template aligned with Art. 35 GDPR covering description necessity proportionality risk to data subjects measures residual risk approval. Output: ready-to-fill DPIA template in English for cross-border or English-speaking deployments. |
| `drittlandstransfer-pruefung` | Datentransfer in Drittlaender außerhalb EU und EWR auf Zulässigkeit prüfen. Art. 44 ff. DSGVO Kapitel V Drittlandstransfer. Prüfraster: Angemessenheitsbeschluss SCC BCR Schrems-II-Folgen Transfer Impact Assessment zusaetzliche Massnahmen. Output: Drittlandstransfer-Prüfmemo TIA-Vorlage. Abgrenzung: nicht für innereuroaeischen Datenaustausch. |
| `drittlandtransfer-behoerdenpaket-output` | Behördenfähiges Dokumentations- und Antwortpaket für Drittlandtransfers erstellen: Deckvermerk, Transferregister, DPF/SCC/TIA-Nachweise, TOMs, Subprozessoren, Maßnahmenplan und Antwort an deutsche Datenschutzaufsicht. |
| `dsb-bestellungspflicht-pruefung` | Bestellungspflicht für Datenschutzbeauftragten prüfen. Art. 37 DSGVO § 38 BDSG Bestellungspflicht. Prüfraster: Schwellenwerte Art. 37 Abs. 1 Betriebsgroe Verarbeitungsart Pflichtbestellung freiwillige Bestellung. Output: Bestellungsprüfmemo Empfehlung. Abgrenzung: nicht für Aufgaben des DSB (Art. 39 DSGVO). |
| `dsfa-art-35-dsgvo-trigger-und-anwendungsbereich` | Pruefung wann eine DSFA nach Art. 35 DSGVO ueberhaupt erforderlich ist. Trigger-Pruefung Anwendungsbereich Schwellwert. Generalklausel Art. 35 Abs. 1 voraussichtlich hohes Risiko; Regelbeispiele Art. 35 Abs. 3; Pflichtlisten Art. 35 Abs. 4 BfDI. Output: Triage-Vermerk DSFA-pflichtig oder nicht. |
| `dsfa-bfdi-und-laender-blacklist` | Abgleich einer Verarbeitung mit der BfDI-Pflichtliste nach Art. 35 Abs. 4 DSGVO und mit den Listen der Landesdatenschutzbehoerden. Output: dokumentierter Listenabgleich mit Trefferanalyse und ggf. Verweis auf zwingende DSFA. |
| `dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii` | Dokumentation der DSFA als Beleg der Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO: Aktenstruktur Versionierung Aufbewahrung Beweiswert. Output: DSFA-Akte mit Aktenuebersicht und Aufbewahrungsregeln. |

## Arbeitsregel

1. Zuerst den passenden Unterabschnitt anhand des früheren Skillnamens oder des Sachthemas auswählen.
2. Danach die dortige Prüfroutine, Normen-/Quellenanker, Beweislogik und Output-Vorgabe vollständig anwenden.
3. Bei mehreren passenden Unterabschnitten eine kurze Synopse bilden und Widersprüche offen markieren.
4. Rechtsprechung, Literatur, Behördenpraxis und Tagesrecht nur mit überprüfbarer Quelle oder Nutzerquelle ausgeben.

## Konsolidierte Inhalte

## 1. `dpa-en-template-controller-processor`

**Frühere Beschreibung:** English language Data Processing Agreement (DPA) template under Article 28 GDPR between a controller and a processor. Use when the contract language is English (cross-border deals UK Ireland US providers) and the parties require a stand-alone DPA. Output is a complete English DPA template covering all eight mandatory items of Article 28 (3) GDPR.

# Data Processing Agreement (DPA) – English Template Controller / Processor

## Zweck / Purpose

English-language DPA template under Article 28 GDPR for cross-border deals where the working language is English (UK/IE counterparties, US providers, EU multinationals). Purpose (DE): Englischsprachige Mustervorlage fuer einen Auftragsverarbeitungsvertrag nach Art. 28 DSGVO.

## Wann brauchen Sie diesen Skill

- Cross-border deal where one party requires English contract language.
- US or UK SaaS / cloud provider is the processor.
- Multinational client requires a single DPA across multiple EU subsidiaries.
- DPA needs to be aligned with EU SCC modules (Decision (EU) 2021/914) for transfers outside the EEA.

## Rechtlicher Rahmen

- Article 28 GDPR – Processor obligations.
- Article 28 (3) (a)-(h) GDPR – Eight mandatory contractual items.
- Article 32 GDPR – Technical and organisational measures.
- Article 33-34 GDPR – Personal data breach notification.
- Decision (EU) 2021/914 of 04 June 2021 – Standard Contractual Clauses for international transfers (in force since 27 June 2021).
- Decision (EU) 2021/915 of 04 June 2021 – Standard Contractual Clauses for the controller-processor relationship inside the EEA.
- UK GDPR – International Data Transfer Agreement (IDTA) where UK personal data is in scope.

## Ablauf / Checkliste

1. Define the parties: Controller, Processor.
2. Annex the description of processing (Annex I).
3. Annex the technical and organisational measures (Annex II).
4. Annex the list of approved sub-processors (Annex III).
5. Identify cross-border transfers and pair the DPA with the appropriate SCC module.
6. Define liability cap, indemnities and audit rights consistent with the playbook.
7. Sign in two counterparts; electronic signature is permitted under Article 28 (9) GDPR.

## Mustertext / Template

```
DATA PROCESSING AGREEMENT

This Data Processing Agreement ("DPA") forms part of and is incorporated into the
Main Agreement entered into between:

  (1) [Controller Legal Name], a company organised under the laws of [jurisdiction],
      with its registered office at [address] ("Controller"); and

  (2) [Processor Legal Name], a company organised under the laws of [jurisdiction],
      with its registered office at [address] ("Processor").

The Controller and the Processor are each a "Party" and together the "Parties".

1. DEFINITIONS
1.1 "GDPR" means Regulation (EU) 2016/679.
1.2 "Personal Data", "Processing", "Data Subject", "Sub-processor" and "Supervisory
    Authority" shall have the meanings ascribed to them in Article 4 GDPR.
1.3 "Annex" means an annex to this DPA which forms an integral part hereof.

2. SCOPE AND ROLES
2.1 The subject matter, duration, nature and purpose of the Processing, the types
    of Personal Data and the categories of Data Subjects are set out in Annex I.
2.2 The Controller is the controller and the Processor is the processor within the
    meaning of Article 4 (7) and (8) GDPR.

3. PROCESSING ON DOCUMENTED INSTRUCTIONS (Art. 28 (3) (a) GDPR)
3.1 The Processor shall process the Personal Data only on documented instructions
    from the Controller, including with regard to transfers of Personal Data to
    a third country or an international organisation, unless required to do so by
    Union or Member State law.
3.2 The Processor shall immediately inform the Controller if, in its opinion, an
    instruction infringes the GDPR or other applicable data protection provisions.

4. CONFIDENTIALITY (Art. 28 (3) (b) GDPR)
4.1 The Processor shall ensure that persons authorised to process the Personal Data
    have committed themselves to confidentiality or are under an appropriate
    statutory obligation of confidentiality.

5. SECURITY OF PROCESSING (Art. 28 (3) (c), Art. 32 GDPR)
5.1 The Processor shall implement the technical and organisational measures set
    out in Annex II.

6. SUB-PROCESSING (Art. 28 (2), (4) GDPR)
6.1 The Processor shall not engage any sub-processor without the prior written
    authorisation of the Controller. General authorisation is granted for the
    sub-processors listed in Annex III.
6.2 The Processor shall inform the Controller of any intended changes concerning
    the addition or replacement of sub-processors at least thirty (30) days in
    advance, giving the Controller the opportunity to object.

7. ASSISTANCE WITH DATA SUBJECT RIGHTS (Art. 28 (3) (e) GDPR)
7.1 The Processor shall assist the Controller, by appropriate technical and
    organisational measures and insofar as this is possible, in the fulfilment of
    the Controller's obligation to respond to requests under Chapter III GDPR.

8. ASSISTANCE WITH SECURITY, BREACHES AND DPIA (Art. 28 (3) (f) GDPR)
8.1 The Processor shall notify the Controller without undue delay and in any event
    within forty-eight (48) hours after becoming aware of a Personal Data breach.

9. RETURN OR DELETION (Art. 28 (3) (g) GDPR)
9.1 Upon termination of the provision of services relating to Processing, the
    Processor shall, at the choice of the Controller, delete or return all the
    Personal Data and delete existing copies unless Union or Member State law
    requires storage of the Personal Data.

10. AUDIT AND INSPECTION (Art. 28 (3) (h) GDPR)
10.1 The Processor shall make available to the Controller all information necessary
     to demonstrate compliance with this DPA and Article 28 GDPR, and allow for and
     contribute to audits, including inspections, conducted by the Controller or
     another auditor mandated by the Controller, no more than once per calendar
     year, save in case of a Personal Data breach.

11. INTERNATIONAL TRANSFERS
11.1 Where Personal Data is transferred outside the EEA, the Parties shall enter
     into the relevant module of the EU Standard Contractual Clauses adopted by
     Commission Implementing Decision (EU) 2021/914 of 04 June 2021.

12. LIABILITY (Art. 82 GDPR)
12.1 Each Party shall be liable in accordance with Article 82 GDPR.

13. TERM AND TERMINATION
13.1 This DPA shall remain in force for the term of the Main Agreement.

14. GOVERNING LAW AND JURISDICTION
14.1 This DPA shall be governed by the laws of [jurisdiction] and the courts of
     [court venue] shall have exclusive jurisdiction.

Annex I  Description of Processing
Annex II Technical and Organisational Measures
Annex III List of Sub-processors

Signed on behalf of the Controller:        Signed on behalf of the Processor:
__________________________________         __________________________________
Name:                                       Name:
Title:                                      Title:
Date:                                       Date:
```

## Typische Drafting-Fehler

- "Controller" and "Processor" labels swapped relative to the actual processing reality.
- Annexes left blank or filled with marketing language.
- Sub-processor notice periods shorter than necessary to exercise meaningful objection rights.
- Liability caps that contradict Article 82 GDPR statutory liability.
- Audit clauses limited to certifications without a residual on-site right.
- Cross-border transfers covered only by general references; SCC module not actually executed.

## Querverweise

- `datenschutzrecht/skills/dpa-en-tom-annex-template/SKILL.md`
- `datenschutzrecht/skills/avv-eu-kommission-musterklauseln-2021-915/SKILL.md`
- `datenschutzrecht/skills/avv-eu-us-data-privacy-framework-bezug/SKILL.md`
- `datenschutzrecht/skills/dpa-en-controller-controller-tmpl/SKILL.md`

## Quellen Stand 06/2026

- Article 28 GDPR – Regulation (EU) 2016/679.
- Commission Implementing Decision (EU) 2021/914 of 04 June 2021, OJ L 199/31 of 07 June 2021.
- Commission Implementing Decision (EU) 2021/915 of 04 June 2021, OJ L 199/18 of 07 June 2021.
- EDPB Guidelines 07/2020 on the concepts of controller and processor in the GDPR, adopted 07 July 2021.
- Citation rules: `../../../references/zitierweise.md`.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 2. `dpa-en-tom-annex-template`

**Frühere Beschreibung:** English language technical and organisational measures (TOM) annex template for a DPA under Article 32 GDPR. Covers pseudonymisation encryption confidentiality integrity availability resilience recoverability and regular testing. Output: complete English TOM annex template suitable for ISO 27001 SOC 2 and BSI C5 alignment.

# TOM Annex – English Template (Article 32 GDPR)

## Zweck / Purpose

English-language annex template setting out the technical and organisational measures (TOM) required under Article 32 GDPR and incorporated by reference into the DPA. Purpose (DE): Englischsprachige TOM-Anlage zum DPA nach Art. 32 DSGVO.

## Wann brauchen Sie diesen Skill

- Cross-border or English-language DPA needs a TOM annex.
- Processor offers ISO 27001 / SOC 2 / BSI C5 alignment and the annex must reflect this.
- Periodic refresh of the TOM annex is due (recommended annually).

## Rechtlicher Rahmen

- Article 32 (1) (a) GDPR – Pseudonymisation and encryption.
- Article 32 (1) (b) GDPR – Ongoing confidentiality, integrity, availability, resilience.
- Article 32 (1) (c) GDPR – Ability to restore availability and access in a timely manner.
- Article 32 (1) (d) GDPR – Process for regularly testing, assessing and evaluating effectiveness.
- Article 25 GDPR – Data protection by design and by default.

## Ablauf / Checkliste

1. Confirm the processing risk profile.
2. Map measures against Article 32 (1) (a)-(d) GDPR.
3. Reference certifications (ISO 27001, SOC 2, BSI C5).
4. Define test cadence (penetration testing, vulnerability scanning).
5. Ensure sub-processor measures are consistent (Article 28 (4) GDPR).
6. Sign annex with date stamp; refresh annually or upon material change.

## Mustertext / Template

```
ANNEX II TO THE DATA PROCESSING AGREEMENT
TECHNICAL AND ORGANISATIONAL MEASURES (Article 32 GDPR)

Effective date: [DATE]
Processor: [NAME]
Review cycle: annually and upon material change

1. PSEUDONYMISATION (Art. 32 (1) (a) GDPR)
   1.1 Personal data shall be pseudonymised in development and test environments.
   1.2 The mapping table shall be stored separately, with access limited to the
       Data Protection Officer.

2. ENCRYPTION (Art. 32 (1) (a) GDPR)
   2.1 In transit: TLS 1.3 with forward secrecy, configured in accordance with
       industry guidance (e.g. BSI TR-02102 or NIST SP 800-52 Rev. 2).
   2.2 At rest: AES-256 (CBC or GCM) for all databases and backups.
   2.3 Key management: hardware security module (HSM) or equivalent; keys rotated
       at least annually.

3. CONFIDENTIALITY (Art. 32 (1) (b) GDPR)
   3.1 Physical access controls: 24/7 guarded data centres with multi-factor
       physical access.
   3.2 Logical access: multi-factor authentication for all privileged accounts.
   3.3 Authorisation: role-based access control on a least-privilege basis;
       periodic recertification.
   3.4 Segregation: multi-tenant logical separation with tenant-scoped access
       control.

4. INTEGRITY (Art. 32 (1) (b) GDPR)
   4.1 Transfer controls: documented interfaces; audit logging of all data
       exports.
   4.2 Input controls: write-operation logging with attribution to authenticated
       identities.
   4.3 Hashing: SHA-256 or stronger for integrity verification.

5. AVAILABILITY AND RESILIENCE (Art. 32 (1) (b) GDPR)
   5.1 Backups: daily incremental, weekly full; retention thirty (30) days.
   5.2 Recovery Point Objective (RPO): twenty-four (24) hours or less.
   5.3 Recovery Time Objective (RTO): eight (8) hours or less for critical
       processing.
   5.4 Geographic redundancy: synchronous replication across at least two EEA
       data centres.
   5.5 DDoS protection: upstream filtering with provider SLA.

6. RECOVERABILITY (Art. 32 (1) (c) GDPR)
   6.1 Incident response runbook; tabletop exercises at least annually.
   6.2 Documented restoration procedures.
   6.3 Restoration drills with actual data restoration tests at least semi-annually.

7. REGULAR TESTING (Art. 32 (1) (d) GDPR)
   7.1 Independent third-party penetration testing at least annually.
   7.2 Vulnerability scanning monthly.
   7.3 Internal ISMS audits annually; external ISO 27001 audits annually.
   7.4 TOM annex review at least annually.

8. ORGANISATIONAL MEASURES
   8.1 Data Protection Officer designated; contact details in Annex IV.
   8.2 Confidentiality undertakings from all personnel processing personal data
       (Article 28 (3) (b) GDPR).
   8.3 Annual data protection training with attendance records.
   8.4 Joiner-mover-leaver process; immediate revocation of access on exit.
   8.5 Incident response procedure with notification to the Controller within
       forty-eight (48) hours of becoming aware of a personal data breach
       (Article 33 GDPR).

9. CERTIFICATIONS AND STANDARDS
   9.1 ISO/IEC 27001:2022 – certified on [DATE] by [BODY].
   9.2 BSI C5:2020 Type 2 – report dated [DATE].
   9.3 SOC 2 Type II – report period [PERIOD].

10. SUB-PROCESSORS
    10.1 Sub-processors are required to implement measures at least equivalent
         to those set out in this Annex II (Article 28 (4) GDPR).
    10.2 Sub-processor audit reports shall be provided to the Controller on
         request.

Signed by:                                  Date:
________________________________            ____________________________
[Processor representative]
```

## Typische Drafting-Fehler

- Marketing copy instead of concrete measures.
- "State of the art" without specifics.
- No update since initial signing.
- Pseudonymisation omitted, even though Article 32 (1) (a) GDPR mentions it.
- No RPO/RTO.
- No test cadence.
- Sub-processor consistency not addressed.

## Querverweise

- `datenschutzrecht/skills/avv-tom-art-32-dsgvo-anlage/SKILL.md`
- `datenschutzrecht/skills/dpa-en-template-controller-processor/SKILL.md`
- `datenschutzrecht/skills/avv-audit-und-kontrollrechte/SKILL.md`
- `datenschutzrecht/skills/avv-cloud-und-subverarbeitung-art-28-iv/SKILL.md`

## Quellen Stand 06/2026

- GDPR Article 25, Article 28 (3) (c), Article 32, Article 33.
- BSI TR-02102 (cryptographic guidance).
- NIST SP 800-52 Rev. 2.
- ISO/IEC 27001:2022.
- BSI C5:2020.
- SOC 2 Trust Services Criteria (AICPA, 2017, as amended).
- Citation rules: `../../../references/zitierweise.md`.
```


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 3. `dpia-en-summary-for-management`

**Frühere Beschreibung:** Concise English DPIA management summary aligned with Art. 35 GDPR for board executive committee or non-legal stakeholders. Output: one-pager covering processing necessity risk measures residual risk approval recommendation.

# DPIA Management Summary in English

## Purpose

Concise English-language management summary of a Data Protection Impact Assessment (DPIA) under Art. 35 GDPR. Designed for board members, executive committees, group risk officers and other non-legal stakeholders who require a defensible one-pager rather than the full DPIA document. The summary follows the six-step methodology and ends with an explicit approval recommendation.

## When to use

- When a DPIA is on the agenda of a board, executive committee or steering committee
- For investor due diligence covering high-risk processing
- For internal audit and group risk reporting in English
- For exchange with English-speaking parent companies, joint controllers or processors
- For cross-border consultation drafts that later are translated into national language

## Legal framework

- Art. 35(7) GDPR mandatory content of a DPIA
- Art. 35(2) GDPR DPO consultation
- Art. 36 GDPR prior consultation if residual risk remains high
- Art. 5(2) GDPR accountability principle
- EDPB Guidelines WP 248 rev.01 on DPIA
- For AI-related processing: Regulation (EU) 2024/1689 Art. 26 and Art. 27

## 6-step structure of the management summary

1. **Description of processing.** One paragraph: purpose, data, subjects, technology, transfers.
2. **Necessity and proportionality assessment.** One paragraph: legal basis, minimisation, alternatives.
3. **Risk to data subjects.** Short risk table with the top scenarios.
4. **Measures to mitigate risk.** Short list of key measures.
5. **Residual risk.** Risk rating before and after measures.
6. **Approval recommendation.** Approve, approve with conditions, prior consultation under Art. 36, do not approve.

## Template (English management summary)

```
DPIA MANAGEMENT SUMMARY
Confidential — for internal management use

Reference: [DPIA-YYYY-NN]
Date: [DD-MM-YYYY]
Controller: [Entity, legal representative]
DPO: [Name, contact]

1. PROCESSING IN ONE PARAGRAPH
[What is processed, for what purpose, on which legal basis, for which categories of data subjects, with which key technology, including transfers to third countries.]

2. NECESSITY AND PROPORTIONALITY
- Legal basis: [Art. 6 / Art. 9 GDPR with national law]
- Data minimisation: [Brief assessment]
- Less intrusive alternatives considered: [Yes / No, with note]
- Storage period: [Period, justification]
- Data subject rights: [Implemented mechanisms]

3. TOP RISKS TO DATA SUBJECTS (BEFORE MEASURES)
| Scenario                          | Likelihood | Severity | Rating |
| Unauthorised access               | [h/m/l]    | [h/m/l]  | [R/O/Y/G] |
| Covert profiling                  |            |          |        |
| Data leakage / transfer exposure  |            |          |        |
| Discrimination of data subjects   |            |          |        |
| Identity theft / fraud            |            |          |        |

4. KEY MEASURES
- Technical: [encryption, pseudonymisation, access control, logging, key management]
- Organisational: [training, four-eyes principle, authorisation concept, incident response]
- Contractual: [DPA Art. 28, SCC for transfers, TIA]
- AI-specific (if applicable): [human oversight, logging Art. 26(6) AI Act, transparency Art. 50 AI Act]

5. RESIDUAL RISK
| Scenario                          | Rating after measures |
| Unauthorised access               | [R/O/Y/G]             |
| Covert profiling                  |                       |
| ...                               |                       |

Overall residual risk: [HIGH / MEDIUM / LOW]

6. APPROVAL RECOMMENDATION
[ ] Approve — proceed with processing
[ ] Approve with conditions — see action items
[ ] Prior consultation under Art. 36 GDPR required
[ ] Do not approve — redesign processing

Action items
| No | Action | Owner | Deadline |

Next review: [DATE]

Sign-off
Controller representative: ____________________ Date: ____________________
DPO: ____________________ Date: ____________________
```

## Typical mistakes

- Management summary uses different wording than the full DPIA — inconsistency creates legal risk.
- Risk table is reduced to a single rating without scenarios — board cannot challenge.
- Approval recommendation is hidden in narrative — should be a binary choice.
- DPO opinion is not referenced — looks like a controller-only decision.
- Cross-border or AI specifics omitted in the summary even though they are key in the full DPIA.
- No action items with owner and deadline — recommendation is not actionable.
- Confidentiality classification missing — risk of unintended disclosure.

## Cross-references

- `datenschutzrecht/skills/dpia-en-template-full-version/SKILL.md` — Full English DPIA template
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — German full template
- `datenschutzrecht/skills/dsfa-restrisiko-und-art-36-konsultation/SKILL.md` — Art. 36 procedure
- `datenschutzrecht/skills/dsfa-fuer-internationale-datentransfers/SKILL.md` — Transfers
- `datenschutzrecht/skills/dsfa-fuer-ki-systeme-schnittstelle-art-26-kivo/SKILL.md` — AI interface
- `references/zitierweise.md` — Citation rules

## Sources as of 06/2026

- Art. 5(2), 35, 36 GDPR
- Regulation (EU) 2024/1689 (AI Act), Art. 26 and 27
- EDPB Guidelines WP 248 rev.01 on DPIA
- EDPB Opinion 28/2024 on AI models
- Case law: do not cite from model knowledge; verify with official sources
- Literature: only cite from user-provided source or licensed live access


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 4. `dpia-en-template-full-version`

**Frühere Beschreibung:** Full English DPIA template aligned with Art. 35 GDPR covering description necessity proportionality risk to data subjects measures residual risk approval. Output: ready-to-fill DPIA template in English for cross-border or English-speaking deployments.

# DPIA Full Template in English

## Purpose

Complete English-language Data Protection Impact Assessment template aligned with Art. 35 GDPR. All six sections required by Art. 35(7) GDPR are pre-filled with placeholders so that a controller can populate the document and submit it to the data protection officer (DPO) or the supervisory authority. The template follows the methodological structure description, necessity and proportionality, risk to data subjects, measures, residual risk, approval.

## When to use

- After a positive DPIA threshold assessment
- When the processing involves English-speaking deployments, joint controllers in the EU and outside the EU, or English documentation requirements
- Before a prior consultation under Art. 36 GDPR with an English-language file
- When the in-house format is missing and a defensible standard template is needed

## Legal framework

- Art. 35(7) GDPR minimum content of a DPIA:
  - lit. a systematic description of processing operations and purposes
  - lit. b assessment of necessity and proportionality
  - lit. c assessment of risk to rights and freedoms of data subjects
  - lit. d measures envisaged to address the risk, including safeguards, security measures and mechanisms
- Art. 35(2) GDPR DPO consultation
- Art. 35(9) GDPR consultation of data subjects or their representatives where appropriate
- Art. 5(2) GDPR accountability
- EDPB Guidelines WP 248 rev.01 on DPIA

## 6-step methodology

1. **Description of processing.** Populate Section 1.
2. **Necessity and proportionality assessment.** Section 2.
3. **Risk to data subjects.** Section 3 with risk matrix.
4. **Measures to mitigate risk.** Section 4.
5. **Residual risk.** Section 5.
6. **Approval.** Section 6 with signatures.

## Template (English Full DPIA)

```
DATA PROTECTION IMPACT ASSESSMENT (DPIA)
pursuant to Article 35 GDPR

Internal reference: [...]
Version: [1.0] | Date: [DD-MM-YYYY]
Controller: [Legal entity, address, legal representative]
DPO: [Name, e-mail, phone]
Lead department: [...]
Classification: [confidential / internal]

COVER PAGE
Processing activity: [Designation]
Legal basis: [Art. 6 / Art. 9 GDPR, plus national law if applicable]
Competent supervisory authority: [BfDI / state DPA / lead authority Art. 56]
Version history: [...]

EXECUTIVE SUMMARY (one page)
Purpose: [...]
Categories of data: [...]
Data subjects: [...]
Overall risk before measures: [HIGH / MEDIUM / LOW]
Overall risk after measures: [HIGH / MEDIUM / LOW]
Approval recommendation: [Approved / Prior consultation Art. 36 / Not approved]

1. DESCRIPTION OF PROCESSING
   (Art. 35(7)(a) GDPR)
1.1 Purpose and nature of processing
[...]
1.2 Categories of personal data
- Identification data: [...]
- Content data: [...]
- Usage data: [...]
- Special categories Art. 9 GDPR: [...]
- Criminal data Art. 10 GDPR: [...]
1.3 Categories of data subjects
[Customers / Employees / Patients / Citizens]
1.4 Recipients and transfers
- Internal recipients: [...]
- External processors: [...]
- Third country transfers: [Country, safeguards under Chapter V]
1.5 Retention periods
[Period, deletion concept]
1.6 Technical environment
[Hosting, sub-processors, encryption baseline]
1.7 Data flow
[Diagram reference or short narrative]

2. NECESSITY AND PROPORTIONALITY ASSESSMENT
   (Art. 35(7)(b) GDPR)
2.1 Necessity of processing for purpose
[Suitable, necessary, no less intrusive means]
2.2 Data minimisation Art. 5(1)(c) GDPR
[...]
2.3 Purpose limitation Art. 5(1)(b) GDPR
[...]
2.4 Storage limitation Art. 5(1)(e) GDPR
[...]
2.5 Lawfulness Art. 6 / Art. 9 GDPR
[Legal basis per category of data and category of data subject]
2.6 Rights of data subjects
[How are access, rectification, erasure, restriction, portability, objection ensured?]
2.7 Transparency Art. 12 et seq. GDPR
[...]

3. RISK TO DATA SUBJECTS
   (Art. 35(7)(c) GDPR)
3.1 Risk matrix before measures
| No | Scenario                          | Likelihood | Severity | Risk |
|----|-----------------------------------|------------|----------|------|
| 1  | Unauthorised access (confid.)     | [h/m/l]    | [h/m/l]  | [R/O/Y/G] |
| 2  | Data leakage to outside           |            |          |      |
| 3  | Covert profiling                  |            |          |      |
| 4  | Data loss / availability          |            |          |      |
| 5  | Manipulation / integrity          |            |          |      |
| 6  | Discrimination of data subjects   |            |          |      |
| 7  | Identity theft                    |            |          |      |
3.2 Protection goals touched
[Confidentiality / Integrity / Availability / Transparency / Intervenability / Unlinkability / Data minimisation]
3.3 Vulnerable data subjects
[Children / Patients / Employees / Consumers]

4. MEASURES TO MITIGATE RISK
   (Art. 35(7)(d) GDPR)
4.1 Technical measures (Art. 32 GDPR)
- Encryption: [type, key length]
- Pseudonymisation: [...]
- Access control: [role / rights concept]
- Logging: [...]
- Backup and restore: [...]
- State of the art: [...]
4.2 Organisational measures
- Training: [target group, frequency]
- Four-eyes principle: [...]
- Authorisation concept: [...]
- Incident response plan: [...]
4.3 Contractual measures
- Data processing agreement (Art. 28 GDPR): [Processor, date, version]
- Standard Contractual Clauses for transfers: [Module, date]
- Transfer impact assessment (TIA): [Reference]
4.4 Measures table
| No | Risk | Measure | Owner | Deadline | Residual risk |

5. RESIDUAL RISK
5.1 Risk matrix after measures
[Table as 3.1 with values after measures]
5.2 Assessment of residual risk
[Remaining risk per scenario, overall rating]
5.3 Need for prior consultation Art. 36 GDPR
[ ] No consultation required (residual risk medium or low)
[ ] Prior consultation required (residual risk high)

6. CONSULTATION AND APPROVAL
6.1 DPO opinion (Art. 35(2) GDPR)
[Wording or reference to annex]
DPO signature: ____________________ Date: ____________________

6.2 Consultation of data subjects (Art. 35(9) GDPR)
[Performed / not performed with justification]

6.3 Approval by controller
Name: ____________________
Role: ____________________
Signature: ____________________ Date: ____________________

6.4 Inclusion in records of processing Art. 30 GDPR
Reference: [...]

6.5 Review plan Art. 35(11) GDPR
Next review: [DATE]
Triggers for ad-hoc review: [change of data categories / recipients / technology / law]
```

## Typical mistakes

- Section 1 stays generic without an actual data flow description.
- Necessity assessment is reduced to legal basis; data minimisation and storage limitation are ignored.
- Risk scenarios only cover confidentiality; other protection goals are left blank.
- Measures table without owner and deadline — not steerable.
- DPO signs late or not at all — evidentiary gap.
- No version control — changes are not traceable.

## Cross-references

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — German full template
- `datenschutzrecht/skills/dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden/SKILL.md` — Risk methodology
- `datenschutzrecht/skills/dpia-en-summary-for-management/SKILL.md` — English management summary
- `datenschutzrecht/skills/dsfa-fuer-internationale-datentransfers/SKILL.md` — International transfers
- `references/zitierweise.md` — Citation rules

## Sources as of 06/2026

- Art. 35(2), (7), (9), (11) GDPR
- Art. 5(2), 30, 32 GDPR
- EDPB Guidelines WP 248 rev.01
- SDM V3.0 (German Standard Data Protection Model) — protection goals
- Case law: do not cite from model knowledge; verify with official sources
- Literature: only cite from user-provided source or licensed live access


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 5. `drittlandstransfer-pruefung`

**Frühere Beschreibung:** Datentransfer in Drittlaender außerhalb EU und EWR auf Zulässigkeit prüfen. Art. 44 ff. DSGVO Kapitel V Drittlandstransfer. Prüfraster: Angemessenheitsbeschluss SCC BCR Schrems-II-Folgen Transfer Impact Assessment zusaetzliche Massnahmen. Output: Drittlandstransfer-Prüfmemo TIA-Vorlage. Abgrenzung: nicht für innereuroaeischen Datenaustausch.

# Drittlandstransfer-Prüfung (Art. 44 ff. DSGVO)

## Zweck

Dieser Skill greift bei jeder Auslagerung personenbezogener Daten an Empfänger außerhalb der EU/des EWR: US-Cloud-Dienste, Konzernverbund-Transfer, KI-Provider, Sub-Auftragsverarbeiter in Drittstaaten. Er führt strukturiert durch die mehrstufige Prüfung gemäß Kapitel V DSGVO, berücksichtigt den Angemessenheitsbeschluss vom 10. Juli 2023 für die USA (EU-US Data Privacy Framework) sowie die Schrems-II-Anforderungen an Standardvertragsklauseln und ergänzende Maßnahmen.

Anwendungsfälle: Kanzlei oder Unternehmen moechte einen US-amerikanischen SaaS-Dienst einsetzen; Konzernmutter in der Schweiz soll Zugriff auf EU-Kundendaten erhalten; Auftragsverarbeiter setzt Sub-Auftragsverarbeiter in Indien ein; Drittlandbezug bei AVV-Prüfung erkannt.

## Eingaben

- Empfängerstaat (z.B. USA, Indien, UK, China)
- Empfänger: Verantwortlicher (Modul 1/3 SCC) oder Auftragsverarbeiter (Modul 2/4 SCC)
- Datenkategorien (Art. 4 Nr. 1 DSGVO; Art. 9/10 DSGVO-Sonderkategorien?)
- Art der Datenverarbeitung (Speicherung, Analyse, Support-Zugriff, Hosting, Backup)
- Liegt bereits ein Transfer Impact Assessment vor? Falls ja, als Dokument einreichen
- Sitz und DPF-Zertifizierungsstatus des Empfängers (für USA: data.privacyframework.gov prüfen)

## Rechtlicher Rahmen

### Primaernormen

- **Art. 44 DSGVO** – Allgemeines Prinzip: Kein Transfer ohne geeignete Garantien oder Ausnahme; gilt auch für Weiterverarbeitung nach Transfer
- **Art. 45 DSGVO** – Angemessenheitsbeschluss der Kommission; kein zusätzliches Genehmigungserfordernis bei positiver Entscheidung
- **Art. 46 DSGVO** – Geeignete Garantien: Standardvertragsklauseln (SCC), Binding Corporate Rules (BCR), Verhaltensregeln mit verbindlichen Verpflichtungen, Zertifizierungsmechanismen
- **Art. 47 DSGVO** – Verbindliche interne Datenschutzvorschriften (BCR); Genehmigung durch federführende Aufsichtsbehörde erforderlich
- **Art. 49 DSGVO** – Ausnahmen: Einwilligung (Art. 49 Abs. 1 lit. a), Vertragserfordernis (lit. b/c), wichtige Gründe des öffentlichen Interesses (lit. d), Rechtsansprueche (lit. e), lebenswichtige Interessen (lit. f), öffentliches Register (lit. g); Abs. 1 Satz 2: gelegentliche, nicht systematische Transfers bei zwingender Notwendigkeit
- **Art. 4 Nr. 23 DSGVO** – Definition "Internationale Organisation"
- **Art. 13 Abs. 1 lit. f, Art. 14 Abs. 1 lit. f DSGVO** – Informationspflicht über Drittlandtransfer und Transfermechanismus

### Rechtsprechung und Leitlinien

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **EDSA, Empfehlungen 01/2020 zu Maßnahmen zur Ergänzung von Übermittlungsinstrumenten**, angenommen am 18.06.2021 (Version 2.0): Sechsstufige Pruefmethodik für Transfer Impact Assessment (TIA); massgeblich für die Schrems-II-Umsetzung in der Praxis
- **EDSA, Leitlinien 05/2021 zum Zusammenwirken von Art. 3 und Kapitel V DSGVO**, angenommen am 18.11.2021: Klärung, wann der raeumliche Anwendungsbereich (Art. 3 DSGVO) und die Drittlandregeln (Kapitel V) kumulativ oder alternativ gelten
- **DSK Orientierungshilfe Drittstaatentransfer**: Handlungsempfehlungen für verantwortliche Stellen bei Transfers in Drittlaender; abrufbar auf dskonferenz.de `[Modellwissen – aktuellen Stand pruefen]`

### Aktuelle Angemessenheitsbeschlüsse (Stand 05/2026)

| Staat | Beschluss | Hinweis |
|---|---|---|
| **USA** | EU-US Data Privacy Framework, Beschluss der Kommission vom 10.07.2023 (C(2023) 4745 final) | Nur für zertifizierte Unternehmen auf der DPF-Liste; Prüfung auf data.privacyframework.gov erforderlich |
| **UK** | Angemessenheitsbeschluss vom 28.06.2021 (Beschluss 2021/1772/EU) | Gilt vorbehaltlich Überprüfung; nach Brexit-Änderungen des britischen Datenschutzrechts beobachten |
| **Schweiz** | Angemessenheitsbeschluss der Kommission; erneuert im Kontext des CH-Datenschutzgesetzes (nDSG, in Kraft ab 01.09.2023) | Teilweiser Angemessenheitsbeschluss; Praxis nach CH-DSG-Reform beachten |
| **Andorra** | Beschluss 2010/625/EU |  |
| **Argentinien** | Beschluss 2003/490/EG |  |
| **Faeroeer** | Beschluss 2010/146/EU |  |
| **Guernsey** | Beschluss 2003/821/EG |  |
| **Isle of Man** | Beschluss 2004/411/EG |  |
| **Israel** | Beschluss 2011/61/EU |  |
| **Japan** | Beschluss vom 23.01.2019 (2019/419/EU) | Mit gegenseitiger Anerkennung; Einschraenkungen beachten |
| **Jersey** | Beschluss 2008/393/EG |  |
| **Kanada** | Beschluss 2002/2/EG | Nur für Organisationen, die dem PIPEDA unterliegen; Bundesbehörden ausgenommen |
| **Neuseeland** | Beschluss 2013/65/EU |  |
| **Suedkorea** | Beschluss vom 17.12.2021 (2022/254/EU) | Erster Angemessenheitsbeschluss in Asien außerhalb Japan |
| **Uruguay** | Beschluss 2012/484/EU |  |

## Ablauf

### 1. Identifizierung des Drittlandstransfers

Prüfen, ob überhaupt ein Transfer i.S.d. Kapitel V DSGVO vorliegt:
- Findet eine Übermittlung an einen Empfänger außerhalb EU/EWR statt?
- Genügt ein "Zugriff" (z.B. Remote-Support, Administrationszugang) aus einem Drittland – nach EDSA-Leitlinien 05/2021 ja, wenn personenbezogene Daten im Zugriffsmittelpunkt stehen
- Art. 3 Abs. 2 DSGVO (extraterritoriale Anwendung): Liegt der Empfänger zwar im Drittland, faellt aber schon unter den raeumlichen Anwendungsbereich der DSGVO? Dann kein Kapitel-V-Transfer, aber Compliance-Prüfung nach Leitlinien 05/2021

### 2. Prüfung Angemessenheitsbeschluss (Art. 45 DSGVO)

- Liegt für das Empfängerland ein gültiger Angemessenheitsbeschluss der Kommission vor? (Tabelle oben)
- **USA:** Ist der Empfänger auf der DPF-Liste eingetragen und für die relevanten Datenkategorien zertifiziert? (data.privacyframework.gov)
- Wenn Angemessenheitsbeschluss vorhanden: Transfer grundsaetzlich zulässig; Art. 13/14 DSGVO-Hinweispflicht beachten
- **Hinweis:** Angemessenheitsbeschlüsse koennen durch den EuGH für ungültig erklärt werden (vgl. Schrems I und II); bei politisch sensiblen Ländern Monitoring empfehlen

### 3. Geeignete Garantien (Art. 46 DSGVO) – falls kein Angemessenheitsbeschluss

**a) Standardvertragsklauseln (SCC) nach Beschluss 2021/914/EU:**

| Modul | Konstellation | Typischer Anwendungsfall |
|---|---|---|
| Modul 1 | Verantwortlicher (EU) → Verantwortlicher (Drittland) | Konzerntransfer, gemeinsam Verantwortliche |
| Modul 2 | Verantwortlicher (EU) → Auftragsverarbeiter (Drittland) | Cloud-Dienst, Hosting, Analytics |
| Modul 3 | Auftragsverarbeiter (EU) → Auftragsverarbeiter (Drittland) | Sub-Auftragsverarbeiter |
| Modul 4 | Auftragsverarbeiter (Drittland) → Verantwortlicher (EU) | Ruecktransfer verarbeiteter Daten |

Prüfpunkte bei SCC: Richtiges Modul? Technische Anlage (Anhang I A–C und II) vollständig ausgefüllt? Technische Maßnahmen (Anhang II TOMs) konkret und nicht pauschal?

**b) Binding Corporate Rules (BCR):**
- Genehmigung durch federführende Aufsichtsbehörde nach Art. 47 DSGVO
- Umfang: alle Konzernunternehmen, die die BCR unterzeichnet haben
- BCR-Update nach Schrems II erforderlich; EDSA-Empfehlungen 01/2020 gelten auch für BCR

**c) Verhaltensregeln mit Verpflichtungen (Art. 46 Abs. 2 lit. e DSGVO):**
- Muss von zuständiger Aufsichtsbehörde genehmigt sein
- In der Praxis bisher wenig verbreitet

**d) Zertifizierungsmechanismen (Art. 46 Abs. 2 lit. f DSGVO):**
- Zertifizierungseinrichtung muss akkreditiert sein; Verpflichtung des Importeurs erforderlich

### 4. Transfer Impact Assessment (TIA) nach Schrems II

Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

**TIA Sechsstufige Methodik (EDSA-Empfehlungen 01/2020):**

1. **Schritt 1:** Alle Übermittlungen kartieren (Zweck, Datenart, Empfänger, Empfängerland)
2. **Schritt 2:** Transfermechanismus identifizieren (SCC, BCR etc.)
3. **Schritt 3:** Rechtslage im Empfängerland beurteilen: Massengesetze (FISA Section 702, USA CLOUD Act), Behördenzugriffsrechte, Rechtsschutzmöglichkeiten für Betroffene, Zugang zu unabhängigen Gerichten
4. **Schritt 4:** Prüfen, ob Recht und Praxis die SCC-Schutzwirkung unterlaufen (Schrems-II-Kriterium: aequivalentes Schutzniveau)
5. **Schritt 5:** Ergänzende Maßnahmen identifizieren und umsetzen (s. Abschnitt 5)
6. **Schritt 6:** Formale Schritte (Vertrag schließen, ggf. Aufsichtsbehörde informieren, Dokumentation)

### 5. Ergänzende Maßnahmen (EDSA-Empfehlungen 01/2020)

Bei unzureichendem Schutzniveau im Empfängerland koennen ergänzende Maßnahmen die Schutzlücke schließen:

**Technische Maßnahmen:**
- Ende-zu-Ende-Verschlüsselung mit Schlüsselhoheit beim Verantwortlichen in der EU (Schlüsselmanagement-Standort entscheidend)
- Pseudonymisierung vor Transfer; Zuordnungsschlüssel verbleibt in der EU
- Zero-Knowledge-Architektur für Cloud-Dienste

**Vertragliche Maßnahmen:**
- Erweiterung der SCC um technische Spezifikation der Verschlüsselung
- Verpflichtung des Importeurs zur Benachrichtigung bei Behördenzugang
- Audit-Rechte für Drittland-Compliance

**Organisatorische Maßnahmen:**
- Datensparsamkeit: nur pseudonymisierte/aggregierte Daten übermitteln
- Trennung von Supportzugriff und Produktionsdaten

### 6. Dokumentation und Informationspflichten

- Verarbeitungsverzeichnis (Art. 30 DSGVO): Transfer, Empfängerland, Mechanismus, TIA vermerken
- Datenschutzerklärung (Art. 13 Abs. 1 lit. f DSGVO): Drittlandtransfer, Mechanismus und ggf. Kopienangebot der SCC erwaehnen
- AVV (Art. 28 Abs. 3 DSGVO): Sub-AV-Kette mit Drittlandsangaben; TIA als Anlage
- TIA als internes Dokument archivieren und bei Anfragen der Aufsichtsbehörde vorlegen koennen

## Pruefschema TIA (Checkliste)

- [ ] **Lokale Massengesetze:** Erlauben Gesetze des Empfängerlandes Massensammlung (z.B. FISA 702, EO 12333 für USA; Geheimdienstgesetze CN, RU)?
- [ ] **Behördenzugriff auf Daten:** Koennen Behörden ohne richterliche Kontrolle auf Daten zugreifen? Wie haeufig werden solche Befugnisse genutzt (Transparenzberichte)?
- [ ] **Verschlüsselung at rest:** Sind Daten beim Empfänger verschlüsselt gespeichert? Wer hat Zugriff auf Schlüssel?
- [ ] **Verschlüsselung in transit:** Wird TLS/mTLS verwendet? Zertifikate kontrolliert?
- [ ] **Schlüsselmanagement-Standort:** Befinden sich Schlüssel und HSMs in der EU? Oder Schlüsselhoheit beim Empfänger im Drittland?
- [ ] **Sub-Processor-Mapping:** Welche Sub-Auftragsverarbeiter des Empfängers befinden sich ebenfalls in Drittlaendern? TIA für Sub-Processor?
- [ ] **Rechtsschutz für Betroffene:** Haben EU-Betroffene Klagemöglichkeiten im Empfängerland oder über Rechtsbehelfsinstanz (z.B. Data Protection Review Court der USA)?
- [ ] **Transparenzberichte:** Veröffentlicht der Empfänger Behördenanfragen (Government Disclosure Reports)?

## Risikoampel

| Konstellation | Rot | Orange | Grün |
|---|---|---|---|
| US-Cloud ohne DPF-Zertifizierung und ohne SCC | x | | |
| US-Cloud mit SCC, ohne TIA | | x | |
| US-Cloud mit DPF-zertifiziertem Anbieter | | | x (zzgl. SCC und TIA empfohlen als Doppelabsicherung) |
| US-Cloud mit SCC und positivem TIA (Verschlüsselung, Schlüssel EU) | | | x |
| UK (Angemessenheitsbeschluss 2021 gültig) | | | x (Monitoring erforderlich) |
| Schweiz nach nDSG (Angemessenheitsbeschluss bestätigt) | | | x |
| Indien ohne SCC | x | | |
| Indien mit SCC und TIA | | x | |
| China ohne Mechanismus | x | | |
| BCR-gedeckter Konzernverbund, TIA positiv | | | x |
| Art. 49 DSGVO Einwilligung, nicht systematisch | | x | |

## Vorlagen und Bausteine

### TIA-Bericht Musterstruktur

```
TIA – Transfer Impact Assessment
Datum: [DATUM]
Erstellt von: [DSB / Datenschutzbeauftragter]
Empfaengerland: [LAND]
Empfaenger: [NAME, Adresse]
Transfermechanismus: [SCC Modul X / BCR / DPF]
Datenkategorien: [Auflistung]

1. Kartierung der Uebermittlung
   [Zweck, Umfang, Haeufigkeit]

2. Rechtslage im Empfaengerland
   [Relevante Gesetze, Massengesetze, Behoerdenzugriffsrechte]
   Quellen: [Transparenzberichte, Rechtsgutachten, EDSA-Laenderanalysen]

3. Schutzlueckenanalyse
   Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

4. Ergaenzende Massnahmen
   [Verschluesselung, Pseudonymisierung, vertragliche Massnahmen]

5. Ergebnis und Restrisiko
   [Gruen / Orange / Rot – Begruendung]

6. Massnahmenplan
   [Bei Orange oder Rot: konkrete Abhilfemassnahmen mit Frist und Verantwortlichen]

Unterschrift DSB: _____________
Freigabe Datenschutzbeauftragter: _____________
```

### SCC-Modul-Auswahl-Matrix (Entscheidungsbaum)

```
Wer ist Exporteur?
├─ Verantwortlicher in EU
│  ├─ Importeur = Verantwortlicher im Drittland → Modul 1
│  └─ Importeur = Auftragsverarbeiter im Drittland → Modul 2
└─ Auftragsverarbeiter in EU
   ├─ Importeur = Auftragsverarbeiter im Drittland (Sub-AV) → Modul 3
   └─ Importeur = Verantwortlicher im Drittland (Ruecktransfer) → Modul 4
```

### Datenschutzerklärungsbaustein Drittlandtransfer

> "Wir übermitteln personenbezogene Daten an Empfänger in [LAND]. Die Übermittlung erfolgt auf Grundlage von [EU-Standardvertragsklauseln nach Beschluss 2021/914/EU, Modul X / Angemessenheitsbeschluss der Kommission vom [DATUM]]. Für die USA gilt: der Empfänger ist unter dem EU-US Data Privacy Framework zertifiziert. Eine Transferfolgenabschätzung (TIA) liegt vor. Auf Anfrage stellen wir Ihnen eine Kopie der Standardvertragsklauseln zur Verfügung (Kontakt: [DSB])."

## Querverweise

- `datenschutzrecht/skills/avv-pruefung/SKILL.md` – Drittlandtransfer-Prüfung im AVV-Kontext (Schritt 5)
- `datenschutzrecht/skills/us-transfer-tia-dokumentation/SKILL.md` – US-Transfers mit DPF-Listing, SCC/BCR-Ausweichpfad, Schrems-Historie und TIA vertiefen
- `datenschutzrecht/skills/standardvertragsklauseln-scc-paket/SKILL.md` – SCC-Modulwahl und Annex I-III konkret erstellen
- `datenschutzrecht/skills/drittlandtransfer-behoerdenpaket-output/SKILL.md` – Deckvermerk, Anlagenverzeichnis und Antwortpaket fuer Aufsichtsbehoerden ausgeben
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` – DSFA bei Hochrisiko-Drittlandtransfers
- `datenschutzrecht/skills/mandantendaten-ki/SKILL.md` – Drittlandtransfer bei KI-Diensten für Berufsgeheimnisträger
- `datenschutzrecht/skills/datenpanne-meldung/SKILL.md` – Datenpannen bei Drittlandempfaengern
- `datenschutzrecht/skills/regulierungs-luecken-analyse/SKILL.md` – Neue Angemessenheitsbeschlüsse in Gap-Analyse einspielen

## Risiken und typische Fehler

- **DPF-Prüfung vergessen:** DPF-Zertifizierung ist nicht permanent; Unternehmen koennen ihre Zertifizierung verlieren. Vor jedem Transfer auf data.privacyframework.gov prüfen und erneut prüfen bei Vertragserneuerung.
- **Falsches SCC-Modul:** Ein Verantwortlicher, der SCC-Modul 3 (AV-zu-AV) verwendet, obwohl er selbst Verantwortlicher ist, erzeugt keine schutzwirkende Grundlage. Konstellation vor Unterzeichnung zwingend prüfen.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- **Art. 49 DSGVO als Regelfall:** Die Ausnahmen des Art. 49 DSGVO sind auf Einzelfälle beschraenkt; systematische und regelmäßige Transfers auf dieser Basis sind nicht zulaessig (EDSA-Leitlinien 2/2018).
- **Sub-Processor-Kette übersehen:** SCC Modul 2/3 legt dem Importeur Pflichten für Sub-Auftragsverarbeiter auf; deren Drittlandstatus muss ebenfalls abgesichert sein (Art. 28 Abs. 4 DSGVO).
- **Schlüsselhoheit nicht geprüft:** Verschlüsselung schuetzt nur dann, wenn Schlüssel nicht im Drittland liegen. Cloud-Dienste mit US-Schlüsselmanagement bieten keinen vollständigen Schutz gegen FISA 702-Zugriffe.
- **Angemessenheitsbeschluss validitaet nicht geprüft:** Nach Schrems I und II koennen Angemessenheitsbeschlüsse wegfallen. Monitoring-Pflicht für sensible Verarbeitungen.

## Quellen und Updates

Stand: 05/2026. Aktualität bei folgenden Ereignissen prüfen und Skill aktualisieren:
- Neue Angemessenheitsbeschlüsse der Europaeischen Kommission
- EuGH-Urteile zu Kapitel V DSGVO
- Änderungen am DPF (data.privacyframework.gov – politische und rechtliche Entwicklungen USA)
- Neue BCR-Anerkennungen durch Aufsichtsbehörden
- Aktualisierungen der EDSA-Empfehlungen 01/2020
- Örtliche Datenschutzgesetze in Drittlaendern (z.B. CLOUD Act Amendments, neue chinesische Datenschutzgesetze PIPL)

Nächste geplante Überprüfung: 05/2027 oder bei wesentlichen Änderungen.

## Faktische Updates (Stand 05/2026)

- **EU-US Data Privacy Framework (DPF):** Der Angemessenheitsbeschluss vom 10.07.2023 (C(2023) 4745 final) ist weiterhin in Kraft. Erstmalige periodische Ueberpruefung durch die Kommission war fuer 07/2024 vorgesehen; weitere Reviews alle vier Jahre. **Achtung:** politische Risiken (Schrems-III-Vorlage, US-Executive-Order-Modifikationen) machen Monitoring zwingend. Quelle: eur-lex.europa.eu, commission.europa.eu/law/law-topic/data-protection.
- **DPF-Listing:** Empfaenger-Status muss vor jeder Uebermittlung ueber dataprivacyframework.gov (offizielle US-Website) verifiziert werden; Selbst-Zertifizierungs-Status kann jederzeit verloren gehen.
- **UK-Angemessenheitsbeschluss (2021/1772):** Gilt nach urspruenglichen vier Jahren Befristung; Verlaengerung war erforderlich — aktuellen Status der Verlaengerung / Ueberpruefung live pruefen.
- **EDSA-Guidelines:** Empfehlungen 01/2020 (Sechs-Stufen-TIA), Guidelines 05/2021 (Wechselwirkung Art. 3 und Kapitel V) sowie aktuelle EDSA-Stellungnahmen 2025 zu Drittlandtransfer-Risiken (insb. China PIPL, US-Executive-Orders) live ueber edpb.europa.eu pruefen.
- **NIS-2 + Drittlandtransfer:** Auftraggeber wichtiger / besonders wichtiger Einrichtungen muessen Cyber-Risiken in der Lieferkette (Art. 21 NIS-2-RL i.V.m. § 30 BSIG n.F.) bei Drittland-Cloud-Diensten zusaetzlich beruecksichtigen; Schnittstelle zu TIA dokumentieren.
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe ueber curia.europa.eu (EuGH) verifizieren.

## Leitrechtsprechung

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn (Entscheidungsbaum)

```
Findet eine Übermittlung außerhalb EU/EWR statt?
  Nein → kein Kapitel-V-DSGVO-Problem
  Ja → Angemessenheitsbeschluss vorhanden?
        Ja (USA/DPF, UK, Schweiz etc.) → Angemessenheitsbeschluss, Scope, Empfänger und Monitoring prüfen
        Nein → SCC (Beschluss 2021/914) vorhanden?
                 Ja → TIA erforderlich; Modul korrekt?
                 Nein → BCR / Art. 49 Ausnahme?
                          Nein → Übermittlung unzulässig
```

## Output-Template — TIA-Ergebnis

**Adressat:** Datenschutzbeauftragter / Rechtsabteilung — Tonfall: sachlich-juristisch

```
Transfer Impact Assessment (TIA) [DATUM]
Empfaengerland: [LAND]
Empfaenger: [NAME, FUNKTION]
Uebermittlungsgrundlage: Angemessenheitsbeschluss / SCC Modul [X] / BCR / Art. 49

Rechtslage Empfaengerland:
- Nachrichtendienstliche Befugnisse: [BESCHREIBUNG]
- Schutzlevel: aequivalent / eingeschraenkt / unzureichend

Risikobewertung:
- Wahrscheinlichkeit behördlicher Zugriffe: hoch / mittel / gering
- Datensensitivität: hoch / mittel / gering
- Gesamtrisiko: hoch / mittel / akzeptabel

Zusatzmassnahmen:
- Verschlüsselung: [ja/nein; Standard]
- Pseudonymisierung: [ja/nein]
- Vertragliche Widerstandspflicht: [ja/nein]

Ergebnis: Übermittlung zulässig / zulässig mit Auflagen / unzulässig
```

## 6. `drittlandtransfer-behoerdenpaket-output`

**Frühere Beschreibung:** Behördenfähiges Dokumentations- und Antwortpaket für Drittlandtransfers erstellen: Deckvermerk, Transferregister, DPF/SCC/TIA-Nachweise, TOMs, Subprozessoren, Maßnahmenplan und Antwort an deutsche Datenschutzaufsicht.

# Drittlandtransfer-Behördenpaket-Output

## Zweck

Dieser Skill erstellt aus vorhandenen Prüfungen ein geordnetes Paket für Datenschutzaufsichtsbehörden, interne Audits, DSB-Berichte oder Geschäftsführungsfreigaben. Er sammelt nicht nur Dokumente, sondern macht sichtbar, warum der Transfer erlaubt, eingeschränkt erlaubt oder vorläufig gestoppt ist.

## Startsignal

Nutze diesen Skill, wenn der Nutzer sagt:

- "Die Aufsichtsbehörde fragt nach dem US-Transfer."
- "Wir brauchen ein Paket, das wir vorlegen können."
- "Bitte druckreif dokumentieren."
- "Zeig, dass DPF/SCC/TIA geprüft wurden."
- "Wir müssen nachweisen, dass ein Anbieter gelistet oder nicht gelistet ist."

## Eingangslogik

1. Liegt bereits ein TIA vor? Wenn nein, `us-transfer-tia-dokumentation` vorschlagen und den fehlenden Kern extrahieren.
2. Liegen SCC vor? Wenn unklar, `standardvertragsklauseln-scc-paket` vorschlagen.
3. Liegt ein DPF-Nachweis vor? Wenn nein, Abruf/Prüfung als `nicht verifiziert` markieren und Nachholung als Sofortmaßnahme setzen.
4. Ist die Behördenfrist bekannt? Wenn ja, Ausgabe nach Frist priorisieren.

## Paketstruktur

### 1. Deckvermerk

Erstelle einen klaren Vermerk:

- Aktenzeichen/Behördenbezug.
- Verantwortliche Stelle und Datenschutzkontakt.
- Betroffener Dienst/Transfer.
- Kurzentscheidung: DPF / SCC + TIA / BCR / Art. 49 / Stop.
- Standdatum.
- Liste der beigefügten Nachweise.
- Offene Punkte und Nachreichungsangebot.

### 2. Entscheidungsmatrix

| Frage | Ergebnis | Nachweis | Risiko | Maßnahme |
|---|---|---|---|---|
| Gibt es einen Drittlandtransfer? | Ja/Nein | Transferregister | ... | ... |
| Ist ein Angemessenheitsbeschluss einschlägig? | Ja/Nein/Teilweise | DPF-Check | ... | ... |
| Sind SCC/BCR erforderlich? | Ja/Nein | Vertrag/Annex | ... | ... |
| Liegt ein TIA vor? | Ja/Nein | TIA-Vermerk | ... | ... |
| Sind Subprozessoren prüfbar? | Ja/Nein | Subprozessorliste | ... | ... |
| Sind ergänzende Maßnahmen ausreichend? | Ja/Nein/Offen | TOM-Matrix | ... | ... |

### 3. Anlagenverzeichnis

Nummeriere die Anlagen:

1. Transferregister-Auszug.
2. DPF-Prüfvermerk mit Abrufdatum.
3. AVV/DPA.
4. SCC mit Modul- und Annex-I-III-Übersicht.
5. TIA-Vermerk.
6. TOM-/Security-Anlage.
7. Subprozessoren-Archiv.
8. Datenschutzhinweis-/VVT-Auszug.
9. Managemententscheidung.
10. Review-Kalender und Maßnahmenplan.

### 4. Behördenantwort

Formuliere neutral, präzise und ohne Überbehauptung:

- Was geprüft wurde.
- Welche Rechtsgrundlage aktuell herangezogen wird.
- Warum Safe Harbor/Privacy Shield nicht als aktuelle Grundlage genutzt werden.
- Ob DPF trägt und für welchen Scope.
- Falls DPF nicht trägt: welche SCC/BCR/TIA-Maßnahmen greifen.
- Welche Lücken erkannt und bis wann geschlossen werden.

**Keine falsche Sicherheit:** Wenn ein Nachweis fehlt, schreibe nicht "liegt vor", sondern "wird bis [Datum] nachgereicht" oder "ist beim Anbieter angefordert".

## Drei Standardszenarien

### A. US-Anbieter aktiv DPF-gelistet

Output-Schwerpunkt:

- DPF-Check als Hauptnachweis.
- Scope-Abgleich.
- Transferregister und AVV.
- TOMs und Subprozessoren als Kontrollnachweise.
- Review alle 6 bis 12 Monate und bei Zertifizierungsablauf.

### B. US-Anbieter nicht oder nicht passend DPF-gelistet

Output-Schwerpunkt:

- SCC-Modulwahl.
- TIA mit Drittlandsrecht/Praxis und Zusatzmaßnahmen.
- Subprozessoren.
- Entscheidung "Freigabe mit Auflagen" oder "Stop".
- Keine Berufung auf DPF für diesen Transfer.

### C. Altfall Safe Harbor/Privacy Shield

Output-Schwerpunkt:

- Historische Grundlage ausdrücklich als überholt markieren.
- Zeitraum und Datenflüsse abgrenzen.
- Aktuelle Ersatzgrundlage festlegen.
- Nachbereinigung von Datenschutzhinweisen, AVV, VVT und Einkaufsakten.

## Druckreifes Ausgabeformat

Wenn der Nutzer "ausdrucken", "vorlegen", "Behörde" oder "Aktenvermerk" sagt, liefere:

1. **Einseitige Executive Summary**.
2. **Vollvermerk** mit Tabellen.
3. **Anlagenliste**.
4. **Antwortschreiben**.
5. **Offene-Punkte-Liste** mit Eigentümer und Datum.

## Qualitätsgate vor Abschluss

- Stimmen Rechtsträgernamen überall überein?
- Ist der genaue Transfer benannt, nicht nur der Anbieter?
- Sind DPF/SCC/TIA logisch konsistent?
- Gibt es keine Behauptung "Shield gültig"?
- Sind Dokumentstände datiert?
- Sind offene Punkte sichtbar statt versteckt?
- Ist die nächste Wiedervorlage gesetzt?

## Quellen und Aktualität

- Stand: 05/2026.
- DSGVO Art. 5 Abs. 2, Art. 24, Art. 28, Art. 30, Art. 44-49.
- EU-US Data Privacy Framework-Angemessenheitsbeschluss vom 10.07.2023.
- Standardvertragsklauseln nach Durchführungsbeschluss (EU) 2021/914.
- EDSA Recommendations 01/2020.


## Qualitäts-Hardening

- Arbeite aktennah: Tatsachen, Belege, Fristen, Zuständigkeit und gewünschtes Arbeitsprodukt zuerst klären.
- Keine Rechtsprechung aus Modellwissen zitieren. Jede Entscheidung vor Ausgabe mit Gericht, Entscheidungsform, Datum, Aktenzeichen und frei oder amtlich prüfbarer Quelle absichern.
- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatz-Blindzitate. Literatur nur verwenden, wenn der Nutzer sie bereitstellt oder ein lizenzierter Live-Zugriff im konkreten Arbeitsschritt dokumentiert ist.
- Wenn eine Quelle, Randnummer, Behördenpraxis oder Frist nicht sicher geprüft ist, sichtbar als Prüfpunkt markieren und keine Scheinpräzision erzeugen.
- Ergebnisse so liefern, dass sie sofort weiterverwendbar sind: Kurzbild, Prüfpfad, Risikoampel, Lückenliste und konkrete nächste Schritte.

## 7. `dsb-bestellungspflicht-pruefung`

**Frühere Beschreibung:** Bestellungspflicht für Datenschutzbeauftragten prüfen. Art. 37 DSGVO § 38 BDSG Bestellungspflicht. Prüfraster: Schwellenwerte Art. 37 Abs. 1 Betriebsgroe Verarbeitungsart Pflichtbestellung freiwillige Bestellung. Output: Bestellungsprüfmemo Empfehlung. Abgrenzung: nicht für Aufgaben des DSB (Art. 39 DSGVO).

# DSB-Bestellungspflicht und -Anforderungen

## Zweck

Häufige Lücke in Unternehmen: Pflicht zur DSB-Bestellung wird nicht erkannt. Dieses Skill prüft Pflicht, Anforderungen an DSB und löst Folge-Probleme (Interessens-Konflikt, externe vs. interne Bestellung).

## Eingaben

- Unternehmens-Typ (öffentlich privat)
- Beschäftigten-Zahl
- Verarbeitungs-Tätigkeiten (Übersicht aus VVT)
- Bestand DSB ja/nein
- Bei Bestand: Person und Rolle (intern extern)

## Schritt 1 — Pflicht-Tatbestände Art. 37 DSGVO

### Lit. a) Öffentliche Stelle / Behörde

- **Pflicht** unabhängig von Größe
- Außer Gerichte in Justizfunktion

### Lit. b) Kerntätigkeit umfangreiche regelmäßige systematische Überwachung

- **Kerntätigkeit** das Geschäft selbst (nicht nur Mittel zur Geschäftsführung)
- **Umfangreich** Skalierung
- **Regelmäßig systematisch** Dauerhaft strukturiert
- **Überwachung** Beobachtung Verhalten Profilbildung

#### Beispiele

- Online-Verhaltens-Tracking Werbe-Netzwerke
- Vermarkter mit Profiling
- Telematik-Versicherer
- Standort-Verfolgung
- CCTV im großen Stil

### Lit. c) Kerntätigkeit umfangreiche Verarbeitung besondere Kategorien

- **Art. 9 DSGVO** Daten (Gesundheit Religion Sexual-Orientierung etc.)
- **Strafrechtliche Daten** Art. 10
- **Umfangreich**

#### Beispiele

- Krankenhäuser
- Religions-Gemeinschaften
- Personalvermittler mit Diversity-Daten
- Strafvollzug-Dienstleister
- Genetik-/Genom-Labore

## Schritt 2 — § 38 BDSG Deutsche Erweiterung

### Schwellenwert

- **In der Regel mindestens 20 Personen**
- **Ständig mit automatisierter Verarbeitung beschäftigt**
- Bei Pflicht zur DSFA (Art. 35) auch bei weniger Personen
- Bei geschäftsmäßiger Verarbeitung zum Zweck der Übermittlung anonymen Übermittlung Markt- oder Meinungsforschung

### "Personen" im Sinne § 38 BDSG

- Mitgezählt werden **eigene Beschäftigte** des Verantwortlichen (Voll- und Teilzeit, Aushilfen, Auszubildende, Werkstudenten, freie Mitarbeiter mit Datenzugriff)
- **Auftragsverarbeiter-Personal zählt NICHT mit** — dieses gehört zum Auftragsverarbeiter, der selbst die DSB-Pflicht prüft
- Entscheidend ist die Ständigkeit der automatisierten Verarbeitung, nicht das Beschäftigungs-Volumen

### Kombination

- EU-DSGVO und § 38 BDSG nebeneinander
- Strengstes Kriterium gilt

## Schritt 3 — Anforderungen DSB Art. 37 Abs. 5 6 DSGVO

### Fachliche Eignung

- **Berufliche Qualifikation** Datenschutz
- **Fachwissen** DSGVO BDSG
- **Spezialwissen** der Branche
- Zertifizierungen: TÜV, GDD, DIA, BvD u.a.

### Persönliche Eignung

- Zuverlässigkeit
- Vertrauenswürdig
- Bei Insolvenz / Strafverfahren prüfen

## Schritt 4 — Stellung DSB Art. 38 DSGVO

### Unabhängigkeit

- **Keine Weisungs-Bindung** in Datenschutz-Fragen
- **Berichts-Linie** an oberste Leitung
- **Schutz vor Abberufung** wegen Aufgaben-Wahrnehmung

### Ressourcen-Pflicht

- **Zeitliche Verfügbarkeit** ausreichend
- **Sachliche Ausstattung** Büro IT Reisekosten
- **Fortbildungs-Budget**
- **Externe Hilfe** wenn nötig

### Schutz vor Kündigung / Abberufung

- **§ 6 Abs. 4 BDSG** Kündigungs-Schutz analog § 4f
- Bei Beendigungs-Schutz auch nach Amtszeit
- Außerordentliche Kündigung nur bei wichtigem Grund

### Schweigepflicht

- DSB unterliegt Schweige-Pflicht
- Auch nach Beendigung

## Schritt 5 — Interne vs. externe Bestellung

### Interner DSB

- **Aus Belegschaft**
- **Voll- oder Teilzeit-DSB-Aufgabe**
- **Vorteil:** Insider-Kenntnis
- **Nachteil:** Interessens-Konflikt-Risiko

### Externer DSB

- **Beratung durch externe Firma / Anwalts-Kanzlei**
- **Vertragliche Bestellung**
- **Vorteil:** Unabhängigkeit Spezialisierung
- **Nachteil:** Externe Person ohne Insider-Kenntnis

### Konzern-DSB

- Ein DSB für mehrere Konzern-Gesellschaften
- Erlaubt § 38 Abs. 1 BDSG ("für mehrere Stellen")
- Konzern-Bestellungs-Akte
- Kommunikations-Linie zu allen Gesellschaften

## Schritt 6 — Interessens-Konflikt-Prüfung

### Problematische Doppelrollen

#### Geschäftsführer / Vorstand

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- ErwGr 97 DSGVO zur Unabhängigkeits-Anforderung
- Strikte Trennung erforderlich

#### IT-Leitung

- Verarbeitung verantwortlich + Datenschutz kontrollierend
- Konflikt häufig
- Strikt: Trennung erforderlich

#### Personalleitung

- Personal-Verarbeitung steuernd + Datenschutz kontrollierend
- Konflikt häufig

#### Compliance-Officer

- Bei klar getrennten Bereichen möglich
- Bei umfassender Compliance-Verantwortung Konflikt

### Unproblematische Rollen

- IT-Sicherheits-Beauftragter (komplementär)
- Externer Anwalt (unabhängig)
- Externe Beratung (klar)

### Bei Konflikt

- **Auswechslung** des DSB
- **Externe Bestellung**
- **Strukturelle Anpassung** der internen Rollen

## Schritt 7 — Aufgaben DSB Art. 39 DSGVO

### Pflicht-Aufgaben

a) **Information und Beratung** Verantwortlicher und Beschäftigte

b) **Überwachung** Einhaltung DSGVO und Datenschutz-Vorschriften

c) **Beratung** zu DSFA und deren Überwachung

d) **Zusammenarbeit** Aufsichtsbehörde

e) **Anlaufstelle Aufsichtsbehörde** für Fragen Beratung

### Zusätzlich

- Mit-wirkung VVT
- Beratung bei AVV-Erstellung
- Schulung Mitarbeiter
- Datenpanne-Bewertung

## Schritt 8 — Meldung Aufsichtsbehörde Art. 37 Abs. 7 DSGVO

### Pflicht zur Veröffentlichung

- Kontakt-Daten DSB
- Mitteilung an Aufsichtsbehörde
- Online-Meldung möglich

### Form

- Schriftlich elektronisch
- Aufsichtsbehörde wo Verantwortlicher Hauptniederlassung
- Inhalt: Name Anschrift Telefon E-Mail

### Bei Änderungen

- Update bei Wechsel DSB
- Bei Wechsel der Aufsichtsbehörden-Zuständigkeit

## Schritt 9 — Bestellungs-Akt

### Form

- **Schriftlich** empfohlen
- **Stellenbeschreibung** mit Aufgaben Rechten
- **Vertrag** bei externem DSB
- **Bestellungs-Urkunde** intern

### Inhalt

- Bestellungs-Datum
- Aufgaben gemäß Art. 39 DSGVO
- Ressourcen-Zusage
- Berichts-Linie
- Vertraulichkeits-Pflicht
- Beendigungs-Regelung

## Schritt 10 — Bei Verstoß

### Sanktionen

- **Art. 83 Abs. 4 DSGVO** bis 10 Mio EUR oder 2 Prozent Konzernumsatz
- **Aufsichts-Anordnung** zur Bestellung
- **Reputations-Schaden**

### Folge-Probleme

- Datenpannen ohne DSB schwerer beherrschbar
- DSFA-Lücken
- Aufsichts-Behörden-Audit kritisch

## Schritt 11 — Beratungs-Schritte

### Erstprüfung

1. **Beschäftigten-Zahl** über 20 mit automatisierter Verarbeitung?
2. **Verarbeitungs-Typ** Kerntätigkeit mit Überwachung oder besonderen Kategorien?
3. **Öffentliche Stelle**?
4. **Bei Bejahung**: DSB-Pflicht — sofort Bestellung erforderlich

### Wenn DSB vorhanden

1. **Eignungs-Prüfung** Qualifikation aktuell?
2. **Stellung** Unabhängigkeit gewährleistet?
3. **Interessens-Konflikt** vorhanden?
4. **Ressourcen** ausreichend?
5. **Meldung** Aufsichtsbehörde erfolgt?

### Wenn DSB-Lücke

1. **Sofortige Bestellung** intern oder extern
2. **Aufsichtsbehörde** informieren
3. **VVT-Eintrag** DSB-Daten
4. **Datenschutz-Hinweise** Webseite aktualisieren

## Schritt 12 — Außerhalb Pflicht — freiwillige Bestellung

### Vorteile

- **Compliance-Sicherheit**
- **Vorbereitung** Wachstum
- **Audit-Vorbereitung**
- **Mandanten-Vertrauen**

### Empfehlung

- Bei jeder Verarbeitung besonderer Kategorien (auch wenn nicht "umfangreich")
- Bei Cookie-Tracking selbst bei kleiner Webseite
- Bei jeder grenz-überschreitenden Verarbeitung

## Verzahnung mit anderen Skills

- `verarbeitungsverzeichnis-vvt-generator` — VVT mit DSB-Bezeichnung
- `dsfa-erstellung` — DSB-Beratung
- `avv-pruefung` — DSB-Beratung
- `datenpanne-meldung` — DSB-Eskalation
- `mandantendaten-ki` — DSB im Kanzlei-Kontext
- `anwendungsfall-triage` — Eingangsprüfung

## Ausgabe

- `dsb-pruefung-{unternehmen}.md` mit Pflicht-Analyse Anforderungs-Prüfung Konflikt-Bewertung
- Bei DSB-Lücke: Bestellungs-Pflicht-Bestätigung + Bestellungs-Vorbereitung
- Bei externem DSB: Vertrags-Entwurf
- Bei internem DSB: Stellenbeschreibung
- Aufsichts-Behörden-Meldung-Vorbereitung
- Frist im Fristenbuch (Bestellung unverzüglich)

## Quellen

- DSGVO Art. 37 38 39 83; ErwGr 97 DSGVO
- BDSG §§ 5 6 38
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.
- BfDI Praxis-Empfehlungen
- DSK Kurzpapier
- GDD und BvD Standards

## Aktuelle Rechtsprechung (v14.2)

- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe über offizielle oder frei zugängliche Quelle mit Gericht, Entscheidungsform, Datum, Aktenzeichen und tragender Aussage verifizieren.

## Triage zu Beginn

1. Öffentliche oder private Stelle? (Art. 37 Abs. 1 lit. a DSGVO vs. § 38 BDSG)
2. Bei privater Stelle: Anzahl Personen, die ständig mit automatisierter Verarbeitung beschäftigt sind (§ 38 Abs. 1 BDSG: ab 20)?
3. Verarbeitung besonderer Kategorien (Art. 9 DSGVO) oder umfangreiche Überwachung?
4. Bestehender DSB: Interessenkonflikt (leitende Verarbeitungsverantwortung)?

## Output-Template — DSB-Prüfvermerk

**Adressat:** Geschäftsführung / Compliance — Tonfall: sachlich-juristisch

```
DSB-Bestellungspflicht-Prüfvermerk [DATUM]
Organisation: [NAME]

Bestellungspflicht-Prüfung:
Öffentliche Stelle (Art. 37 Abs. 1 lit. a DSGVO): ja / nein
Kerntätigkeit umfangreiche Überwachung (Art. 37 Abs. 1 lit. b): ja / nein
Besondere Kategorien umfangreich (Art. 37 Abs. 1 lit. c): ja / nein
§ 38 BDSG: [X] Personen staendig automatisiert → ab 20: Pflicht

Ergebnis Bestellungspflicht: JA / NEIN

Aktueller DSB (falls bestellt):
Name: [NAME] | intern / extern
Interessenkonflikt-Check: kein Konflikt / Konflikt (Grund: [...])
Qualifikation ausreichend: ja / nein / unklar

Empfehlung: DSB bestellen (bis [FRIST]) / DSB wechseln / kein Handlungsbedarf
```

## 8. `dsfa-art-35-dsgvo-trigger-und-anwendungsbereich`

**Frühere Beschreibung:** Pruefung wann eine DSFA nach Art. 35 DSGVO ueberhaupt erforderlich ist. Trigger-Pruefung Anwendungsbereich Schwellwert. Generalklausel Art. 35 Abs. 1 voraussichtlich hohes Risiko; Regelbeispiele Art. 35 Abs. 3; Pflichtlisten Art. 35 Abs. 4 BfDI. Output: Triage-Vermerk DSFA-pflichtig oder nicht.

# DSFA Trigger und Anwendungsbereich nach Art. 35 DSGVO

## Zweck

Dieser Skill liefert eine strukturierte Erstpruefung der Frage, ob fuer eine konkrete Verarbeitungstaetigkeit eine Datenschutz-Folgenabschaetzung (DSFA) nach Art. 35 DSGVO durchzufuehren ist. Ergebnis ist ein Triage-Vermerk mit klarer Aussage DSFA-pflichtig, optional oder entbehrlich und einer Begruendung mit Norm-Anker.

## Wann brauchen Sie diesen Skill

- Vor Einfuehrung einer neuen Verarbeitungstaetigkeit
- Bei wesentlicher Aenderung einer bestehenden Verarbeitung (Art. 35 Abs. 11 DSGVO)
- Bei Aufnahme eines neuen Auftragsverarbeiters, neuer Technologie oder neuer Datenkategorie
- Wenn die interne Compliance, der DSB oder eine Aufsichtsbehoerde die Frage stellt
- Vor Erstellung einer vollstaendigen DSFA (Vorab-Triage)

## Rechtlicher Rahmen

- Art. 35 Abs. 1 DSGVO Generalklausel: DSFA verpflichtend wenn eine Form der Verarbeitung, insbesondere bei Verwendung neuer Technologien, aufgrund Art, Umfang, Umstaenden und Zwecken voraussichtlich ein hohes Risiko fuer die Rechte und Freiheiten natuerlicher Personen zur Folge hat.
- Art. 35 Abs. 3 DSGVO Regelbeispiele:
  - lit. a systematische und umfassende Bewertung persoenlicher Aspekte einschliesslich Profiling und darauf gestuetzter automatisierter Entscheidung mit Rechtswirkung
  - lit. b umfangreiche Verarbeitung besonderer Kategorien nach Art. 9 Abs. 1 oder von Daten ueber strafrechtliche Verurteilungen nach Art. 10
  - lit. c systematische umfangreiche Ueberwachung oeffentlich zugaenglicher Bereiche
- Art. 35 Abs. 4 DSGVO Pflichtliste der Aufsichtsbehoerde (BfDI bzw. zustaendige Landesbehoerde) — sogenannte Blacklist.
- Art. 35 Abs. 5 DSGVO optionale Whitelist der Aufsichtsbehoerde.
- Art. 35 Abs. 10 DSGVO Ausnahme bei gesetzlicher Grundlage mit bereits durchgefuehrter allgemeiner DSFA durch den Gesetzgeber.
- EDSA-Leitlinien WP 248 rev.01 (uebernommen durch EDSA), insbesondere die 9 Kriterien zur Bestimmung von voraussichtlich hohem Risiko.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Kurzbeschreibung der Verarbeitung in maximal 10 Saetzen: Zweck, Datenarten, Betroffenenkreise, Technologie, Drittlandbezug, Aufbewahrung. Ohne diese Beschreibung ist die Trigger-Pruefung nicht moeglich.
2. **Verhaeltnismaessigkeitspruefung.** In dieser Stufe nur grobe Plausibilitaet: Liegt ein offensichtliches Missverhaeltnis von Zweck und Eingriff vor? Falls ja, ist die DSFA bereits aus diesem Grund angezeigt.
3. **Risikoanalyse Trigger-Ebene.** Pruefen der 9 EDSA-Kriterien:
   - Bewertung oder Scoring
   - automatisierte Entscheidung mit Rechtswirkung
   - systematische Ueberwachung
   - besondere Kategorien Art. 9 oder Art. 10
   - umfangreiche Verarbeitung
   - Zusammenfuehrung oder Abgleich von Datensaetzen
   - schutzbeduerftige Personen (Kinder, Patienten, Beschaeftigte)
   - neue Technologien (KI, Biometrie, IoT)
   - Verhinderung der Ausuebung von Betroffenenrechten
4. **Massnahmen.** Pruefen ob bereits getroffene risikomindernde Massnahmen den Schwellwert unter hohes Risiko druecken (Pseudonymisierung, Anonymisierung, technische Beschraenkung). Ergebnis dokumentieren.
5. **Restrisiko / Schwellwertergebnis.** Drei moegliche Ergebnisse:
   - DSFA-PFLICHTIG (Art. 35 Abs. 3, Abs. 4 oder mindestens 2 EDSA-Kriterien)
   - DSFA-EMPFOHLEN (1 EDSA-Kriterium, Grenzfall)
   - DSFA-ENTBEHRLICH (kein Kriterium erfuellt, Blacklist nicht einschlaegig)
6. **Konsultation / Genehmigung.** DSB nach Art. 35 Abs. 2 DSGVO anhoeren. Triage-Vermerk gegenzeichnen lassen und in Verarbeitungsverzeichnis nach Art. 30 verlinken.

## Mustertext / Template

```
DSFA-TRIAGE-VERMERK [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME, ROLLE]
Vorpruefer: [NAME] | DSB-Anhoerung: [DATUM]

1. Kurzbeschreibung
[Zweck, Datenarten, Betroffene, Technologie, Drittlandbezug, Aufbewahrung]

2. Pruefung Art. 35 Abs. 3 DSGVO (Regelbeispiele)
- lit. a Profiling mit Rechtswirkung: ja / nein — [Begruendung]
- lit. b besondere Kategorien umfangreich: ja / nein — [Begruendung]
- lit. c oeffentlicher Bereich Ueberwachung: ja / nein — [Begruendung]

3. Pruefung Art. 35 Abs. 4 DSGVO BfDI-/Landes-Blacklist
- Einschlaegig: ja / nein — [Listen-Position]

4. EDSA-Kriterien WP 248 rev.01 (Anzahl erfuellt)
- [X] von 9

5. Ergebnis
[ ] DSFA PFLICHTIG nach Art. 35 [Abs. 1 / Abs. 3 / Abs. 4]
[ ] DSFA EMPFOHLEN (Grenzfall, Dokumentation der Nicht-DSFA)
[ ] DSFA ENTBEHRLICH (Dokumentation der Begruendung)

6. Naechster Schritt
[ ] Vollstaendige DSFA durchfuehren (Skill dsfa-template-deutsch-vollvorlage)
[ ] Negative Triage-Dokumentation ablegen (Art. 5 Abs. 2 DSGVO Rechenschaftspflicht)

Unterschrift Verantwortlicher: ____________________
Unterschrift DSB: ____________________
```

## Typische Fehler

- Triage wird muendlich erledigt, kein Vermerk angelegt — Verstoss gegen Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO.
- Nur Art. 35 Abs. 3 geprueft, Generalklausel Abs. 1 uebersehen — auch ausserhalb der Regelbeispiele kann DSFA-Pflicht bestehen.
- Blacklist der eigenen Landesbehoerde uebersehen (siehe Skill dsfa-bfdi-und-laender-blacklist).
- Negative Triage nicht dokumentiert — bei spaeterem Aufsichtsverfahren kein Nachweis.
- DSB nicht beteiligt obwohl Art. 35 Abs. 2 ausdruecklich Anhoerung verlangt.
- Wesentliche Aenderung uebersehen — Re-Triage nach Art. 35 Abs. 11 notwendig.

## Querverweise

- `datenschutzrecht/skills/dsfa-bfdi-und-laender-blacklist/SKILL.md` — Blacklist-Abgleich
- `datenschutzrecht/skills/dsfa-edpb-leitlinien-9-19-anwendung/SKILL.md` — EDSA-Kriterien im Detail
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Vollvorlage nach positiver Triage
- `datenschutzrecht/skills/dsfa-typische-fehler-bei-erstpruefung/SKILL.md` — Fehlerquellen Erstpruefung
- `datenschutzrecht/skills/anwendungsfall-triage/SKILL.md` — Plugin-weite Triage
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35, 36 DSGVO (Verordnung EU 2016/679)
- Art. 5 Abs. 2 DSGVO (Rechenschaftspflicht)
- § 67 BDSG (Pflichtliste BfDI)
- EDSA-Leitlinien WP 248 rev.01 zur DSFA
- BfDI: bfdi.bund.de — aktuelle Blacklist und Whitelist live pruefen
- Landesdatenschutzbehoerden (LfDI BW, LDA Bayern u.a.) — eigene Listen
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle oder lizenziertem Live-Zugriff

## 9. `dsfa-bfdi-und-laender-blacklist`

**Frühere Beschreibung:** Abgleich einer Verarbeitung mit der BfDI-Pflichtliste nach Art. 35 Abs. 4 DSGVO und mit den Listen der Landesdatenschutzbehoerden. Output: dokumentierter Listenabgleich mit Trefferanalyse und ggf. Verweis auf zwingende DSFA.

# BfDI- und Laender-Blacklist Abgleich

## Zweck

Dieser Skill fuehrt einen sauberen Abgleich einer konkreten Verarbeitungstaetigkeit mit der Pflichtliste der zustaendigen Aufsichtsbehoerde nach Art. 35 Abs. 4 DSGVO (Blacklist) und mit der Whitelist nach Art. 35 Abs. 5 DSGVO durch. Ergebnis ist ein dokumentierter Listenabgleich, der die Erforderlichkeit oder Entbehrlichkeit einer DSFA stuetzt.

## Wann brauchen Sie diesen Skill

- In der DSFA-Trigger-Pruefung (Schwellwertanalyse)
- Bei einer Aufsichtsanfrage zur Begruendung einer durchgefuehrten oder unterlassenen DSFA
- Bei wesentlichen Aenderungen der Verarbeitung
- Wenn unklar ist, welche Landesdatenschutzbehoerde zustaendig ist (Sitzland-Pruefung)

## Rechtlicher Rahmen

- Art. 35 Abs. 4 DSGVO: Aufsichtsbehoerden erstellen und veroeffentlichen Listen der Verarbeitungstaetigkeiten, fuer die eine DSFA durchzufuehren ist.
- Art. 35 Abs. 5 DSGVO: Aufsichtsbehoerden koennen Listen veroeffentlichen, fuer die keine DSFA erforderlich ist (Whitelist).
- Art. 35 Abs. 6 DSGVO: Listen werden dem Ausschuss EDSA uebermittelt, Koehaerenzverfahren bei grenzueberschreitenden Verarbeitungen.
- § 40 BDSG: Zustaendigkeit der Landesdatenschutzbehoerden fuer den nicht-oeffentlichen Bereich.
- § 67 BDSG verweist auf die Pflichtliste im oeffentlichen Bereich des Bundes.
- EDSA-Leitlinien WP 248 rev.01 als Auslegungshilfe.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welche Verarbeitung soll abgeglichen werden? Konkrete Bezeichnung, Branche, eingesetzte Technologie, Datenkategorien.
2. **Verhaeltnismaessigkeitspruefung.** Zustaendige Aufsichtsbehoerde ermitteln: Bund (BfDI) fuer oeffentliche Stellen des Bundes, Telekommunikation und Postwesen; Laender fuer den nicht-oeffentlichen Bereich, sortiert nach Sitzland des Verantwortlichen.
3. **Risikoanalyse Listenabgleich.** Aktuelle Blacklist der zustaendigen Behoerde live abrufen (bfdi.bund.de bzw. Landesbehoerde). Treffer dokumentieren mit konkretem Listenpunkt und Datum des Abrufs.
4. **Massnahmen.** Pruefen ob die Verarbeitung exakt unter einen Listenpunkt faellt oder nur partiell. Bei partieller Deckung: Begruendung warum trotzdem oder warum nicht DSFA-pflichtig.
5. **Restrisiko.** Falls Blacklist-Treffer: DSFA zwingend. Falls Whitelist-Treffer: DSFA entbehrlich, Dokumentation der Whitelist-Position. Falls weder noch: Pruefung nach Art. 35 Abs. 1 und Abs. 3 DSGVO erforderlich.
6. **Konsultation / Genehmigung.** Listenabgleich dem DSB vorlegen, gegenzeichnen lassen, in das Verarbeitungsverzeichnis nach Art. 30 verlinken.

## Mustertext / Template

```
LISTENABGLEICH NACH ART. 35 ABS. 4 / ABS. 5 DSGVO [DATUM]

Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME, SITZLAND]
Zustaendige Aufsichtsbehoerde: [BfDI / LfDI BW / LDA Bayern / ...]

Quelle Blacklist (Stand): [URL, Abrufdatum]
Quelle Whitelist (Stand): [URL, Abrufdatum]

Pruefung Blacklist
- Listenpunkt 1: [Bezeichnung] — Treffer ja / nein — Begruendung
- Listenpunkt 2: [Bezeichnung] — Treffer ja / nein — Begruendung
- ...

Pruefung Whitelist
- Listenpunkt: [Bezeichnung] — Treffer ja / nein — Begruendung

Ergebnis
[ ] BLACKLIST-TREFFER — DSFA zwingend nach Art. 35 Abs. 4 DSGVO
[ ] WHITELIST-TREFFER — DSFA entbehrlich nach Art. 35 Abs. 5 DSGVO
[ ] KEIN LISTENTREFFER — Pruefung nach Art. 35 Abs. 1, 3 DSGVO fortsetzen

Naechster Schritt: [Vollstaendige DSFA / Dokumentation / Weiterleitung an Skill]

Unterschrift: ____________________
```

## Praxishinweise zur Zustaendigkeit

- Nicht-oeffentlicher Bereich: Landesdatenschutzbehoerde am Sitz des Verantwortlichen.
- Oeffentlicher Bereich Bund (Bundesbehoerden, Telekommunikation, Post): BfDI.
- Oeffentlicher Bereich Land: jeweilige Landesdatenschutzbehoerde.
- Grenzueberschreitende Verarbeitung Art. 56 DSGVO: Federfuehrungsbehoerde am Sitz der Hauptniederlassung.
- Konzern mit mehreren Sitzlaendern: Hauptniederlassung nach Art. 4 Nr. 16 DSGVO bestimmen.

## Typische Fehler

- Nur BfDI geprueft, Landesbehoerde uebersehen — im nicht-oeffentlichen Bereich ist regelmaessig die Landesbehoerde des Sitzlandes zustaendig.
- Listenstand veraltet — Listen werden fortgeschrieben, immer aktuelles Datum dokumentieren.
- Partielle Deckung als Volltreffer behandelt — Listenpunkte sind typenoffen, aber konkret zu pruefen.
- Whitelist als Freibrief verstanden — Whitelist entlastet nur, wenn die Verarbeitung exakt zur Listenposition passt.
- Keine Dokumentation des Abrufdatums — Aufsicht kann den Stand nicht nachvollziehen.
- Grenzueberschreitende Verarbeitung: Federfuehrungsbehoerde nach Art. 56 DSGVO uebersehen.
- Konzerngesellschaften mit Sitz in mehreren Bundeslaendern: jede Gesellschaft hat eigene Aufsicht; nicht zentralisieren.
- Konflikt Bundes- versus Landesliste: bei Doppelpflicht die strengere Vorgabe anwenden.

## Beispielfaelle

- Kreditscoring-Plattform: regelmaessig auf mehreren Landeslisten (Scoring + automatisierte Entscheidung).
- Patientenakte mit Cloud-Speicherung: meist auf BfDI- bzw. Landesliste (besondere Kategorien Art. 9 + neue Technologie).
- Videoueberwachung Bahnhofsvorplatz: Art. 35 Abs. 3 lit. c DSGVO unmittelbar und zusaetzlich Listentreffer wegen oeffentlichem Bereich.
- KI-Personalauswahl: regelmaessig Listentreffer wegen Profiling und neuen Technologien.

## Querverweise

- `datenschutzrecht/skills/dsfa-art-35-dsgvo-trigger-und-anwendungsbereich/SKILL.md` — Trigger-Pruefung
- `datenschutzrecht/skills/dsfa-edpb-leitlinien-9-19-anwendung/SKILL.md` — Wenn kein Listentreffer
- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Bei Blacklist-Treffer
- `datenschutzrecht/skills/spezial-dpia-dokumentenmatrix-und-lueckenliste/SKILL.md` — Dokumentenmatrix
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 35 Abs. 4, 5, 6 DSGVO
- § 40, § 67 BDSG
- BfDI: bfdi.bund.de — Pflichtliste und Whitelist (live pruefen)
- LfDI Baden-Wuerttemberg, LDA Bayern, BlnBDI Berlin, HmbBfDI Hamburg, HBDI Hessen, LfDI Rheinland-Pfalz, LfD Niedersachsen, LDI NRW, ULD Schleswig-Holstein, LfDI Saarland, SaechsDSB, LfD Sachsen-Anhalt, TLfDI, LfD Mecklenburg-Vorpommern, LfDI Bremen, LfD Brandenburg — eigene Listen abrufen
- EDSA-Leitlinien WP 248 rev.01
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle

## 10. `dsfa-dokumentation-und-rechenschaftspflicht-art-5-ii`

**Frühere Beschreibung:** Dokumentation der DSFA als Beleg der Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO: Aktenstruktur Versionierung Aufbewahrung Beweiswert. Output: DSFA-Akte mit Aktenuebersicht und Aufbewahrungsregeln.

# DSFA-Dokumentation und Rechenschaftspflicht

## Zweck

Strukturierte Dokumentation einer DSFA als Beleg der Rechenschaftspflicht nach Art. 5 Abs. 2 DSGVO. Ergebnis dieses Skills ist eine vollstaendige DSFA-Akte mit Aktenuebersicht, Versionierung, Aufbewahrungsregeln und Beweiswertbeurteilung. Ziel ist die jederzeitige Vorlagefaehigkeit gegenueber Aufsicht, Gericht oder DSB.

## Wann brauchen Sie diesen Skill

- Nach Abschluss einer DSFA, vor Archivierung
- Bei Aufsichtsanfrage zur Vorlage der DSFA
- Bei Audit durch DSB oder externen Pruefer
- Bei Wechsel des DSB oder des Verantwortlichen — Aktenuebergabe
- Bei wesentlicher Aenderung (Versionierung)

## Rechtlicher Rahmen

- Art. 5 Abs. 2 DSGVO: Rechenschaftspflicht — der Verantwortliche muss die Einhaltung der Grundsaetze nachweisen koennen.
- Art. 24 DSGVO: Verantwortung des fuer die Verarbeitung Verantwortlichen.
- Art. 30 DSGVO: Verzeichnis von Verarbeitungstaetigkeiten — DSFA-Verweis.
- Art. 35 Abs. 11 DSGVO: Re-Pruefungspflicht.
- Art. 58 Abs. 1 lit. a DSGVO: Auskunftsbefugnis der Aufsicht.
- § 257 HGB, § 147 AO fuer Aufbewahrungsfristen kaufmaennischer und steuerlicher Unterlagen — DSFA ist nicht kaufmaennisches Dokument, aber an die Verarbeitungstaetigkeit gekoppelt.

## Ablauf 6-Schritte-Methodik

1. **Verarbeitungsbeschreibung.** Welcher Verarbeitungsvorgang? Eindeutige Akten-Identifikation (z. B. VV-Nummer, DSFA-Aktenzeichen).
2. **Verhaeltnismaessigkeitspruefung.** Pruefung welche Dokumente in die DSFA-Akte gehoeren — Vollstaendigkeit ohne Ueberfrachtung.
3. **Risikoanalyse.** Beweiswertrisiken pruefen — fehlende Unterschriften, fehlende Versionen, fehlende Datierungen, unklare Verantwortlichkeiten.
4. **Massnahmen.** Strukturierte Aktenfuehrung in standardisierter Form (digital signiert, mit Datum und Versionierung).
5. **Restrisiko.** Beweiswertbeurteilung — wie sicher ist die DSFA bei Aufsichtsverfahren? Ergaenzungen oder Bekraeftigungen.
6. **Konsultation / Genehmigung.** DSB bestaetigt Vollstaendigkeit; Aufbewahrung und Zugriffsrechte regeln.

## Aktenstruktur DSFA

```
DSFA-AKTE Aktenzeichen: [VV-XX-DSFA-YYYY-NN]
Verarbeitung: [BEZEICHNUNG]
Verantwortlicher: [NAME]
DSB: [NAME]

01 Deckblatt mit Versionshistorie
02 Schwellwertanalyse / Triage-Vermerk (Skill dsfa-art-35-dsgvo-trigger-und-anwendungsbereich)
03 Listenabgleich (Skill dsfa-bfdi-und-laender-blacklist)
04 WP-248-Pruefung (Skill dsfa-edpb-leitlinien-9-19-anwendung)
05 Methodenwahl-Memo (Skill dsfa-methodik-cnil-pia-vs-bsfd-bsi)
06 Vollstaendige DSFA (Skill dsfa-template-deutsch-vollvorlage)
07 Risikomatrix (Skill dsfa-risikoanalyse-eintrittswahrscheinlichkeit-schaden)
08 TIA falls Drittlandtransfer (Skill dsfa-fuer-internationale-datentransfers)
09 KI-FRIA falls Hochrisiko-KI (Skill dsfa-fuer-ki-systeme-schnittstelle-art-26-kivo)
10 Stakeholder-Konsultation (Skill dsfa-stakeholder-konsultation-art-35-9)
11 DSB-Stellungnahme
12 Vorabkonsultation Art. 36 (falls erfolgt)
13 Freigabe Verantwortlicher
14 Verweis Verarbeitungsverzeichnis Art. 30
15 Revisionsplan (Skill dsfa-update-bei-aenderungen-und-revision)
16 Korrespondenz mit Aufsichtsbehoerde (falls)
17 Beweismittel: Datenflussdiagramm, AVV, SCC, TOM-Konzept

Versionsverzeichnis
| Version | Datum | Aenderung | Autor | Freigabe |

Zugriffskonzept
- Lesend: [Liste der berechtigten Personen]
- Schreibend: [Verantwortlicher, DSB, dokumentierender Mitarbeiter]
- Aufsichtsbehoerde: auf Anforderung Vollzugriff
```

## Aufbewahrungsregeln

- DSFA muss waehrend der gesamten Dauer der Verarbeitungstaetigkeit aufbewahrt werden.
- Nach Ende der Verarbeitung mindestens fuer den Zeitraum etwaiger Anspruchsverjaehrungen (Art. 82 DSGVO; immaterieller Schaden) — Empfehlung: 5 Jahre nach Ende der Verarbeitung; bei oeffentlichen Stellen oft 10 Jahre.
- Alte Versionen nicht loeschen, sondern archivieren.
- Bei Anbieterwechsel: Uebergabe der Akte einschliesslich aller Versionen.
- Bei steuerlich relevanten Verarbeitungen ggf. § 147 AO 10 Jahre.

## Beweiswertkriterien

- Datierung und Unterschrift jedes Dokuments
- Versionierung und Aenderungshistorie
- Klare Autorenschaft (Wer hat dokumentiert, wer hat beschlossen?)
- DSB-Anhoerung dokumentiert mit Datum
- Quellenverzeichnis (Aufsichtshinweise, Leitlinien, Rechtsprechung)
- Verweis auf Verarbeitungsverzeichnis und AVV

## Typische Fehler

- DSFA wird im Mail-Anhang verteilt, aber nicht in einer strukturierten Akte gefuehrt.
- Versionen werden ueberschrieben — alte Versionen unwiederbringlich verloren.
- DSB-Stellungnahme nur muendlich — kein Nachweis.
- Aktenzeichen fehlt — DSFA nicht zuordenbar.
- Aufbewahrungsfrist nicht definiert — DSFA wird mit Mitarbeiter-Personalakte vernichtet.
- Zugriffsrechte ungeregelt — DSFA mit personenbezogenen Risikobeschreibungen offen einsehbar.
- Beweismittel (Datenflussdiagramm) nicht beigefuegt — DSFA bleibt abstrakt.

## Querverweise

- `datenschutzrecht/skills/dsfa-template-deutsch-vollvorlage/SKILL.md` — Vollvorlage
- `datenschutzrecht/skills/dsfa-update-bei-aenderungen-und-revision/SKILL.md` — Versionierung
- `datenschutzrecht/skills/verarbeitungsverzeichnis-vvt-generator/SKILL.md` — VV Art. 30 Verlinkung
- `datenschutzrecht/skills/spezial-dpia-dokumentenmatrix-und-lueckenliste/SKILL.md` — Dokumentenmatrix
- `datenschutzrecht/skills/spezial-datenschutzrecht-compliance-dokumentation-und-akte/SKILL.md` — Aktenfuehrung allg.
- `references/zitierweise.md` — Zitierweise

## Quellen Stand 06/2026

- Art. 5 Abs. 2 DSGVO
- Art. 24, 30, 35, 58, 82 DSGVO
- § 147 AO; § 257 HGB (Bezugsfristen)
- EDSA-Leitlinien WP 248 rev.01
- BfDI / Landesbehoerden — Hinweise zur Rechenschaftspflicht
- Rechtsprechung: keine Entscheidung aus Modellwissen zitieren; vor Ausgabe verifizieren
- Literatur: Kommentar- und Aufsatzfundstellen nur bei eigener Quelle
