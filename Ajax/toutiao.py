import requests
from urllib import parse
import json, os
from hashlib import md5
from requests import codes
from multiprocessing.pool import  Pool

def get_page(offset):
    params = {
        'offset': offset,
        'format': 'json',
        'keyword': '街拍',
        'autoload': 'true',
        'count': 20,
        'cur_tab': 1,
        'from': 'search_tab',
        'pd': 'synthesis'

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
                    'image': image.get('url'),
                    'title': title
                }


def save_image(item):
    img_path = 'img' + os.path.sep + item.get('title')
    if not os.path.exists(img_path):
        os.makedirs(img_path)
        try:
            response = requests.get('https:' + item.get('image'))
            if codes.ok == response.status_code:
                file_path = img_path + os.path.sep + '{file_name}.{file_suffix}'.format(
                    file_name=md5(response.content).hexdigest(),
                    file_suffix='jpg'
                )
                if not os.path.exists(file_path):
                    with open(file_path, 'wb') as f:
                        f.write(response.content)
                    print('Download image path is %s' % file_path)
                else:
                    print('Already Download', file_path)
        except requests.ConnectionError:
            print('Failed to Save Image %s' % item)


def main(offset):
    json = get_page(offset)
    for item in get_image(json):
        print(item)
        save_image(item)

GROUP_SRTAE = 1
GROUP_END = 20

if __name__ == '__main__':
    pool = Pool()
    groups = ([x * 20 for x in range(GROUP_SRTAE, GROUP_END + 1)])
    pool.map(main, groups)
    pool.close()
    pool.join()
