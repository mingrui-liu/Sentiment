# Sentiment
SnowNLP是一个python写的类库，可以方便的处理中文文本内容，是受到了TextBlob的启发而写的，由于现在大部分的自然语言处理库基本都是针对英文的，于是写了一个方便处理中文的类库，并且和TextBlob不同的是，这里没有用NLTK，所有的算法都是自己实现的，并且自带了一些训练好的字典。注意本程序都是处理的unicode编码，所以使用时请自行decode成unicode。
## Features

* 中文分词（[Character-Based Generative Model](http://aclweb.org/anthology//Y/Y09/Y09-2047.pdf)）
* 词性标注（[TnT](http://aclweb.org/anthology//A/A00/A00-1031.pdf) 3-gram 隐马）
* 情感分析（现在训练数据主要是买卖东西时的评价，所以对其他的一些可能效果不是很好，待解决）
* 文本分类（Naive Bayes）
* 转换成拼音（Trie树实现的最大匹配）
* 繁体转简体（Trie树实现的最大匹配）
* 提取文本关键词（[TextRank](http://acl.ldc.upenn.edu/acl2004/emnlp/pdf/Mihalcea.pdf)算法）
* 提取文本摘要（[TextRank](http://acl.ldc.upenn.edu/acl2004/emnlp/pdf/Mihalcea.pdf)算法）
* tf，idf
* Tokenization（分割成句子）
* 文本相似（[BM25](http://en.wikipedia.org/wiki/Okapi_BM25)）
* 支持python3（感谢[erning](https://github.com/erning)）



我在snownlp的基础上改进了sentiment的算法：
1、原有的sentiment单纯使用了bayes分类，所有的词完全依靠于训练语料，并且不能很好地识别 不高兴， 不是不高兴这类反转的情感。再添加了识别与反转的逻辑之后能够识别否定情感
2、原有的训练模式是建立新的词典并覆盖原有的词典，这里添加了添加新语料的功能
3、加入了大量的智能机器人问答系统相关的语料，单纯的疑问句能识别为中性

