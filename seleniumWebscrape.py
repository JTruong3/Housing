import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
from SinglePage import SinglePage
from tqdm import tqdm

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

headers = {
    'authority': 'remax.com',
    'dnt': '1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
}

driver = webdriver.Chrome('/Users/jasontruong/Downloads/Learn/Rental/Housing/chromedriver')
base_url = 'https://www.remax.ca/on/toronto-real-estate?pageNumber='
test_list = []
for m in range(1,2):
    siteurl = base_url + str(m)
    driver.get(siteurl)

    websites = driver.find_elements_by_xpath('//a[@class="listing-card_listingCard__G6M8g"]')

    for i in websites:
        test_list.append(i.get_attribute("href"))

list_1 = []
for i in tqdm(test_list):

    pageInfo = SinglePage(i,headers)

    list_1.append(pageInfo)
    
dataTable = pd.DataFrame(list_1)
dataTable["Estimated Monthly Mortgage Payment ($)"] = dataTable["Estimated Monthly Mortgage Payment ($)"].replace('Est. Payment: ', '', regex=True).replace(' monthly', '', regex=True)
dataTable['Link'] = test_list
dataTable.to_csv("ProjectRental_Toronto.csv")


driver.close

# https://www.ratehub.ca/mortgage-affordability-calculator

# https://www.remax.ca/on/toronto-real-estate/215-151-dan-leckie-way-wp_id301136190-lst

