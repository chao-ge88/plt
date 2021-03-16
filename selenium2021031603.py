from selenium import webdriver
chrome_options = webdriver.ChromeOptions()  # 设置无界面浏览器设置
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(options=chrome_options)
browser.get('http://finance.sina.com.cn/realstock/company/sh000001/nc.shtml')
data = browser.page_source
print(data)
