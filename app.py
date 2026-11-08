import re
from functools import wraps

from flask import (
    Flask,
    abort,
    flash,
    redirect,
    render_template_string,
    request,
    session,
    url_for,
)
from jinja2 import DictLoader

app = Flask(__name__)
app.secret_key = "dev"  # demo only, never hard-code a real secret

USERS = {
    "mario": {
        "password": "password123",
        "name": "Mario",
        "student_id": "1000012345",
        "degree": "Computer Science (BSc)",
        "email": "mario@example.com",
    }
}
EXAMS = {"mario": [("Programming 1", 28), ("Algorithms", 30), ("Databases", 27)]}
UPCOMING_EXAMS = {
    "swe": {"course": "Software Engineering", "date": "2027-01-15", "full": False},
    "net": {"course": "Computer Networks", "date": "2027-01-22", "full": True},
    "os": {"course": "Operating Systems", "date": "2027-02-05", "full": False},
}
OFFICE_HOURS = [
    ("Monday", "09:00 - 12:00"),
    ("Wednesday", "14:00 - 17:00"),
    ("Friday", "09:00 - 12:00"),
]
LANGUAGES = {"en": "English", "it": "Italiano"}
EMAIL_PATTERN = re.compile(r"[^@\s]+@[^@\s]+\.[^@\s]+")

STYLE = """
<!doctype html>
<meta charset="utf-8">
<style>
  body { font-family: sans-serif; background: #f4f6fa; color: #1f2937; margin: 0; }
  nav { display: flex; flex-wrap: wrap; align-items: center; gap: 16px; min-height: 58px;
        box-sizing: border-box; background: #fff; padding: 12px 24px;
        box-shadow: 0 1px 4px rgba(0, 0, 0, 0.1); }
  nav a { color: #1d4ed8; text-decoration: none; }
  nav a[aria-current="page"] { font-weight: bold; text-decoration: underline; }
  nav form { margin-left: auto; }
  nav button { margin-top: 0; }
  main { max-width: 520px; margin: 60px auto; background: #fff; padding: 32px;
         border-radius: 8px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }
  h1 { margin-top: 0; font-size: 1.6em; }
  h2 { margin-top: 28px; font-size: 1.2em; }
  label { display: block; margin-top: 12px; font-weight: bold; }
  input, select { width: 100%; box-sizing: border-box; padding: 8px; margin-top: 4px; }
  input[type="checkbox"] { width: auto; margin: 0 8px 0 0; }
  button { margin-top: 20px; padding: 8px 20px; background: #1d4ed8; color: #fff;
           border: none; border-radius: 4px; font-size: 1em; cursor: pointer; }
  button:disabled { background: #9ca3af; cursor: not-allowed; }
  td button { margin-top: 0; padding: 4px 12px; }
  table { width: 100%; border-collapse: collapse; }
  th, td { text-align: left; padding: 8px; border-bottom: 1px solid #e5e7eb; }
  dt { margin-top: 12px; font-weight: bold; }
  dd { margin: 4px 0 0; }
  [role="alert"] { color: #b91c1c; }
  [role="status"] { color: #15803d; }
</style>
"""

NAV = """
<nav>
  {% if session.username %}
    {% set links = [("exams", "My exams"), ("booking", "Book an exam"),
                    ("profile", "Profile"), ("contact", "Contact")] %}
  {% else %}
    {% set links = [("login", "Log in"), ("contact", "Contact")] %}
  {% endif %}
  {% for endpoint, label in links %}
  <a href="{{ url_for(endpoint) }}" data-testid="nav-{{ endpoint }}"
     {% if request.endpoint == endpoint %}aria-current="page"{% endif %}>{{ label }}</a>
  {% endfor %}
  {% if session.username %}
  <form method="post" action="{{ url_for('logout') }}">
    <button type="submit" data-testid="logout-button">Log out</button>
  </form>
  {% endif %}
</nav>
"""

# Lets every page template pull in the shared nav with {% include "nav.html" %}.
app.jinja_loader = DictLoader({"nav.html": NAV})

LOGIN_PAGE = STYLE + """
<title>Student portal</title>
{% include "nav.html" %}
<main>
  <h1>Student portal</h1>
  {% if error %}<p role="alert" data-testid="login-error">{{ error }}</p>{% endif %}
  <form method="post">
    <label for="username">Username</label>
    <input id="username" name="username" data-testid="username-input">
    <label for="password">Password</label>
    <input id="password" name="password" type="password" data-testid="password-input">
    <button type="submit" data-testid="login-button">Log in</button>
  </form>
</main>
"""

EXAMS_PAGE = STYLE + """
<title>My exams</title>
{% include "nav.html" %}
<main>
  <h1 data-testid="greeting">Welcome, {{ name }}</h1>
  <table>
    <thead><tr><th>Exam</th><th>Grade</th></tr></thead>
    <tbody>
      {% for exam, grade in exams %}
      <tr data-testid="exam-row"><td>{{ exam }}</td><td>{{ grade }}</td></tr>
      {% endfor %}
    </tbody>
  </table>
</main>
"""

CONTACT_PAGE = STYLE + """
<title>Contact</title>
{% include "nav.html" %}
<main>
  <h1>Contact</h1>
  <p>Questions about exams, bookings or your study plan? Get in touch with the student office.</p>
  <dl>
    <dt>Email</dt>
    <dd>
      <a href="mailto:student.office@example.com"
         data-testid="contact-email">student.office@example.com</a>
    </dd>
    <dt>Phone</dt>
    <dd data-testid="contact-phone">+39 095 000 0000</dd>
    <dt>Address</dt>
    <dd data-testid="contact-address">Student office, building A, room 12</dd>
  </dl>
  <h2>Office hours</h2>
  <table>
    <thead><tr><th>Day</th><th>Hours</th></tr></thead>
    <tbody>
      {% for day, hours in office_hours %}
      <tr data-testid="office-hours-row"><td>{{ day }}</td><td>{{ hours }}</td></tr>
      {% endfor %}
    </tbody>
  </table>
</main>
"""

BOOKING_PAGE = STYLE + """
<title>Book an exam</title>
{% include "nav.html" %}
<main>
  <h1>Book an exam</h1>
  {% for message in get_flashed_messages() %}
  <p role="status" data-testid="flash-message">{{ message }}</p>
  {% endfor %}
  <p data-testid="booking-count">Booked exams: {{ booked | length }}</p>
  <table>
    <thead><tr><th>Exam</th><th>Date</th><th>Status</th><th></th></tr></thead>
    <tbody>
      {% for exam_id, exam in upcoming_exams.items() %}
      <tr data-testid="upcoming-exam-row">
        <td>{{ exam.course }}</td>
        <td>{{ exam.date }}</td>
        <td data-testid="booking-status">
          {% if exam_id in booked %}Booked{% elif exam.full %}Full{% else %}Available{% endif %}
        </td>
        <td>
          <form method="post">
            <input type="hidden" name="exam_id" value="{{ exam_id }}">
            {% if exam_id in booked %}
            <button type="submit" name="action" value="cancel"
                    data-testid="cancel-button">Cancel</button>
            {% else %}
            <button type="submit" name="action" value="book" data-testid="book-button"
                    {% if exam.full %}disabled{% endif %}>Book</button>
            {% endif %}
          </form>
        </td>
      </tr>
      {% endfor %}
    </tbody>
  </table>
</main>
"""

PROFILE_PAGE = STYLE + """
<title>My profile</title>
{% include "nav.html" %}
<main>
  <h1>My profile</h1>
  {% for message in get_flashed_messages() %}
  <p role="status" data-testid="flash-message">{{ message }}</p>
  {% endfor %}
  {% if error %}<p role="alert" data-testid="profile-error">{{ error }}</p>{% endif %}
  <dl>
    <dt>Name</dt>
    <dd data-testid="profile-name">{{ user.name }}</dd>
    <dt>Student ID</dt>
    <dd data-testid="profile-student-id">{{ user.student_id }}</dd>
    <dt>Degree course</dt>
    <dd data-testid="profile-degree">{{ user.degree }}</dd>
  </dl>
  <h2>Settings</h2>
  <form method="post">
    <label for="email">Email</label>
    <input id="email" name="email" value="{{ settings.email }}" data-testid="email-input">
    <label for="language">Language</label>
    <select id="language" name="language" data-testid="language-select">
      {% for code, label in languages.items() %}
      <option value="{{ code }}" {% if code == settings.language %}selected{% endif %}>
        {{ label }}
      </option>
      {% endfor %}
    </select>
    <label>
      <input type="checkbox" name="notifications" data-testid="notifications-checkbox"
             {% if settings.notifications %}checked{% endif %}>
      Notify me about new exam dates
    </label>
    <button type="submit" data-testid="save-button">Save</button>
  </form>
</main>
"""


def login_required(view):
    @wraps(view)
    def wrapper(*args, **kwargs):
        if "username" not in session:
            return redirect(url_for("login"))
        return view(*args, **kwargs)

    return wrapper


@app.get("/")
def index():
    return redirect(url_for("login"))


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template_string(LOGIN_PAGE)

    username = request.form.get("username", "")
    user = USERS.get(username)

    if user is None or user["password"] != request.form.get("password"):
        return (
            render_template_string(LOGIN_PAGE, error="Invalid username or password"),
            401,
        )

    session["username"] = username
    return redirect(url_for("exams"))


@app.get("/exams")
@login_required
def exams():
    username = session["username"]
    return render_template_string(
        EXAMS_PAGE, name=USERS[username]["name"], exams=EXAMS[username]
    )


@app.get("/contact")
def contact():
    return render_template_string(CONTACT_PAGE, office_hours=OFFICE_HOURS)


# Bookings and profile settings live in the session cookie, not in the module:
# every browser context (so every Playwright test) starts from the same state.
@app.route("/booking", methods=["GET", "POST"])
@login_required
def booking():
    booked = session.get("bookings", [])
    if request.method == "GET":
        return render_template_string(
            BOOKING_PAGE, upcoming_exams=UPCOMING_EXAMS, booked=booked
        )

    exam_id = request.form.get("exam_id")
    exam = UPCOMING_EXAMS.get(exam_id)
    action = request.form.get("action")

    if exam is None:
        abort(400)
    if action == "book" and exam_id not in booked and not exam["full"]:
        session["bookings"] = booked + [exam_id]
        flash(f"Booked {exam['course']} on {exam['date']}")
    elif action == "cancel" and exam_id in booked:
        session["bookings"] = [b for b in booked if b != exam_id]
        flash(f"Cancelled the booking for {exam['course']}")
    else:
        abort(400)

    return redirect(url_for("booking"))


@app.route("/profile", methods=["GET", "POST"])
@login_required
def profile():
    user = USERS[session["username"]]
    if request.method == "GET":
        settings = session.get(
            "settings",
            {"email": user["email"], "language": "en", "notifications": True},
        )
        return render_template_string(
            PROFILE_PAGE, user=user, settings=settings, languages=LANGUAGES
        )

    settings = {
        "email": request.form.get("email", "").strip(),
        "language": request.form.get("language", ""),
        "notifications": "notifications" in request.form,
    }

    if not EMAIL_PATTERN.fullmatch(settings["email"]):
        error = "Enter a valid email address"
    elif settings["language"] not in LANGUAGES:
        error = "Choose a language from the list"
    else:
        session["settings"] = settings
        flash("Profile saved")
        return redirect(url_for("profile"))

    return (
        render_template_string(
            PROFILE_PAGE, user=user, settings=settings, languages=LANGUAGES, error=error
        ),
        400,
    )


@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
