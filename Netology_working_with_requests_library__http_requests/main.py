import requests
import json
from pprint import pprint

url = "https://functions.yandexcloud.net/d4e8qsrmeednndemfsus"

payload = json.dumps({
    "name": "Дмитрий",
    "surname": "Морозов",
    "patronymic": "Отсутствует",
    "telephone": "+7(903)392-22-29",
    "birthdate": "1991-03-10",
    "passport": "1111 11111111"
})
headers = {
    'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, data=payload)
# response = requests.post(url, json=json.loads(payload))

# print(response.json())

# response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)



# Получаем инфомацию о картинке дня
url_nasa = 'https://api.nasa.gov/planetary/apod'
parametrs = {
    'api_key': '',
    'date': '2024-02-01'
}
response = requests.get(url_nasa, params=parametrs)
# print(response.text)
url_image = response.json().get('url')
image_name = url_image.split('/')[-1]
# print(image_name)
# print(url_image)

# Скачать картинку дня
response = requests.get(url_image)
print(response)
with open(image_name, 'wb') as image:
    image.write(response.content)

response = requests.get(requests.get(url_nasa, params=parametrs).json().get('hdurl'))
with open('HD_' + image_name, 'wb') as image:
    image.write(response.content)

# Работа с yandex disk
headers = {
    'Authorization': ''
}
response = requests.put('https://cloud-api.yandex.net/v1/disk/resources',
                        headers=headers,
                        params={'path': 'image'})

pprint(response.json())

# Загрузка файла на диск
url_yandex_disk = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
response = requests.get(url_yandex_disk,
                        headers=headers,
                        params={'path': f'image/{image_name}'})
pprint(response.json())
url_for_uploud = response.json().get('href')
with open('HD_' + image_name, 'rb') as f:
    requests.put(url_for_uploud, files={'file': f})

print('Загрузка завершена')