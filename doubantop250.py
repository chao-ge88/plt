from selenium import webdriver
import re
import time
for p in range(11):

    chrome_options = webdriver.ChromeOptions()  # 设置无界面浏览器设置
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    url = 'https://movie.douban.com/top250?start='+str(25*p)+'&filter='
    browser.get(url)
    time.sleep(1)
    data = browser.page_source
    browser.quit()

    p_title = '<div class="hd">.*?>(.*?)</span>'
    p_href = '<div class="hd">.*?=(.*?) class="">'
    p_star = '<span class="rating_num" property="v:average">(.*?)</span>'
    title = re.findall(p_title, data, re.S)
    href = re.findall(p_href, data, re.S)
    star = re.findall(p_star, data, re.S)
    for i in range(len(title)):
        title[i] = title[i].strip()
        title[i] = re.sub('<.*?>', '', title[i])

    for i in range(len(title)):
        print(str(i+1)+'.'+title[i]+'--'+star[i])
        print(href[i])




