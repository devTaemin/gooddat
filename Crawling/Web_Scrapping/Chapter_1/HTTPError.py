# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:50:05 2019

@author: Taemin
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError


def getTitle(URL):
    
    try:
        html = urlopen(URL)
    except HTTPError as e:
        return None
    
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


URL = 'https://pythonscraping.com/pages/page1.html'
title = getTitle(URL)

if title==None:
    print("Title could not be found")
else:
    print(title)
    
    


'''
* 스크레이퍼 예외처리

- 문제가 생길 수 있는 부분
    1. 페이지를 찾을 수 없거나 URL 해석에서 에러가 생긴 경우(404 Page Not Found)
    2. 서버를 찾을 수 없는 경우(500 Interner Server Error)   
- BeautifulSoup 객체에 들어있는 태그에 접근을 할 때마다 그 태그가 실제 존재하는지 체크하는 편이 좋다.
  왜냐하면 존재하지 않는 태그에 접근을 시도하면 BeautifulSoup는 None객체를 반환하기 때문이다. 
- 그렇기 때문에 태그 해석에 문제가 생기면 None객체를 반환하는 getTitle함수를 만든다.

'''

'''


1. from urllib.error import HTTPError
- urllib 디렉터리에 있는 error모듈에서 HTTPError 함수를 임포트합니다.

2.
def getTitle(URL):
    
    try:
        html = urlopen(URL)
    except HTTPError as e:
        return None
    
    try:
        bsObj = BeautifulSoup(html.read(), 'html.parser')
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

* try--except문이 쓰입니다
  
    1. try로 urlopen을 통해 URL에 지정된 원격객체를 읽어봅니다
       except를 이용해 시도를 했는데 에러페이지가 발생하면 None값을 리턴합니다.
  
    2. try로 BeautifulSoup를 통해 HTML 컨텐츠를 변형하여 정리합니다.
       태그를 이용하여 특정 값을 assign합니다
       except를 이용해 시도를 했는데 특정 태그에 접근이 실패했을 경우 None값을
       리턴합니다.



3.

URL = 'https://pythonscraping.com/pages/page1.html'
title = getTitle(URL)

if title==None:
    print("Title could not be found")
else:
    print(title)
    

- title변수에 함수값을 넣습니다. title값이 None일 경우 NOT Found가 출력되고
  아닌경우에는 title이 정상적으로 출력됩니다.
  
'''
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    