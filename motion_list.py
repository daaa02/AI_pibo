import time
from openpibo.motion import Motion

"""
Motor number
0:왼발, 1:왼다리, 2:왼팔, 3:왼손, 4:머리_pan, 5:머리_tilt, 6:오른발, 7:오른다리, 8:오른팔, 9:오른손
0:25,  1:35,    2: 80,  3:30,  4:50,       5:25,       6:25,    7:35,      8:80,     9:30

movetime: 행동 A에서 행동 B로 넘어가는데 걸리는 시간
ex) 행동 A = 1000, 행동 B = 4000 이면, A->B로 모터가 움직이는 시간이 4초;
"""


def m_init():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 0, 0, 0, 0, 80, 0], movetime=500)
        time.sleep(0.6)
        break


def m_question():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -45, 0, 0, 10, 0, 0, 45, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -45, 30, 0, 10, 0, 0, 45, -30], movetime=500)
        time.sleep(0.6)
        break


def m_suggestion():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 0, -80, 5, 0, 0, 0, 0, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 0, 0, 10, 0, 0, 0, 0, 0], movetime=500)  # 흔
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 0, -60, 10, 0, 0, 0, 0, 0], movetime=500)  # 들
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 0, 10, 10, 0, 0, 0, 0, 0], movetime=500)  # 흔
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 0, -60, 10, 0, 0, 0, 0, 0], movetime=500)  # 들
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 0, 0, 0, 10, 0, 0, 0, 20], movetime=1000)
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, 0, 0, 0, 10, 0, 0, 0, -20], movetime=1000)
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, 0, 0, 0, 10, 0, 0, 0, 20], movetime=1000)
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, 0, 0, 0, 10, 0, 0, 0, 0], movetime=1000)
        time.sleep(1.1)
        break


def m_explain():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -45, 0, -10, 0, 0, 0, -60, 0], movetime=500)  # 끄
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -45, 0, 10, 0, 0, 0, -60, 0], movetime=1000)  # 덕
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, -45, 0, -10, 0, 0, 0, -60, 0], movetime=1000)  # 끄
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, -45, -20, 0, 0, 0, 0, -60, 20], movetime=500)  # 덕
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -45, 20, 0, 0, 0, 0, -60, -20], movetime=1000)
        time.sleep(1.1)
        break


def m_photo():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 0, 0, 0, 0, -80, 0], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, -20, 0, 0, 0, 0, -80, 20], movetime=1000)
        time.sleep(1.1)
        break


def m_stamp():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 20, -30, 0, 0, 0, 0, 80, 0], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, -30, 0, 0, 0, 0, 80, 0], movetime=500)
        time.sleep(0.5)
        o.set_motors(positions=[0, 0, 0, -30, 0, 0, 0, 0, 80, 0], movetime=500)
        time.sleep(0.6)
        break


def m_waiting():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 20, 35, 0, 0, 0, 80, -20], movetime=500)  # 도
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -80, 0, -35, 0, 0, 0, 80, 0], movetime=1000)  # 리
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, -80, 20, 35, 0, 0, 0, 80, -20], movetime=500)  # 도
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -80, 0, -35, 0, 0, 0, 80, 0], movetime=1000)  # 리
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, -80, 20, 0, 0, 0, 0, 80, -20], movetime=500)
        time.sleep(0.6)
        break


def m_cheer():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[30, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, -30, 0, -80, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[30, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, -30, 0, -80, 0], movetime=500)
        time.sleep(0.6)
        break


def m_compliment():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[30, 0, 0, 20, 0, 0, 0, 0, 0, -20], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 0, -20, 0, 0, 0, -30, 0, 20], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[30, 0, 0, 20, 0, 0, 0, 0, 0, -20], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 0, -20, 0, 0, 0, -30, 0, 20], movetime=500)
        time.sleep(0.6)
        break


def m_concil():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -45, 0, 10, 0, 0, 0, 30, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -45, 0, -10, 0, 0, 0, 30, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -45, 0, 10, 0, 0, 0, 30, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -45, 0, -10, 0, 0, 0, 30, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 20, 0, 0, 0, 0, 0, -60, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -45, 0, 0, 0, 0, 0, 60, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 20, 0, 0, 0, 0, 0, -60, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -45, 0, 0, 0, 0, 0, 60, 0], movetime=500)
        time.sleep(0.6)
        break


def m_search():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 40, 0, 0, 0, 80, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -80, -20, -40, 0, 0, 0, 80, 20], movetime=2000)
        time.sleep(2.1)
        o.set_motors(positions=[0, 0, -80, -20, 40, 0, 0, 0, 80, 20], movetime=2000)
        time.sleep(2.1)
        o.set_motors(positions=[0, 0, -80, -20, -40, 0, 0, 0, 80, 20], movetime=2000)
        time.sleep(2.1)
        o.set_motors(positions=[0, 0, -80, -20, 0, 0, 0, 0, 80, 20], movetime=1000)
        time.sleep(1.1)
        break


def m_sleep():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 0, 10, 0, 0, 80, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -80, 0, 0, -20, 0, 0, 80, 0], movetime=2000)
        time.sleep(2.1)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=1000)
        time.sleep(1.1)
        break


def m_wakeup():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 0, -10, 0, 0, 80, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[20, 0, 80, 0, 0, 25, 0, 0, -80, 0], movetime=2000)
        time.sleep(2.1)
        o.set_motors(positions=[20, 0, 80, 30, 0, 20, 0, 0, -80, 30], movetime=1000)
        time.sleep(1.1)
        break


def m_agree():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 30, 0, 20, 0, 0, 80, -30], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, 30, 0, -10, 0, 0, 80, -30], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, 30, 0, 20, 0, 0, 80, -30], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, 30, 0, -10, 0, 0, 80, -30], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, 30, 0, 0, 0, 0, 80, -30], movetime=500)
        time.sleep(0.6)
        break


def m_deny():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, -30, 0, 0, 0, 0, 80, 30], movetime=1000)
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, -80, -30, 35, 0, 0, 0, 80, 30], movetime=300)  # 도
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, -30, -35, 0, 0, 0, 80, 30], movetime=300)  # 리
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, -30, 35, 0, 0, 0, 80, 30], movetime=300)  # 도
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, -30, -35, 0, 0, 0, 80, 30], movetime=300)  # 리
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, -30, 0, 0, 0, 0, 80, 30], movetime=300)
        time.sleep(0.4)
        break


def m_joy():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[10, 0, 80, 10, 0, 10, -10, 0, -80, -30], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 80, 30, 0, 0, 0, 0, -80, -10], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[10, 0, 80, 10, 0, 10, -10, 0, -80, -30], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, 80, 30, 0, 0, 0, 0, -80, -10], movetime=500)
        time.sleep(0.6)
        break


def m_angry():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, -50, 0, 0, 0, 80, 0], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -80, 30, -50, 0, -20, 0, 80, -30], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, 30, -50, 0, 0, 0, 80, -30], movetime=300)
        time.sleep(0.4)
        o.set_motors(positions=[0, 0, -80, 30, -50, 0, -20, 0, 80, -30], movetime=300)
        time.sleep(0.4)
        break


def m_sad():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, -30, 0, -20, 0, 0, 80, 30], movetime=1500)
        time.sleep(1.6)
        o.set_motors(positions=[0, 0, -80, -30, 20, -20, 0, 0, 80, 30], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -80, -30, -20, -20, 0, 0, 80, 30], movetime=1000)
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, -80, -30, 20, -20, 0, 0, 80, 30], movetime=1000)
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, -80, -30, -20, -20, 0, 0, 80, 30], movetime=1000)
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, -80, -30, 0, -20, 0, 0, 80, 30], movetime=500)
        time.sleep(0.6)
        break


def m_tired():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 10, 0, 10, 0, 0, 80, -10], movetime=1000)
        time.sleep(1.1)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=1500)
        time.sleep(1.6)
        o.set_motors(positions=[0, 0, -80, 20, -15, 10, 0, 0, 80, -20], movetime=500)
        time.sleep(0.6)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=1500)
        time.sleep(1.6)
        o.set_motors(positions=[0, 0, -80, 20, -15, 10, 0, 0, 80, -20], movetime=500)
        time.sleep(0.6)
        break
