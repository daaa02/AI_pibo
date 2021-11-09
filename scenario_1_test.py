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
import oled_list
import behavior_list

from NLP import nlp, Dictionary

nlp = nlp()
dic = Dictionary()

speech = Speech()
audio = Audio()


def record():
    os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")


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
    filename = openpibo.config['DATA_PATH'] + "/tts.mp3"
    speech.tts(
        f"<speak><voice name='WOMAN_READ_CALM'><prosody rate='slow'>{speech_text}<break time='1500ms'/></voice></prosody></speak>",
        filename)
    audio.play(filename, out='local', volume=-2000, background=False)
    print(speech_text)


###
def play_balloon_soccer():

    motion_list.m_init()    # 모션 초기화

    # 1) 준비물 설명
    o1 = Thread(target=oled_list.o_question(), args=())
    m1 = Thread(target=motion_list.m_question(), args=())
    t1 = Thread(target=tts('풍선과 천을 준비할 수 있어?'), args=())
    o1.daemon = True
    m1.daemon = True
    t1.daemon = True
    o1.start()
    m1.start()
    t1.start()

    record()
    user_input = stt()
    # user_input = input("input: ")
    answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

    while answer != -1:
        if answer == 'YES':
            print(answer)
        elif answer == 'NO':
            print(answer)
            while True:
                m2 = Thread(target=motion_list.m_question(), args=())
                t2 = Thread(target=tts('이번 놀이는 천이 없어도 할 수 있어!'), args=())
                m2.daemon = True
                t2.daemon = True
                m2.start()
                t2.start()
        else:
            tts('말 다시')
            record()
            user_input = stt()
            # user_input = input("input: ")
            answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
            print(answer)
            continue
        break


    while True:
        o3 = Thread(target=oled_list.o_waiting, args=())
        m3 = Thread(target=motion_list.m_waiting(), args=())
        t3 = Thread(target=tts('풍선 준비가 되면 준비 완료 라고 말해줘'), args=())
        o3.daemon = True
        m3.daemon = True
        t3.daemon = True
        o3.start()
        m3.start()
        t3.start()

        record()
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)

        if answer == 'DONE':
            print(answer)
        else:
            tts('말 다시')
            record()
            user_input = stt()
            # user_input = input("input: ")
            answer = nlp.nlp_done(user_input=user_input, dic=dic)
            print(answer)
            continue

        while True:
            o4 = Thread(target=oled_list.o_suggestion(), args=())
            m4 = Thread(target=motion_list.m_suggestion(), args=())
            t4 = Thread(target=tts('너가 좋아하는 색깔의 풍선을 골라봐.'), args=())
            o4.daemon = True
            m4.daemon = True
            t4.daemon = True
            o4.start()
            m4.start()
            t4.start()

            record()
            user_input = stt()
            # user_input = input("input: ")
            answer = nlp.nlp_done(user_input=user_input, dic=dic)
            print(answer)

            while True:
                o5 = Thread(target=oled_list.o_suggestion(), args=())
                m5 = Thread(target=motion_list.m_suggestion(), args=())
                t5 = Thread(target=tts('자 이제 풍선을 불어보자. 할 수 있지?'), args=())
                o5.daemon = True
                m5.daemon = True
                t5.daemon = True
                o5.start()
                m5.start()
                t5.start()

                record()
                user_input = stt()
                # user_input = input("input: ")
                answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

                if answer == 'YES':
                    print(answer)
                elif answer == 'NO':
                    print(answer)
                    tts('엄마에게 도움을 요청해')
                    time.sleep(3)
                else:
                    tts('말 다시')
                    record()
                    user_input = stt()
                    # user_input = input("input: ")
                    answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
                    print(answer)
                    continue

                while True:
                    o6 = Thread(target=oled_list.o_suggestion(), args=())
                    m6 = Thread(target=motion_list.m_suggestion(), args=())
                    t6 = Thread(target=tts('풍선을 묶지 말고 멀리 날려보자!'), args=())
                    o6.daemon = True
                    m6.daemon = True
                    t6.daemon = True
                    o6.start()
                    m6.start()
                    t6.start()

                    print("여기 행동 촬영 들어갈 곳 1")
                    time.sleep(2)

                    while True:
                        o7 = Thread(target=oled_list.o_joy(), args=())
                        m7 = Thread(target=motion_list.m_joy(), args=())
                        t7 = Thread(target=tts('정말 재밌어 보여!'), args=())
                        o7.daemon = True
                        m7.daemon = True
                        t7.daemon = True
                        o7.start()
                        m7.start()
                        t7.start()

                        while True:
                            o8 = Thread(target=oled_list.o_suggestion(), args=())
                            m8 = Thread(target=motion_list.m_suggestion(), args=())
                            t8 = Thread(target=tts('다음엔 풍선 축구를 해볼까?'), args=())
                            o8.daemon = True
                            m8.daemon = True
                            t8.daemon = True
                            o8.start()
                            m8.start()
                            t8.start()

                            while True:
                                o9 = Thread(target=oled_list.o_question(), args=())
                                m9 = Thread(target=motion_list.m_question(), args=())
                                t9 = Thread(target=tts('축구 선수처럼 발 혹은 무릎 높이로 차보자. 준비 됐어?'), args=())
                                o9.daemon = True
                                m9.daemon = True
                                t9.daemon = True
                                o9.start()
                                m9.start()
                                t9.start()

                                record()
                                user_input = stt()
                                # user_input = input("input: ")
                                answer = nlp.nlp_done(user_input=user_input, dic=dic)

                                if answer == 'DONE':
                                    print(answer)
                                else:
                                    tts('말 다시')
                                    record()
                                    user_input = stt()
                                    # user_input = input("input: ")
                                    answer = nlp.nlp_done(user_input=user_input, dic=dic)
                                    print(answer)
                                    continue

                                while True:
                                    o10 = Thread(target=oled_list.o_compliment(), args=())
                                    m10 = Thread(target=motion_list.m_compliment(), args=())
                                    t10 = Thread(target=tts('잘한다! 이번엔 머리로 헤딩슛을 해보자!'), args=())
                                    o10.daemon = True
                                    m10.daemon = True
                                    t10.daemon = True
                                    o10.start()
                                    m10.start()
                                    t10.start()

                                    while True:
                                        o11 = Thread(target=oled_list.o_question(), args=())
                                        m11 = Thread(target=motion_list.m_question(), args=())
                                        t11 = Thread(target=tts('풍선으로 하는 축구 놀이 재미있었어?'), args=())
                                        o11.daemon = True
                                        m11.daemon = True
                                        t11.daemon = True
                                        o11.start()
                                        m11.start()
                                        t11.start()

                                        record()
                                        user_input = stt()
                                        # user_input = input("input: ")
                                        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

                                        if answer == 'YES':
                                            print(answer)
                                        elif answer == 'NO':
                                            print(answer)

                                        while True:
                                            o12 = Thread(target=oled_list.o_sad(), args=())
                                            m12 = Thread(target=motion_list.m_sad(), args=())
                                            t12 = Thread(target=tts('파이보는 달리느라 힘들었어. 너는 오늘 힘든 일 있었어?'), args=())
                                            o12.daemon = True
                                            m12.daemon = True
                                            t12.daemon = True
                                            o12.start()
                                            m12.start()
                                            t12.start()

                                            record()
                                            user_input = stt()
                                            # user_input = input("input: ")
                                            answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

                                            if answer == 'YES':
                                                print(answer)

                                                o13 = Thread(target=oled_list.o_sad(), args=())
                                                m13 = Thread(target=motion_list.m_sad(), args=())
                                                t13 = Thread(target=tts('그랬구나, 다음에 그런 일이 또 생기면 주변에 도움을 요청해봐'), args=())
                                                o13.daemon = True
                                                m13.daemon = True
                                                t13.daemon = True
                                                o13.start()
                                                m13.start()
                                                t13.start()

                                            elif answer == 'NO':
                                                print(answer)

                                                o14 = Thread(target=oled_list.o_joy(), args=())
                                                m14 = Thread(target=motion_list.m_joy(), args=())
                                                t14 = Thread(target=tts('그랬구나!'), args=())
                                                o14.daemon = True
                                                m14.daemon = True
                                                t14.daemon = True
                                                o14.start()
                                                m14.start()
                                                t14.start()

                                            while True:
                                                o15 = Thread(target=oled_list.o_stamp(), args=())
                                                m15 = Thread(target=motion_list.m_stamp(), args=())
                                                t15 = Thread(target=tts('오늘은 튼튼 스탬프를 찍어줄게'), args=())
                                                o15.daemon = True
                                                m15.daemon = True
                                                t15.daemon = True
                                                o15.start()
                                                m15.start()
                                                t15.start()

                                                while True:
                                                    o16 = Thread(target=oled_list.o_photo(), args=())
                                                    m16 = Thread(target=motion_list.m_photo(), args=())
                                                    t16 = Thread(target=tts('사진을 찍어줄게. 브~~이!'), args=())
                                                    o16.daemon = True
                                                    m16.daemon = True
                                                    t16.daemon = True
                                                    o16.start()
                                                    m16.start()
                                                    t16.start()

                                                    while True:
                                                        o17 = Thread(target=oled_list.o_question(), args=())
                                                        m17 = Thread(target=motion_list.m_question(), args=())
                                                        t17 = Thread(target=tts('다음 놀이 할까?'), args=())
                                                        o17.daemon = True
                                                        m17.daemon = True
                                                        t17.daemon = True
                                                        o17.start()
                                                        m17.start()
                                                        t17.start()

                                                        record()
                                                        user_input = stt()
                                                        # user_input = input("input: ")
                                                        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

                                                        if answer == 'YES':
                                                            print(answer)
                                                        elif answer == 'NO':
                                                            print(answer)
                                                        elif answer == 'SOSO':
                                                            print(answer)
                                                        break
                                                    break
                                                break
                                            break
                                        break
                                    break
                                break
                            break
                        break
                    break
                break
            break
        break

    motion_list.m_init()

    print("\n\n**시나리오 30: 풍선 축구 놀이 끄읏**\n\n")
