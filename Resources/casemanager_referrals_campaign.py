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
refAndCampaign = wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Referrals & Campaigns")))
refAndCampaign.click()
pageTitle = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[@role='main']/div/div[2]/div/div[@class='ui-widget']/div//lst-breadcrumbs//h1[@class='slds-var-p-right_x-small']")))
print("Page's title is :", pageTitle.text)
assert driver.title == "Referrals"

#dropdown
driver.find_element(By.CSS_SELECTOR, "button[title='Select a List View: Referrals']").click()
dropdownHeader = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(1) > div[role='presentation']")))
assert dropdownHeader.text == "LIST VIEWS"
dropdownOption1 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(2) > a[role='option'] > .virtualAutocompleteOptionText")))
assert dropdownOption1.text == "All Referrals-Community"
dropdownOption2 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(3) > a[role='option'] > .virtualAutocompleteOptionText")))
assert dropdownOption2.text == "Closed Cases"
dropdownOption3 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(4) > a[role='option'] > .virtualAutocompleteOptionText")))
assert dropdownOption3.text == "No Report By Provider"
dropdownOption4 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(5) > a[role='option'] > .virtualAutocompleteOptionText")))
assert dropdownOption4.text == "Recently Viewed"
dropdownOption5 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(6) > a[role='option'] > .virtualAutocompleteOptionText")))
assert dropdownOption5.text == "Recently Viewed Referrals"
dropdownOption6 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(7) > a[role='option'] > .virtualAutocompleteOptionText")))
assert dropdownOption6.text == "Referrals - Unassigned"

# Search field
searchField = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[@role='main']//div[@class='ui-widget']/div//force-list-view-manager-search-bar//lightning-input[@class='slds-form-element']/lightning-primitive-input-simple//div[@class='slds-form-element__control slds-grow slds-input-has-icon slds-input-has-icon_left-right']/input[@name='Case-search-input']")))

# View a referral
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "a[title='00011748']")))
wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="/s/case/500Ea00000TXp9VIAT/bob-blob"]')))
element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "a[target='_blank']")))
driver.get("https://community-qa.opendoorsatl.org/s/case/500Ea00000TXp9VIAT/bob-blob")
pageTitle = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[@role='main']/div/div[2]/div/div[@class='ui-widget']//records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_case___0126a000000ykgcqak___compact___view___recordlayout2[@class='forcegenerated-record-layout2']/records-highlights2//slot[@name='entityLabel']/records-entity-label[.='Referral']")))
assert pageTitle.text == "Referral"
## Details Tab
detailsTab = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".uiTabset.uiTabset--base.uiTabset--default > div[role='tablist'] > ul[role='presentation'] > li:nth-of-type(1) > a[role='tab'] > .title")))
print("Current Tab displayed is ",detailsTab.text)
assert detailsTab.text == "DETAILS"
## Related Tab
relatedTab = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(2) > a[role='tab'] > .title")))
print("Current Tab displayed is ",relatedTab.text)
assert relatedTab.text == "RELATED"
##Accept/reject applicant to property(ies)
button1 = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@role='main']/div/div[2]/div/div[@class='ui-widget']//records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_case___0126a000000ykgcqak___compact___view___recordlayout2[@class='forcegenerated-record-layout2']/records-highlights2//runtime_platform_actions-actions-ribbon/ul[@role='presentation']/li[2]/runtime_platform_actions-action-renderer[@title='Accept/Reject Applicant to Property']/runtime_platform_actions-executor-page-reference//lightning-button/button[@class='slds-button slds-button_neutral']")))
print("button name is: ",button1.text)
button2 = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@role='main']/div/div[2]/div/div[@class='ui-widget']//records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_case___0126a000000ykgcqak___compact___view___recordlayout2[@class='forcegenerated-record-layout2']/records-highlights2//runtime_platform_actions-actions-ribbon/ul[@role='presentation']/li[3]/runtime_platform_actions-action-renderer[@title='Accept/Reject Applicant to Multiple Properties']/runtime_platform_actions-executor-page-reference//lightning-button/button[@class='slds-button slds-button_neutral']")))
print("button name is: ",button2.text)
## Follow and Edit buttons
followBtn = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[@role='main']/div/div[2]/div/div[@class='ui-widget']//records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_case___0126a000000ykgcqak___compact___view___recordlayout2[@class='forcegenerated-record-layout2']/records-highlights2/div[1]/div[1]/div[2]/div/span/div/button[@type='button']/span[@title='Follow']")))
print(followBtn)
#assert followBtn == "Follow"
editBtn = wait.until(ec.visibility_of_element_located((By.XPATH, "//div[@role='main']/div/div[2]/div/div[@class='ui-widget']//records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_case___0126a000000ykgcqak___compact___view___recordlayout2[@class='forcegenerated-record-layout2']/records-highlights2//runtime_platform_actions-actions-ribbon/ul[@role='presentation']/li[1]/runtime_platform_actions-action-renderer[@title='Edit']/runtime_platform_actions-executor-delayed-aura-legacy//lightning-button/button[@name='Edit']")))
print(editBtn)
#assert editBtn == "Edit"

sleep(15)

driver.quit()