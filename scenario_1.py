# 1. 시나리오 구현: 대근육/소근육 놀이

import sys
import time
from threading import Thread

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


def stt():
    result = speech.stt()
    print(result)
    return result['value']


def tts(speech_text):
    filename = openpibo.config['DATA_PATH'] + "/tts.mp3"
    speech.tts(f"<speak><voice name='WOMAN_READ_CALM'>{speech_text}<break time='2000ms'/></voice></speak>", filename)
    audio.play(filename, out='local', volume=-2000, background=False)
    print(speech_text)


###
def play_soccer():
    # 1) 준비물 설명
    behavior_list.do_explain()
    while True:
        time.sleep(2)
        tts('풍선과 천을 준비할 수 있어?')
        break

    behavior_list.do_waiting()
    while True:
        user_input = input("input: ")
        user_in = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while user_in != -1:
            if user_in == 'YES':
                break
            elif user_in == 'NO':
                tts('이번 놀이는 천이 없어도 할 수 있어!')
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
        tts('너가 좋아하는 색깔의 풍선을 골라봐.')
        user_input = input("input: ")
        # user_in = nlp.nlp_done(user_input=user_input, dic=dic)
        break

    # 3) 놀이 진행
    behavior_list.do_suggestion()
    while True:
        tts('자 이제 풍선을 불어보자. 할 수 있지?')
        user_input = input("input: ")
        user_in = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while user_in != -1:
            if user_in == 'YES':
                break
            elif user_in == 'NO':
                behavior_list.do_explain()
                while True:
                    tts('엄마에게 도움을 요청해')
                    time.sleep(3)
                    break
                break
            else:
                tts('말 다시')
                continue
        break

    behavior_list.do_suggestion()
    while True:
        tts('풍선을 묶지 말고 멀리 날려보자!')
        behavior_list.do_photo()
        while True:
            time.sleep(5)
            print('여기 opencv capture 들어갈 곳. 아마도?')
            break
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
        user_input = input("input: ")
        user_in = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
        break
    while user_in != -1:
        if user_in == 'YES':
            break
        elif user_in == 'NO':
            tts('??')
            break
        else:
            tts('말 다시')
            continue

    behavior_list.do_compliment()
    while True:
        tts('잘한다! 이번엔 머리로 헤딩슛을 해보자!')
        behavior_list.do_cheer()
        while True:
            time.sleep(5)
            break
        break

    # 5) 마무리 대화
    behavior_list.do_question()
    while True:
        tts('풍선으로 하는 축구 놀이 재미있었어?')

        user_input = input("input: ")
        user_in = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while user_in != -1:
            if user_in == 'YES':
                break
            elif user_in == 'NO':
                break
            else:
                break
        break

    behavior_list.do_tired()
    while True:
        tts('파이보는 달리느라 힘들었어. 너는 오늘 힘든 일 있었어?')

        user_input = input("input: ")
        user_in = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
        break

    while user_in != -1:
        if user_in == 'YES':
            behavior_list.do_sad()
            while True:
                tts('그랬구나, 다음에 그런 일이 또 생기면 주변에 도움을 요청해봐')
                time.sleep(5)
                break
            break

        elif user_in == 'NO':
            behavior_list.do_joy()
            while True:
                tts('그랬구나!')
                time.sleep(5)
                break
            break
        else:
            break


    # 6) 놀이 기록
    behavior_list.do_stamp()
    while True:
        tts('오늘 놀이 스탬프를 찍을게')
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

    print("시나리오 30: 풍선 축구 놀이 끄읏")
