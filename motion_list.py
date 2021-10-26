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
        o.set_motors(positions=[0, 0, 45, 0, 0, 20, 0, 0, -45, 0], movetime=1000)
        o.set_motors(positions=[0, 0, 45, 30, 0, 20, 0, 0, -45, -30], movetime=1000)
        break


def m_suggestion():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 80, 0, 10, 0, 0, 0, -80, 0], movetime=1000)
        o.set_motors(positions=[0, 0, 80, 0, 20, 0, 0, 0, -80, 0], movetime=1000)
        o.set_motors(positions=[0, 0, 80, -20, 20, 0, 0, 0, -80, 20], movetime=500)  # 흔
        o.set_motors(positions=[0, 0, 80, 20, 20, 0, 0, 0, -80, -20], movetime=500)  # 들
        o.set_motors(positions=[0, 0, 80, -20, 20, 0, 0, 0, -80, 20], movetime=500)  # 흔
        o.set_motors(positions=[0, 0, 80, 20, 20, 0, 0, 0, -80, -20], movetime=500)  # 들
        break


def m_explain():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 60, 0, -10, 0, 0, 0, -60, 0], movetime=500)   # 끄
        o.set_motors(positions=[0, 0, 60, 0,  10, 0, 0, 0, -60, 0], movetime=1000)  # 덕
        o.set_motors(positions=[0, 0, 60, 0, -10, 0, 0, 0, -60, 0], movetime=1000)  # 끄
        o.set_motors(positions=[0, 0, 60, -20, 0, 0, 0, 0, -60, 20], movetime=500)  # 덕
        o.set_motors(positions=[0, 0, 60, 20, 0, 0, 0, 0, -60, -20], movetime=500)
        o.set_motors(positions=[0, 0, 60, -20, 0, 0, 0, 0, -60, 20], movetime=500)
        o.set_motors(positions=[0, 0, 60, 20, 0, 0, 0, 0, -60, -20], movetime=500)
        break


def m_photo():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 0, 0, 0, 0, 80, 0], movetime=1000)
        o.set_motors(positions=[0, 0, -80, -20, 0, 0, 0, 0, 80, 20], movetime=1000)
        break


def m_stamp():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 20, 30, 0, 0, 0, 0, 0, 0], movetime=500)
        o.set_motors(positions=[0, 0, -60, 0, 0, 0, 0, 0, 0, 0], movetime=1500)
        o.set_motors(positions=[0, 0, 0, -20, 0, 0, 0, 0, 0, 0], movetime=1000)
        o.set_motors(positions=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], movetime=500)
        break


def m_waiting():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 20, 35, 0, 0, 0, 80, -20], movetime=1000)  # 도
        o.set_motors(positions=[0, 0, -80, 0, -35, 0, 0, 0, 80, 0], movetime=2000)  # 리
        o.set_motors(positions=[0, 0, -80, 20, 35, 0, 0, 0, 80, -20], movetime=2000)  # 도
        o.set_motors(positions=[0, 0, -80, 0, -35, 0, 0, 0, 80, 0], movetime=2000)  # 리
        o.set_motors(positions=[0, 0, -80, 20, 0, 0, 0, 0, 80, -20], movetime=2000)
        break


def m_cheer():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=1000)
        o.set_motors(positions=[10, 0, 80, 0, 0, 0, -10, 0, -80, 0], movetime=500)
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=500)
        o.set_motors(positions=[10, 0, 80, 0, 0, 0, -10, 0, -80, 0], movetime=500)
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=500)
        break


def m_compliment():  # 2,8 80º -> (3,9 30º && 0,6 10º)x2
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=1000)
        o.set_motors(positions=[10, 0, 80, 20, 0, 0, -10, 0, -80, -20], movetime=500)
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=500)
        o.set_motors(positions=[10, 0, 80, 20, 0, 0, -10, 0, -80, -20], movetime=500)
        o.set_motors(positions=[0, 0, 80, 20, 0, 0, 0, 0, -80, -20], movetime=500)
        break


def m_concil():  # 4 20º,-20º -> 2,8 80,-80ºx2
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -30, 0, 20, 0, 0, 0, 30, 0], movetime=500)
        o.set_motors(positions=[0, 0, -30, 0, -20, 0, 0, 0, 30, 0], movetime=1000)
        o.set_motors(positions=[0, 0, -30, 0, 20, 0, 0, 0, 30, 0], movetime=1000)
        o.set_motors(positions=[0, 0, -30, 0, -20, 0, 0, 0, 30, 0], movetime=1000)
        o.set_motors(positions=[0, 0, 60, 0, -20, 0, 0, 0, -60, 0], movetime=500)
        o.set_motors(positions=[0, 0, -60, 0, -20, 0, 0, 0, 60, 0], movetime=1000)
        o.set_motors(positions=[0, 0, 60, 0, -20, 0, 0, 0, -60, 0], movetime=1000)
        break


def m_search():  # 4 20º,-20ºx2 && 2,8 60, 0º
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 40, 0, 0, 0, 80, 0], movetime=500)
        o.set_motors(positions=[0, 0, -80, -20, -40, 0, 0, 0, 80, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -80, -20, 40, 0, 0, 0, 80, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -80, -20, -40, 0, 0, 0, 80, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -80, -20, 0, 0, 0, 0, 80, 20], movetime=500)
        break


def m_sleep():  # 5 20->-10º -> 2,8 0º
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -20, 0, 0, 10, 0, 0, 20, 0], movetime=500)
        o.set_motors(positions=[0, 0, -40, -20, 0, -20, 0, 0, 40, 20], movetime=2000)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=2000)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=2500)
        break


def m_wakeup():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -80, 0, 0, -10, 0, 0, 0, 0], movetime=500)
        o.set_motors(positions=[0, 0, 80, 0, 0, 40, 0, 0, 0, 0], movetime=3000)
        o.set_motors(positions=[20, 0, 80, 30, 0, 40, 0, 0, 80, 30], movetime=1000)
        break


def m_agree():
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 0, 0, 0, 20, 0, 0, 0, 0], movetime=500)
        o.set_motors(positions=[0, 0, -60, 15, 0, -10, 0, 0, 60, -15], movetime=500)
        o.set_motors(positions=[0, 0, -60, 30, 0, 20, 0, 0, 60, -30], movetime=500)
        o.set_motors(positions=[0, 0, -60, 30, 0, 0, 0, 0, 60, -30], movetime=500)
        break


def m_deny():  # 3,9 0º -> 4 20ºx2
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -40, -15, 0, 0, 0, 0, 40, 15], movetime=1000)  # 도
        o.set_motors(positions=[0, 0, -80, -30, 35, 0, 0, 0, 80, 30], movetime=1000)  # 도
        o.set_motors(positions=[0, 0, -80, -30, -35, 0, 0, 0, 80, 30], movetime=500)  # 리
        o.set_motors(positions=[0, 0, -80, -30, 35, 0, 0, 0, 80, 30], movetime=500)  # 도
        o.set_motors(positions=[0, 0, -80, -30, -35, 0, 0, 0, 80, 30], movetime=500)  # 리
        break


def m_joy():  # 2,8 80º -> 3,9 30º && 0,6 10º
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 80, 0, 0, 0, 0, 0, -80, 0], movetime=1000)
        o.set_motors(positions=[10, 0, 80, 30, 0, 20, -10, 0, -80, -30], movetime=500)
        o.set_motors(positions=[0, 0, 80, 10, 0, 10, 0, 0, -80, -10], movetime=500)
        o.set_motors(positions=[10, 0, 80, 30, 0, 20, -10, 0, -80, -30], movetime=500)
        o.set_motors(positions=[0, 0, 80, 10, 0, 10, 0, 0, -80, -10], movetime=500)
        break


def m_angry():  # 4 -50º -> 6 10º
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 0, 0, -50, 0, 0, 0, 0, 0], movetime=1000)
        o.set_motors(positions=[0, 0, 0, 0, -50, 0, -20, 0, 0, 0], movetime=200)
        o.set_motors(positions=[0, 0, 0, 0, -50, 0, 0, 0, 0, 0], movetime=200)
        o.set_motors(positions=[0, 0, 0, 0, -50, 0, -20, 0, 0, 0], movetime=200)
        break


def m_sad():  # 4 -30,30º && 5 -10º && 3,9 0º
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, -40, -20, 0, -20, 0, 0, 40, 20], movetime=1500)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -80, -20, 20, -20, 0, 0, 80, 20], movetime=500)
        o.set_motors(positions=[0, 0, -80, -20, -20, -20, 0, 0, 80, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -80, -20, 20, -20, 0, 0, 80, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -80, -20, -20, -20, 0, 0, 80, 20], movetime=1000)
        o.set_motors(positions=[0, 0, -80, -20, 0, -20, 0, 0, 80, 20], movetime=500)
        break


def m_tired():  # (5 -10,20º && 3,9 20,0º)x2
    o = Motion()
    while True:
        o.set_motors(positions=[0, 0, 10, 10, 0, 10, 0, 0, -10, -10], movetime=500)
        o.set_motors(positions=[0, 0, -60, -20, 0, -20, 0, 0, 60, 20], movetime=2000)
        o.set_motors(positions=[0, 0, -20, 20, -15, 10, 0, 0, 20, -20], movetime=500)
        o.set_motors(positions=[0, 0, -60, -20, 0, -20, 0, 0, 60, 20], movetime=2000)
        o.set_motors(positions=[0, 0, -20, 20, -15, 10, 0, 0, 20, -20], movetime=500)
        break


