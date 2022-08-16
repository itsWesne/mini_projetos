def find_wan(driver, By):
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[4]/a').click()


def apply_changes(driver, By):
    # Aplicando mudanças
    driver.find_element(By.ID, 'apply').click()
    # Reset de frame
    driver.switch_to.default_content()


def pon_wan(driver, By, Select, vlan):
    vl = vlan
    # Trocar o frame
    driver.switch_to.frame(driver.find_element(By.ID, 'contentIframe'))
    # VLAN ID
    driver.find_element(By.NAME, 'vid').clear()
    driver.find_element(By.NAME, 'vid').send_keys(vl)
    # Channel Mode (PPPoE)
    select = Select(driver.find_element(By.NAME, 'adslConnectionMode'))
    select.select_by_visible_text('PPPoE')


def ppp_settings(driver, By, user, ppppass):
    username = user
    password = ppppass
    # PPP Settings
    driver.find_element(By.NAME, 'pppUserName').clear()
    driver.find_element(By.NAME, 'pppUserName').send_keys(username)
    driver.find_element(By.NAME, 'pppPassword').clear()
    driver.find_element(By.NAME, 'pppPassword').send_keys(password)


def port_mapping(driver, By, lan1, lan2, lan3, lan4):
    # Checkboxs das portas
    lan_1 = driver.find_element(By.XPATH, '//*[@id="tbl_pmap"]/tbody/tr[2]/td[1]/input')
    lan_2 = driver.find_element(By.XPATH, '//*[@id="tbl_pmap"]/tbody/tr[2]/td[2]/input')
    lan_3 = driver.find_element(By.XPATH, '//*[@id="tbl_pmap"]/tbody/tr[3]/td[1]/input')
    lan_4 = driver.find_element(By.XPATH, '//*[@id="tbl_pmap"]/tbody/tr[3]/td[2]/input')
    # Habilitando portas
    if lan1:
        lan_1.click()
    if lan2:
        lan_2.click()
    if lan3:
        lan_3.click()
    if lan4:
        lan_4.click()
    # Aplicar mudanças
    apply_changes(driver, By)





