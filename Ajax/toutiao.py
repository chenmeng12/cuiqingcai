import requests
from urllib import parse
import json

def get_page(offset):
    params = {
        'offset':offset,
        'format':'json',
        'keyword':'街拍',
        'autoload':'true',
        'count':20,
        'cur_tab':1,
        'from':'search_tab',
        'pd':'synthesis'

    }
    url = 'https://www.toutiao.com/search_content/?' + parse.urlencode(params)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except ConnectionError:
        return None


if __name__ == '__main__':
    for item in get_page(0)['data']:
        title = item.get('title')
        for image in item['image_list']:
            print(image['url'])
