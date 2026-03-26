import sqlite3, get_dict

def create():
    c.execute(
        '''
        CREATE TABLE IF NOT EXISTS DICTS
        (
        ID INT PRIMARY KEY  NOT NULL,
        word TEXT NOT NULL,
        meanings TEXT NOT NULL,
        correct_rate REAL,
        times INT
        );
        '''
    )
    dic.commit()

def add_word_if_not_existed(word: str, meaning: list):
    mean = ''
    word = word.strip()
    for i in meaning:
        mean += i.strip() + '#'
    c.execute(f'SELECT 1 from DICTS where word = {word}')
    a = c.fetchone()
    print(a)
    c.execute(f"INSERT INTO DICTS (word,meanings) \
      VALUES ({word}, {mean})")
    id += 1
def add():
    dic = get_dict.get()
    for i in (dic.items()):
        add_word_if_not_existed(i[0], i[1])

dic = sqlite3.connect('dict.db')
c = dic.cursor()
create()
c.execute('SELECT MAX(ID) from DICTS')

id = c.fetchone()
if not id:
    id = 0
add()
dic.commit()
dic.close()
