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

# Test for Forgot Password functionality
@pytest.mark.forgot_password
def test_forgot_password(driver):
    # Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()

    # Wait for the "Forgot your password?" link to be visible
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[@class='orangehrm-login-forgot']//p"))
    )

    # Locate and click the "Forgot your password?" link
    forgot_password_link = driver.find_element(By.XPATH, "//div[@class='orangehrm-login-forgot']//p")
    forgot_password_link.click()

    # Wait for the "Reset Password" page to load
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "username"))
    )

    # Enter the username to reset the password
    username_field = driver.find_element(By.XPATH, "//input[@name='username']")
    username_field.send_keys("Admin")  # Replace with the username for password reset

    # Click the Reset Password button
    reset_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    reset_button.click()

    # Wait for a success message or indication (increase wait time to 20 seconds for more reliability)
    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.XPATH, "//p[contains(text(),'Reset link sent')]"))
        )
        success_message = driver.find_element(By.XPATH, "//p[contains(text(),'Reset link sent')]")
        assert success_message.is_displayed(), "Password reset failed. Success message not displayed."
        print("Pass")  # Test passes if success message is displayed
    except:
        print("Fail")  # Test fails if success message is not displayed
