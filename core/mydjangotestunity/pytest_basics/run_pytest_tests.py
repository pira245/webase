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
# Firefox
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
##############################################################################################
"""
    Testing with pytest
"""
##############################################################################################
# Import all test files
import core
import core.mytestunity.system_file as system_file
import core.web_core
##############################################################################################

def test_system_file():
    # Test system_file.py
    system_file.test_system_file()


if __name__ == "__main__":
    # Run all tests available
    print("Running tests...")
    pytest.main(["-v", __file__])
   