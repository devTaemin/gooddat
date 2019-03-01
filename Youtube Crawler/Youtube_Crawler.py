#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 15:31:12 2019

@author: donghoon
"""
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup  as soup

#ID=str(input('type your youtube id'))
#PW=str(input('type your youtube pw'))
ID="유투브 아이디"
PW="유투브 비밀번호"

driver=webdriver.Chrome('/Users/donghoon/Downloads/chromedriver')
driver.get("https://accounts.google.com/signin/v2/identifier?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Fnext%3D%252F%26hl%3Dko%26app%3Ddesktop%26action_handle_signin%3Dtrue&hl=ko&service=youtube&flowName=GlifWebSignIn&flowEntry=ServiceLogin")
elem=driver.find_element_by_xpath('//*[@id="identifierId"]')
elem.send_keys(ID)
elem.send_keys(Keys.RETURN)
driver.implicitly_wait(3)

elem=driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
elem.send_keys(PW)
elem.send_keys(Keys.RETURN)
time.sleep(2)
elem=driver.find_element_by_xpath('//*[@id="guide-icon"]')
elem.click()
elem=driver.find_element_by_xpath('//*[@id="section-items"]/ytd-guide-entry-renderer[1]')
elem.click()
time.sleep(2)
elem=driver.find_element_by_xpath('//*[@id="options"]/ytd-sub-feed-option-renderer[3]')
elem.click()
'''
며칠동안 헤맸던 부분이 바로 아래이다.
시청기록으로 되어있던 것을 댓글을 눌러서 바꾸었는데 
그 후 html이 바뀔 시간이 필요해서 time.sleep()을 넣어야 한다.
'''
time.sleep(2)
#여기까지 실행하면 댓글 창에 도달한다.

comment_html=driver.page_source
comment_obj=soup(comment_html,"html.parser")

comment_container=[]
comm=[]
print("해당 계정의 최근 댓글을 추출 중....")
while len(comm)==0:
    time.sleep(1)
    comm=comment_obj.find('body').find('ytd-app').find('div',{'class':'style-scope ytd-app'}).find('ytd-page-manager',{'class':'style-scope ytd-app'}).find('ytd-browse',{'page-subtype':"history"}).find('ytd-two-column-browse-results-renderer',{'class':'style-scope ytd-browse'}).find('ytd-section-list-renderer',{'class':'style-scope ytd-two-column-browse-results-renderer'}).find('div',{'id':'contents'}).find('ytd-item-section-renderer',{'class':'style-scope ytd-section-list-renderer'}).find('div',{'id':'contents'}).findAll('ytd-comment-history-entry-renderer',{'class':'style-scope ytd-item-section-renderer'})  
    
for i in comm:
    temp1=i.find('a').text
    temp2=i.find('yt-formatted-string',{'class':'content style-scope ytd-comment-history-entry-renderer'}).text
    result=temp1+"\n"+temp2+"\n\n"
    comment_container.append(result)
print("저장 완료")
for i in comment_container:
    print(i)
    
driver.quit()
