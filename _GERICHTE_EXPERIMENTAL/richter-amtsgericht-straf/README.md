# Richter Amtsgericht Strafsachen

> **Experimentelles Plugin im Ordner `_GERICHTE_EXPERIMENTAL/`** — siehe Vorspruch unten.

## Rolle

Strafrichter:in oder Schoeffengericht am Amtsgericht (Paragraf 24 GVG, Paragraf 25 GVG, Paragrafen 28-30 GVG)

## Rechtsrahmen

StGB, StPO, GVG, JGG, OWiG, BZRG, RVG

## Inhalt

- **10 Skills** (siehe `skills/`)
- **Megaprompt** (`MEGAPROMPT.md`)
- **Miniprompt** (`MINIPROMPT.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-akte-erstdurchsicht-strafsache** — Strukturierte Erstdurchsicht: Anklagesatz, wesentliches Ergebnis der Ermittlungen, hinreichender Tatverdacht, Beweismitt
- **02-zustaendigkeit-und-eroeffnungsbeschluss** — Zustaendigkeit Strafrichter oder Schoeffengericht (Paragraf 25 oder 28 GVG), Eroeffnung Paragrafen 199-203 StPO, Nichter
- **03-hauptverhandlung-vorbereiten** — Terminierung, Ladung Paragraf 214 StPO, Beweisantraege, Erforderlichkeit Verteidigerbestellung Paragraf 140 StPO, Versta
- **04-beweisaufnahme-und-beweisantraege** — Beweisaufnahme nach Paragrafen 244-256 StPO, Umgang mit Beweisantraegen, Praesenzvermutung Paragraf 244 Abs. 6, Wahrunte
- **05-beweiswuerdigung-strafrecht** — Beweiswuerdigung Paragraf 261 StPO: Indizien, Aussage gegen Aussage, Glaubhaftigkeit, In-dubio-pro-reo, Sachverstaendige
- **06-strafzumessung-paragraf-46-stgb** — Strafzumessung Paragraf 46 StGB: Schuld als Grundlage, Strafzumessungstatsachen, Strafrahmen, Strafmilderung Paragrafen 
- **07-tenor-und-rechtsmittelbelehrung-straf** — Tenor: Schuldspruch, Strafausspruch, Nebenstrafen, Bewaehrung, Einziehung Paragraf 73 StGB, Kostenentscheidung Paragraf 
- **08-urteilsbegruendung-paragraf-267-stpo** — Urteilsgruende: Persoenliche Verhaeltnisse, Feststellungen zum Tatgeschehen, Beweiswuerdigung, rechtliche Wuerdigung, St
- **09-strafbefehl-und-beschleunigtes-verfahren** — Strafbefehlsverfahren Paragrafen 407-412 StPO, Voraussetzungen, Inhalt, Einspruch, Hauptverhandlung nach Einspruch; besc
- **10-entscheidungsvorschlag-strafrichter** — Strukturierter Entscheidungsvorschlag mit Schuldspruch-Skizze, Strafzumessungs-Skizze, Nebenfolgen, Risikohinweisen, aus

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
