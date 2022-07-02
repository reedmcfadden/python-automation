'''
Created on Jul 1, 2022

@author: reed
'''

from datetime import datetime
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


def get_world_temperature(driver):
    """ Get the temperature from the text, contained in the last characters of the string """
    element = driver.find_element(by="xpath", value='//*[@id="displaytimer"]')
    world_temp = element.text.split(": ")[1]
    return world_temp 


def write_new_temperature(driver):
    with open("temperatures.txt", "a") as temperature_file:
        new_entry = str(datetime.now()) + " -- Temperature: " + get_world_temperature(driver) + "\n"
        temperature_file.write(new_entry)


def main():
    driver = get_driver()
    login(driver)
    click_home_button(driver)
    
    # write each updated temperature to a file. check every 2 seconds.
    while True:
        time.sleep(2)
        write_new_temperature(driver)


if __name__ == '__main__':
    main()
