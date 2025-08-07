import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
import time

@pytest.mark.usefixtures("driver")
def test_ods_docusign_module(driver):
    """
    Test the DocuSign module in the ODS Salesforce app.
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

    # Clicking on Docusign Module
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/dfsle__Recipient__c/home"'))).click()
    # Docusign Dropdown
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Select a List View: DocuSign Envelope Recipients' and contains(@class, 'slds-button_icon-container')]"))).click()
    # Pin Recently viewed
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='This list is pinned.' and contains(@class, 'slds-button_icon')]"))).click()

    # Assert all other buttons
    Topbar1 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='New' and contains(@class, 'forceActionLink')]")))
    assert Topbar1.text == "New"
    Topbar2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Import' and contains(@class, 'forceActionLink')]")))
    assert Topbar2.text == "Import"
    Topbar3 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Assign Label' and contains(@class, 'forceActionLink')]")))
    assert Topbar3.text == "Assign Label"

    # Assert available Icons
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='List View Controls' and contains(@class, 'slds-button_icon-more')]"))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Select list display' and contains(@class, 'slds-button_icon-more')]"))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Refresh' and @name='refreshButton' and contains(@class, 'slds-button_icon-border-filled')]"))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Edit List' and @name='inlineEditButton' and contains(@class, 'slds-button_icon-border-filled')]"))).click()

    time.sleep(20)