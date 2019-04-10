#db URL 읽어오기
#Crawler 모듈 import해서 Crawler URL 넘겨주기
#---------------Crawler 결과 DB에 저장 --------------
#Crawler 결과 받아오기
#Algorithm에 문장 넘기기
#결과값 DB에 저장하기

from db import * 
import crawler 
import categorize

# DB 읽어오기
urlLink = dataDownload()

# Crawler에 URL 넘겨주기 및 작동
crawlResult = crawler.driver(urlLink)

# Algorithm에 결과 넘기기
categResult = categorize.tokenize(crawlResult)

# 최종 결과값 DB에 저장하기
dataUpload(categResult)