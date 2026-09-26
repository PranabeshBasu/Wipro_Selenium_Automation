import pytest
from pages.login_page import LoginPage


def test_invalid_login(driver):
    login_page = LoginPage(driver)

    login_page.open_login_page()
    login_page.login("wrong@example.com", "wrongpassword")

    assert "Warning: No match for E-Mail Address and/or Password." not in driver.page_source