import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
import time

@pytest.mark.usefixtures("driver")
def test_ods_dashboard_module(driver):
    """
    Test the Dashboard module in the ODS Salesforce app.
    """
    fake = Faker()
    driver.get("https://opendoors--qa.sandbox.my.salesforce.com")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    # Login Page
    driver.find_element(By.CSS_SELECTOR, "#logo")
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("udeme@opendoorsatl.org.qa")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1Gconnect!")
    driver.find_element(By.CSS_SELECTOR, "#Login").click()

    # Home Page
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[class='slds-global-header__item'] div[class='slds-global-header__logo']"))).click()

    # Clicking on Dashboard Module
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/Dashboard/home"]'))).click()
    time.sleep(10)
    Sidebar1 = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='tab' and @title='Recent' and contains(@class, 'slds-nav-vertical__action')]")))
    assert Sidebar1.text == "Recent"
    Sidebar2 = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='tab' and @title='Created by Me' and contains(@class, 'slds-nav-vertical__action') and @aria-current='false']")))
    assert Sidebar2.text == "Created by Me"
    Sidebar3 = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='tab' and @title='Private Dashboards' and contains(@class, 'slds-nav-vertical__action') and @aria-current='false']")))
    assert Sidebar3.text == "Private Dashboards"
    Sidebar4 = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='tab' and @title='All Dashboards' and contains(@class, 'slds-nav-vertical__action') and @aria-current='false']")))
    assert Sidebar4.text == "All Dashboards"
    Sidebar5 = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='tab' and @title='All Folders' and contains(@class, 'slds-nav-vertical__action') and @aria-current='false']")))
    assert Sidebar5.text == "All Folders"
    Sidebar7 = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='tab' and @title='Created by Me' and contains(@class, 'slds-nav-vertical__action') and @aria-current='false']")))
    assert Sidebar7.text == "Created by Me"
    Sidebar8 = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='tab' and @title='Shared with Me' and contains(@class, 'slds-nav-vertical__action') and @aria-current='false']")))
    assert Sidebar8.text == "Shared with Me"
    Sidebar9 = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='tab' and @title='All Favorites' and contains(@class, 'slds-nav-vertical__action') and @aria-current='false']")))
    assert Sidebar9.text == "All Favorites"

    # Create a New Dashboard
    wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='button' and @title='New Dashboard' and contains(@class, 'forceActionLink')]")))
    # Create a new folder
    wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//button[@type='button' and @title='New Folder' and contains(@class, 'slds-button') and contains(@class, 'folderActionBar')]")))
    time.sleep(20)
