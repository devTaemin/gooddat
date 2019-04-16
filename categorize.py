import os
from soyspacing.countbase import RuleDict, CountSpace
import soyspacing
from pprint import pprint
from soynlp.tokenizer import RegexTokenizer, LTokenizer, MaxScoreTokenizer
from collections import Counter
from konlpy.tag import Okt


def tokenize():

    #띄어쓰기 부분 
    current_dir =  os.path.abspath(os.path.dirname(__file__))
    parent_dir = os.path.abspath(current_dir + "/../")
    current_dir = os.path.abspath(parent_dir + "gooddat/txt_files/")
   
    courpus_fname = current_dir + "onlyForModeling.txt"
    model = CountSpace()
    model.train(courpus_fname)

    model_fname = current_dir + "modelingResults.txt"
    model.save_model(model_fname, json_format=False)

    model2 = CountSpace()
    model2.load_model(current_dir + 'modelingResults.txt', json_format=False)

    verbose=False
    mc = 10  # min_count
    ft = 0.3 # force_abs_threshold
    nt =-0.3 # nonspace_threshold
    st = 0.3 # space_threshold

    with open(current_dir + 'raw_comment_file.txt', 'r', encoding='UTF8') as f:
        for line in f:
            sent = line
            sent_corrected, tags = model.correct(
                    sent,
                    verbose=verbose,
                    force_abs_threshold=ft,
                    nonspace_threshold=nt,
                    space_threshold=st,
                    min_count=mc   
                )
            with open(current_dir + 'space_comment_file.txt', 'a', encoding='UTF8') as f:
                f.write(sent)
    
    okt = Okt()
    with open(current_dir + 'space_comment_file.txt', 'r', encoding='UTF8') as f:
        for line in f:
            token = okt.pos(line)
            with open (current_dir + 'token_comment_file.txt', 'a', encoding='UTF8') as fd:
                for i in range(len(token)):
                    if(i == len(token) - 1):
                        if(token[i][1] == 'Noun' or token[i][1] == 'Adjective' or token[i][1] == 'Verb'):
                            fd.write(str(token[i]))
                        fd.write("\n")
                    else:
                        if(token[i][1] == 'Noun' or token[i][1] == 'Adjective' or token[i][1] == 'Verb'):
                            fd.write(str(token[i]))

    
                    #for number, letter in token:
                        #fd.write("\n".join(["%s %s" % (number, letter)]) + "\n")



                


            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        