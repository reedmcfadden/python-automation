'''
Created on Jul 1, 2022

@author: reed
'''

from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
import time

loginSite = 'https://www.vooray.com/account/login?return_url=%2Faccount';
username = "reed.mcfadden@gmail.com"
pwd = "744479267835367879742992"


def get_driver():
    opts = Options()
    driver = webdriver.Firefox(options=opts)
    driver.get(loginSite)
    return driver


def login(driver):
    driver.find_element(by="id", value="CustomerEmail").send_keys(username)
    driver.find_element(by="id", value="CustomerPassword").send_keys(pwd + Keys.RETURN)

    
def click_contact_button(driver):
    time.sleep(2)  # wait for button to be available. could be done w/ waits
    # todo update with actual vooray contact button
    driver.find_element(by="xpath", value="/html/body/div[6]/div/footer/div[1]/div/div[2]/div/ul/li[2]/a").click()


def main():
    driver = get_driver()
    login(driver)
    click_contact_button(driver)
    

if __name__ == '__main__':
    main()
