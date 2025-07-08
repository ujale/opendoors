from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def test_pm_login_logout(driver):
    """
    Test login and logout functionality for the Property Manager user.
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

    # Step 2: Logout
    profile_icon = driver.find_element(By.CSS_SELECTOR, "img[class='profile-icon']")
    profile_icon.click()
    logout_link = driver.find_element(By.CSS_SELECTOR, "a[title='Logout']")
    logout_link.click()
    sleep(2)