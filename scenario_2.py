# 2. 시나리오 구현: 인지/지각/사고 놀이

import os
import sys
import time
import json
import requests
from threading import Thread
from konlpy.tag import Mecab

import openpibo
import openpibo_models
from openpibo.speech import Speech
from openpibo.audio import Audio

import motion_list
import eye_list
import behavior_list
from NLP import nlp, Dictionary

nlp = nlp()
dic = Dictionary()

speech = tts()
audio = Audio()


def tts(speech_text):
    filename = openpibo.config['DATA_PATH'] + "/tts.mp3"
    speech.tts(f"<speak><voice name='WOMAN_READ_CALM'>{speech_text}<break time='2000ms'/></voice></speak>", filename)
    audio.play(filename, out='local', volume=-2000, background=False)
    print(speech_text)


def play_tissue():
    # 1) 준비물 설명
    behavior_list.do_explain()
    while True:
        time.sleep(2)
        tts('놀이를 위해 휴지가 필요해. 준비할 수 있어?')
        break

    behavior_list.do_waiting()
    while True:
        user_input = input("input: ")
        user_in = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while user_in != -1:
            if user_in == 'YES':
                break
            elif user_in == 'NO':
                tts('휴지는 화장실에도 많을거야')
                break
            else:
                tts('말 다시')
                continue
        break

    behavior_list.do_waiting()
    while True:
        tts('준비가 되면 준비 완료 라고 말해줘')
        user_input = input("input: ")
        user_in = nlp.nlp_done(user_input=user_input, dic=dic)

        while user_in != -1:
            if user_in == 'DONE':
                break
            else:
                continue
        break


    # 2) 놀이 설명
    behavior_list.do_suggestion()
    while True:
        tts('휴지를 풀어서 길을 만들어 볼거야. 할 수 있지?')
        user_input = input("input: ")
        user_in = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while user_in != -1:
            if user_in == 'YES':
                break
            elif user_in == 'NO':
                behavior_list.do_explain()
                while True:
                    tts('휴지를 뜯어서 하나의 길로 연결해보자!')
                    time.sleep(3)
                    break
                break
            else:
                tts('말 다시')
                continue
        break

    behavior_list.do_waiting()
    while True:
        tts('휴지 길은 미끄러울 수 있으니 뛰면 안 돼. 준비됐지?')
        user_input = input("input: ")
        user_in = nlp.nlp_done(user_input=user_input, dic=dic)

        while user_in != -1:
            if user_in == 'DONE':
                break
            else:
                continue
        break


    # 3) 놀이 진행
    behavior_list.do_waiting()
    while True:
        tts('휴지 길을 만들어 보자! 다 만들면 알려줘')
        user_input = input("input: ")
        user_in = nlp.nlp_done(user_input=user_input, dic=dic)

        while user_in != -1:
            if user_in == 'DONE':
                break
            else:
                tts('휴지를 짧게 뜯으면 모양을 만들기 쉬울거야.')
                continue
        break

    behavior_list.do_compliment()
    while True:
        tts('정말 멋진 길이 완성되었는걸? 천천히 걸어보자')
        break


    behavior_list.do_suggestion()
    while True:
        tts('곳곳에 휴지 섬을 만들어 보자. 휴지를 통째로 놓고 쌓아줘~')
        break

    # 4) 놀이 완료
    behavior_list.do_waiting()
    while True:
        tts('휴지 성을 완성하면 말해줘~')
        user_input = input("input: ")
        user_in = nlp.nlp_done(user_input=user_input, dic=dic)

        while user_in != -1:
            if user_in == 'DONE':
                break
            else:
                continue
        break

    tts('정말 열심히 만들었는걸? 휴지로 만들어서 포근해보여')

    behavior_list.do_photo()
    while True:
        tts('파이보가 사진찍어서 부모님께도 보여드릴게. 깜짝 놀라실거야!')
        break


    # 5) 마무리 대화
    tts('길을 만들 때 쓴 휴지를 찢어서 휴지 성에 눈을 내리자')
    tts('휴지 눈이 내리니까 정말 포근해. 너는 언제 포근함을 느껴?')
    # 그냥 녹음만
    tts('정말? 왜?')
    # 그냥 녹음만
    tts('생각만 해도 기분이 좋아!')

    # 6) 놀이 기록
    behavior_list.do_stamp()
    while True:
        tts('오늘 창작 스탬프를 찍을게')
        break
    behavior_list.do_photo()
    while True:
        tts('사진을 찍어 줄게. 브이~ ^-^v')
        time.sleep(5)
        print('여기 opencv capture 들어갈 곳2. 아마도?')
        break

    # 7) 다음 놀이 제안
    behavior_list.do_question()
    while True:
        tts('다음 놀이 할까?')

        user_input = input("input: ")
        user_in = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while user_in != -1:
            if user_in == 'YES':
                break
            elif user_in == 'NO':
                break
            elif user_in == 'SOSO':
                break
            else:
                tts('말 다시')
                continue
        break

    # print("시나리오 30: 풍선 축구 놀이 끄읏")

