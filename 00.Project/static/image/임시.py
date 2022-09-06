!pip install -U googlemaps

import googlemaps

gmaps = googlemaps.Client(key='AIzaSyC1ozHs1I96tzadkejUGanL7zD3ALzRbqI')
geocode_result = gmaps.geocode(('광주광역시 동구 경양로 235번길'), language='ko')
geocode_result[0]['geometry']['location']['lat']
geocode_result[0]['geometry']['location']['lng']
print(geocode_result[0]['geometry']['location']['lat'])
