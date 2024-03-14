import requests
from time import sleep
# from pprint import pprint


def find_uk_city(coordinates:list) -> str:
    url = 'https://geocode.maps.co/reverse'
    API_key = ''
    list_of_cities = ['Leeds', 'London', 'Liverpool', 'Manchester', 'Oxford', 'Edinburgh', 'Norwich', 'York']
    for latitude, longitude in coordinates:
        params = {
            'lat': latitude,
            'lon': longitude,
            'api_key': API_key
        }
        response = requests.get(url, params=params)
        if response.status_code == 200:
            city = response.json()['address']['city']
            if city in list_of_cities:
                return city
        sleep(1)

if __name__ == '__main__':
    _coordinates = [
        ('55.7514952', '37.618153095505875'),
        ('52.3727598', '4.8936041'),
        ('53.4071991', '-2.99168')
    ]
    assert find_uk_city(_coordinates) == 'Liverpool'