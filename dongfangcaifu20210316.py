from selenium import webdriver
import re
import time
def dongfang(company):
    chrome_options = webdriver.ChromeOptions()  # 设置无界面浏览器设置
    chrome_options.add_argument('--headless')
    browser = webdriver.Chrome(options=chrome_options)
    url = 'http://so.eastmoney.com/Web/s?keyword='+company
    browser.get(url)
    time.sleep(1)
    data = browser.page_source
    browser.quit()

    p_title = '<div class="news-item"><h3><a href=".*?">(.*?)</a>'
    p_href = '<div class="news-item"><h3><a href="(.*?)">.* ?</a>'
    p_date = '<p class="news-desc">(.*?)</p>'
    title = re.findall(p_title, data)
    href = re.findall(p_href, data)
    date = re.findall(p_date, data, re.S)

    for i in range(len(title)):
        title[i] = re.sub('<.*?>', '', title[i])
        date[i] = date[i].split(' ')[0]
        print(str(i+1)+'.'+title[i]+'-----'+date[i])
        print(href[i])
        
companys = ['招商银行', '阿里巴巴', '三友化工', '晨鸣纸业', '腾讯控股']
for i in companys:
    try:
        dongfang(i)
        print(i+'该公司东方财富网爬取成功')
    except:
        print(i+'该公司东方财富网爬取失败')