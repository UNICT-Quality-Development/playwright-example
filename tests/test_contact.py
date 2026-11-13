from playwright.sync_api import Page, expect


def test_contact_mail(page: Page) -> None:
    # act
    page.goto("/contact")

    # assert
    expect(page.get_by_test_id("contact-email")).to_have_text("student.office@example.com")
