import requests

goroda = ['Хабаровск', 'Уфа', 'Нижний Новгород', 'Калининград']

for gorod in goroda:
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?geocode={gorod}, 1&format=json"
    result = requests.get(geocoder_request).json()['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']\
        ['metaDataProperty']['GeocoderMetaData']['Address']['Components'][1]\
        ['name']
    print(result)
