import requests
import pandas as pd
import os
import time
import random
from bs4 import BeautifulSoup as bs
from selenium import webdriver
import re
import numpy as np
import warnings
import itertools

option = webdriver.ChromeOptions()
option.add_argument("--no-sandbox")
option.add_argument("--disable-dev-shm-usage")
option.add_argument("--incognito")
option.add_argument("--disable-infobars")
option.add_argument("--disable-notifications")
option.add_experimental_option("excludeSwitches", ["enable-automation"])

driver = webdriver.Chrome(options=option)
driver.implicitly_wait(10)

MostActiveStocks = pd.DataFrame(columns=["Ticker", "Position"])
url = "https://www.nasdaq.com/market-activity/most-active"

driver.get(url)

sourceCode = driver.page_source
soup = bs(sourceCode, "html.parser")

StockList = []

for Active in soup.find("tbody", {"class": "most-active__body"}).find_all(
    "a", class_="firstCell"
):
    StockList.append(Active.text)


TickerList = StockList[::2]
NameList = [x for x in StockList if x not in TickerList]

dfStock = pd.DataFrame(columns=["Ticker", "Name"])
dfStock["Ticker"] = TickerList
dfStock["Name"] = NameList
dfStock.reset_index(drop=True)
