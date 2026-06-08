from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import html
import pandas as pd

web = webdriver.Edge()

web.get(f'https://www.shanghairanking.cn/rankings/bcur/2026')

import time 

time.sleep(4)

ord = web.find_elements(By.XPATH, '//span[@data-v-389300f0 and @class="sort-normal"]')[1]
ord.click()
ord.click()


but = web.find_elements(By.XPATH, '//input[@type="text" and @readonly="readonly" and @placeholder="选择"]')[3]
but.click()
ele = web.find_elements(By.XPATH, '//ul[@class="options"]')[3]
a = ele.find_elements(By.XPATH, './/li')
asp = []
for i in a:
    asp.append(i.text.strip())
time.sleep(2)
but.click()


cnt = 0
with pd.ExcelWriter('rank3.xlsx', engine='openpyxl') as xls:
    for i in a:
        # time.sleep(3)
        but.click()
        time.sleep(2)
        i = ele.find_elements(By.XPATH, './/li')[cnt]
        sheetname = i.text
        i.click()
        doc = html.fromstring(web.page_source)
        _schools = doc.xpath('//td[@class="align-left"]//span[@class="name-cn"]')
        form = pd.DataFrame({
            '排名': [j for j in range(1, 1 + len(_schools))],
            '学校': [j.text.strip() for j in _schools],
        })
        # for i in _schools:
        #     print(i.text.strip())
        form.to_excel(xls, sheet_name=f'{sheetname}', index=False)
        time.sleep(3)
        cnt += 1

    tsi = []
    bei = []


time.sleep(2)
web.close()