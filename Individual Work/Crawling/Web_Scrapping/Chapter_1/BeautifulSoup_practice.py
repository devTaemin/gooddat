# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:31:56 2019

@author: Taemin
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = 'https://pythonscraping.com/pages/page1.html'
html = urlopen(URL)

bsObj = BeautifulSoup(html.read(), 'html.parser')
print(bsObj)
print('\n')
print(bsObj.html)
print('\n')
print(bsObj.title)
print('\n')
print(bsObj.body)
print('\n')
print(bsObj.h1)
print('\n')
print(bsObj.div)

'''
(+) 

    bsObj = BeautifulSoup(html.read(), 'html.parser')

- html을 urlopen(URL)을 통해 받아서 html.read()를 이용하여 HTML콘텐츠를 얻습니다.
- BeautifulSoup(Variable, 'html.parser')는 이 HTML 콘텐츠를 변형하여 출력합니다.
- BeautifulSoup의 자료구조는 다음과 같습니다.

* html -> <html><head>...</head> <body>...</body></html>

    -head -> <head><title>...</title></head>
    -body -> <body><h1>...</h1><div>...</div></body>
    
- 출력형식 확인
'''