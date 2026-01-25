from pages.login_page import LoginPage

def test_valid_login(page):
    login = LoginPage(page)
    login.login("testuser", "password")
    assert page.title() is not None
