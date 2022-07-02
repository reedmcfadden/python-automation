'''
Created on Jun 30, 2022

@author: reed mcfadden
'''

from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_driver():
    opts = Options()

    driver = webdriver.Firefox(options=opts)
    driver.get("http://automated.pythonanywhere.com")
    return driver


def get_aristotle_quote(driver):
    return driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")


def main():
    driver = get_driver()
    element = get_aristotle_quote(driver)
    return element.text


if __name__ == "__main__":
    print(main())
    
