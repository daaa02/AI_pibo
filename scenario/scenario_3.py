# 3. 시나리오 구현: 의사소통/언어표현 놀이
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


def play_animal():
    # 1) 준비물 설명
    tts('놀이를 위해 훌라후프와 크레파스, 신문지가 필요해. 준비할 수 있어?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            break
        elif speech_yes_or_no().user_input == 'NO':
            tts('색연필이나 종이를 써도 좋아.')
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
    tts('먼저 동물을 그리고 모양대로 자를거야.')
    tts('그리고 바람을 일으켜 훌라후프 안으로 동물들을 날려 넣을거야. 할 수 있지?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            break
        elif speech_yes_or_no().user_input == 'NO':
            tts('바람은 입으로 불거나 부채를 활용하면 돼.')
            break
        else:
            tts('말 다시')
            continue

    tts('훌라후프 안에 다양한 동물을 넣어보자! 준비됐지?')
    speech_done()

    while speech_done().user_input != -1:
        if speech_done().user_input == 'DONE':
            break
        else:
            continue

    # 3) 놀이 진행
    tts('너는 어떤 동물을 좋아해?')
    user_in = input("input: ")
    user_input = nlp.nlp_animal(input=user_in, dic=dic)
    print("input = {}".format(user_input) + '\n')

    tts('그럼 먼저 ') + tts(user_input) + tts('를 종이에 그려보자. 다 그리면 보여줘!')
    speech_done()

    while speech_done().user_input != -1:
        if speech_done().user_input == 'DONE':
            break
        else:
            continue

    tts('정말 귀엽다! 이제 그림 모양대로 오려보자. 다 오리면 알려줘.')
    speech_done()

    while speech_done().user_input != -1:
        if speech_done().user_input == 'DONE':
            break
        else:
            continue

    tts('잘했어! 그럼 이제 바람을 일으켜서 동물을을 훌라후프 안에 날려 넣자!')
    # m_photo()
    tts('잘 하는 걸?')

    # 4) 놀이 완료
    tts('또 그리고 싶은 동물이 있어?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            tts('좋아. 어떤 동물을 그려볼까?')
            # 다시 활동으로
        elif speech_yes_or_no().user_input == 'NO':
            tts('수고 했어~')
            break
        else:
            tts('말 다시')
            continue

    # 5) 마무리 대화
    tts('놀이는 재미있었어?')
    speech_yes_or_no()

    while speech_yes_or_no().user_input != -1:
        if speech_yes_or_no().input == 'YES':
            tts('파이보도 너가 동물을 잘 그려줘서 재미있었어.')
            break
        elif speech_yes_or_no().user_input == 'NO':
            tts('아쉬운걸? 파이보는 너가 동물을 잘 그려줘서 재미있었어.')
            break
        else:
            continue

    tts('너는 어떤 동물을 키우고 싶어?')
    # 그냥 녹음
    tts('왜~?')
    # 그냥 녹음
    tts('그렇구나. 키우면 정말 좋겠다!')

    # 6) 놀이 기록
    tts('오늘은 창작 스탬프를 찍을게')
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
