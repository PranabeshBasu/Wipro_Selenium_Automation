import pytest
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from utilities.csv_reader import CSVReader


@pytest.mark.order(3)
def test_add_product_to_cart(driver):

    data = CSVReader.read_data()[0]

    quantity = data["quantity"]

    product_page = ProductPage(driver)
    cart_page = CartPage(driver)

    product_page.add_to_cart()

    product_page.open_cart()

    assert "checkout/cart" in driver.current_url

    cart_page.update_quantity(quantity)

    updated_quantity = cart_page.get_quantity()

    assert updated_quantity == quantity


