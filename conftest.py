import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")                   # Run in headless mode
    options.add_argument("--no-sandbox")                 # Recommended for CI
    options.add_argument("--disable-dev-shm-usage")      # Recommended for CI
    options.add_argument("--window-size=1920,1080")      # Optional: for responsive testing

    driver = webdriver