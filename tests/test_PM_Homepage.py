from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from time import sleep

def test_pm_homepage(driver):
    """
    Test the Property Manager homepage for correct topbar and dashboard elements.
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

    # Step 2: Assert all topbar buttons
    Topbar1 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/s/"]')))
    assert Topbar1.text == "Home"
    Topbar2 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/s/property/Property__c/Default"]')))
    assert Topbar2.text == "Property"
    Topbar3 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://properties-dev.opendoorsatl.org/"]')))
    assert Topbar3.text == "Property Locator App"
    sleep(2)
    Topbar4 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://www.google.com"]')))
    assert Topbar4.text == "Platform Guide"
    Topbar5 = driver.find_element(By.CSS_SELECTOR, 'button[title="Expand search"]')
    Topbar6 = driver.find_element(By.CSS_SELECTOR, 'button.slds-global-actions__notifications[aria-haspopup="dialog"]')

    # Step 3: Dashboard
    iframe = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#dashboardFrameWrapper > div > div.dashboardContainer > iframe")))
    driver.switch_to.frame(iframe)

    element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'span.slds-page-header__title.slds-truncate[title="Property Manager Dashboard"]')))
    print("HomePage Title is :", element.text)
    refresh = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "button.slds-button.slds-button_neutral.refresh")))
    TARSClink = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and contains(text(), 'View Report')]")))
    print("Chart of :", TARSClink.text)
    PTLlink = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and @data-id='00OEa000004PhVhMAK' and contains(., 'Property Tenant List')]")))
    print("Chart of :", PTLlink.text)
    TLVRlink = wait.until(ec.presence_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and @data-id='00OEa0000046fNxMAI' and contains(., 'Total Lease Violation Request')]")))
    print("Chart of :", TLVRlink.text)
    TSRlink = wait.until(ec.presence_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and @data-id='00OEa0000046eTXMAY' and contains(., 'Total Support Request')]")))
    print("Chart of :", TSRlink.text)
    sleep(2)
    TPIUlink = wait.until(ec.presence_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and @data-id='00OEa0000046fSnMAI' and contains(., 'Total Property Information Update')]")))
    print("Chart of :", TPIUlink.text)
    TUISlink = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and @data-id='00OEa0000046fUPMAY' and contains(., 'Total Unit Information Update')]")))
    print("The Report link is labelled: ", TUISlink.text)
    sleep(2)