from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver matches your browser version

try:
    # Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    driver.maximize_window()
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
    if success_message.is_displayed():
        print("Password reset successful. Check your email for instructions.")
    else:
        print("Password reset failed. No success message displayed.")

finally:
    # Close the browser after testing
    input("Press Enter to close the browser...")
    driver.quit()
