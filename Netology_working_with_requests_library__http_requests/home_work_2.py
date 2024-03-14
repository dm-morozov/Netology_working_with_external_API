import requests
from pprint import pprint

def superheros():
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    all_heroes_info = requests.get(url).json()
    hero_list_id = []
    for hero_info in all_heroes_info:
        hero_id = hero_info.get('id')
        hero_list_id.append(hero_id)
    return hero_list_id

def get_the_smartest_superhero(superheros) -> str:
    heroes_list = superheros()
    the_smartest_superhero = ''
    intelligence_count = 0
    url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
    all_heroes_info = requests.get(url).json()
    for hero_info in all_heroes_info:
        hero_id = hero_info.get('id')
        hero_name = hero_info.get('name')
        if hero_id in heroes_list:
            intelligence = hero_info['powerstats']['intelligence']
            if intelligence_count < intelligence :
                intelligence_count = intelligence
                the_smartest_superhero = hero_name
    # print(the_smartest_superhero)
    return the_smartest_superhero

if __name__ == '__main__':
    assert get_the_smartest_superhero(superheros) == 'Ant-Man'