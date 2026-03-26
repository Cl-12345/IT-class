dicts = dict()

with open('dict.txt', 'r', encoding='utf-8') as f:
    s = f.readlines()
    for i in s:
        dicts[i.split()[0].lower()] = i.split()[1:]
# print(dicts)
while True:
    k = input('请输入你要查找的单词（英文），退出请输入exit：').strip().lower()
    if k == 'exit':
        break
    elif dicts.get(k):
        print(f'这个单词的中文意思是：{''.join('\n' + i for i in dicts.get(k))}')
    else:
        print('抱歉，没找到这个单词。')
    
