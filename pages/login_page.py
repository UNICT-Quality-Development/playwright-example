from playwright.sync_api import Page


class LoginPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username = page.get_by_label("Username")
        self.password = page.get_by_label("Password")
        self.submit = page.get_by_role(
            "button", name="Log in"
        )
        self.error = page.get_by_role("alert")

    def goto(self) -> None:
        self.page.goto("/login")

    def login(
        self, username: str, password: str
    ) -> None:
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()
