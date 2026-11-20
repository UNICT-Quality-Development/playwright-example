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

Every exercise must be implemented using the Page Object pattern and the BDD pattern: add a page object for each page you use in the `pages` folder, describe the scenario in a `.feature` file in `tests/features` and implement its steps with `pytest-bdd` on top of the page objects. `tests/test_login_bdd.py` shows how the two patterns work together.

1. **Contact email.** Go to the Contact page and verify that the student office email is shown on the page and that it is `student.office@example.com`.
2. **Student ID.** Log in as `mario`, go to the Profile page and verify that the student ID is shown on the page and that it is `1000012345`.
3. **Book and cancel an exam.** Log in as `mario` and go to the Book an exam page.
   1. Book Software Engineering and verify that its status becomes `Booked`, that the page shows `Booked exams: 1` and that the message `Booked Software Engineering on 2027-01-15` appears.
   2. Cancel the booking and verify that the status goes back to `Available`, that the page shows `Booked exams: 0` and that the message `Cancelled the booking for Software Engineering` appears.
4. **Full exam.** Log in as `mario`, go to the Book an exam page and verify that Computer Networks has the status `Full`, that its Book button is disabled and that the page shows `Booked exams: 0`.
5. **Profile settings.** Log in as `mario` and go to the Profile page.
   1. Change the email to `mario.rossi@example.com`, choose the language `Italiano`, untick "Notify me about new exam dates" and save.
   2. Verify that the message `Profile saved` appears.
   3. Reload the page and verify that the form still shows the three new values.
6. **Invalid email.** Log in as `mario` and go to the Profile page.
   1. Change the email to `mario` and save.
   2. Verify that the error `Enter a valid email address` appears and that the message `Profile saved` does not.
   3. Open the Profile page again from the navigation bar (reloading would send the form again) and verify that the email is still `mario@example.com`.
7. **Log out.** Log in as `mario` and log out, then open `/exams` and verify that you are back on the login page.
