from playwright.sync_api import Page, expect


def test_contact_email(page: Page) -> None:
    page.goto("/contact")

    contact_email = page.get_by_test_id("contact-email")

    expect(contact_email).to_have_text("student.office@example.com")
    expect(contact_email).to_have_attribute("href", "mailto:student.office@example.com")
