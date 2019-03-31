# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:28:54 2019

@author: Taemin
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

URL = 'https://pythonscraping.com/pages/warandpeace.html'
html = urlopen(URL)
bsObj = BeautifulSoup(html, 'html.parser')

nameList = bsObj.findAll('span',{'class':'green'}) #리스트로 정리됩니다!
for name in nameList:
    # print(name)
    print(name.get_text())
    

'''
1. html = urlopen(URL)
- 네트워크를 통해 해당 URL의 정보를 가져옵니다.


2. bsObj = BeautifulSoup(html, 'html.parser')
- BeautifulSoup를 이용하여 가져온 정보를 정리합니다.

3. ***
nameList = bsObj.findAll('span',{'class':'green'})
for name in nameList:
    # print(name)
    print(name.get_text())

- BeautifulSoup를 이용하여 내용을 정리한 bsObj 변수를 findAll을 이용하여 원하는 
  특정 정보를 리스트에 저장합니다
- 저장한 리스트안의 변수들을 for loop를 이용하여 출력합니다, 단 태그도 함께 저장되기
  때문에 .get_text()를 이용하여 text정보만 출력해줍니다.
  태그를 보존하기 때문에 .get_text는 최종적으로 사용해야 합니다.

'''