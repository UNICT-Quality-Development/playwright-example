from flask import Flask, redirect, render_template_string, request, session, url_for

app = Flask(__name__)
app.secret_key = "dev"  # demo only, never hard-code a real secret

USERS = {"mario": {"password": "password123", "name": "Mario"}}
EXAMS = {"mario": [("Programming 1", 28), ("Algorithms", 30), ("Databases", 27)]}

STYLE = """
<!doctype html>
<meta charset="utf-8">
<style>
  body { font-family: sans-serif; background: #f4f6fa; color: #1f2937; margin: 0; }
  main { max-width: 420px; margin: 60px auto; background: #fff; padding: 32px;
         border-radius: 8px; box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1); }
  h1 { margin-top: 0; font-size: 1.6em; }
  label { display: block; margin-top: 12px; font-weight: bold; }
  input { width: 100%; box-sizing: border-box; padding: 8px; margin-top: 4px; }
  button { margin-top: 20px; padding: 8px 20px; background: #1d4ed8; color: #fff;
           border: none; border-radius: 4px; font-size: 1em; cursor: pointer; }
  table { width: 100%; border-collapse: collapse; }
  th, td { text-align: left; padding: 8px; border-bottom: 1px solid #e5e7eb; }
  [role="alert"] { color: #b91c1c; }
</style>
"""

LOGIN_PAGE = STYLE + """
<title>Student portal</title>
<main>
  <h1>Student portal</h1>
  {% if error %}<p role="alert">{{ error }}</p>{% endif %}
  <form method="post">
    <label for="username">Username</label>
    <input id="username" name="username">
    <label for="password">Password</label>
    <input id="password" name="password" type="password">
    <button type="submit">Log in</button>
  </form>
</main>
"""

EXAMS_PAGE = STYLE + """
<title>My exams</title>
<main>
  <h1>Welcome, {{ name }}</h1>
  <table>
    <thead><tr><th>Exam</th><th>Grade</th></tr></thead>
    <tbody>
      {% for exam, grade in exams %}
      <tr data-testid="exam-row"><td>{{ exam }}</td><td>{{ grade }}</td></tr>
      {% endfor %}
    </tbody>
  </table>
  <form method="post" action="{{ url_for('logout') }}">
    <button type="submit">Log out</button>
  </form>
</main>
"""


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
        return render_template_string(LOGIN_PAGE, error="Invalid username or password"), 401
    session["username"] = username
    return redirect(url_for("exams"))


@app.get("/exams")
def exams():
    username = session.get("username")
    if username is None:
        return redirect(url_for("login"))
    return render_template_string(
        EXAMS_PAGE, name=USERS[username]["name"], exams=EXAMS[username]
    )


@app.post("/logout")
def logout():
    session.clear()
    return redirect(url_for("login"))
