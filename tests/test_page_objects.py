import re

from playwright.sync_api import Page, expect

from pages.exams_page import ExamsPage
from pages.login_page import LoginPage


def test_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("mario", "password123")

    exams_page = ExamsPage(page)
    expect(exams_page.greeting).to_have_text("Welcome, Mario")


def test_wrong_password(page: Page) -> None:
    # arrange
    login_page = LoginPage(page)
    login_page.goto()

    # act
    login_page.login("mario", "wrong")

    # assert
    expect(login_page.error).to_have_text("Invalid username or password")
    expect(page).to_have_url(re.compile("/login"))


def test_exams_after_login(page: Page) -> None:
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("mario", "password123")

    exams_page = ExamsPage(page)
    expect(exams_page.greeting).to_have_text("Welcome, Mario")
    expect(exams_page.rows).to_have_count(3)
