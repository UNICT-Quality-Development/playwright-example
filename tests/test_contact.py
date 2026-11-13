from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenarios, then, when

from pages.contact_page import ContactPage

scenarios("features/contact.feature")

@when("I am on Contact page.", target_fixture="contact_page")
def open_contact_page(page: Page) -> ContactPage:
    contact_page = ContactPage(page)
    contact_page.goto()
    return contact_page

@then(parsers.parse('I should see the Email "{email}".'))
def see_email(contact_page: ContactPage, email: str) -> None:
    expect(contact_page.email).to_have_text(email)