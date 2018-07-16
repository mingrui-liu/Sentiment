#!/usr/bin/env python
# -*- coding:utf-8 -*-

from math import log
import os


# 打开词典文件，返回列表
def open_dict(Dict='hahah'):
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                        '%s.txt' % Dict)
    dictionary = open(path, 'r', encoding='utf-8')
    dict = []
    for word in dictionary:
        word = word.strip('\n')
        dict.append(word)
    return dict


def judgeodd(num):
    if (num % 2) == 0:
        return 'even'
    else:
        return 'odd'


def change(self,word,z,k):#z表示往哪个方向改， k表示当前的标签
    y = self.d[k].freq(word)
    x = abs(self.d["pos"].freq(word) - self.d["neg"].freq(word))
    z = x
    n = 0
    while z<1:
        z*=10
        n+=1

    if (z==k):
        if(z=="pos"):
            y = self.d["pos"].freq(word) + x + 10**(-n)
        else:
            y = self.d["neg"].freq(word) + x + 10**(-n)
    return y


def sentiment_score_list(self, datalist, k):
    # 修改词语的情感倾向
    change_flag = False
    change_word = "奇怪"
    change_way ="pos"

    # 注意，这里你要修改path路径。
    deny_word = open_dict(Dict='否定词')
    posdict = open_dict(Dict='pos_word')
    negdict = open_dict(Dict='neg_word')

    degree_word = open_dict(Dict='程度级别词语')
    mostdict = degree_word[degree_word.index('extreme') + 1: degree_word.index('very')]  # 权重4，即在情感词前乘以3
    verydict = degree_word[degree_word.index('very') + 1: degree_word.index('more')]  # 权重3
    moredict = degree_word[degree_word.index('more') + 1: degree_word.index('ish')]  # 权重2
    ishdict = degree_word[degree_word.index('ish') + 1: degree_word.index('last')]  # 权重0.5
    i = 0  # 记录扫描到的词的位置
    a = 0  # 记录情感词的位置

    result = 0
    poscount = 0  # 积极词的第一次分值
    negcount = 0

    for word in datalist:
        y =self.d[k].freq(word)
        if change_flag == True:
            y = change(self,change_word,change_way,k)
        possibility = log(y)  # log（input里每个单词在正向或负向标签里出现的概率 ）
        print("possibility of",word,"in",k,"is",y)
        if word in posdict:  # 判断词语是否是情感词
            poscount += 1
            c = 0
            x = i - a
            if x > 2:
                x = 2
            for w in datalist[i - x:i]:  # 扫描情感词前的程度词
                if w in mostdict:
                    poscount *= 2.5
                elif w in verydict:
                    poscount *= 2.0
                elif w in moredict:
                    poscount *= 1.5
                elif w in ishdict:
                    poscount *= 0.95
                elif w in deny_word:
                    c += 1
            if judgeodd(c) == 'odd':  # 扫描情感词前的否定词数
                poscount *= -3
            a = i + 1  # 情感词的位置变化

        elif word in negdict:  # 消极情感的分析，与上面一致
            negcount += 1
            d = 0
            x = i - a
            if x > 2:
                x = 2
            for w in datalist[i - x:i]:
                if w in mostdict:
                    negcount *= 2.5
                elif w in verydict:
                    negcount *= 2.0
                elif w in moredict:
                    negcount *= 1.5
                elif w in ishdict:
                    negcount *= 0.95
                elif w in deny_word:
                    d += 1
            if judgeodd(d) == 'odd':
                negcount *= -3
            a = i + 1
        # elif word == '！' or word == '!':  ##判断句子是否有感叹号
        # for w2 in datalist[::-1]:  # 扫描感叹号前的情感词，发现后权值+2，然后退出循环
        # if w2 in posdict or negdict:
        # poscount3 += 2
        # negcount3 += 2
        # break
        i += 1  # 扫描词位置前移

        # 以下是防止出现负数的情况
        pos_count = 0
        neg_count = 0
        if poscount < 0 and negcount >= 0:
            neg_count += negcount - poscount
            pos_count = 0
        elif negcount < 0 and poscount >= 0:
            pos_count = poscount - negcount
            neg_count = 0
        elif poscount < 0 and negcount < 0:
            neg_count = -poscount
            pos_count = -negcount
        else:
            pos_count = poscount
            neg_count = negcount
        # print("poscount", pos_count)
        # print("negcount", neg_count)

        if k == "pos":
            possibility += pos_count
            # print("possibility of", word, "in", k, "is", possibility)
        elif k == "neg":
            possibility += neg_count
            # print("possibility of", word, "in", k, "is", possibility)
        result += possibility
    return result
