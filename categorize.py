import os
from soyspacing.countbase import RuleDict, CountSpace
import soyspacing
from pprint import pprint
from soynlp.tokenizer import RegexTokenizer, LTokenizer, MaxScoreTokenizer
from collections import Counter
from konlpy.tag import Okt
from pprint import pprint
import nltk
import numpy as np

from tensorflow.keras import models
from tensorflow.keras import layers
from tensorflow.keras import optimizers
from tensorflow.keras import losses
from tensorflow.keras import metrics

def term_frequency(doc, selected_words):
    return [doc.count(word) for word in selected_words]

def predict_pos_neg(review, model):
    token = tokenize(review)
    tf = term_frequency(token)
    data = np.expand_dims(np.asarray(tf).astype('float32'), axis=0)
    score = float(model.predict(data))
    if(score > 0.5):
        print("[{}]는 {:.2f}% 확률로 긍정 리뷰이지 않을까 추측해봅니다.^^\n".format(review, score * 100))
    else:
        print("[{}]는 {:.2f}% 확률로 부정 리뷰이지 않을까 추측해봅니다.^^;\n".format(review, (1 - score) * 100))


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
    tokenArray = []
    
    with open(current_dir + 'space_comment_file.txt', 'r', encoding='UTF8') as f:
        for line in f:
            token = okt.pos(line)
            tokenArray.append(token)
    
    tokens = []
    for d in tokenArray:
        for t in d:
            if (t[1] == 'Noun' or t[1] == 'Adjective' or t[1] == 'Verb'):
                tokens.append(t)
    
    text = nltk.Text(tokens, name = 'NMSC')
    print (len(text.tokens))
    print(len(set(text.tokens)))
    pprint(text.vocab().most_common(10))
    
    
    
    # 데이터 전처리
    selected_words = [f[0] for f in text.vocab().most_common(10000)]
    
    train_x = [term_frequency(d, selected_words) for d, _ in tokenArray]
    test_x = [term_frequency(d, selected_words) for d, _ in tokenArray]
    train_y = [c for _, c in tokenArray]
    test_y = [c for _, c in tokenArray]

    x_train = np.asarray(train_x).astype('float32')
    x_test = np.asarray(test_x).astype('float32')

    y_train = np.asarray(train_y).astype('float32')
    y_test = np.asarray(test_y).astype('float32')
    
    '''
    
    # 모델 정의 및 학습하기
    model = models.Sequential()
    model.add(layers.Dense(64, activation='relu', input_shape=(10000,)))
    model.add(layers.Dense(64, activation='relu'))
    model.add(layers.Dense(1, activation='sigmoid'))

    model.compile(optimizer=optimizers.RMSprop(lr=0.001),
                  loss=losses.binary_crossentropy,
                  metrics=[metrics.binary_accuracy])

    model.fit(x_train, y_train, epochs=10, batch_size=512)
    results = model.evaluate(x_test, y_test)
    
    print(results)
    
    #모델 예측하기
    predict_pos_neg("올해 최고의 영화! 세 번 넘게 봐도 질리지가 않네요.", model)
    predict_pos_neg("배경 음악이 영화의 분위기랑 너무 안 맞았습니다. 몰입에 방해가 됩니다.", model)
    predict_pos_neg("주연 배우가 신인인데 연기를 진짜 잘 하네요. 몰입감 ㅎㄷㄷ", model)
    predict_pos_neg("믿고 보는 감독이지만 이번에는 아니네요", model)
    predict_pos_neg("주연배우 때문에 봤어요", model)

'''

    '''
    with open(current_dir + 'space_comment_file.txt', 'r', encoding='UTF8') as f:
        for line in f:
            token = okt.pos(line)
            with open (current_dir + 'token_comment_file.txt', 'a', encoding='UTF8') as fd:
                for i in range(len(token)):
                    if(i == len(token) - 1):
                        if(token[i][1] == 'Noun' or token[i][1] == 'Adjective' or token[i][1] == 'Verb' or token[i][1] == 'Josa'):
                            fd.write(str(token[i]))
                        fd.write("\n")
                    else:
                        if(token[i][1] == 'Noun' or token[i][1] == 'Adjective' or token[i][1] == 'Verb' or token[i][1] == 'Josa'):
                            fd.write(str(token[i]))
                            '''


    



                


            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        