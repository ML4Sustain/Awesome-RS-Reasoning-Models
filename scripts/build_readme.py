#!/usr/bin/env python3
"""Render the README from locally stored catalog and GitHub metrics."""

from __future__ import annotations

import json
import re
from pathlib import Path
from urllib.parse import quote
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "survey.csv"
ECOSYSTEM = ROOT / "data" / "ecosystem.csv"
ECOSYSTEM_STARS = ROOT / "data" / "ecosystem_github_stars.json"
DATASETS = ROOT / "data" / "datasets.csv"
METRICS = ROOT / "data" / "github_metrics.json"
STATS = ROOT / "data" / "stats.json"
README = ROOT / "README.md"
MECHANISMS = {
    "VLM+SFT": ("Supervised", "🧩"),
    "VLM+RL": ("Reinforcement", "🎯"),
    "Agent": ("Agentic", "🛠️"),
}


def clean(value: object) -> str:
    return "" if pd.isna(value) else str(value).strip()


def md_link(label: str, url: str) -> str:
    return f"[{label}]({url})" if url else "—"


def link_badge(label: str, message: str, url: str, *, logo: str = "", color: str = "16858a") -> str:
    if not url:
        return "—"
    query = f"label={quote(label)}&amp;message={quote(message)}&amp;color={color}&amp;style=flat-square"
    if logo:
        query += f"&amp;logo={quote(logo)}"
    badge = f'<img alt="{label}: {message}" src="https://img.shields.io/static/v1?{query}">'
    return f'<a href="{url}">{badge}</a>'


def paper_badge(url: str) -> str:
    if not url:
        return "—"
    if "arxiv.org" in url:
        return link_badge("Paper", "arXiv", url, logo="arxiv", color="b31b1b")
    if "doi.org" in url:
        return link_badge("Paper", "DOI", url, logo="doi", color="4051b5")
    if "ieeexplore.ieee.org" in url:
        return link_badge("Paper", "IEEE", url, logo="ieee", color="00629b")
    return link_badge("Paper", "Article", url, color="526d82")


def code_badge(url: str) -> str:
    return link_badge("Code", "GitHub", url, logo="github", color="24292f") if url and url != "No" else "—"


def access_badge(platform: str, url: str, *, kind: str = "Weights") -> str:
    platform = platform or kind
    lower = platform.lower()
    if "huggingface" in lower or "hugging face" in lower:
        return link_badge(kind, "Hugging Face", url, logo="huggingface", color="f4b400")
    if "modelscope" in lower:
        return link_badge(kind, "ModelScope", url, color="624aff")
    if "baidu" in lower:
        return link_badge(kind, "Baidu", url, logo="baidu", color="1677ff")
    if "github" in lower:
        return link_badge(kind, "GitHub", url, logo="github", color="24292f")
    if "paper" in lower:
        return paper_badge(url)
    if "project" in lower or "website" in lower:
        return link_badge("Project", "Website", url, color="16858a")
    return link_badge(kind, platform, url, color="526d82")


def star_badge(stars: int, repo: str) -> str:
    """Render a GitHub-style badge from the stored snapshot, never a live count."""
    if not repo or repo == "No" or stars < 0:
        return "—"
    if stars >= 1_000_000:
        label = f"{stars / 1_000_000:.1f}m".replace(".0m", "m")
    elif stars >= 1_000:
        label = f"{stars / 1_000:.1f}k".replace(".0k", "k")
    else:
        label = str(stars)
    badge = f'<img alt="{stars:,} Stars" src="https://img.shields.io/static/v1?label=Stars&amp;message={label}&amp;logo=github&amp;style=social">'
    return f'<a href="{repo.rstrip("/")}/stargazers">{badge}</a>'


def paper_link(comments: str) -> str:
    """Extract the first paper/DOI URL stored in the audit notes."""
    match = re.search(r"(?:Paper:\s*)?(https?://(?:arxiv\.org/abs/|doi\.org/|ieeexplore\.ieee\.org/document/)[^\s;,]+)", comments)
    return paper_badge(match.group(1).rstrip(".)")) if match else "—"


def table(headers: list[str], rows: list[list[object]]) -> str:
    def esc(value: object) -> str:
        return clean(value).replace("|", "\\|").replace("\n", " ")
    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join(":---:" for _ in headers) + " |",
    ]
    lines += ["| " + " | ".join(esc(v) for v in row) + " |" for row in rows]
    return "\n".join(lines)


def replace_block(text: str, name: str, body: str) -> str:
    start, end = f"<!-- AUTO_{name}_START -->", f"<!-- AUTO_{name}_END -->"
    if text.count(start) != 1 or text.count(end) != 1:
        raise ValueError(f"Expected exactly one {name} marker pair")
    before, tail = text.split(start)
    _, after = tail.split(end)
    return f"{before}{start}\n\n{body.rstrip()}\n\n{end}{after}"


def load() -> tuple[pd.DataFrame, dict[str, dict]]:
    df = pd.read_csv(DATA, dtype=str).fillna("")
    required = {"method", "year", "institution", "title", "model", "url", "task", "github", "submitted_v1"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing catalog columns: {', '.join(sorted(missing))}")
    df["date"] = pd.to_datetime(df["submitted_v1"], errors="coerce")
    df["name"] = df["model"].where(df["model"].str.strip().ne(""), df["title"])
    df["mechanism"] = df["method"].map(lambda x: MECHANISMS.get(x, ("Foundation", "🧱"))[0])
    metrics = json.loads(METRICS.read_text(encoding="utf-8")) if METRICS.exists() else {}
    df["stars"] = df["github"].map(lambda url: int(metrics.get(url, {}).get("stars", 0)) if url else -1)
    return df.sort_values(["date", "stars"], ascending=[False, False]), metrics


def dashboard(df: pd.DataFrame, metrics: dict[str, dict]) -> tuple[str, dict]:
    tracked = df[df["github"].str.strip().ne("")]
    total_stars = int(tracked["stars"].clip(lower=0).sum())
    last_metrics = max((clean(v.get("fetched_at")) for v in metrics.values()), default="—")
    stats = {
        "entries": int(len(df)),
        "open_source": int(len(tracked)),
        "tracked_stars": total_stars,
        "latest_entry": df["date"].max().strftime("%Y-%m-%d"),
        "metrics_updated": last_metrics,
    }
    cards = table(
        ["📚 Resources", "💻 Open source", "Tracked stars", "🕒 Metrics snapshot"],
        [[f"**{stats['entries']}**", f"**{stats['open_source']}**", f"**{total_stars}**", f"**{last_metrics}**"]],
    )
    rows = []
    for _, row in df.head(5).iterrows():
        code = md_link("Code", row["github"]) if row["github"] else "No public code"
        star = star_badge(int(row["stars"]), row["github"])
        rows.append([
            row["date"].strftime("%Y-%m-%d"),
            md_link(row["name"], row["url"]),
            f"\x60{row['mechanism']}\x60",
            row["task"],
            code,
            star,
        ])
    return cards + "\n\n#### Fresh arrivals\n\n" + table(
        ["Date", "Resource", "Track", "Focus", "Code", "Stars"], rows
    ), stats


def catalog(df: pd.DataFrame) -> str:
    output: list[str] = []
    for method, (label, icon) in MECHANISMS.items():
        group = df[df["method"] == method].sort_values(["stars", "date"], ascending=[False, False])
        if group.empty:
            continue
        rows = []
        for _, row in group.iterrows():
            paper = paper_badge(row["url"])
            code = code_badge(row["github"])
            stars = star_badge(int(row["stars"]), row["github"])
            rows.append([
                md_link(f"**{row['name']}**", row["url"]),
                row["task"],
                row["institution"],
                f"{row['year']} · arXiv",
                f"{paper} · {code}",
                stars,
            ])
        output.append(
            f"### {icon} {label} reasoning <sub>{len(group)} resources</sub>\n\n"
            + table(["Resource", "Focus", "Institution", "Venue", "Links", "Stored stars"], rows)
        )
    return "\n\n".join(output)


def load_ecosystem() -> tuple[pd.DataFrame, dict[str, int], str]:
    df = pd.read_csv(ECOSYSTEM, dtype=str, encoding="utf-8-sig").fillna("")
    required = {"Name", "Year", "Venue", "Cls1", "Cls2", "Platform1", "Download_Link1", "Platform2", "Download_Link2", "ModelScope_Mirror", "GitHub_Repo", "GitHub_Stars"}
    missing = required - set(df.columns)
    if missing:
        raise ValueError(f"Missing ecosystem columns: {', '.join(sorted(missing))}")
    payload = json.loads(ECOSYSTEM_STARS.read_text(encoding="utf-8"))
    stars = {url.rstrip("/"): int(value) for url, value in payload.get("stars", {}).items()}
    return df, stars, clean(payload.get("fetched_at")) or "—"


def ecosystem_catalog(df: pd.DataFrame, stars: dict[str, int], *, expanded: bool = False) -> str:
    family_labels = {
        "Vision-Language Models": "Remote Sensing Vision-Language Modeling",
        "Related RS Models": "Reasoning-Enabling Models",
        "Perception Models": "Perception Foundations",
    }
    groups: list[str] = []
    for (family, category), group in df.groupby(["Cls1", "Cls2"], sort=False):
        ranked = group.copy()
        ranked["_stars"] = ranked["GitHub_Repo"].map(lambda url: stars.get(url.rstrip("/"), int(clean(ranked.loc[ranked["GitHub_Repo"] == url, "GitHub_Stars"].iloc[0]) or 0)) if url else 0)
        ranked = ranked.sort_values(["_stars", "Year"], ascending=[False, False])
        rows = []
        for _, row in ranked.iterrows():
            downloads = []
            if row["Download_Link1"]:
                downloads.append(access_badge(row["Platform1"], row["Download_Link1"]))
            if row["Download_Link2"]:
                downloads.append(access_badge(row["Platform2"], row["Download_Link2"]))
            if row["ModelScope_Mirror"] and row["ModelScope_Mirror"] not in {"No", row["Download_Link2"]}:
                downloads.append(access_badge("ModelScope", row["ModelScope_Mirror"]))
            repo = code_badge(row["GitHub_Repo"])
            star = star_badge(int(row["_stars"]), row["GitHub_Repo"])
            rows.append([f"**{row['Name']}**", f"{row['Year']} · {row['Venue']}", paper_link(row["Comments"]), " · ".join(downloads) or "—", repo, star])
        body = table(["Resource", "Year / Venue", "Paper", "Weights / Data", "Official code", "Stars"], rows)
        details_tag = "<details open>" if expanded else "<details>"
        display_family = family_labels.get(family, family)
        unit = "resource" if len(group) == 1 else "resources"
        groups.append(f"{details_tag}\n<summary><b>{display_family} › {category}</b> · {len(group)} {unit}</summary>\n\n{body}\n\n</details>")
    return "\n\n".join(groups)


def ecosystem_dashboard(df: pd.DataFrame, stars: dict[str, int], metrics_updated: str) -> tuple[str, dict[str, object]]:
    dataset_count = len(pd.read_csv(DATASETS))
    reasoning = int((df["Cls1"] == "Reasoning Models").sum())
    repos = int(df["GitHub_Repo"].isin(["", "No"]).eq(False).sum())
    weights = int(df["Download_Link1"].str.strip().ne("").sum())
    mirrors = int(df["ModelScope_Mirror"].isin(["", "No"]).eq(False).sum())
    total_stars = sum(stars.get(url.rstrip("/"), 0) for url in set(df["GitHub_Repo"]) if url and url != "No")
    stats = {
        "entries": int(len(df)),
        "reasoning_models": reasoning,
        "official_repositories": repos,
        "weights_available": weights,
        "modelscope_mirrors": mirrors,
        "datasets_benchmarks": dataset_count,
        "tracked_stars": int(total_stars),
        "metrics_updated": metrics_updated,
    }
    cards = table(
        ["🌍 Methods & models", "🧠 Reasoning", "🗃️ Data / benches", "💻 Official repos", "📦 Weights", "🔁 MS mirrors"],
        [[f"**{len(df)}**", f"**{reasoning}**", f"**{dataset_count}**", f"**{repos}**", f"**{weights}**", f"**{mirrors}**"]],
    )
    note = f"Repository Stars are stored snapshots refreshed daily by GitHub Actions. Last refresh: **{metrics_updated}**."
    return cards + "\n\n" + note, stats


def dataset_catalog() -> str:
    df = pd.read_csv(DATASETS, dtype=str).fillna("").sort_values(["year", "name"], ascending=[False, True])
    rows = []
    for _, row in df.iterrows():
        link_label = row["platform"] or "Resource"
        rows.append([f"**{row['name']}**", row["kind"], row["paired_model"], row["task"], access_badge(link_label, row["url"], kind="Data")])
    return table(["Dataset / benchmark", "Type", "Companion model", "Focus", "Links"], rows)


def main() -> None:
    df, metrics = load()
    ecosystem_df, ecosystem_stars, metrics_updated = load_ecosystem()
    if metrics_updated == "—":
        metrics_updated = max((clean(value.get("fetched_at")) for value in metrics.values()), default="—")
    text = README.read_text(encoding="utf-8")
    dashboard_md, stats = ecosystem_dashboard(ecosystem_df, ecosystem_stars, metrics_updated)
    text = replace_block(text, "DASHBOARD", dashboard_md)
    text = replace_block(text, "CATALOG", ecosystem_catalog(ecosystem_df[ecosystem_df["Cls1"] == "Reasoning Models"], ecosystem_stars, expanded=True))
    text = replace_block(text, "ECOSYSTEM", ecosystem_catalog(ecosystem_df[ecosystem_df["Cls1"] != "Reasoning Models"], ecosystem_stars, expanded=True))
    text = replace_block(text, "DATASETS", dataset_catalog())
    README.write_text(text, encoding="utf-8")
    STATS.write_text(json.dumps(stats, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Rendered {stats['reasoning_models']} reasoning models, {len(ecosystem_df)} ecosystem resources, and {stats['datasets_benchmarks']} datasets.")


if __name__ == "__main__":
    main()
