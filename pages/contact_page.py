from playwright.sync_api import Page


class ContactPage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.email = page.get_by_test_id("contact-email")
        self.phone = page.get_by_test_id("contact-phone")
        self.address = page.get_by_test_id("contact-address")

    def goto(self) -> None:
        self.page.goto("/contact")