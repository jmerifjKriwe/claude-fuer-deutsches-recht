---
name: workflow-rechtsquellen-livecheck
description: "Rechtsquellen-Livecheck für das Plugin gewerblicher-rechtsschutz: Systematisches Vorgehen beim Prüfen von Normen, Rechtsprechung und Behördenpraxis in Echtzeit. Welche Quellen für welche Frage; wie man Modellwissen von Live-Daten unterscheidet."
---

# Workflow: Rechtsquellen-Livecheck

## Zweck

Dieser Skill gibt das **systematische Vorgehen beim Rechtsquellen-Livecheck** vor. Im gewerblichen Rechtsschutz ändern sich Normen, Behördengebühren, Verfahrenspraxis und Rechtsprechung laufend. Modellwissen allein ist zu unzuverlässig für tragfähige juristische Aussagen.

Mandatsbezug: Anwalt will Normtext oder Rechtsprechung zitieren; er prüft zuerst die Live-Quelle, bevor er eine Aussage macht. Oder: Mandant fragt nach aktuellen DPMA-Gebühren; Anwalt prüft nicht aus dem Kopf, sondern live.

## Wann ist ein Livecheck zwingend?

### Zwingend live prüfen:

- Aktueller Normtext (Gesetzesänderungen, Novellen, EU-Richtlinien-Umsetzungen).
- Behördengebühren (DPMA, EUIPO, EPA – ändern sich regelmäßig).
- Fristen (besonders: aktuelle EUIPO-Praxis, gerichtliche Fristen nach Verfahrensreformen).
- Rechtsprechung, die für eine tragende Aussage zitiert werden soll.
- Status eines laufenden Verfahrens (Eintragung, Widerspruch, Einspruch).
- Laufzeit eines Schutzrechts (Jahresgebühren, Verlängerungsstatus).

### Aus Modellwissen akzeptabel (mit Vorbehalt):

- Grundstruktur eines Verfahrens (Wie funktioniert DPMA-Widerspruch generell?).
- Typische Fristenrahmen (z.B. „Widerspruchsfrist ist üblicherweise 3 Monate bei MarkenG").
- Allgemeine Rechtsgrundsätze (Verwechslungsgefahr, Wechselwirkungstheorem).

**Wichtig:** Aussagen aus Modellwissen müssen als solche gekennzeichnet werden, wenn keine Live-Prüfung erfolgt ist.

## Live-Quellenmatrix

### Normen und Gesetze

| Quelle | Inhalt | URL |
|---|---|---|
| gesetze-im-internet.de | Deutsche Bundesgesetze aktuell | [gesetze-im-internet.de](https://www.gesetze-im-internet.de) |
| dejure.org | Deutsche Gesetze mit Verlinkungen | [dejure.org/gesetze](https://dejure.org/gesetze) |
| eur-lex.europa.eu | EU-Recht (Verordnungen, Richtlinien) | [eur-lex.europa.eu](https://eur-lex.europa.eu) |
| bundesgerichtshof.de | BGH-Entscheidungen | [bundesgerichtshof.de](https://www.bundesgerichtshof.de) |
| bundesverfassungsgericht.de | BVerfG-Entscheidungen | [bundesverfassungsgericht.de](https://www.bundesverfassungsgericht.de) |

### Rechtsprechung

| Quelle | Inhalt | URL |
|---|---|---|
| openjur.de | Deutsche Gerichtsurteile (frei) | [openjur.de](https://openjur.de) |
| curia.europa.eu | EuGH / EuG Entscheidungen | [curia.europa.eu](https://curia.europa.eu) |
| bundespatentgericht.de | BPatG Entscheidungen | [bundespatentgericht.de](https://www.bundespatentgericht.de) |
| bundesgerichtshof.de | BGH-Urteile + Leitsätze | [bundesgerichtshof.de](https://www.bundesgerichtshof.de) |

### Behörden und Register

| Quelle | Inhalt | URL |
|---|---|---|
| dpma.de | DPMA: Gebühren, Formulare, Verfahren | [dpma.de](https://www.dpma.de) |
| dpmaregister.dpma.de | DPMA-Marken- und Patentregister | [dpmaregister.dpma.de](https://dpmaregister.dpma.de) |
| euipo.europa.eu | EUIPO: Gebühren, Fristen, eSearch | [euipo.europa.eu](https://www.euipo.europa.eu) |
| epo.org | EPA: Patente, Verfahren, Gebühren | [epo.org](https://www.epo.org) |
| wipo.int | WIPO: UDRP, IR-Marke, PCT | [wipo.int](https://www.wipo.int) |
| handelsregister.de | Handelsregister Deutschland | [handelsregister.de](https://www.handelsregister.de) |
| schutzschriftenregister.de | ZSSR Schutzschriften | [schutzschriftenregister.de](https://www.schutzschriftenregister.de) |

### Patentdatenbanken

| Quelle | Inhalt | URL |
|---|---|---|
| worldwide.espacenet.com | Europäische und internationale Patente | [worldwide.espacenet.com](https://worldwide.espacenet.com) |
| depatisnet.dpma.de | DPMA Patentrecherche Profi-Tool | [depatisnet.dpma.de](https://depatisnet.dpma.de) |
| patents.google.com | Google Patents: schnelle Volltext-Suche | [patents.google.com](https://patents.google.com) |
| patentscope.wipo.int | PCT-Anmeldungen und Nationales | [patentscope.wipo.int](https://patentscope.wipo.int) |

## Livecheck-Protokoll

Für jede Aussage, die auf einer Live-Quelle beruhen muss:

```
LIVECHECK-PROTOKOLL
Aussage: [Was soll geprüft werden]
Quelle: [URL]
Datum des Checks: [Datum]
Ergebnis: [Was wurde gefunden / nicht gefunden]
Verwertbarkeit: [Aussage gesichert / Lücke / Vorbehalt nötig]
```

## Zitierpflicht nach Live-Check

Nach einem Live-Check jede Aussage so zitieren:

- Norm: „§ 42 Abs. 1 MarkenG (Stand: gesetze-im-internet.de, geprüft am [Datum])"
- Rechtsprechung: „BGH, Urteil vom [Datum], AZ [AZ], [bgh.de]"
- Behördeninfo: „DPMA-Gebührenübersicht, geprüft am [Datum], [dpma.de/service/gebuehren]"

## Was dieser Skill nicht macht

- Er ersetzt nicht den inhaltlichen IP-Sachverstand.
- Er gibt keine Bewertung, ob eine Rechtsprechung richtig oder angemessen ist.
- Er überprüft nicht, ob Aussagen aus dem Modellwissen inhaltlich korrekt sind – das muss die Fachperson tun.

## Quellenregel (dieses Skills)

- Dieser Skill selbst ist ein Prozess-Skill; er verweist auf externe Live-Quellen.
- Alle oben genannten URLs müssen zum Zeitpunkt des Checks tatsächlich aufgerufen werden.

## Anschluss-Skills

- `spezial-patentscreening-livequellen-und-rechtsprechungscheck` – Patentrecherche Live
- `spezial-markenrecherche-risikoampel-und-gegenargumente` – Markenrecherche
- `spezial-source-red-team-und-qualitaetskontrolle` – Qualitätskontrolle
- `workflow-redteam-qualitygate` – Red-Team-Gate
