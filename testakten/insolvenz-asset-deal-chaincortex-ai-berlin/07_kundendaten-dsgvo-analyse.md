# 07 — Kundendaten — DSGVO-Risikoanalyse (B2B vs. B2C)

> Auftrag: Prüfung, unter welchen Voraussetzungen die Kundendaten der Schuldnerin im Asset Deal an die Voracis Ventures GmbH übertragen werden dürfen. Ergebnisrelevant für APA-§ 2 (Kaufgegenstände) und das Anschreiben Privatkunden. Verfasst durch RAin Beate Lottberg, gegengeprüft durch externen Datenschutzbeauftragten Dr. Heiko Manderscheid (Voracis-Seite), Datum 14.06.2026.

## 1. Sachverhalt der Kundendaten

Die Schuldnerin betrieb das SaaS-Produkt „ChainCortex Compliance Engine" mit zwei klar abgrenzbaren Kundenklassen:

- **Business-Tarif** (12 Verträge): juristische Personen — siehe `xlsx/kundendaten-business.xlsx`. Datenfelder: Firmenname, Anschrift, Branche, Ansprechpartner (Vor-/Nachname, dienstliche E-Mail, Funktion), Vertragsdaten.
- **Privat-/Freemium-Tarif** (8 Verträge): natürliche Personen — siehe `xlsx/kundendaten-privat.xlsx`. Datenfelder: Klar-Vor- und -Nachname, private E-Mail, Anschrift (privat), Geburtsjahr (für KYC light), Sprachpräferenz, Vertragsdaten.

## 2. Maßgebliche Rechtsgrundlagen

| Norm | Inhalt | Anwendbar |
|---|---|---|
| Art. 4 Nr. 1 DSGVO | Personenbezogene Daten | nur B2C voll; B2B-Ansprechpartner-Daten teilweise (EDPB Guidelines 03/2022) |
| Art. 4 Nr. 2 DSGVO | „Verarbeitung" — auch Übermittlung | ja, der Asset Deal ist eine Übermittlung |
| Art. 4 Nr. 9 DSGVO | „Empfänger" | Voracis ist Empfänger |
| Art. 6 I lit. f DSGVO | berechtigtes Interesse als RG | grundsätzlich ja, aber strenges Abwägungsergebnis |
| Art. 13/14 DSGVO | Informationspflicht | ja, Art. 14 (Daten nicht direkt vom Betroffenen erhoben durch Voracis) |
| Art. 28 DSGVO | Auftragsverarbeitung | nicht einschlägig — Voracis wird **Verantwortlicher**, nicht AV |
| § 26 BDSG | Beschäftigtendaten | für AN-Daten relevant — separat in `08_…` |
| § 25 TTDSG | Cookies/Endeinrichtungs-Zugriff | nicht direkt relevant |

## 3. Maßgebliche Rechtsprechung

| Entscheidung | Inhalt | Bewertung für Asset Deal |
|---|---|---|
| EuGH **C-732/22** (Bonprix, Urt. v. 26.09.2024) | Personenbezogene Daten aus Asset Deal — Rechtsgrundlage Art. 6 I lit. f DSGVO grundsätzlich denkbar, aber strenger Maßstab bei der Interessenabwägung; Informationspflicht nach Art. 14 zwingend; Widerspruchsmöglichkeit unverzichtbar | **Leitentscheidung**, daran ist sich auszurichten |
| EuGH **C-621/22** (Koninklijke Nederlandse Lawn Tennisbond, Urt. v. 04.10.2024) | „Berechtigtes Interesse" auch wirtschaftlich; aber konkrete Erforderlichkeit + Interessenabwägung | bestätigt Linie |
| EuGH **C-184/20** (Vyriausioji tarnybinės etikos komisija) | Bei Verarbeitung „sensibler" Daten erhöhte Anforderungen | hier nicht einschlägig (keine besonderen Kategorien) |
| OLG Düsseldorf 16. ZS, 23.11.2023 — VI-W (Kart) 4/22 (DSGVO im Asset Deal) | Übermittlung im Asset Deal grundsätzlich zulässig, aber „informierte Übertragung" mit echter Widerspruchsmöglichkeit | bestätigt Praxis |
| BfDI-Stellungnahme „Asset Deals mit personenbezogenen Daten" v. 12.02.2024 | Empfehlung: Information vor Übermittlung, 30-Tage-Widerspruchsfrist | Best Practice; im APA und in `eml/…` berücksichtigt |

## 4. B2B — Bewertung

Reine Firmendaten (juristische Personen, Firmenname, Anschrift) sind **keine personenbezogenen Daten** i. S. d. Art. 4 Nr. 1 DSGVO. Die dazu erfassten Ansprechpartner-Daten (Vor-/Nachname, dienstliche E-Mail, Funktion) sind jedoch **personenbezogen**. Dafür gilt:

- Rechtsgrundlage: Art. 6 I lit. f DSGVO + § 28 BDSG entfällt seit 2018, jetzt vollständig DSGVO.
- Interessenabwägung: Übermittlung dient der **Fortführung der Geschäftsbeziehung** im Sinne und Interesse des Kunden; Auftraggeber-Ansprechpartner haben typischerweise eine geringere Schutzbedarfslage (Daten erscheinen ohnehin auf Visitenkarten, in Signaturen).
- Information nach Art. 14 DSGVO: trotzdem zwingend (E-Mail-Vorlage in `eml/dsgvo-information-b2b-ansprechpartner.eml`).
- Widerspruchsmöglichkeit: ja, aber wird typischerweise nicht ausgeübt.

**Ergebnis B2B:** Übertragung im APA ohne Widerspruchsfrist möglich; Information nach Art. 14 DSGVO begleitend.

## 5. B2C — Bewertung

Die 8 Privatkunden sind eindeutige Betroffene. Übermittlung an Voracis ist Verarbeitung i. S. d. Art. 4 Nr. 2 DSGVO. Folgendes Vorgehen:

### 5.1 Rechtsgrundlage Art. 6 I lit. f DSGVO

**Interessenabwägung:**

- Voracis-Interesse: Geschäftsfortführung, Wert der erworbenen Kundenbasis. EuGH C-732/22: wirtschaftliches Interesse anerkannt.
- Betroffenen-Interesse: Schutz vor unkontrollierter Datenübermittlung. Hier in mitigierter Form: a) gleicher Vertragsgegenstand, b) gleiche Datennutzung, c) Voracis ist DSGVO-konform organisiert (Datenschutzbeauftragter, DPIA vom 10.06.2026, Stellungnahme 2-seitig).
- **Erforderlichkeit:** Ohne Datenübernahme stürzt der Service der 8 Privatkunden ab → Service-Verlust. Datenübernahme ist erforderlich, mildere Mittel nicht praktikabel.
- **Strikte Zweckbindung:** Voracis verarbeitet die Daten ausschließlich für die Fortführung des bestehenden Vertragsverhältnisses; keine Profilierung, kein Marketing ohne separate Einwilligung.

### 5.2 Information nach Art. 14 DSGVO

Schreiben an alle 8 Privatkunden bis spätestens **20.06.2026** (1 Monat vor Übernahmestichtag), gemeinsam unterzeichnet von Schuldner-Vertreter (Verwalter) und Käufer-Verantwortlichem (Voracis-DSB Manderscheid). Inhalt:

1. Identität des neuen Verantwortlichen (Voracis Ventures GmbH, Anschrift, DSB-Kontakt).
2. Kategorien betroffener Daten.
3. Rechtsgrundlage Art. 6 I lit. f DSGVO sowie Hinweis auf Interessenabwägung.
4. Empfänger (keine Drittübermittlungen außerhalb des Datenraums).
5. Speicherdauer.
6. Rechte: Auskunft (Art. 15), Berichtigung (Art. 16), Löschung (Art. 17), Einschränkung (Art. 18), Datenübertragbarkeit (Art. 20), **Widerspruch (Art. 21)**, Beschwerde bei Aufsichtsbehörde (Art. 77).
7. Quelle der Daten (Schuldnerin ChainCortex AI GmbH i. Ins.).
8. **Widerspruchsfrist 30 Kalendertage** (bis 20.07.2026 inkl.). Bei Widerspruch: Datenlöschung durch Voracis innerhalb von 7 Werktagen, vorab Datenexport für Betroffenen ermöglicht.

E-Mail-Entwurf siehe `eml/dsgvo-information-b2c-privatkunden-entwurf.eml`. Postversand parallel (für Anschriftenpflege).

### 5.3 Vertragsklausel APA

In den Asset-Purchase-Agreement-Text wird in **§ 2 Abs. 4** explizit aufgenommen, dass die Übertragung der Kundendaten erst nach Ablauf der 30-Tages-Widerspruchsfrist abgeschlossen ist und der Käufer die widersprechenden Betroffenen unverzüglich aus dem CRM-System löscht; Verwalter haftet nicht für nachträgliche Löschungsfolgen.

## 6. Beschäftigtendaten (AN-Übergang)

§ 26 BDSG i. V. m. § 613a BGB: Datentransfer im Rahmen des Betriebsübergangs ist erforderlich für die Begründung des neuen Arbeitsverhältnisses und § 26 I 1 BDSG-konform. Informationspflicht aus § 13 BDSG erfüllt durch die § 613a V BGB-Unterrichtung (siehe `08_…`).

## 7. Ergebnis und Risikoampel

| Komponente | Ampel | Begründung |
|---|---|---|
| Übertragung B2B-Firmendaten | 🟢 | keine personenbezogenen Daten; Ansprechpartner-Übermittlung gerechtfertigt |
| Übertragung B2B-Ansprechpartner-Daten | 🟢 | Art. 6 I lit. f DSGVO, Information nach Art. 14 ausreichend |
| Übertragung B2C-Privatkunden-Daten | 🟠 | Art. 6 I lit. f möglich, aber zwingend 30-Tages-Widerspruchsfrist + Art. 14-Info; Bußgeldrisiko bei Verzicht: Art. 83 IV DSGVO bis 10 Mio. EUR oder 2 % Konzernumsatz |
| AN-Daten (10 Übergänge) | 🟢 | § 26 BDSG + § 613a BGB; mit § 613a V-Schreiben erledigt |
| Cookies / Tracking-Daten | 🟢 | wurden nicht im SaaS gesetzt; nicht Asset-Deal-Gegenstand |

## 8. Drei vorbehaltliche Schlussempfehlungen

1. **Vertragsklausel** zur 30-Tages-Widerspruchsfrist im APA aufnehmen — siehe `09_…` § 2 Abs. 4.
2. **Information** an alle Betroffenen (B2B-Ansprechpartner + B2C) bis 20.06.2026 versenden.
3. **Voracis-DPIA** (Datenschutz-Folgenabschätzung, Art. 35 DSGVO) zur Personenkundendaten-Übernahme dokumentieren und im Verzeichnis von Verarbeitungstätigkeiten (Art. 30 DSGVO) eintragen — vor dem Übernahmestichtag.
