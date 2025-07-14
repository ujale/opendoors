from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def test_ods_support_module(driver):
    """
    Test the Support Request module for correct login, navigation, and button/icon assertions.
    """
    driver.get("https://opendoors--qa.sandbox.my.salesforce.com")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    action = ActionChains(driver)

    # Step 1: Login
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("udeme@opendoorsatl.org.qa")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1Gconnect!")
    driver.find_element(By.CSS_SELECTOR, "#Login").click()

    # Step 2: Home Page
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[class='slds-global-header__item'] div[class='slds-global-header__logo']"))).click()

    # Step 3: Support Request Module
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/Support_Request__c/home"]'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Select a List View: Support Request']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='This list is pinned.' and contains(@class, 'slds-button_icon-border-filled')]"))).click()

    # Step 4: Assert all other buttons
    Topbar1 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='New' and @role='button' and contains(@class, 'forceActionLink')]")))
    assert Topbar1.text == "New"
    Topbar2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Import' and @role='button' and contains(@class, 'forceActionLink')]")))
    assert Topbar2.text == "Import"
    Topbar3 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Change Owner' and @role='button' and contains(@class, 'forceActionLink')]")))
    assert Topbar3.text == "Change Owner"
    Topbar4 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Assign Label' and @role='button']")))
    assert Topbar4.text == "Assign Label"

    # Step 5: Assert available Icons
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='List View Controls' and contains(@class, 'slds-button_icon-more')]"))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Select list display' and contains(@class, 'slds-button_icon-more')]"))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Refresh' and @name='refreshButton' and contains(@class, 'slds-button_icon-border-filled')]"))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Edit List' and @name='inlineEditButton' and contains(@class, 'slds-button_icon-border-filled')]"))).click()
    sleep(2)


