import requests
from pprint import pprint

url = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
token = ''
lang = 'ru-en'

def translate_word(word):
    params = {
        'key': token,
        'lang': lang,
        'text': word,
        'ui': 'ru'
    }
    trans_word = requests.get(url, params=params).json()['def'][0]['tr'][0]['text']
    # pprint(trans_word)
    return trans_word

print(translate_word('машина'))

# if __name__ == '__main__':
#     word = 'машина'
#     assert translate_word(word) == 'car'