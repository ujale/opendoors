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
from faker import Faker
from time import sleep

fake =Faker()

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
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[class='slds-global-header__item'] div[class='slds-global-header__logo']"))).click()

#Clicking on Report Tab
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/Report/home"]'))).click()
sleep(10)
Sidebar1 = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='tab' and @title='Recent' and contains(@class, 'slds-nav-vertical__action')]")))
assert Sidebar1.text == "Recent"
Sidebar2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='Created by Me' and contains(@class, 'slds-nav-vertical__action')]")))
assert Sidebar2.text== "Created by Me"
Sidebar3 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='Private Reports' and contains(@class, 'slds-nav-vertical__action')]")))
assert Sidebar3.text  == "Private Reports"
Sidebar4 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='Public Reports' and contains(@class, 'slds-nav-vertical__action')]")))
assert Sidebar4.text == "Public Reports"
Sidebar5 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='All Reports' and contains(@class, 'slds-nav-vertical__action')]")))
assert Sidebar5.text== "All Reports"
Sidebar6 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='All Folders' and contains(@class, 'slds-nav-vertical__action')]")))
assert Sidebar6.text== "All Folders"
Sidebar7 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='Created by Me' and contains(@class, 'slds-nav-vertical__action')]")))
assert Sidebar7.text == "Created by Me"
Sidebar8 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='Shared with Me' and contains(@class, 'slds-nav-vertical__action')]")))
assert Sidebar8.text == "Shared with Me"
Sidebar9 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='All Favorites' and contains(@class, 'slds-nav-vertical__action')]")))
assert Sidebar9.text == "All Favorites"

#NEW REPORT
wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@title='New Report' and @role='button' and contains(@class, 'forceActionLink')]/div[@title='New Report']"))).click()
#Assert all Report
# Wait for the iframe to load and locate it
iframe = wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='brandBand_2']/div/div/div/iframe")))
# Switch to the iframe
driver.switch_to.frame(iframe)

# Locate the element inside the iframe
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="All Report Type Category"]')))
element.click()
print("Link Title is :", element.text)
#wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@class='slds-nav-vertical__action report-section-text' and @aria-label='All Report Type Category' and @aria-selected='true']"))).click()
#To search for Tab Click Log
driver.find_element(By.ID, "modal-search-input").send_keys("Tab")
#Click on Tab Click Log
wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@class='slds-text-link_reset' and @href='#' and @aria-label='']/p[@class='slds-truncate' and @data-tooltip='Tab Click Log']"))).click()
#To click on Start Report
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@class='slds-button slds-button_brand asset-action-button' and @id='start-report-btn' and @type='button']"))).click()
#To Click on Filter
wait.until(ec.element_to_be_clickable((By.XPATH, "//h2[@class='tab-title' and text()='Filters']"))).click()
#To Run
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@class='slds-button slds-button_brand action-bar-action-runReport reportAction report-action-runReport filtersButton' and text()='Run']"))).click()
#To Select a Report
wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@href='/lightning/r/a3vEa000002NbnJIAS/view' and @data-id='a3vEa000002NbnJIAS' and text()='TC-000146']"))).click()
sleep(30)