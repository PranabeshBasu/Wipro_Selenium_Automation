import time
from selenium.webdriver.common.by import By


class ProductPage:

    def __init__(self, driver):
        self.driver = driver

        self.product_name = (
            By.CSS_SELECTOR,
            "div.product-thumb h4 a"
        )

        self.add_to_cart_button = (
            By.CSS_SELECTOR,
            "button[onclick*='cart.add']"
        )

        self.shopping_cart_link = (
            By.CSS_SELECTOR,
            "a[href*='route=checkout/cart']"
        )

    def get_product_name(self):
        return self.driver.find_element(
            *self.product_name
        ).text

    def add_to_cart(self):
        self.driver.find_element(
            *self.add_to_cart_button
        ).click()

        time.sleep(2)

    def open_cart(self):
        self.driver.find_element(
            *self.shopping_cart_link
        ).click()

        time.sleep(3)