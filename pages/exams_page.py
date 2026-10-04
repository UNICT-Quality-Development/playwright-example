from playwright.sync_api import Locator, Page


class ExamsPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.greeting: Locator = page.get_by_role("heading", level=1)
        self.rows: Locator = page.get_by_test_id("exam-row")
        self.logout_button: Locator = page.get_by_role("button", name="Log out")

    def logout(self) -> None:
        self.logout_button.click()
