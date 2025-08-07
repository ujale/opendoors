
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.usefixtures("driver")
def test_ods_login_logout(driver):
    """
    Test login and logout functionality for the ODS Salesforce portal, including navigation and tab visibility.
    """
    driver.get("https://opendoors--qa.sandbox.my.salesforce.com")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    # Login Page
    driver.find_element(By.CSS_SELECTOR, "#logo")
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("udeme@opendoorsatl.org.qa")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1Gconnect!")
    driver.find_element(By.CSS_SELECTOR, "#Login").click()

    # Home Page
    driver.find_element(By.CSS_SELECTOR, "div[class='slds-global-header__item'] div[class='slds-global-header__logo']")
    title = driver.find_element(By.XPATH, "//span[@title='Open Doors']")
    print("Page title:", title.text)

    # SF Tabs
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Home']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Accounts']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Contacts']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Properties']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Referrals']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Reports']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Dashboards']")
    driver.find_element(By.XPATH, "//a[@class='slds-button slds-button_reset slds-context-bar__label-action']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='People']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Unit Availability']")
    driver.find_elements(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Applicants']")
    driver.find_element(By.XPATH, "//span[@class='slds-p-right_small']")
    driver.find_element(By.XPATH, "//lightning-icon[@class='slds-icon-utility-down slds-icon_container']//lightning-primitive-icon[@exportparts='icon']//*[name()='svg']").click()
    driver.find_element(By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Rental Concessions')]")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'DocuSign Envelope Recipients')]")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Property Inspection')]")

    # Home Page Dashboard
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "span[title='Today’s Tasks']")))
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "span[title=\"Today's Events\"]")))

    # Log out
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".tooltip-trigger.tooltipTrigger.uiTooltip .uiImage")))
    driver.find_element(By.CSS_SELECTOR, ".tooltip-trigger.tooltipTrigger.uiTooltip .uiImage").click()
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div.profile-card-toplinks>a[data-aura-class='uiOutputURL']"))).click()