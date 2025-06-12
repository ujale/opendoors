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
import allure
import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://community-qa.opendoorsatl.org")
driver.maximize_window()
action = ActionChains(driver)
wait = WebDriverWait(driver, 15)
opdLogo = driver.find_element(By.CSS_SELECTOR, "img[alt='Open Doors Community']")
loginField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_username_container  .input.inputBox")
loginField.send_keys("udeme@opendoorsatl.org.qa.casemanager")
passwordField = driver.find_element(By.CSS_SELECTOR, "")
passwordField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container  .input.inputBox")
passwordField.send_keys("13Gconnect,")
loginBtn = driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label").click()
wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Home")))
caorLink = driver.find_element(By.LINK_TEXT, "Create Applicant Only Referral")
print(caorLink.text)
caorLink.click()
wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[@role='main']/div/div/div[@class='ui-widget']/div/div[3]/div/div/div[1]/c-referral-creator//article[@class='slds-card']//header")))
raoHeader = driver.find_element(By.XPATH, "/html/body/div[3]/div[@role='main']/div/div/div[@class='ui-widget']/div/div[3]/div/div/div[1]/c-referral-creator//article[@class='slds-card']//header")
print("Page Header is: ", raoHeader.text)
applicantInputBox = driver.find_element(By.XPATH, "/html/body/div[3]/div[@role='main']/div/div/div[@class='ui-widget']/div/div[3]/div/div/div[1]/c-referral-creator//article[@class='slds-card']//c-custom-lookup-comp//div[@role='combobox']/div[@role='none']/input[@role='textbox']")
applicantInputBox.click()
applicantInputBox.send_keys(Keys.ARROW_DOWN)
applicantInputBox.send_keys(Keys.RETURN)
#driver.find_element(By.CSS_SELECTOR, ".fix_button-group-flexbox").click()
sleep(5)
print("Searched Applicant is: ", applicantInputBox.text)
#wait.until(ec.visibility_of_element_located((By.CLASS_NAME, ".newapplicant")))
#newApplicants = driver.find_element(By.CSS_SELECTOR, "div:nth-of-type(2) > .slds-media__body")
#newApplicants.click()

#applicantInputBox.send_keys("Dylan W")
driver.quit()