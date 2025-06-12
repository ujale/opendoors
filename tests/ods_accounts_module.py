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

driver.get("https://opendoors--qa.sandbox.my.salesforce.com")
driver.maximize_window()

wait = WebDriverWait(driver, 15)
# Login Page
driver.find_element(By.CSS_SELECTOR, "#logo")
driver.find_element(By.CSS_SELECTOR, "#username").send_keys("udeme@opendoorsatl.org.qa")
driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1Gconnect.")
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
#Accounts Tab
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[title="Accounts"]')))
driver.find_element(By.CSS_SELECTOR, 'a[title="Accounts"]').click()
wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='forceActionLink' and @title='New' and @role='button']")))
wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='forceActionLink' and @title='Discover Companies' and @role='button']")))
wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='forceActionLink' and @title='Import' and @role='button']")))
wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='forceActionLink' and @title='Assign Label' and @role='button']")))
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, '.search-button.slds-button.slds-button_neutral.slds-truncate')))
driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Search"]').send_keys("Unique Udeme")
##View An Account
driver.find_element(By.CSS_SELECTOR, "a[title='Unique Udeme']").click()
acctName = driver.find_element(By.PARTIAL_LINK_TEXT, "Unique Udeme")
print("Account Owner Name:", acctName.text)
## Details Sub module

#driver.find_element(By.CSS_SELECTOR, "a[title='Unique Udeme']").click()
driver.find_element(By.CSS_SELECTOR, "a[href=\"/lightning/r/001Ea00000TlJVHIA3/view\"]")
sleep(5)
# Agency lease campaign button
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@name='Account.Agency_Lease_Campaign']")))
agencyLeaseBtn = driver.find_element(By.XPATH, "//button[@name='Account.Agency_Lease_Campaign']")
agencyLeaseBtn.click()
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "img[src='/resource/1727803440000/AgencyLeaseCampaignHeader']")))
driver.find_element(By.XPATH, "//span[@title='Unit Information']")
nextBtn = driver.find_element(By.XPATH, "./html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div[2]/div/article/flowruntime-flow/flowruntime-navigation-bar/footer/div/lightning-button/button")
nextBtn.click()
closeBtn = driver.find_element(By.CSS_SELECTOR, "button[title='Cancel and close'] lightning-primitive-icon[variant='bare']")
closeBtn.click()

#Edit Button
# wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li[data-target-selection-name='sfdc:StandardButton.Account.Edit']")))
# driver.find_element(By.CSS_SELECTOR, "li[data-target-selection-name='sfdc:StandardButton.Account.Edit']").click()
# saveBtn = driver.find_element(By.CSS_SELECTOR, "button[name='SaveEdit']")
#saveBtn.click()

#Account - Contacts submodule
driver.refresh()
driver.find_element(By.CSS_SELECTOR, 'a[href="/lightning/o/Contact/home"]').click()



# # Type a search value
# search_value = "Unique Udeme"
# input_field.send_keys(search_value)
# # Simulate pressing the 'Enter' key
# input_field.send_keys(Keys.RETURN)

