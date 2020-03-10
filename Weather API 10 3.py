import json

from urllib.request import urlopen


query = input('Query please: ')


queryLink = 'https://www.metaweather.com/api/location/search/?query=' + query

link = 'https://www.metaweather.com/api/location/'




wget = urlopen(queryLink)



webtext = wget.read()

woeid = (json.loads(webtext.decode('utf-8')))[0]['woeid']

linkoin = link + str(woeid)

wget1 = urlopen(linkoin)

weatherInfo = wget1.read()

jsonDecode = json.loads(weatherInfo.decode('utf-8'))

weatherArray = jsonDecode['consolidated_weather']

for i in weatherArray:
     (i['the_temp'])



#print(weatherInfo)
