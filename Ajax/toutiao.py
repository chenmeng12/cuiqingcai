import requests
from urllib import parse

def get_page(offset):
    params = {
        'offset':offset,

    }