import requests
from pprint import pprint


heroes_str = 'Hulk, Captain America, Thanos'
heroes_list = heroes_str.split(', ')
the_smartest_superhero = ''
intelligence_count = 0
url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
all_heroes_info = requests.get(url).json()
for hero_info in all_heroes_info:
    hero_name = hero_info.get('name')
    if hero_name in heroes_list:
        intelligence = hero_info['powerstats']['intelligence']
        if intelligence_count < intelligence :
            intelligence_count = intelligence
            the_smartest_superhero = hero_name
print(f'Интелект у {the_smartest_superhero}: {intelligence_count}')


# def get_the_smartest_superhero() -> str:
#     heroes_str = 'Hulk, Captain America, Thanos'
#     heroes_list = heroes_str.split(', ')
#     the_smartest_superhero = ''
#     intelligence_count = 0
#     url = 'https://cdn.jsdelivr.net/gh/akabab/superhero-api@0.3.0/api/all.json'
#     all_heroes_info = requests.get(url).json()
#     for hero_info in all_heroes_info:
#         hero_name = hero_info.get('name')
#         if hero_name in heroes_list:
#             intelligence = hero_info['powerstats']['intelligence']
#             if intelligence_count < intelligence :
#                 intelligence_count = intelligence
#                 the_smartest_superhero = hero_name
#     return the_smartest_superhero