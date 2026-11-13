from playwright.sync_api import Page, expect

def test_contact_email(page: Page):
    page.goto("http://127.0.0.1:5000/contact")
    email = page.get_by_text("student.office@example.com")
    expect(email).to_be_visible()