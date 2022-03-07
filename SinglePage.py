import requests
import pandas as pd
from bs4 import BeautifulSoup

def SinglePage(prop_link,headers):
    r = requests.get(prop_link, headers = headers)
    c = r.content
    soup = BeautifulSoup(c,"html.parser")

    d_set = {}
    try:
        d_set["Address"] = soup.find("span",{"class","listing-address_splitLines__2G5sK"}).text + " , " + soup.find("span",{"class","listing-summary_cityLine__3WHGT listing-address_splitLines__2G5sK"}).text
        
    except:
        d_set["Address"] = None

    try:
        d_set["Price"] = soup.find("div",{"class","listing-summary_listPrice__1bUVm"}).text
        
    except:
        d_set["Price"] = None

    try:
        d_set["Beds"] = soup.find_all("span",{"class":"listing-summary_propertyDetailValue__DzQcA"})[0].text
    except:
        d_set["Beds"] = None

    try:
        d_set["Baths"] = soup.find_all("span",{"class":"listing-summary_propertyDetailValue__DzQcA"})[1].text
    except:
        d_set["Baths"] = None


    ### Property Details
    try:
        prop_features = soup.find_all("ul",{"class":"bullet-section_bulletPointContainer__Ybc96"})
    except:
        prop_features = False
    
    if prop_features != False:
        try:
            d_set["Property Tax"] = prop_features.find_all("span",{"class","detail-value normal-font-weight"})[0].text#
        except:
            d_set["Property Tax"] = None

        try:
            d_set["Date Listed"] = prop_features.find_all("h4",{"class","bullet-section_bulletTitle__3yUEc"})[3].text#
        except:
            d_set["Date Listed"] = None

    # Home Features
    try:
        home_features = soup.find_all("ul",{"class":"bullet-section_bulletPointContainer__Ybc96"})[1]#
    except:
        home_features = False
    
    if home_features != False:
        try:
            d_set["Property Type"] = home_features.find_all("h4",{"class","bullet-section_bulletPointRpw__1IHWv"})[0].text#
        except:
            d_set["Property Type"] = None

    try:
        d_set["Square Footage"] = soup.find_all("span",{"class":"detail ng-star-inserted"})[2].text#
    except:
        d_set["Sqaure Footage"] = None

    try:
        d_set["Estimated Monthly Mortgage Payment ($)"] = soup.find("a",{"class","mortgage-payment_payment__3dpyX"}).text
    except:
        d_set["Estimated Monthly Mortgage Payment ($)"] = None


    return d_set
