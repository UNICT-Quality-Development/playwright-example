from playwright.sync_api import Page, expect


def test_contact_email(page: Page) -> None:
    page.goto("/contact")
    email = page.get_by_text("student.office@example.com")
    expect(email).to_be_visible()
