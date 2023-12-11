import phonenumbers
import opencage
import folium
from number import num
from phonenumbers import geocoder

pnum = phonenumbers.parse(num)
loc = geocoder.description_for_number(pnum, 'en')

print(loc)

from phonenumbers import carrier
service_provider = phonenumbers.parse(num)
print(carrier.name_for_number(service_provider,'en'))

from opencage.geocoder import OpenCageGeocode
key = 'a3f8482246fe4f5595984de7747e90ef'

geocoder = OpenCageGeocode(key)
query = str(loc)
results = geocoder.geocode(query)
#print(results)
latitude = results[0]['geometry']['lat']
langitude = results[0]['geometry']['lng']

print(latitude, langitude)

map = folium.Map(loc=[latitude,langitude],zoom_start=6)
folium.Marker([latitude,langitude],popup=loc).add_to(map)
map.save('location.html')