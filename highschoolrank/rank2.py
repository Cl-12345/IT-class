from selenium import webdriver

web = webdriver.Edge()


for i in range(2016, 2027):
    web.get(f'https://www.shanghairanking.cn/rankings/bcur/{i}')
    import time 
    time.sleep(5)
    text = web.page_source
    with open(f'{i}.html', 'w', encoding='utf-8') as f:
        f.write(text)

web.close()