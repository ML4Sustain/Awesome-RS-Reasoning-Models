#!/usr/bin/env python3
import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "survey.csv"
README = ROOT / "README.md"


def mk_link(label, url):
    if isinstance(url, str) and url.strip():
        return f"[{label}]({url})"
    return ""


def main():
    df = pd.read_csv(DATA)

    if "submitted_v1" in df.columns:
        df["submitted_v1"] = pd.to_datetime(df["submitted_v1"], errors="coerce")
    else:
        df["submitted_v1"] = pd.NaT

    df = df.sort_values(["submitted_v1", "year"], ascending=[False, False])

    df["arxiv"] = df.apply(lambda r: mk_link(r.get("arxiv_id", ""), r.get("url", "")), axis=1)
    df["code"] = df.apply(lambda r: mk_link("GitHub", r.get("github", "")), axis=1)

    out = pd.DataFrame({
        "arXiv v1 date": df["submitted_v1"].dt.strftime("%Y-%m-%d").fillna(""),
        "Model": df.get("model", "").fillna(""),
        "Institution": df.get("institution", "").fillna(""),
        "Method": df.get("method", "").fillna(""),
        "Paradigm": df.get("paradigm", "").fillna(""),
        "arXiv": df["arxiv"].fillna(""),
        "Code": df["code"].fillna(""),
    })

    md_table = out.to_markdown(index=False)

    start = "<!-- AUTO_TABLE_START -->"
    end = "<!-- AUTO_TABLE_END -->"

    content = README.read_text(encoding="utf-8") if README.exists() else ""
    block = f"{start}\n\n{md_table}\n\n{end}"

    if start in content and end in content:
        pre = content.split(start)[0]
        post = content.split(end)[1]
        content = pre + block + post
    else:
        content += "\n\n## Model List (auto-generated)\n\n" + block + "\n"

    README.write_text(content, encoding="utf-8")
    print("README updated.")


if __name__ == "__main__":
    main()
