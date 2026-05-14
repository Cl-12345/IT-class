from selenium import webdriver

web = webdriver.Edge()

sch = 'peking-university'
web.get(f'https://www.shanghairanking.cn/institution/{sch}')

import time 

time.sleep(5)
text = web.page_source

with open(f'{sch}.html', 'w', encoding='utf-8') as f:
    f.write(text)

web.close()