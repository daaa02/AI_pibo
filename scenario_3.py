# 3. 시나리오 구현: 의사소통/언어표현 놀이

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
def play_animal_in_hoop():
    # 1) 준비물 설명
    behavior_list.do_question()
    while True:
        time.sleep(1)
        tts('놀이를 위해 훌라후프와 크레파스, 신문지가 필요해.')
        tts('준비할 수 있어?')
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
                    tts('색연필이나 종이를 써도 좋아.')
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
    behavior_list.do_waiting()
    while True:
        time.sleep(1)
        tts('준비가 되면 준비 완료 라고 말해줘')

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
        tts('먼저 동물을 그리고 모양대로 자를거야.')
        tts('그리고 바람을 일으켜 훌라후프 안으로 동물들을 날려 넣을거야.')
        break

    behavior_list.do_question()
    while True:
        tts('할 수 있지?')
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
                    tts('바람은 입으로 불거나 부채를 활용하면 돼.')
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
    behavior_list.do_cheer()
    while True:
        time.sleep(1)
        tts('훌라후프 안에 다양한 동물을 넣어보자!')
        break
        
    time.sleep(1)
    behavior_list.do_question()
    while True:
        tts('준비됐지?')
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
        tts('너는 어떤 동물을 좋아해?')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_animal(user_input=user_input, dic=dic)
        print(answer)

        tts('그럼 먼저 ' + answer + '를 종이에 그려보자.')
        break

    behavior_list.do_waiting()
    while True:
        time.sleep(1)
        tts('다 그리면 알려줘!')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)

        if answer == 'DONE':
            print(answer)
        break

    behavior_list.do_compliment()
    while True:
        time.sleep(1)
        tts('정말 귀엽다! 이제 그림 모양대로 오려보자.')
        break

    behavior_list.do_waiting()
    while True:
        time.sleep(1)
        tts('다 오리면 알려줘!')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_done(user_input=user_input, dic=dic)

        if answer == 'DONE':
            print(answer)
        break

    behavior_list.do_suggestion()
    while True:
        time.sleep(1)
        tts('잘했어!')
        tts('그럼 이제 바람을 일으켜서 동물을을 훌라후프 안에 날려 넣자')

        print('---여기 행동 촬영 들어갈 곳 2---')
        time.sleep(2)
        break

    behavior_list.do_suggestion()
    while True:
        time.sleep(1)
        tts('곳곳에 휴지 섬을 만들어 보자. 휴지를 통째로 놓고 쌓아줘~')
        break

    # 4) 놀이 완료
    behavior_list.do_question()
    while True:
        time.sleep(1)
        tts('또 그리고 싶은 동물이 있어?')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        while answer != -1:
            if answer == 'YES':  # 다시 활동으로
                print(answer)
                print('# 다시 활동으로 - 아직 구현 X')
            elif answer == 'NO':  # 그만
                print(answer)
            else:
                tts('말 다시')
                # os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
                # user_input = stt()
                # user_input = input("input: ")
                answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)
                print(answer)
                continue
            break
        break
        
    time.sleep(1)
    behavior_list.do_compliment()
    while True:
        time.sleep(1)
        tts('다양한 동물을 그려서 훌라후프에 넣었어. 수고했어~')
        break

    # 5) 마무리 대화
    behavior_list.do_question()
    while True:
        time.sleep(1)
        tts('놀이 재미있었어?')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 7 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        answer = nlp.nlp_yes_or_no(user_input=user_input, dic=dic)

        if answer == 'YES':
            print(answer)
            behavior_list.do_joy()
            while True:
                time.sleep(2)
                tts('파이보도 너가 동물을 잘 그려줘서 재미있었어.')
                break

        elif answer == 'NO':
            print(answer)
            behavior_list.do_joy()
            while True:
                time.sleep(2)
                tts('아쉬운걸? 파이보는 너가 동물을 잘 그려줘서 재미있었어.')
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

    behavior_list.do_question()
    while True:
        time.sleep(1)
        tts('너는 어떤 동물을 키우고 싶어?')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        print(user_input)
        break

    behavior_list.do_joy()
    while True:
        time.sleep(1)
        tts('정말? 왜?')

        os.system("arecord -t wav -c 1 -D plughw:1,0 -f S16_LE -d 5 -r 16000 stream.wav")
        user_input = stt()
        # user_input = input("input: ")
        print(user_input)
        break

    behavior_list.do_agree()
    while True:
        time.sleep(2)
        tts('그렇구나. 키우면 정말 좋겠다!')
        break

    # 6) 놀이 기록
    time.sleep(1)
    tts('오늘은 술술 스탬프를 찍어줄게')
    behavior_list.do_stamp()
    while True:
        time.sleep(2)
        audio.play(filename=openpibo.config['DATA_PATH']+"/audio/스탬프소리1.mp3", out='local', volume=-1000, background=False)
        break

    tts('사진을 찍어 줄게. 브으으으으이~!')
    behavior_list.do_photo()
    while True:
        time.sleep(2)
        print('---여기 행동 촬영 들어갈 곳 2---')
        audio.play(filename=openpibo.config['DATA_PATH']+"/audio/사진기소리.mp3", out='local', volume=-1000, background=False)
        time.sleep(2)
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

    tts('세 번째 시나리오 훌라후프에 동물 넣기 놀이 끝')
    motion_list.m_init()

    print("\n\n**시나리오 45: 훌라후프에 동물 넣기 놀이 끄읏**\n\n")
