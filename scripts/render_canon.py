#!/usr/bin/env python3
"""Render literal Markdown derivatives from canonical YAML without third-party dependencies."""
from pathlib import Path
import hashlib

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "canon/company-sop-xos-hq.yaml"
DESTINATION = ROOT / "Company SOP 4 XOS-HQ.md"
HEADER = "<!-- Generated readable copy. Canonical YAML: XLR8ROS/xlr8ros-hq/canon/company-sop-xos-hq.yaml. Do not edit independently. -->\n\n"

def render():
    data = SOURCE.read_text(encoding="utf-8")
    if "  mode: literal\n" not in data or "  markdown_path: Company SOP 4 XOS-HQ.md\n" not in data:
        raise SystemExit("Unrecognized rendering contract")
    marker = "content: |\n"
    if data.count(marker) != 1:
        raise SystemExit("Expected exactly one literal content block")
    lines = data.split(marker, 1)[1].splitlines(keepends=True)
    if any(line.strip() and not line.startswith("  ") for line in lines):
        raise SystemExit("Invalid content indentation")
    body = "".join(line[2:] if line.startswith("  ") else line for line in lines)
    expected = HEADER + body
    DESTINATION.write_text(expected, encoding="utf-8")
    actual = DESTINATION.read_bytes()
    if hashlib.sha256(actual).digest() != hashlib.sha256(expected.encode()).digest():
        raise SystemExit("Generated Markdown verification failed")
    print("Verified:", DESTINATION.relative_to(ROOT))

if __name__ == "__main__":
    render()
