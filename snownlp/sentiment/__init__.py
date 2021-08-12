# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from jieba import cut
from jieba import load_userdict
from jieba import set_dictionary
import os
import codecs

from .. import normal
from ..classification.bayes import Bayes

data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                         'sentiment.marshal')
load_userdict(os.path.join(os.path.dirname(os.path.abspath(__file__)), '分词.txt'))
#set_dictionary(os.path.join(os.path.dirname(os.path.abspath(__file__)), '分词2.txt'))


class Sentiment(object):

    def __init__(self):
        self.classifier = Bayes()

    def save(self, fname, iszip=True):
        self.classifier.save(fname, iszip)

    def save_train(self, fname, iszip=True):
        self.classifier.save_train(fname, iszip)

    def load(self, fname=data_path, iszip=True):
        self.classifier.load(fname, iszip)

    def handle(self, doc):
        words = cut(doc)
        list = []
        for i in words:
            if '1' not in i and '2' not in i and '3'not in i  and '4'not in i and '5' not in i and '6' not in i and '7' not in i and '8'not in i and '9' not in i and '0' not in i :
                list.append(i)
        words = normal.filter_stop(list)
        print(words)
        return words

    def train(self, neg_docs, pos_docs):
        data = []
        for sent in neg_docs:
            data.append([self.handle(sent), 'neg'])
        for sent in pos_docs:
            data.append([self.handle(sent), 'pos'])
        self.classifier.train(data)

    def train_first(self, neg_docs, pos_docs):
        data = []
        for sent in neg_docs:
            data.append([self.handle(sent), 'neg'])
        for sent in pos_docs:
            data.append([self.handle(sent), 'pos'])
        self.classifier.train_first(data)

    def classify(self, sent):
        x = self.handle(sent)
        ret, prob = self.classifier.classify(x)
        if ret == 'pos':
            return prob
        return 1-prob




classifier = Sentiment()
classifier.load()

def train(neg_file, pos_file):
    neg_docs = codecs.open(neg_file, 'r', 'utf-8').readlines()
    pos_docs = codecs.open(pos_file, 'r', 'utf-8').readlines()
    global classifier
    classifier = Sentiment()
    classifier.train(neg_docs, pos_docs)

def train_first(neg_file, pos_file):
    neg_docs = codecs.open(neg_file, 'r', 'utf-8').readlines()
    pos_docs = codecs.open(pos_file, 'r', 'utf-8').readlines()
    global classifier
    classifier = Sentiment()
    classifier.train_first(neg_docs, pos_docs)

def save(fname, iszip=True):
    classifier.save(fname, iszip)


def load(fname, iszip=True):
    classifier.load(fname, iszip)


def classify(sent):
    return classifier.classify(sent)