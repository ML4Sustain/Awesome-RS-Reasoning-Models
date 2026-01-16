#!/usr/bin/env python3
from __future__ import annotations

import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "survey.csv"

ARXIV_API = "https://export.arxiv.org/api/query"


def normalize_arxiv_id(x: str) -> str:
    s = str(x).strip()
    s = s.replace("arXiv:", "").strip()
    s = re.sub(r"^https?://arxiv\.org/abs/", "", s)
    s = re.sub(r"^https?://arxiv\.org/pdf/", "", s)
    s = s.replace(".pdf", "")
    return s


def fetch_arxiv_atom(arxiv_id: str) -> dict | None:
    params = {"id_list": arxiv_id, "max_results": "1"}
    url = ARXIV_API + "?" + urllib.parse.urlencode(params)

    with urllib.request.urlopen(url, timeout=30) as resp:
        xml_bytes = resp.read()

    ns = {"atom": "http://www.w3.org/2005/Atom"}
    root = ET.fromstring(xml_bytes)
    entry = root.find("atom:entry", ns)
    if entry is None:
        return None

    title = entry.findtext("atom:title", default="", namespaces=ns).strip()
    published = entry.findtext("atom:published", default="", namespaces=ns).strip()

    abs_url = ""
    for link in entry.findall("atom:link", ns):
        if link.attrib.get("rel") == "alternate" and link.attrib.get("href", "").startswith("http"):
            abs_url = link.attrib["href"]
            break

    submitted_v1 = published.split("T")[0] if published else ""

    return {
        "title": re.sub(r"\s+", " ", title),
        "submitted_v1": submitted_v1,
        "url": abs_url,
    }


def main():
    df = pd.read_csv(DATA)

    if "arxiv_id" not in df.columns:
        raise SystemExit("survey.csv must contain 'arxiv_id' column")

    for col in ["title", "url", "submitted_v1"]:
        if col not in df.columns:
            df[col] = ""

    changed = False
    for i, row in df.iterrows():
        raw_id = row.get("arxiv_id", "")
        if pd.isna(raw_id) or str(raw_id).strip() == "":
            continue

        arxiv_id = normalize_arxiv_id(raw_id)

        need_title = (pd.isna(row.get("title")) or str(row.get("title")).strip() == "")
        need_url = (pd.isna(row.get("url")) or str(row.get("url")).strip() == "")
        need_date = (pd.isna(row.get("submitted_v1")) or str(row.get("submitted_v1")).strip() == "")

        if not (need_title or need_url or need_date):
            continue

        meta = fetch_arxiv_atom(arxiv_id)
        if meta is None:
            continue

        if need_title and meta.get("title"):
            df.at[i, "title"] = meta["title"]; changed = True
        if need_url and meta.get("url"):
            df.at[i, "url"] = meta["url"]; changed = True
        if need_date and meta.get("submitted_v1"):
            df.at[i, "submitted_v1"] = meta["submitted_v1"]; changed = True

        if str(raw_id).strip() != arxiv_id:
            df.at[i, "arxiv_id"] = arxiv_id; changed = True

    if changed:
        df.to_csv(DATA, index=False)
        print("survey.csv updated with arXiv metadata.")
    else:
        print("No metadata updates needed.")


if __name__ == "__main__":
    main()
