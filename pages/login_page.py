from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = page.get_by_test_id("username-input")
        self.password = page.get_by_test_id("password-input")
        self.submit = page.get_by_test_id("login-button")
        self.error = page.get_by_test_id("login-error")

    def goto(self) -> None:
        self.page.goto("/login")

    def login(self, username: str, password: str) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()
