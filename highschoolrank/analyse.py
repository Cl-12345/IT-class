from lxml import html
import pandas as pd

year = [_ for _ in range(2016, 2027)]
with pd.ExcelWriter('rank.xlsx', engine='openpyxl', ) as xls:
    for i in year:
        with open(f'{i}.html', 'r', encoding='utf-8') as f:
            # print(''.join(i for i in f.readlines()))
            doc = html.fromstring(''.join(i for i in f.readlines()))
            _schools = doc.xpath('//td[@class="align-left"]//span[@class="name-cn"]')
            mess = doc.xpath('//table[@class="rk-table"]//tbody//tr')
            stu = []
            subject = []
            grade = []
            for j in mess:
                subject.append(j[3].text.strip())
                grade.append(j[4].text.strip())
                stu.append(j[5].text.strip())
            # xls.close()
            schools = []

            for j in _schools:
                schools.append(j.text.strip())
            form = pd.DataFrame({
                '排名': [i for i in range(1, len(schools) + 1)],
                '学校': schools,
                '评分': grade, 
                '主要学科': subject,
                '生源质量': stu,
            })
            
            form.to_excel(xls, sheet_name=f'{i}年', index=False)
