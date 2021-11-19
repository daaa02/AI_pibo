import re

from konlpy.tag import Kkma
from konlpy.tag import Komoran
from konlpy.tag import Okt
from pandas import DataFrame, Series
import pandas as pd


class nlp:
    def __init__(self):
        self.kk = Kkma()
        self.km = Komoran()
        self.okt = Okt()
        self.user_tag = []
        self.temp = {}
        self.n = 0


    def nlp_yes_or_no(self, user_input, dic):
        answer = ''
        for i in range(len(dic.yes_or_no['Yes'])):
            if dic.yes_or_no['Yes'][i] in user_input:
                answer = 'YES'  # 'Yes'
        for j in range(len(dic.yes_or_no['No'])):
            if dic.yes_or_no['No'][j] in user_input:
                answer = 'NO'  # No
        for k in range(len(dic.yes_or_no['SoSo'])):
            if dic.yes_or_no['SoSo'][k] in user_input:
                answer = 'SOSO'  # SoSo
        return answer


    def nlp_done(self, user_input, dic):
        answer = ''
        for i in range(len(dic.done['Done'])):
            if dic.done['Done'][i] in user_input:
                answer = 'DONE'  # 'Done'
        return answer

    
    def nlp_animal(self, user_input, dic):
        a_list = re.split('[ 가랑을를]', user_input)     # ' ', 가, 랑, 을, 를 제거하고 리스트

        answer = [i for i in a_list if i in dic.animal]
        return answer[0]


class Dictionary:
    def __init__(self):
        self.yes_or_no = \
            {
                'Yes': ['yes', '네', '예', '응', '어', '있어', '좋아', '그래', '맞아', '알았어', '알겠어', '당연'],
                'No': ['no', '아니', '안', '별로', '글쎄', '싫어', '싫', '못 하', '못 하겠어', '못해', '없었어', '없어', '없네',
                       '없는', '몰라', '모르', '몰라' '그만'],
                'SoSo': ['again', '또', '같은', '한 번 더', '한번 더', '계속']
            }
        self.done = \
            {
                'Done': ['done', '완료', '됐어', '했어', '하자', '왔어', '시작', '끝', '다 만들었어', '다 그렸어', '다 오렸어']
            }
        self.animal = ['토끼', '타조', '돌고래', '사슴', '호랑이', '고양이', '강아지', '개', '수달', '코끼리', '오리', '사자', '새']
