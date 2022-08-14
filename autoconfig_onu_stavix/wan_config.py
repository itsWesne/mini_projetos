def find_wan(driver, By):
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[4]/a').click()


def pon_wan(driver, By, Select):
    vlan = '2800'
    # Trocar o frame
    driver.switch_to.frame(driver.find_element(By.ID, 'contentIframe'))
    # VLAN ID
    driver.find_element(By.NAME, 'vid').clear()
    driver.find_element(By.NAME, 'vid').send_keys(vlan)
    # Channel Mode (PPPoE)
    select = Select(driver.find_element(By.NAME, 'adslConnectionMode'))
    select.select_by_visible_text('PPPoE')


def ppp_settings(driver, By):
    username = 'itswesne'
    password = '102030'
    # PPP Settings
    driver.find_element(By.NAME, 'pppUserName').clear()
    driver.find_element(By.NAME, 'pppUserName').send_keys(username)
    driver.find_element(By.NAME, 'pppPassword').send_keys(password)


def port_mapping(driver, By):
    # Checkboxs das portas
    lan_1 = driver.find_element(By.XPATH, '//*[@id="tbl_pmap"]/tbody/tr[2]/td[1]/input')
    lan_2 = driver.find_element(By.XPATH, '//*[@id="tbl_pmap"]/tbody/tr[2]/td[2]/input')
    lan_3 = driver.find_element(By.XPATH, '//*[@id="tbl_pmap"]/tbody/tr[3]/td[1]/input')
    lan_4 = driver.find_element(By.XPATH, '//*[@id="tbl_pmap"]/tbody/tr[3]/td[2]/input')
    # Habilitando portas
    lan_1.click()
    lan_2.click()
    lan_3.click()
    lan_4.click()
    # Aplicando mudanças
    driver.find_element(By.ID, 'apply').click()





