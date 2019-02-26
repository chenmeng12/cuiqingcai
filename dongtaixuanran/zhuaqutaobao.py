from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib.parse import quote
from pyquery import PyQuery as pq
from pymongo import MongoClient

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(browser, 100)
KEYWORD = 'iPad'
MONGO_URL = 'localhost'
MONGO_DB = 'taobao'
MONGO_COLLECTION = 'products'
client = MongoClient(MONGO_URL)
db = client[MONGO_DB]
MAX_PAGE = 100

def index_page(page):
    """
    抓取索引页
    :param page:页码
    :return:
    """
    print('正在抓取第', page, '页')
    try:
        url = 'https://s.taobao.com/search?q=' + quote(KEYWORD)
        browser.get(url)
        if page > 1:
            input = wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#mainsrp-page div.form > input'))
            )
            submit = wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, '#mainsrp-page div.form > span.btn.J_Submit'))
            )
            input.clear()
            input.send_keys(page)
            submit.click()
        wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#mainsrp-page li.item.active > span'), str(page))
        )
        wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'm-itemlist .items .item')))
        get_products()
    except TimeoutException:
        index_page(page)

def get_products():
    """
    提取商品数据
    :return:
    """
    html = browser.page_source()
    doc = pq(html)
    items = doc('#mainsrp-item. items .item').items()
    for item in items:
        product = {
            'image' : item.find(' .pic .img').attr('data-src'),
            'price' : item.find('.pricc').text(),
            'deal' : item.find('.deal-cnt').text(),
            'title' : item.find('title').text(),
            'shop' : item.find('.shop').text(),
            'location' : item.find('.location').text()
        }
        print(product)
        save_to_mongo(product)

def save_to_mongo(result):
    """
    保存至Mongodb
    :param result:结果
    :return:
    """
    try:
        if db[MONGO_COLLECTION].insert(result):
            print('存储到Mongodb成功')
    except Exception:
        print('存储到Mongodb失败')

def main():
    """
    遍历每一页
    :return:
    """
    for i in range(1, MAX_PAGE + 1):
        index_page(i)

if __name__ == '__main__':
    main()
