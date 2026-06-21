# Relationstechnik Zivilrecht (Praxis-Werkstatt)

> **Experimentelles Plugin im Ordner `_GERICHTE_EXPERIMENTAL/`** — siehe Vorspruch unten.

## Rolle

Jede:r Zivilrechtler:in (Richter, Referendar, Anwalt) der eine grosse Relation aufbauen will

## Rechtsrahmen

ZPO, BGB, HGB, Methodenlehre des Buergerlichen Rechts (Larenz, Wieacker)

## Inhalt

- **20 Skills** (siehe `skills/`)
- **Megaprompt** (`MEGAPROMPT.md`)
- **Miniprompt** (`MINIPROMPT.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-akte-erstdurchsicht-zivil** — Strukturierte Erstdurchsicht der Zivilakte: Parteien identifizieren, Antrag isolieren, Lebenssachverhalt extrahieren, be
- **02-parteivortrag-strukturieren** — Klaeger- und Beklagtenvortrag in Behauptungen, Bestreiten, Nichtwissen Paragraf 138 Abs. 4 ZPO, Gestaendnis Paragraf 288
- **03-streitstand-erfassen** — Streitiger und unstreitiger Sachverhalt heraussortieren, Geltung von Paragraf 138 Abs. 3 ZPO (Gestaendnisfiktion), Bewei
- **04-klage-antrag-auslegen** — Klageantrag auslegen Paragraf 133 BGB analog, Bestimmtheit Paragraf 253 Abs. 2 Nr. 2 ZPO, Haupt- und Hilfsantraege, Stuf
- **05-anspruchsgrundlagen-identifizieren** — Anspruchsgrundlagen aufstellen: vertraglich, vertragsaehnlich, dinglich, deliktisch, bereicherungsrechtlich; Anspruchssy
- **06-schluessigkeit-pruefen** — Schluessigkeitspruefung (Klaegerstation): liegen die Voraussetzungen der Anspruchsgrundlage nach dem Klaegervortrag vor?
- **07-klaegerstation-votum** — Schriftliches Votum der Klaegerstation: Anspruchsgrundlage, gepruefte Tatbestandsmerkmale, schluessige Rechtsfolge oder 
- **08-beklagtenvortrag-strukturieren** — Beklagtenvortrag ordnen: Bestreiten der Anspruchsvoraussetzungen, Einwendungen (rechtshindernd, rechtsvernichtend), Einr
- **09-einwendungen-einreden-pruefen** — Pruefung der Einwendungen und Einreden: Verjaehrung Paragrafen 194 ff. BGB, Erfuellung Paragrafen 362 ff., Aufrechnung P
- **10-erheblichkeit-pruefen** — Erheblichkeitspruefung (Beklagtenstation): sind Einwendungen und Einreden rechtlich erheblich? Schluessigkeit + Erheblic
- **11-beklagtenstation-votum** — Schriftliches Votum der Beklagtenstation: erhebliche Einwendungen und Einreden, unerhebliche Verteidigungsmittel, Beweis
- **12-beweisbeduerftige-tatsachen-isolieren** — Beweisbeduerftige Tatsachen isolieren: erhebliche und streitige Tatsachen, Trennung von Rechtsfragen und Tatsachenfragen
- **13-beweislastverteilung-pruefen** — Beweislastverteilung nach allgemeinen Regeln (Rosenberg-Formel) und Sondernormen (Paragraf 280 Abs. 1 S. 2 BGB, Paragraf
- **14-beweismittel-wuerdigen** — Beweismittel und ihre Wuerdigung: Augenschein Paragrafen 371 ff. ZPO, Zeuge Paragrafen 373 ff., Sachverstaendiger Paragr
- **15-beweisstation-votum** — Schriftliches Votum der Beweisstation: Beweisaufnahmebedarf, Beweisbeschluss-Entwurf Paragraf 358a ZPO, antizipierte Bew
- **16-tenor-formulieren** — Tenor formulieren: Hauptsache (Verurteilung zur Zahlung, Herausgabe, Unterlassung, Feststellung), Nebenforderungen (Zins
- **17-tatbestand-schreiben** — Tatbestand Paragraf 313 Abs. 1 Nr. 5 ZPO: gestraffter unstreitiger Sachverhalt, streitiger Klaegervortrag, streitiger Be
- **18-entscheidungsgruende-aufbauen** — Entscheidungsgruende aufbauen: Zulaessigkeit, Begruendetheit (Anspruchspruefung Schritt fuer Schritt), Beweiswuerdigung,
- **19-nebenentscheidungen-kosten-vorlaeufige-vollstreckbarkeit** — Nebenentscheidungen: Kosten Paragrafen 91 ff. ZPO, Baumbach'sche Formel bei subjektiver Klagehaeufung, vorlaeufige Volls
- **20-urteilsentwurf-finalisieren** — Urteilsentwurf finalisieren: Rubrum, Tenor, Tatbestand, Entscheidungsgruende, Nebenentscheidungen, Rechtsmittelbelehrung

## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment fuer den Einsatz von KI an deutschen Gerichten. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: KI-Systeme, die von einer Justizbehoerde oder in deren Auftrag bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts auf konkrete Sachverhalte** verwendet werden, sind grundsaetzlich **Hochrisiko-KI**.
- **Aber Art. 6 Abs. 3 KI-VO**: Ein KI-System gilt **nicht** als Hochrisiko-KI, wenn es nur eine **vorbereitende Aufgabe** wahrnimmt (z.B. Vorbereitung von Dokumenten, reine Recherche ohne Subsumtion).
- **Notifizierungspflicht**: Auch im Ausnahmefall des Art. 6 Abs. 3 ist der Anbieter bzw. Betreiber verpflichtet, das KI-System bei der zustaendigen Aufsicht zu **registrieren** (Art. 49 Abs. 2 KI-VO).
- Die Einordnung ist im Einzelfall zu pruefen. Sobald das System konkrete Entscheidungsvorschlaege produziert, die Subsumtion vornimmt oder die richterliche Wuerdigung ersetzt, wird die Schwelle zur Hochrisiko-KI ueberschritten.

### Art. 22 DSGVO — Verbot ausschliesslich automatisierter Entscheidung

Die richterliche Letztentscheidung muss zwingend bei einem Menschen liegen. **Keine Maschine entscheidet als Richter.** Diese Skills sind ausschliesslich **Unterstuetzung** der richterlichen Arbeit, niemals deren Ersatz. Der Richter prueft, gewichtet, entscheidet — die KI bereitet vor und macht Vorschlaege.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und **Paragraf 43 DRiG** (Amtsverschwiegenheit der Richter) sind strikt zu wahren.
- Akteninhalte duerfen nicht ungepruefte an externe KI-Anbieter uebermittelt werden. Vor jeder Verwendung ist zu pruefen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewaehrleistet.
- **Schatten-KI ist ausdruecklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behoerdlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Revisionssicherheit

- Saemtliche Arbeitsergebnisse muessen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Aenderungen wurden danach durch den Richter vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde?
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die richterliche Bearbeitung dokumentiert werden.
- Aufbewahrungsfristen nach Aktenordnung der Gerichte und ggf. KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Gerichte werden Claude und Anthropic auf absehbare Zeit nicht produktiv einsetzen koennen — das wissen wir. Der Wert dieses Plugins liegt darin, dass **Megaprompt und Miniprompt portabel** sind: Sie funktionieren in jedem KI-Tool mit ausreichendem Kontextfenster und Datei-Upload (z.B. einem behoerdlich freigegebenen On-Premise-System). Wer im Gericht bereits eine zugelassene KI-Umgebung hat, kann den Megaprompt oder Miniprompt zusammen mit weiteren Instruktionen dort einsetzen, soweit das jeweilige Hausrecht und die Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu pruefen — und kann auch zu dem Ergebnis fuehren, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.


## Quellenhygiene

- Keine erfundenen Aktenzeichen.
- Rechtsprechung nur mit Aktenzeichen + Datum + Verfahrensbezeichnung.
- Bei Unsicherheit lieber Lueckenliste als Erfindung.
- Vor Verwendung Aktenzeichen in offiziellen Datenbanken (Bundesgerichte, juris frei, Bundesverfassungsgericht.de) live verifizieren.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.
