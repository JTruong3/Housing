import requests
import pandas as pd
import json
from bs4 import BeautifulSoup

cookies = {
    'user': '{%22id%22:%22689083%22%2C%22firstName%22:%22Jason%22%2C%22lastName%22:%22Truong%22%2C%22email%22:%22jasontruong35@gmail.com%22%2C%22newsletter%22:false%2C%22homePhone%22:%225879378391%22%2C%22jwt%22:%22eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NTI5NzMwNDEsInVzZXJfaWQiOjY4OTA4M30.JL5umcbFzhMM59eqggvQWx9CTBX30a-sCKbPVhxAAs8%22}',
    'jwt': 'eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NTI5NzMwNDEsInVzZXJfaWQiOjY4OTA4M30.JL5umcbFzhMM59eqggvQWx9CTBX30a-sCKbPVhxAAs8',
    'listing-params': '{%22sort%22:%22-date%22%2C%22filter%22:{%22rental%22:false%2C%22status%22:%22not-available-sold%22%2C%22slug%22:%22%22%2C%22latitude%22:44.029542185448754%2C%22longitude%22:-79.4547579295987%2C%22zoom%22:14%2C%22homeType%22:{%22houseDetached%22:true%2C%22houseSemidetached%22:true%2C%22houseAttached%22:true%2C%22townhouse%22:true%2C%22condo%22:true}%2C%22priceMin%22:null%2C%22priceMax%22:null%2C%22listedSince%22:null%2C%22listedTo%22:null%2C%22bedrooms%22:%220+%22%2C%22sqftMin%22:null%2C%22sqftMax%22:null%2C%22bathrooms%22:%221+%22%2C%22parkingSpaces%22:%220+%22%2C%22openHouse%22:false%2C%22garage%22:false%2C%22pool%22:false%2C%22fireplace%22:false%2C%22waterfront%22:false%2C%22additional%22:{%22house%22:{%22singleFamily%22:false%2C%22basementApartment%22:false%2C%22duplex%22:false%2C%22triplex%22:false%2C%22fourplex+%22:false}%2C%22condoOrTownhouse%22:{%22locker%22:%22any%22%2C%22maintenanceFee%22:null}}%2C%22areaName%22:%22Toronto%2C%20ON%22%2C%22boundary%22:%22{%5C%22type%5C%22:%5C%22Polygon%5C%22%2C%5C%22coordinates%5C%22:[[[-79.50368142203034%2C44.010905560115454]%2C[-79.50368142203034%2C44.048178810782055]%2C[-79.40583443716706%2C44.048178810782055]%2C[-79.40583443716706%2C44.010905560115454]%2C[-79.50368142203034%2C44.010905560115454]]]}%22}}',
    '_bazooka_app_session': 'elpPbkhXQUdCNXZKNzRjLzZIRXUzVGVLSnFnQVFhNnJQWWlyVmpkRm1xMXRURm5iRVY0QkV3b2dZMVdYVWZWa1dWZHRTenl5dFFzTEtNbWxXSVNXS1IzSitUT1ZpQk80TURrcnFrczdFelg0cU8rbzl1R0lwOURURVNhdWhoaTEtLUdPYVZSTzRweVlRYUMzQWFmU2lPdGc9PQ%3D%3D--0bca9e48de36b1ef39c2b40a37495c2844fc2990',
    'screen': '{%22width%22:589}',
}

headers = {
    'authority': 'www.zoocasa.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'user={%22id%22:%22689083%22%2C%22firstName%22:%22Jason%22%2C%22lastName%22:%22Truong%22%2C%22email%22:%22jasontruong35@gmail.com%22%2C%22newsletter%22:false%2C%22homePhone%22:%225879378391%22%2C%22jwt%22:%22eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NTI5NzMwNDEsInVzZXJfaWQiOjY4OTA4M30.JL5umcbFzhMM59eqggvQWx9CTBX30a-sCKbPVhxAAs8%22}; jwt=eyJhbGciOiJIUzI1NiJ9.eyJpYXQiOjE2NTI5NzMwNDEsInVzZXJfaWQiOjY4OTA4M30.JL5umcbFzhMM59eqggvQWx9CTBX30a-sCKbPVhxAAs8; listing-params={%22sort%22:%22-date%22%2C%22filter%22:{%22rental%22:false%2C%22status%22:%22not-available-sold%22%2C%22slug%22:%22%22%2C%22latitude%22:44.029542185448754%2C%22longitude%22:-79.4547579295987%2C%22zoom%22:14%2C%22homeType%22:{%22houseDetached%22:true%2C%22houseSemidetached%22:true%2C%22houseAttached%22:true%2C%22townhouse%22:true%2C%22condo%22:true}%2C%22priceMin%22:null%2C%22priceMax%22:null%2C%22listedSince%22:null%2C%22listedTo%22:null%2C%22bedrooms%22:%220+%22%2C%22sqftMin%22:null%2C%22sqftMax%22:null%2C%22bathrooms%22:%221+%22%2C%22parkingSpaces%22:%220+%22%2C%22openHouse%22:false%2C%22garage%22:false%2C%22pool%22:false%2C%22fireplace%22:false%2C%22waterfront%22:false%2C%22additional%22:{%22house%22:{%22singleFamily%22:false%2C%22basementApartment%22:false%2C%22duplex%22:false%2C%22triplex%22:false%2C%22fourplex+%22:false}%2C%22condoOrTownhouse%22:{%22locker%22:%22any%22%2C%22maintenanceFee%22:null}}%2C%22areaName%22:%22Toronto%2C%20ON%22%2C%22boundary%22:%22{%5C%22type%5C%22:%5C%22Polygon%5C%22%2C%5C%22coordinates%5C%22:[[[-79.50368142203034%2C44.010905560115454]%2C[-79.50368142203034%2C44.048178810782055]%2C[-79.40583443716706%2C44.048178810782055]%2C[-79.40583443716706%2C44.010905560115454]%2C[-79.50368142203034%2C44.010905560115454]]]}%22}}; _bazooka_app_session=elpPbkhXQUdCNXZKNzRjLzZIRXUzVGVLSnFnQVFhNnJQWWlyVmpkRm1xMXRURm5iRVY0QkV3b2dZMVdYVWZWa1dWZHRTenl5dFFzTEtNbWxXSVNXS1IzSitUT1ZpQk80TURrcnFrczdFelg0cU8rbzl1R0lwOURURVNhdWhoaTEtLUdPYVZSTzRweVlRYUMzQWFmU2lPdGc9PQ%3D%3D--0bca9e48de36b1ef39c2b40a37495c2844fc2990; screen={%22width%22:589}',
    'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36',
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