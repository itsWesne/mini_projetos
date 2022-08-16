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


# Conexão com o webdriver.
options = webdriver.ChromeOptions()
options.add_argument('--headless')
driver = webdriver.Chrome(chrome_options=options)


def ip_access(ip_url):
    # Abrir página web
    driver.get(f'http://{ip_url}')


def login():
    # ‘Login’ na ONU com usuario e senha
    driver.find_element(By.NAME, 'username').send_keys('admin' + Keys.TAB)
    driver.find_element(By.NAME, 'password').send_keys('admin' + Keys.ENTER)


def wifi_config(wname2, wpass2, wname5, wpass5):
    # Configuração de WIFIs
    find_wlan(driver, By)
    wifi_fiveghz(driver, By, Select, wname2, wpass2)
    wifi_twoghz(driver, By, Select, wname5, wpass5)


def pon_config(vlan, user, ppppass, lan1, lan2, lan3, lan4):
    # Configuração WAN
    find_wan(driver, By)
    pon_wan(driver, By, Select, vlan)
    ppp_settings(driver, By, user, ppppass)
    port_mapping(driver, By, lan1, lan2, lan3, lan4)


def services_config(upnp):
    # Configuração Services
    find_services(driver, By)
    upnp_config(driver, By, Select, upnp)


def advance_config(ping):
    # Configurações Advance
    find_advance(driver, By)
    remote_access(driver, By, ping)


def admin_config(oldpass, newpass):
    # Configurações de admin
    find_admin(driver, By)
    password_config(driver, By, oldpass, newpass)










