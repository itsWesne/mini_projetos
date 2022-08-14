def find_advance(driver, By):
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[7]/a').click()


def remote_access(driver, By):
    # Acessar as configurações de acesso remoto
    driver.find_element(By.LINK_TEXT, 'Remote Access').click()
    # Trocar o frame
    driver.switch_to.frame(driver.find_element(By.ID, 'contentIframe'))
    # Habilitar wan ping
    driver.find_element(By.XPATH, '/html/body/form/div[1]/div/table/tbody/tr[6]/td[3]/input').click()
    # Aplicar mudanças
    driver.find_element(By.XPATH, '/html/body/form/div[2]/input[1]').click()
    # Resetar frame
    driver.switch_to.default_content()


