from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

fake = Faker()


def fill_property_details(driver, wait):
    """
    Fill out the property details form using Faker-generated data.
    Assumes driver and wait are already set up and on the correct page.
    """
    phone = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='Phone__c']")))
    phone.send_keys(fake.phone_number())

    email_address = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='Email__c']")))
    email_address.send_keys(fake.email())

    street = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='Address_Street__c']")))
    street.send_keys(fake.street_address())

    city_address = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "input[name='Address_City__c']")))
    city_address.send_keys(fake.city())

    state = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='State__c']")))
    state.send_keys("GA")

    zip = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='Zip__c']")))
    zip.send_keys(fake.postcode())

    county = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@name='County__c']")))
    county.send_keys("Dekalb")

    # Management Account
    mgt_acct = wait.until(ec.visibility_of_element_located((By.XPATH, "//input[@role='combobox']")))
    mgt_acct.click()

    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#combobox-input-2792"))).send_keys("Unique Udeme")
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#combobox-input-5200"))).send_keys("Agent Unique")
    wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#combobox-input-5209"))).send_keys("Unique Agent")

    wait.until(ec.element_to_be_clickable((By.XPATH, "//runtime_platform_actions-actions-ribbon//button"))).click()

    # New Property Inspection (HQS)
    wait.until(ec.element_to_be_clickable((By.XPATH, "//lst-object-home//a"))).click()

    wait.until(ec.visibility_of_element_located((By.XPATH, "//input"))).send_keys("love")
    wait.until(ec.element_to_be_clickable((By.XPATH, "//input[@role='combobox']"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//runtime_platform_actions-actions-ribbon//button"))).click()

    wait.until(ec.element_to_be_clickable((By.XPATH, "//runtime_platform_actions-actions-ribbon//button"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//select"))).click()

    wait.until(ec.element_to_be_clickable((By.XPATH, "//lightning-file-upload//label/span"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//button/span[text()='Done']"))).click()

    wait.until(ec.element_to_be_clickable((By.XPATH, "//flowruntime-navigation-bar//footer//button"))).click()
    wait.until(ec.element_to_be_clickable((By.XPATH, "//flowruntime-navigation-bar//footer//button"))).click()

    # New Property inspection (Soft Walk)
    driver.find_element(By.XPATH, "//one-app-nav-bar-item-root[4]/a").click()

    wait.until(ec.element_to_be_clickable((By.XPATH, "//tbody/tr[1]/th/span/div/lightning-primitive-custom-cell//span"))).click()

    # Do not quit the driver here; let the test or fixture handle teardown.
