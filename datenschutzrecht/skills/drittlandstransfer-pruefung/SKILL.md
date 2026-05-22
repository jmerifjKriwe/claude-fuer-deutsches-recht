---
name: drittlandstransfer-pruefung
description: "Prueft Datenuebermittlungen in Drittlaender nach Art. 44 ff. DSGVO: Angemessenheitsbeschluesse (USA: EU-US Data Privacy Framework 2023, UK, Schweiz), Standardvertragsklauseln (SCC 2021 Module 1 bis 4), Transfer Impact Assessment nach EuGH C-311/18 Schrems II, BCR und Ausnahmen nach Art. 49 DSGVO."
---

# Drittlandstransfer-Prüfung (Art. 44 ff. DSGVO)

## Zweck

Dieser Skill greift bei jeder Auslagerung personenbezogener Daten an Empfaenger ausserhalb der EU/des EWR: US-Cloud-Dienste, Konzernverbund-Transfer, KI-Provider, Sub-Auftragsverarbeiter in Drittstaaten. Er fuehrt strukturiert durch die mehrstufige Pruefung gemaess Kapitel V DSGVO, beruecksichtigt den Angemessenheitsbeschluss vom 10. Juli 2023 fuer die USA (EU-US Data Privacy Framework) sowie die Schrems-II-Anforderungen an Standardvertragsklauseln und ergaenzende Massnahmen.

Anwendungsfaelle: Kanzlei oder Unternehmen moechte einen US-amerikanischen SaaS-Dienst einsetzen; Konzernmutter in der Schweiz soll Zugriff auf EU-Kundendaten erhalten; Auftragsverarbeiter setzt Sub-Auftragsverarbeiter in Indien ein; Drittlandbezug bei AVV-Pruefung erkannt.

## Eingaben

- Empfaengerstaat (z.B. USA, Indien, UK, China)
- Empfaenger: Verantwortlicher (Modul 1/3 SCC) oder Auftragsverarbeiter (Modul 2/4 SCC)
- Datenkategorien (Art. 4 Nr. 1 DSGVO; Art. 9/10 DSGVO-Sonderkategorien?)
- Art der Datenverarbeitung (Speicherung, Analyse, Support-Zugriff, Hosting, Backup)
- Liegt bereits ein Transfer Impact Assessment vor? Falls ja, als Dokument einreichen
- Sitz und DPF-Zertifizierungsstatus des Empfaengers (fuer USA: data.privacyframework.gov pruefen)

## Rechtlicher Rahmen

### Primaernormen

- **Art. 44 DSGVO** – Allgemeines Prinzip: Kein Transfer ohne geeignete Garantien oder Ausnahme; gilt auch fuer Weiterverarbeitung nach Transfer
- **Art. 45 DSGVO** – Angemessenheitsbeschluss der Kommission; kein zusaetzliches Genehmigungserfordernis bei positiver Entscheidung
- **Art. 46 DSGVO** – Geeignete Garantien: Standardvertragsklauseln (SCC), Binding Corporate Rules (BCR), Verhaltensregeln mit verbindlichen Verpflichtungen, Zertifizierungsmechanismen
- **Art. 47 DSGVO** – Verbindliche interne Datenschutzvorschriften (BCR); Genehmigung durch federführende Aufsichtsbehörde erforderlich
- **Art. 49 DSGVO** – Ausnahmen: Einwilligung (Art. 49 Abs. 1 lit. a), Vertragserfordernis (lit. b/c), wichtige Gruende des oeffentlichen Interesses (lit. d), Rechtsansprueche (lit. e), lebenswichtige Interessen (lit. f), oeffentliches Register (lit. g); Abs. 1 Satz 2: gelegentliche, nicht systematische Transfers bei zwingender Notwendigkeit
- **Art. 4 Nr. 23 DSGVO** – Definition „Internationale Organisation"
- **Art. 13 Abs. 1 lit. f, Art. 14 Abs. 1 lit. f DSGVO** – Informationspflicht ueber Drittlandtransfer und Transfermechanismus

### Rechtsprechung und Leitlinien

- **EuGH, Urt. v. 16.07.2020 – C-311/18 (Data Protection Commissioner/Facebook Ireland und Maximillian Schrems), NJW 2020, 2945** (Schrems II): Der EuGH erklaert den EU-US-Privacy-Shield-Angemessenheitsbeschluss fuer ungueltig (Rn. 201). Standardvertragsklauseln bleiben als Transfermechanismus gueltig, jedoch nur dann, wenn der Verantwortliche oder Auftragsverarbeiter vor der Uebermittlung sicherstellt, dass im Drittland ein dem Unionsrecht aequivalentes Schutzniveau gewaehrleistet ist (Rn. 134). Der Verantwortliche muss pruefen, ob das Rechtssystem des Empfaengerlandes einen Schutz bietet, der dem in der Union garantierten Schutzniveau der Sache nach gleichwertig ist; ist dies nicht der Fall, ist die Uebermittlung zu unterlassen (Rn. 142–146). `[Modellwissen – Vollzitat geprueft]`
- **EuGH, Urt. v. 06.10.2015 – C-362/14 (Maximillian Schrems/Data Protection Commissioner), NJW 2015, 3151** (Schrems I): Ungueltigkeitserklaerung des Safe-Harbor-Angemessenheitsbeschlusses; Grundlage fuer Schrems II
- **EDSA, Empfehlungen 01/2020 zu Massnahmen zur Ergaenzung von Uebermittlungsinstrumenten**, angenommen am 18.06.2021 (Version 2.0): Sechsstufige Pruefmethodik fuer Transfer Impact Assessment (TIA); massgeblich fuer die Schrems-II-Umsetzung in der Praxis
- **EDSA, Leitlinien 05/2021 zum Zusammenwirken von Art. 3 und Kapitel V DSGVO**, angenommen am 18.11.2021: Klaerung, wann der raeumliche Anwendungsbereich (Art. 3 DSGVO) und die Drittlandregeln (Kapitel V) kumulativ oder alternativ gelten
- **DSK Orientierungshilfe Drittstaatentransfer**: Handlungsempfehlungen fuer verantwortliche Stellen bei Transfers in Drittlaender; abrufbar auf dskonferenz.de `[Modellwissen – aktuellen Stand pruefen]`

### Aktuelle Angemessenheitsbeschluesse (Stand 05/2026)

| Staat | Beschluss | Hinweis |
|---|---|---|
| **USA** | EU-US Data Privacy Framework, Beschluss der Kommission vom 10.07.2023 (C(2023) 4745 final) | Nur fuer zertifizierte Unternehmen auf der DPF-Liste; Pruefung auf data.privacyframework.gov erforderlich |
| **UK** | Angemessenheitsbeschluss vom 28.06.2021 (Beschluss 2021/1772/EU) | Gilt vorbehaltlich Ueberpruefung; nach Brexit-Aenderungen des britischen Datenschutzrechts beobachten |
| **Schweiz** | Angemessenheitsbeschluss der Kommission; erneuert im Kontext des CH-Datenschutzgesetzes (nDSG, in Kraft ab 01.09.2023) | Teilweiser Angemessenheitsbeschluss; Praxis nach CH-DSG-Reform beachten |
| **Andorra** | Beschluss 2010/625/EU |  |
| **Argentinien** | Beschluss 2003/490/EG |  |
| **Faeroeer** | Beschluss 2010/146/EU |  |
| **Guernsey** | Beschluss 2003/821/EG |  |
| **Isle of Man** | Beschluss 2004/411/EG |  |
| **Israel** | Beschluss 2011/61/EU |  |
| **Japan** | Beschluss vom 23.01.2019 (2019/419/EU) | Mit gegenseitiger Anerkennung; Einschraenkungen beachten |
| **Jersey** | Beschluss 2008/393/EG |  |
| **Kanada** | Beschluss 2002/2/EG | Nur fuer Organisationen, die dem PIPEDA unterliegen; Bundesbehörden ausgenommen |
| **Neuseeland** | Beschluss 2013/65/EU |  |
| **Suedkorea** | Beschluss vom 17.12.2021 (2022/254/EU) | Erster Angemessenheitsbeschluss in Asien ausserhalb Japan |
| **Uruguay** | Beschluss 2012/484/EU |  |

## Ablauf

### 1. Identifizierung des Drittlandstransfers

Pruefen, ob ueberhaupt ein Transfer i.S.d. Kapitel V DSGVO vorliegt:
- Findet eine Uebermittlung an einen Empfaenger ausserhalb EU/EWR statt?
- Genügt ein „Zugriff" (z.B. Remote-Support, Administrationszugang) aus einem Drittland – nach EDSA-Leitlinien 05/2021 ja, wenn personenbezogene Daten im Zugriffsmittelpunkt stehen
- Art. 3 Abs. 2 DSGVO (extraterritoriale Anwendung): Liegt der Empfaenger zwar im Drittland, faellt aber schon unter den raeumlichen Anwendungsbereich der DSGVO? Dann kein Kapitel-V-Transfer, aber Compliance-Prüfung nach Leitlinien 05/2021

### 2. Pruefung Angemessenheitsbeschluss (Art. 45 DSGVO)

- Liegt fuer das Empfaengerland ein gültiger Angemessenheitsbeschluss der Kommission vor? (Tabelle oben)
- **USA:** Ist der Empfaenger auf der DPF-Liste eingetragen und fuer die relevanten Datenkategorien zertifiziert? (data.privacyframework.gov)
- Wenn Angemessenheitsbeschluss vorhanden: Transfer grundsaetzlich zulässig; Art. 13/14 DSGVO-Hinweispflicht beachten
- **Hinweis:** Angemessenheitsbeschluesse koennen durch den EuGH fuer ungueltig erklaert werden (vgl. Schrems I und II); bei politisch sensiblen Laendern Monitoring empfehlen

### 3. Geeignete Garantien (Art. 46 DSGVO) – falls kein Angemessenheitsbeschluss

**a) Standardvertragsklauseln (SCC) nach Beschluss 2021/914/EU:**

| Modul | Konstellation | Typischer Anwendungsfall |
|---|---|---|
| Modul 1 | Verantwortlicher (EU) → Verantwortlicher (Drittland) | Konzerntransfer, gemeinsam Verantwortliche |
| Modul 2 | Verantwortlicher (EU) → Auftragsverarbeiter (Drittland) | Cloud-Dienst, Hosting, Analytics |
| Modul 3 | Auftragsverarbeiter (EU) → Auftragsverarbeiter (Drittland) | Sub-Auftragsverarbeiter |
| Modul 4 | Auftragsverarbeiter (Drittland) → Verantwortlicher (EU) | Ruecktransfer verarbeiteter Daten |

Prüfpunkte bei SCC: Richtiges Modul? Technische Anlage (Anhang I A–C und II) vollstaendig ausgefuellt? Technische Massnahmen (Anhang II TOMs) konkret und nicht pauschal?

**b) Binding Corporate Rules (BCR):**
- Genehmigung durch federführende Aufsichtsbehörde nach Art. 47 DSGVO
- Umfang: alle Konzernunternehmen, die die BCR unterzeichnet haben
- BCR-Update nach Schrems II erforderlich; EDSA-Empfehlungen 01/2020 gelten auch fuer BCR

**c) Verhaltensregeln mit Verpflichtungen (Art. 46 Abs. 2 lit. e DSGVO):**
- Muss von zustaendiger Aufsichtsbehörde genehmigt sein
- In der Praxis bisher wenig verbreitet

**d) Zertifizierungsmechanismen (Art. 46 Abs. 2 lit. f DSGVO):**
- Zertifizierungseinrichtung muss akkreditiert sein; Verpflichtung des Importeurs erforderlich

### 4. Transfer Impact Assessment (TIA) nach Schrems II

Nach EuGH C-311/18 Rn. 134 und EDSA-Empfehlungen 01/2020 muss bei SCC-Transfers geprueft werden, ob das Rechtssystem des Empfaengerlandes die Wirksamkeit der SCC nicht untergrabt.

**TIA Sechsstufige Methodik (EDSA-Empfehlungen 01/2020):**

1. **Schritt 1:** Alle Uebermittlungen kartieren (Zweck, Datenart, Empfaenger, Empfaengerland)
2. **Schritt 2:** Transfermechanismus identifizieren (SCC, BCR etc.)
3. **Schritt 3:** Rechtslage im Empfaengerland beurteilen: Massengesetze (FISA Section 702, USA CLOUD Act), Behoerdenzugriffsrechte, Rechtsschutzmoeglichkeiten fuer Betroffene, Zugang zu unabhaengigen Gerichten
4. **Schritt 4:** Pruefen, ob Recht und Praxis die SCC-Schutzwirkung unterlaufen (Schrems-II-Kriterium: aequivalentes Schutzniveau)
5. **Schritt 5:** Ergaenzende Massnahmen identifizieren und umsetzen (s. Abschnitt 5)
6. **Schritt 6:** Formale Schritte (Vertrag schliessen, ggf. Aufsichtsbehörde informieren, Dokumentation)

### 5. Ergaenzende Massnahmen (EDSA-Empfehlungen 01/2020)

Bei unzureichendem Schutzniveau im Empfaengerland koennen ergaenzende Massnahmen die Schutzluecke schliessen:

**Technische Massnahmen:**
- Ende-zu-Ende-Verschluesselung mit Schluesselhoheit beim Verantwortlichen in der EU (Schluesselmanagement-Standort entscheidend)
- Pseudonymisierung vor Transfer; Zuordnungsschluessel verbleibt in der EU
- Zero-Knowledge-Architektur fuer Cloud-Dienste

**Vertragliche Massnahmen:**
- Erweiterung der SCC um technische Spezifikation der Verschluesselung
- Verpflichtung des Importeurs zur Benachrichtigung bei Behoerdenzugang
- Audit-Rechte fuer Drittland-Compliance

**Organisatorische Massnahmen:**
- Datensparsamkeit: nur pseudonymisierte/aggregierte Daten uebermitteln
- Trennung von Supportzugriff und Produktionsdaten

### 6. Dokumentation und Informationspflichten

- Verarbeitungsverzeichnis (Art. 30 DSGVO): Transfer, Empfaengerland, Mechanismus, TIA vermerken
- Datenschutzerklaerung (Art. 13 Abs. 1 lit. f DSGVO): Drittlandtransfer, Mechanismus und ggf. Kopienangebot der SCC erwaehnen
- AVV (Art. 28 Abs. 3 DSGVO): Sub-AV-Kette mit Drittlandsangaben; TIA als Anlage
- TIA als internes Dokument archivieren und bei Anfragen der Aufsichtsbehörde vorlegen koennen

## Pruefschema TIA (Checkliste)

- [ ] **Lokale Massengesetze:** Erlauben Gesetze des Empfaengerlandes Massensammlung (z.B. FISA 702, EO 12333 fuer USA; Geheimdienstgesetze CN, RU)?
- [ ] **Behoerdenzugriff auf Daten:** Koennen Behoerden ohne richterliche Kontrolle auf Daten zugreifen? Wie haeufig werden solche Befugnisse genutzt (Transparenzberichte)?
- [ ] **Verschluesselung at rest:** Sind Daten beim Empfaenger verschluesselt gespeichert? Wer hat Zugriff auf Schluessel?
- [ ] **Verschluesselung in transit:** Wird TLS/mTLS verwendet? Zertifikate kontrolliert?
- [ ] **Schluesselmanagement-Standort:** Befinden sich Schluessel und HSMs in der EU? Oder Schluesselhoheit beim Empfaenger im Drittland?
- [ ] **Sub-Processor-Mapping:** Welche Sub-Auftragsverarbeiter des Empfaengers befinden sich ebenfalls in Drittlaendern? TIA fuer Sub-Processor?
- [ ] **Rechtsschutz fuer Betroffene:** Haben EU-Betroffene Klagemöglichkeiten im Empfaengerland oder ueber Rechtsbehelfsinstanz (z.B. Data Protection Review Court der USA)?
- [ ] **Transparenzberichte:** Veroeffentlicht der Empfaenger Behördenanfragen (Government Disclosure Reports)?

## Risikoampel

| Konstellation | Rot | Orange | Gruen |
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
   [Unterlaefen lokale Gesetze die SCC-Schutzwirkung? Pruefung nach EuGH C-311/18 Rn. 134 ff.]

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

### Datenschutzerklaerungsbaustein Drittlandtransfer

> „Wir uebermitteln personenbezogene Daten an Empfaenger in [LAND]. Die Uebermittlung erfolgt auf Grundlage von [EU-Standardvertragsklauseln nach Beschluss 2021/914/EU, Modul X / Angemessenheitsbeschluss der Kommission vom [DATUM]]. Fuer die USA gilt: der Empfaenger ist unter dem EU-US Data Privacy Framework zertifiziert. Eine Transferfolgenabschätzung (TIA) liegt vor. Auf Anfrage stellen wir Ihnen eine Kopie der Standardvertragsklauseln zur Verfuegung (Kontakt: [DSB])."

## Querverweise

- `datenschutzrecht/skills/avv-pruefung/SKILL.md` – Drittlandtransfer-Pruefung im AVV-Kontext (Schritt 5)
- `datenschutzrecht/skills/dsfa-erstellung/SKILL.md` – DSFA bei Hochrisiko-Drittlandtransfers
- `datenschutzrecht/skills/mandantendaten-ki/SKILL.md` – Drittlandtransfer bei KI-Diensten fuer Berufsgeheimnistraeger
- `datenschutzrecht/skills/datenpanne-meldung/SKILL.md` – Datenpannen bei Drittlandempfaengern
- `datenschutzrecht/skills/regulierungs-luecken-analyse/SKILL.md` – Neue Angemessenheitsbeschluesse in Gap-Analyse einspielen

## Risiken und typische Fehler

- **DPF-Pruefung vergessen:** DPF-Zertifizierung ist nicht permanent; Unternehmen koennen ihre Zertifizierung verlieren. Vor jedem Transfer auf data.privacyframework.gov pruefen und erneut pruefen bei Vertragserneuerung.
- **Falsches SCC-Modul:** Ein Verantwortlicher, der SCC-Modul 3 (AV-zu-AV) verwendet, obwohl er selbst Verantwortlicher ist, erzeugt keine schutzwirkende Grundlage. Konstellation vor Unterzeichnung zwingend prüfen.
- **TIA als Formalie:** EuGH C-311/18 Rn. 134: Die Pruefung muss ehrlich und konkret sein; pauschal „Risiko akzeptabel" ohne Begruendung genuegt nicht. Transparenzberichte auswerten.
- **Art. 49 DSGVO als Regelfall:** Die Ausnahmen des Art. 49 DSGVO sind auf Einzelfaelle beschraenkt; systematische und regelmaessige Transfers auf dieser Basis sind nicht zulaessig (EDSA-Leitlinien 2/2018).
- **Sub-Processor-Kette uebersehen:** SCC Modul 2/3 legt dem Importeur Pflichten fuer Sub-Auftragsverarbeiter auf; deren Drittlandstatus muss ebenfalls abgesichert sein (Art. 28 Abs. 4 DSGVO).
- **Schluesselhoheit nicht geprueft:** Verschluesselung schuetzt nur dann, wenn Schluessel nicht im Drittland liegen. Cloud-Dienste mit US-Schlüsselmanagement bieten keinen vollstaendigen Schutz gegen FISA 702-Zugriffe.
- **Angemessenheitsbeschluss validitaet nicht geprueft:** Nach Schrems I und II koennen Angemessenheitsbeschluesse wegfallen. Monitoring-Pflicht fuer sensible Verarbeitungen.

## Quellen und Updates

Stand: 05/2026. Aktualitaet bei folgenden Ereignissen pruefen und Skill aktualisieren:
- Neue Angemessenheitsbeschluesse der Europaeischen Kommission
- EuGH-Urteile zu Kapitel V DSGVO
- Aenderungen am DPF (data.privacyframework.gov – politische und rechtliche Entwicklungen USA)
- Neue BCR-Anerkennungen durch Aufsichtsbehörden
- Aktualisierungen der EDSA-Empfehlungen 01/2020
- Oertliche Datenschutzgesetze in Drittlaendern (z.B. CLOUD Act Amendments, neue chinesische Datenschutzgesetze PIPL)

Naechste geplante Ueberpruefung: 05/2027 oder bei wesentlichen Aenderungen.
