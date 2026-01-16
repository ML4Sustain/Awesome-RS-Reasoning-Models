# Dataset schema

Each row in `survey.csv` corresponds to one paper/model entry.

Required (recommended) columns:
- paradigm: e.g., RSVLRM
- method: e.g., VLM+RL / VLM+SFT / Agent
- year: integer
- institution
- title
- model
- arxiv_id: e.g., 2509.21976
- url: arXiv abs URL (auto-filled if missing)
- submitted_v1: YYYY-MM-DD (auto-filled if missing)

Optional:
- task
- notes
- github
- bibtex
