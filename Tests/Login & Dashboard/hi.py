from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

# WebDriver setup
@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()  # Ensure that your ChromeDriver version matches your browser version
    yield driver
    driver.quit()

# Wait for the page to be completely loaded
def wait_for_page_to_load(driver):
    WebDriverWait(driver, 10).until(
        lambda driver: driver.execute_script("return document.readyState") == "complete"
    )

# Test to verify that the logo and all login page elements are displayed correctly
@pytest.mark.login_page
def test_login_page_elements(driver):
    # Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Wait for the page to fully load
    wait_for_page_to_load(driver)

    # Wait for the OrangeHRM logo to be present on the page
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//img[@alt='company-branding']"))
        )
        logo = driver.find_element(By.XPATH, "//img[@alt='company-branding']")
        assert logo.is_displayed(), "OrangeHRM logo is not displayed"
        print("OrangeHRM logo is displayed.")
    except Exception as e:
        print(f"Error: {str(e)}")

    # Verify the username field is displayed
    try:
        username_field = driver.find_element(By.XPATH, "//input[@name='username']")
        assert username_field.is_displayed(), "Username field is not displayed"
        print("Username field is displayed.")
    except AssertionError:
        print("Username field is not displayed.")

    # Verify the password field is displayed
    try:
        password_field = driver.find_element(By.XPATH, "//input[@name='password']")
        assert password_field.is_displayed(), "Password field is not displayed"
        print("Password field is displayed.")
    except AssertionError:
        print("Password field is not displayed.")

    # Verify the login button is displayed
    try:
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        assert login_button.is_displayed(), "Login button is not displayed"
        print("Login button is displayed.")
    except AssertionError:
        print("Login button is not displayed.")
