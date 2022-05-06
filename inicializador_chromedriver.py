from time import sleep
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By


chromedriver_autoinstaller.install()

browser = webdriver.Chrome()

browser.get('http://app.vemrodar.com.br/login/')


input_login = browser.find_element(By.ID, 'login').send_keys('henrique.siconeli')
input_senha = browser.find_element(By.ID, 'senha').send_keys('020406')

sleep(5000)
