# 2. 시나리오 구현: 인지/지각/사고 놀이

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


###
def play_tissue_load():
    # 1) 준비물 설명
    behavior_list.do_question()
    while True:
        time.sleep(1)
        tts('놀이를 위해 휴지가 필요해. 준비할 수 있어?')
        break

    behavior_list.do_waiting()
    while True:
        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
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
                    tts('휴지는 화장실에도 많을거야')
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
    tts('준비가 되면 준비 완료 라고 말해줘')
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
    behavior_list.do_explain()
    while True:
        time.sleep(1)
        tts('휴지를 풀어서 길을 만들어 볼거야.')        
        break
        
    time.sleep(1)
    behavior_list.do_question()
    tts('할 수 있지?')
    while True:
        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
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
                    tts('휴지를 뜯어서 하나의 길로 연결하면 돼')
                    break
            else:
                tts('말 다시')
                os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
                user_input = stt()
                # user_input = input("input: ")
                answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
                print(answer)
                continue
            break
        break
    
    time.sleep(1)
    behavior_list.do_explain()
    while True:
        time.sleep(1)
        tts('휴지 길은 미끄러울 수 있으니 뛰면 안 돼.')
        break

    behavior_list.do_question()
    while True:
        tts('준비 됐지?')
        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)

        if answer == 'DONE':
            print(answer)
        break

    # 3) 놀이 진행
    behavior_list.do_explain()
    while True:
        time.sleep(1)
        tts('휴지 길을 만들어 보자!') 
        tts('다 만들면 알려줘')
        break

    behavior_list.do_waiting()
    while True:
        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 6 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)

        while answer != -1:
            if answer == 'DONE':
                print(answer)
            else:
                tts('휴지를 짧게 뜯으면 모양을 만들기 쉬워')
                os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
                user_input = stt()
                # user_input = input("input: ")
                answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
                print(answer)
                continue
            break
        break

    behavior_list.do_compliment()
    while True:
        time.sleep(2)
        tts('정말 멋진 길이 완성되었는걸?')
        break

    behavior_list.do_suggestion()
    while True:
        time.sleep(1)
        tts('천천히 걸어보자')

        print('---여기 행동 촬영 들어갈 곳 3---')
        time.sleep(2)
        break

    behavior_list.do_suggestion()
    while True:
        time.sleep(1)
        tts('곳곳에 휴지 섬을 만들어 보자. 휴지를 통째로 놓고 쌓아줘~')
        break

    # 4) 놀이 완료
    motion_list.m_init()
    behavior_list.do_waiting()
    while True:
        time.sleep(1)
        tts('휴지 성을 완성하면 말해줘~')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
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
        time.sleep(1)
        tts('정말 열심히 만들었는걸? 휴지로 만들어서 포근해보여')
        break

    behavior_list.do_suggestion()
    while True:
        time.sleep(1)
        tts('파이보가 사진찍어서 부모님께도 보여드릴게. 깜짝 놀라실거야!')
        time.sleep(1)
        break


    # 5) 마무리 대화
    behavior_list.do_suggestion()
    while True:
        tts('길을 만들 때 쓴 휴지를 찢어서 휴지 성에 눈을 내리자')
        time.sleep(2)
        break

    behavior_list.do_compliment()
    while True:
        tts('휴지 눈이 내리니까 정말 포근하다.') 
        tts('다영이는 언제 포근함을 느껴?')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        print(user_input)
        break

    behavior_list.do_question()
    while True:
        time.sleep(1)
        tts('정말? 왜?')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        print(user_input)
        break

    time.sleep(1)
    behavior_list.do_joy()
    while True:
        time.sleep(1)
        tts('생각만 해도 기분이 좋아!')
        break


    # 6) 놀이 기록
    motion_list.m_init()
    tts('오늘은 똑똑 스탬프를 찍어줄게')
    behavior_list.do_stamp()
    while True:
        time.sleep(2)
        audio.play(filename=openpibo.config['DATA_PATH']+"/audio/스탬프소리2.wav", out='local', volume=-1000, background=False)
        break

    tts('사진을 찍어 줄게. 브이 해봐!')
    behavior_list.do_photo()
    while True:
        time.sleep(1)
        tts('하나, 둘, 셋 ')        
        audio.play(filename=openpibo.config['DATA_PATH']+"/audio/사진기소리.mp3", out='local', volume=-1000, background=False)
        print('---여기 행동 촬영 들어갈 곳 6---')
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

    tts('두 번째 시나리오 휴지 길 놀이 끝')
    motion_list.m_init()

    print("\n\n**시나리오 6: 휴지길 놀이 끄읏**\n\n")

