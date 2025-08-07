
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("driver")
def test_casemanager_login_logout(driver):
    """
    Test login and logout functionality for the Case Manager portal.
    """
    driver.get("https://community-qa.opendoorsatl.org")
    driver.maximize_window()
    action = ActionChains(driver)
    wait = WebDriverWait(driver, 15)

    opdLogo = driver.find_element(By.CSS_SELECTOR, "img[alt='Open Doors Community']")
    loginField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_username_container  .input.inputBox")
    loginField.send_keys("udeme@opendoorsatl.org.qa.casemanager")
    passwordField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container  .input.inputBox")
    passwordField.send_keys("13Gconnect#")
    driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label").click()
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Home")))

    profileIcon = driver.find_element(By.CSS_SELECTOR, "img[class='profile-icon']")
    profileIcon.click()
    logoutLink = driver.find_element(By.CSS_SELECTOR, "a[title='Logout']")
    logoutLink.click()