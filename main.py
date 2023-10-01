import phonenumbers
import opencage
import folium
from phonenumber import numbers

from phonenumbers import geocoder

pepnumber= phonenumbers.parse(numbers)
location = geocoder.description_for_number(pepnumber,"en")
print(location)

from phonenumbers import carrier
service_pro = phonenumbers.parse(numbers)
print(carrier.name_for_number(service_pro, "en"))

from opencage.geocoder import OpenCageGeocode
key = "9383c5e87b4840f8a168be8641d0b92e"
geocoder = OpenCageGeocode(key)
query = str(location)
results = geocoder.geocode(query)
#print(results)


lat = results [0]['geometry']['lat']
lng = results [0]['geometry']['lng']
print(lat,lng)


myMap = folium.Map(location=[lat, lng], zoom_start= 9 )
folium.Marker([lat, lng], popup=location).add_to(myMap)

myMap.save("mylocation.html")