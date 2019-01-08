import requests

url = 'http://httpbin.org/cookies/set/number/123456789'
url1 = 'http://httpbin.org/cookies'
url2 = 'https://www.12306.cn'
url3 = 'https；//www.taobao.com'
url4 = 'http://httpbin.org/post'
# s = requests.Session()
# s.get(url)
# r = s.get(url1)
# print(r.text)

# r = requests.get(url2)
# print(r.status_code)
# print(r.request)

# p = {
#     'http':'http://10.10.1.10:3128',
#     'https':'http://10.10.1.10:1080'
# }

# requests.get(url3, proxies=proxies)

data = {
    'name':'germay'
}
header = {
    'User-Agent ' : 'Mozilla/s.o (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53 .0.2785.116 Safari/537 .36'

}
s = requests.Session()
req = requests.Request('POST', url4, data=data, headers=header)
prepped = s.prepare_request(req)
r = s.send(prepped)
print(r.text)
