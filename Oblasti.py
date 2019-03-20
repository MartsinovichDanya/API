import requests

goroda = ['Барнаул', 'Мелеуз', 'Йошкар-Ола']

for gorod in goroda:
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?geocode={gorod}, 1&format=json"
    result = requests.get(geocoder_request).json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']\
        ['metaDataProperty']['GeocoderMetaData']['AddressDetails']['Country']['AdministrativeArea']\
        ['AdministrativeAreaName']
    print(result)
