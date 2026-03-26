import sqlite3, get_dict

def create():
    c.execute(
        '''
        CREATE TABLE DICTS
        (
        ID INT PRIMARY KEY  NOT NULL,
        word CHAR(50) NOT NULL,
        meanings CHAR(200) NOT NULL,
        correct_rate REAL,
        times INT
        );
        '''
    )

def add_word(word: str, meaning: str):
    c.execute()
def add():
    
    pass
dic = sqlite3.connect('dict.db')
c = dic.cursor()
c.execute('SELECT MAX(ID) from DICTS')
id = c.fetchone()
if not id:
    id = 0
add()
dic.commit()
dic.close()