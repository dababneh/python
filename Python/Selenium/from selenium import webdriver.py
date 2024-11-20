from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

# Path to ChromeDriver
path_to_chrome = "/Users/jamildababneh/Desktop/Dev/Python/Selenium/chromedriver"

# Set Chrome options
options = Options()
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.geolocation": 2  # Block location prompts
})

# Initialize WebDriver with service and options
service = Service(executable_path=path_to_chrome)
driver = webdriver.Chrome(service=service, options=options)

try:
    # Open Google
    driver.get("https://google.com")

    # Wait for the search input box to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))
    )

    # Locate the search input box
    input_element = driver.find_element(By.CLASS_NAME, "gLFyf")
    input_element.clear()

    # Input the search query and press Enter
    input_element.send_keys("Jamil Dababneh" + Keys.ENTER)
    time.sleep(5)

    # Wait for the search results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a"))
    )

    # Locate all links in the search results
    links = driver.find_elements(By.CSS_SELECTOR, "a")

      # Print the text and href of each link
    for idx, link in enumerate(links[:10]):  # Limit to the first 10 links
        print(f"Link {idx + 1}: {link.text} -> {link.get_attribute('href')}")
   
    # Wait to observe the result of the click
    time.sleep(5)

finally:
    # Quit the browser
    driver.quit()
