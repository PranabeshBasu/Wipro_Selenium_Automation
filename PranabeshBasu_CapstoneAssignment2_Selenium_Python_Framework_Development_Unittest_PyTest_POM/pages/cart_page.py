import time
from selenium.webdriver.common.by import By


class CartPage:

    def __init__(self, driver):

        self.driver = driver

        self.quantity_input = (
            By.CSS_SELECTOR,
            "input[name^='quantity']"
        )

        self.update_button = (
            By.CSS_SELECTOR,
            "button[data-original-title='Update']"
        )

    def update_quantity(self, quantity):

        quantity_field = self.driver.find_element(
            *self.quantity_input
        )

        quantity_field.click()
        quantity_field.clear()
        quantity_field.send_keys(str(quantity))

        time.sleep(1)

        self.driver.find_element(
            *self.update_button
        ).click()

        time.sleep(3)

    def get_quantity(self):

        quantity_field = self.driver.find_element(
            *self.quantity_input
        )

        return quantity_field.get_attribute("value")