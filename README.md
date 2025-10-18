# Trend-to-Product Agent (browser-use)

A simple agent that looks at current Google Trends and finds products that fit those trends (e.g., on Costco or Amazon), powered by `browser-use` and OpenAI.

## What’s here
- `simple_agent.py` — minimal agent example.
- `agent.py` — uses an existing Chrome session (CDP) and searches trends then products (Costco/Amazon).
- `use_real_browser.py` — example using a real browser via CDP.
- `use_real_browser_remote.py` — like `agent.py`, connects to Chrome via CDP.
- `browser_basics.py` — minimal browser + agent wiring.

## Prerequisites
- Python 3.10+
- Google Chrome (for scripts that connect to a real browser)
- An OpenAI API key

## Setup
1. Create and activate a virtual environment with uv, then install dependencies:
```bash
uv venv --python 3.12
source .venv/bin/activate
uv pip install browser-use
uvx playwright install chromium --with-deps
```
2. Create `.env` with your OpenAI key:
```bash
# .env
OPENAI_API_KEY=sk-...
```

## Running
- Simple example (no real browser connection):
```bash
python simple_agent.py
```

- Use an existing Chrome via CDP (required by `agent.py` and `use_real_browser_remote.py`):
  1) Start Chrome with remote debugging on port 9222:
```bash
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome \
  --remote-debugging-port=9222 \
  --user-data-dir=/tmp/chrome-debug \
  --no-first-run --no-default-browser-check
```
  2) Run an agent that checks Google Trends and looks for related products:
```bash
python agent.py
# or
python use_real_browser_remote.py
```

- Alternative local browser wiring example:
```bash
python use_real_browser.py
```

## Customize the task
- Edit the `task` strings in `agent.py`, `use_real_browser_remote.py`, or `simple_agent.py`.
  - Example in `agent.py`: it goes to Google Trends and then searches Costco/Amazon for a related product.

## Notes
- Ensure Chrome is running with `--remote-debugging-port=9222` before launching the CDP-based scripts.
- The environment variables are loaded from `.env` (see `simple_agent.py`).
