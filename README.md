## Playwright example

This repository contains the example for the E2E test section of the Software Quality and Project Development course at the University of Catania: a small Flask web app and the Playwright tests that drive it from a real browser.

### Setup

```bash
git clone https://github.com/UNICT-Quality-Development/playwright-example
cd playwright-example
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
playwright install chromium
```

### Run the app

```bash
flask --app app run
```

The app runs on http://127.0.0.1:5000. Log in with the test user `mario`, password `password123`.

### Run the tests

Keep the app running and open a second terminal:

```bash
source .venv/bin/activate
pytest
```

Useful options:

```bash
# show the browser and slow down every action
pytest --headed --slowmo 500

# run on another browser (install it first with playwright install firefox)
pytest --browser firefox

# keep a trace of every failed test
pytest --tracing retain-on-failure
```

### Record a test with codegen

```bash
playwright codegen --target python-pytest 127.0.0.1:5000/login
```

### Open a trace

```bash
playwright show-trace test-results/<test-folder>/trace.zip
```
