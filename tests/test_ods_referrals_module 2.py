from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def test_ods_referrals_module(driver):
    """
    Test the Referrals module for correct login, navigation, and referral editing.
    """

    driver.get("https://opendoors--qa.sandbox.my.salesforce.com")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    # Step 1: Login
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("udeme@opendoorsatl.org.qa")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1Gconnect!")
    driver.find_element(By.CSS_SELECTOR, "#Login").click()

    # Step 2: Home Page
    driver.find_element(By.CSS_SELECTOR, "div[class='slds-global-header__item'] div[class='slds-global-header__logo']")
    wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/div/div/h1/span")))

    # Step 3: Referral Tab
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/Case/home"]'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".slds-dropdown-trigger.slds-dropdown-trigger_click.lst-temp-slds-lineHeight > button"))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'span.virtualAutocompleteOptionText'))).click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".slds-grid.slds-grow"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body//button[@name='Edit' and contains(@class, 'slds-button')]"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@role='combobox' and @aria-label='Status' and contains(@class, 'slds-combobox__input')]"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@type='button' and @name='SaveEdit' and contains(@class, 'slds-button_brand')]"))).click()
    sleep(2)