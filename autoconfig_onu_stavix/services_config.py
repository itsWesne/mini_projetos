def find_services(driver, By):
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[5]/a').click()


def upnp_config(driver, By, Select, upnp):
    if upnp:
        # Acessar as configurações UPnP
        driver.find_element(By.LINK_TEXT, 'UPnP').click()
        # Acessar o frame das configurações
        driver.switch_to.frame(driver.find_element(By.ID, 'contentIframe'))
        # Ativação do UPnP
        driver.find_element(By.XPATH, '/html/body/form/div[1]/table/tbody/tr[1]/td/input[2]').click()
        select = Select(driver.find_element(By.XPATH, '/html/body/form/div[1]/table/tbody/tr[2]/td/select'))
        select.select_by_value('65536')
        driver.find_element(By.XPATH, '/html/body/form/div[2]/input[1]').click()
        driver.switch_to.default_content()




