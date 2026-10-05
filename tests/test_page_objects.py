from playwright.sync_api import Page, expect

from pages.exams_page import ExamsPage
from pages.login_page import LoginPage


def test_exams_after_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("mario", "password123")
    exams_page = ExamsPage(page)
    expect(exams_page.greeting).to_have_text(
        "Welcome, Mario"
    )
    expect(exams_page.rows).to_have_count(3)
