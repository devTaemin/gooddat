# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 16:51:00 2019

@author: Taemin
"""

from bs4 import BeautifulSoup
import requests

maximum = 0
page = 1

URL = 'https://land.naver.com/news/expertColumn.nhn'
response = requests.get(URL)
source = response.text
soup = BeautifulSoup(source, 'html.parser')



while True:
    page_list = soup.findAll('a',{'class':'NP=r:' + str(page)})
    if not page_list:
        maximum = page - 1
        break
    page = page + 1
    
print("총 " + str(maximum) + " 개의 페이지가 확인 됬습니다.")
# next버튼을 누른 다음에 있는 page도 확인해야한다.


whole_source = ""
for page_number in range(1, maximum+1):
    URL = 'https://land.naver.com/news/expertColumn.nhn?page=' + str(page_number)
    response = requests.get(URL)
    whole_source = whole_source + response.text

soup = BeautifulSoup(whole_source, 'html.parser')
find_title = soup.select('#content > div.table_list_column > table > tbody > tr > td.title > a')
                         

for title in find_title:
    print(title.text)
    
    
# 회의안 solution : next 버튼으로 돌리기
















