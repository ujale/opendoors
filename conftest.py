import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless=new")                   # Comment this out if you want to watch the browser
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")        # Important for headless rendering on macOS
    options.add_argument("--enable-features=NetworkService,NetworkServiceInProcess")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    
    #Set Chrome binary manually
    options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

    driver = webdriver.Chrome(options=options)
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
