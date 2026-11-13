import re

from playwright.sync_api import Page, expect


def test_contact_email(page: Page) -> None:
    # arrange
    page.goto("/contact")
    contact_email = page.get_by_test_id("contact-email")
    expect(contact_email).to_be_visible()
    expect(contact_email).to_have_text("student.office@example.com")

