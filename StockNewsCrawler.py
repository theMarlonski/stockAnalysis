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

dfNews = pd.DataFrame(columns=["ticker", "headline", "text"])

url = "http://www.nasdaq.com/symbol/" + "nflx" + "/news-headlines"
"""scrape the html of the site"""
resp = requests.get(links_site)

if not resp.ok:
    return None

html = resp.content

"""convert html to BeautifulSoup object"""
soup = BeautifulSoup(html, "lxml")

"""get list of all links on webpage"""
links = soup.find_all("a")

urls = [link.get("href") for link in links]
urls = [url for url in urls if url is not None]

"""Filter the list of urls to just the news articles"""
news_urls = [url for url in urls if "/article/" in url]


landing_site = "http://www.nasdaq.com/symbol/" + "nflx" + "/news-headlines"

all_news_urls = get_news_urls(landing_site)

current_urls_list = all_news_urls.copy()

index = 2

"""Loop through each sequential page, scraping the links from each"""
while (
    (current_urls_list is not None)
    and (current_urls_list != [])
    and (index <= upper_page_limit)
):

    """Construct URL for page in loop based off index"""
    current_site = landing_site + "?page=" + str(index)
    current_urls_list = get_news_urls(current_site)

    """Append current webpage's list of urls to all_news_urls"""
    all_news_urls = all_news_urls + current_urls_list

    index = index + 1

all_news_urls = list(set(all_news_urls))

"""Now, we have a list of urls, we need to actually scrape the text"""
# all_articles = [scrape_news_text(news_url) for news_url in all_news_urls]

# return all_articles
