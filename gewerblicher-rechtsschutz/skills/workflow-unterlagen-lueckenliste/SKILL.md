---
name: workflow-unterlagen-lueckenliste
description: Unterlagen-Lückenliste für IP-Mandate – systematische Erfassung fehlender Dokumente, Mandantenabfrage und Lückenschluss vor Einreichung oder Schriftsatzfertigung.
---

# Workflow: Unterlagen-Lückenliste

## Zweck und Mandatsbezug

Jedes IP-Mandat – ob Abmahnung, einstweilige Verfügung, Markenanmeldung, Verletzungsklage
oder Lizenzverhandlung – steht und fällt mit der Vollständigkeit der Unterlagen. Fehlende
Prioritätsnachweise, unvollständige Registerauszüge, nicht gesicherte Verletzungsbelege
oder fehlende Vollmachten können Fristen reißen, Anträge scheitern lassen oder die
Glaubhaftmachung im Eilverfahren gefährden.

Dieser Skill steuert den strukturierten Abgleich zwischen vorhandenen und benötigten
Unterlagen. Er erzeugt eine priorisierte Lückenliste, formuliert gezielte Mandantenanfragen
und gibt Hinweise auf Beschaffungswege (DPMA-Datenbank, EUIPO-Register, EPO-Register,
Gerichtsvollzieher, Notariat, beglaubigte Übersetzungen).

Einsatz: Zu Mandatsbeginn (Intake), vor jedem Einreichungstermin, nach Gegnerangriff
(wenn neue Dokumente erforderlich werden) und bei Mandatsübergabe.

---

## Rechtlicher Rahmen

### Normen mit Relevanz für Dokumentenpflichten

| Norm | Inhalt | Quelle |
|------|--------|--------|
| § 12 ZPO | Gerichtsstand und Klagevoraussetzungen | https://dejure.org/gesetze/ZPO/12.html |
| § 253 ZPO | Klageschrift – Mindestinhalt und Beweismittel | https://dejure.org/gesetze/ZPO/253.html |
| § 920 ZPO | Verfügungsantrag – Glaubhaftmachung | https://dejure.org/gesetze/ZPO/920.html |
| § 294 ZPO | Glaubhaftmachung – zulässige Beweismittel | https://dejure.org/gesetze/ZPO/294.html |
| § 936 ZPO | Anwendung der Arrestvorschriften auf eV | https://dejure.org/gesetze/ZPO/936.html |
| § 80 ZPO | Vollmacht – Form und Nachweis | https://dejure.org/gesetze/ZPO/80.html |
| § 4 MarkenG | Entstehung des Markenschutzes | https://dejure.org/gesetze/MarkenG/4.html |
| § 14 MarkenG | Ausschließliches Recht des Markeninhabers | https://dejure.org/gesetze/MarkenG/14.html |
| § 17 MarkenG | Übertragung und Lizenz | https://dejure.org/gesetze/MarkenG/17.html |
| § 30 PatG | Anmeldung – Erforderliche Angaben | https://dejure.org/gesetze/PatG/30.html |
| § 7 DesignG | Designinhaber und Übertragung | https://dejure.org/gesetze/DesignG/7.html |
| § 10 UrhG | Vermutung der Urheberschaft | https://dejure.org/gesetze/UrhG/10.html |
| § 4 GeschGehG | Maßnahmen zum Schutz von Geschäftsgeheimnissen | https://dejure.org/gesetze/GeschGehG/4.html |
| Art. 18 UMV | Benutzungsnachweis Unionsmarke | https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:02017R1001-20190101 |

---

## Kaltstart-Fragen

Bevor die Lückenliste erstellt wird, kläre:

1. **Mandatstyp**: Abmahnung, einstweilige Verfügung, Hauptsacheklage, Markenanmeldung,
   Lizenzverhandlung, Widerspruch, Nichtigkeitsverfahren oder anderes?
2. **Schutzrechtsart**: Marke, Patent, Gebrauchsmuster, Design, Urheberrecht,
   Geschäftsgeheimnis, UWG-Verstoß – oder Kombination?
3. **Registerlage**: Sind Registerauszüge (DPMA/EUIPO/EPO) bereits vorhanden und aktuell
   (max. 4 Wochen alt für Eilverfahren)?
4. **Verletzungsbelege**: Screenshot, Testkauf, eidesstattliche Versicherung des Mandanten,
   Detektivbericht – was liegt vor?
5. **Vollmacht**: Prozessvollmacht oder nur Beratungsauftrag? Liegt Originalvollmacht vor?
6. **Fristen**: Gibt es laufende Fristen (Widerspruchsfrist, Klagefrist, Erneuerungsfrist),
   die den Dokumentenbedarf zeitlich priorisieren?
7. **Auslandsbezug**: Sind Dokumente in Fremdsprache vorhanden – liegt beglaubigte
   Übersetzung vor oder muss sie beauftragt werden?
8. **Priorität**: Bei Marken-/Patentanmeldung – wird Priorität aus einer Voranmeldung
   beansprucht? Liegt die Prioritätsurkunde vor?

---

## Prüfprogramm: Lückenliste erstellen

### Schritt 1 – Dokumenten-Ist-Aufnahme

Erfasse alle vorliegenden Unterlagen und kategorisiere sie:

- **Schutzrechtsdokumente**: Eintragungsurkunden, Registerauszüge, Anmeldebestätigungen,
  Verlängerungsnachweise, Lizenzverträge, Übertragungsurkunden
- **Verletzungsdokumente**: Screenshots (mit Zeitstempel und URL), Testkaufbelege,
  Produktfotos, Kataloge, eidesstattliche Versicherungen, Detektivberichte
- **Verfahrensdokumente**: Abmahnschreiben und Antworten, frühere Gerichtsentscheidungen,
  Vergleiche, Unterlassungserklärungen
- **Mandantendokumente**: Vollmacht, Handelsregisterauszug (max. 3 Monate alt),
  Gesellschaftsvertrag bei Sondervollmacht, Geschäftsführerbestellung
- **Korrespondenz**: Gegnerische Schreiben, E-Mails, Abmahnungen an Mandanten

### Schritt 2 – Soll-Profil nach Mandatstyp

**Einstweilige Verfügung (Dringlichkeit!):**
- [ ] Registerauszug (max. 4 Wochen): DPMA / EUIPO / EPO
- [ ] Verletzungsbeleg mit Datum (Screenshot + Metadaten, Testkauf + Quittung)
- [ ] Eidesstattliche Versicherung des Mandanten zur Verletzung und Dringlichkeit
- [ ] Vollmacht (Original oder beglaubigte Kopie)
- [ ] Nachweis der Aktivlegitimation (Inhaber = Mandant? Lizenznehmerkette?)
- [ ] Bei Marke: Benutzungsnachweis wenn älter als 5 Jahre (Art. 18 UMV / § 26 MarkenG)

**Abmahnung:**
- [ ] Registerauszug oder Benutzungsnachweis
- [ ] Verletzungsbeleg (Datum, Kontext, Umfang)
- [ ] Vollmacht oder Vollmachtsnachweis
- [ ] Geschäftswert-Grundlagen (Umsatzdaten, Marktstellung)
- [ ] Frühere Kontakte/Abmahnungen (Wiederholungsgefahr)

**Markenanmeldung:**
- [ ] Wiedergabe des Zeichens (Wort, Bild, Kombination – druckfähige Qualität)
- [ ] Waren-/Dienstleistungsverzeichnis (nach Nizza-Klassen)
- [ ] Nachweis der Priorität falls beansprucht (Voranmeldedatum, Aktenzeichen)
- [ ] Vollmacht für DPMA oder EUIPO
- [ ] Handelsregisterauszug bei juristischen Personen

**Verletzungsklage (Hauptsache):**
- [ ] Alle EV-Dokumente (s. oben), ergänzt um:
- [ ] Schadensberechnung (Lizenzanalogie, Verletzergewinn, konkreter Schaden)
- [ ] Buchauszug oder Auskunftsanspruchsdokumentation
- [ ] Gutachten falls technische Fragen streitig
- [ ] Gerichtsvollzieherprotokoll bei Beschlagnahme

**Widerspruch / Nichtigkeitsverfahren:**
- [ ] Widerspruchsmarke: Registerauszug, Benutzungsnachweis (5-Jahres-Zeitraum)
- [ ] Angegriffene Marke: Registerauszug
- [ ] Widersprechende Kennzeichnung: Nachweis des Benutzungsbeginns

### Schritt 3 – Lücken identifizieren und priorisieren

Erstelle dreistufige Prioritätsliste:

**KRITISCH (ohne diese Unterlage scheitert das Verfahren):**
- Beispiele: fehlende Vollmacht, kein Registerauszug, kein Verletzungsbeleg

**WICHTIG (ohne diese Unterlage droht Schwächung der Position):**
- Beispiele: kein Benutzungsnachweis bei älterer Marke, keine eidesstattliche Versicherung
  zur Dringlichkeit, unvollständiger Handelsregisterauszug

**ERGÄNZEND (stärken die Position, sind aber verzichtbar):**
- Beispiele: zusätzliche Verletzungsbelege, wirtschaftliche Kennzahlen zum Schaden,
  parallele ausländische Registerauszüge

### Schritt 4 – Beschaffungswege

| Dokument | Quelle | Zeitbedarf | Hinweise |
|----------|--------|------------|----------|
| DPMA-Registerauszug | https://www.dpma.de/dpmaregister | sofort | DPMAregister online |
| EUIPO-Registerauszug | https://www.euipo.europa.eu/eSearch | sofort | eSearch Plus |
| EPO-Registerauszug | https://www.epo.org/en/searching-for-patents/technical/espacenet | sofort | Espacenet |
| Handelsregisterauszug | https://www.handelsregister.de | sofort | amtliches Dokument |
| Beglaubigte Übersetzung | Beeidigte/r Übersetzer/in | 2–7 Tage | Eilservice möglich |
| Gerichtsvollzieherprotokoll | Zuständiges Vollstreckungsgericht | variabel | §§ 753 ff. ZPO |
| Eidesstattliche Versicherung | Mandant / Notar | 1–2 Tage | Form: §§ 478, 479 ZPO |
| Testkaufbericht | Detektiv / eigener Testkauf | 1–5 Tage | Dokumentationspflicht |

### Schritt 5 – Mandantenanfrage formulieren

Strukturiere die Anfrage nach Dringlichkeit:

```
Betreff: Unterlagen für [Mandatstyp] – [Schutzrecht/Aktenzeichen]

Sehr geehrte/r [Mandant],

für die Bearbeitung Ihres Mandats benötigen wir noch folgende Unterlagen.
Bitte übermitteln Sie die als KRITISCH markierten Dokumente bis [Datum/Uhrzeit]:

KRITISCH (bis [Datum]):
• [Dokument 1] – [Beschaffungshinweis]
• [Dokument 2] – [Beschaffungshinweis]

WICHTIG (bis [Datum+2 Tage]):
• [Dokument 3]

ERGÄNZEND (sobald möglich):
• [Dokument 4]

Bei Fragen zur Beschaffung stehen wir gerne zur Verfügung.
```

---

## Typische Fallen

**Registerauszug zu alt**: Im Eilverfahren akzeptieren viele Gerichte nur Auszüge der letzten
4 Wochen. Älteren Auszüge führen zu Glaubhaftmachungsproblemen. Auszug unmittelbar vor
Antragstellung aktualisieren.

**Aktivlegitimation ungeklärt**: Mandant ist nicht (mehr) eingetragener Inhaber – z. B.
nach Umfirmierung, Verschmelzung oder Übertragung ohne Umschreibung im Register. Immer
Registerstand mit Mandantenangaben abgleichen.

**Lizenznehmerkette unterbrochen**: Mandant hat Unterlizenz, aber die Hauptlizenz ist nicht
dokumentiert oder der Lizenzvertrag enthält kein Klagerecht. Vollständige Kette prüfen.

**Benutzungsnachweis fehlt**: Bei Marken älter als 5 Jahre (§ 26 MarkenG, Art. 18 UMV) kann
Gegner Nichtbenutzungseinrede erheben. Benutzungsbelege (Rechnungen, Werbemittel, Fotos mit
Datum) müssen lückenlos den relevanten Zeitraum abdecken.

**Verletzungsbeleg ohne Datum**: Screenshots ohne Zeitstempel oder URL sind im Verfahren
kaum verwertbar. Immer Wayback-Machine-Archiv oder notarielle Sicherung einplanen.

**Vollmacht nicht ausreichend**: Allgemeine Vollmacht deckt nicht alle Verfahrenshandlungen.
Bei DPMA, EUIPO, Gericht jeweils spezifische Anforderungen prüfen.

**Übersetzungsfrist unterschätzt**: Beglaubigte Übersetzungen bei Auslandsbezug (WIPO,
EUIPO-Widerspruch, ausländisches Prioritätsdokument) brauchen Zeit – früh beauftragen.

---

## Output-Module

| Modul | Format | Inhalt |
|-------|--------|--------|
| Lückenliste (intern) | Tabelle / Checkliste | Alle fehlenden Dokumente mit Priorität und Deadline |
| Mandantenanfrage | E-Mail-Entwurf | Strukturiert nach Dringlichkeit, mit Beschaffungshinweisen |
| Beschaffungsnotiz | Kurzvermerk | Welche Dokumente Anwaltskanzlei selbst beschafft (DPMA etc.) |
| Fristennotiz | Fristenliste | Dokumentenfristen eingetragen in Wiedervorlage |
| Vollständigkeitsvermerk | Abhakliste | Bestätigung nach Eingang aller kritischen Unterlagen |

---

## Quellenregel

Ausschließlich folgende Quellen für Normen und Rechtsprechung verwenden:

- Gesetze: https://www.gesetze-im-internet.de
- Normen (verlinkt): https://dejure.org/gesetze
- BGH-Rechtsprechung: https://www.bundesgerichtshof.de
- BVerfG: https://www.bundesverfassungsgericht.de
- BPatG: https://www.bundespatentgericht.de
- EU-Recht: https://eur-lex.europa.eu
- EuGH: https://curia.europa.eu
- DPMA (Register + Formulare): https://www.dpma.de
- EUIPO: https://www.euipo.europa.eu
- EPO: https://www.epo.org
- WIPO: https://www.wipo.int
- Entscheidungen (offen): https://openjur.de

Keine allgemeinen Rechtsdatenbanken, keine Verlage, keine Kommentarseiten ohne
primärquellennahen Beleg.

---

## Anschluss-Skills

- `workflow-dokumentenintake` – Ersterfassung eingehender Unterlagen zu Mandatsbeginn
- `workflow-fristen-und-risikoampel` – Fristen aus Dokumentenlage ableiten und überwachen
- `workflow-kaltstart-und-routing` – Mandatstyp bestimmen und Lückenliste auslösen
- `workflow-redteam-qualitygate` – Vollständigkeit und Qualität der Unterlagen prüfen
- `spezial-abmahnung-compliance-dokumentation-und-akte` – Aktenaufbau nach Dokumenteneingang
- `spezial-dpma-fristen-form-und-zustaendigkeit` – DPMA-spezifische Dokumentenanforderungen
- `spezial-euipo-dokumentenmatrix-und-lueckenliste` – EUIPO-Verfahren: Dokumentenmatrix
- `evvollzug-neu-001-einstweilige-verfuegung-vollziehung-frist-und-parteizustellung` – EV-Vollzug nach Dokumenteneingang
