# ============================================================
# 程序 2：训练模型并预测 2029 年排名
# 对每个学校训练线性回归模型，保存到 checkpoints/，并输出 2029 年预测前 10
# ============================================================

import os
import pandas as pd
import numpy as np
from BaseML import Regression as reg

def train_all_and_predict():
    os.makedirs('checkpoints', exist_ok=True)
    train_dir = 'data/train'
    pred_list = []

    for filename in os.listdir(train_dir):
        if not filename.endswith('.csv'):
            continue
        school = filename[:-4]
        train_path = os.path.join(train_dir, filename)

        try:
            model = reg(algorithm='LinearRegression')
            model.load_tab_data(train_path)   # 自动识别表头
            model.train()
            model.save(f'checkpoints/{school}.pkl')
            print(f"✔ 训练完成：{school}")
        except Exception as e:
            print(f"✖ {school} 训练失败：{e}")
            continue

        try:
            pred_rank = model.inference([[2029]])[0]
            pred_list.append((school, pred_rank))
            print(f"   → 预测 2029 排名：{pred_rank:.2f}")
        except Exception as e:
            print(f"   ✖ {school} 预测失败：{e}")

    return pred_list

if __name__ == '__main__':
    preds = train_all_and_predict()
    if preds:
        df = pd.DataFrame(preds, columns=['学校', '2029年预测排名'])
        top10 = df.sort_values('2029年预测排名').head(10)
        print("\n" + "="*50)
        print("预测的 2029 年大学排名前 10 榜单")
        print("="*50)
        for i, row in top10.reset_index(drop=True).iterrows():
            print(f"第 {i+1} 名: {row['学校']} (预测排名: {row['2029年预测排名']:.2f})")
    else:
        print("没有成功预测任何学校。")