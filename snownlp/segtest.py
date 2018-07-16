#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from snownlp import SnowNLP

import jieba
jieba.load_userdict("分词.txt")

text = input()
allchat =[]
while text != "结束":
    allchat.append(text)
    print("The jieba segment of %s is %s" % (text, list(jieba.cut(text))))
    print("The jieba segment of %s is %s"%(text,list(jieba.cut(text,cut_all=True))))
    print("The jieba segment of %s is %s" % (text, list(jieba.cut_for_search(text))))
    text = input()