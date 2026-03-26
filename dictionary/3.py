import sqlite3, get_dict

def create():
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS DICTS
        (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        word TEXT NOT NULL,
        meanings TEXT NOT NULL,
        correct_rate REAL,
        times INT
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

def ui():
    print('欢迎使用单词错题本！')
    print('请输入你的操作：')
    
def main():
    ui()



dic = sqlite3.connect('dict.db')
c = dic.cursor()
create()

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