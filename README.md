## Playwright example

This repository contains the example for the E2E test section of the Software Quality and Project Development course at the University of Catania: a small Flask web app and the Playwright tests that drive it from a real browser.

### Setup

```bash
git clone https://github.com/UNICT-Quality-Development/playwright-example
cd playwright-example
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r requirements_dev.txt
playwright install chromium
```

### Run the app

```bash
flask --app app run
```

The app runs on http://127.0.0.1:5000. Log in with the test user `mario`, password `password123`.

| Page       | Login required | What it does                                                 |
| ---------- | -------------- | ------------------------------------------------------------ |
| `/login`   | no             | Login form                                                   |
| `/contact` | no             | Student office contacts and office hours                     |
| `/exams`   | yes            | Passed exams with their grades                               |
| `/booking` | yes            | Book or cancel upcoming exams (one of them is full)          |
| `/profile` | yes            | Student details and a settings form with server-side checks  |

Opening a page that needs login without being logged in redirects to `/login`. Bookings and profile settings are kept in the session cookie, so every new browser context (and every test) starts from a clean state.

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

### Laboratory exercises

Write each exercise as a Playwright test in the `tests` folder and run it with `pytest` while the app is running.

1. **Contact email.** Go to the Contact page and verify that the student office email is shown on the page and that it is `student.office@example.com`.
2. **Student ID.** Log in as `mario`, go to the Profile page and verify that the student ID is shown on the page and that it is `1000012345`.
