from playwright.sync_api import Page, expect
from pages.exams_page import ContactPage


def test_contact_mail(page: Page) -> None:

    contact_page= ContactPage(page)

    # act
    ContactPage.goto()

    # assert
    expect(page.contact_mail).to_have_text("student.office@example.com")
