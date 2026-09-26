from selenium import webdriver


class DriverFactory:

    @staticmethod
    def get_driver(browser):
        if browser.lower() == "chrome":
            driver = webdriver.Chrome()
        elif browser.lower() == "firefox":
            driver = webdriver.Firefox()
        else:
            raise ValueError(f"Unsupported browser: {browser}")

        driver.maximize_window()
        driver.implicitly_wait(2)

        return driver