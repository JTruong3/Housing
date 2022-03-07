cd /Users/jasontruong/Downloads/Learn

import requests
import pandas as pd
import json
from bs4 import BeautifulSoup
from Housing.SinglePage import SinglePage

headers = {
    'authority': 'zillow.com',
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
#a
base_url = 'https://www.remax.ca/on/markham-real-estate?v=1&page='
list_1 = []
test_list = []
why_no_work = []
for m in range(3,5):
    siteurl = base_url + str(m)
    r = requests.get(siteurl, headers = headers)
    c = r.content
    soup = BeautifulSoup(c,"html.parser")
    b_all = soup.find("div",{"class","gallery-list is-flex has-flex-wrap"})
    testing = b_all.find_all("app-listing-card",{"class":"ng-star-inserted"})
    why_no_work.append(siteurl)
    for item in testing:
        placeholder = item.find("script",{"type":"application/ld+json"})
        res = json.loads(placeholder.string)
        prop_link = "https://www.remax.ca" + res['@graph'][2]['url']
        test_list.append(prop_link)


for i in test_list:

    pageInfo = SinglePage(i,headers)

    list_1.append(pageInfo)
    
dataTable = pd.DataFrame(list_1)
dataTable["Estimated Monthly Mortgage Payment"] = dataTable["Estimated Monthly Mortgage Payment"].replace('Estimated Mortgage Payment: ', '', regex=True).replace('/Monthly', '', regex=True)
dataTable.to_csv("ProjectRental.csv")