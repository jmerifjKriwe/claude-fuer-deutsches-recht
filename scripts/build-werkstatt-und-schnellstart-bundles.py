#!/usr/bin/env python3
"""
Stillgelegtes Bundle-Skript.

Werkstatt- und Schnellstart-Prompts werden nicht mehr als ZIP ausgeliefert.
Stattdessen verlinken die Plugin-READMEs direkt auf die Markdown-Dateien
unter raw.githubusercontent.com. Echte Markdown-Direkt-Downloads ohne Umweg
ueber ZIP.

Dieses Skript bleibt nur als No-Op-Stub erhalten, damit Altaufrufe nicht
hart fehlschlagen. Es erzeugt bewusst keine Dateien mehr.
"""

from __future__ import annotations

import sys


def main() -> int:
    print(
        "build-werkstatt-und-schnellstart-bundles.py ist stillgelegt: "
        "Werkstatt- und Schnellstart-Prompts werden nur noch als Markdown "
        "ueber die README-Links angeboten, nicht mehr als ZIP."
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
