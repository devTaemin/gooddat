# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:40:31 2019

@author: Sewoong
"""

from pprint import pprint
import sys
sys.path.append('../')

from soynlp.tokenizer import RegexTokenizer, LTokenizer, MaxScoreTokenizer

scores = {'가격':0.5, '배송':0.5, '사이즈':0.5}

tokenizer = LTokenizer(scores=scores)

print('\nflatten=True\nsent = 옷 입고 여친 만나자마자 티 이쁘다며 자기도 사달라고 하여서 라지 사이즈로 구입하였습니다 남녀 모두 잘 어울립니다 구뜨구뜨 ㅋㅋㅋ')
print(tokenizer.tokenize('옷 입고 여친 만나자마자 티 이쁘다며 자기도 사달라고 하여서 라지 사이즈로 구입하였습니다 남녀 모두 잘 어울립니다 구뜨구뜨 ㅋㅋㅋ'))

print('\nflatten=False\nsent = 옷 입고 여친 만나자마자 티 이쁘다며 자기도 사달라고 하여서 라지 사이즈로 구입하였습니다 남녀 모두 잘 어울립니다 구뜨구뜨 ㅋㅋㅋ')
print(tokenizer.tokenize('옷 입고 여친 만나자마자 티 이쁘다며 자기도 사달라고 하여서 라지 사이즈로 구입하였습니다 남녀 모두 잘 어울립니다 구뜨구뜨 ㅋㅋㅋ', flatten=False))

print('\nflatten=False\nsent = 가격대비는 좋네요~ 목부분에 힘이 있어서 좋아요 ㅎㅎ 안늘어날구같네요~')
print(tokenizer.tokenize('가격대비는 좋네요~ 목부분에 힘이 있어서 좋아요 ㅎㅎ 안늘어날구같네요~', flatten=False))

print('\nflatten=True\nsent = 가격대비는 좋네요~ 목부분에 힘이 있어서 좋아요 ㅎㅎ 안늘어날구같네요~')
print(tokenizer.tokenize('가격대비는 좋네요~ 목부분에 힘이 있어서 좋아요 ㅎㅎ 안늘어날구같네요~'))