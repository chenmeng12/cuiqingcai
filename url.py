import urllib.parse
import urllib


# data = bytes(urllib.parse.urlencode({'hello':'world'}), encoding='utf8')
# response =urllib.request.urlopen('http://httpbin.org/post', data = data)

# print(response.read())

data = urllib.request.Request(url='http://python.org')
response = urllib.request.urlopen(data)

print(response.read())