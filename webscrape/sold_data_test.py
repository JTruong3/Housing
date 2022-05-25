import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

cookies = {
}

headers = {
}
city = 'markham'
address = ['129-cornwall-dr','7-millstone-ct','40-drawbridge-dr']
final_list = []
may19m = pd.read_csv('ProjectRental_may19m.csv')
may19m['Address'] = may19m['Address'].replace(' - ','-',regex = True).str.lower()
may19m['Address'] = may19m['Address'].replace(' ','-',regex = True)
may19m['Location'] = may19m['Location'].replace(' ','-',regex = True).str.lower()
def soldPrice(city,address):

    scrappedData = {}
    webpage = 'https://www.zoocasa.com/'+ city +'-on-real-estate/'+ address
    response = requests.get(webpage, cookies=cookies, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    scrappedData['Address'] = address

    try: 
            house_status = soup.find("div",{"class","style_component__Dee_J style_for-sale__IKf5m undefined"}).text

    except:
        try:
            house_status = soup.find("div",{"class","style_component__Dee_J undefined undefined"}).text
        except:
            house_status = None

    if house_status == 'For Sale':
        try:
            scrappedData['List Price'] = soup.find("div",{"class","style_price__Vq72L"}).text.replace('$','')
        except:
            scrappedData['List Price'] = None

        scrappedData['Sold Price'] = None

    elif house_status =='Sold':
        try:
            scrappedData['List Price'] = soup.find("div",{"class","style_list-price__RRgvp"}).text.replace('$','')
        except:
            scrappedData['List Price'] = None

        try:
            scrappedData['Sold Price'] = soup.find("div",{"class","style_price__Vq72L"}).text.replace('$','')
        except:
            scrappedData['Sold Price'] = None
    
    
    return scrappedData

for index in may19m.index:
    a = soldPrice(may19m['Location'][index],may19m['Address'][index])
    final_list.append(a)



#https://curlconverter.com/