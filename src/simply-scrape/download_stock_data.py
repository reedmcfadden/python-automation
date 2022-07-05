'''
Created on Jul 3, 2022

@author: reed
'''

import requests


def main():
    stock_url = "https://query1.finance.yahoo.com/v7/finance/download/INTC?period1=1625335145&period2=1656871145&interval=1d&events=history&includeAdjustedClose=true"

    request_headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"} 

    byte_content = requests.get(stock_url, headers=request_headers).content

    with open('intc_data.csv', 'wb') as file:
        file.write(byte_content)


if __name__ == '__main__':
    main()
