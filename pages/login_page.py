from playwright.sync_api import Locator, Page

from pages.exams_page import ExamsPage


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username: Locator = page.get_by_label("Username")
        self.password: Locator = page.get_by_label("Password")
        self.submit: Locator = page.get_by_role("button", name="Log in")
        self.error: Locator = page.get_by_role("alert")

    def goto(self) -> None:
        self.page.goto("/login")

    def login(self, username: str, password: str) -> ExamsPage:
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()
        return ExamsPage(self.page)
