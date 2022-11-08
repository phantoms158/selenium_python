import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

username = 'administrator'
password = '3QHR1EAEgUgIhQj4jC8ZM/bnC1Qdr7vBPGd'

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://yakult.salefie.net/")

#input username
inputUsername = driver.find_element(by=By.NAME, value='username')
inputUsername.send_keys(username)

#input pass
inputPass = driver.find_element(by=By.NAME, value='password')
inputPass.send_keys(password)

#click button
btnLogin = driver.find_element(by=By.ID, value= 'login-submit')
btnLogin.click()

time.sleep(2)