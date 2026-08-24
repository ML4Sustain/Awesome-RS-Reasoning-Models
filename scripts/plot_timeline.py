#!/usr/bin/env python3
"""Render a compact, dependency-free SVG timeline from the catalog."""

from __future__ import annotations

import csv
import html
import json
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "survey.csv"
METRICS = ROOT / "data" / "github_metrics.json"
OUT = ROOT / "assets" / "timeline.svg"
SITE_OUT = ROOT / "site" / "public" / "timeline.svg"

WIDTH = 1600
LEFT = 175
RIGHT = 45
TOP = 142
COLORS = {
    "VLM+SFT": ("#55d6be", "Supervised"),
    "VLM+RL": ("#f6bd60", "Reinforcement"),
    "Agent": ("#e78ac3", "Agentic / tools"),
}
LANE_Y = {"VLM+SFT": 215, "VLM+RL": 425, "Agent": 655}


def esc(value: object) -> str:
    return html.escape(str(value), quote=True)


def label(row: dict[str, str]) -> str:
    return row.get("model", "").strip() or row["title"].split(":")[0][:24]


def main() -> None:
    with DATA.open(encoding="utf-8", newline="") as stream:
        rows = list(csv.DictReader(stream))
    metrics = json.loads(METRICS.read_text(encoding="utf-8")) if METRICS.exists() else {}
    dated = []
    for row in rows:
        try:
            row["_date"] = datetime.strptime(row["submitted_v1"], "%Y-%m-%d")
        except ValueError:
            continue
        row["_stars"] = metrics.get(row.get("github", ""), {}).get("stars")
        dated.append(row)
    if not dated:
        raise SystemExit("No valid submitted_v1 dates found")

    months = []
    cursor = datetime(min(r["_date"].year for r in dated), min(r["_date"].month for r in dated), 1)
    last = max(r["_date"] for r in dated)
    while cursor <= last:
        months.append(cursor)
        cursor = datetime(cursor.year + (cursor.month == 12), cursor.month % 12 + 1, 1)
    step = (WIDTH - LEFT - RIGHT) / max(1, len(months) - 1)
    month_x = {(m.year, m.month): LEFT + i * step for i, m in enumerate(months)}

    grouped: dict[tuple[str, int, int], list[dict]] = defaultdict(list)
    for row in dated:
        grouped[(row["method"], row["_date"].year, row["_date"].month)].append(row)
    for values in grouped.values():
        values.sort(key=lambda r: r["_date"])

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{WIDTH}" height="790" viewBox="0 0 {WIDTH} 790" role="img" aria-labelledby="title desc">',
        '<title id="title">Remote sensing reasoning timeline</title>',
        '<desc id="desc">Publications arranged by month and dominant reasoning mechanism. Larger highlighted nodes have more stored GitHub stars.</desc>',
        '<defs><linearGradient id="bg" x1="0" y1="0" x2="1" y2="1"><stop stop-color="#071a2d"/><stop offset="1" stop-color="#103947"/></linearGradient>',
        '<filter id="shadow" x="-30%" y="-30%" width="160%" height="160%"><feDropShadow dx="0" dy="4" stdDeviation="5" flood-color="#000" flood-opacity=".22"/></filter></defs>',
        '<rect width="1600" height="790" rx="22" fill="url(#bg)"/>',
        '<text x="54" y="60" fill="#f4fbfc" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="30" font-weight="750">The reasoning wave</text>',
        '<text x="54" y="91" fill="#9dcbd5" font-family="Inter,Segoe UI,Arial,sans-serif" font-size="15">First public release · grouped by dominant acquisition or execution mechanism</text>',
        '<g font-family="Inter,Segoe UI,Arial,sans-serif">',
    ]

    for i, month in enumerate(months):
        x = month_x[(month.year, month.month)]
        major = month.month == 1 or i == 0
        parts.append(f'<line x1="{x:.1f}" y1="120" x2="{x:.1f}" y2="724" stroke="#8bb9c2" stroke-opacity="{".22" if major else ".10"}"/>')
        month_text = month.strftime("%b")
        parts.append(f'<text x="{x:.1f}" y="123" text-anchor="middle" fill="#b8dce3" font-size="13">{month_text}</text>')
        if major:
            parts.append(f'<text x="{x:.1f}" y="108" text-anchor="middle" fill="#f4fbfc" font-size="14" font-weight="700">{month.year}</text>')

    for method, (color, lane_name) in COLORS.items():
        y = LANE_Y[method]
        parts.append(f'<rect x="31" y="{y-40}" width="1538" height="{175 if method != "Agent" else 120}" rx="16" fill="#ffffff" fill-opacity=".035" stroke="#b9dfe5" stroke-opacity=".08"/>')
        parts.append(f'<circle cx="58" cy="{y}" r="7" fill="{color}"/>')
        parts.append(f'<text x="76" y="{y+5}" fill="#eaf7f8" font-size="15" font-weight="700">{esc(lane_name)}</text>')
        parts.append(f'<line x1="{LEFT}" y1="{y}" x2="{WIDTH-RIGHT}" y2="{y}" stroke="{color}" stroke-opacity=".35" stroke-width="2"/>')

    for (method, year, month), values in grouped.items():
        if method not in LANE_Y:
            continue
        x = month_x[(year, month)]
        base_y = LANE_Y[method]
        count = len(values)
        spacing = 25
        start = -(count - 1) * spacing / 2
        for index, row in enumerate(values):
            y = base_y + start + index * spacing
            name = label(row)
            stars = row["_stars"]
            radius = 7 if stars is None else min(15, 8 + (stars ** 0.5) * 0.55)
            color = COLORS[method][0]
            align_left = x > WIDTH - 210
            text_x = x - radius - 8 if align_left else x + radius + 8
            anchor = "end" if align_left else "start"
            detail = f"{stars} stars" if stars is not None else ""
            parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{radius:.1f}" fill="{color}" stroke="#071a2d" stroke-width="3" filter="url(#shadow)"/>')
            parts.append(f'<text x="{text_x:.1f}" y="{y+4:.1f}" text-anchor="{anchor}" fill="#f4fbfc" font-size="12.5" font-weight="650">{esc(name)}</text>')
            if detail:
                parts.append(f'<text x="{text_x:.1f}" y="{y+18:.1f}" text-anchor="{anchor}" fill="{color}" font-size="10.5">{esc(detail.strip())}</text>')

    parts += [
        '<g transform="translate(54 751)" font-size="12">',
        '<circle cx="5" cy="0" r="5" fill="#d6eef2"/><text x="17" y="4" fill="#b8dce3">public paper</text>',
        '<circle cx="126" cy="0" r="10" fill="#d6eef2"/><text x="144" y="4" fill="#b8dce3">node size = repository stars snapshot</text>',
        '<text x="1450" y="4" text-anchor="end" fill="#799faa">generated from data/survey.csv</text>',
        '</g></g></svg>',
    ]
    rendered = "\n".join(parts) + "\n"
    OUT.write_text(rendered, encoding="utf-8")
    SITE_OUT.parent.mkdir(parents=True, exist_ok=True)
    SITE_OUT.write_text(rendered, encoding="utf-8")
    print(f"Saved {OUT.relative_to(ROOT)} with {len(dated)} entries.")


if __name__ == "__main__":
    main()
