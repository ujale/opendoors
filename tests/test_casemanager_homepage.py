
import pytest
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


@pytest.mark.usefixtures("driver")
def test_casemanager_homepage_dashboard(driver):
    """
    Test the Case Manager homepage dashboard and its key widgets.
    """
    driver.get("https://community-qa.opendoorsatl.org")
    driver.maximize_window()
    action = ActionChains(driver)
    wait = WebDriverWait(driver, 15)

    # Login
    opdLogo = driver.find_element(By.CSS_SELECTOR, "img[alt='Open Doors Community']")
    loginField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_username_container  .input.inputBox")
    loginField.send_keys("udeme@opendoorsatl.org.qa.casemanager")
    passwordField = driver.find_element(By.CSS_SELECTOR, "div#sfdc_password_container  .input.inputBox")
    passwordField.send_keys("13Gconnect#")
    driver.find_element(By.CSS_SELECTOR, ".loginButton.slds-button.slds-button--brand.uiButton.uiButton--none > .bBody.label").click()
    wait.until(ec.visibility_of_element_located((By.LINK_TEXT, "Home")))

    # Dashboard
    iframe = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "#dashboardFrameWrapper > div > div.dashboardContainer > iframe")))
    driver.switch_to.frame(iframe)

    element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "span[title='New Case Manager Dashboard']")))
    print("HomePage Title is :", element.text)

    wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "button[class='slds-button slds-button_neutral refresh disabled']")))

    tarsTitle = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "div[title='Total Agency Referrals Submitted']")))
    print("Chart of :", tarsTitle.text)
    tarsReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://community-qa.opendoorsatl.org/00OEa000003lU8zMAE?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
    print("The Report link is labelled: ", tarsReportLink.text)
    sleep(5)

    tahTitle = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@title='Total Agency Housed']")))
    print("Chart of :", tahTitle.text)
    tahReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://community-qa.opendoorsatl.org/00OEa000003lUCDMA2?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
    print("The Report link is labelled: ", tahReportLink.text)

    tihTitle = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@title='Total Individuals Housed']")))
    print("Chart of :", tihTitle.text)
    tihReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://community-qa.opendoorsatl.org/00OEa000003lULtMAM?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
    print("The Report link is labelled: ", tihReportLink.text)

    taorTitle = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@title='Total Agency Open Referrals']")))
    print("Chart of :", taorTitle.text)
    assert taorTitle.text == "Total Agency Open Referrals"
    taorReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://community-qa.opendoorsatl.org/00OEa000003lUNVMA2?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
    print("The Report link is labelled: ", taorReportLink.text)

    borbsTitle = wait.until(ec.presence_of_element_located((By.XPATH, "//div[@title='Break Open Referrals down by status']")))
    print("Chart of :", borbsTitle.text)
    assert borbsTitle.text == "Break Open Referrals down by status"
    borbsReportLink = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, 'a[href="https://community-qa.opendoorsatl.org/00OEa000003lUTxMAM?drilldown=1&drillcol=Network.Id&drillval=0DB3u000000kWLY&drillop=equals"]')))
    print("The Report link is labelled: ", borbsReportLink.text)

    driver.switch_to.default_content()

    # Optionally, add more assertions or steps as needed
