import requests
import os
import pygame
import sys
from distance import lonlat_distance

toponym_to_find = " ".join(sys.argv[1:])
geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"
geocoder_params = {"geocode": toponym_to_find, "format": "json"}
response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
toponym_coodrinates = toponym["Point"]["pos"]
toponym_longitude, toponym_lattitude = toponym_coodrinates.split(" ")

delta = "0.005"

search_api_server = "https://search-maps.yandex.ru/v1/"
api_key = "dda3ddba-c9ea-4ead-9010-f43fbc15c6e3"

address_ll = ','.join((toponym_longitude, toponym_lattitude))

search_params = {
    "apikey": api_key,
    "text": "аптека",
    "lang": "ru_RU",
    "ll": address_ll,
    "type": "biz",
    "spn": ",".join([delta, delta])
}

response = requests.get(search_api_server, params=search_params)
if not response:
    pass

json_response = response.json()

organization = json_response["features"][0]
org_name = organization["properties"]["CompanyMetaData"]["name"]
org_address = organization["properties"]["CompanyMetaData"]["address"]

point = organization["geometry"]["coordinates"]
org_point = "{0},{1}".format(point[0], point[1])

map_params = {
    "ll": address_ll,
    # "spn": ",".join([delta, delta]),
    "l": "sat,skl",
    "pt": f"{org_point},pm2wtm2~{address_ll},pm2grm1"
}

dist = lonlat_distance((float(point[0]), float(point[1])),
                       (float(toponym_longitude), float(toponym_lattitude)))

print(org_name)
print(org_address)
print(organization['properties']['CompanyMetaData']['Hours']['text'])
print(f'Расстояние до аптеки - {int(dist)}м')

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

map_file = "map.png"
try:
    with open(map_file, "wb") as file:
        file.write(response.content)
except IOError as ex:
    print("Ошибка записи временного файла:", ex)
    sys.exit(2)

pygame.init()
screen = pygame.display.set_mode((600, 450))
screen.blit(pygame.image.load(map_file), (0, 0))
pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
pygame.quit()

os.remove(map_file)
