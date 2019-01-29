from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
brower = webdriver.Chrome()
keyword = 'iPad'
wait = WebDriverWait(brower, 10)

url = 'https://s.taobao.com/search?q='+quote(keyword)

brower.get(url)
