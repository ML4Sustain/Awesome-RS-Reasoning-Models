#!/usr/bin/env python3
"""Refresh stored GitHub stars/forks for catalog repositories."""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from datetime import date
from pathlib import Path
from urllib.parse import urlparse
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "survey.csv"
ECOSYSTEM = ROOT / "data" / "ecosystem.csv"
OUT = ROOT / "data" / "github_metrics.json"
ECOSYSTEM_OUT = ROOT / "data" / "ecosystem_github_stars.json"


def repo_slug(url: str) -> str:
    path = urlparse(url).path.strip("/").removesuffix(".git")
    if len(path.split("/")) != 2:
        raise ValueError(f"Not a GitHub repository URL: {url}")
    return path


def main() -> None:
    df = pd.read_csv(DATA, dtype=str).fillna("")
    ecosystem = pd.read_csv(ECOSYSTEM, dtype=str, encoding="utf-8-sig").fillna("")
    urls = sorted(
        {url.strip().rstrip("/") for url in df["github"] if url.strip()}
        | {url.strip().rstrip("/") for url in ecosystem["GitHub_Repo"] if url.strip() and url.strip() != "No"}
    )
    previous = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    ecosystem_payload = json.loads(ECOSYSTEM_OUT.read_text(encoding="utf-8")) if ECOSYSTEM_OUT.exists() else {"stars": {}, "canonical": {}}
    token = os.environ.get("GITHUB_TOKEN", "")
    headers = {"Accept": "application/vnd.github+json", "User-Agent": "awesome-rs-reasoning"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    updated, failures = dict(previous), []
    for url in urls:
        request = urllib.request.Request(f"https://api.github.com/repos/{repo_slug(url)}", headers=headers)
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                payload = json.load(response)
            updated[url] = {
                "stars": payload["stargazers_count"],
                "forks": payload["forks_count"],
                "fetched_at": date.today().isoformat(),
            }
            ecosystem_payload.setdefault("stars", {})[url] = payload["stargazers_count"]
            ecosystem_payload.setdefault("canonical", {})[url] = payload.get("html_url", url)
        except (urllib.error.URLError, KeyError, ValueError) as error:
            failures.append(f"{url}: {error}")
    OUT.write_text(json.dumps(updated, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    ecosystem_payload["fetched_at"] = date.today().isoformat()
    ECOSYSTEM_OUT.write_text(json.dumps(ecosystem_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    succeeded = len(urls) - len(failures)
    print(f"Updated {succeeded}/{len(urls)} repositories.")
    if failures:
        print("Some repositories could not be refreshed; their previous snapshots were preserved:", file=sys.stderr)
        print("\n".join(failures), file=sys.stderr)
    if urls and succeeded == 0:
        raise SystemExit("No repository metrics could be refreshed.")


if __name__ == "__main__":
    main()
