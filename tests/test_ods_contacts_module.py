
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time

@pytest.mark.usefixtures("driver")
def test_ods_contacts_module(driver):
    """
    Test the Contacts module in the ODS Salesforce app.
    """
    driver.get("https://opendoors--qa.sandbox.my.salesforce.com")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    # Login Page
    driver.find_element(By.CSS_SELECTOR, "#logo")
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("udeme@opendoorsatl.org.qa")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1Gconnect!")
    driver.find_element(By.CSS_SELECTOR, "#Login").click()

    # Home Page
    driver.find_element(By.CSS_SELECTOR, "div[class='slds-global-header__item'] div[class='slds-global-header__logo']")
    title = driver.find_element(By.XPATH, "//span[@title='Open Doors']")
    print("Page title:", title.text)

    # SF Tabs
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Home']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Accounts']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Contacts']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Properties']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Referrals']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Reports']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Dashboards']")
    driver.find_element(By.XPATH, "//a[@class='slds-button slds-button_reset slds-context-bar__label-action']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='People']")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Unit Availability']")
    driver.find_elements(By.XPATH, "//span[@class='slds-truncate'][normalize-space()='Applicants']")
    driver.find_element(By.XPATH, "//span[@class='slds-p-right_small']")
    driver.find_element(By.XPATH, "//lightning-icon[@class='slds-icon-utility-down slds-icon_container']//lightning-primitive-icon[@exportparts='icon']//*[name()='svg']").click()
    driver.find_element(By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Rental Concessions')]")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'DocuSign Envelope Recipients')]")
    driver.find_element(By.XPATH, "//span[@class='slds-truncate']//span[contains(text(),'Property Inspection')]")

    # Home Page Dashboard
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "span[title='Today’s Tasks']")))
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "span[title=\"Today's Events\"]")))

    # Contacts Tab
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/Contact/home"]')))
    driver.find_element(By.CSS_SELECTOR, 'a[href="/lightning/o/Contact/home"]').click()
    pageTitle = wait.until(ec.element_to_be_clickable((By.LINK_TEXT, "Contacts")))
    print("Title on page is: ", pageTitle.text)

    # New Contact
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "li:nth-of-type(1) > a[role='button']")))
    driver.find_element(By.CSS_SELECTOR, "li:nth-of-type(1) > a[role='button']").click()
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, ".inlineTitle.slds-p-top--large.slds-p-horizontal--medium.slds-p-bottom--medium.slds-text-heading--medium")))
    pageTitle = driver.find_element(By.CSS_SELECTOR, ".inlineTitle.slds-p-top--large.slds-p-horizontal--medium.slds-p-bottom--medium.slds-text-heading--medium")
    print("Title on page is: ", pageTitle.text)
    driver.find_element(By.CSS_SELECTOR, ".changeRecordTypeLeftColumn.form-element__legend.slds-form-element__label")
    driver.find_element(By.CSS_SELECTOR, "label[for='0126A000000YkFAQA0'] span[class='slds-radio--faux']").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='0126A000000xPrGQAU'] span[class='slds-radio--faux']").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='0126A000000YkFCQA0'] span[class='slds-radio--faux']").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='0126A000000YkFDQA0'] span[class='slds-radio--faux']").click()
    driver.find_element(By.CSS_SELECTOR, "label[for='0126A000000YkFBQA0'] span[class='slds-radio--faux']").click()

    # Next button
    driver.find_element(By.CSS_SELECTOR, "button[class='slds-button slds-button_neutral slds-button slds-button_brand uiButton'] span[class=' label bBody']").click()
    wait.until(ec.visibility_of_element_located((By.XPATH, "//body/div[4]/div[@class='DESKTOP uiContainerManager']/div/div[@role='dialog']//div[@class='modal-body scrollable slds-modal__content slds-p-around_medium']//records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker//records-lwc-detail-panel//h2[.='New Contact: Donor']")))
    pageTitle = driver.find_element(By.XPATH, "//body/div[4]/div[@class='DESKTOP uiContainerManager']/div/div[@role='dialog']//div[@class='modal-body scrollable slds-modal__content slds-p-around_medium']//records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker//records-lwc-detail-panel//h2[.='New Contact: Donor']")
    print("Title on page is: ", pageTitle.text)
    driver.find_element(By.XPATH, "//body[@class='desktop']/div[4]/div[@class='DESKTOP uiContainerManager']/div/div[@role='dialog']//div[@class='modal-body scrollable slds-modal__content slds-p-around_medium']//records-modal-lwc-detail-panel-wrapper/records-record-layout-event-broker//records-lwc-detail-panel/records-base-record-form//records-lwc-record-layout[@class='record-layout-container-bottom-padding']/forcegenerated-detailpanel_contact___0126a000000ykfbqa0___full___create___recordlayout2[@class='forcegenerated-record-layout2']/records-record-layout-block/slot/records-record-layout-section[1]/div/div/dl/slot/records-record-layout-row[1]/slot/records-record-layout-item[1]//slot[@name='inputField']/records-record-layout-input-name/lightning-input-name//lightning-picklist/lightning-combobox[@class='slds-form-element']//lightning-base-combobox[@class='slds-combobox_container']//div[@role='none']/button[@role='combobox']").click()

    # close
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@title='Cancel and close']//lightning-primitive-icon[@variant='bare']")))
    driver.find_element(By.XPATH, "//button[@title='Cancel and close']//lightning-primitive-icon[@variant='bare']").click()

    # Intelligent view button
    driver.find_element(By.CSS_SELECTOR, "a[role='button'] > div[title='Intelligence View']").click()

    # List View
    wait.until(ec.element_to_be_clickable((By.XPATH, "//body/div[4]/div[@class='viewport']/section/div[1]/div[2]/div[@role='main']/div[@class='contentArea fullheight']/div/div/div//div[@class='slds-page-header__controls']/div/div[@role='group']/runtime_pipeline_inspector-actions-button-group/lightning-button-group[@role='group']//lightning-button[@class='slds-button_last']/button[@name='pipelineInspectionToListView']"))).click()
    time.sleep(5)

    # View a contact
    wait.until(ec.element_to_be_clickable((By.XPATH, "//div[@id='sfdc-splitview-content']/div/div/div/div[@class='oneConsoleObjectHome']/div/div[2]/div/div[1]/div[2]/div[@class='listViewContent slds-table--header-fixed_container slds-table_header-fixed_container']/div[1]//table[@role='grid']/tbody/tr[1]/th//a[@title='Unique Agent']"))).click()
    contactName = wait.until(ec.element_to_be_clickable((By.XPATH, "//lightning-formatted-name[@slot='primaryField']")))
    print("Account Owner Name:", contactName.text)

    # Details Tab
    detailsTab = wait.until(ec.visibility_of_element_located((By.XPATH, "/html//a[@id='detailTab__item']")))
    print("Current Tab displayed is ", detailsTab.text)
    assert detailsTab.text == "Details"
    contactDetails = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Contact Details']")))
    assert contactDetails.text == "Contact Details"
    contactInformation = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Contact Information']")))
    assert contactInformation.text == "Contact Information"
    addressInformation = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Address Information']")))
    assert addressInformation.text == "Address Information"
    householdAddress = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Household Address']")))
    assert householdAddress.text == "Household Address"
    donationInformation = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Donation Information']")))
    assert donationInformation.text == "Donation Information"
    donationTotals = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Donation Totals']")))
    assert donationTotals.text == "Donation Totals"
    softCreditTotal = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(@class,'test-id__section-header-title')][normalize-space()='Soft Credit Total']")))
    assert softCreditTotal.text == "Soft Credit Total"
    householdDonationInfo = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Household Donation Info']")))
    assert householdDonationInfo.text == "Household Donation Info"
    membershipInformation = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Membership Information']")))
    assert membershipInformation.text == "Membership Information"
    volunteerInformation = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Volunteer Information']")))
    assert volunteerInformation.text == "Volunteer Information"
    systemInformation = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[normalize-space()='System Information']")))
    assert systemInformation.text == "System Information"

    # Related Tab
    relatedTab = wait.until(ec.visibility_of_element_located((By.XPATH, "/html//a[@id='relatedListsTab__item']")))
    print("Current Tab displayed is ", relatedTab.text)
    assert relatedTab.text == "Related"
    relatedTab.click()
    relationships = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@title='Relationships']")))
    assert relationships.text == "Relationships"
    organizationAffiliations = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[contains(@title,'Organization Affiliations')]")))
    assert organizationAffiliations.text == "Organization Affiliations"
    engagementPlans = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@title='Engagement Plans']")))
    assert engagementPlans.text == "Engagement Plans"
    opportunities = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@title='Opportunities']")))
    assert opportunities.text == "Opportunities"
    recurringDonation = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@title='Recurring Donations']")))
    assert recurringDonation.text == "Recurring Donations"
    driver.execute_script("window.scrollBy(0, 1000);")
    campaignHistory = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "span[title='Campaign History']")))
    assert campaignHistory.text == "Campaign History"
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    volunteerHours = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "span[title='Volunteer Hours']")))
    assert volunteerHours.text == "Volunteer Hours"
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    notesAttachments = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@title='Notes & Attachments']")))
    assert notesAttachments.text == "Notes & Attachments"
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    referrals = wait.until(ec.visibility_of_element_located((By.XPATH, "//span[@title='Referrals']")))
    assert referrals.text == "Referrals"