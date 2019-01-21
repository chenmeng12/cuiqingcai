from selenium import webdriver
import traceback
import time

# brower  = webdriver.Chrome()
# brower.get('https://www.taobao.com')
# print(brower.page_source)
# try:
#     first = brower.find_element_by_id('q')
#     second = brower.find_element_by_css_selector('#q')
#     # third = brower.find_element_by_xpath('//*[id="q"]')
#     print(first, second)
#     brower.close()
# except Exception:
#     traceback.print_exc()
#     brower.close()

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# brower = webdriver.Chrome()
# url = 'https://www.taobao.com'
# brower.get(url)
# wait = WebDriverWait(brower, 10)
# input = wait.until(EC.presence_of_all_elements_located((By.ID, 'q')))
# button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn-search')))
# print(input, button)

# from selenium import webdriver
#
# brower = webdriver.Chrome()
# brower.get('http://www.zhihu.com/explore')
# print(brower.get_cookies())
# brower.add_cookie({'name':'name', 'domain':'www.zhihu.com', 'value':'germey'})
# print(brower.get_cookies())
# print(brower.delete_all_cookies())
# print(brower.get_cookies())

brower = webdriver.Chrome()
brower.get('https://www.baidu.com')
brower.execute_script('window.open()')
print(brower.window_handles)
brower.switch_to.window(brower.window_handles[1])
brower.get('https://www.taobao.com')
time.sleep(1)
brower.switch_to.window(brower.window_handles[0])
brower.get('https://python.org')

brower.close()