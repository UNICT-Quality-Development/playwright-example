from playwright.sync_api import Page, expect


def test_login_page_title(page: Page) -> None:
    # act
    page.goto("/login")

    # assert
    expect(page).to_have_title("Student portal")
