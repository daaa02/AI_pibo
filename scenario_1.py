# 1. 시나리오 구현: 대근육/소근육 놀이

import os
import time
import json
import requests

import openpibo
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

'''
def stt():
    rest_api_key = 'f8f8c3f66bb3310016fdeccffba152e8'

    kakao_speech_url = "https://kakaoi-newtone-openapi.kakao.com/v1/recognize"
    headers = {
        "Content-Type": "application/octet-stream",
        "X-DSS-Service": "DICTATION",
        "Authorization": "KakaoAK " + rest_api_key,
    }

    with open('stream.wav', 'rb') as fp:
        stream = fp.read()

    res = requests.post(kakao_speech_url, headers=headers, data=stream)
    # print(res.text)

    result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1]
    result_final = json.loads(result_json_string)
    result = result_final['value']
    print(result)
    return result


def tts(speech_text):
    file = openpibo.config['DATA_PATH'] + "/tts.wav"
    speech.tts(f"<speak>\
                <voice name='WOMAN_READ_CALM'><prosody rate='slow'>{speech_text}<break time='500ms'/></prosody></voice>\
                </speak>", file)
    audio.play(file, 'local', '-1000', False)
    print("\n")
    print(speech_text)
'''

###
def play_balloon_soccer():
    # 1) 준비물 설명
    behavior_list.do_question()
    while True:
        time.sleep(1)
        tts('풍선과 천을 준비할 수 있어?')
        break
    
    behavior_list.do_waiting()
    while True:
        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 6 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while answer != -1:
            if answer == 'YES':
                print(answer)
            elif answer == 'NO':
                print(answer)
                behavior_list.do_explain()
                while True:
                    time.sleep(1)
                    tts('이번 놀이는 천이 없어도 할 수 있어!')
                    break
#             else:
#                 tts('말 다시')
#                 os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
#                 user_input = stt()
#                 # user_input = input("input: ")
#                 answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
#                 print(answer)
#                 continue
            break
        break

    time.sleep(1)
    tts('풍선 준비가 되면 준비 완료 라고 말해줘')
    behavior_list.do_waiting()
    while True:
        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 6 -r 16000 stream.wav")
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
        time.sleep(1)
        tts('다영이가 좋아하는 색깔의 풍선을 골라봐.')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)
        print(answer)
        break

    # 3) 놀이 진행
    behavior_list.do_suggestion()
    while True:
        time.sleep(1)
        tts('자 이제 풍선을 불어보자. 할 수 있지?')
        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        if answer == 'YES':
            print(answer)
        elif answer == 'NO':
            print(answer)
            behavior_list.do_explain()
            while True:
                time.sleep(1)
                tts('엄마에게 도움을 요청하자')
                break
        # else:
        #     tts('말 다시')
        #     continue
        break
    
    time.sleep(1)
    behavior_list.do_suggestion()
    while True:
        time.sleep(1)
        tts('풍선을 묶지 말고 멀리 날려보자!')

        print('---여기 행동 촬영 들어갈 곳 1---')
        time.sleep(1)
        break

    behavior_list.do_joy()
    while True:
        time.sleep(2)
        tts('정말 재밌어보여!')
        break

    behavior_list.do_suggestion()
    while True:
        time.sleep(1)
        tts('이번에는 풍선으로 축구를 해보자')
        break

    # 4) 놀이 완료
    time.sleep(1)
    tts('마지막으로 축구 선수들처럼 발이나 무릎 높이로 던져보자.')
    tts('준비 됐어?')

    os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
    user_input = stt()
    # user_input = input("input: ")
    answer = nlp.nlp_done(user_input=user_input, dic=dic)

    if answer == 'DONE':
        print(answer)
    # else:
    #     tts('?')
    #     continue

    behavior_list.do_compliment()
    while True:
        time.sleep(2)
        tts('정말 축구 선수 같은 걸? 멋지다 !')
        break


    # 5) 마무리 대화
    behavior_list.do_question()
    while True:
        time.sleep(1)
        tts('풍선으로 하는 축구 놀이 재미있었어?')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
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

    behavior_list.do_sad()
    while True:
        tts('파이보는 달리느라 힘들었어.') 
        time.sleep(1)
        tts('다영이는 오늘 힘든 일 있었어?')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 6 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        if answer == 'YES':
            print(answer)
            behavior_list.do_agree()
            while True:
                time.sleep(2)
                tts('그랬구나, 다음에 그런 일이 또 생기면 주변에 도움을 요청해봐')
                break

        elif answer == 'NO':
            print(answer)
            behavior_list.do_joy()
            while True:
                time.sleep(2)
                tts('그랬구나!')
                break
        # else:
        #     break
        break

    # 6) 놀이 기록
    motion_list.m_init()
    tts('오늘은 튼튼 스탬프를 찍어줄게')
    behavior_list.do_stamp()
    while True:
        time.sleep(2)
        audio.play(filename=openpibo.config['DATA_PATH']+"/audio/스탬프소리1.mp3", out='local', volume=-1000, background=False)
        break    

    tts('사진을 찍어 줄게. 브이 해봐!')
    behavior_list.do_photo()
    while True:
        time.sleep(1)
        tts('하나, 둘, 셋 ')        
        audio.play(filename=openpibo.config['DATA_PATH']+"/audio/사진기소리.mp3", out='local', volume=-1000, background=False)
        print('---여기 행동 촬영 들어갈 곳 2---')
        motion_list.m_init()
        break

    # 7) 다음 놀이 제안
    behavior_list.do_question()
    while True:
        time.sleep(1)
        tts('다음 놀이 할까?')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
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

    tts('첫 번째 시나리오 풍선 축구 놀이 끝')
    motion_list.m_init()

    print("\n\n**시나리오 30: 풍선 축구 놀이 끄읏**\n\n")
