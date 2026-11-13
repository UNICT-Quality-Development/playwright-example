from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenarios, then, when

from pages.contact_page import ContactPage

scenarios("features/contact.feature")


@given("I am on the contact page", target_fixture="contact_page")
def open_contact_page(page: Page) -> ContactPage:
    contact_page = ContactPage(page)
    contact_page.goto()
    return contact_page


@then(parsers.parse('I see the email "{text}"'))
def see_email(page: Page, text: str) -> None:
    contact_page = ContactPage(page)
    expect(contact_page.email).to_have_text(text)
