# 2. 시나리오 구현: 인지/지각/사고 놀이
import time
import openpibo

from config.motion_list import Motion
from config.eye_list import Eye
from NLP import nlp, Dictionary

nlp = nlp()


def speech(speech_text):
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


def play_tissue():
    # 1) 준비물 설명
    speech('놀이를 위해 휴지가 필요해. 준비할 수 있어?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            break
        elif speech_yes_or_no().user_input == 'NO':
            speech('휴지는 화장실에도 많을거야.')
            break
        else:
            speech('말 다시')
            continue

    speech('준비가 되면 준비 완료 라고 말해줘')
    speech_done()

    while speech_done().user_input != -1:
        if speech_done().user_input == 'DONE':
            break
        else:
            continue

    # 2) 놀이 설명
    speech('휴지를 풀어서 길을 만들어 볼거야. 할 수 있지?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            break
        elif speech_yes_or_no().user_input == 'NO':
            speech('휴지를 뜯어서 하나의 길로 연결해보자!')
            break
        else:
            speech('말 다시')
            continue

    speech('휴지 길은 미끄러울 수 있으니 뛰면 안 돼. 준비됐지?')
    speech_done()

    while speech_done().user_input != -1:
        if speech_done().user_input == 'DONE':
            break
        else:
            continue

    # 3) 놀이 진행
    speech('휴지 길을 만들어 보자! 다 만들면 알려줘')
    speech_done()

    while speech_done().user_input != -1:
        if speech_done().user_input == 'DONE':
            break
        else:
            speech('휴지를 짧게 뜯으면 모양을 만들기 쉬울거야.')
            continue

    speech('정말 멋진 길이 완성되었는걸? 천천히 걸어보자')

    speech('곳곳에 휴지 섬을 만들어 보자. 휴지를 통째로 놓고 쌓아줘~')

    # 4) 놀이 완료
    speech('휴지 성을 완성하면 말해줘~')
    speech_done()

    while speech_done().user_input != -1:
        if speech_done().user_input == 'DONE':
            break
        else:
            continue

    speech('정말 열심히 만들었는걸? 휴지로 만들어서 포근해보여')
    speech('파이보가 사진찍어서 부모님께도 보여드릴게. 깜짝 놀라실거야!')

    # 5) 마무리 대화
    speech('길을 만들 때 쓴 휴지를 찢어서 휴지 성에 눈을 내리자')
    speech('휴지 눈이 내리니까 정말 포근해. 너는 언제 포근함을 느껴?')
    # 그냥 녹음만
    speech('정말? 왜?')
    # 그냥 녹음만
    speech('생각만 해도 기분이 좋아!')

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
