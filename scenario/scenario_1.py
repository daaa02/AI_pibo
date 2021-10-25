# 1. 시나리오 구현: 대근육/소근육 놀이
import time
import openpibo

from config.motion_list import Motion
from config.eye_list import Eye
from NLP import nlp, Dictionary
from openpibo.speech import Speech
from openpibo.audio import Audio

nlp = nlp()
speech = Speech()
audio = Audio()


def stt():
    result = speech.stt()
    print(result)
    return result['value']


def tts(speech_text):
    filename = openpibo.config['DATA_PATH'] + "/tts.mp3"
    audio.tts(f"<speak><voice name='WOMAN_READ_CALM'>{speech_text}<break time='2000ms'/></voice></speak>", filename)
    audio.play(filename, out='local', volume=-2000, background=False)


def speech_yes_or_no():
    # user_in = stt()
    user_in = input("input: ")
    user_input = nlp.nlp_yes_or_no(input=user_in, dic=Dictionary)
    print("input = {}".format(user_input) + '\n')
    return user_input


def speech_done():
    # user_in = stt()
    user_in = input("input: ")
    user_input = nlp.nlp_done(input=user_in, dic=Dictionary)
    print("input = {}".format(user_input) + '\n')
    return user_input


###
def play_soccer():
    from multiprocessing import Process

    # 1) 준비물 설명
    # Process(target=Motion.m_suggestion()).start()
    # Process(target=Eye.e_suggestion()).start()

    tts('풍선과 천을 준비할 수 있어?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            break
        elif speech_yes_or_no().user_input == 'NO':
            tts('이번 놀이는 천이 없어도 할 수 있어!')
            break
        else:
            tts('말 다시')
            continue

    tts('준비가 되면 준비 완료 라고 말해줘')
    speech_done()

    while speech_done().user_input != -1:
        if speech_done().user_input == 'DONE':
            break
        else:
            continue

    # 2) 놀이 설명
    tts('너가 좋아하는 색깔의 풍선을 골라봐.')
    speech_yes_or_no()

    # 3) 놀이 진행
    tts('자 이제 풍선을 불어보자. 할 수 있지?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            break
        elif speech_yes_or_no().input == 'NO':
            tts('엄마에게 도움을 요청해')
            break
        else:
            tts('말 다시')
            continue

    tts('풍선을 묶지 말고 멀리 날려보자!')
    # m_photo()
    tts('정말 재밌어보여! 다음엔 풍선 축구를 해볼까?')

    # 4) 놀이 완료
    tts('축구 선수처럼 발 혹은 무릎 높이로 차보자. 준비 됐어?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            break
        elif speech_yes_or_no().input == 'NO':
            tts('??')
            break
        else:
            tts('말 다시')
            continue
    tts('잘한다! 이번엔 머리로 헤딩슛을 해보자!')

    # 5) 마무리 대화
    tts('풍선으로 하는 축구 놀이 재미있었어?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            break
        elif speech_yes_or_no().input == 'NO':
            break
        else:
            break

    tts('파이보는 달리느라 힘들었어. 너는 오늘 힘든 일 있었어?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        # 그냥 녹음만
        tts('그랬구나, 다음에 그런 일이 또 생기면 주변에 도움을 요청해봐')

    # 6) 놀이 기록
    tts('오늘 놀이 스탬프를 찍을게')
    tts('사진을 찍어 줄게. 브이~ ^-^v')

    # 7) 다음 놀이 제안
    tts('다음 놀이 할까?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            break
        elif speech_yes_or_no().input == 'NO':
            break
        elif speech_yes_or_no().input == 'SOSO':
            break
        else:
            tts('말 다시')
            continue
