from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from time import sleep

def test_pm_property(driver):
    """
    Test the Property page for correct navigation and icon presence.
    """
    driver.get("https://community-qa.opendoorsatl.org")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    action = ActionChains(driver)

    # Step 1: Login
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='Open Doors Community']")))
    login_field = driver.find_element(By.CSS_SELECTOR, "div#sfdc_username_container  .input.inputBox")
    login_field.send_keys("tess@wrcdv.org.qa")
    password_field = driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container  .input.inputBox")
    password_field.send_keys("1Gconnect*")
    login_btn = driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label")
    login_btn.click()
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Home")))

    # Step 2: Navigate to Property section and pin All Properties
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/s/property/Property__c/Default"]'))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(@title, 'Select a List View') and @role='button']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//li[@role='presentation' and contains(@class, 'forceVirtualAutocompleteMenuOption') and .//span[text()='All Properties']]"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Pin this list view.']"))).click()

    # Step 3: Assert all other icons
    wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='search' and contains(@class, 'slds-input') and @placeholder='Search this list...']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='List View Controls' and contains(@class, 'slds-button_icon-more')]")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Select list display' and contains(@class, 'slds-button_icon-more')]")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Refresh' and @name='refreshButton']")))
    wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Edit List' and @name='inlineEditButton']")))
    sleep(2)

