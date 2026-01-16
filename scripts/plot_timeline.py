#!/usr/bin/env python3
from pathlib import Path

import matplotlib.dates as mdates
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "survey.csv"
OUT = ROOT / "assets" / "timeline.png"


def short(s, n=24):
    s = "" if pd.isna(s) else str(s)
    return s if len(s) <= n else (s[: n - 1] + "…")


def main():
    df = pd.read_csv(DATA)
    df["submitted_v1"] = pd.to_datetime(df.get("submitted_v1"), errors="coerce")
    df = df.dropna(subset=["submitted_v1"]).sort_values("submitted_v1")

    df["ModelLabel"] = df.get("model", "").fillna("").astype(str)
    missing = df["ModelLabel"].str.strip() == ""
    if "title" in df.columns:
        df.loc[missing, "ModelLabel"] = df.loc[missing, "title"].apply(lambda x: short(x, 18))

    df["InstLabel"] = df.get("institution", "").apply(lambda x: short(x, 32))

    palette = {
        "VLM+RL": "#2563eb",
        "VLM+SFT": "#f97316",
    }
    default_color = "#10b981"
    colors = df["method"].map(palette).fillna(default_color)

    # Wider canvas so labels and annotations don't crowd the plot
    fig, ax = plt.subplots(figsize=(13, 9), facecolor="#f8fafc")
    ax.set_facecolor("#f8fafc")

    xmin = df["submitted_v1"].min() - pd.Timedelta(days=10)
    y = list(range(len(df)))
    for x, y_pos, color in zip(df["submitted_v1"], y, colors):
        ax.hlines(
            y=y_pos,
            xmin=xmin,
            xmax=x,
            color="#d0d7e2",
            linewidth=1.1,
            zorder=1,
        )

    ax.scatter(
        df["submitted_v1"],
        y,
        c=colors,
        s=70,
        edgecolors="#ffffff",
        linewidth=1.1,
        zorder=3,
    )

    ax.set_yticks(y)
    ax.set_yticklabels(df["ModelLabel"].tolist())
    ax.set_xlabel("arXiv v1 submission date")
    ax.set_ylabel("")
    ax.set_title(
        "Remote Sensing Reasoning Models — Timeline",
        loc="left",
        fontsize=15,
        fontweight="bold",
        color="#0f172a",
        pad=12,
    )
    ax.grid(True, axis="x", linestyle="--", linewidth=0.8, color="#e2e8f0")
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m"))
    ax.xaxis.set_tick_params(labelsize=10, colors="#475569")
    ax.yaxis.set_tick_params(labelsize=10, colors="#0f172a", pad=6)

    for spine in ax.spines.values():
        spine.set_color("#d0d7e2")

    for i, row in df.reset_index(drop=True).iterrows():
        ax.annotate(
            row["InstLabel"],
            (row["submitted_v1"], i),
            xytext=(6, 0),
            textcoords="offset points",
            va="center",
            fontsize=9,
            color="#334155",
            zorder=4,
        )

    fig.autofmt_xdate()
    handles = [
        mpatches.Patch(color=color, label=label)
        for label, color in palette.items()
    ]
    handles.append(mpatches.Patch(color=default_color, label="Other"))
    ax.legend(
        handles=handles,
        title="Method",
        frameon=False,
        loc="lower center",
        bbox_to_anchor=(0.5, 1.08),
        ncol=len(handles),
        labelcolor="#334155",
        title_fontsize=10,
        fontsize=9,
    )
    plt.margins(y=0.04)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    plt.tight_layout(rect=(0, 0, 1, 0.88))
    plt.savefig(OUT, dpi=260)
    print(f"Saved: {OUT}")


if __name__ == "__main__":
    main()
