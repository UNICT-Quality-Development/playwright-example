from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.profile_page import ProfilePage


def test_student_id(page: Page) -> None:
    login_page = LoginPage(page)
    profile_page = ProfilePage(page)

    login_page.login("mario", "password123")

    profile_page.goto()

    expect(profile_page.student_id).to_have_text("1000012345")
