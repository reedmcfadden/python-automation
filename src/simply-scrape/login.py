'''
Created on Jul 1, 2022

@author: reed
'''

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

loginSite = 'http:://automated.pythonanywhere.com/login/';
username = "automated"
pwd = "automatedautomated"


def get_driver():
    opts = Options()
    driver = webdriver.Firefox(options=opts)
    driver.get("http://automated.pythonanywhere.com/login/")
    return driver


def login(driver):
    driver.find_element(by="id", value="id_username").send_keys(username)
    driver.find_element(by="id", value="id_password").send_keys(pwd + Keys.RETURN)

    
def click_home_button(driver):
    time.sleep(2)  # wait for button to be available. could be done w/ waits
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()


def main():
    driver = get_driver()
    login(driver)
    click_home_button(driver)


if __name__ == '__main__':
    main()
