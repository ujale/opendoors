from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def test_login_logout(driver):
    """
    Test login and logout functionality for the Open Doors QA site.
    """
    driver.get("https://community-qa.opendoorsatl.org")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    # Step 1: Login
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='Open Doors Community']")))
    driver.find_element(By.CSS_SELECTOR, "div#sfdc_username_container  .input.inputBox").send_keys("udeme@opendoorsatl.org.qa.casemanager")
    driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container  .input.inputBox").send_keys("13Gconnect#")
    driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label").click()
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Home")))

    # Step 2: Logout
    driver.find_element(By.CSS_SELECTOR, "img[class='profile-icon']").click()
    driver.find_element(By.CSS_SELECTOR, "a[title='Logout']").click()
    sleep(2)


