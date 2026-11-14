from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenarios, then, when

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage

scenarios("features/student_id.feature")


@given(parsers.parse('I log in as "{username}" with password "{password}"'))
def login_as_user(page: Page, username: str, password: str) -> None:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login(username, password)


@when("I goto profile page", target_fixture="profile_page")
def goto_profile_page(page: Page) -> ProfilePage:
    profile_page = ProfilePage(page)
    profile_page.goto()
    return profile_page


@then(parsers.parse('I see the student ID "{student_id}"'))
def see_student_id(profile_page: ProfilePage, student_id: str) -> None:
    expect(profile_page.student_id).to_have_text(student_id)


@then("I do not see any student ID")
def dont_see_student_id(profile_page: ProfilePage) -> None:
    expect(profile_page.student_id).to_have_count(0)


@then("I cannot enter profile page")
def dont_see_student_id(page: Page) -> None:
    expect(page).not_to_have_url("/profile")
