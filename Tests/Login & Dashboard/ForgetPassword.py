import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

# Fixture to set up and tear down WebDriver
@pytest.fixture(scope="module")
def driver():
    # Set up the WebDriver using the Service class
    service = Service('../driver/chromedriver-win64/chromedriver.exe')  # Update path to match your chromedriver
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    yield driver
    driver.quit()

# Test case for "Forgot your password?" functionality
@pytest.mark.forgot_password
def test_forgot_password(driver):
    # Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    print("Navigated to OrangeHRM login page.")

    # Wait for the "Forgot your password?" link to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='orangehrm-login-forgot']//p"))
    )

    # Locate and click the "Forgot your password?" link
    forgot_password_link = driver.find_element(By.XPATH, "//div[@class='orangehrm-login-forgot']//p")
    forgot_password_link.click()
    print("Clicked on the 'Forgot your password?' link.")

    # Wait for the "Reset Password" page to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    # Enter the username to reset the password
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys("Admin")  # Replace with the username for password reset
    print("Entered the username for password reset.")

    # Click the Reset Password button
    reset_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    reset_button.click()
    print("Clicked 'Reset Password' button.")

    # Wait for a success message or indication
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Reset link sent')]"))
    )

    # Check for success message
    success_message = driver.find_element(By.XPATH, "//p[contains(text(),'Reset link sent')]")
    assert success_message.is_displayed(), "Password reset failed. No success message displayed."
    print("Password reset successful. Check your email for instructions.")
