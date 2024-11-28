from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Set up WebDriver
driver = webdriver.Chrome()  # Ensure ChromeDriver matches your browser version

try:
    # Navigate to the login page
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    # Maximize the browser window
    driver.maximize_window()
    print("Navigated to OrangeHRM login page.")

    # Wait for the page to load
    time.sleep(3)  # Can be replaced with explicit waits

    # Locate the username and password fields
    username_field = driver.find_element(By.NAME, "username")  # 'username' locator
    password_field = driver.find_element(By.NAME, "password")  # 'password' locator

    # Automatically input username and password
    username = "Admin"  # Replace with your username
    password = "admin123"  # Replace with your password
    # Wrong Password
    # username = "Admin"
    # password = "adminn123"
    # Wrong Username
    # username = "Admin1"
    # password = "admin123"
    # Wrong Username & Password
    # username = "Admin1"
    # password = "adminm123"
    username_field.send_keys(username)
    password_field.send_keys(password)
    print("Entered username and password.")

    # Locate and click the login button
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("Logged in automatically.")

    # Wait for the next page to load
    time.sleep(5)  # Adjust as needed to confirm login success

    # Check login success by URL or page element
    if "dashboard" in driver.current_url.lower():
        print("Login successful. Dashboard loaded.")
    else:
        print("Login failed. Please verify credentials or locator.")

finally:
    # Close the browser
    input("Press Enter to close the browser...")
    driver.quit()

