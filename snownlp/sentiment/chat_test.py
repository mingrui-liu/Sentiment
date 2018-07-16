#!/usr/bin/env python
# -*- coding:utf-8 -*-
from snownlp import SnowNLP
import jieba
import time
import numpy as np
#jieba.load_userdict("/Users/liumingrui/Documents/IBM/银行业务词4.txt")




text = input('Enter: ')
allchat =[]
allscore = []
while text != "结束":
    allchat.append(text)
    s = SnowNLP(text)
    start = time.clock()
    score = s.sentiments
    allscore.append([score])
    if score >0.55:
        print("The sentiment of %s is %f : positive"% (text, score))
    elif score <= 0.55 and score > 0.3:
        print("The sentiment of %s is %f : moderate" % (text, score))
    elif score <= 0.30 and score >0.149:
        print("The sentiment of %s is %f : slightly negative" %( text, score))
    elif score <= 0.149:
        print("The sentiment of %s is %f : negative" % (text, score))

    elapsed = (time.clock()-start)
    print("Time used :",elapsed)

    text = input()

allscore_mean = np.mean(allscore)

if allscore_mean > 0.55:
    print("The sentiment of %s is %f : positive" % (text, allscore_mean))
elif allscore_mean <= 0.55 and allscore_mean > 0.3:
    print("The sentiment of %s is %f : moderate" % (text, allscore_mean))
elif allscore_mean <= 0.30 and allscore_mean > 0.149:
    print("The sentiment of %s is %f : slightly negative" % (text, allscore_mean))
elif allscore_mean <= 0.149:
    print("The sentiment of %s is %f : negative" % (text, allscore_mean))