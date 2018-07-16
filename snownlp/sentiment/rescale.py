#!/usr/bin/env python 
# -*- coding:utf-8 -*-

import pandas as pd
from snownlp.sentiment import plot
from snownlp import SnowNLP

all_data = []
sentence_score =[]
filename = "/Users/liumingrui/unique3.txt"

f = open(filename,'r')
for line in open(filename):
    line = f.readline()
    s = SnowNLP(line)
    score = s.sentiments
    all_data.append(score)

    sentence_score.append([line,score])

csv_pd = pd.DataFrame(sentence_score)
csv_pd.to_csv("all_data_3.0.csv", sep=',', header=False, index=False)


plot.drawHist(sentence_score[1])
plot.stat(sentence_score[1])