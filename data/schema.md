# Catalog schema

Each row in `survey.csv` is one paper/model resource. The CSV stores scholarly metadata and verified official repository URLs. Time-varying popularity metrics are stored separately in `github_metrics.json` so snapshots remain auditable.

## Fields

| Field | Required | Meaning |
| --- | :---: | --- |
| `paradigm` | yes | Broad family, currently `RSVLRM` |
| `method` | yes | Dominant mechanism: `VLM+SFT`, `VLM+RL`, or `Agent` |
| `year` | yes | First public year |
| `institution` | recommended | Primary institution(s) stated by the work |
| `title` | yes | Full paper/resource title |
| `model` | recommended | Short model or benchmark name |
| `arxiv_id` | recommended | Bare identifier, for example `2509.21976` |
| `url` | yes | Stable paper or project URL |
| `task` | recommended | Compact, evidence-based focus description |
| `notes` | optional | Qualification or curation note |
| `github` | optional | Official implementation URL |
| `bibtex` | optional | Citation key or BibTeX payload |
| `submitted_v1` | recommended | First public date as `YYYY-MM-DD` |

## GitHub metrics

`github_metrics.json` is keyed by the exact official repository URL stored in `survey.csv`. Each value stores integer `stars`, integer `forks`, and ISO date `fetched_at`. Run `scripts/fetch_github_metrics.py` to refresh it; do not hand-author live badge values in the README.

## Extended ecosystem snapshot

`ecosystem.csv` is the normalized local snapshot of 79 audited remote-sensing resources. It stores two-level taxonomy, release year and venue, weight/data platforms, official code, ModelScope mirrors, release constraints, curation comments, and a dated Star value. `ecosystem_github_stars.json` retains the corresponding API snapshot for reproducible sorting. The snapshot was imported from the public ModelScope Studio `VoyagerX/Awesome-RS-Reasoning-Models` on 2026-08-24 and is maintained locally thereafter.

`datasets.csv` normalizes standalone datasets and benchmarks found in verified release links, with resource kind, year, companion model, task, platform, URL, and access status.

`scripts/fetch_arxiv_meta.py` can fill missing `title`, `url`, and `submitted_v1` values for valid arXiv identifiers. `scripts/build_readme.py` validates the required columns before writing generated sections.
