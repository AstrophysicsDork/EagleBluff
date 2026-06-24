#!/usr/bin/env python3
"""
Eagle Bluff — WiFi QR generator.

Reads the WiFi SSID + password from secrets/SECRETS.local.md (gitignored)
and writes a scannable QR code to secrets/wifi-qr.local.png (also gitignored).

A guest scans the QR with their phone camera and joins the WiFi automatically —
no typing the password. Put the PNG on the printed Quick Start Sheet.

Usage:
    python tools/wifi_qr.py                         # read from SECRETS.local.md
    python tools/wifi_qr.py --ssid "herron bluff" --password "Zaq!23Wsx"
    python tools/wifi_qr.py --security WPA          # WPA (default) | WEP | nopass

Output:
    secrets/wifi-qr.local.png   (gitignored — contains the password, do not commit)
    secrets/wifi-qr.local.svg

Dependency: segno  (pip install segno)
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import segno
    from segno import helpers
except ImportError:
    sys.exit("Missing dependency. Run:  python -m pip install segno")

REPO = Path(__file__).resolve().parent.parent
SECRETS = REPO / "secrets" / "SECRETS.local.md"
OUT_PNG = REPO / "secrets" / "wifi-qr.local.png"
OUT_SVG = REPO / "secrets" / "wifi-qr.local.svg"


def read_from_secrets() -> tuple[str | None, str | None]:
    """Pull SSID + password out of the WiFi table in SECRETS.local.md."""
    if not SECRETS.exists():
        return None, None
    ssid = password = None
    for line in SECRETS.read_text(encoding="utf-8").splitlines():
        # table rows look like: | Network (SSID) | `herron bluff` | ... |
        cells = [c.strip().strip("`").strip() for c in line.split("|")]
        if len(cells) < 3:
            continue
        label = cells[1].lower()
        value = cells[2]
        if "ssid" in label or "network" in label:
            ssid = value or ssid
        elif "password" in label:
            password = value or password
    return ssid, password


def main() -> int:
    ap = argparse.ArgumentParser(description="Generate a WiFi join QR code.")
    ap.add_argument("--ssid")
    ap.add_argument("--password")
    ap.add_argument("--security", default="WPA", choices=["WPA", "WEP", "nopass"])
    ap.add_argument("--hidden", action="store_true", help="network is hidden")
    args = ap.parse_args()

    ssid, password = args.ssid, args.password
    if not ssid or not password:
        s2, p2 = read_from_secrets()
        ssid = ssid or s2
        password = password or p2

    if not ssid:
        return _fail("No SSID. Pass --ssid or fill it into secrets/SECRETS.local.md")
    if args.security != "nopass" and not password:
        return _fail("No password. Pass --password or fill secrets/SECRETS.local.md")

    qr = helpers.make_wifi(
        ssid=ssid,
        password=None if args.security == "nopass" else password,
        security=None if args.security == "nopass" else args.security,
        hidden=args.hidden,
    )
    qr.save(OUT_PNG, scale=8, border=2)
    qr.save(OUT_SVG, scale=8, border=2)

    print(f"WiFi QR generated:")
    print(f"  SSID:     {ssid}")
    print(f"  Security: {args.security}")
    print(f"  PNG:      {OUT_PNG.relative_to(REPO)}")
    print(f"  SVG:      {OUT_SVG.relative_to(REPO)}")
    print("\nBoth outputs are gitignored (they encode the password). Do not commit.")
    return 0


def _fail(msg: str) -> int:
    print(f"ERROR: {msg}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
