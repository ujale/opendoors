import os
from datetime import datetime
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Get the outcome of the test run
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            # Create directories for attachments
            os.makedirs("screenshots", exist_ok=True)
            os.makedirs("html", exist_ok=True)

            timestamp = datetime.now().strftime("%d%m%Y_%H%M%S")
            test_name = item.name.replace("/", "_").replace("\\", "_")

            # Screenshot
            screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            with open(screenshot_path, "rb") as f:
                allure.attach(f.read(), name=f"{test_name}_screenshot", attachment_type=allure.attachment_type.PNG)

            # HTML source
            html_path = f"html/{test_name}_{timestamp}.html"
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            allure.attach(driver.page_source, name=f"{test_name}_html", attachment_type=allure.attachment_type.HTML)


def take_screenshot(driver, name="screenshot"):
    """
    Utility to take a screenshot manually during a test step.
    """
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG
    )
