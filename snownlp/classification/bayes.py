# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from snownlp.sentiment.NegationAndDegree import sentiment_score_list
import sys
import gzip
import marshal
from math import log, exp

from ..utils.frequency import AddOneProb


class Bayes(object):

    def __init__(self):
        self.d = {}
        self.total = 0

    def save(self, fname, iszip=True):
        d = {}
        d['total'] = self.total
        d['d'] = {}
        for k, v in self.d.items():
            d['d'][k] = v.__dict__
        if sys.version_info[0] == 3:
            fname = fname + '.3'
        if not iszip:
            marshal.dump(d, open(fname, 'wb'))
        else:
            f = gzip.open(fname, 'wb')
            f.write(marshal.dumps(d))
            f.close()

    def load(self, fname, iszip=True):
        if sys.version_info[0] == 3:
            fname = fname + '.3'
        if not iszip:
            d = marshal.load(open(fname, 'rb'))
        else:
            try:
                f = gzip.open(fname, 'rb')
                d = marshal.loads(f.read())
            except IOError:
                f = open(fname, 'rb')
                d = marshal.loads(f.read())
            f.close()
        self.total = d['total']
        self.d = {}
        for k, v in d['d'].items():
            self.d[k] = AddOneProb()
            self.d[k].__dict__ = v

    def train_first(self, data):
        for d in data:
            c = d[1]
            if c not in self.d:
                self.d[c] = AddOneProb()
            for word in d[0]:
                self.d[c].add(word, 1)
        self.total = sum(map(lambda x: self.d[x].getsum(), self.d.keys()))

    def train(self, data):
        self.load('sentiment.marshal')
        for d in data:
            c = d[1]
            if c not in self.d:
                self.d[c] = AddOneProb()
            for word in d[0]:
                self.d[c].add(word, 1)
        self.total = sum(map(lambda x: self.d[x].getsum(), self.d.keys()))



    #贝叶斯分类
    def classify(self, x):
        tmp = {}
        #遍历每个分类标签  （pos/neg)
        for k in self.d:
            #获取每个分类标签下的总词数和所有标签总词数，求对数差相当于log（某标签下的总词数/所有标签总词数）
            #得到每句话的正向或负向概率(得到这个标签的概率)
            tmp[k] = log(self.d[k].getsum()) - log(self.total)
            #print(k)
            #print("tem1",tmp[k] )


            tmp[k] += sentiment_score_list(self, x, k)
            #print("tem2", tmp[k])
            #for word in x:
                #possibility = log(self.d[k].freq(word))# log（input里每个单词在正向或负向标签里出现的概率 ）
                #tmp[k] += possibility    # 每句话的初始值加上每个单词的概率log(self.d[k].getsum()) - log(self.total)，得到整句话的正向或负向概率

        ret, prob = 0, 0  #ret 为 "pos" "neg"
        #print(k)
       # print("tem3", tmp[k])

        ##双层loop 判断这句话的正向概率比较大还是负向概率比较大
        for k in self.d:
            now = 0
            try:
                for otherk in self.d:
                    now += exp(tmp[otherk]-tmp[k])
                now = 1/now
            except OverflowError:
                now = 0
            if now > prob:
                ret, prob = k, now
        return (ret, prob) #return整句话的标签（pos/neg)和这个标签下的概率
