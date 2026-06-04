import matplotlib.pyplot as plt
import pandas as pd

year = [i for i in range(2016, 2026)]
tsin = []
bei = []
for i in year:
    form = pd.read_excel('rank.xlsx', sheet_name=f'{i}年')
    rank = {}
    cnt = 0
    for i in form['学校']:
        cnt += 1
        if i == '清华大学':
            tsin.append(cnt)
        elif i == '北京大学':
            bei.append(cnt)

    # break
print(bei, tsin)