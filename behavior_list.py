import time
from threading import Thread

import openpibo
from openpibo.motion import Motion
from openpibo.device import Device
from openpibo.speech import Speech
from openpibo.audio import Audio

import motion_list
import eye_list

audio = Audio()


def do_question():
    # audio.play('/home/pi/openpibo/question.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_question()
    m = Thread(target=motion_list.m_question(), args=())

    m.daemon = True
    m.start()


def do_suggestion():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_suggestion()
    m = Thread(target=motion_list.m_suggestion(), args=())

    m.daemon = True
    m.start()


def do_explain():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_explain()
    m = Thread(target=motion_list.m_explain(), args=())

    m.daemon = True
    m.start()


def do_photo():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_photo()
    m = Thread(target=motion_list.m_photo(), args=())

    m.daemon = True
    m.start()


def do_stamp():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_stamp()
    m = Thread(target=motion_list.m_stamp(), args=())

    m.daemon = True
    m.start()


def do_waiting():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_waiting()
    m = Thread(target=motion_list.m_waiting(), args=())

    m.daemon = True
    m.start()


def do_cheer():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_cheer()
    m = Thread(target=motion_list.m_cheer(), args=())

    m.daemon = True
    m.start()


def do_compliment():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_compliment()
    m = Thread(target=motion_list.m_compliment(), args=())

    m.daemon = True
    m.start()


def do_concil():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_concil()
    m = Thread(target=motion_list.m_concil(), args=())

    m.daemon = True
    m.start()


def do_search():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_search()
    m = Thread(target=motion_list.m_search(), args=())

    m.daemon = True
    m.start()


def do_sleep():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_sleep(),
    m = Thread(target=motion_list.m_sleep(), args=())

    m.daemon = True
    m.start()


def do_wakeup():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_wakeup()
    m = Thread(target=motion_list.m_wakeup(), args=())

    m.daemon = True
    m.start()


def do_agree():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_agree()
    m = Thread(target=motion_list.m_agree(), args=())

    m.daemon = True
    m.start()


def do_deny():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_deny()
    m = Thread(target=motion_list.m_deny(), args=())

    m.daemon = True
    m.start()


def do_joy():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_joy()
    m = Thread(target=motion_list.m_joy(), args=())

    m.daemon = True
    m.start()


def do_angry():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_angry()
    m = Thread(target=motion_list.m_angry(), args=())

    m.daemon = True
    m.start()


def do_sad():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_sad()
    m = Thread(target=motion_list.m_sad(), args=())

    m.daemon = True
    m.start()


def do_tired():
    # audio.play('/home/pi/openpibo/~.mp3', out='local', volume=-2000, background=False)
    # eye_list.e_tired()
    m = Thread(target=motion_list.m_sad(), args=())

    m.daemon = True
    m.start()
