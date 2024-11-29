import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


# Pytest fixture to handle WebDriver setup and teardown
@pytest.fixture
def driver():
    # Setup WebDriver using Service
    service = Service('C:/Users/HP/PycharmProjects/EMS/drivers/chromedriver-win64/chromedriver.exe')
    driver = webdriver.Chrome(service=service)
    yield driver  # Yielding the driver to the test
    driver.quit()  # Teardown: Close the browser after test completion


def test_login(driver):
    print("Starting the OrangeHRM login test.")

    # Step 1: Navigate to the OrangeHRM demo page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
    print("Opened OrangeHRM login page.")

    # Step 2: Verify the page title
    assert "OrangeHRM" in driver.title, "Incorrect page title!"
    print("Page title verified.")

    try:
        # Step 3: Locate username and password fields
        username_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "username"))
        )
        password_field = driver.find_element(By.NAME, "password")
        print("Located username and password fields.")
    except NoSuchElementException:
        raise AssertionError("Test failed: Username and password fields not found.")

    # Step 4: Enter login credentials
    username_field.send_keys("Admin")
    password_field.send_keys("admin123")
    print("Entered login credentials.")

    # Step 5: Click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("Clicked login button.")

    try:
        # Step 6: Wait for dashboard to load or error message
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//span[text()='Dashboard']"))
        )
        print("Login successful. Dashboard loaded.")
    except NoSuchElementException:
        # Step 7: Check for error message in case of failed login
        error_message = driver.find_element(By.XPATH, "//p[contains(@class, 'oxd-alert-content-text')]")
        assert "Invalid credentials" in error_message.text, "Unexpected error message!"
        raise AssertionError("Test failed: Invalid credentials provided.")

    # Step 8: Navigate to "Admin" module
    admin_module = driver.find_element(By.XPATH, "//span[text()='Admin']")
    admin_module.click()
    print("Navigated to Admin module.")
    time.sleep(5)  # Adding delay to observe the module navigation

    # Step 9: Verify navigation to the Admin module
    assert "admin/viewSystemUsers" in driver.current_url, "Failed to navigate to Admin module!"
    print("Admin module verified.")

    # Step 10: Navigate to "PIM" module
    pim_module = driver.find_element(By.XPATH, "//span[text()='PIM']")
    pim_module.click()
    print("Navigated to PIM module.")
    time.sleep(5)  # Adding delay to observe the PIM module navigation

    # Step 11: Verify navigation to the PIM module
    assert "pim/viewEmployeeList" in driver.current_url, "Failed to navigate to PIM module!"
    print("PIM module verified.")

    # Step 12: Navigate to "Leave" module
    pim_module = driver.find_element(By.XPATH, "//span[text()='Leave']")
    pim_module.click()
    print("Navigated to Leave module.")
    time.sleep(5)  # Adding delay to observe the Leave module navigation

    # Step 13: Verify navigation to the PIM module
    assert "leave/viewLeaveList" in driver.current_url, "Failed to navigate to Leave module!"
    print("Leave module verified.")

    # Step 14: Navigate to "Time" module
    pim_module = driver.find_element(By.XPATH, "//span[text()='Time']")
    pim_module.click()
    print("Navigated to Time module.")
    time.sleep(5)  # Adding delay to observe the Leave module navigation




    # Step 12: Example navigation to Education module (optional, replace with relevant paths)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewEducation")
    print("Navigated to Education module.")
    time.sleep(5)

    # Step 13: Assert successful navigation
    assert "viewEducation" in driver.current_url, "Failed to navigate to Education module!"
    print("Education module test passed.")
