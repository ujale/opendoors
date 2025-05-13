from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import Select
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver import Keys
from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://community-qa.opendoorsatl.org")
driver.maximize_window()
action = ActionChains(driver)
wait = WebDriverWait(driver, 15)
opdLogo = driver.find_element(By.CSS_SELECTOR, "img[alt='Open Doors Community']")
loginField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_username_container  .input.inputBox")
loginField.send_keys("tess@wrcdv.org.qa")
passwordField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container  .input.inputBox")
passwordField.send_keys("1Gconnect")
loginBtn = driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label").click()
wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Home")))

#Assert all other buttons

Topbar1= wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/s/"]')))
assert Topbar1.text== "Home"
Topbar2 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/s/property/Property__c/Default"]')))
assert Topbar2.text== "Property"
Topbar3 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://properties-dev.opendoorsatl.org/"]')))
assert Topbar3.text== "Property Locator App"
sleep(10)
Topbar4 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://www.google.com"]')))
assert Topbar4.text== "Platform Guide"
Topbar5 = driver.find_element(By.CSS_SELECTOR, 'button[title="Expand search"]')
Topbar6 = driver.find_element(By.CSS_SELECTOR, 'button.slds-global-actions__notifications[aria-haspopup="dialog"]')

# Dashboard

# Wait for the iframe to load and locate it
iframe = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#dashboardFrameWrapper > div > div.dashboardContainer > iframe")))
# Switch to the iframe
driver.switch_to.frame(iframe)

# Locate the element inside the iframe
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'span.slds-page-header__title.slds-truncate[title="Property Manager Dashboard"]' )))
print("HomePage Title is :", element.text)
#refresh button
refresh = wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "button.slds-button.slds-button_neutral.refresh")))
# Total Agency Referral submitted Chart
TARSClink = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and contains(text(), 'View Report')]")))
print("Chart of :", TARSClink.text)
#Property Tenant List
PTLlink = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and @data-id='00OEa000004PhVhMAK' and contains(., 'Property Tenant List')]")))
print("Chart of :", PTLlink.text)
# Total List Violation Request
TLVRlink = wait.until(ec.presence_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and @data-id='00OEa0000046fNxMAI' and contains(., 'Total Lease Violation Request')]")))
print("Chart of :", TLVRlink.text)
#Total Support Request
TSRlink =wait.until(ec.presence_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and @data-id='00OEa0000046eTXMAY' and contains(., 'Total Support Request')]")))
print("Chart of :", TSRlink.text)
sleep(5)
# Total Property Information Update
TPIUlink = wait.until(ec.presence_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and @data-id='00OEa0000046fSnMAI' and contains(., 'Total Property Information Update')]")))
print("Chart of :", TPIUlink.text)
#Total Unit Information Update
TUISlink = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='truncation enabledLink' and @data-id='00OEa0000046fUPMAY' and contains(., 'Total Unit Information Update')]")))
print("The Report link is labelled: ", TUISlink.text)

sleep(15)

driver.quit()