from playwright.sync_api import Page, expect

def test_email_page(page: Page) -> None:
    # 1. Inserisci l'URL completo (es. "http://localhost:3000/contact" o il sito reale)
    page.goto("/contact")
    
    # 2. Sintassi Python (niente 'const' o ';')
    email_value = page.locator('dt:text-is("Email") + dd')

    # 3. Verifica (niente 'await' perché stiamo usando la sync_api, e to_contain_text in snake_case)
    expect(email_value).to_contain_text("student.office@example.com")