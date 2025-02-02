import os
import pytest
import logging
#Selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
# Django
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
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
FirefoxVar = system_file.get_firefox_variables()

# Specify Chrome application location explicitly
GECKODRIVER_PATH = FirefoxVar[0]  # Change this path accordingly
FIREFOX_APPLICATION_PATH = FirefoxVar[1]  # Change this path accordingly
FIREFOX_APPLICATION_DATA = "--user-data-dir={}".format(FirefoxVar[2])  # Change this path accordingly

@pytest.fixture(scope="session")
def get_headless_firefox_driver(live_server):

    """Initialize and return a headless Firefox WebDriver instance with logging."""
    options = FirefoxOptions()
    
    # Set explicit Firefox binary location
    if os.path.exists(FIREFOX_APPLICATION_PATH):
        options.binary_location = FIREFOX_APPLICATION_PATH
    else:
        logging.error(f"Firefox binary not found at: {FIREFOX_APPLICATION_PATH}")
        raise FileNotFoundError(f"Firefox binary not found at: {FIREFOX_APPLICATION_PATH}")
    
    # Add headless options
    options.add_argument("--headless")  # Run browser in headless mode
    options.add_argument("--disable-gpu")  # Disable GPU acceleration
    options.add_argument("--window-size=1920,1080")  # Set window size
    options.add_argument("--no-sandbox")  # Bypass OS security model
    options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
    options.add_argument("--disable-extensions")    # Disable extensions
    options.add_argument("--disable-infobars")  # Disable infobars
    options.add_argument("--start-maximized")  # Start maximized
    # Specify a unique user data directory
    options.add_argument(FIREFOX_APPLICATION_DATA)
    service = FirefoxService(executable_path=GECKODRIVER_PATH)
    logging.info("Initializing headless Firefox WebDriver with specified binary location...")
    driver = webdriver.Firefox(service=service, options=options)
    try:
        yield driver
    finally:
        logging.info("Closing WebDriver...")
        driver.quit()
   
@pytest.fixture(scope="session")
def live_server_url(live_server):
    """Provides the Django live server URL for testing."""
    return live_server.url

def test_firefox_search(get_headless_firefox_driver):
    """Test the Firefox WebDriver with a Google search."""    
    driver = get_headless_firefox_driver
    driver.get("https://www.google.com")
    logging.info("Assert that the title of the page is 'Google'")
    assert "Google" in driver.title






if __name__ == "__main__":
    # Run all tests available
    print("Running tests...")
    pytest.main(["-v", __file__])
    