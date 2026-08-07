# Scenecraft — AI Storyboard Studio

Turn a one-line idea into a cinematic script, parsed scenes, and render-ready
visual prompts. Powered by Hugging Face Inference.

## Quickstart

```bash
git clone <your-repo-url> && cd <repo>
pip install -r requirements.txt
cp .env.example .env      # then paste your token into .env
streamlit run app.py
```

Get a token at https://huggingface.co/settings/tokens (read access is enough).

## Files

| File | Purpose |
| --- | --- |
| `app.py` | Streamlit UI |
| `pipeline.py` | Generation logic — importable, no UI |
| `.env` | Your `HF_TOKEN` (gitignored) |

## Use as a library

```python
from pipeline import run_pipeline
script, scenes, design, storyboard = run_pipeline("A lighthouse at the end of time")
```

## Deploy

Push to GitHub, then deploy free on [Streamlit Community Cloud](https://share.streamlit.io) —
add `HF_TOKEN` under App settings → Secrets.
