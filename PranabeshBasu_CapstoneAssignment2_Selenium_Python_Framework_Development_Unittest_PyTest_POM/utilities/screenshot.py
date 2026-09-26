import os
from datetime import datetime


class Screenshot:

    @staticmethod
    def capture(driver, name="screenshot"):

        screenshot_dir = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "screenshots"
        )

        os.makedirs(
            screenshot_dir,
            exist_ok=True
        )

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        file_path = os.path.join(
            screenshot_dir,
            f"{name}_{timestamp}.png"
        )

        driver.save_screenshot(file_path)

        return file_path