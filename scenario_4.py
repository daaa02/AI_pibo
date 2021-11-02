# 4. 시나리오 구현: 사회성/정서 놀이

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
        stream = fp.read()

    res = requests.post(kakao_speech_url, headers=headers, data=stream)
    # print(res.text)

    result_json_string = res.text[res.text.index('{"type":"finalResult"'):res.text.rindex('}') + 1]
    result_final = json.loads(result_json_string)
    result = result_final['value']
    print(result)
    return result


def tts(speech_text):
    filename = openpibo.config['DATA_PATH'] + "/tts.mp3"
    speech.tts(f"<speak><voice name='WOMAN_READ_CALM'><prosody rate='slow'>{speech_text}<break time='1500ms'/></voice></prosody></speak>", filename)
    audio.play(filename, out='local', volume=-2000, background=False)
    print(speech_text)


###
def play_im_king():
    # 1) 준비물 설명
    behavior_list.do_explain()
    while True:
        time.sleep(2)
        tts('\n놀이를 위해 왕관이 필요해. 준비할 수 있어?')
        break

    behavior_list.do_question()
    while True:
        # os.system('python record.py')
        # user_input = stt()
        user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while answer != -1:
            if answer == 'YES':
                print(answer)
            elif answer == 'NO':
                print(answer)
                tts('왕관 대신 모자를 준비해도 좋아.')
            else:
                tts('말 다시')
                # os.system('python record.py')
                # user_input = stt()
                user_input = input("input: ")
                answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
                print(answer)
                continue
            break
        break

    behavior_list.do_waiting()
    while True:
        tts('준비가 되면 준비 완료 라고 말해줘')

        # os.system('python record.py')
        # user_input = stt()
        user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)

        if answer == 'DONE':
            print(answer)
        # else:
        #     continue
        break

    # 2) 놀이 설명
    behavior_list.do_explain()
    while True:
        time.sleep(2)
        tts('\n파이보가 왕이다!를 외치면, 먼저 왕관을 쓴 사람이 왕이 되는 거야.')
        tts('시민은 왕의 행동을 그대로 따라해야해.')
        tts('할 수 있지?')
        break

    behavior_list.do_question()
    while True:
        # os.system('python record.py')
        # user_input = stt()
        user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while answer != -1:
            if answer == 'YES':
                print(answer)
            elif answer == 'NO':
                print(answer)
                tts('재빨리 왕관을 차지하면, 시민들이 왕을 따라할거야.')
            else:
                tts('말 다시')
                # os.system('python record.py')
                # user_input = stt()
                user_input = input("input: ")
                answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
                print(answer)
                continue
            break
        break

    behavior_list.do_explain()
    while True:
        tts('왕이 왕관을 벗어서 상대방에게 씌워주면 그 사람은 왕이 될 수 있어!')
        break

    behavior_list.do_question()
    while True:
        tts('준비 됐어?')

        # os.system('python record.py')
        # user_input = stt()
        user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)

        if answer == 'DONE':
            print(answer)
        break


    # 3) 놀이 진행
    behavior_list.do_explain()
    while True:
        tts('\n왕관을 먼저 중앙에 놓아줘')
        time.sleep(2)

        # os.system('python record.py')
        # user_input = stt()
        user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
        print(answer)
        break

    behavior_list.do_question()
    while True:
        time.sleep(1)
        tts('왕이다!!')

        time.sleep(5)
        print('여기 행동 촬영 들어갈 곳. 아마도?')
        time.sleep(2)
        break

    behavior_list.do_question()
    while True:
        tts('누가 왕이 됐어?')

        # os.system('python record.py')
        # user_input = stt()
        user_input = input("input: ")
        print(user_input)
        break

    behavior_list.do_suggestion()
    while True:
        tts('그럼 시민은 왕을 따라해보자!')

        time.sleep(5)
        print('여기 행동 촬영 들어갈 곳. 아마도?')
        time.sleep(2)
        break


    # 4) 놀이 완료
    behavior_list.do_question()
    while True:
        tts('\n또 왕이 되고 싶은 사람 있어?')

        # os.system('python record.py')
        # user_input = stt()
        user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while answer != -1:
            if answer == 'YES':     # 다시 활동으로
                print(answer)
                print('# 다시 활동으로 - 아직 구현 X')
            elif answer == 'NO':    # 그만
                print(answer)
            else:
                tts('말 다시')
                # os.system('python record.py')
                # user_input = stt()
                user_input = input("input: ")
                answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
                print(answer)
                continue
            break
        break

    behavior_list.do_compliment()
    while True:
        time.sleep(2)
        tts('정말 훌륭한 왕과 시민이었어!')
        tts('고생했어~')
        break


    # 5) 마무리 대화
    behavior_list.do_question()
    while True:
        tts('\n놀이 재미있었어?')
        break

    # os.system('python record.py')
    # user_input = stt()
    user_input = input("input: ")
    answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

    while answer != -1:
        if answer == 'YES':
            print(answer)
            behavior_list.do_joy()
            while True:
                time.sleep(2)
                tts('파이보도 너가 역할을 잘 해내서 재미있었어.')
                break

        elif answer == 'NO':
            print(answer)
            behavior_list.do_joy()
            while True:
                time.sleep(2)
                tts('아쉬운걸? 파이보는 너가 역할을 잘 해내서 재미있었어.')
                break

        else:
            tts('말 다시')
            # os.system('python record.py')
            # user_input = stt()
            user_input = input("input: ")
            answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
            print(answer)
            continue
        break

    behavior_list.do_question()
    while True:
        tts('왕이 재미있었어, 아니면 시민이 재미있었어?')

        # os.system('python record.py')
        # user_input = stt()
        user_input = input("input: ")
        print(user_input)
        break

    behavior_list.do_joy()
    while True:
        time.sleep(2)
        tts('정말? 왜?')
        # os.system('python record.py')
        # user_input = stt()
        user_input = input("input: ")
        print(user_input)
        break

    behavior_list.do_compliment()
    while True:
        time.sleep(2)
        tts('그렇구나. 시민과 왕을 서로 양보하는 모습이 보기 좋았어!')
        break


    # 6) 놀이 기록
    behavior_list.do_stamp()
    while True:
        time.sleep(3)
        tts('\n오늘은 바른 스탬프를 찍어줄게')
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
        tts('\n다음 놀이 할까?')

        # os.system('python record.py')
        # user_input = stt()
        user_input = input("input: ")
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

    print("\n\n**시나리오 13: 나는 와아아앙 놀이 끄읏**\n\n")