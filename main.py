
from Notes import apicode
import requests
import json
import pandas as pd
#Proximity scoring

api_code = apicode()
p_rental = pd.read_csv('ProjectRental_Toronto.csv',header = 0)
p_rental = p_rental.drop(['Unnamed: 0','Link'],axis = 1)
p_rental = p_rental.dropna(axis = 0, how = 'all')
final_data = []
address = '1307 - 56 Forest Manor Rd Toronto, ON'
for i in p_rental['Address']:
    url_coord


url_coord = 'https://maps.googleapis.com/maps/api/geocode/json?address='+address+'&key='+api_code
coordinates = '43.77346259999999,-79.34492729999999'

url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location='+ coordinates + '&radius=25000&keyword=grocery&key='+api_code

data_source = requests.get(url)
prox_data = json.loads(data_source)
results = prox_data['results']

for result in results:
    name = result['name']
    place_id = result ['place_id']
    lat = result['geometry']['location']['lat']
    lng = result['geometry']['location']['lng']
    rating = result['rating']
    types = result['types']
    vicinity = result['vicinity']
    data = [name, place_id, lat, lng, rating, types, vicinity]
    final_data.append(data)

labels = ['Place Name','Place ID', 'Latitude', 'Longitude', 'Rating', 'Types', 'Vicinity']
grocery1 = pd.DataFrame.from_records(final_data, columns=labels)

grocery1.to_csv("grocery.csv")


https://maps.googleapis.com/maps/api/distancematrix/json?origins=3025 Queen St E , The Beaches, Toronto, ON, M1N 1A5&destinations=43.767539,-79.3418757&key=AIzaSyAytgDBnfkBcKVJwUS4cHUoIxwkSh0EZvM