import re

from playwright.sync_api import Page, expect


def test_student_id(page: Page) -> None:
    # arrange
    page.goto("/login")
    page.get_by_label("Username").fill("mario")
    page.get_by_label("Password").fill("password123")

    # act
    page.get_by_role("button", name="Log in").click()

    # assert
    expect(page.get_by_role("heading", name="Welcome, Mario")).to_be_visible()

    page.goto("/profile")

    student_id = page.get_by_test_id("profile-student-id")
    expect(student_id).to_be_visible()
    expect(student_id).to_have_text("1000012345")

