import os
import pytest
import logging
#Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Chrome
import chromedriver_binary
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
# Django
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

import core.web_core.web_core
import core.web_core.web_core.settings
##############################################################################################
"""
    Testing with pytest
"""
##############################################################################################
# Import all test files
import core
import core.mydjangotestunity.system_file as system_file
##############################################################################################
os.environ['DJANGO_SETTINGS_MODULE'] = 'core.web_core.web_core.settings'
# Import all test in integration_tests files:
import run_test_integration_tests as integration_tests
# Import all test in unit_tests files:
import run_test_unit_tests_classes as unit_tests_classes
# Import all test in unit_tests files:
import run_test_unit_tests_functions as unit_tests_functions
##############################################################################################

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Set the path to the Chrome binary
ChromeVar = system_file.get_chrome_variables()

# Specify Chrome application location explicitly
CHROME_APPLICATION_PATH = ChromeVar[0]  # Change this path accordingly
CHROME_APPLICATION_DATA = "--user-data-dir={}".format(ChromeVar[1])  # Change this path accordingly

@pytest.fixture(scope="session")
def get_headless_chrome_driver(live_server):

    """Initialize and return a headless Chrome WebDriver instance with logging."""
    options = ChromeOptions()
    # Set explicit Chrome application path
    if os.path.exists(CHROME_APPLICATION_PATH):
        options.binary_location = CHROME_APPLICATION_PATH
    else:
        logging.error(f"Chrome binary not found at: {CHROME_APPLICATION_PATH}")
        raise FileNotFoundError(f"Chrome binary not found at: {CHROME_APPLICATION_PATH}")
    options.add_argument("--headless")  # Run browser in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration (useful for headless mode)
    options.add_argument("--window-size=1920,1080")  # Set window size
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument("--disable-extensions")    # Disable extensions
    options.add_argument("--disable-infobars")  # Disable infobars
    options.add_argument("--start-maximized")  # Start maximized
    # Specify a unique user data directory
    options.add_argument(CHROME_APPLICATION_DATA)
    options.add_argument("--remote-debugging-port=9222")  # Fix DevToolsActivePort file doesn't exist error
    service = ChromeService(executable_path=chromedriver_binary.chromedriver_filename)
    logging.info("Initializing headless Chrome WebDriver...")
    driver = webdriver.Chrome(service=service, options=options)
    try:
        yield driver
    finally:
        #logging.info("Closing WebDriver...")
        driver.quit()

@pytest.fixture(scope="session")
def live_server_url(live_server):
    """Provides the Django live server URL for testing."""
    return live_server.url


def test_chrome_search(get_headless_chrome_driver):
    
    driver = get_headless_chrome_driver
    driver.get("https://www.google.com")
    logging.info("Assert that the title of the page is 'Google'")
    assert "Google" in driver.title


if __name__ == "__main__":
    # Run all tests available
    print("Running tests...")
    pytest.main(["-v", __file__])
   