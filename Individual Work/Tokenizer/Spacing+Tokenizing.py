# -*- coding: utf-8 -*-
"""
Created on Tue Apr  2 21:47:31 2019

@author: Sewoong
"""

import os
import sys
sys.path.append('../')
from soyspacing.countbase import RuleDict, CountSpace
from pprint import pprint
from soynlp.tokenizer import RegexTokenizer, LTokenizer, MaxScoreTokenizer

model = CountSpace()
model_fname = "SapcingResult_exmaple.txt"
rule_fname = os.path.abspath("additional_rules.txt")

model.load_model(model_fname, json_format = False)
rule_dict = RuleDict(rule_fname)

sent = '옷입고여친만나자마자티이쁘다며자기도사달라고하여서라지사이즈로구입하였습니다 남녀 모두 잘 어울립니다 구뜨구뜨 ㅋㅋㅋ'
sent_corrected, tags = model.correct(sent, rules = rule_dict)

print('before: %s' % sent)
print('after : %s' % sent_corrected)

scores = {'가격':0.5, '배송':0.5, '사이즈':0.5}

tokenizer = LTokenizer(scores=scores)

print('\nflatten=True\nsent = 옷 입고 여친 만나자마자 티 이쁘다며 자기도 사달라고 하여서 라지 사이즈로 구입하였습니다 남녀 모두 잘 어울립니다 구뜨구뜨 ㅋㅋㅋ')
print(tokenizer.tokenize(sent))