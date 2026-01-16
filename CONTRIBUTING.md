# Contributing

Thanks for contributing!

## Add a new entry
Edit `data/survey.csv` and add a new row with:
- `model`, `institution`, `method`, `paradigm`
- `arxiv_id` + `url` + `submitted_v1` (preferred; but `url/submitted_v1/title` can be auto-filled)
- `github` (optional)

## Rules
- Use **arXiv v1 submission date** for `submitted_v1` (UTC)
- Do not merge different institutions into one row
- Keep model names consistent with the paper
