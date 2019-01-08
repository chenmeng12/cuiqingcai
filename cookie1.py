import http.cookiejar, urllib.request

filename1 = 'cookie1.txt'
filename2 = 'cookie2.txt'
cookie = http.cookiejar.LWPCookieJar(filename2)
# cookie = http.cookiejar.MozillaCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True, ignore_expires=True)