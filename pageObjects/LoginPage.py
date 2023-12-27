from selenium import webdriver
from selenium.webdriver.common.by import By


class Login:
    textbox_username_name = "userName"
    textbox_name_psw = "password"
    button_login_name = "submit"

    def __init__(self, driver):
        self.driver = driver

    def setUsername(self, userName, textbox_username_name=textbox_username_name):
        self.driver.find_element(By.NAME, textbox_username_name).clear()
        self.driver.find_element(By.NAME, textbox_username_name).send_keys(userName)

    def setPassword(self, password, textbox_name_psw=textbox_name_psw):
        self.driver.find_element(By.NAME, textbox_name_psw).clear()
        self.driver.find_element(By.NAME, textbox_name_psw).send_keys(password)

    def submitLoginBtn(self, button_login_name=button_login_name):
        self.driver.find_element(By.NAME, button_login_name).click()