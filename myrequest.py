import requests

URL = 'http://github.com/favicon.ico'
data = {'name' : "Jack", 'age':22}
URL1 = 'http://httpbin.org/post'
r = requests.get(URL)
print(r.__doc__)
# with open('github.ico', 'wb') as f:
#     f.write(r.content)

r1 = requests.post(URL1, data=data)
print(r.text.decode('utf-8').encode('gbk'))