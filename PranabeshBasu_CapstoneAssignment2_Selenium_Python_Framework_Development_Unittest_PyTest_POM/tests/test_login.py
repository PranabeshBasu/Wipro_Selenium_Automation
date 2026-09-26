import pytest
from pages.login_page import LoginPage
from utilities.csv_reader import CSVReader


@pytest.mark.order(1)
def test_login(driver):

    data = CSVReader.read_data()[0]

    login_page = LoginPage(driver)

    login_page.open_login_page()

    login_page.login(
        data["username"],
        data["password"]
    )

    assert "My Account" in driver.page_source


