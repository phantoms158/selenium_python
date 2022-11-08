import pytest
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = None

@pytest.fixture(scope="class")
def setup(request):
    global driver
    driver = webdriver.Chrome(ChromeDriverManager().install())

    driver.get("https://facebook.com")
    driver.maximize_window()

    request.cls.driver = driver
    yield
    driver.close()