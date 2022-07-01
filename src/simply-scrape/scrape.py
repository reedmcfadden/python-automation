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


def main():
    driver = get_driver()
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text


if __name__ == "__main__":
    print(main())
    
