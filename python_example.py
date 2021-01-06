from src.testproject.sdk.drivers import webdriver
from selenium.webdriver import ChromeOptions
import pytest
import os

def test_simple_test():
    driver = webdriver.Chrome()

    driver.get("https://example.testproject.io/web/")

    driver.find_element_by_css_selector("#name").send_keys("John Smith")
    driver.find_element_by_css_selector("#password").send_keys(os.environ['PASSWORD'])
    driver.find_element_by_css_selector("#login").click()

    passed = driver.find_element_by_css_selector("#logout").is_displayed()

    print("Test passed") if passed else print("Test failed")

    driver.quit()
