from playwright.sync_api import Page, expect

def test_email_page(page: Page) -> None:
    # 1. Inserisci l'URL completo (es. "http://localhost:3000/contact" o il sito reale)
    page.goto("/contact")
    
    # 2. Sintassi Python (niente 'const' o ';')
    email_value = page.locator('dt:text-is("Email") + dd')

    # 3. Verifica (niente 'await' perché stiamo usando la sync_api, e to_contain_text in snake_case)
    expect(email_value).to_contain_text("student.office@example.com")

def test_example(page:Page) -> None:
    page.goto("/login")
    page.get_by_role("textbox",name="Username").click()
    page.get_by_role("textbox",name = "Username").fill("mario")
    page.get_by_role("textbox",name="Password").click()
    page.get_by_role("textbox",name="Password").fill("password123")
    page.get_by_role("button", name="Log in").click()
    page.goto("/profile")
    matr_value = page.locator('dt:text-is("Student ID") + dd')
    expect(matr_value).to_contain_text("1000012345")