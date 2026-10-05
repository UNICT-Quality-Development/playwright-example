from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenarios, then, when

from pages.exams_page import ExamsPage
from pages.login_page import LoginPage

scenarios("features/login.feature")


@given("I am on the login page",
       target_fixture="login_page")
def open_login_page(page: Page) -> LoginPage:
    login_page = LoginPage(page)
    login_page.goto()
    return login_page


@when(
    parsers.parse(
        'I log in as "{username}" '
        'with password "{password}"'
    )
)
def log_in(
    login_page: LoginPage, username: str, password: str
) -> None:
    login_page.login(username, password)


@then(parsers.parse('I see the greeting "{text}"'))
def see_greeting(page: Page, text: str) -> None:
    exams_page = ExamsPage(page)
    expect(exams_page.greeting).to_have_text(text)
