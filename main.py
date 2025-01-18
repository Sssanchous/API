import requests
from urllib.parse import urlparse
from dotenv import load_dotenv
import os


SHORT_URL = 'https://api.vk.ru/method/utils.getShortLink'
COUNT_URL = 'https://api.vk.ru/method/utils.getLinkStats'


def is_shorten_link(token, url):
    parsed_url = urlparse(url)
    if parsed_url.netloc != 'vk.cc':
        return False

    params = {
        'access_token': token,
        'url': url,
        'v': '5.199'
    }

    response = requests.get(SHORT_URL, params)
    response.raise_for_status()
    short_link = response.json()

    return not(short_link['error'] == 'error')


def shorten_link(token, link):
    params = {
        'access_token': token,
        'url': link,
        'v': '5.199'
    }

    response = requests.get(SHORT_URL, params)
    response.raise_for_status()
    short_link = response.json()['response']['short_url']

    return short_link


def count_clicks(token, link):
    parsed_url = urlparse(link)
    params = {
       'access_token': token,
       'key': parsed_url.path[1:],
       'v': '5.199',
       'interval': 'forever'
    }

    response = requests.get(COUNT_URL, params)
    response.raise_for_status()
    counts_link = response.json()['response']['stats'][0]['views']

    return counts_link


if __name__ == "__main__":

    dotenv_path = os.path.join('short_link', 'token.env')
    load_dotenv(dotenv_path=dotenv_path)
    vk_token = os.environ['VK_TOKEN']

    user_input = input('Введите ссылку: ')

    try:
        if is_shorten_link(vk_token, user_input):
            clicks_count = count_clicks(vk_token, user_input)
            print('Количество кликов по ссылке: ', clicks_count)
        else:
            short_link = shorten_link(vk_token, user_input)
            print('Сокращённая ссылка: ', short_link)
    except requests.exceptions.HTTPError:
        print('Произошла ошибка при работе с API')
    except KeyError:
        print('Прозошла ошибка при обработке данных')
    except IndexError:
        print('Произошла ошибка при обработке данных')