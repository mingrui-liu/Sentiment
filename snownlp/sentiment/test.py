#!/usr/bin/env python
# -*- coding:utf-8 -*-
from snownlp import SnowNLP
import time
import pandas as pd
import jieba

jieba.load_userdict("分词.txt")
f = list(open("/Users/liumingrui/Documents/IBM/test(1).txt"))
p = open("/Users/liumingrui/Documents/IBM/test_result/positive_pureTxt.txt","w")
m = open("/Users/liumingrui/Documents/IBM/test_result/moderate_pureTxt.txt","w")
sn = open("/Users/liumingrui/Documents/IBM/test_result/slightly negative_pureTxt.txt","w")
n = open("/Users/liumingrui/Documents/IBM/test_result/negative_pureTxt.txt","w")

for row in f:
    if row != '\n':
        text = str(row).strip('\n')

    s = SnowNLP(text)
    start = time.clock()
    score = s.sentiments
    neg = []
    if score >0.6:
        #print("The sentiment of %s is %f : positive" % (text, score))
        p.write("%s\n" % text)
    elif score <= 0.55 and score > 0.3:
        #print("The sentiment of %s is %f : moderate" % (text, score))
        m.write("The sentiment of %s is %f : moderate\n" % (text, score))

    elif score <= 0.30 and score >0.149:
        #print("The sentiment of %s is %f : slightly negative" % (text, score))
        sn.write("%s\n"%text)
        #neg.append(row)
    elif score <= 0.149:
        #print("The sentiment of %s is %f : negative" % (text, score))
        n.write("%s\n"%text)
        #neg.append(row)

    elapsed = (time.clock() - start)
    # print("Time used :", elapsed)

#csv_pd = pd.DataFrame(neg)
#csv_pd.to_csv("negtest.csv", sep=',', header=False, index=False)
