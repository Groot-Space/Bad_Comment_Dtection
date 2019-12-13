# -*- coding: utf-8 -*-
"""
Word2vec 학습
"""

import os
from konlpy.tag import Okt
import gensim 
import tensorflow as tf
import numpy as np
import codecs

os.chdir("C:\\Users\\NohTaeHyun\\Desktop\\Bad_Comment_Dtection_Project\\Word2Vec\\Movie_rating_data")

def read_data(filename):    
    with open(filename, 'r',encoding='utf-8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]        
        data = data[1:]   # header 제외 #
    return data 
    
train_data = read_data('ratings_train.txt') 
test_data = read_data('ratings_test.txt') 

pos_tagger = Okt()

def tokenize(doc): #단어 옆에 형태소 붙여주는 메소드

    return ['/'.join(t) for t in pos_tagger.pos(doc, norm=True, stem=True)]


## training Word2Vec model using skip-gram   
tokens = [tokenize(row[1]) for row in train_data]
model = gensim.models.Word2Vec(sentences= tokens, size=300, window=5, workers=4, min_count= 1, sg = 1, alpha= 0.025 ,min_alpha=0.025, seed=1234)#size=300,sg = 1, alpha=0.025,min_alpha=0.025, seed=1234


model.save('Word2vec.model2')
model.most_similar('팝콘/Noun',topn = 20)  ## topn = len(model.wv.vocab)
