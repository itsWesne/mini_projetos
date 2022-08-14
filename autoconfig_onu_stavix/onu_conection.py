from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from wlan_config import find_wlan, wifi_fiveghz, wifi_twoghz
from wan_config import find_wan, pon_wan, ppp_settings, port_mapping
from services_config import upnp_config
from services_config import find_services
from advance_config import find_advance, remote_access
from admin_config import find_admin, password_config


# Conexão com o webdriver
driver = webdriver.Chrome()

# Abrir página web // Criar uma função?
ipaddress = "http://192.168.1.1"
driver.get(ipaddress)

# ‘Login’ na ONU com usuario e senha
driver.find_element(By.NAME, 'username').send_keys('admin' + Keys.TAB)
driver.find_element(By.NAME, 'password').send_keys('admin' + Keys.ENTER)


# Configuração de WIFIs
find_wlan(driver, By)
wifi_fiveghz(driver, By, Select)
wifi_twoghz(driver, By, Select)

# Configuração WAN
find_wan(driver, By)
pon_wan(driver, By, Select)
ppp_settings(driver, By)
port_mapping(driver, By)

# Configuração Services
find_services(driver, By)
upnp_config(driver, By, Select)

# Configurações Advance
find_advance(driver, By)
remote_access(driver, By)

# Configurações de admin
find_admin(driver, By)
password_config(driver, By)










