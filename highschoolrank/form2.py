import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

file_path = 'rank3.xlsx'
xl = pd.ExcelFile(file_path)

uni1 = '清华大学'
uni2 = '北京大学'

all_ranks = []
dimension_data = []

for sheet_name in xl.sheet_names:
    df = pd.read_excel(xl, sheet_name=sheet_name)
    # get sheet
    df.columns = ['排名', '学校']
    # get specific data
    df['学校'] = df['学校'].astype(str).str.strip()
    rank1 = df.loc[df['学校'] == uni1, '排名'].values
    rank2 = df.loc[df['学校'] == uni2, '排名'].values
    # get ranks
    if len(rank1) > 0 and len(rank2) > 0:
        dimension_data.append((sheet_name, rank1[0], rank2[0]))
        all_ranks.append(rank1[0])
        all_ranks.append(rank2[0])
        # data collect

max_rank = max(all_ranks)
# reverse rank to guarantee the higher rank is higher in graph
base = max_rank + 1

dimensions = [d[0] for d in dimension_data]
ranks1 = [d[1] for d in dimension_data]
ranks2 = [d[2] for d in dimension_data]
scores1 = [base - r for r in ranks1]
scores2 = [base - r for r in ranks2]

x = np.arange(len(dimensions))
width = 0.35
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.bar(x - width/2, scores1, width, label=uni1, color='#1f77b4')
plt.bar(x + width/2, scores2, width, label=uni2, color='#ff7f0e')
# seperate two columns

plt.ylabel('排名得分')

plt.ylim(0, max(scores1+scores2) * 1.1)
plt.title(f'{uni1} vs {uni2} - 各维度排名优势对比')
# pretend borders from cover the labels
plt.xticks(x, dimensions, rotation=45, ha='right')
plt.legend()

for i, (s, r) in enumerate(zip(scores1, ranks1)):
    plt.text(i - width/2, s + 0.3, f'{s}({r})', ha='center', va='bottom', fontsize=8)
for i, (s, r) in enumerate(zip(scores2, ranks2)):
    plt.text(i + width/2, s + 0.3, f'{s}({r})', ha='center', va='bottom', fontsize=8)
# set the labels

# plt.tight_layout()
plt.savefig('form2.png')

plt.show()