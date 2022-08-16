def find_wlan(driver, By):
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[3]/a').click()


def config_wifi(driver, By, Select, wifi_name, wifi_pass):
    # Troca de Frame para conseguir acessar os elementos de configuração
    driver.switch_to.frame(driver.find_element(By.ID, 'contentIframe'))
    # Trocar nome da rede
    driver.find_element(By.NAME, 'ssid').clear()
    driver.find_element(By.NAME, 'ssid').send_keys(wifi_name)
    driver.find_element(By.NAME, 'save').click()
    # Resetar frame & acessar troca de senha
    driver.switch_to.default_content()
    driver.find_element(By.LINK_TEXT, 'Security').click()
    # Troca de Frame
    driver.switch_to.frame(driver.find_element(By.ID, 'contentIframe'))
    # Trocar a categoria de segurança da senha pelo Dropdown
    select = Select(driver.find_element(By.ID, 'security_method'))
    select.select_by_visible_text('WPA2 Mixed')
    # Inserir a senha desejada
    driver.find_element(By.ID, 'wpapsk').clear()
    driver.find_element(By.ID, 'wpapsk').send_keys(wifi_pass)
    driver.find_element(By.NAME, 'save').click()
    # Reset de frame
    driver.switch_to.default_content()


# CONFIGURAÇÃO REDE 5.8
def wifi_fiveghz(driver, By, Select, wname, wpass):
    wifi_name = wname
    wifi_pass = wpass
    config_wifi(driver, By, Select, wifi_name, wifi_pass)


# CONFIGURAÇÃO REDE 2.4
def wifi_twoghz(driver, By, Select, wname, wpass):
    wifi_name = wname
    wifi_pass = wpass
    driver.find_element(By.LINK_TEXT, 'wlan1 (2.4GHz)').click()
    config_wifi(driver, By, Select, wifi_name, wifi_pass)





