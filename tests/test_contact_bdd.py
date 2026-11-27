from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenarios, then

from pages.contact_page import ContactPage

scenarios("features/contact.feature")


@given("I'm on the contact page", target_fixture="contact_page")
def open_contact_page(page: Page) -> ContactPage:
    contact_page = ContactPage(page)
    contact_page.goto()
    return contact_page


@then("the student office email is visible")
def email_is_visible(contact_page: ContactPage) -> None:
    expect(contact_page.email).to_be_visible()


@then(parsers.parse('the email is "{email}"'))
def email_has_expected_text(contact_page: ContactPage, email: str) -> None:
    expect(contact_page.email).to_have_text(email)
