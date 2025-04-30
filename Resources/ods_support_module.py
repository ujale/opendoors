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

#Clicking on Support Request Module
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/Support_Request__c/home"]'))).click()
#Rental Concession Dropdown
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Select a List View: Support Request']"))).click()
#Pin Recently viewed
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='This list is pinned.' and contains(@class, 'slds-button_icon-border-filled')]"))).click()

#Assert all other buttons
Topbar1 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='New' and @role='button' and contains(@class, 'forceActionLink')]")))
assert Topbar1.text == "New"
Topbar2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Import' and @role='button' and contains(@class, 'forceActionLink')]")))
assert Topbar2.text== "Import"
Topbar3 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Change Owner' and @role='button' and contains(@class, 'forceActionLink')]")))
assert Topbar3.text== "Change Owner"
Topbar4 = wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@title='Assign Label' and @role='button']")))
assert Topbar4.text== "Assign Label"

#Assert available Icons
wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='List View Controls' and contains(@class, 'slds-button_icon-more')]"))).click()
wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Select list display' and contains(@class, 'slds-button_icon-more')]"))).click()
wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Refresh' and @name='refreshButton' and contains(@class, 'slds-button_icon-border-filled')]"))).click()
wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Edit List' and @name='inlineEditButton' and contains(@class, 'slds-button_icon-border-filled')]"))).click()


