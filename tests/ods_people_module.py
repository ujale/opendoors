from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def test_ods_people_module(driver):
    """
    Test the All Users list view: login, navigation, dropdown selection, pinning, and basic UI assertions.
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
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[class='slds-global-header__item'] div[class='slds-global-header__logo']"))).click()

    # Step 3: Navigate to Users Module
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/User/home"]'))).click()

    # Step 4: Open List View dropdown and select 'All Users'
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@role='button' and @title='Select a List View: People']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@role='option']//span[text()='All Users']"))).click()

    # Step 5: Pin the List View
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Pin this list view.']"))).click()

    # Step 6: Assert action buttons are visible
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='New' and contains(@class, 'forceActionLink')]"))).text == "New"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Import' and contains(@class, 'forceActionLink')]"))).text == "Import"

    # Step 7: Assert list view control icons are present
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='List View Controls' and contains(@class, 'slds-button_icon-more')]"))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Select list display' and contains(@class, 'slds-button_icon-more')]"))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Refresh' and @name='refreshButton' and contains(@class, 'slds-button_icon-border-filled')]"))).click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Edit List' and @name='inlineEditButton' and contains(@class, 'slds-button_icon-border-filled')]"))).click()

    sleep(2)
