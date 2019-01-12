import requests
from urllib.parse import urlencode

def get_page(offset):
    params = {
        'offset' : offset,
        'format' : 'json',
        'keyword': '街拍',
        'autoload' : 'true',
        'count' : 20,
        'cur_tab' : 1,
        'from' : 'search_tab',
        'pd' : 'synthesis'

    }
    url = 'https://www.toutiao.com/search/?' + urlencode(params)

    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
    except ConnectionError:
        return

if __name__ == '__main__':
    print(get_page(0))