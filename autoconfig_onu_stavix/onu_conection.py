from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from wlan_config import find_wlan, wifi_fiveghz, wifi_twoghz
from time import sleep

# Conexão com o webdriver
driver = webdriver.Chrome()

# Abrir página web // Criar uma função?
ipaddress = "http://192.168.1.1"
driver.get(ipaddress)

# ‘Login’ na ONU com usuario e senha
driver.find_element(By.NAME, 'username').send_keys('admin' + Keys.TAB)
sleep(1)
driver.find_element(By.NAME, 'password').send_keys('admin' + Keys.ENTER)
sleep(1)

# Configuração de WIFIs
# find_wlan(driver, By)
# sleep(1)
# wifi_fiveghz(driver, By, Select)
# wifi_twoghz(driver, By, Select)

# Configuração WAN




