# -*- coding: utf-8 -*-
"""
Created on Sun Mar 24 15:20:47 2019

@author: Taemin
"""

from urllib.request import urlopen

URL = 'https://pythonscraping.com/pages/page1.html'
html = urlopen(URL)
print(html.read())




"""

1. from urllib.request import urlopen
- urllib 라이브러리에서 파이썬 모듈 request를 읽고 그 안에 있는 urlopen함수 하나를 임포트한다.

2. URL
- url을 따로 지정한다. 추후 입력을 받아야 하기 때문이다.

3. html = urlopen(URL)
- urlopen함수을 이용하여 네트워크를 통해 지정된 URL 원격 객체를 읽습니다. 출력을 위해 html 변수에 assign 해줍니다.

4. print(html.read())
https://pythonscraping.com 서버의, /pages 디렉터리에 있는 ,/pages1.html HTML파일을 받아온것이다.

"""
