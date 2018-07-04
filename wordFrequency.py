# - * - coding: utf - 8 -*-

import sys
import matplotlib.pyplot as plt
import FontCN_NLPtools as fts
import nltk
import pandas as pd

# 解决matplotlib 与 pandas 的乱码问题
import matplotlib as mpl

mpl.rcParams['font.sans-serif'] = ['KaiTi']
mpl.rcParams['font.serif'] = ['KaiTi']
# mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题,或者转换负号为字符串
import seaborn as sns

sns.set_style("darkgrid", {"font.sans-serif": ['KaiTi', 'Arial']})

reload(sys)
sys.setdefaultencoding('utf-8')
sys.path.append("../")

text_path = u'outcome.txt'  # 设置要分析的文本路径
stopwords_path = u'1.txt'  # 停用词词表

fontsTools = fts.FontCN_NLPtools(textPath=text_path, stopwordsPath=stopwords_path)

print
fontsTools.addUserWords([u'路明非'])
lztext = fontsTools.getText(isAddWord=True)

tokenstr = nltk.word_tokenize(lztext)
fdist1 = nltk.FreqDist(tokenstr)

listkey = []
listval = []

print u".........统计出现最多的前30个词..............."
for key, val in sorted(fdist1.iteritems(), key=lambda x: (x[1], x[0]), reverse=True)[:30]:
    listkey.append(key)
    listval.append(val)
    print key, val, u' ',

df = pd.DataFrame(listval, columns=[u'次数'])
df.index = listkey
df.plot(kind='bar')
plt.title(u'关于中美互加关税的词频统计')
plt.show()

posstr = fontsTools.jiebaCutStrpos(NewText=lztext)
strtag = [nltk.tag.str2tuple(word) for word in posstr.split()]

cutTextList = []
for word, tag in strtag:
    # 获取动词,在jieba采取和NLPIR兼容的的词性标注,对应关系我会贴在最后
    if tag[0] == "V":
        cutTextList.append(word)

tokenstr = nltk.word_tokenize(" ".join(cutTextList))

fdist1 = nltk.FreqDist(tokenstr)

listkey = []
listval = []

print
print u".........统计出现最多的前30个动词..............."
for key, val in sorted(fdist1.iteritems(), key=lambda x: (x[1], x[0]), reverse=True)[:30]:
    listkey.append(key)
    listval.append(val)
    print key, val, u' ',

df = pd.DataFrame(listval, columns=[u'次数'])
df.index = listkey
df.plot(kind='bar')
plt.title(u'关于龙族一中动词的词频统计')
plt.show()