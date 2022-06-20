from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from time import sleep

navegador = webdriver.Chrome()

navegador.get('https://192.168.1.1')
