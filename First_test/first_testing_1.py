from selenium import webdriver
import time

# Set up the WebDriver (Chrome in this case)
driver = webdriver.Chrome()
driver.maximize_window()

time.sleep(3)

# Define a list of resolutions to test
resolutions = [(1920, 1080), (1366, 768), (1536, 864)]  # Add more as needed

for width, height in resolutions:
    driver.set_window_size(width, height)  # Resize window
    driver.get("https://www.getcalley.com/")
    
    # Insert your tests here (like checking for element visibility or layout)
    print(f"Testing at resolution: {width}x{height}")
    time.sleep(3)
    
   

# Close the browser
driver.quit()
