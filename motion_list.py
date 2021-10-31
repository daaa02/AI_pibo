import time
from openpibo.motion import Motion

"""
Motor number
0:왼발, 1:왼다리, 2:왼팔, 3:왼손, 4:머리_pan, 5:머리_tilt, 6:오른발, 7:오른다리, 8:오른팔, 9:오른손
0:25,  1:35,    2: 80,  3:30,  4:50,       5:25,       6:25,    7:35,      8:80,     9:30

movetime: 행동 A에서 행동 B로 넘어가는데 걸리는 시간
ex) 행동 A = 1000, 행동 B = 4000 이면, A->B로 모터가 움직이는 시간이 4초;
"""


def m_question():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 45, 0, 0, 20, 0, 0, -45, 0], movetime=200)
        o.set_motors(positions=[0, 0, 45, 30, 0, 20, 0, 0, -45, -30], movetime=200)
        break


def m_suggestion():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 80, 0, 10, 0, 0, 0, -80, 0], movetime=300)
        o.set_motors(positions=[0, 0, 80, 0, 20, 0, 0, 0, -80, 0], movetime=300)
        o.set_motors(positions=[0, 0, 80, -20, 20, 0, 0, 0, -80, 20], movetime=200)  # 흔
        o.set_motors(positions=[0, 0, 80, 20, 20, 0, 0, 0, -80, -20], movetime=200)  # 들
        o.set_motors(positions=[0, 0, 80, -20, 20, 0, 0, 0, -80, 20], movetime=200)  # 흔
        o.set_motors(positions=[0, 0, 80, 20, 20, 0, 0, 0, -80, -20], movetime=200)  # 들
        break


def m_explain():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 60, 0, -10, 0, 0, 0, -60, 0], movetime=200)   # 끄
        o.set_motors(positions=[0, 0, 60, 0,  10, 0, 0, 0, -60, 0], movetime=300)  # 덕
        o.set_motors(positions=[0, 0, 60, 0, -10, 0, 0, 0, -60, 0], movetime=300)  # 끄
        o.set_motors(positions=[0, 0, 60, -20, 0, 0, 0, 0, -60, 20], movetime=200)  # 덕
        o.set_motors(positions=[0, 0, 60, 20, 0, 0, 0, 0, -60, -20], movetime=300)
        o.set_motors(positions=[0, 0, 60, -20, 0, 0, 0, 0, -60, 20], movetime=300)
        o.set_motors(positions=[0, 0, 60, 20, 0, 0, 0, 0, -60, -20], movetime=300)
        break


def m_photo():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 0, 0, 0, 0, 80, 0], movetime=300)
        o.set_motors(positions=[0, 0, -80, -20, 0, 0, 0, 0, 80, 20], movetime=200)
        break


def m_stamp():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 20, 30, 0, 0, 0, 0, 0, 0], movetime=200)
        o.set_motors(positions=[0, 0, -60, 0, 0, 0, 0, 0, 0, 0], movetime=1000)
        o.set_motors(positions=[0, 0, 0, -20, 0, 0, 0, 0, 0, 0], movetime=300)
        o.set_motors(positions=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], movetime=200)
        break


def m_waiting():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 20, 35, 0, 0, 0, 80, -20], movetime=200)  # 도
        o.set_motors(positions=[0, 0, -80, 0, -35, 0, 0, 0, 80, 0], movetime=400)  # 리
        o.set_motors(positions=[0, 0, -80, 20, 35, 0, 0, 0, 80, -20], movetime=400)  # 도
        o.set_motors(positions=[0, 0, -80, 0, -35, 0, 0, 0, 80, 0], movetime=400)  # 리
        o.set_motors(positions=[0, 0, -80, 20, 0, 0, 0, 0, 80, -20], movetime=200)
        break


def m_cheer():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=400)
        o.set_motors(positions=[10, 0, 80, 0, 0, 0, -10, 0, -80, 0], movetime=200)
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=400)
        o.set_motors(positions=[10, 0, 80, 0, 0, 0, -10, 0, -80, 0], movetime=400)
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=400)
        break


def m_compliment():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=400)
        o.set_motors(positions=[10, 0, 80, 20, 0, 0, -10, 0, -80, -20], movetime=200)
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=200)
        o.set_motors(positions=[10, 0, 80, 20, 0, 0, -10, 0, -80, -20], movetime=200)
        o.set_motors(positions=[0, 0, 80, 20, 0, 0, 0, 0, -80, -20], movetime=200)
        break


def m_concil():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -30, 0, 20, 0, 0, 0, 30, 0], movetime=200)
        o.set_motors(positions=[0, 0, -30, 0, -20, 0, 0, 0, 30, 0], movetime=400)
        o.set_motors(positions=[0, 0, -30, 0, 20, 0, 0, 0, 30, 0], movetime=400)
        o.set_motors(positions=[0, 0, -30, 0, -20, 0, 0, 0, 30, 0], movetime=400)
        o.set_motors(positions=[0, 0, 60, 0, -20, 0, 0, 0, -60, 0], movetime=200)
        o.set_motors(positions=[0, 0, -60, 0, -20, 0, 0, 0, 60, 0], movetime=400)
        o.set_motors(positions=[0, 0, 60, 0, -20, 0, 0, 0, -60, 0], movetime=400)
        break


def m_search():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 40, 0, 0, 0, 80, 0], movetime=200)
        o.set_motors(positions=[0, 0, -80, -20, -40, 0, 0, 0, 80, 20], movetime=400)
        o.set_motors(positions=[0, 0, -80, -20, 40, 0, 0, 0, 80, 20], movetime=400)
        o.set_motors(positions=[0, 0, -80, -20, -40, 0, 0, 0, 80, 20], movetime=400)
        o.set_motors(positions=[0, 0, -80, -20, 0, 0, 0, 0, 80, 20], movetime=200)
        break


def m_sleep():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -20, 0, 0, 10, 0, 0, 20, 0], movetime=200)
        o.set_motors(positions=[0, 0, -40, -20, 0, -20, 0, 0, 40, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=500)
        break


def m_wakeup():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 0, -10, 0, 0, 0, 0], movetime=300)
        o.set_motors(positions=[0, 0, 80, 0, 0, 40, 0, 0, 0, 0], movetime=1500)
        o.set_motors(positions=[20, 0, 80, 30, 0, 40, 0, 0, 80, 30], movetime=700)
        break


def m_agree():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 0, 0, 0, 20, 0, 0, 0, 0], movetime=200)
        o.set_motors(positions=[0, 0, -60, 15, 0, -10, 0, 0, 60, -15], movetime=200)
        o.set_motors(positions=[0, 0, -60, 30, 0, 20, 0, 0, 60, -30], movetime=200)
        o.set_motors(positions=[0, 0, -60, 30, 0, 0, 0, 0, 60, -30], movetime=200)
        break


def m_deny():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -40, -15, 0, 0, 0, 0, 40, 15], movetime=400)  
        o.set_motors(positions=[0, 0, -80, -30, 35, 0, 0, 0, 80, 30], movetime=200)  # 도
        o.set_motors(positions=[0, 0, -80, -30, -35, 0, 0, 0, 80, 30], movetime=200)  # 리
        o.set_motors(positions=[0, 0, -80, -30, 35, 0, 0, 0, 80, 30], movetime=200)  # 도
        o.set_motors(positions=[0, 0, -80, -30, -35, 0, 0, 0, 80, 30], movetime=200)  # 리
        break


def m_joy():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=400)
        o.set_motors(positions=[10, 0, 80, 30, 0, 20, -10, 0, -80, -30], movetime=200)
        o.set_motors(positions=[0, 0, 80, 10, 0, 10, 0, 0, -80, -10], movetime=200)
        o.set_motors(positions=[10, 0, 80, 30, 0, 20, -10, 0, -80, -30], movetime=200)
        o.set_motors(positions=[0, 0, 80, 10, 0, 10, 0, 0, -80, -10], movetime=200)
        break


def m_angry():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 0, 0, -50, 0, 0, 0, 0, 0], movetime=500)
        o.set_motors(positions=[0, 0, 0, 0, -50, 0, -20, 0, 0, 0], movetime=200)
        o.set_motors(positions=[0, 0, 0, 0, -50, 0, 0, 0, 0, 0], movetime=200)
        o.set_motors(positions=[0, 0, 0, 0, -50, 0, -20, 0, 0, 0], movetime=200)
        break


def m_sad():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -40, -20, 0, -20, 0, 0, 40, 20], movetime=700)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=400)
        o.set_motors(positions=[0, 0, -80, -20, 20, -20, 0, 0, 80, 20], movetime=200)
        o.set_motors(positions=[0, 0, -80, -20, -20, -20, 0, 0, 80, 20], movetime=400)
        o.set_motors(positions=[0, 0, -80, -20, 20, -20, 0, 0, 80, 20], movetime=400)
        o.set_motors(positions=[0, 0, -80, -20, -20, -20, 0, 0, 80, 20], movetime=400)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=200)
        break


def m_tired():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 10, 10, 0, 10, 0, 0, -10, -10], movetime=300)
        o.set_motors(positions=[0, 0, -60, -20, 0, -20, 0, 0, 60, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -20, 20, -15, 10, 0, 0, 20, -20], movetime=300)
        o.set_motors(positions=[0, 0, -60, -20, 0, -20, 0, 0, 60, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -20, 20, -15, 10, 0, 0, 20, -20], movetime=300)
        break


