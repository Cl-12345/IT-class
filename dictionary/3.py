import sqlite3, get_dict, random

class my_dict:
    def __init__(self, id, mean, rate, times, wr):
        self.id = id
        self.meaning = ''.join(i + '\n' for i in mean.split('$'))
        self.wt = times if times else 0
        self.wr = wr if wr else 0
        self.cor = rate if rate else 0
        self.is_change = 0
    def __str__(self):
        return f'{self.id} {self.meaning} {self.cor} T{self.wt} F{self.wr}'


def create():
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS DICTS
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        meanings TEXT NOT NULL,
        correct_rate REAL,
        times INT,
        wrong_times INT
        );
        '''
    )
    dic.commit()

def add_word_if_not_existed(word: str, meaning: list):
    global id
    mean = ''
    word = word.strip()
    for i in meaning:
        mean += i.strip() + '$'
    c.execute('SELECT * from DICTS where word = ?', (word,))
    a = c.fetchone()
    if a:
        # print(a)
        return
    c.execute("INSERT INTO DICTS (word,meanings) VALUES (?, ?)", (word, mean,))
    # id += 1
def add():
    dic = get_dict.get()
    for i in (dic.items()):
        add_word_if_not_existed(i[0], i[1])

def test():
    n = 10
    for i in range(10):
        wei = [(i.cor + 1 if i.cor else 1) for i in dicts.values()]
        word = [str(i) for i in dicts.keys()]
        ans = random.choices(word, wei)[0]
        # print(k)
        # print(dicts)
        mea = dicts[ans]
        # print(mea)
        print(f'这个单词的中文是：\n{mea.meaning}')
        inp = input('请输入这个单词的英文：').strip()
        mea.is_change = True
        if inp != ans:
            mea.wr += 1
            mea.rate = mea.wt / (mea.wt + mea.wr)
            print(f'错误，错误次数{mea.wr}，正确率{mea.rate}，正确答案是{ans}\n\n\n')
        else:
            print('正确\n\n\n')
            mea.wt += 1
            mea.rate = mea.wt / (mea.wt + mea.wr)
def ui():
    print('欢迎使用单词错题本！')
    while True:
        print('请输入你的操作(数字)：')
        op = int(input(('1.测试\n2.错题本\n3.退出\n')))
        if op == 3:
            for i in dicts.values():
                if i.is_change:
                    c.execute('UPDATE DICTS SET correct_rate = (?), times = (?), wrong_times = (?) WHERE ID = (?)', (i.cor, i.wt, i.wr, i.id, ))
            return
        elif op == 1:
            test()
        elif op == 2:
            f = True
            for i in dicts.items():
                if i[1].wr:
                    print(f'{i[0]}: 错误次数{i[1].wr}，正确率{i[1].cor}\n意思：{i[1].meaning}')
                    f = False

            if (f):
                print('你还没有错题，请开始测试')

def init():
    c.execute('SELECT * FROM DICTS')
    words = c.fetchall()
    for i in words:
        dicts[i[1]] = my_dict(i[0], i[2], i[3], i[4], i[5])
def main():
    init()
    ui()



dic = sqlite3.connect('dict.db')
c = dic.cursor()
create()
add()
dicts = dict()

main()
dic.commit()
dic.close()

'''
四选二，可添加其他个性化功能

错题本通过文件记录统计错误的单词和其含义
每次程序重新运行都能知道之前错误的单词
每次出题时，错过的单词有较高概率被问到
输入“错题本”后，应能够输出错过的单词及出错次数
'''