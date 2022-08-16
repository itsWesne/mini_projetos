def find_admin(driver, By):
    driver.find_element(By.XPATH, '//*[@id="nav"]/li[9]/a').click()


def password_config(driver, By, oldpassword, newpassword):
    oldpass = oldpassword
    newpass = newpassword

    # Acessando configuração de senha
    driver.find_element(By.LINK_TEXT, 'Password').click()
    # Troca de fram
    driver.switch_to.frame(driver.find_element(By.ID, 'contentIframe'))
    # Adicionar nova senha
    driver.find_element(By.NAME, 'oldpass').send_keys(oldpass)
    driver.find_element(By.NAME, 'newpass').send_keys(newpass)
    driver.find_element(By.NAME, 'confpass').send_keys(newpass)
    # Aplicar
    driver.find_element(By.XPATH, '/html/body/form/div[2]/input[2]').click()


