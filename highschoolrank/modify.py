# ============================================================
# 程序 1：数据预处理
# 从 rank.xlsx 读取 2016–2026 年数据
# 训练集：2016–2023（8年），验证集：2024–2026（3年）
# 每个学校保存为 CSV（列：年份, 排名），带表头
# ============================================================

import os
import pandas as pd

os.makedirs('data/train', exist_ok=True)
os.makedirs('data/val', exist_ok=True)

all_years = list(range(2016, 2027))  # 2016–2026
all_data = []

for year in all_years:
    try:
        df = pd.read_excel('rank.xlsx', sheet_name=f'{year}年')
        df['年份'] = year
        all_data.append(df[['学校', '排名', '年份']])
        print(f"✔ 读取 {year} 年数据")
    except Exception as e:
        print(f"✖ 读取 {year} 年数据失败：{e}")

if not all_data:
    raise ValueError("未读取到任何数据，请检查 rank.xlsx")

data = pd.concat(all_data, ignore_index=True)

# 划分年份
train_years = list(range(2016, 2024))  # 2016–2023
val_years = [2024, 2025, 2026]         # 近3年

schools = data['学校'].unique()
for school in schools:
    school_data = data[data['学校'] == school].sort_values('年份')
    train_data = school_data[school_data['年份'].isin(train_years)][['年份', '排名']]
    val_data = school_data[school_data['年份'].isin(val_years)][['年份', '排名']]

    if len(train_data) >= 2:
        train_data.to_csv(f'data/train/{school}.csv', index=False, header=True, sep=',')
        print(f"训练集：{school}，{len(train_data)} 条")
    else:
        print(f"⚠ 跳过 {school}（训练数据不足 2 条）")
        continue

    if len(val_data) >= 1:
        val_data.to_csv(f'data/val/{school}.csv', index=False, header=True, sep=',')
        print(f"验证集：{school}，{len(val_data)} 条")
    else:
        print(f"⚠ {school} 无验证数据")

print("数据预处理完成。")