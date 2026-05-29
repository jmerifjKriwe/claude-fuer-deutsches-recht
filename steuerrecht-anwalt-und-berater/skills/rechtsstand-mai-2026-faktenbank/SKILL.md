---
name: rechtsstand-mai-2026-faktenbank
description: "Faktenbank und Quellen-Gate für aktuelle steuerrechtliche Aussagen mit Stand 29.05.2026. Nutze diesen Skill vor Ausgaben zu E-Rechnung, Umsatzsteuer, Krypto, Grundsteuer, Mindeststeuer, DBA, Betriebsprüfung, Einspruch, AdV und Steuer-/SV-Schnittstellen. Zitiert nur freie amtliche Quellen, BFH/BMF/BZSt/Gesetze-im-Internet und verifizierte Gerichtsentscheidungen."
---

# Rechtsstand Mai 2026 — Faktenbank Steuerrecht

## Zweck

Dieser Skill bündelt verifizierte Rechtsstandsanker für das Steuerrecht-Plugin. Er verhindert Blindzitate und zwingt Ausgaben zu einer sauberen Quellenlage.

Stand dieser Faktenbank: **29.05.2026**. Vor streitentscheidenden Ausgaben immer den aktuellen Gesetzestext, BMF/BZSt-Veröffentlichungen und BFH-Volltext prüfen.

## Quellenregel

- Keine BeckRS-, juris-, Kommentar-, Handbuch- oder Aufsatzfundstellen aus Modellwissen.
- BFH/FG-Rechtsprechung nur mit Gericht, Entscheidungsform, Datum, Aktenzeichen und freiem Link.
- Verwaltungsauffassung nur als BMF-/BZSt-/Bundesregierung-/Bundesgesetzblatt-Quelle zitieren; nicht als Ersatz für Gesetz und Rechtsprechung behandeln.
- Wenn eine Aussage nur aus Datenbankkürzeln bekannt ist, nicht verwenden.

## Aktuelle Steuerrechtsanker

| Thema | Gesicherter Anker | Praktische Aussage | Freie Quelle |
|---|---|---|---|
| E-Rechnung B2B | BMF-FAQ und BMF-Schreiben vom 15.10.2024 zur Einführung der obligatorischen E-Rechnung | Ab 01.01.2025 müssen inländische Unternehmer E-Rechnungen empfangen können; Ausstellungspflichten laufen mit Übergangsregeln. Reine PDF ist grundsätzlich sonstige Rechnung. Formate wie XRechnung/ZUGFeRD nur prüfen, wenn strukturiert und zulässig. | https://www.bundesfinanzministerium.de/Content/DE/FAQ/e-rechnung.html |
| Krypto private Veräußerung | BFH, Urteil vom 14.02.2023, IX R 3/22 | Currency Token/Kryptowerte können andere Wirtschaftsgüter i. S. d. § 23 Abs. 1 Satz 1 Nr. 2 EStG sein; Veräußerung/Tausch innerhalb der Jahresfrist kann steuerbar sein. | https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/pdf/STRE202310089?type=1646225765 |
| Krypto Verwaltungsauffassung | BMF-Schreiben vom 06.03.2025 zu Einzelfragen der ertragsteuerrechtlichen Behandlung bestimmter Kryptowerte | Steuerreports, Wallet-/Transaktionsdaten, Staking/Lending/Claiming und Mitwirkungspflichten konkret dokumentieren; nicht pauschal aus Börsenexporten folgern. | https://www.bundesfinanzministerium.de/Content/DE/Downloads/BMF_Schreiben/Steuerarten/Einkommensteuer/2025-03-06-einzelfragen-kryptowerte.html |
| Grundsteuer Bundesmodell / AdV | BFH, Beschlüsse vom 27.05.2024, II B 78/23 (AdV) und II B 79/23 (AdV) | Im AdV-Verfahren sind ernstliche Zweifel möglich, wenn der Steuerpflichtige einen deutlich niedrigeren gemeinen Wert plausibel macht; Einzelfallbelege sammeln. | https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/STRE202410095/ |
| Grundsteuer Bundesmodell / Hauptsache | BFH, Urteil vom 12.11.2025, II R 3/25 | Bei Grundsteuerwerten im Bundesmodell immer aktuelle BFH-Linie und landesrechtliche Sondermodelle trennen; Bundesmodell nicht mit Länderöffnungsklauseln vermischen. | https://www.bundesfinanzhof.de/de/entscheidung/entscheidungen-online/detail/pdf/STRE202620008?type=1646225765 |
| Private Veräußerungsgeschäfte | § 23 EStG | Freigrenze und Haltefristen anhand des aktuellen Gesetzestexts prüfen; Krypto, Grundstücke und sonstige Wirtschaftsgüter getrennt behandeln. | https://www.gesetze-im-internet.de/estg/__23.html |
| Kapitaleinkünfte / Verlustverrechnung | § 20 EStG und BMF-EStH-Hinweise zum JStG 2024 | Bei Termingeschäften, Totalverlusten und Verlustverrechnung keine alten Deckel fortschreiben, sondern offenen Fall, Übergang und aktuellen Gesetzestext prüfen. | https://ao.bundesfinanzministerium.de/esth/2024/C-Anhaenge/Anhang-19/II/anhang-19-II.html |

## Mandats-Workflow

1. **Steuerart und Verfahrensstand zuerst:** Bescheid, Einspruch, Außenprüfung, AdV, Klage, Lohn/SV oder reine Deklaration.
2. **Rechtsstandsfenster setzen:** Veranlagungszeitraum, Leistungs-/Rechnungsdatum, Bekanntgabe, Gesetzesänderung, Übergangsvorschrift.
3. **Quelle hart trennen:** Gesetz, Verwaltungsauffassung, Rechtsprechung, Mandatsunterlagen.
4. **Kein Datenbank-Blendwerk:** keine BeckRS-/juris-/Kommentarzitate ohne geöffneten Nutzerzugang.
5. **Output dokumentierbar machen:** Quellenblock, Annahmenblock, Beleganforderung, nächster Verfahrensschritt.

## Typische Spezial-Skills

| Wenn das Problem ist ... | Lade danach ... |
|---|---|
| Bescheid, Einspruch, AdV, FG-Klage | `anw-steuerbescheid-analyse`, `anw-einspruch-finanzamt`, `anw-aussetzung-vollziehung`, `anw-klage-finanzgericht` |
| E-Rechnung / Vorsteuer | `anw-umsatzsteuer-vorsteuerabzug-pruefen` |
| Krypto / Plattform / DAC | `anw-dac7-dac8-plattformen-krypto`, `anw-defi-lending-yield-farming-bmf-22-11-2024` |
| Außenprüfung / Verständigung | `anw-aussenpruefung-strategien`, `anw-tatsaechliche-verstaendigung-schlussbesprechung` |
| Haftung / Insolvenzschnittstelle | `anw-gf-haftung-69-ao-nicht-abgefuehrte-steuern`, `anw-insolvenzreife-pruefung-17-19-inso`, `stb-bwa-sus-bilanz-pruefung` |
