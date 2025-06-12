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
driver.find_element(By.CSS_SELECTOR, "div[class='slds-global-header__item'] div[class='slds-global-header__logo']")
title = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/div/div/h1/span")))

#REFERRAL TAB
#clicking the tab
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/Case/home"]'))).click()
# Dropdown To see all options
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".slds-dropdown-trigger.slds-dropdown-trigger_click.lst-temp-slds-lineHeight > button"))).click()

#To click on All Referrals
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'span.virtualAutocompleteOptionText'))).click()

#select Test Referral
wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, ".slds-grid.slds-grow"))).click()

#To Edit a Selected Referral
wait.until(ec.element_to_be_clickable((By.XPATH, "/html/body//button[@name='Edit' and contains(@class, 'slds-button')]"))).click()

#To click on Required Status
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@role='combobox' and @aria-label='Status' and contains(@class, 'slds-combobox__input')]"))).click()
wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@type='button' and @name='SaveEdit' and contains(@class, 'slds-button_brand')]"))).click()
sleep(15)