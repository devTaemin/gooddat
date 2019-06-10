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
import webbrowser
import time
import csv

from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from math import ceil
import re


import matplotlib.pyplot as plt
from wordcloud import WordCloud
from matplotlib import font_manager, rc
from PIL import Image
from wordcloud import ImageColorGenerator

from pprint import pprint
from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Imvely_crawler(url):
    #From input url, make the review_widget_url
    product_number = url[url.find("product_no=")+11:url.find("&")]
    widget_url = "http://widgets6.cre.ma/imvely.com/products/reviews?product_code=" + product_number + "&iframe_id=crema-product-reviews-2&widget_id=82&app=0"
    
    
    source = urlopen(widget_url)
    obj = soup(source,"html.parser")
    pages = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"products_reviews_header"}).find('div',{"class":"products_reviews_header__upper"}).find('span',{"class":"products_reviews_header__sort_type products_reviews_header__sort_type--selected"}).find('span',{"class":"reviews-count"}).text
    
    #Product name
    name = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_product_info"}).find('div',{"class":"products_reviews_product_info__name"}).text
    #Product Photo (Use image_src)
    image = obj.find("img")
    image_src = image.get("src")
    
    textfile = open('img.txt','w',encoding='utf-8')
    textfile.write(image_src)
    textfile.close()
    
    textfile = open('name.txt','w',encoding='utf-8')
    textfile.write(name)
    textfile.close()
    
    #Calculate number of pages
    temp=""
    for i in range(0,len(pages)):
        if(pages[i].isdigit()):
            temp+=pages[i]
    pages=ceil(int(temp)/10)
    m = 0
  
    #Crawling and write on text file
    textfile=open('Imvely.txt','w',encoding='utf-8')
    for i in range(1,pages+1):
        urls=urlopen(widget_url + "&page=" + str(i))
        obj=soup(urls,"html.parser")
        
        reviews = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('ul',{"class":"reviews reviews-product"})
        
        for comments in reviews.findAll('div',{"class":"products_reviews_list_review__message_content"}):
            comment = comments.text
            comment = comment.strip()
            EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
            comment_refine = EMOJI.sub(r'',comment) 
            textfile.write(comment_refine+"\n")
            m = m + 1
    print("--------------------------------")
    print("Crawler complete the operation!")
    print("--------------------------------")
    textfile.close()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def FLYDAY_crawler(url):
    #From input url, make the review_widget_url
    product_number = url[url.find("branduid=")+9:url.find("&")]
    widget_url = "http://widgets2.cre.ma/flyday.co.kr/products/reviews?product_code=" + product_number
    
    source = urlopen(widget_url)
    obj = soup(source,"html.parser")
    pages = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"products_reviews_header"}).find('div',{"class":"products_reviews_header__upper"}).find('span',{"class":"products_reviews_header__sort_type products_reviews_header__sort_type--selected"}).find('span',{"class":"reviews-count"}).text
    
    #Product name
    name = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_product_info"}).find('div',{"class":"products_reviews_product_info__name"}).text
    #Product Photo (Use image_src)
    image = obj.find("img")
    image_src = image.get("src")
    
    #Calculate number of pages
    temp=""
    for i in range(0,len(pages)):
        if(pages[i].isdigit()):
            temp+=pages[i]
    pages=ceil(int(temp)/5)
    m = 0
  
    #Crawling and write on text file
    textfile=open('FLYDAY.txt','w',encoding='utf-8')
    for i in range(1,pages+1):
        urls=urlopen(widget_url + "&page=" + str(i))
        obj=soup(urls,"html.parser")
        
        reviews = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('ul',{"class":"reviews reviews-product"})
              
        for comments in reviews.findAll('div',{"class":"products_reviews_list_review__message_content"}):
            comment = comments.text
            comment = comment.strip()
            EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
            comment_refine = EMOJI.sub(r'',comment) 
            textfile.write(comment_refine+"\n")
            m = m + 1
    print("--------------------------------")
    print("Crawler complete the operation!")
    print("--------------------------------")
    textfile.close()
    
    return image_src
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def Naning9_crawler(url):
    #From input url, make the review_widget_url
    product_number = url[url.find("index_no=")+9:]
    widget_url = "https://widgets1.cre.ma/naning9.com/products/reviews?product_code=" + product_number
    
    
    source = urlopen(widget_url)
    obj = soup(source,"html.parser")
    pages = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('div',{"class":"widget_reviews"}).find('div',{"class":"products_reviews_header"}).find('div',{"class":"products_reviews_header__upper"}).find('span',{"class":"products_reviews_header__sort_type products_reviews_header__sort_type--selected"}).find('span',{"class":"reviews-count"}).text

    #Product name
    name = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_product_info"}).find('div',{"class":"products_reviews_product_info__name"}).text
    #Product Photo (Use image_src)
    image = obj.find("img")
    image_src = image.get("src")
    
    #Calculate number of pages
    temp=""
    for i in range(0,len(pages)):
        if(pages[i].isdigit()):
            temp+=pages[i]
    pages=ceil(int(temp)/5)

  
    #Crawling and write on text file
    textfile=open('Naning9.txt','w',encoding='utf-8')
    for i in range(1,pages+1):
        urls=urlopen(widget_url + "&page=" + str(i))
        obj=soup(urls,"html.parser")
        
        reviews = obj.find('div',{"id":"content"}).find('div',{"class":"products_reviews_list"}).find('ul',{"class":"reviews reviews-product"})
        
        for comments in reviews.findAll('div',{"class":"products_reviews_list_review__message_content"}):
            comment = comments.text
            comment = comment.strip()
            EMOJI = re.compile('[\U00010000-\U0010ffff]', flags=re.UNICODE)
            comment_refine = EMOJI.sub(r'',comment) 
            textfile.write(comment_refine+"\n")
    print("--------------------------------")
    print("Crawler complete the operation!")
    print("--------------------------------")
    textfile.close()
    
    return image_src
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
  


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
                #if (t[1] == 'Noun' or t[1] == 'Adjective' or t[1] == 'Verb'):
                if (t[1] == 'Noun' or t[1] == 'Adjective'):
                    token_array_pro.append(t)
    #부정적일 경우
    else:
        temp = okt.pos(review)
        temp_con.append(temp)
        for d in temp_con:
            for t in d:
                #if (t[1] == 'Noun' or t[1] == 'Adjective' or t[1] == 'Verb'):
                if (t[1] == 'Noun' or t[1] == 'Adjective'):
                    token_array_con.append(t)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# URL 입력하기
webbrowser.open_new_tab('C:/Users/Sewoong/Desktop/Develop/gooddat/index.html')
while(True):
    if(os.path.exists("C:/Users/Sewoong/Downloads/undefined.txt")):
      break;
    else:
        time.sleep(3)

f=open("C:/Users/Sewoong/Downloads/undefined.txt",'r', encoding="utf-8")
line=f.readline()
f.close()
os.remove("C:/Users/Sewoong/Downloads/undefined.txt")

img = ""
name = ""

if('imvely' in line):
    Imvely_crawler(line)
elif('flyday' in line):
    FLYDAY_crawler(line)  
elif('naning9' in line):
    Naning9_crawler(line)
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#


#모델링 코드
train_data = read_data('ratings_train.txt')
test_data = read_data('ratings_test.txt')

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
current_dir = os.path.abspath(parent_dir + "gooddat/")

if os.path.isfile('FLYDAY.txt'):
    with open('FLYDAY.txt', 'r', encoding='UTF8') as f:
        for line in f:
            predict_pos_neg(line, token_array_pro, token_array_con)
    os.remove("C:/Users/Sewoong/Desktop/Develop/gooddat/FLYDAY.txt")
elif os.path.isfile('Imvely.txt'):
    with open('Imvely.txt', 'r', encoding='UTF8') as f:
        for line in f:
            predict_pos_neg(line, token_array_pro, token_array_con)
    os.remove("C:/Users/Sewoong/Desktop/Develop/gooddat/Imvely.txt")
elif os.path.isfile('Naning9.txt'):
    with open('Naning9.txt', 'r', encoding='UTF8') as f:
        for line in f:
            predict_pos_neg(line, token_array_pro, token_array_con)
    os.remove("C:/Users/Sewoong/Desktop/Develop/gooddat/Naning9.txt")
        
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
    fig = plt.gcf()
    plt.show()
    fig.savefig('C:/Users/Sewoong/Desktop/Develop/gooddat/images/G1.jpg')
    
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
    fig = plt.gcf()
    plt.show()
    fig.savefig('C:/Users/Sewoong/Desktop/Develop/gooddat/images/G2.jpg')

positive_comment = []
negative_comment = []
for i in range(0, len(text_pro.vocab().most_common(len(text_pro)))):
    y_pro.append(text_pro.vocab().most_common(len(text_pro))[i][0][0])
    x_pro.append(text_pro.vocab().most_common(len(text_pro))[i][1])
    positive_comment.append((y_pro[i], x_pro[i]))
    
for i in range(0, len(text_con.vocab().most_common(len(text_con)))):
    y_con.append(text_con.vocab().most_common(len(text_con))[i][0][0])
    x_con.append(text_con.vocab().most_common(len(text_con))[i][1])
    negative_comment.append((y_con[i], x_con[i]))

shirt_coloring = np.array(Image.open("C:/Users/Sewoong/Desktop/Develop/gooddat/images/tshirt1.png"))
image_colors = ImageColorGenerator(shirt_coloring)


tmp_data = dict(positive_comment)
wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      relative_scaling = 0.2, mask = shirt_coloring,
                      background_color='white',
                      min_font_size=1, max_font_size=40
                      ).generate_from_frequencies(tmp_data)
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
fig = plt.gcf()
plt.show()
fig.savefig('C:/Users/Sewoong/Desktop/Develop/gooddat/images/G3.jpg')

tmp_data = dict(positive_comment)
wordcloud = WordCloud(font_path="c:/Windows/Fonts/malgun.ttf",
                      relative_scaling = 0.2, mask = shirt_coloring,
                      background_color='white',
                      min_font_size=1, max_font_size=40
                      ).generate_from_frequencies(tmp_data)
plt.figure(figsize=(12, 12))
plt.imshow(wordcloud.recolor(color_func=image_colors), interpolation="bilinear")
plt.axis("off")
fig = plt.gcf()
plt.show()
fig.savefig('C:/Users/Sewoong/Desktop/Develop/gooddat/images/G4.jpg')



#웹페이지 열기
webbrowser.open_new_tab('C:/Users/Sewoong/Desktop/Develop/gooddat/chart.html')
os.remove("C:/Users/Sewoong/Desktop/Develop/gooddat/img.txt")
os.remove("C:/Users/Sewoong/Desktop/Develop/gooddat/name.txt")

