# 1. 시나리오 구현: 대근육/소근육 놀이

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

speech = Speech()
audio = Audio()


# def record(self, filename="stream.wav", timeout=10):
#     if os.path.isfile(filename):
#         os.remove(filename)

#     cmd = f"arecord default -c1 -r16000 -f S16_LE -d {timeout} -t wav -q -vv -V streo stream.raw;sox stream.raw -c 1 -b 16 {filename};rm stream.raw"
#     os.system(cmd)


def stt():
    rest_api_key = 'f8f8c3f66bb3310016fdeccffba152e8'

    kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    headers = {
        "Content-Type": "application/octet-stream",
        "X-DSS-Service": "DICTATION",
        "Authorization": "KakaoAK " + rest_api_key,
    }

    with open('stream.wav', 'rb') as fp:
        audio = fp.read()

    res = requests.post(kakao_speech_url, headers=headers, data=audio)
    # print(res.text)

    result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1]
    result_final = json.loads(result_json_string)
    result = result_final['value']
    print(result)
    return result


def tts(speech_text):
    speech = Speech()
    audio = Audio()
    
    file = openpibo.config['DATA_PATH'] + "/tts.wav"
    speech.tts(f"<speak>\
                <voice name='WOMAN_READ_CALM'><prosody rate='slow'>{speech_text}<break time='500ms'/></prosody></voice>\
                </speak>", file)
    audio.play(file, 'local', '-2000', True)
    print("\n")
    print(speech_text)


###
def play_balloon_soccer():
    # 1) 준비물 설명
    behavior_list.do_explain()
    while True:
        print("\n")
        tts('풍선과 천을 준비할 수 있어?')
        break

    behavior_list.do_waiting()
    while True:
        os.system('python record.py')
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while answer != -1:
            if answer == 'YES':
                print(answer)
            elif answer == 'NO':
                print(answer)
                tts('이번 놀이는 천이 없어도 할 수 있어!')
            else:
                tts('말 다시')
                os.system('python record.py')
                user_input = stt()
                # user_input = input("input: ")
                answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
                print(answer)
                continue
            break
        break

    behavior_list.do_waiting()
    while True:
        tts('풍선 준비가 되면 준비 완료 라고 말해줘')

        os.system('python record.py')
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)

        if answer == 'DONE':
            print(answer)
        # else:
        #     continue
        break

    # 2) 놀이 설명
    behavior_list.do_suggestion()
    while True:
        tts('너가 좋아하는 색깔의 풍선을 골라봐.')

        os.system('python record.py')
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)
        print(answer)
        break

    # 3) 놀이 진행
    behavior_list.do_suggestion()
    while True:
        tts('자 이제 풍선을 불어보자. 할 수 있지?')
        os.system('python record.py')
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        if answer == 'YES':
            print(answer)
        elif answer == 'NO':
            print(answer)
            tts('엄마에게 도움을 요청해')
            time.sleep(3)
        # else:
        #     tts('말 다시')
        #     continue
        break

    behavior_list.do_suggestion()
    while True:
        tts('풍선을 묶지 말고 멀리 날려보자!')
        time.sleep(2)
        break

    behavior_list.do_photo()
    while True:
        time.sleep(5)
        print('여기 행동 촬영 들어갈 곳. 아마도?')
        time.sleep(2)
        break

    behavior_list.do_joy()
    while True:
        time.sleep(2)
        tts('정말 재밌어보여!')
        break

    behavior_list.do_suggestion()
    while True:
        tts('다음엔 풍선 축구를 해볼까?')
        break

    # 4) 놀이 완료
    behavior_list.do_question()
    while True:
        tts('축구 선수처럼 발 혹은 무릎 높이로 차보자. 준비 됐어?')

        os.system('python record.py')
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)

        if answer == 'DONE':
            print(answer)
        # else:
        #     tts('?')
        #     continue
        break

    behavior_list.do_compliment()
    while True:
        time.sleep(2)
        tts('잘한다! 이번엔 머리로 헤딩슛을 해보자!')
        break

    behavior_list.do_cheer()
    while True:
        time.sleep(5)
        break

    # 5) 마무리 대화
    behavior_list.do_question()
    while True:
        tts('풍선으로 하는 축구 놀이 재미있었어?')

        os.system('python record.py')
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        if answer == 'YES':
            print(answer)
        elif answer == 'NO':
            print(answer)
        # else:
        #     break
        break

    behavior_list.do_tired()
    while True:
        tts('파이보는 달리느라 힘들었어. 너는 오늘 힘든 일 있었어?')

        os.system('python record.py')
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        if answer == 'YES':
            print(answer)
            behavior_list.do_sad()
            while True:
                tts('그랬구나, 다음에 그런 일이 또 생기면 주변에 도움을 요청해봐')
                time.sleep(5)
                break

        elif answer == 'NO':
            print(answer)
            behavior_list.do_joy()
            while True:
                tts('그랬구나!')
                time.sleep(5)
                break
        # else:
        #     break
        break

    # 6) 놀이 기록
    behavior_list.do_stamp()
    while True:
        time.sleep(3)
        tts('오늘은 튼튼 스탬프를 찍어줄게')
        break

    behavior_list.do_photo()
    while True:
        tts('사진을 찍어 줄게. 브이~ ^-^v')

        time.sleep(5)
        print('여기 행동 촬영 들어갈 곳. 아마도?')
        time.sleep(2)
        break

        
    # 7) 다음 놀이 제안
    behavior_list.do_question()
    while True:
        tts('다음 놀이 할까?')

        os.system('python record.py')
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        if answer == 'YES':
            print(answer)
        elif answer == 'NO':
            print(answer)
        elif answer == 'SOSO':
            print(answer)
        # else:
        #     tts('말 다시')
        #     continue
        break
    
    motion_list.m_init()
    
    print("\n\n**시나리오 30: 풍선 축구 놀이 끄읏**\n\n")
