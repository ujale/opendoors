

import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


@pytest.mark.usefixtures("driver")
def test_casemanager_properties(driver):
    """
    Test the Case Manager properties page and its key widgets.
    """
    driver.get("https://community-qa.opendoorsatl.org")
    driver.maximize_window()
    action = ActionChains(driver)
    wait = WebDriverWait(driver, 15)

    opdLogo = driver.find_element(By.CSS_SELECTOR, "img[alt='Open Doors Community']")
    loginField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_username_container  .input.inputBox")
    loginField.send_keys("udeme@opendoorsatl.org.qa.casemanager")
    passwordField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container  .input.inputBox")
    passwordField.send_keys("13Gconnect#")
    driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label").click()
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Properties"))).click()

    pageTitle = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[@role='main']/div/div[2]/div/div[@class='ui-widget']/div//lst-breadcrumbs//h1[@class='slds-var-p-right_x-small']")))
    print("Page's title is :", pageTitle.text)
    assert driver.title == "Properties"

    # dropdown
    driver.find_element(By.CSS_SELECTOR, "button[title='Select a List View: Properties']").click()
    dropdownHeader = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(1) > div[role='presentation']")))
    assert dropdownHeader.text == "LIST VIEWS"
    dropdownOption1 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(2) > a[role='option'] > .virtualAutocompleteOptionText")))
    assert dropdownOption1.text == "All Properties"
    dropdownOption2 = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(3) > a[role='option'] > .virtualAutocompleteOptionText")))
    assert dropdownOption2.text == "Recently Viewed"

    # View a referral
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "a[title='You Properties']")))
    driver.get("https://community-qa.opendoorsatl.org/s/property/a2IEa000000diafMAA/you-properties")
    pageTitle = wait.until(ec.visibility_of_element_located((By.XPATH, "//records-entity-label[@slot='entityLabel']")))
    assert pageTitle.text == "Property"

    # Details Tab
    detailsTab = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "a[data-tab-name='Details'] span[class='title']")))
    print("Current Tab displayed is ", detailsTab.text)
    assert detailsTab.text == "DETAILS"
    propertyInfo = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[@role='main']/div/div[2]/div/div[2]//div[@class='recordHomePrimaryContent']/div/section[1]//records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker//records-lwc-detail-panel/records-base-record-form//records-lwc-record-layout/forcegenerated-detailpanel_property__c___012000000000000aaa___full___view___recordlayout2[@class='forcegenerated-record-layout2']/records-record-layout-block/slot/records-record-layout-section[1]//h3/button/span[@class='test-id__section-header-title']")))
    assert propertyInfo.text == "Property Information"
    propertyName = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[@role='main']/div/div[2]/div/div[2]/div[@class='forceCommunityRecordHomeTabs']/div[@class='recordHomePrimaryContent']/div/section[1]//records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker//records-lwc-detail-panel/records-base-record-form//records-lwc-record-layout/forcegenerated-detailpanel_property__c___012000000000000aaa___full___view___recordlayout2[@class='forcegenerated-record-layout2']/records-record-layout-block/slot/records-record-layout-section[1]/div/div//records-record-layout-row[@class='slds-form__row']/slot/records-record-layout-item[1]//slot[@name='outputField']/lightning-formatted-text[.='You Properties']")))
    print("The property name is: ", propertyName.text)
    description = wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[3]/div[@role='main']/div/div[2]/div/div[2]//div[@class='recordHomePrimaryContent']/div/section[1]//records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker//records-lwc-detail-panel/records-base-record-form//records-lwc-record-layout/forcegenerated-detailpanel_property__c___012000000000000aaa___full___view___recordlayout2[@class='forcegenerated-record-layout2']/records-record-layout-block/slot/records-record-layout-section[2]//button/span[@class='test-id__section-header-title']")))
    assert description.text == "Description"

    # Related Tab
    relatedTab = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "li:nth-of-type(2) > a[role='tab'] > .title")))
    print("Current Tab displayed is ", relatedTab.text)
    assert relatedTab.text == "RELATED"

    # Optionally, add more assertions or steps as needed
    sleep(15)