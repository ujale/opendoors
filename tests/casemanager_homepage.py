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
loginField.send_keys("udeme@opendoorsatl.org.qa.casemanager") 
passwordField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container  .input.inputBox")
passwordField.send_keys("13Gconnect,")
loginBtn = driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label").click()
wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Home")))

# Dashboard

# Wait for the iframe to load and locate it
iframe = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#dashboardFrameWrapper > div > div.dashboardContainer > iframe")))  
# Switch to the iframe
driver.switch_to.frame(iframe)

# Locate the element inside the iframe
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "span[title='New Case Manager Dashboard']")))  
print("HomePage Title is :", element.text)
#refresh button
wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "button[class='slds-button slds-button_neutral refresh disabled']"))) 
# Total Agency Referral submitted Chart
tarsTitle = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div[title='Total Agency Referrals Submitted']")))
print("Chart of :", tarsTitle.text)
tarsReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://community-qa.opendoorsatl.org/00OEa000003lU8zMAE?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
print("The Report link is labelled: ", tarsReportLink.text)
sleep(5)
# Total Agency Housed
tahTitle = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@title='Total Agency Housed']")))
print("Chart of :", tahTitle.text)
tahReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://community-qa.opendoorsatl.org/00OEa000003lUCDMA2?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
print("The Report link is labelled: ", tahReportLink.text)
# Total Individuals Housed
tihTitle = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@title='Total Individuals Housed']")))
print("Chart of :", tihTitle.text)
tihReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://community-qa.opendoorsatl.org/00OEa000003lULtMAM?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
print("The Report link is labelled: ", tihReportLink.text)
# Total Agency Open Referrals 
taorTitle = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@title='Total Agency Open Referrals']")))
print("Chart of :", taorTitle.text)
assert taorTitle.text == "Total Agency Open Referrals"
taorReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://community-qa.opendoorsatl.org/00OEa000003lUNVMA2?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
print("The Report link is labelled: ", taorReportLink.text)
# Break Open Referrals Down By Status
borbsTitle = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@title='Break Open Referrals down by status']")))
print("Chart of :", borbsTitle.text)
assert borbsTitle.text == "Break Open Referrals down by status"
borbsReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://community-qa.opendoorsatl.org/00OEa000003lUTxMAM?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
print("The Report link is labelled: ", borbsReportLink.text)
# Switch back to the main content
driver.switch_to.default_content()
# # Wait for the iframe to load and locate it
# iframe = wait.until(ec.visibility_of_element_located((By.XPATH, '//*[@id="dashboardFrameWrapper"]/div/div[2]/iframe')))  
# # Switch to the iframe
# driver.switch_to.frame(iframe)

# # Open Referrals By Property
# orbpTitle = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@title='Open Referrals To Property']")))
# print("Chart of :", orbpTitle.text)
# assert borbsTitle.text == "Open Referrals To Property"
# orbsReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="href="https://community-qa.opendoorsatl.org/00O3u0000078q26EAA?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
# print("The Report link is labelled: ", orbsReportLink.text)

platformGuide = driver.find_element(By.CSS_SELECTOR, "a[target='_blank']")
print("Link Text is :", platformGuide.text)
sleep(5)

driver.quit()