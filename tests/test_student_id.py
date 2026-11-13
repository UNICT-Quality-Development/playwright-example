from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


def test_student_id(page: Page) -> None:

    login_page = LoginPage(page)
    profile_page = ProfilePage(page)

    login_page.goto()
    login_page.username.fill("mario")
    login_page.username.fill("password123")
    login_page.login()

    profile_page.goto()
    expect(profile_page.student_id).to_have_text("1000012345")
