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


    def nlp_yes_or_no(self, input, dic):
        user_input = ''
        for i in range(len(dic.yes_or_no['Yes'])):
            if dic.yes_or_no['Yes'][i] in input:
                user_input = 'YES'  # 'Yes'
        for j in range(len(dic.yes_or_no['No'])):
            if dic.yes_or_no['No'][j] in input:
                user_input = 'NO'  # No
        for k in range(len(dic.yes_or_no['SOSO'])):
            if dic.yes_or_no['SOSO'][k] in input:
                user_input = 'SOSO'  # No
        return user_input


    def nlp_done(self, input, dic):
        user_input = ''
        for i in range(len(dic.done['Done'])):
            if dic.done['Done'][i] in input:
                user_input = 'YES'  # 'Yes'
        for j in range(len(dic.done['No'])):
            if dic.done['No'][j] in input:
                user_input = 'NO'  # No
        for k in range(len(dic.done['SOSO'])):
            if dic.done['SOSO'][k] in input:
                user_input = 'SOSO'  # No
        return user_input


class Dictionary:
    def __init__(self):
        self.yes_or_no = \
            {
                'Yes': ['네', '예', '응', '어', '있어', '좋아', '그래'],
                'No': ['아니', '안', '별로', '글쎄', '싫어', '싫', '못하', '못해', '없어', '없네', '없는', '몰라', '모르', '몰라' '그만']
                'SOSO': ['또', '같은', '한 번 더', '계속']
            }
        self.done = \
            {
                'Done': ['완료', '됐어', '했어', '하자', '왔어']
            }