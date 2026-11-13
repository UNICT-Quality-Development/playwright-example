import re

from playwright.sync_api import Page, expect

from pages.contact_page import ContactPage


def test_contact_email(page: Page) -> None:
    # arrange
    contact_page = ContactPage(page)
    contact_page.goto()

    # assert
    expect(contact_page.email).to_have_text("student.office@example.com")