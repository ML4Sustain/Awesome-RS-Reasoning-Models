# Contributing

Thank you for helping keep the remote sensing reasoning map accurate and current.

## Submit a resource

Add a reasoning-core row to `data/survey.csv`, or an extended resource to `data/ecosystem.csv`, then run:

```bash
python -m pip install -r requirements.txt
python scripts/fetch_github_metrics.py
python scripts/build_readme.py
python scripts/plot_timeline.py
```

Commit the source row and regenerated files together. If you do not want to edit CSV, open a Resource submission issue with the same information.

## Inclusion principles

A reasoning-specific entry should demonstrate:

1. a conclusion that combines multiple evidence items or inference steps;
2. intermediate claims or actions linked to observations, constraints, or tool outputs; and
3. evaluation beyond final-answer accuracy, such as grounding, process validity, calibration, consistency, or trajectory execution.

Useful perception or vision-language work that does not meet all three criteria may be included as an enabling foundation, provided its role is labeled accurately.

## Catalog conventions

- Use the arXiv v1 date in `submitted_v1` (`YYYY-MM-DD`).
- Use the paper's own spelling for model and institution names.
- Use one row per primary paper/model resource.
- Set `method` to `VLM+SFT`, `VLM+RL`, or `Agent` when one is the dominant mechanism.
- Add a stable paper URL; add the official code repository when available.
- Never substitute an unofficial fork for an official repository just to show Stars.
- Keep popularity data in `data/github_metrics.json`; the refresh script owns these values.
- Do not infer capabilities from marketing language. Describe only what the paper evaluates or exposes.
- Leave unknown values empty rather than guessing.

## Pull request checklist

- [ ] The paper/resource URL resolves.
- [ ] The category reflects the dominant reported mechanism.
- [ ] Claims in `task` or `notes` are supported by the paper.
- [ ] The README and timeline were regenerated.
- [ ] No hand-written content inside generated README markers was edited directly.
