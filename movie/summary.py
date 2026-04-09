import jieba
from jieba import posseg
import os, re
import wordcloud
from matplotlib import pyplot as plt
def get_word(cl):
    global sorted_d_desc
    ans = ''
    for i in sorted_d_desc:
        if str(i[0]).split('/')[1] == cl:
            ans += str(i[0]).split('/')[0] * i[1]
    wc = wordcloud.WordCloud(font_path='d:/cl/project/movie/zhao.ttf', #如果是中文必须要添加这个，否则会显示成框框
               background_color='#FFF0F5',
               width=1000,
               height=800,
               ).generate(ans)
    wc.to_file('aaa.jpg')
    plt.imshow(wc)  #用plt显示图片
    plt.axis('off') #不显示坐标轴
    plt.show() #显示图片


dic = {}

def remove_punctuation(text):
    pattern = re.compile(r'[^\w\s]', re.UNICODE)
    return re.sub(pattern, '', text)
os.chdir('comments')
for file in os.listdir():
    with open(file, 'r', encoding='utf-8') as f:
        k = f.readlines()
        str_ = ''.join(i for i in k)
        words = posseg.cut(remove_punctuation(str_))
        for i in words:
            if i not in dic:
                dic[i] = 0 
            dic[i] += 1
sorted_d_desc = sorted(dic.items(), key=lambda x: x[1], reverse=True)
get_word('nr')


