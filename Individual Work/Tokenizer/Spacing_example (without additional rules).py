# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:40:02 2019

@author: Sewoong
"""

import os
from soyspacing.countbase import RuleDict, CountSpace

corpus_fname = os.path.abspath("Sentence_example.txt")
model = CountSpace()
model.train(corpus_fname)

model_fname = "SapcingResult_exmaple.txt"
model.save_model(model_fname, json_format=False)

model = CountSpace()
model.load_model(model_fname, json_format = False)

sent = '이건진짜좋은영화 라라랜드진짜좋은영화'
sent_corrected, tags = model.correct(sent)

print('before: %s' % sent)
print('after : %s' % sent_corrected)


