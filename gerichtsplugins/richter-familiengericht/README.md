# Familiengericht (großes Familiengericht)

<!-- BEGIN direkt-loslegen (autogen) -->
## Was ist das hier?

Familiengericht: Ehesachen Scheidung Versorgungsausgleich Kindschaftssachen elterliche Sorge Umgang Kindesunterhalt Trennungs- und Ehegattenunterhalt Gewaltschutz Adoption Vormundschaft Betreuungsteile mit Verfahrenskostenhilfe und Tenorvorschlag

Dieses Plugin gehört zum Marketplace mit 232 Plugins für deutsches Recht. Es bündelt die zugehörigen Skills, Prüfraster, Vorlagen und Arbeitsroutinen in einem installierbaren Plugin-ZIP. Die zwei Markdown-Prompts sind vollwertige Ein-Datei-Starts für den Fall, dass kein Plugin-Setup genutzt werden soll: Werkstatt für den ausführlichen Arbeitsmodus, Schnellstart für den kompakten Einstieg.

## Downloads

| Was | Format | Direkt-Download |
| --- | --- | --- |
| Plugin als Komplett-ZIP (Hauptweg) | ZIP | [`richter-familiengericht.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-familiengericht.zip) |
| Großer Prompt (Werkstatt) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-familiengericht-werkstatt.md" download><code>richter-familiengericht-werkstatt.md</code></a> |
| Kleiner Prompt (Schnellstart) | Markdown | <a href="https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-familiengericht-schnellstart.md" download><code>richter-familiengericht-schnellstart.md</code></a> |
| Testakte(n) als ZIP | ZIP | [`richter-familiengericht-testakte.zip`](https://github.com/Klotzkette/claude-fuer-deutsches-recht/releases/latest/download/richter-familiengericht-testakte.zip) |

> Marketplace-Hinweis: Dieses Plugin gehört zum Marketplace mit 232 Plugins. Wer alle Plugins auf einmal will, nimmt `alle-plugins-megazip.zip`. Wer nur einzelne Werkstatt- oder Schnellstart-Prompts will, nimmt die Markdown-Downloads.
<!-- END direkt-loslegen (autogen) -->

Wenn du das hier öffnest, willst du Versorgungsausgleich, Zugewinn und Unterhalt sauber durchrechnen und beantragen.
> **Experimentelles Plugin im Ordner `gerichtsplugins/`** — siehe Vorspruch unten.

> **Kritisch — Hochrisiko-KI und Art. 22 DSGVO beachten.** Der Einsatz von KI in der Rechtspflege ist nach Art. 6 Abs. 2 in Verbindung mit Anhang III Nr. 8 Buchstabe a der KI-Verordnung (VO (EU) 2024/1689) grundsätzlich **Hochrisiko-KI**. Die Rückausnahme des Art. 6 Abs. 3 KI-VO greift nur bei rein vorbereitender Tätigkeit ohne Subsumtion; auch dann besteht Registrierungspflicht nach Art. 49 Abs. 2 KI-VO. Eine Entscheidung mit rechtlicher Wirkung über Menschen darf nicht einer Maschine überlassen werden (Art. 22 DSGVO) — die richterliche Letztentscheidung liegt zwingend beim Menschen. Einzelheiten unten unter „Wichtiger Hinweis vor Verwendung".

## Rolle

Familienrichter am Amtsgericht (Paragraf 23a Abs. 1 Nr. 1 GVG i.V.m. Paragraf 23b GVG) für Ehe-, Kindschafts-, Unterhalts-, Versorgungsausgleichs-, Gewaltschutz- und sonstige Familiensachen nach FamFG

## Rechtsrahmen

FamFG, BGB (Familienrecht), ZPO (subsidiaer), VersAusglG, GewSchG, KSchG (Kindschaftsrecht), UnterhaltsR (Paragrafen 1601 ff. BGB), FamGKG, RVG, Haager Kinderschutzübereinkommen, EuEheVO, Bruessel IIb

## Inhalt

- **11 Skills** (siehe `skills/`; inklusive Schnellstart-Skill)
- **Werkstatt-Prompt** (`richter-familiengericht-werkstatt.md`)
- **Schnellstart-Prompt** (`richter-familiengericht-schnellstart.md`)
- **Testakte** (`testakte/README.md`) — aus Richtersicht

## Skill-Liste

- **01-zuständigkeit-und-zuteilung-familiensache** — Prüfung Zuständigkeit Paragraf 23a Abs. 1 Nr. 1 GVG i.V.m. Paragraf 23b GVG, örtliche Zuständigkeit Paragrafen 122-1
- **02-ehesache-scheidung-paragraf-1565** — Scheidungsverfahren Paragrafen 1564 ff. BGB i.V.m. Paragrafen 121 ff. FamFG: Trennungsjahr Paragraf 1566, Zerruettung Pa
- **03-versorgungsausgleich-vorbereiten** — Versorgungsausgleich nach VersAusglG: Auskuenfte der Versorgungstraeger einholen, Ehezeit feststellen Paragraf 3 VersAus
- **04-kindschaftssache-elterliche-sorge** — Sorgerechtsverfahren Paragrafen 1626 ff. BGB i.V.m. Paragrafen 151 ff. FamFG: Kindeswohlprüfung (Bindungs-, Foerder-, K
- **05-umgangsrecht-paragraf-1684-bgb** — Umgangsverfahren Paragraf 1684 BGB i.V.m. Paragrafen 156 ff. FamFG: Wohl des Kindes, begleiteter Umgang, Umgangspflegsch
- **06-kindesunterhalt-duesseldorfer-tabelle** — Kindesunterhalt Paragrafen 1601 ff. BGB: Bedürftigkeit, Leistungsfähigkeit (Selbstbehalt nach Leitlinien), Duesseldorf
- **07-ehegattenunterhalt-trennung-und-nachehe** — Trennungsunterhalt Paragraf 1361 BGB und nachehelicher Unterhalt Paragrafen 1569 ff. BGB: Anspruchsgrundlagen (Betreuung
- **08-gewaltschutz-und-eilanordnung** — Gewaltschutzverfahren GewSchG: Schutzanordnungen Paragraf 1 (Abstand, Naehe, Kontakt), Wohnungszuweisung Paragraf 2, Eil
- **09-beschluss-familiensache-paragraf-38-famfg** — Beschluss in Familiensache Paragraf 38 FamFG: Tenor, Sachverhalt (knapp), Gründe, Nebenentscheidungen FamGKG-Wert und V
- **10-entscheidungsvorschlag-familienrichter** — Strukturierter Entscheidungsvorschlag für den Familienrichter: Tenor-Skizze (Scheidungsausspruch, Folgesachen, Sorge/Um

## Wichtiger Hinweis vor Verwendung

**Experimentelles Plugin — Vorsicht.** Dieses Plugin ist ein Funktionsexperiment für den Einsatz von KI an deutschen Gerichten. Es geht hier um die **Capability**, nicht um eine Produktivempfehlung.

### Rechtliche Einordnung der KI-Verordnung (KI-VO, VO (EU) 2024/1689)

- **Art. 6 Abs. 2 i.V.m. Anhang III Nr. 8 lit. a KI-VO**: KI-Systeme, die von einer Justizbehoerde oder in deren Auftrag bei der **Recherche und Auslegung von Sachverhalten und Rechtsvorschriften** sowie bei der **Anwendung des Rechts auf konkrete Sachverhalte** verwendet werden, sind grundsaetzlich **Hochrisiko-KI**.
- **Aber Art. 6 Abs. 3 KI-VO**: Ein KI-System gilt **nicht** als Hochrisiko-KI, wenn es nur eine **vorbereitende Aufgabe** wahrnimmt (z.B. Vorbereitung von Dokumenten, reine Recherche ohne Subsumtion).
- **Notifizierungspflicht**: Auch im Ausnahmefall des Art. 6 Abs. 3 ist der Anbieter bzw. Betreiber verpflichtet, das KI-System bei der zuständigen Aufsicht zu **registrieren** (Art. 49 Abs. 2 KI-VO).
- Die Einordnung ist im Einzelfall zu prüfen. Sobald das System konkrete Entscheidungsvorschlaege produziert, die Subsumtion vornimmt oder die richterliche Würdigung ersetzt, wird die Schwelle zur Hochrisiko-KI überschritten.

### Art. 22 DSGVO — Verbot ausschliesslich automatisierter Entscheidung

Die richterliche Letztentscheidung muss zwingend bei einem Menschen liegen. **Keine Maschine entscheidet als Richter.** Diese Skills sind ausschliesslich **Unterstuetzung** der richterlichen Arbeit, niemals deren Ersatz. Der Richter prüft, gewichtet, entscheidet — die KI bereitet vor und macht Vorschlaege.

### Aktengeheimnis und Datenschutz

- **Paragraf 353b StGB** (Verletzung von Dienstgeheimnissen) und **Paragraf 43 DRiG** (Amtsverschwiegenheit der Richter) sind strikt zu wahren.
- Akteninhalte duerfen nicht ungeprüfte an externe KI-Anbieter übermittelt werden. Vor jeder Verwendung ist zu prüfen, ob die genutzte KI-Umgebung den Datenschutz und das Aktengeheimnis gewaehrleistet.
- **Schatten-KI ist ausdrücklich abgelehnt.** Dieses Plugin soll keine Hilfe sein, KI an behoerdlichen Datenschutz- und IT-Richtlinien vorbei einzusetzen.

### Revisionssicherheit

- Saemtliche Arbeitsergebnisse müssen revisionssicher dokumentiert werden: Wer hat wann welche KI-Ausgabe genutzt, welche Änderungen wurden danach durch den Richter vorgenommen, welche Akten- und Promptbestandteile lagen zugrunde?
- Die KI-Ausgabe muss als KI-Ausgabe erkennbar bleiben (Markierung, Versionierung); die richterliche Bearbeitung dokumentiert werden.
- Aufbewahrungsfristen nach Aktenordnung der Gerichte und ggf. KI-VO-Logging-Pflichten beachten.

### Realismus-Hinweis

Viele Gerichte werden externe Cloud-Dienste auf absehbare Zeit nicht produktiv einsetzen können. Der Wert dieses Plugins liegt darin, dass **Werkstatt-Prompt und Schnellstart-Prompt portabel** sind: Sie funktionieren in einem behördlich freigegebenen Fachsystem mit ausreichendem Kontextfenster und Datei-Upload. Wer im Gericht bereits eine zugelassene Umgebung hat, kann den Werkstatt-Prompt oder Schnellstart-Prompt dort einsetzen, soweit Hausrecht und Datenschutzfreigabe das erlauben.

### Verwendung auf eigene Gefahr

Die Nutzung erfolgt **auf eigene Gefahr und eigene Verantwortung**. Es handelt sich um ein Capability-Experiment. Die Frage, ob und wie der hier abgebildete Workflow rechtssicher betrieben werden kann, ist im Einzelfall zu prüfen — und kann auch zu dem Ergebnis führen, dass es nicht geht. Wir wollen das wissen, indem wir es bauen und ausprobieren.

## Quellenhygiene

- Keine erfundenen Aktenzeichen.
- Rechtsprechung nur mit Aktenzeichen + Datum + Verfahrensbezeichnung.
- Bei Unsicherheit lieber Lueckenliste als Erfindung.
- Vor Verwendung Aktenzeichen in offiziellen Datenbanken (Bundesgerichte, juris frei, Bundesverfassungsgericht.de) live verifizieren.

## Lizenz

Dual-lizenziert MIT und Apache-2.0.


<!-- BEGIN SKILLS-OVERVIEW (auto-generated) -->

## Alle Skills im Ueberblick

Automatisch generierte Komplett-Liste aller 12 Skills in diesem Plugin. Beschreibungen stammen aus dem `description`-Feld der jeweiligen SKILL.md.

| Skill | Beschreibung |
| --- | --- |
| `01-zustaendigkeit-und-zuteilung-familiensache` | Prüfung Zuständigkeit Paragraf 23a Abs. 1 Nr. 1 GVG i.V.m. Paragraf 23b GVG, örtliche Zuständigkeit Paragrafen 122-124 FamFG, Geschaeftsverteilung; Verbund Paragraf 137 FamFG bei Scheidung; Verfahrenskostenhilfe Paragraf 76 FamFG |
| `02-ehesache-scheidung-paragraf-1565` | Scheidungsverfahren Paragrafen 1564 ff. BGB i.V.m. Paragrafen 121 ff. FamFG: Trennungsjahr Paragraf 1566, Zerruettung Paragraf 1565, Versorgungsausgleich Paragraf 1587, Folgesachen Paragraf 137 FamFG (Unterhalt, Sorgerecht, Zugewinn, Hau... |
| `03-versorgungsausgleich-vorbereiten` | Bereitet den Versorgungsausgleich richterlich vor: Ehezeit, Versorgungsträgerauskünfte, interne und externe Teilung, Geringfügigkeit, Härte, Anhörung, Nachforderung und tenorierungsfähiger Beschluss. |
| `04-kindschaftssache-elterliche-sorge` | Sorgerechtsverfahren Paragrafen 1626 ff. BGB i.V.m. Paragrafen 151 ff. FamFG: Kindeswohlprüfung (Bindungs-, Foerder-, Kontinuitaetsprinzip, Kindeswille), Anhörung des Kindes Paragraf 159 FamFG, Verfahrensbeistand Paragraf 158, Eilanordnu... |
| `05-umgangsrecht-paragraf-1684-bgb` | Umgangsverfahren Paragraf 1684 BGB i.V.m. Paragrafen 156 ff. FamFG: Wohl des Kindes, begleiteter Umgang, Umgangspflegschaft Paragraf 1684 Abs. 3, Vermittlungsverfahren Paragraf 165 FamFG, Eilanordnung |
| `06-kindesunterhalt-duesseldorfer-tabelle` | Prüft Kindesunterhalt richterlich mit Bedarf, Einkommen, Leistungsfähigkeit, Düsseldorfer Tabelle, Leitlinien, Selbstbehalt, Mangelfall, dynamischem Titel und vollstreckbarem Tenor. |
| `07-ehegattenunterhalt-trennung-und-nachehe` | Trennungsunterhalt Paragraf 1361 BGB und nachehelicher Unterhalt Paragrafen 1569 ff. BGB: Anspruchsgrundlagen (Betreuungs-, Alters-, Krankheits-, Aufstockungsunterhalt), Befristung und Begrenzung Paragraf 1578b, Verwirkung Paragraf 1579 |
| `08-gewaltschutz-und-eilanordnung` | Gewaltschutzverfahren GewSchG: Schutzanordnungen Paragraf 1 (Abstand, Naehe, Kontakt), Wohnungszuweisung Paragraf 2, Eilbeschluss Paragraf 214 FamFG, sofortige Wirksamkeit Paragraf 209 FamFG, Strafbewehrung Paragraf 4 GewSchG |
| `09-beschluss-familiensache-paragraf-38-famfg` | Erstellt richterliche Beschlüsse in Familiensachen nach Paragraf 38 FamFG mit Rubrum, Tenor, Gründen, Kosten, Vollstreckbarkeit, Rechtsmittelbelehrung und sauberer Nummerierung. |
| `10-entscheidungsvorschlag-familienrichter` | Strukturierter Entscheidungsvorschlag für den Familienrichter: Tenor-Skizze (Scheidungsausspruch, Folgesachen, Sorge/Umgang/Unterhalt), Kindeswohlerwaegungen, Risikohinweise (insbesondere bei Eilanordnungen), ausdrücklich zur richterlich... |
| `99-finale-entscheidung-volltext` | Erzeugt die finale entscheidung als volltext (beschluss familiengericht) als versandfertigen Volltext mit Rubrum, Tenor, Tatbestand, Entscheidungsgründen, Nebenentscheidungen und Rechtsmittelbelehrung. |
| `v392-praxisraster-richter-familiengericht` | Praxisraster für Familiengericht: Zuständigkeit, Verfahrensstand, Pflichtnormen, Beweisbedarf und passendes Endprodukt werden in der richtigen gerichtlichen oder staatsanwaltschaftlichen Rolle abgearbeitet. |

<!-- END SKILLS-OVERVIEW (auto-generated) -->
