from playwright.sync_api import Page


class ProfilePage:
    def __init__(self, page: Page) -> None:
        self.page = page
        self.name = page.get_by_test_id("profile-name")
        self.student_id = page.get_by_test_id("profile-student-id")
        self.degree_course = page.get_by_test_id("profile-degree")

    def goto(self):
        self.page.goto('/profile')