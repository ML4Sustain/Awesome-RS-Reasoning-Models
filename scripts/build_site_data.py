#!/usr/bin/env python3
"""Generate the website's static catalog payload from repository data."""

from __future__ import annotations

import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ECOSYSTEM = ROOT / "data" / "ecosystem.csv"
DATASETS = ROOT / "data" / "datasets.csv"
SURVEY = ROOT / "data" / "survey.csv"
STARS = ROOT / "data" / "ecosystem_github_stars.json"
OUT = ROOT / "site" / "app" / "catalog-data.json"
PAPER_RE = re.compile(r"(?:Paper:\s*)?(https?://(?:arxiv\.org/abs/|doi\.org/|ieeexplore\.ieee\.org/document/)[^\s;,]+)")


def read_csv(path: Path) -> list[dict[str, str]]:
    with path.open(encoding="utf-8-sig", newline="") as stream:
        return list(csv.DictReader(stream))


def main() -> None:
    methods = read_csv(ECOSYSTEM)
    datasets = read_csv(DATASETS)
    survey = read_csv(SURVEY)
    missing_venues = [row.get("Name", "<unnamed>") for row in methods if not row.get("Venue", "").strip()]
    if missing_venues:
        raise SystemExit(f"Missing Venue for: {', '.join(missing_venues)}")
    snapshot = json.loads(STARS.read_text(encoding="utf-8"))
    stars = {key.rstrip("/").lower(): int(value) for key, value in snapshot.get("stars", {}).items()}

    catalog = []
    for row in methods:
        comments = row.get("Comments", "")
        match = PAPER_RE.search(comments)
        repo = row.get("GitHub_Repo", "")
        repo = "" if repo == "No" else repo
        downloads = []
        for platform, url in ((row.get("Platform1", ""), row.get("Download_Link1", "")), (row.get("Platform2", ""), row.get("Download_Link2", ""))):
            if url:
                downloads.append({"label": platform or "Download", "url": url})
        catalog.append({
            "name": row["Name"],
            "year": row["Year"],
            "venue": row["Venue"],
            "family": row["Cls1"],
            "category": row["Cls2"],
            "paper": match.group(1).rstrip(".)") if match else "",
            "repo": repo,
            "stars": stars.get(repo.rstrip("/").lower(), int(row.get("GitHub_Stars") or 0)) if repo else 0,
            "downloads": downloads,
        })

    data_entries = [{
        "name": row["name"], "year": row["year"], "kind": row["kind"],
        "model": row["paired_model"], "focus": row["task"],
        "label": row["platform"], "url": row["url"],
    } for row in datasets]

    mechanism_labels = {
        "VLM+SFT": "Supervised",
        "VLM+RL": "Reinforcement",
        "Agent": "Agentic / tools",
    }
    catalog_by_name = {item["name"].lower(): item for item in catalog}
    timeline = []
    for row in survey:
        mechanism = mechanism_labels.get(row.get("method", ""))
        if not mechanism or not row.get("submitted_v1"):
            continue
        name = row.get("model") or row.get("title")
        catalog_match = catalog_by_name.get(name.lower())
        repo = (row.get("github", "") or (catalog_match or {}).get("repo", "")).rstrip("/")
        timeline.append({
            "name": name,
            "title": row.get("title", ""),
            "date": row["submitted_v1"],
            "mechanism": mechanism,
            "paper": row.get("url", ""),
            "repo": repo,
            "stars": stars.get(repo.lower(), (catalog_match or {}).get("stars", 0)) if repo else 0,
        })
    timeline.sort(key=lambda item: item["date"])

    unique_repos = {item["repo"].rstrip("/").lower() for item in catalog if item["repo"]}
    payload = {
        "updated": snapshot.get("fetched_at", "2026-08-24"),
        "stats": {
            "resources": len(catalog),
            "reasoning": sum(item["family"] == "Reasoning Models" for item in catalog),
            "datasets": len(data_entries),
            "repositories": len(unique_repos),
        },
        "methods": catalog,
        "datasets": data_entries,
        "timeline": timeline,
    }
    OUT.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")) + "\n", encoding="utf-8")
    print(f"Generated {OUT.relative_to(ROOT)} with {len(catalog)} methods and {len(data_entries)} datasets.")


if __name__ == "__main__":
    main()
