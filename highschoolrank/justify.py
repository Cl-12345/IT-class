# ============================================================
# 程序 3：验证模型（仅 R²）
# 用 2024–2026 年数据计算每个学校的 R²
# 输出每个学校的 R²、样本数，并解释 R² 为负或 NaN 的含义
# ============================================================

import os
import pandas as pd
import numpy as np
from BaseML import Regression as reg

def validate_all():
    val_dir = 'data/val'
    model_dir = 'checkpoints'
    results = []

    for filename in os.listdir(val_dir):
        if not filename.endswith('.csv'):
            continue
        school = filename[:-4]
        val_path = os.path.join(val_dir, filename)
        model_path = os.path.join(model_dir, f'{school}.pkl')

        if not os.path.exists(model_path):
            print(f"⚠ 跳过 {school}：模型不存在")
            continue

        try:
            model = reg()
            model.load(model_path)
            val_df = pd.read_csv(val_path)
            X_val = val_df[['年份']].values
            y_true = val_df['排名'].values
            y_pred = model.inference(X_val).flatten()

            n = len(y_true)
            # 计算 R²（样本数≥2才有效）
            if n >= 2:
                ss_res = np.sum((y_true - y_pred) ** 2)
                ss_tot = np.sum((y_true - np.mean(y_true)) ** 2)
                if ss_tot > 0:
                    r2 = 1 - ss_res / ss_tot
                else:
                    r2 = np.nan  # 总平方和为0（所有真实值相同）
            else:
                r2 = np.nan      # 样本数不足2，无法计算

            results.append({'学校': school, '样本数': n, 'R²': r2})
            print(f"✔ {school}：样本数={n}，R²={r2:.4f}" if not np.isnan(r2) else f"✔ {school}：样本数={n}，R²=NaN")

        except Exception as e:
            print(f"✖ {school} 验证失败：{e}")

    # 输出汇总
    if results:
        df = pd.DataFrame(results)
        print("\n" + "="*60)
        print("📊 各学校 R² 明细 (验证集：2024–2026)")
        print("="*60)
        print(df.to_string(index=False))

        # 解释 R² 为负或 NaN 的情况
        print("\n" + "="*60)
        print("📖 R² 含义说明")
        print("="*60)
        print("• R² 取值范围：(-∞, 1]")
        print("• R² = 1 ：完美预测")
        print("• R² = 0 ：预测效果等同于直接用均值")
        print("• R² < 0 ：模型预测比直接用均值还差")
        print("• R² = NaN ：样本数 < 2 或真实值方差为 0")
        print("\n本次验证中：")
        neg_r2 = df[df['R²'] < 0]
        nan_r2 = df[df['R²'].isna()]
        if not neg_r2.empty:
            print(f"⚠ 有 {len(neg_r2)} 个学校的 R² 为负，分别是：{', '.join(neg_r2['学校'])}")
        else:
            print("✅ 没有 R² 为负的学校。")
        if not nan_r2.empty:
            print(f"⚠ 有 {len(nan_r2)} 个学校的 R² 为 NaN，分别是：{', '.join(nan_r2['学校'])}")
        else:
            print("✅ 没有 R² 为 NaN 的学校。")
    else:
        print("没有验证结果。")

if __name__ == '__main__':
    validate_all()