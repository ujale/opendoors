from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep


from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from time import sleep

def test_create_applicant_only_referral(driver):
    """
    Automates the login and applicant-only referral creation process on the Open Doors QA site.
    """
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)
    action = ActionChains(driver)

    driver.get("https://community-qa.opendoorsatl.org")

    # Step 2: Login
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "img[alt='Open Doors Community']")))
    login_field = driver.find_element(By.CSS_SELECTOR, "div#sfdc_username_container .input.inputBox")
    login_field.send_keys("udeme@opendoorsatl.org.qa.casemanager")

    password_field = driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container .input.inputBox")
    password_field.send_keys("13Gconnect#")

    login_btn = driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label")
    login_btn.click()

    # Step 3: Wait for home and navigate to CAOR
    wait.until(EC.visibility_of_element_located((By.LINK_TEXT, "Home")))
    caor_link = driver.find_element(By.LINK_TEXT, "Create Applicant Only Referral")
    print("CAOR Link Text:", caor_link.text)
    caor_link.click()

    # Step 4: Wait for page header
    wait.until(EC.visibility_of_element_located((
        By.XPATH,
        "//article[@class='slds-card']//header"
    )))
    rao_header = driver.find_element(By.XPATH, "//article[@class='slds-card']//header")
    print("Page Header is:", rao_header.text)

    # Step 5: Applicant selection
    applicant_input_box = driver.find_element(By.XPATH, "//c-custom-lookup-comp//input[@role='textbox']")
    applicant_input_box.click()
    applicant_input_box.send_keys(Keys.ARROW_DOWN)
    applicant_input_box.send_keys(Keys.RETURN)
    sleep(5)
    print("Searched Applicant is:", applicant_input_box.get_attribute("value"))
