import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By

class FacebookPage:

    def __init__(self, driver):
        self.driver = driver

    email = (By.NAME, 'email')
    password = (By.NAME, 'pass')
    btnLogin = (By.NAME, 'login')

    def getEmail(self):
        return self.driver.find_element(*FacebookPage.email)


    def getPassword(self):
        return self.driver.find_element(*FacebookPage.password)

    def submitForm(self):
        return self.driver.find_element(*FacebookPage.btnLogin)

    def screenshot(self):
        self.driver.save_screenshot("ss.png")

