#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from snownlp import sentiment
# 读取txt文件进行训练
negative_file = 'negative_train.txt'
positive_file = 'positive_train.txt'

#第一次训练
#sentiment.train_first(negative_file, positive_file)

#之后的增加训练
sentiment.train(negative_file, positive_file)

#保存词典
sentiment.save('sentiment.marshal')

print('ok')