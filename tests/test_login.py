import re

from playwright.sync_api import Page, expect


def test_login(page: Page) -> None:
    page.goto("/login")
    page.get_by_label("Username").fill("mario")
    page.get_by_label("Password").fill("password123")
    page.get_by_role("button", name="Log in").click()
    expect(page.get_by_role("heading", name="Welcome, Mario")).to_be_visible()


def test_wrong_password(page: Page) -> None:
    # arrange
    page.goto("/login")
    page.get_by_label("Username").fill("mario")
    page.get_by_label("Password").fill("wrong")
    # act
    page.get_by_role("button", name="Log in").click()
    # assert
    expect(page.get_by_role("alert")).to_have_text("Invalid username or password")
    expect(page).to_have_url(re.compile("/login"))
