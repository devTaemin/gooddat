# -*- coding: utf-8 -*-
"""
Created on Thu May  9 08:18:18 2019

@author: Sewoong
"""
import numpy as np
from konlpy.tag import Okt
import json
import os
import nltk

import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

from pprint import pprint
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics

# 파일 데이터 읽어오기
def read_data(filename):
    with open(filename, 'r', encoding='UTF8') as f:
        data = [line.split('\t') for line in f.read().splitlines()]
        # txt 파일의 헤더(id document label)는 제외하기
        data = data[1:]
    return data

# Test set & Training set 문장 형태소 분할하기
def tokenize(doc):
    # norm은 정규화, stem은 근어로 표시하기를 나타냄
    return ['/'.join(t) for t in okt.pos(doc, norm=True, stem=True)]

# 단어 빈도수 세기
def term_frequency(doc):
    return [doc.count(word) for word in selected_words]

# 긍정 부정 점수 예측하기
def predict_pos_neg(review, token_array_pro, token_array_con):
    temp_pro = []
    temp_con = []
    token = tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
    score = float(model.predict(data))
    #긍정적일 경우
    if(score > 0.5):
        temp = okt.pos(review)
        temp_pro.append(temp)
        for d in temp_pro:
            for t in d:
                if (t[1] == 'Noun' or t[1] == 'Adjective' or t[1] == 'Verb'):
                    token_array_pro.append(t)
    #부정적일 경우
    else:
        temp = okt.pos(review)
        temp_con.append(temp)
        for d in temp_con:
            for t in d:
                if (t[1] == 'Noun' or t[1] == 'Adjective' or t[1] == 'Verb'):
                    token_array_con.append(t)
       
train_data = read_data('nratings_train.txt')
test_data = read_data('nratings_test.txt')

okt = Okt()

# JSON 파일 만들기
if os.path.isfile('train_docs.json'):
    with open('train_docs.json', encoding="utf-8") as f:
        train_docs = json.load(f)
    with open('test_docs.json', encoding="utf-8") as f:
        test_docs = json.load(f)
else:
    train_docs = [(tokenize(row[1]), row[2]) for row in train_data]
    test_docs = [(tokenize(row[1]), row[2]) for row in test_data]
    # JSON 파일로 저장
    with open('train_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(train_docs, make_file, ensure_ascii=False, indent="\t")
    with open('test_docs.json', 'w', encoding="utf-8") as make_file:
        json.dump(test_docs, make_file, ensure_ascii=False, indent="\t")

# 예쁘게 출력하기 위해서 pprint 라이브러리 사용
# 모델링
tokens = [t for d in train_docs for t in d[0]]

text = nltk.Text(tokens, name='NMSC')
          
selected_words = [f[0] for f in text.vocab().most_common(1000)]

train_x = [term_frequency(d) for d, _ in train_docs]
test_x = [term_frequency(d) for d, _ in test_docs]
train_y = [c for _, c in train_docs]
test_y = [c for _, c in test_docs]

x_train = np.asarray(train_x).astype('float32')
x_test = np.asarray(test_x).astype('float32')
y_train = np.asarray(train_y).astype('float32')
y_test = np.asarray(test_y).astype('float32')

model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(1000,)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

model.compile(optimizer=optimizers.RMSprop(lr=0.001),
             loss=losses.binary_crossentropy,
             metrics=[metrics.binary_accuracy])

model.fit(x_train, y_train, epochs=10, batch_size=512)
results = model.evaluate(x_test, y_test)

# 예측하려고 하는 데이터 입력
token_array_pro = []
token_array_con = []

current_dir =  os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.abspath(current_dir + "/../")
current_dir = os.path.abspath(parent_dir + "gooddat/txt_files/")
with open(current_dir + 'FLYDAY_testdata_6.txt', 'r', encoding='UTF8') as f:
    for line in f:
        predict_pos_neg(line, token_array_pro, token_array_con)
        
# 긍정적인 댓글에 대한 결과        
text_pro = nltk.Text(token_array_pro, name = 'NMSC')
print (len(text_pro.tokens))
print(len(set(text_pro.tokens)))
pprint(text_pro.vocab().most_common(10))

# 부정적인 댓글에 대한 결과
text_con = nltk.Text(token_array_con, name = 'NMSC')
print (len(text_con.tokens))
print(len(set(text_con.tokens)))
pprint(text_con.vocab().most_common(10))

# 그래프를 그리기 위한 초기화
font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
rc('font', family=font_name)
y_pro = []
x_pro = []
y_con = []
x_con = []
    
# 긍정적인 댓글에 대한 그래프
if(len(text_pro) == 0 and len(text_pro) == 0):
    print('긍정적인 댓글이 없습니다')
else:
    for i in range(0, 10):
        y_pro.append(text_pro.vocab().most_common(10)[i][0][0])
        x_pro.append(text_pro.vocab().most_common(10)[i][1])
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)
    ypos = np.arange(10)
    rects = plt.barh(ypos, x_pro, align='center', height=0.5)
    plt.yticks(ypos, y_pro)
    plt.xlabel('긍정적인 결과')
    plt.show()

# 부정적인 댓글에 대한 그래프
if(len(text_con) == 0 and len(text_con) == 0):
    print('부정적인 댓글이 없습니다')
else:
    for i in range(0, 10):
        y_con.append(text_con.vocab().most_common(10)[i][0][0])
        x_con.append(text_con.vocab().most_common(10)[i][1])
    fig = plt.figure(figsize=(12, 8))
    ax = fig.add_subplot(111)
    ypos = np.arange(10)
    rects = plt.barh(ypos, x_con, align='center', height=0.5)
    plt.yticks(ypos, y_con)
    plt.xlabel('부정적인 결과')
    plt.show()

