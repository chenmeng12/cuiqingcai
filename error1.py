import socket
from urllib import request, error

try:
    response = request.urlopen('https://www.baidu.com', timeout = 0.01)
except error.URLError as e:
    print(e.reason, type(e.reason),sep='\n')
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT', )