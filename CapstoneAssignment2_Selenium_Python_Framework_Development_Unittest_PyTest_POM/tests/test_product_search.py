import pytest
from pages.home_page import HomePage
from pages.product_page import ProductPage
from utilities.csv_reader import CSVReader


@pytest.mark.order(2)
def test_product_search(driver):

    data = CSVReader.read_data()[0]

    home_page = HomePage(driver)
    product_page = ProductPage(driver)

    home_page.search_product(data["product"])

    product_name = product_page.get_product_name()

    assert data["product"].lower() in product_name.lower()


