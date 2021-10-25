# 4. 시나리오 구현: 사회성/정서 놀이
import time
import openpibo

from config.motion_list import Motion
from config.eye_list import Eye
from NLP import nlp, Dictionary

nlp = nlp()


def tts(speech_text):
    filename = openpibo.config['DATA_PATH'] + "/tts.mp3"
    pibo.tts(f"<speak><voice name='WOMAN_READ_CALM'>{speech_text}<break time='2000ms'/></voice></speak>", filename)
    pibo.play_audio(filename, out='local', volume=-2000, background=False)


def speech_yes_or_no():
    user_in = input("input: ")
    user_input = nlp.nlp_yes_or_no(input=user_in, dic=Dictionary)
    print("input = {}".format(user_input) + '\n')
    return user_input


def speech_done():
    user_in = input("input: ")
    user_input = nlp.nlp_done(input=user_in, dic=Dictionary)
    print("input = {}".format(user_input) + '\n')
    return user_input


def play_soccer():
    # 1) 준비물 설명


    # 2) 놀이 설명


    # 3) 놀이 진행


    # 4) 놀이 완료


    # 5) 마무리 대화


    # 6) 놀이 기록
    speech('오늘은 창작 스탬프를 찍을게')
    speech('사진을 찍어 줄게. 브이~ ^-^v')

    # 7) 다음 놀이 제안
    speech('다음 놀이 할까?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            break
        elif speech_yes_or_no().input == 'NO':
            break
        elif speech_yes_or_no().input == 'SOSO':
            break
        else:
            speech('말 다시')
            continue
