from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then, parsers

from pages.contact_page import ContactPage

scenarios("features/contact_email.feature")


@given("I am on the contact page", target_fixture="contact_page")
def open_contact_page(page: Page) -> ContactPage:
    contact_page = ContactPage(page)
    contact_page.goto()
    return contact_page


@then(parsers.parse('I see the contact email "{email}"'))
def see_contact_email(contact_page: ContactPage, email: str) -> None:
    expect(contact_page.email).to_have_text(email)