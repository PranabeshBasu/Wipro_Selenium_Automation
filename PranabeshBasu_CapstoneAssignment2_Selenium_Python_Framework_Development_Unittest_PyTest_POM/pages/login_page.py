import time
from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

        self.my_account = (By.XPATH, "//span[text()='My Account']")
        self.login_link = (By.LINK_TEXT, "Login")
        self.email = (By.ID, "input-email")
        self.password = (By.ID, "input-password")
        self.login_button = (By.CSS_SELECTOR, "input[type='submit'][value='Login']")

    def open_login_page(self):
        self.driver.find_element(*self.my_account).click()
        time.sleep(2)

        self.driver.find_element(*self.login_link).click()
        time.sleep(2)

    def login(self, username, password):
        self.driver.find_element(*self.email).send_keys(username)
        time.sleep(1)

        self.driver.find_element(*self.password).send_keys(password)
        time.sleep(1)

        self.driver.find_element(*self.login_button).click()
        time.sleep(3)