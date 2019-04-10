# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 17:54:03 2019

@author: Sewoong
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 16:40:02 2019

@author: Sewoong
"""

import os
from soyspacing.countbase import RuleDict, CountSpace

model = CountSpace()
model_fname = "SapcingResult_exmaple.txt"
rule_fname = os.path.abspath("additional_rules.txt")

model.load_model(model_fname, json_format = False)
rule_dict = RuleDict(rule_fname)

sent = '이건진짜좋은영화 라라랜드진짜좋은영화'
sent_corrected, tags = model.correct(sent, rules = rule_dict)

print('before: %s' % sent)
print('after : %s' % sent_corrected)
