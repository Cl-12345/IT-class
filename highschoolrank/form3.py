import pandas as pd
import matplotlib.pyplot as plt

file_path = 'rank2.xlsx'
sheets = ['tsinghua-university', 'peking-university']
unames = ['清华大学', '北京大学']
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.figure(figsize=(12, 5))

for i, (sheet, uname) in enumerate(zip(sheets, unames), 1):
    plt.subplot(1, 2, i)
    df = pd.read_excel(file_path, sheet_name=sheet)
    rating_counts = df['评级'].value_counts()
    print(dict(rating_counts))
    # return a dict with {grades: quatities}
    plt.pie(rating_counts, labels=rating_counts.index, autopct='%1.1f%%', startangle=90)
    plt.title(f'{uname} 专业评级分布')

plt.tight_layout()
plt.savefig('form3.png')
plt.show()