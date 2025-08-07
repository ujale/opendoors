
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import Keys
from time import sleep

@pytest.mark.usefixtures("driver")
def test_create_applicant_only_referral(driver):
    """
    Test the 'Create Applicant Only Referral' flow for a Case Manager user.
    """
    driver.get("https://community-qa.opendoorsatl.org")
    driver.maximize_window()
    action = ActionChains(driver)
    wait = WebDriverWait(driver, 15)

    # Login
    opdLogo = driver.find_element(By.CSS_SELECTOR, "img[alt='Open Doors Community']")
    loginField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_username_container  .input.inputBox")
    loginField.send_keys("udeme@opendoorsatl.org.qa.casemanager")
    passwordField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container  .input.inputBox")
    passwordField.send_keys("13Gconnect#")
    driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label").click()

    # Wait for Home and navigate to Create Applicant Only Referral
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Home")))
    caorLink = driver.find_element(By.LINK_TEXT, "Create Applicant Only Referral")
    print(caorLink.text)
    caorLink.click()

    # Wait for Referral Creator page
    wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[@role='main']/div/div/div[@class='ui-widget']/div/div[3]/div/div/div[1]/c-referral-creator//article[@class='slds-card']//header")))
    raoHeader = driver.find_element(By.XPATH, "/html/body/div[3]/div[@role='main']/div/div/div[@class='ui-widget']/div/div[3]/div/div/div[1]/c-referral-creator//article[@class='slds-card']//header")
    print("Page Header is: ", raoHeader.text)

    # Select applicant
    applicantInputBox = driver.find_element(By.XPATH, "/html/body/div[3]/div[@role='main']/div/div/div[@class='ui-widget']/div/div[3]/div/div/div[1]/c-referral-creator//article[@class='slds-card']//c-custom-lookup-comp//div[@role='combobox']/div[@role='none']/input[@role='textbox']")
    applicantInputBox.click()
    applicantInputBox.send_keys(Keys.ARROW_DOWN)
    applicantInputBox.send_keys(Keys.RETURN)
    sleep(5)
    print("Searched Applicant is: ", applicantInputBox.text)

    # Optionally, add more assertions or steps as needed