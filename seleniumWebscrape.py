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
base_url = 'https://www.remax.ca/on/markham-real-estate?pageNumber='
test_list = []
i = 0
j = 1
while len(test_list) <= 15:

    for m in range(i,j):
        siteurl = base_url + str(m)
        driver.get(siteurl)

        # List of elements for websites
        websites = driver.find_elements_by_xpath('//a[@class="listing-card_listingCard__G6M8g"]')
    
        # List of elements for prices
        p_list = websites[0].find_elements_by_xpath('//h2[@class="listing-card_price__sL9TT"]')


        for idx,i_sites in enumerate(websites):

            h_price = int(p_list[idx].text.replace('$','').replace(',',''))
            
            # Removes rental properties
            if h_price > 25000:
                test_list.append(i_sites.get_attribute("href"))
    i += 1
    j += 1

list_1 = []
for i in tqdm(test_list):

    pageInfo = SinglePage(i,headers)

    list_1.append(pageInfo)
    
dataTable = pd.DataFrame(list_1)
dataTable["Estimated Monthly Mortgage Payment ($)"] = dataTable["Estimated Monthly Mortgage Payment ($)"].replace('Est. Payment: ', '', regex=True).replace(' monthly', '', regex=True)
numCols = ['Price','Estimated Monthly Mortgage Payment ($)']
dataTable[numCols] = dataTable[numCols].replace(',','',regex = True)
dataTable[numCols] = dataTable[numCols].replace("\$",'',regex = True)
dataTable['Link'] = test_list
dataTable.to_csv("ProjectRental_may19m.csv")


driver.close

# https://www.ratehub.ca/mortgage-affordability-calculator

# https://www.remax.ca/on/toronto-real-estate/215-151-dan-leckie-way-wp_id301136190-lst

