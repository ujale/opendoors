from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def test_units_available_module(driver):
    """
    Test the Unit Availability module for correct login, navigation, and unit assertions.
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

    # Step 3: Dashboard Module
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/Unit_Availability__c/home'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Select a List View: Unit Availability']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='This list is pinned.']"))).click()

    # Step 4: Assert available Unit
    unit1 = wait.until(ec.visibility_of_element_located((By.XPATH, '//span[@title="Unit Name" and contains(@class, "slds-truncate")]')))
    assert unit1.text == "Unit Name"
    unit2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//tr[@data-row-key-value='a2yEa0000012MOrIAM']//a[text()='news']")))
    assert unit2.text == "news"
    unit3 = wait.until(ec.visibility_of_element_located((By.XPATH, "//tr[@data-row-key-value='a2yEa0000012MOrIAM']//td[@data-col-key-value='0-rowNumber-0']")))
    assert unit3.text == "kkk"
    sleep(2)
