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
from data_elements.elements import CommunityLoginPage

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get(CommunityLoginPage.communityUrl)
driver.maximize_window()
action = ActionChains(driver)
wait = WebDriverWait(driver, 15)
opdLogo = driver.find_element(By.CSS_SELECTOR, "img[alt='Open Doors Community']")
loginField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_username_container  .input.inputBox")
loginField.send_keys("udeme@opendoorsatl.org.qa.casemanager") 
passwordField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container  .input.inputBox")
passwordField.send_keys("12Gconnect,")
loginBtn = driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label").click()
wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Home")))
profileIcon = driver.find_element(By.CSS_SELECTOR, "img[class='profile-icon']")
profileIcon.click()
logoutLink = driver.find_element(By.CSS_SELECTOR, "a[title='Logout']")
logoutLink.click()

driver.quit()