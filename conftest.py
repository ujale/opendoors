import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import allure

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")  # "new" is more stable for newer Chrome versions
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # For CI: rely on Chrome installed in PATH
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            os.makedirs("html", exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name

            screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
            html_path = f"html/{test_name}_{timestamp}.html"

            driver.save_screenshot(screenshot_path)
            with open(screenshot_path, "rb") as img_file:
                allure.attach(img_file.read(), name=f"{test_name}_screenshot", attachment_type=allure.attachment_type.PNG)

            with open(html_path, "w", encoding="utf-8") as f:
                f.write(driver.page_source)
            allure.attach(driver.page_source, name=f"{test_name}_html", attachment_type=allure.attachment_type.HTML)