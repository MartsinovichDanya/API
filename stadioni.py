import pygame
import requests
import sys
import os

response = None
try:
    map_request = "https://static-maps.yandex.ru/1.x/?ll=37.617635,55.740814&spn=0.2,0.2&l=map&pt=37.694944,55.803944,pmdbm1~37.559379,55.791243,pmdbm2~37.552166,55.715677,pmdbm3"
    response = requests.get(map_request)

    if not response:
        print("Ошибка выполнения запроса:")
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
except Exception:
    print("Запрос не удалось выполнить. Проверьте наличие сети Интернет.")
    sys.exit(1)

map_file = "map.jpg"
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
