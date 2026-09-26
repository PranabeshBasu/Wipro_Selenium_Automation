import os
import pytest

from utilities.config_reader import ConfigReader
from utilities.driver_factory import DriverFactory
from utilities.screenshot import Screenshot


@pytest.fixture(scope="session")
def driver():

    config = ConfigReader()

    driver = DriverFactory.get_driver(
        config.get_browser()
    )

    driver.get(config.get_base_url())

    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):

    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:

        driver = item.funcargs.get("driver")

        if driver:

            os.makedirs("screenshots", exist_ok=True)

            Screenshot.capture(
                driver,
                item.name
            )