from lxml import html
import pandas as pd

schools = [
    'tsinghua-university',
    'peking-university',
]
with pd.ExcelWriter('rank2.xlsx', engine='openpyxl', ) as xls:
    for i in schools:
        with open(f'{i}.html', 'r', encoding='utf-8') as f:
            # print(''.join(i for i in f.readlines()))
            doc = html.fromstring(''.join(i for i in f.readlines()))
            datas = doc.xpath('//div[@class="all-subj"]//div[@class="table-container"]//table[@data-v-6f721d4e]//tbody//tr[@data-v-6f721d4e]')
            ids = []
            subject = []
            grade = []
            rank = []    
            for j in datas:
                ids.append(j[0].text.strip())
                subject.append(j[1].text.strip())
                grade.append(j[2].text.strip())
                rank.append(int(j[3].text.strip()))
                form = pd.DataFrame({
                    '编号': [i for i in range(1, len(ids) + 1)],
                    '专业编号': ids,
                    '专业名称': subject, 
                    '评级': grade,
                    '专业排名': rank,
                })
            
                form.to_excel(xls, sheet_name=f'{i}', index=False)
