from selenium import webdriver
import time
browser = webdriver.Chrome()
browser.maximize_window()
browser.get('https://www.baidu.com')
browser.find_element_by_xpath('//*[@id="kw"]').clear()
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('python')
browser.find_element_by_xpath('//*[@id="su"]').click()
time.sleep(3)  # 因为是单击后跳转，所以等待几秒再获取源代码
data = browser.page_source
print(data)
browser.quit()  # 完成网页源代码后退出模拟浏览器
