from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import html

web = webdriver.Edge()

web.get(f'https://www.shanghairanking.cn/rankings/bcur/2026')

import time 

# time.sleep(3)

ord = web.find_elements(By.XPATH, '//span[@data-v-389300f0 and @class="sort-normal"]')[1]
ord.click()
ord.click()

ele = web.find_elements(By.XPATH, '//ul[@class="options"]')[3]
a = ele.find_elements(By.XPATH, './/li')
asp = []
for i in a:
    asp.append(i.get_attribute('textContent'))

doc = html.fromstring(web.page_source)
_schools = doc.xpath('//td[@class="align-left"]//span[@class="name-cn"]')

for i in a:
    i.click()
    print(i.get_attribute('testContent'))
    for i in _schools:
        print(i.text.strip())
    time.sleep(2)

tsi = []
bei = []


time.sleep(2)
web.close()