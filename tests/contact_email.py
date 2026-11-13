from playwright.sync_api import Page, expect
from pytest_bdd import given, parsers, scenarios, then

scenarios("features/contact.feature")


@given("I am on the contact page")
def open_contact_page(page: Page) -> None:
    page.goto("/contact")


@then(parsers.parse('I see the contact email "{email}"'))
def verify_contact_email(page: Page, email: str) -> None:
    contact_email = page.get_by_test_id("contact-email")

    expect(contact_email).to_have_text(email)
    expect(contact_email).to_have_attribute("href", f"mailto:{email}")