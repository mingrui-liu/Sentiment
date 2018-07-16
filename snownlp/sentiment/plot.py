#!/usr/bin/env python 
# -*- coding:utf-8 -*-
from matplotlib import pyplot
import pandas as pd
import numpy as np

filename = "/Users/liumingrui/PycharmProjects/first_try/all_data_2.0.csv"
csv_data = pd.read_csv(filename, header=None)
data = np.array(csv_data)

print(type(data))
data2=[]


# 绘制直方图
def drawHist(heights):
    # 创建直方图
    # 第一个参数为待绘制的定量数据，不同于定性数据，这里并没有事先进行频数统计
    # 第二个参数为划分的区间个数
    pyplot.hist(heights, 70)
    pyplot.xlabel('Probability')
    pyplot.ylabel('Frequency')
    pyplot.title('Probability of Sentiment')
    pyplot.show()

for element in data:
    if element <= 0.5:
        #print(element)
        data2.append(element)
data2 = np.array(data2)
print(type(data2))

drawHist(data2)

def stat(data) :
    print("The mean sentiment is%f" % np.mean(data))
    print("The median sentiment is%f" % np.median(data))
    print("The max sentiment is%f" % max(data))
    print("The min sentiment is%f" % min(data))
    print("The 25 quartile sentiment is%f" % np.percentile(data, 25))
    print("The 75 quartile sentiment is%f" % np.percentile(data, 75))


