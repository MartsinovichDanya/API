import requests

geocoder_request = "http://geocode-maps.yandex.ru/1.x/?geocode=Красная пл-дь, 1&format=json"
result = requests.get(geocoder_request).json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']
print(result['metaDataProperty']['GeocoderMetaData']['Address']['formatted'])
print(result['Point']['pos'])
