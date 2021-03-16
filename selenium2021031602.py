from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
browser.find_element_by_css_selector('#kw').clear()  # 默认清空下输入框
browser.find_element_by_css_selector('#kw').send_keys('python')
browser.find_element_by_css_selector('#su').click()
time.sleep(5)
data = browser.page_source
print(data)
