import requests
import pandas as pd
from bs4 import BeautifulSoup

def SinglePage(prop_link,headers):
    r = requests.get(prop_link, headers = headers)
    c = r.content
    soup = BeautifulSoup(c,"html.parser")

    d_set = {}
    try:
        d_set["Address"] = soup.find("span",{"class","listing-address_splitLines__pLZIy"}).text
        
    except:
        d_set["Address"] = None


    try:
        d_set["Location"],d_set["Province"],d_set["Postal Code"] = soup.find("span",{"class","listing-summary_cityLine__YxXgL listing-address_splitLines__pLZIy"}).text.split(',')

    except:
        d_set["Location"],d_set["Province"],d_set["Postal Code"] = None

    try:
        d_set["Description"] = soup.find('p').getText()

        if "Laundry" in d_set["Description"] or "Washer" in d_set["Description"] or "Dryer" in d_set["Description"]:
            d_set["Laundry"] = "Yes"
        else:
            d_set["Laundry"] = "No"
        
    except:
        d_set["Description"] = None
    

    try:
        d_set["Price"] = soup.find("div",{"class","listing-summary_listPrice__PJawt"}).text
        
    except:
        d_set["Price"] = None

    try:
        d_set["Beds"] = soup.find_all("span",{"class":"listing-summary_propertyDetailValue__UOUcR"})[0].text
    except:
        d_set["Beds"] = None

    try:
        d_set["Baths"] = soup.find_all("span",{"class":"listing-summary_propertyDetailValue__UOUcR"})[1].text
    except:
        d_set["Baths"] = None


    ### Property Details
    try:
        prop_features = soup.findAll("ul",{"class":"bullet-section_residentialBulletPointContainer__ox7JW"})[0]
    except:
        prop_features = False
    
    if prop_features != False:
        # try:
        #     d_set["Property Tax"] = prop_features.findAll("li",{"class","bullet-section_bulletPointRow__4pBp6 listing-detail-bullet-section_propertyDetailsBullet__EevAP"})[0].text#
        # except:
        #     d_set["Property Tax"] = None

        try:
            d_set["Date Listed"] = prop_features.findAll("li",{"class","bullet-section_bulletPointRow__4pBp6 listing-detail-bullet-section_propertyDetailsBullet__EevAP"})[3].text#
        except:
            d_set["Date Listed"] = None

    # Home Features
    try:
        home_features = soup.findAll("ul",{"class":"bullet-section_residentialBulletPointContainer__ox7JW"})[1]
    except:
        home_features = False
    
    if home_features != False:
        try:
            d_set["Property Type"] = home_features.findAll("li",{"class","bullet-section_bulletPointRow__4pBp6"})[0].text#
        except:
            d_set["Property Type"] = None

    # try:
    #     d_set["Property Type"] = soup.find_all("span",{"class":"listing-summary_propertyDetailValue__UOUcR"})[3].text#
    # except:
    #     d_set["Property Type"] = None


    # try:
    #     d_set["Square Footage"] = soup.find_all("span",{"class":"listing-summary_propertyDetailValue__UOUcR"})[2].text#
    # except:
    #     d_set["Square Footage"] = None

    try:
        d_set["Estimated Monthly Mortgage Payment ($)"] = soup.find("a",{"class","mortgage-payment_payment__kyP2h"}).text
    except:
        d_set["Estimated Monthly Mortgage Payment ($)"] = None


    return d_set

