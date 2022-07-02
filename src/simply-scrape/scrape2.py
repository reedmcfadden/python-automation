'''
Created on Jun 30, 2022

@author: reed
'''

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time


def get_driver():
    opts = Options()

    driver = webdriver.Firefox(options=opts)
    driver.get("http://automated.pythonanywhere.com")
    return driver


def get_world_temperature(driver):
    """ Get the temperature from the text, contained in the last characters of the string """
    time.sleep(2)
    element = driver.find_element(by="xpath", value='//*[@id="displaytimer"]')
    world_temp = element.text.split(": ")[1]
    return world_temp 


def main():
    driver = get_driver()
    return get_world_temperature(driver)


if __name__ == '__main__':
    print(main())
