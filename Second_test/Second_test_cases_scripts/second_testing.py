from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize WebDriver
driver = webdriver.Chrome()

# Open the website login page
driver.get("https://demo.dealsdray.com/")
driver.maximize_window()

# Wait for the page to load
wait = WebDriverWait(driver, 10)

# Find the username and password fields using 'By.NAME'
username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
password_field = driver.find_element(By.NAME, "password")

# Enter login credentials
username_field.send_keys("prexo.mis@dealsdray.com")
password_field.send_keys("prexo.mis@dealsdray.com")

# Find the login button by XPATH and click it
login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for the first button to load and click it
button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'MuiPaper-root MuiPaper-elevation MuiPaper-rounded MuiPaper-elevation3 MuiCard-root css-1cl20sq')]")))
button.click()

# Try to locate button2 and interact with it
try:
    button2 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root  css-vwfva9')]")))
    print("Button2 found and is clickable")
    button2.click()

    # Wait for file input to be available and upload the file
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    file_path = "C:/Users/Tech/Downloads/demo-data.xlsx"  # Replace with the path to your file

    # Upload the file
    file_input.send_keys(file_path)
    print("File uploaded successfully")

    button3 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root  css-6aomwy')]")))
    print("Button3 found and is clickable")
    button3.click()
    
    button4 = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(@class, 'MuiButton-root MuiButton-contained MuiButton-containedPrimary MuiButton-sizeMedium MuiButton-containedSizeMedium MuiButtonBase-root  css-6aomwy')]")))
    print("Button4 found and is clickable")
    button4.click()


except Exception as e:
    print(f"Error occurred: {e}")

# Wait for a few seconds for the next actions
time.sleep(10)

# Close the browser after your operations
driver.quit()
