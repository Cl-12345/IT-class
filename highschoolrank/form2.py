import matplotlib.pyplot as plt
import pandas as pd

tsin = []
bei = []
form = pd.read_excel('rank3.xlsx', sheet_name=None)
for i, df in form.items():
    print(i, df)
exit(0)
cnt = 0
for school in form['学校']:
    cnt += 1
    if school == '清华大学':
        tsin.append(cnt)
    elif school == '北京大学':
        bei.append(cnt)

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

plt.figure(figsize=(10, 5))
plt.plot(year, tsin, 'o-', linewidth=2, label='清华大学', color='#6A0DAD')
plt.plot(year, bei, 's-', linewidth=2, label='北京大学', color='#C41E3A')

plt.xlabel('年份', fontsize=11)
plt.ylabel('排名', fontsize=11)
plt.title('2016-2025年 清华大学与北京大学排名变化', fontsize=13)
plt.gca().invert_yaxis()
plt.yticks(range(1, 3))
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()

for x, y in zip(year, tsin):
    plt.text(x, y, str(y), ha='center', va='bottom', fontsize=9)
for x, y in zip(year, bei):
    plt.text(x, y, str(y), ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()