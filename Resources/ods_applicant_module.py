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

#Clicking on Applicant Module
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/Applicant__c/home"]'))).click()
#people Dropdown
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Select a List View: Applicants']"))).click()
#Pin Recently viewed
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='This list is pinned.']"))).click()

#Assert all other buttons
Topbar1 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='New' and contains(@class, 'forceActionLink')]")))
assert Topbar1.text == "New"
Topbar2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Import' and @class='forceActionLink' and @role='button']")))
assert Topbar2.text== "Import"
#Topbar3 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Change Owner' and contains(@class, 'forceActionLink')]")))
#assert Topbar3.text== "Import"
Topbar4 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Assign Label' and @class='forceActionLink' and @role='button']")))
assert Topbar4.text== "Assign Label"

#Assert Available Icons
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='List View Controls' and contains(@class, 'slds-button_icon')]"))).click()
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Select list display' and contains(@class, 'slds-button_icon')]"))).click()
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Refresh' and contains(@class, 'slds-button_icon')]"))).click()
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Edit List' and contains(@class, 'slds-button') and contains(@class, 'slds-button_icon') and contains(@class, 'slds-button_icon-border-filled')]"))).click()

sleep(20)
