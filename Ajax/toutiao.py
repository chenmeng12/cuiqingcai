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

def get_image(json):
    if json.get('data'):
        for item in json.get('data'):
            if item.get('cell_type') is not None:
                continue
            title = item.get('title')
            images = item.get('image_list')
            for image in images:
                yield {
                    'image':image.get('url'),
                    'title':title
                }

if __name__ == '__main__':
    for i in get_image(get_page(0)):
        print(i)
