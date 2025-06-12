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

#Property
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/s/property/Property__c/Default"]'))).click()
#Property Dropdown
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[contains(@title, 'Select a List View') and @role='button']"))).click()
#property view
wait.until(ec.element_to_be_clickable((By.XPATH, "//li[@role='presentation' and contains(@class, 'forceVirtualAutocompleteMenuOption') and .//span[text()='All Properties']]"))).click()
#Pin All properties
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Pin this list view.']"))).click()

#Assert all other Icons
#Search Field
wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@type='search' and contains(@class, 'slds-input') and @placeholder='Search this list...']")))
#List View Control
wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='List View Controls' and contains(@class, 'slds-button_icon-more')]")))
#List Display dropdown
wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Select list display' and contains(@class, 'slds-button_icon-more')]")))
#Refresh
wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Refresh' and @name='refreshButton']")))
#Edit
wait.until(ec.visibility_of_element_located((By.XPATH, "//button[@title='Edit List' and @name='inlineEditButton']")))
sleep(10)


