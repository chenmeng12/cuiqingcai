from urllib.parse import urlparse
from urllib import parse
URL = 'www.baidu.com/index.html;user?id=5#conmment'
import urllib

result = urlparse(URL,scheme='https')
print(type(result), result, sep='\n')

params = {
    'name':'Jack',
    'age':22
}

base_url = 'https://www.baidu.com?'
url = base_url+parse.urlencode(params)
print(url)

query = 'name=Jack&age=22'
print(parse.parse_qs(query))
print(parse.parse_qsl(query))

keys = '壁纸'
url1 = 'https://www.baidu.com/?wd=' + parse.quote(keys)
url2 = parse.quote('https://www.baidu.com?wd=壁纸')
print(url2)
print(url1)
print(parse.unquote(url1))