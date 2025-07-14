from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait
from time import sleep

def test_ods_reports_module(driver):
    """
    Test the Reports module for correct login, navigation, sidebar, and report creation.
    """
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support import expected_conditions as ec
    from selenium.webdriver.support.wait import WebDriverWait
    from time import sleep

    driver.get("https://opendoors--qa.sandbox.my.salesforce.com")
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    # Step 1: Login
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#logo")))
    driver.find_element(By.CSS_SELECTOR, "#username").send_keys("udeme@opendoorsatl.org.qa")
    driver.find_element(By.CSS_SELECTOR, "#password").send_keys("1Gconnect!")
    driver.find_element(By.CSS_SELECTOR, "#Login").click()

    # Step 2: Home Page
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[class='slds-global-header__item'] div[class='slds-global-header__logo']"))).click()

    # Step 3: Report Tab
    wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'a[href="/lightning/o/Report/home"]'))).click()
    sleep(2)
    # Sidebar assertions
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "/html/body//a[@role='tab' and @title='Recent' and contains(@class, 'slds-nav-vertical__action')]"))).text == "Recent"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='Created by Me' and contains(@class, 'slds-nav-vertical__action')]"))).text == "Created by Me"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='Private Reports' and contains(@class, 'slds-nav-vertical__action')]"))).text == "Private Reports"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='Public Reports' and contains(@class, 'slds-nav-vertical__action')]"))).text == "Public Reports"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='All Reports' and contains(@class, 'slds-nav-vertical__action')]"))).text == "All Reports"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='All Folders' and contains(@class, 'slds-nav-vertical__action')]"))).text == "All Folders"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='Created by Me' and contains(@class, 'slds-nav-vertical__action')]"))).text == "Created by Me"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='Shared with Me' and contains(@class, 'slds-nav-vertical__action')]"))).text == "Shared with Me"
    assert wait.until(ec.visibility_of_element_located((By.XPATH, "//a[@role='tab' and @title='All Favorites' and contains(@class, 'slds-nav-vertical__action')]"))).text == "All Favorites"

    # Step 4: New Report
    wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@title='New Report' and @role='button' and contains(@class, 'forceActionLink')]/div[@title='New Report']"))).click()
    # Wait for the iframe to load and locate it
    iframe = wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='brandBand_2']/div/div/div/iframe")))
    driver.switch_to.frame(iframe)

    # Locate the element inside the iframe
    element = wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'a[aria-label="All Report Type Category"]')))
    element.click()
    print("Link Title is :", element.text)
    driver.find_element(By.ID, "modal-search-input").send_keys("Tab")
    wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@class='slds-text-link_reset' and @href='#' and @aria-label='']/p[@class='slds-truncate' and @data-tooltip='Tab Click Log']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@class='slds-button slds-button_brand asset-action-button' and @id='start-report-btn' and @type='button']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//h2[@class='tab-title' and text()='Filters']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button[@class='slds-button slds-button_brand action-bar-action-runReport reportAction report-action-runReport filtersButton' and text()='Run']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//a[@href='/lightning/r/a3vEa000002NbnJIAS/view' and @data-id='a3vEa000002NbnJIAS' and text()='TC-000146']"))).click()
    sleep(5)