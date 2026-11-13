from playwright.sync_api import Page


class ContactPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.email = page.get_by_test_id("contact-email")

    def goto(self) -> None:
        self.page.goto("/contact")