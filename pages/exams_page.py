from playwright.sync_api import Page


class ExamsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.greeting = page.get_by_role("heading")
        self.rows = page.get_by_test_id("exam-row")
        self.logout_button = page.get_by_role(
            "button", name="Log out"
        )

    def logout(self) -> None:
        self.logout_button.click()
