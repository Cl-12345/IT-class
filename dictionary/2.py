import get_dict
import random

dicts = get_dict.get()
keys = list(dicts.keys())
while True:
    # try:
    op = int(input('请输入测试模式:\n1.单词练习\n2.单词测试\n3.退出\n'))
    if op == 1:
        ans = random.choice(keys)
        cn = dicts[ans]
        k = input(f'这个单词的英文是{''.join('\n' + i for i in cn)}\n请输入这个单词的英文：').strip().lower()
        print(k)
        if k == ans.strip():
            print('正确！')
        else:
            print(f'错误！答案是：{ans}')
    elif op == 2:
        n = int(input('请输入你测试单词个数（中途不会输出结果）：'))
        res = []
        out = []
        for i in range(n):
            ans = random.choice(keys)
            cn = dicts[ans]
            
            k = input(f'这个单词的英文是：{''.join('\n' + i for i in cn)}\n请输入这个单词的英文：').strip().lower()
            if k == ans:
                res.append(0)
                out.append(f'{ans} 正确')
            else:
                res.append(1)
                out.append(f'{k} 错误！答案： {ans}')
        print(f'正确率: {res.count(0) / n * 100} %')
        for i in out:
            print(i)
    elif op == 3:
        break
    else:
        print('请重新输入')
    # except:
    #     print('非法输入')
