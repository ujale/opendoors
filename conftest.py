import os
import platform
from datetime import datetime
import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture
def driver():
    options = Options()

    # Enable headless Chrome (new mode is more stable)
    options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")

    # Set Chrome binary location for macOS only (local dev)
    if platform.system() == "Darwin":
        mac_chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        if os.path.exists(mac_chrome_path):
            options.binary_location = mac_chrome_path

    # Create WebDriver instance
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()),
        options=options
    )

    yield driver
    driver.quit()

# Auto-capture screenshot on failure + attach to Allure
@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    if result.when == "call" and result.failed:
        driver = item.funcargs.get("driver", None)
        if driver:
            os.makedirs("screenshots", exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            test_name = item.name
            screenshot_path = f"screenshots/{test_name}_{timestamp}.png"
            driver.save_screenshot(screenshot_path)
            print(f"📸 Screenshot saved: {screenshot_path}")

            # Attach screenshot to Allure report
            with open(screenshot_path, "rb") as image_file:
                allure.attach(image_file.read(), name=f"{test_name}_failure", attachment_type=allure.attachment_type.PNG)
